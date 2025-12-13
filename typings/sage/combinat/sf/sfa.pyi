from _typeshed import Incomplete
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.functor import Functor as Functor
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.hopf_algebras_with_basis import HopfAlgebrasWithBasis as HopfAlgebrasWithBasis
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent
from sage.categories.tensor import tensor as tensor
from sage.categories.unique_factorization_domains import UniqueFactorizationDomains as UniqueFactorizationDomains
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.partition import Partition as Partition, Partitions as Partitions, Partitions_n as Partitions_n
from sage.data_structures.blas_dict import convert_remove_zeroes as convert_remove_zeroes, linear_combination as linear_combination
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import coerce_binop as coerce_binop
from sage.structure.factorization import Factorization as Factorization

def is_SymmetricFunctionAlgebra(x):
    """
    Check whether ``x`` is a symmetric function algebra.

    EXAMPLES::

        sage: from sage.combinat.sf.sfa import is_SymmetricFunctionAlgebra
        sage: is_SymmetricFunctionAlgebra(5)
        doctest:warning...
        DeprecationWarning: the function is_SymmetricFunctionAlgebra is deprecated;
        use 'isinstance(..., SymmetricFunctionAlgebra_generic)' instead
        See https://github.com/sagemath/sage/issues/37896 for details.
        False
        sage: is_SymmetricFunctionAlgebra(ZZ)
        False
        sage: is_SymmetricFunctionAlgebra(SymmetricFunctions(ZZ).schur())
        True
        sage: is_SymmetricFunctionAlgebra(SymmetricFunctions(QQ).e())
        True
        sage: is_SymmetricFunctionAlgebra(SymmetricFunctions(QQ).macdonald(q=1,t=1).P())
        True
        sage: is_SymmetricFunctionAlgebra(SymmetricFunctions(FractionField(QQ['q','t'])).macdonald().P())
        True
    """
def zee(part) -> Integer:
    """
    Return the size of the centralizer of any permutation of cycle type
    ``part``.

    Note that the size of the centralizer is the inner product between
    ``p(part)`` and itself, where `p` is the power-sum symmetric
    functions.

    INPUT:

    - ``part`` -- integer partition (for example, ``[2,1,1]``)

    OUTPUT:

    - the integer `\\prod_{i} i^{m_i(part)} m_i(part)!` where `m_i(part)` is
      the number of parts in the partition ``part`` equal to `i`

    EXAMPLES::

        sage: from sage.combinat.sf.sfa import zee
        sage: zee([2,1,1])
        4
    """
def is_SymmetricFunction(x):
    """
    Check whether ``x`` is a symmetric function.

    EXAMPLES::

        sage: from sage.combinat.sf.sfa import is_SymmetricFunction
        sage: s = SymmetricFunctions(QQ).s()
        sage: is_SymmetricFunction(2)
        doctest:warning...
        DeprecationWarning: The function is_SymmetricFunction is deprecated;
        use 'isinstance(..., SymmetricFunctionAlgebra_generic.Element)' instead.
        See https://github.com/sagemath/sage/issues/38279 for details.
        False
        sage: is_SymmetricFunction(s(2))
        True
        sage: is_SymmetricFunction(s([2,1]))
        True
    """

class SymmetricFunctionsBases(Category_realization_of_parent):
    """
    The category of bases of the ring of symmetric functions.

    INPUT:

    - ``self`` -- a category of bases for the symmetric functions
    - ``base`` -- ring of symmetric functions

    TESTS::

        sage: from sage.combinat.sf.sfa import SymmetricFunctionsBases
        sage: Sym = SymmetricFunctions(QQ)
        sage: bases = SymmetricFunctionsBases(Sym); bases
        Category of bases of Symmetric Functions over Rational Field
        sage: Sym.schur() in bases
        True
    """
    def super_categories(self) -> list:
        '''
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import SymmetricFunctionsBases
            sage: Sym = SymmetricFunctions(QQ)
            sage: bases = SymmetricFunctionsBases(Sym)
            sage: bases.super_categories()
            [Category of realizations of Symmetric Functions over Rational Field,
             Category of commutative Hopf algebras with basis over Rational Field,
             Join of Category of realizations of Hopf algebras over Rational Field
                 and Category of graded algebras over Rational Field
                 and Category of graded coalgebras over Rational Field,
             Category of unique factorization domains]

            sage: Sym = SymmetricFunctions(ZZ["x"])
            sage: bases = SymmetricFunctionsBases(Sym)
            sage: bases.super_categories()
            [Category of realizations of Symmetric Functions over Univariate Polynomial Ring in x over Integer Ring,
             Category of commutative Hopf algebras with basis over Univariate Polynomial Ring in x over Integer Ring,
             Join of Category of realizations of Hopf algebras over Univariate Polynomial Ring in x over Integer Ring
                 and Category of graded algebras over Univariate Polynomial Ring in x over Integer Ring
                 and Category of graded coalgebras over Univariate Polynomial Ring in x over Integer Ring]
        '''
    class ParentMethods:
        def is_integral_domain(self, proof: bool = True) -> bool:
            """
            Return whether ``self`` is an integral domain. (It is if
            and only if the base ring is an integral domain.)

            INPUT:

            - ``self`` -- a basis of the symmetric functions
            - ``proof`` -- an optional argument (default: value: ``True``)

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: s.is_integral_domain()
                True

                sage: s = SymmetricFunctions(Zmod(14)).s()
                sage: s.is_integral_domain()
                False
            """
        @cached_method
        def fraction_field(self):
            """
            Return the fraction field of ``self``.

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: s.fraction_field()
                Fraction Field of Symmetric Functions over Rational Field in the Schur basis
            """
        def is_field(self, proof: bool = True) -> bool:
            """
            Return whether ``self`` is a field. (It is not.)

            INPUT:

            - ``self`` -- a basis of the symmetric functions
            - ``proof`` -- an optional argument (default: value: ``True``)

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: s.is_field()
                False
            """
        def is_commutative(self) -> bool:
            """
            Return whether this symmetric function algebra is commutative.

            INPUT:

            - ``self`` -- a basis of the symmetric functions

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: s.is_commutative()
                True
            """
        @cached_method
        def one_basis(self):
            """
            Return the empty partition, as per ``AlgebrasWithBasis.ParentMethods.one_basis``.

            INPUT:

            - ``self`` -- a basis of the ring of symmetric functions

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
                sage: s = Sym.s()
                sage: s.one_basis()
                []
                sage: Q = Sym.hall_littlewood().Q()
                sage: Q.one_basis()
                []

            .. TODO:: generalize to Modules.Graded.Connected.ParentMethods
            """
        def degree_on_basis(self, b):
            """
            Return the degree of the basis element indexed by ``b``.

            INPUT:

            - ``self`` -- a basis of the symmetric functions
            - ``b`` -- a partition

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ['q,t'].fraction_field())
                sage: m = Sym.monomial()
                sage: m.degree_on_basis(Partition([3,2]))
                5
                sage: P = Sym.macdonald().P()
                sage: P.degree_on_basis(Partition([]))
                0
            """
        def corresponding_basis_over(self, R):
            """
            Return the realization of symmetric functions corresponding to
            ``self`` but over the base ring ``R``. Only works when ``self``
            is one of the classical bases, not one of the `q,t`-dependent
            ones. In the latter case, ``None`` is returned instead.

            INPUT:

            - ``R`` -- a commutative ring

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: m = Sym.monomial()
                sage: m.corresponding_basis_over(ZZ)
                doctest:warning
                ...
                DeprecationWarning: S.corresponding_basis_over(R) is deprecated.
                Use S.change_ring(R) instead.
                See https://github.com/sagemath/sage/issues/37220 for details.
                Symmetric Functions over Integer Ring in the monomial basis

                sage: Sym = SymmetricFunctions(CyclotomicField())
                sage: s = Sym.schur()
                sage: s.corresponding_basis_over(Integers(13))
                Symmetric Functions over Ring of integers modulo 13 in the Schur basis

                sage: P = ZZ['q','t']
                sage: Sym = SymmetricFunctions(P)
                sage: mj = Sym.macdonald().J()
                sage: mj.corresponding_basis_over(Integers(13)['q','t'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over
                 Ring of integers modulo 13 in the Macdonald J basis

            TESTS:

            Let's check that this handles each of the bases properly::

                sage: P = QQ['q','t']
                sage: Sym = SymmetricFunctions(P)
                sage: Q = CyclotomicField()['q','t']
                sage: Sym.s().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the Schur basis
                sage: Sym.p().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the powersum basis
                sage: Sym.m().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the monomial basis
                sage: Sym.e().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the elementary basis
                sage: Sym.h().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the homogeneous basis
                sage: Sym.f().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the forgotten basis
                sage: Sym.w().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the Witt basis
                sage: Sym.macdonald().P().change_ring(CyclotomicField()['q', 't'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over Universal Cyclotomic Field in the Macdonald P basis
                sage: Sym.macdonald().Q().change_ring(CyclotomicField()['q', 't'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over Universal Cyclotomic Field in the Macdonald Q basis
                sage: Sym.macdonald().J().change_ring(CyclotomicField()['q', 't'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over Universal Cyclotomic Field in the Macdonald J basis
                sage: Sym.macdonald().H().change_ring(CyclotomicField()['q', 't'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over Universal Cyclotomic Field in the Macdonald H basis
                sage: Sym.macdonald().Ht().change_ring(CyclotomicField()['q', 't'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over Universal Cyclotomic Field in the Macdonald Ht basis
                sage: Sym.macdonald().S().change_ring(CyclotomicField()['q', 't'])
                Symmetric Functions over Multivariate Polynomial Ring in q, t over Universal Cyclotomic Field in the Macdonald S basis
                sage: Sym.macdonald(q=1).S().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Macdonald S with q=1 basis
                sage: Sym.macdonald(q=1,t=3).P().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the Macdonald P with q=1 and t=3 basis
                sage: Sym.hall_littlewood().P().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Hall-Littlewood P basis
                sage: Sym.hall_littlewood().Q().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Hall-Littlewood Q basis
                sage: Sym.hall_littlewood().Qp().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Hall-Littlewood Qp basis
                sage: Sym.hall_littlewood(t=1).P().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the Hall-Littlewood P with t=1 basis
                sage: Sym.jack().J().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Jack J basis
                sage: Sym.jack().P().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Jack P basis
                sage: Sym.jack().Q().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Jack Q basis
                sage: Sym.jack().Qp().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the Jack Qp basis
                sage: Sym.jack(t=1).J().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the Jack J with t=1 basis
                sage: Sym.zonal().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the zonal basis
                sage: Sym.llt(3).hspin().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the level 3 LLT spin basis
                sage: Sym.llt(3).hcospin().change_ring(CyclotomicField()['t'])
                Symmetric Functions over Univariate Polynomial Ring in t over Universal Cyclotomic Field in the level 3 LLT cospin basis
                sage: Sym.llt(3, t=1).hspin().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the level 3 LLT spin with t=1 basis
                sage: Sym.llt(3, t=1).hcospin().change_ring(CyclotomicField())
                Symmetric Functions over Universal Cyclotomic Field in the level 3 LLT cospin with t=1 basis

            .. TODO::

                This function is an ugly hack using strings. It should be
                rewritten as soon as the bases of ``SymmetricFunctions`` are
                put on a more robust and systematic footing.
            """
        def skew_schur(self, x):
            """
            Return the skew Schur function indexed by ``x`` in ``self``.

            INPUT:

            - ``x`` -- a skew partition

            EXAMPLES::

                sage: sp = SkewPartition([[5,3,3,1], [3,2,1]])
                sage: s = SymmetricFunctions(QQ).s()
                sage: s.skew_schur(sp)
                s[2, 2, 1, 1] + s[2, 2, 2] + s[3, 1, 1, 1] + 3*s[3, 2, 1]
                 + s[3, 3] + 2*s[4, 1, 1] + 2*s[4, 2] + s[5, 1]

                sage: e = SymmetricFunctions(QQ).e()
                sage: ess = e.skew_schur(sp); ess
                e[2, 1, 1, 1, 1] - e[2, 2, 1, 1] - e[3, 1, 1, 1] + e[3, 2, 1]
                sage: ess == e(s.skew_schur(sp))
                True

            TESTS::

                sage: s.skew_schur([[2,1], [1]])
                s[1, 1] + s[2]

                sage: s.skew_schur([[2,1], [3]])
                Traceback (most recent call last):
                ...
                ValueError: not a valid skew partition

                sage: s = SymmetricFunctions(GF(2)).s()
                sage: s.skew_schur([[3,2,1],[2,1]])
                s[1, 1, 1] + s[3]
            """
        def Eulerian(self, n, j, k=None):
            """
            Return the Eulerian symmetric function `Q_{n,j}` (with `n`
            either an integer or a partition) or `Q_{n,j,k}` (if the
            optional argument ``k`` is specified) in terms of the basis
            ``self``.

            It is known that the Eulerian quasisymmetric functions are
            in fact symmetric functions [SW2010]_. For more information,
            see :meth:`QuasiSymmetricFunctions.Fundamental.Eulerian()`,
            which accepts the same syntax as this method.

            INPUT:

            - ``n`` -- the nonnegative integer `n` or a partition
            - ``j`` -- the number of excedances
            - ``k`` -- (optional) if specified, determines the number of fixed
              points of the permutations which are being summed over

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: m = Sym.m()
                sage: m.Eulerian(3, 1)
                4*m[1, 1, 1] + 3*m[2, 1] + 2*m[3]
                sage: h = Sym.h()
                sage: h.Eulerian(4, 2)
                h[2, 2] + h[3, 1] + h[4]
                sage: s = Sym.s()
                sage: s.Eulerian(5, 2)
                s[2, 2, 1] + s[3, 1, 1] + 5*s[3, 2] + 6*s[4, 1] + 6*s[5]
                sage: s.Eulerian([2,2,1], 2)
                s[2, 2, 1] + s[3, 2] + s[4, 1] + s[5]
                sage: s.Eulerian(5, 2, 2)
                s[3, 2] + s[4, 1] + s[5]

            We check Equation (5.4) in [SW2010]_::

                sage: h.Eulerian([6], 3)
                h[3, 2, 1] - h[4, 1, 1] + 2*h[4, 2] + h[5, 1]
                sage: s.Eulerian([6], 3)
                s[3, 2, 1] + s[3, 3] + 3*s[4, 2] + 3*s[5, 1] + 3*s[6]
            """
        def gessel_reutenauer(self, lam):
            '''
            Return the Gessel-Reutenauer symmetric function
            corresponding to the partition ``lam`` written in the basis
            ``self``.

            Let `\\lambda` be a partition. The *Gessel-Reutenauer
            symmetric function* `\\mathbf{GR}_\\lambda` corresponding to
            `\\lambda` is the symmetric function denoted `L_\\lambda` in
            [GR1993]_ and in Exercise 7.89 of [STA]_ and denoted
            `\\mathbf{GR}_\\lambda` in Definition 6.6.34 of [GriRei18]_.
            It is also called the *higher Lie character*, for instance
            in [Sch2003b]_.
            It can be defined in several ways:

            - It is the sum of the monomials `\\mathbf{x}_w` over all
              words `w` over the alphabet
              `\\left\\{ 1, 2, 3, \\ldots \\right\\}` which have CFL type
              `\\lambda`. Here, the monomial `\\mathbf{x}_w` for a word
              `w = \\left(w_1, w_2, \\ldots, w_k\\right)` is defined as
              `x_{w_1} x_{w_2} \\cdots x_{w_k}`, and the *CFL type* of
              a word `w` is defined as the partition obtained by
              sorting (in decreasing order) the lengths of the factors
              in the Lyndon factorization
              (:meth:`~sage.combinat.words.finite_word.FiniteWord_class.lyndon_factorization`)
              of `w`. The fact that this power series
              `\\mathbf{GR}_\\lambda` is symmetric is not obvious.

            - It is the sum of the fundamental quasisymmetric
              functions `F_{\\operatorname{Des} \\sigma}` over all
              permutations `\\sigma` that have cycle type `\\lambda`. See
              :class:`sage.combinat.ncsf_qsym.qsym.QuasiSymmetricFunctions.Fundamental`
              for the definition of fundamental quasisymmetric functions,
              and :meth:`~sage.combinat.permutation.Permutation.cycle_type`
              for that of cycle type. For a permutation `\\sigma`, we use
              `\\operatorname{Des} \\sigma` to denote the descent composition
              (:meth:`~sage.combinat.permutation.Permutation.descents_composition`)
              of `\\sigma`. Again, this definition does not make the
              symmetry of `\\mathbf{GR}_\\lambda` obvious.

            - For every positive integer `n`, we have

              .. MATH::

                  \\mathbf{GR}_{\\left(n\\right)}
                  = \\frac{1}{n} \\sum_{d \\mid n} \\mu(d) p_d^{n/d},

              where `p_d` denotes the `d`-th power-sum symmetric
              function. This `\\mathbf{GR}_{\\left(n\\right)}` is also
              denoted by `L_n`, and is called the Lie character. Now,
              the higher Lie character `\\mathbf{GR}_\\lambda` is defined as the product:

              .. MATH::

                  h_{m_1} \\left[L_1\\right] \\cdot h_{m_2} \\left[L_2\\right]
                  \\cdot h_{m_3} \\left[L_3\\right] \\cdots,

              where `m_i` denotes the multiplicity of the part `i` in
              `\\lambda`, and where the square brackets stand for
              plethysm (:meth:`plethysm`). This definition makes
              the symmetry (but not the integrality!) of
              `\\mathbf{GR}_\\lambda` obvious.

            The equivalences of these three definitions are proven in
            [GR1993]_ Sections 2-3. (See also [GriRei18]_ Subsection
            6.6.2 for the equivalence of the first two definitions and
            further formulas.)

            `\\mathbf{GR}_\\lambda` has further significance in representations afforded
            by the tensor algebra `T(V)` of a finite dimensional vector space.
            The Poincaré-Birkhoff-Witt theorem describes the universal enveloping algebra
            of a Lie algebra. It gives a decomposition of the degree-`n` component `T_n(V)`
            of `T(V)` into `GL(V)` representations indexed by partitions.
            The higher Lie characters are the symmetric group `S_n` characters corresponding
            to this decomposition via Schur-Weyl duality.

            Another important question, *Thrall\'s problem* (see e.g. [Sch2003b]_)
            asks, for `\\lambda` a partition of `n`, can we combinatorially interpret
            the coefficients `\\alpha_\\mu^\\lambda` in the Schur-expansion of
            `\\mathbf{GR}_\\lambda`:

            .. MATH::

                \\mathbf{GR}_\\lambda = \\sum_{\\mu \\vdash n} \\alpha_\\mu^\\lambda s_\\mu.

            INPUT:

            - ``lam`` -- a partition or a positive integer (in the latter
              case, it is understood to mean the partition ``[lam]``)

            OUTPUT:

            The Gessel-Reutenauer symmetric function
            `\\mathbf{GR}_\\lambda`, where `\\lambda` is ``lam``,
            expanded in the basis ``self``.

            EXAMPLES:

            The first few values of `\\mathbf{GR}_{(n)} = L_n`::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: h = Sym.h()
                sage: h.gessel_reutenauer(1)
                h[1]
                sage: h.gessel_reutenauer(2)
                h[1, 1] - h[2]
                sage: h.gessel_reutenauer(3)
                h[2, 1] - h[3]
                sage: h.gessel_reutenauer(4)
                h[2, 1, 1] - h[2, 2]
                sage: h.gessel_reutenauer(5)
                h[2, 1, 1, 1] - h[2, 2, 1] - h[3, 1, 1] + h[3, 2] + h[4, 1] - h[5]
                sage: h.gessel_reutenauer(6)
                h[2, 1, 1, 1, 1] - h[2, 2, 1, 1] - h[2, 2, 2]
                 - 2*h[3, 1, 1, 1] + 5*h[3, 2, 1] - 2*h[3, 3] + h[4, 1, 1]
                 - h[4, 2] - h[5, 1] + h[6]

            Gessel-Reutenauer functions indexed by partitions::

                sage: h.gessel_reutenauer([2, 1])
                h[1, 1, 1] - h[2, 1]
                sage: h.gessel_reutenauer([2, 2])
                h[1, 1, 1, 1] - 3*h[2, 1, 1] + 2*h[2, 2] + h[3, 1] - h[4]

            The Gessel-Reutenauer functions are Schur-positive::

                sage: s = Sym.s()
                sage: s.gessel_reutenauer([2, 1])
                s[1, 1, 1] + s[2, 1]
                sage: s.gessel_reutenauer([2, 2, 1])
                s[1, 1, 1, 1, 1] + s[2, 1, 1, 1] + s[2, 2, 1] + s[3, 2]

            They do not form a basis, as the following example (from
            [GR1993]_ p. 201) shows::

                sage: s.gessel_reutenauer([4]) == s.gessel_reutenauer([2, 1, 1])
                True

            They also go by the name *higher Lie character*::

                sage: s.higher_lie_character([2, 2, 1]) == s.gessel_reutenauer([2, 2, 1])
                True

            Of the above three equivalent definitions of
            `\\mathbf{GR}_\\lambda`, we use the third one for
            computations. Let us check that the second one gives the
            same results::

                sage: QSym = QuasiSymmetricFunctions(ZZ)
                sage: F = QSym.F() # fundamental basis
                sage: def GR_def2(lam): # `\\mathbf{GR}_\\lambda`
                ....:     n = lam.size()
                ....:     r = F.sum_of_monomials([sigma.descents_composition()
                ....:                             for sigma in Permutations(n)
                ....:                             if sigma.cycle_type() == lam])
                ....:     return r.to_symmetric_function()
                sage: all( GR_def2(lam) == h.gessel_reutenauer(lam)
                ....:      for n in range(5) for lam in Partitions(n) )
                True

            And the first one, too (assuming symmetry)::

                sage: m = Sym.m()
                sage: def GR_def1(lam): # `\\mathbf{GR}_\\lambda`
                ....:     n = lam.size()
                ....:     Permus_mset = sage.combinat.permutation.Permutations_mset
                ....:     def coeff_of_m_mu_in_result(mu):
                ....:         words_to_check = Permus_mset([i for i, l in enumerate(mu)
                ....:                                       for _ in range(l)])
                ....:         return sum((1 for w in words_to_check if
                ....:                     Partition(list(reversed(sorted([len(v) for v in Word(w).lyndon_factorization()]))))
                ....:                     == lam))
                ....:     r = m.sum_of_terms([(mu, coeff_of_m_mu_in_result(mu))
                ....:                         for mu in Partitions(n)],
                ....:                        distinct=True)
                ....:     return r
                sage: all( GR_def1(lam) == h.gessel_reutenauer(lam)
                ....:      for n in range(5) for lam in Partitions(n) )
                True

            TESTS:

            This works fine over other base rings::

                sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
                sage: P = Sym.macdonald().P()
                sage: h = Sym.h()
                sage: P.gessel_reutenauer(3) == P(h.gessel_reutenauer(3))
                True

            .. NOTE::

                The currently existing implementation of this function is
                technically unsatisfactory. It distinguishes the case when the
                base ring is a `\\QQ`-algebra from the case
                where it isn\'t. In the latter, it does a computation using
                universal coefficients, again distinguishing the case when it is
                able to compute the "corresponding" basis of the symmetric function
                algebra over `\\QQ` (using the ``corresponding_basis_over`` hack)
                from the case when it isn\'t (in which case it transforms everything
                into the Schur basis, which is slow).
            '''
        higher_lie_character = gessel_reutenauer
        def lehrer_solomon(self, lam):
            """
            Return the Lehrer-Solomon symmetric function (also known as the
            Whitney homology character) corresponding to the partition ``lam``
            written in the basis ``self``.

            Let `\\lambda \\vdash n` be a partition. The *Lehrer-Solomon
            symmetric function* `\\mathbf{LS}_\\lambda` corresponding to
            `\\lambda` is the Frobenius characteristic of the representation
            denoted `\\operatorname{Ind}_{Z_\\lambda}^{S_n}(\\xi_\\lambda)` in
            Theorem 4.5 of [LS1986]_ or `W_\\lambda` in Theorem 2.7 of
            [HR2017]_. It was first computed as a symmetric function in
            [Sun1994]_.

            It is the symmetric group representation corresponding to a
            summand of the Whitney homology of the set partition lattice.
            The summand comes from the orbit of set partitions with block
            sizes corresponding to `\\lambda` (after reordering appropriately).

            It can be computed using Sundaram's plethystic formula
            (see [Sun1994]_ Theorem 1.8):

            .. MATH::

                  \\mathbf{LS}_\\lambda =
                    \\prod_{\\text{odd } j \\geq 1} h_{m_j}[\\pi_j]
                    \\prod_{\\text{even } j \\geq 2} e_{m_j}[\\pi_j],

            where `h_{m_j}` are complete homogeneous symmetric functions,
            `e_{m_j}` are elementary symmetric functions, and `\\pi_j` are
            the images of the Gessel-Reutenauer symmetric function
            `\\mathbf{GR}_{(j)}` (see :meth:`gessel_reutenauer`) under the
            involution `\\omega` (i.e. :meth:`omega_involution`)::

                sage: Sym = SymmetricFunctions(QQ)
                sage: s = Sym.s()
                sage: pi_2 = (s.gessel_reutenauer(2)).omega_involution()
                sage: pi_1 = (s.gessel_reutenauer(1)).omega_involution()
                sage: s.lehrer_solomon([2,1]) == pi_2 * pi_1 # since h_1, e_1 are plethystic identities
                True

            Note that this also gives the `S_n`-equivariant structure of the
            Orlik-Solomon algebra of the braid arrangement (also known as the
            type-`A` reflection arrangement).

            The representation corresponding to `\\mathbf{LS}_\\lambda` exhibits
            representation stability [Chu2012]_, and a sharp bound is given
            in [HR2017]_.

            INPUT:

            - ``lam`` -- a partition or a positive integer (in the latter
              case, it is understood to mean the partition ``[lam]``)

            OUTPUT:

            The Lehrer-Solomon symmetric function
            `\\mathbf{LS}_\\lambda`, where `\\lambda` is ``lam``,
            expanded in the basis ``self``.

            EXAMPLES:

            The first few values of `\\mathbf{LS}_{(n)}`::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: h = Sym.h()
                sage: h.lehrer_solomon(1)
                h[1]
                sage: h.lehrer_solomon(2)
                h[2]
                sage: h.lehrer_solomon(3)
                h[2, 1] - h[3]
                sage: h.lehrer_solomon(4)
                h[2, 1, 1] - h[2, 2]
                sage: h.lehrer_solomon(5)
                h[2, 1, 1, 1] - h[2, 2, 1] - h[3, 1, 1] + h[3, 2] + h[4, 1] - h[5]

            The :meth:`whitney_homology_character` method is an alias::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: s = Sym.schur()
                sage: s.lehrer_solomon([2, 2, 1]) == s.whitney_homology_character([2, 2, 1])
                True

            Lehrer-Solomon functions indexed by partitions::

                sage: h.lehrer_solomon([2, 1])
                h[2, 1]
                sage: h.lehrer_solomon([2, 2])
                h[3, 1] - h[4]

            The Lehrer-Solomon functions are Schur-positive::

                sage: s = Sym.s()
                sage: s.lehrer_solomon([2, 1])
                s[2, 1] + s[3]
                sage: s.lehrer_solomon([2, 2, 1])
                s[3, 1, 1] + s[3, 2] + s[4, 1]
                sage: s.lehrer_solomon([4, 1])
                s[2, 1, 1, 1] + s[2, 2, 1] + 2*s[3, 1, 1] + s[3, 2] + s[4, 1]

            TESTS:

            This works fine over other base rings::

                sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
                sage: P = Sym.macdonald().P()
                sage: h = Sym.h()
                sage: P.lehrer_solomon(3) == P(h.lehrer_solomon(3))
                True

                sage: s = SymmetricFunctions(GF(2)).s()
                sage: s.lehrer_solomon([4,1])
                s[2, 1, 1, 1] + s[2, 2, 1] + s[3, 2] + s[4, 1]
            """
        whitney_homology_character = lehrer_solomon
        def carlitz_shareshian_wachs(self, n, d, s, comparison=None):
            """
            Return the Carlitz-Shareshian-Wachs symmetric function
            `X_{n, d, s}` (if ``comparison`` is ``None``), or
            `U_{n, d, s}` (if ``comparison`` is ``-1``), or
            `V_{n, d, s}` (if ``comparison`` is ``0``), or
            `W_{n, d, s}` (if ``comparison`` is ``1``) written in the
            basis ``self``. These functions are defined below.

            The Carlitz-Shareshian-Wachs symmetric functions have been
            introduced in [GriRei18]_, Exercise 2.9.11, as
            refinements of a certain particular case of chromatic
            quasisymmetric functions defined by Shareshian and Wachs.
            Their definitions are as follows:

            Let `n`, `d` and `s` be three nonnegative integers. Let
            `W(n, d, s)` denote the set of all `n`-tuples
            `(w_1, w_2, \\ldots, w_n)` of positive integers having the
            property that there exist precisely `d` elements `i`
            of `\\left\\{ 1, 2, \\ldots, n-1 \\right\\}` satisfying
            `w_i > w_{i+1}`, and precisely `s` elements `i` of
            `\\left\\{ 1, 2, \\ldots, n-1 \\right\\}` satisfying
            `w_i = w_{i+1}`. For every
            `w = (w_1, w_2, \\ldots, w_n) \\in W(n, d, s)`, let `x_w`
            be the monomial `x_{w_1} x_{w_2} \\cdots x_{w_n}`. We then
            define the power series `X_{n, d, s}` by

            .. MATH::

                X_{n, d, s} = \\sum_{w \\in W(n, d, s)} x_w .

            This is a symmetric function (according to
            [GriRei18]_, Exercise 2.9.11(b)), and for `s = 0` equals
            the `t^d`-coefficient of the descent enumerator of Smirnov
            words of length `n` (an example of a chromatic
            quasisymmetric function which happens to be symmetric --
            see [ShaWach2014]_, Example 2.5).

            Assume that `n > 0`. Then, we can define three further
            power series as follows:

            .. MATH::

                U_{n, d, s} = \\sum_{w_1 < w_n} x_w ; \\qquad
                V_{n, d, s} = \\sum_{w_1 = w_n} x_w ; \\qquad
                W_{n, d, s} = \\sum_{w_1 > w_n} x_w ,

            where all three sums range over
            `w = (w_1, w_2, \\ldots, w_n) \\in W(n, d, s)`. These
            three power series `U_{n, d, s}`, `V_{n, d, s}` and
            `W_{n, d, s}` are symmetric functions as well
            ([GriRei18]_, Exercise 2.9.11(c)). Their sum is
            `X_{n, d, s}`.

            REFERENCES:

            .. [ShaWach2014] John Shareshian, Michelle L. Wachs.
               *Chromatic quasisymmetric functions*.
               :arxiv:`1405.4629v2`.

            .. [GriRei18]_

            INPUT:

            - ``n`` -- nonnegative integer

            - ``d`` -- nonnegative integer

            - ``s`` -- nonnegative integer

            - ``comparison`` -- (default: ``None``) a variable
              which can take the forms ``None``, ``-1``, ``0``
              and ``1``

            OUTPUT:

            The Carlitz-Shareshian-Wachs symmetric function
            `X_{n, d, s}` (if ``comparison`` is ``None``), or
            `U_{n, d, s}` (if ``comparison`` is ``-1``), or
            `V_{n, d, s}` (if ``comparison`` is ``0``), or
            `W_{n, d, s}` (if ``comparison`` is ``1``) written in the
            basis ``self``.

            EXAMPLES:

            The power series `X_{n, d, s}`::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: m = Sym.m()
                sage: m.carlitz_shareshian_wachs(3, 2, 1)
                0
                sage: m.carlitz_shareshian_wachs(3, 1, 1)
                m[2, 1]
                sage: m.carlitz_shareshian_wachs(3, 2, 0)
                m[1, 1, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 2)
                m[3]
                sage: m.carlitz_shareshian_wachs(3, 1, 0)
                4*m[1, 1, 1] + m[2, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 1)
                m[2, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 0)
                m[1, 1, 1]
                sage: m.carlitz_shareshian_wachs(5, 2, 2)
                m[2, 2, 1] + m[3, 1, 1]
                sage: m.carlitz_shareshian_wachs(1, 0, 0)
                m[1]
                sage: m.carlitz_shareshian_wachs(0, 0, 0)
                m[]

            The power series `U_{n, d, s}`::

                sage: m.carlitz_shareshian_wachs(3, 2, 1, comparison=-1)
                0
                sage: m.carlitz_shareshian_wachs(3, 1, 1, comparison=-1)
                0
                sage: m.carlitz_shareshian_wachs(3, 2, 0, comparison=-1)
                0
                sage: m.carlitz_shareshian_wachs(3, 0, 2, comparison=-1)
                0
                sage: m.carlitz_shareshian_wachs(3, 1, 0, comparison=-1)
                2*m[1, 1, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 1, comparison=-1)
                m[2, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 0, comparison=-1)
                m[1, 1, 1]
                sage: m.carlitz_shareshian_wachs(5, 2, 2, comparison=-1)
                0
                sage: m.carlitz_shareshian_wachs(4, 2, 0, comparison=-1)
                3*m[1, 1, 1, 1]
                sage: m.carlitz_shareshian_wachs(1, 0, 0, comparison=-1)
                0

            The power series `V_{n, d, s}`::

                sage: m.carlitz_shareshian_wachs(3, 2, 1, comparison=0)
                0
                sage: m.carlitz_shareshian_wachs(3, 1, 1, comparison=0)
                0
                sage: m.carlitz_shareshian_wachs(3, 2, 0, comparison=0)
                0
                sage: m.carlitz_shareshian_wachs(3, 0, 2, comparison=0)
                m[3]
                sage: m.carlitz_shareshian_wachs(3, 1, 0, comparison=0)
                m[2, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 1, comparison=0)
                0
                sage: m.carlitz_shareshian_wachs(3, 0, 0, comparison=0)
                0
                sage: m.carlitz_shareshian_wachs(5, 2, 2, comparison=0)
                0
                sage: m.carlitz_shareshian_wachs(4, 2, 0, comparison=0)
                m[2, 1, 1]
                sage: m.carlitz_shareshian_wachs(1, 0, 0, comparison=0)
                m[1]

            The power series `W_{n, d, s}`::

                sage: m.carlitz_shareshian_wachs(3, 2, 1, comparison=1)
                0
                sage: m.carlitz_shareshian_wachs(3, 1, 1, comparison=1)
                m[2, 1]
                sage: m.carlitz_shareshian_wachs(3, 2, 0, comparison=1)
                m[1, 1, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 2, comparison=1)
                0
                sage: m.carlitz_shareshian_wachs(3, 1, 0, comparison=1)
                2*m[1, 1, 1]
                sage: m.carlitz_shareshian_wachs(3, 0, 1, comparison=1)
                0
                sage: m.carlitz_shareshian_wachs(3, 0, 0, comparison=1)
                0
                sage: m.carlitz_shareshian_wachs(5, 2, 2, comparison=1)
                m[2, 2, 1] + m[3, 1, 1]
                sage: m.carlitz_shareshian_wachs(4, 2, 0, comparison=1)
                8*m[1, 1, 1, 1] + 2*m[2, 1, 1] + m[2, 2]
                sage: m.carlitz_shareshian_wachs(1, 0, 0, comparison=1)
                0

            TESTS:

            This works fine over other base rings::

                sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
                sage: P = Sym.macdonald().P()
                sage: m = Sym.m()
                sage: m.carlitz_shareshian_wachs(4, 1, 1)
                4*m[2, 1, 1] + 2*m[2, 2] + 2*m[3, 1]
                sage: P.carlitz_shareshian_wachs(4, 1, 1) == P(m.carlitz_shareshian_wachs(4, 1, 1))
                True
            """
        def abreu_nigro_g(self, H, k, q: str = 'q'):
            """
            Return the Abreu-Nigro `g_{H,k}(x; q)` symmetric function
            for the Hessenberg function ``H`` in the basis ``self``.

            INPUT:

            - ``H`` -- list; the Hessenberg function
            - ``k`` -- integer; must satisfy ``0 <= k < len(H)``
            - ``q`` -- (default: ``'q'``) base ring element for `q`

            A *Hessenberg function* (of length `n`) is a function `H \\colon
            \\{1, \\ldots, n\\} \\to \\{1, \\ldots, n\\}` such that `\\max(i, H(i-1))
            \\leq H(i) \\leq n` for all `i` (by convention `H(0) = 0`). The
            *Abreu-Nigro* `g` *symmetric function* [AN2023]_ (Definition 1.3)
            is defined by

            .. MATH::

                g_{H,k}(x; q) := \\sum_{\\sigma = \\tau_1 \\cdots \\tau_j}
                (-1)^{|\\tau_1|-n+k} q^{w_H(\\sigma)} h_{|\\tau_1|-n+k}(x)
                \\omega( \\rho_{|\\tau_2|,\\ldots,|\\tau_j|}(x; q) ),

            where the sum is over all permutations `\\sigma \\in S_n` such that
            `|\\tau_1| \\geq n - k` and `\\sigma(i) \\leq H(i)` for all `i`;
            `\\tau_1, \\ldots, \\tau_j` is the cycle decomposition of `\\sigma`
            (with cycles sorted by smallest elements, and with these
            smallest elements placed at the beginning of each cycle);
            `\\rho_{\\lambda}` is the Abreu-Nigro basis [AN2021II]_
            (see :class:`SymmetricFunctions.abreu_nigro`); and

            .. MATH::

                w_H(\\sigma) = |\\{(i, j) \\mid i < j \\leq H(i) \\text{ and } j
                                 \\text{ precedes } i \\text{ in } \\sigma^c \\}|,

            with `\\sigma^c` being the permutation formed by removing the
            parentheses in the cycle decomposition `\\tau_1 \\cdots \\tau_j`.

            EXAMPLES:

            We verify the `e`-positivity of some examples::

                sage: q = ZZ['q'].fraction_field().gen()
                sage: Sym = SymmetricFunctions(q.parent())
                sage: e = Sym.e()
                sage: e.abreu_nigro_g([1,2], 0, q)
                0
                sage: e.abreu_nigro_g([1,2], 1, q)
                e[1]
                sage: e.abreu_nigro_g([2,2], 0, q)
                e[]
                sage: e.abreu_nigro_g([2,2], 1, q)
                0
                sage: H = [3, 3, 4, 5, 6, 7, 7]
                sage: [e.abreu_nigro_g(H, k, q) for k in range(7)]
                [(q+1)*e[],
                 q*e[1],
                 (q^2+q)*e[2],
                 q^2*e[2, 1] + (q^3+2*q^2+q)*e[3],
                 (q^3+q^2)*e[2, 2] + (q^3+q^2)*e[3, 1] + (q^4+2*q^3+2*q^2+q)*e[4],
                 q^3*e[3, 2] + (q^4+q^3+q^2)*e[5],
                 (q^4+q^3)*e[3, 3] + (q^4+q^3)*e[4, 2] + (q^5+q^4+q^3+q^2)*e[6]]

            We reproduce Example 1.5 in [AN2023]_::

                sage: H = [2, 4, 4, 5, 6, 6]
                sage: [e.abreu_nigro_g(H, k, q) for k in range(6)]
                [(q+1)*e[],
                 q*e[1],
                 (q^2+q)*e[2],
                 q^2*e[3],
                 (q^3+q^2)*e[4],
                 (q^4+3*q^3+q^2)*e[3, 2] + (q^4+q^3+q^2)*e[4, 1]
                  + (q^5+2*q^4+2*q^3+2*q^2+q)*e[5]]

            We verify Theorem 1.7 in [AN2023]_ for an example::

                sage: from sage.combinat.q_analogues import q_int
                sage: H = [2, 4, 4, 4]
                sage: G = posets.HessenbergPoset(H).incomparability_graph()
                sage: cqf = G.chromatic_quasisymmetric_function(q, q.parent()); cqf
                (q^4+6*q^3+10*q^2+6*q+1)*M[1, 1, 1, 1] + (q^3+2*q^2+q)*M[1, 1, 2]
                 + (q^3+2*q^2+q)*M[1, 2, 1] + (q^3+2*q^2+q)*M[2, 1, 1]
                sage: e(cqf.to_symmetric_function())
                (q^3+2*q^2+q)*e[3, 1] + (q^4+2*q^3+2*q^2+2*q+1)*e[4]
                sage: sum(q_int(k, q) * e[k] * e.abreu_nigro_g(H, len(H)-k, q)
                ....:     for k in range(1, len(H)+1))
                (q^3+2*q^2+q)*e[3, 1] + (q^4+2*q^3+2*q^2+2*q+1)*e[4]

            TESTS::

                sage: e = SymmetricFunctions(ZZ['q'].fraction_field()).e()
                sage: e.abreu_nigro_g([3, 2, 3], 2, q)
                Traceback (most recent call last):
                ...
                ValueError: [3, 2, 3] is not a Hessenberg function
                sage: e.abreu_nigro_g([1, 4, 5], 2, q)
                Traceback (most recent call last):
                ...
                ValueError: [1, 4, 5] is not a Hessenberg function
                sage: e.abreu_nigro_g([1, 1, 3], 2, q)
                Traceback (most recent call last):
                ...
                ValueError: [1, 1, 3] is not a Hessenberg function
                sage: e.abreu_nigro_g([1, 3, 3], 5, q)
                Traceback (most recent call last):
                ...
                ValueError: k must be between 0 and 3
            """
        def formal_series_ring(self):
            """
            Return the completion of all formal linear combinations of
            ``self`` with finite linear combinations in each homogeneous
            degree (computed lazily).

            EXAMPLES::

                sage: s = SymmetricFunctions(ZZ).s()
                sage: L = s.formal_series_ring()
                sage: L
                Lazy completion of Symmetric Functions over Integer Ring in the Schur basis

            TESTS::

                sage: type(L)
                <class 'sage.rings.lazy_series_ring.LazySymmetricFunctions_with_category'>
                sage: s.completion() is s.formal_series_ring()
                True
            """
        completion = formal_series_ring

class FilteredSymmetricFunctionsBases(Category_realization_of_parent):
    """
    The category of filtered bases of the ring of symmetric functions.

    TESTS::

        sage: from sage.combinat.sf.sfa import FilteredSymmetricFunctionsBases
        sage: Sym = SymmetricFunctions(QQ)
        sage: bases = FilteredSymmetricFunctionsBases(Sym); bases
        Category of filtered bases of Symmetric Functions over Rational Field
        sage: Sym.schur() in bases
        True
        sage: Sym.sp() in bases
        True
    """
    def super_categories(self) -> list:
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import FilteredSymmetricFunctionsBases
            sage: Sym = SymmetricFunctions(QQ)
            sage: bases = FilteredSymmetricFunctionsBases(Sym)
            sage: bases.super_categories()
            [Category of bases of Symmetric Functions over Rational Field,
             Category of commutative filtered Hopf algebras with basis over Rational Field]
        """

class GradedSymmetricFunctionsBases(Category_realization_of_parent):
    """
    The category of graded bases of the ring of symmetric functions.

    These are further required to have the property that the basis element
    indexed by the empty partition is `1`.

    TESTS::

        sage: from sage.combinat.sf.sfa import GradedSymmetricFunctionsBases
        sage: Sym = SymmetricFunctions(QQ)
        sage: bases = GradedSymmetricFunctionsBases(Sym); bases
        Category of graded bases of Symmetric Functions over Rational Field
        sage: Sym.schur() in bases
        True
        sage: Sym.sp() in bases
        False
    """
    def super_categories(self) -> list:
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import GradedSymmetricFunctionsBases
            sage: Sym = SymmetricFunctions(QQ)
            sage: bases = GradedSymmetricFunctionsBases(Sym)
            sage: bases.super_categories()
            [Category of filtered bases of Symmetric Functions over Rational Field,
             Category of commutative graded Hopf algebras with basis over Rational Field]
        """
    class ParentMethods:
        def antipode_by_coercion(self, element):
            """
            The antipode of ``element``.

            INPUT:

            - ``element`` -- element in a basis of the ring of symmetric functions

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: p = Sym.p()
                sage: s = Sym.s()
                sage: e = Sym.e()
                sage: h = Sym.h()
                sage: (h([]) + h([1])).antipode() # indirect doctest
                h[] - h[1]
                sage: (s([]) + s([1]) + s[2]).antipode()
                s[] - s[1] + s[1, 1]
                sage: (p([2]) + p([3])).antipode()
                -p[2] - p[3]
                sage: (e([2]) + e([3])).antipode()
                e[1, 1] - e[1, 1, 1] - e[2] + 2*e[2, 1] - e[3]
                sage: f = Sym.f()
                sage: f([3,2,1]).antipode()
                -f[3, 2, 1] - 4*f[3, 3] - 2*f[4, 2] - 2*f[5, 1] - 6*f[6]

            The antipode is an involution::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: s = Sym.s()
                sage: all( s[u].antipode().antipode() == s[u] for u in Partitions(4) )
                True

            The antipode is an algebra homomorphism::

                sage: Sym = SymmetricFunctions(FiniteField(23))
                sage: h = Sym.h()
                sage: all( all( (s[u] * s[v]).antipode() == s[u].antipode() * s[v].antipode()
                ....:           for u in Partitions(3) )
                ....:      for v in Partitions(3) )
                True

            TESTS:

            Everything works over `\\ZZ`::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: p = Sym.p()
                sage: s = Sym.s()
                sage: e = Sym.e()
                sage: h = Sym.h()
                sage: (h([]) + h([1])).antipode() # indirect doctest
                h[] - h[1]
                sage: (s([]) + s([1]) + s[2]).antipode()
                s[] - s[1] + s[1, 1]
                sage: (p([2]) + p([3])).antipode()
                -p[2] - p[3]
                sage: (e([2]) + e([3])).antipode()
                e[1, 1] - e[1, 1, 1] - e[2] + 2*e[2, 1] - e[3]
            """
        def counit(self, element):
            """
            Return the counit of ``element``.

            The counit is the constant term of ``element``.

            INPUT:

            - ``element`` -- element in a basis of the ring of symmetric functions

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: m = Sym.monomial()
                sage: f = 2*m[2,1] + 3*m[[]]
                sage: f.counit()
                3
            """
        def degree_negation(self, element):
            """
            Return the image of ``element`` under the degree negation
            automorphism of the ring of symmetric functions.

            The degree negation is the automorphism which scales every
            homogeneous element of degree `k` by `(-1)^k` (for all `k`).

            INPUT:

            - ``element`` -- symmetric function written in ``self``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: m = Sym.monomial()
                sage: f = 2*m[2,1] + 4*m[1,1] - 5*m[1] - 3*m[[]]
                sage: m.degree_negation(f)
                -3*m[] + 5*m[1] + 4*m[1, 1] - 2*m[2, 1]

            TESTS:

            Using :meth:`degree_negation` on an element of a different
            basis works correctly::

                sage: e = Sym.elementary()
                sage: m.degree_negation(e[3])
                -m[1, 1, 1]
                sage: m.degree_negation(m(e[3]))
                -m[1, 1, 1]
            """
    class ElementMethods:
        def degree_negation(self):
            """
            Return the image of ``self`` under the degree negation
            automorphism of the ring of symmetric functions.

            The degree negation is the automorphism which scales every
            homogeneous element of degree `k` by `(-1)^k` (for all `k`).

            Calling ``degree_negation(self)`` is equivalent to calling
            ``self.parent().degree_negation(self)``.

            EXAMPLES::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: m = Sym.monomial()
                sage: f = 2*m[2,1] + 4*m[1,1] - 5*m[1] - 3*m[[]]
                sage: f.degree_negation()
                -3*m[] + 5*m[1] + 4*m[1, 1] - 2*m[2, 1]
                sage: x = m.zero().degree_negation(); x
                0
                sage: parent(x) is m
                True
            """
        def degree_zero_coefficient(self):
            """
            Return the degree zero coefficient of ``self``.

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: m = Sym.monomial()
                sage: f = 2*m[2,1] + 3*m[[]]
                sage: f.degree_zero_coefficient()
                3
            """
        def is_unit(self) -> bool:
            """
            Return whether this element is a unit in the ring.

            EXAMPLES::

                sage: m = SymmetricFunctions(ZZ).monomial()
                sage: (2*m[2,1] + m[[]]).is_unit()
                False

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: (3/2*m([])).is_unit()
                True
            """

class SymmetricFunctionAlgebra_generic(CombinatorialFreeModule):
    """
    Abstract base class for symmetric function algebras.

    .. TODO::

        Most of the methods in this class are generic (manipulations of
        morphisms, ...) and should be generalized (or removed)

    TESTS::

        sage: s = SymmetricFunctions(QQ).s()
        sage: m = SymmetricFunctions(ZZ).m()
        sage: s(m([2,1]))
        -2*s[1, 1, 1] + s[2, 1]
    """
    def __init__(self, Sym, basis_name=None, prefix=None, graded: bool = True) -> None:
        """
        Initialize the symmetric function algebra.

        INPUT:

        - ``Sym`` -- the ring of symmetric functions
        - ``basis_name`` -- name of basis (default: ``None``)
        - ``prefix`` -- prefix used to display basis
        - ``graded`` -- boolean (default: ``True``); if ``True``, then the basis is
          considered to be graded, otherwise the basis is filtered

        TESTS::

            sage: from sage.combinat.sf.classical import SymmetricFunctionAlgebra_classical
            sage: s = SymmetricFunctions(QQ).s()
            sage: isinstance(s, SymmetricFunctionAlgebra_classical)
            True
            sage: TestSuite(s).run()
        """
    def __getitem__(self, c):
        """
        This method implements the abuses of notations ``p[2,1]``,
        ``p[[2,1]]``, ``p[Partition([2,1])]``.

        INPUT:

        - ``c`` -- list, list of lists, or partition

        .. TODO::

            Should call ``super.term`` so as not to interfere with the
            standard notation ``p['x,y,z']``.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s[2,1]
            s[2, 1]
            sage: s[[2,1]]
            s[2, 1]
            sage: s[Partition([2,1])]
            s[2, 1]

        TESTS:

        Check that a single number which is in ``ZZ`` can be used::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s[QQbar(2)]
            s[2]
        """
    def symmetric_function_ring(self):
        """
        Return the family of symmetric functions associated to the
        basis ``self``.

        OUTPUT: an instance of the ring of symmetric functions

        EXAMPLES::

            sage: schur = SymmetricFunctions(QQ).schur()
            sage: schur.symmetric_function_ring()
            Symmetric Functions over Rational Field
            sage: power = SymmetricFunctions(QQ['t']).power()
            sage: power.symmetric_function_ring()
            Symmetric Functions over Univariate Polynomial Ring in t over Rational Field
        """
    def prefix(self) -> str:
        """
        Return the prefix on the elements of ``self``.

        EXAMPLES::

            sage: schur = SymmetricFunctions(QQ).schur()
            sage: schur([3,2,1])
            s[3, 2, 1]
            sage: schur.prefix()
            's'
        """
    def transition_matrix(self, basis, n):
        """
        Return the transition matrix between ``self`` and ``basis`` for the
        homogeneous component of degree ``n``.

        INPUT:

        - ``basis`` -- a basis of the ring of symmetric functions
        - ``n`` -- nonnegative integer

        OUTPUT:

        A matrix of coefficients giving the expansion of the homogeneous
        degree-`n` elements of ``self`` in the degree-`n` elements of ``basis``.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: m = SymmetricFunctions(QQ).m()
            sage: s.transition_matrix(m,5)
            [1 1 1 1 1 1 1]
            [0 1 1 2 2 3 4]
            [0 0 1 1 2 3 5]
            [0 0 0 1 1 3 6]
            [0 0 0 0 1 2 5]
            [0 0 0 0 0 1 4]
            [0 0 0 0 0 0 1]
            sage: s.transition_matrix(m,1)
            [1]
            sage: s.transition_matrix(m,0)
            [1]

        ::

            sage: p = SymmetricFunctions(QQ).p()
            sage: s.transition_matrix(p, 4)
            [ 1/4  1/3  1/8  1/4 1/24]
            [-1/4    0 -1/8  1/4  1/8]
            [   0 -1/3  1/4    0 1/12]
            [ 1/4    0 -1/8 -1/4  1/8]
            [-1/4  1/3  1/8 -1/4 1/24]
            sage: StoP = s.transition_matrix(p,4)
            sage: a = s([3,1])+5*s([1,1,1,1])-s([4])
            sage: a
            5*s[1, 1, 1, 1] + s[3, 1] - s[4]
            sage: mon = sorted(a.support())
            sage: coeffs = [a[i] for i in mon]
            sage: coeffs
            [5, 1, -1]
            sage: mon
            [[1, 1, 1, 1], [3, 1], [4]]
            sage: cm = matrix([[-1,1,0,0,5]])
            sage: cm * StoP
            [-7/4  4/3  3/8 -5/4 7/24]
            sage: p(a)
            7/24*p[1, 1, 1, 1] - 5/4*p[2, 1, 1] + 3/8*p[2, 2] + 4/3*p[3, 1] - 7/4*p[4]

        ::

            sage: h = SymmetricFunctions(QQ).h()
            sage: e = SymmetricFunctions(QQ).e()
            sage: s.transition_matrix(m,7) == h.transition_matrix(s,7).transpose()
            True

        ::

            sage: h.transition_matrix(m, 7) == h.transition_matrix(m, 7).transpose()
            True

        ::

            sage: h.transition_matrix(e, 7) == e.transition_matrix(h, 7)
            True

        ::

            sage: p.transition_matrix(s, 5)
            [ 1 -1  0  1  0 -1  1]
            [ 1  0 -1  0  1  0 -1]
            [ 1 -1  1  0 -1  1 -1]
            [ 1  1 -1  0 -1  1  1]
            [ 1  0  1 -2  1  0  1]
            [ 1  2  1  0 -1 -2 -1]
            [ 1  4  5  6  5  4  1]

        ::

            sage: e.transition_matrix(m,7) == e.transition_matrix(m,7).transpose()
            True
        """
    def dual_basis(self, scalar=None, scalar_name: str = '', basis_name=None, prefix=None):
        """
        Return the dual basis of ``self`` with respect to the scalar
        product ``scalar``.

        INPUT:

        - ``scalar`` -- a function ``zee`` from partitions to the base ring
          which specifies the scalar product by `\\langle p_{\\lambda},
          p_{\\lambda} \\rangle = \\mathrm{zee}(\\lambda)`. (Independently on the
          function chosen, the power sum basis will always be orthogonal;
          the function ``scalar`` only determines the norms of the basis
          elements.) If ``scalar`` is None, then the standard (Hall) scalar
          product is used.
        - ``scalar_name`` -- name of the scalar function
        - ``prefix`` -- prefix used to display the basis

        EXAMPLES:

        The duals of the elementary symmetric functions with respect to the
        Hall scalar product are the forgotten symmetric functions.

        ::

            sage: e = SymmetricFunctions(QQ).e()
            sage: f = e.dual_basis(prefix='f'); f
            Dual basis to Symmetric Functions over Rational Field in the elementary basis with respect to the Hall scalar product
            sage: f([2,1])^2
            4*f[2, 2, 1, 1] + 6*f[2, 2, 2] + 2*f[3, 2, 1] + 2*f[3, 3] + 2*f[4, 1, 1] + f[4, 2]
            sage: f([2,1]).scalar(e([2,1]))
            1
            sage: f([2,1]).scalar(e([1,1,1]))
            0

        Since the power-sum symmetric functions are orthogonal, their duals
        with respect to the Hall scalar product are scalar multiples of
        themselves.

        ::

            sage: p = SymmetricFunctions(QQ).p()
            sage: q = p.dual_basis(prefix='q'); q
            Dual basis to Symmetric Functions over Rational Field in the powersum basis with respect to the Hall scalar product
            sage: q([2,1])^2
            4*q[2, 2, 1, 1]
            sage: p([2,1]).scalar(q([2,1]))
            1
            sage: p([2,1]).scalar(q([1,1,1]))
            0
        """
    def basis_name(self):
        """
        Return the name of the basis of ``self``.

        This is used for output and, for the classical bases of
        symmetric functions, to connect this basis with Symmetrica.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.s()
            sage: s.basis_name()
            'Schur'
            sage: p = Sym.p()
            sage: p.basis_name()
            'powersum'
            sage: h = Sym.h()
            sage: h.basis_name()
            'homogeneous'
            sage: e = Sym.e()
            sage: e.basis_name()
            'elementary'
            sage: m = Sym.m()
            sage: m.basis_name()
            'monomial'
            sage: f = Sym.f()
            sage: f.basis_name()
            'forgotten'
        """
    def get_print_style(self):
        """
        Return the value of the current print style for ``self``.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s.get_print_style()
            'lex'
            sage: s.set_print_style('length')
            sage: s.get_print_style()
            'length'
            sage: s.set_print_style('lex')
        """
    def set_print_style(self, ps):
        """
        Set the value of the current print style to ``ps``.

        INPUT:

        - ``ps`` -- string specifying the printing style

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s.get_print_style()
            'lex'
            sage: s.set_print_style('length')
            sage: s.get_print_style()
            'length'
            sage: s.set_print_style('lex')
        """
    def from_polynomial(self, poly, check: bool = True):
        """
        Convert polynomial to a symmetric function in the monomial basis
        and then to the basis ``self``.

        INPUT:

        - ``poly`` -- a symmetric polynomial
        - ``check`` -- boolean (default: ``True``); specifies whether
          the computation checks that the polynomial is indeed symmetric

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: h = Sym.homogeneous()
            sage: f = (h([]) + h([2,1]) + h([3])).expand(3)
            sage: h.from_polynomial(f)
            h[] + h[2, 1] + h[3]
            sage: s = Sym.s()
            sage: g = (s([]) + s([2,1])).expand(3); g
            x0^2*x1 + x0*x1^2 + x0^2*x2 + 2*x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + 1
            sage: s.from_polynomial(g)
            s[] + s[2, 1]
        """
    def product_by_coercion(self, left, right):
        """
        Return the product of elements ``left`` and ``right`` by coercion to
        the Schur basis.

        INPUT:

        - ``left``, ``right`` -- instances of this basis

        OUTPUT: the product of ``left`` and ``right`` expressed in the basis ``self``

        EXAMPLES::

            sage: p = SymmetricFunctions(QQ).p()
            sage: p.product_by_coercion(p[3,1,1], p[2,2])
            p[3, 2, 2, 1, 1]
            sage: m = SymmetricFunctions(QQ).m()
            sage: m.product_by_coercion(m[2,1],m[1,1]) == m[2,1]*m[1,1]
            True
        """
    def coproduct_by_coercion(self, elt):
        """
        Return the coproduct of the element ``elt`` by coercion to
        the Schur basis.

        INPUT:

        - ``elt`` -- an instance of this basis

        OUTPUT:

        - The image of ``elt`` under the comultiplication (=coproduct)
          of the coalgebra of symmetric functions. The result is an
          element of the tensor squared of the basis ``self``.

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).m()
            sage: m[3,1,1].coproduct()
            m[] # m[3, 1, 1] + m[1] # m[3, 1] + m[1, 1] # m[3] + m[3] # m[1, 1] + m[3, 1] # m[1] + m[3, 1, 1] # m[]
            sage: m.coproduct_by_coercion(m[2,1])
            m[] # m[2, 1] + m[1] # m[2] + m[2] # m[1] + m[2, 1] # m[]
            sage: m.coproduct_by_coercion(m[2,1]) == m([2,1]).coproduct()
            True
            sage: McdH = SymmetricFunctions(QQ['q','t'].fraction_field()).macdonald().H()
            sage: McdH[2,1].coproduct()
            McdH[] # McdH[2, 1] + ((q^2*t-1)/(q*t-1))*McdH[1] # McdH[1, 1] + ((q*t^2-1)/(q*t-1))*McdH[1] # McdH[2] + ((q^2*t-1)/(q*t-1))*McdH[1, 1] # McdH[1] + ((q*t^2-1)/(q*t-1))*McdH[2] # McdH[1] + McdH[2, 1] # McdH[]
            sage: HLQp = SymmetricFunctions(QQ['t'].fraction_field()).hall_littlewood().Qp()
            sage: HLQp[2,1].coproduct()
            HLQp[] # HLQp[2, 1] + HLQp[1] # HLQp[1, 1] + HLQp[1] # HLQp[2] + HLQp[1, 1] # HLQp[1] + HLQp[2] # HLQp[1] + HLQp[2, 1] # HLQp[]
            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: LLT = Sym.llt(3)
            sage: LLT.cospin([3,2,1]).coproduct()
            (t+1)*m[] # m[1, 1] + m[] # m[2] + (t+1)*m[1] # m[1] + (t+1)*m[1, 1] # m[] + m[2] # m[]
            sage: f = SymmetricFunctions(ZZ).f()
            sage: f[3].coproduct()
            f[] # f[3] + f[3] # f[]
            sage: f[3,2,1].coproduct()
            f[] # f[3, 2, 1] + f[1] # f[3, 2] + f[2] # f[3, 1] + f[2, 1] # f[3] + f[3] # f[2, 1] + f[3, 1] # f[2] + f[3, 2] # f[1] + f[3, 2, 1] # f[]
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: s.construction()
            (SymmetricFunctionsFunctor[Schur], Integer Ring)
        """
    def change_ring(self, R):
        """
        Return the base change of ``self`` to `R`.

        EXAMPLES::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: s.change_ring(QQ)
            Symmetric Functions over Rational Field in the Schur basis
        """

class SymmetricFunctionAlgebra_generic_Element(CombinatorialFreeModule.Element):
    """
    Class of generic elements for the symmetric function algebra.

    TESTS::

        sage: m = SymmetricFunctions(QQ).m()
        sage: f = sum([m(p) for p in Partitions(3)])
        sage: m.set_print_style('lex')
        sage: f
        m[1, 1, 1] + m[2, 1] + m[3]
        sage: m.set_print_style('length')
        sage: f
        m[3] + m[2, 1] + m[1, 1, 1]
        sage: m.set_print_style('maximal_part')
        sage: f
        m[1, 1, 1] + m[2, 1] + m[3]
        sage: m.set_print_style('lex')
    """
    def __truediv__(self, x):
        """
        Return the quotient of ``self`` by ``other``.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s[1]/(1+s[1])
            s[1]/(s[] + s[1])

            sage: s[1]/2
            1/2*s[1]

        TESTS::

            sage: (s[1]/2).parent()
            Symmetric Functions over Rational Field in the Schur basis
        """
    def factor(self):
        """
        Return the factorization of this symmetric function.

        EXAMPLES::

            sage: e = SymmetricFunctions(QQ).e()
            sage: factor((5*e[3] + e[2,1] + e[1])*(7*e[2] + e[5,1]))
            (e[1] + e[2, 1] + 5*e[3]) * (7*e[2] + e[5, 1])

            sage: R.<x, y> = QQ[]
            sage: s = SymmetricFunctions(R.fraction_field()).s()
            sage: factor((s[3] + x*s[2,1] + 1)*(3*y*s[2] + s[4,1] + x*y))
            (-s[] - x*s[2, 1] - s[3]) * (-x*y*s[] - 3*y*s[2] - s[4, 1])

        TESTS::

            sage: p = SymmetricFunctions(QQ).p()
            sage: factor((p[3] + p[2,1])*(p[2] + p[4,1]))
            (p[2, 1] + p[3]) * (p[2] + p[4, 1])

            sage: s = SymmetricFunctions(QQ).s()
            sage: factor((s[3] + s[2,1])*(s[2] + s[4,1]))
            (-1) * s[1] * s[2] * (-s[2] - s[4, 1])

            sage: s = SymmetricFunctions(ZZ).s()
            sage: factor((s[3] + s[2,1])*(s[2] + s[4,1]))
            (-1) * s[1] * s[2] * (-s[2] - s[4, 1])

            sage: R.<t> = QQ[]
            sage: JP = SymmetricFunctions(FractionField(R)).jack(t).P()
            sage: f = (JP[2,1]*t + JP[1,1,1])^2
            sage: f.factor()
            (1/(t^2 + 4*t + 4)) * ((-t-2)*JackP[1, 1, 1] + (-t^2-2*t)*JackP[2, 1])^2

        Some corner cases::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: factor(s(6))
            2 * 3

            sage: factor(6*s[1])
            2*s[] * 3*s[] * s[1]
        """
    @coerce_binop
    def gcd(self, other):
        """
        Return the greatest common divisor with ``other``.

        INPUT:

        - ``other`` -- the other symmetric function

        EXAMPLES::

            sage: e = SymmetricFunctions(ZZ).e()
            sage: A = 5*e[3] + e[2,1] + e[1]
            sage: B = 7*e[2] + e[5,1]
            sage: C = 3*e[1,1] + e[2]
            sage: gcd(A*B^2, B*C)
            7*e[2] + e[5, 1]

            sage: p = SymmetricFunctions(ZZ).p()
            sage: gcd(e[2,1], p[1,1]-p[2])
            e[2]
            sage: gcd(p[2,1], p[3,2]-p[2,1])
            p[2]

        TESTS::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: gcd(s(0), s[1])
            s[1]

            sage: gcd(s(0), s(1))
            s[]

            sage: gcd(s(9), s(6))
            3*s[]
        """
    def plethysm(self, x, include=None, exclude=None):
        """
        Return the outer plethysm of ``self`` with ``x``.

        This is implemented only over base rings which are
        `\\QQ`-algebras.  (To compute outer plethysms over general
        binomial rings, change bases to the fraction field.)

        The outer plethysm of `f` with `g` is commonly denoted by
        `f \\left[ g \\right]` or by `f \\circ g`. It is an algebra map
        in `f`, but not (generally) in `g`.

        By default, the degree one elements are taken to be the
        generators for the ``self``'s base ring. This setting can be
        modified by specifying the ``include`` and ``exclude`` keywords.

        INPUT:

        - ``x`` -- a symmetric function over the same base ring as
          ``self``
        - ``include`` -- list of variables to be treated as
          degree one elements instead of the default degree one elements
        - ``exclude`` -- list of variables to be excluded
          from the default degree one elements

        OUTPUT:

        An element in the parent of ``x`` or the base ring `R` of ``self``
        when ``x`` is in `R`.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.s()
            sage: h = Sym.h()
            sage: h3h2 = h[3](h[2]); h3h2
            h[2, 2, 2] - 2*h[3, 2, 1] + h[3, 3] + h[4, 1, 1] - h[5, 1] + h[6]
            sage: s(h3h2)
            s[2, 2, 2] + s[4, 2] + s[6]
            sage: p = Sym.p()
            sage: p3s21 = p[3](s[2,1]); p3s21
            s[2, 2, 2, 1, 1, 1] - s[2, 2, 2, 2, 1] - s[3, 2, 1, 1, 1, 1]
             + s[3, 2, 2, 2] + s[3, 3, 1, 1, 1] - s[3, 3, 2, 1] + 2*s[3, 3, 3]
             + s[4, 1, 1, 1, 1, 1] - s[4, 3, 2] + s[4, 4, 1] - s[5, 1, 1, 1, 1]
             + s[5, 2, 2] - s[5, 4] + s[6, 1, 1, 1] - s[6, 2, 1] + s[6, 3]
            sage: p(p3s21)
            1/3*p[3, 3, 3] - 1/3*p[9]
            sage: e = Sym.e()
            sage: e[3](e[2])
            e[3, 3] + e[4, 1, 1] - 2*e[4, 2] - e[5, 1] + e[6]

        Note that the output is in the basis of the input ``x``::

            sage: s[2,1](h[3])
            h[4, 3, 2] - h[4, 4, 1] - h[5, 2, 2] + h[5, 3, 1] + h[5, 4]
             + h[6, 2, 1] - 2*h[6, 3] - h[7, 1, 1] + h[7, 2] + h[8, 1] - h[9]

            sage: h[2,1](s[3])
            s[4, 3, 2] + s[4, 4, 1] + s[5, 2, 2] + s[5, 3, 1] + s[5, 4]
             + s[6, 2, 1] + 2*s[6, 3] + 2*s[7, 2] + s[8, 1] + s[9]

        Examples over a polynomial ring::

            sage: R.<t> = QQ[]
            sage: s = SymmetricFunctions(R).s()
            sage: a = s([3])
            sage: f = t * s([2])
            sage: a(f)
            t^3*s[2, 2, 2] + t^3*s[4, 2] + t^3*s[6]
            sage: f(a)
            t*s[4, 2] + t*s[6]
            sage: s(0).plethysm(s[1])
            0
            sage: s(1).plethysm(s[1])
            s[]
            sage: s(1).plethysm(s(0))
            s[]

        When ``x`` is a constant, then it is returned as an element
        of the base ring::

            sage: s[3](2).parent() is R
            True

        Sage also handles plethysm of tensor products of symmetric functions::

            sage: s = SymmetricFunctions(QQ).s()
            sage: X = tensor([s[1],s[[]]])
            sage: Y = tensor([s[[]],s[1]])
            sage: s[1,1,1](X+Y)
            s[] # s[1, 1, 1] + s[1] # s[1, 1] + s[1, 1] # s[1] + s[1, 1, 1] # s[]
            sage: s[1,1,1](X*Y)
            s[1, 1, 1] # s[3] + s[2, 1] # s[2, 1] + s[3] # s[1, 1, 1]

        One can use this to work with symmetric functions in two sets of
        commuting variables. For example, we verify the Cauchy identities
        (in degree 5)::

            sage: m = SymmetricFunctions(QQ).m()
            sage: P5 = Partitions(5)
            sage: sum(s[mu](X)*s[mu](Y) for mu in P5) == sum(m[mu](X)*h[mu](Y) for mu in P5)
            True
            sage: sum(s[mu](X)*s[mu.conjugate()](Y) for mu in P5) == sum(m[mu](X)*e[mu](Y) for mu in P5)
            True

        Sage can also do the plethysm with an element in the completion::

            sage: s = SymmetricFunctions(QQ).s()
            sage: L = LazySymmetricFunctions(s)
            sage: f = s[2,1]
            sage: g = L(s[1]) / (1 - L(s[1])); g
            s[1] + (s[1,1]+s[2]) + (s[1,1,1]+2*s[2,1]+s[3])
             + (s[1,1,1,1]+3*s[2,1,1]+2*s[2,2]+3*s[3,1]+s[4])
             + (s[1,1,1,1,1]+4*s[2,1,1,1]+5*s[2,2,1]+6*s[3,1,1]+5*s[3,2]+4*s[4,1]+s[5])
             + ... + O^8
            sage: fog = f(g)
            sage: fog[:8]
            [s[2, 1],
             s[1, 1, 1, 1] + 3*s[2, 1, 1] + 2*s[2, 2] + 3*s[3, 1] + s[4],
             2*s[1, 1, 1, 1, 1] + 8*s[2, 1, 1, 1] + 10*s[2, 2, 1]
             + 12*s[3, 1, 1] + 10*s[3, 2] + 8*s[4, 1] + 2*s[5],
             3*s[1, 1, 1, 1, 1, 1] + 17*s[2, 1, 1, 1, 1] + 30*s[2, 2, 1, 1]
             + 16*s[2, 2, 2] + 33*s[3, 1, 1, 1] + 54*s[3, 2, 1] + 16*s[3, 3]
             + 33*s[4, 1, 1] + 30*s[4, 2] + 17*s[5, 1] + 3*s[6],
             5*s[1, 1, 1, 1, 1, 1, 1] + 30*s[2, 1, 1, 1, 1, 1] + 70*s[2, 2, 1, 1, 1]
             + 70*s[2, 2, 2, 1] + 75*s[3, 1, 1, 1, 1] + 175*s[3, 2, 1, 1]
             + 105*s[3, 2, 2] + 105*s[3, 3, 1] + 100*s[4, 1, 1, 1] + 175*s[4, 2, 1]
             + 70*s[4, 3] + 75*s[5, 1, 1] + 70*s[5, 2] + 30*s[6, 1] + 5*s[7]]
            sage: parent(fog)
            Lazy completion of Symmetric Functions over Rational Field in the Schur basis

        .. SEEALSO::

            :meth:`adams_operator`

        TESTS::

            sage: (1+p[2]).plethysm(p[2])
            p[] + p[4]

        Check that degree one elements are treated in the correct way::

            sage: R.<a1,a2,a11,b1,b21,b111> = QQ[]
            sage: p = SymmetricFunctions(R).p()
            sage: f = a1*p[1] + a2*p[2] + a11*p[1,1]
            sage: g = b1*p[1] + b21*p[2,1] + b111*p[1,1,1]
            sage: r = f(g); r
            a1*b1*p[1] + a11*b1^2*p[1, 1] + a1*b111*p[1, 1, 1]
             + 2*a11*b1*b111*p[1, 1, 1, 1] + a11*b111^2*p[1, 1, 1, 1, 1, 1]
             + a2*b1^2*p[2] + a1*b21*p[2, 1] + 2*a11*b1*b21*p[2, 1, 1]
             + 2*a11*b21*b111*p[2, 1, 1, 1, 1] + a11*b21^2*p[2, 2, 1, 1]
             + a2*b111^2*p[2, 2, 2] + a2*b21^2*p[4, 2]
            sage: r - f(g, include=[])
            (a2*b1^2-a2*b1)*p[2] + (a2*b111^2-a2*b111)*p[2, 2, 2] + (a2*b21^2-a2*b21)*p[4, 2]

        Check that we can compute the plethysm with a constant::

            sage: p[2,2,1](2)
            8

            sage: p[2,2,1](int(2))
            8

            sage: p[2,2,1](a1)
            a1^5

            sage: X = algebras.Shuffle(QQ, 'ab')
            sage: Y = algebras.Shuffle(QQ, 'bc')
            sage: T = tensor([X, Y])
            sage: s = SymmetricFunctions(T).s()
            sage: s[2](5)
            15*B[] # B[]

        .. TODO::

            The implementation of plethysm in
            :class:`sage.data_structures.stream.Stream_plethysm` seems
            to be faster.  This should be investigated.
        """
    __call__ = plethysm
    def inner_plethysm(self, x):
        """
        Return the inner plethysm of ``self`` with ``x``.

        Whenever `R` is a `\\QQ`-algebra, and `f` and `g` are two
        symmetric functions over `R` such that the constant term of `f`
        is zero, the inner plethysm of `f` with `g` is a symmetric
        function over `R`, and the degree of this symmetric function is
        the same as the degree of `g`. We will denote the inner plethysm
        of `f` with `g` by `f \\{ g \\}` (in contrast to the notation of
        outer plethysm which is generally denoted `f [ g ]`); in Sage
        syntax, it is ``f.inner_plethysm(g)``.

        First we describe the axiomatic definition of the operation; see
        below for a representation-theoretic interpretation.
        In the following equations, we denote the outer product
        (i.e., the standard product on the ring of symmetric functions,
        :meth:`~sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.product`)
        by `\\cdot` and the Kronecker product (:meth:`itensor`) by `\\ast`).

        .. MATH::

            (f + g) \\{ h \\} = f \\{ h \\} + g \\{ h \\}

            (f \\cdot g) \\{ h \\} = (f \\{ h \\}) \\ast (g \\{ h \\})

            p_k \\{ f + g \\} = p_k \\{ f \\} + p_k \\{ g \\}

        where `p_k` is the `k`-th power-sum symmetric function for every
        `k > 0`.

        Let `\\sigma` be a permutation of cycle type `\\mu` and let `\\mu^k`
        be the cycle type of `\\sigma^k`. Then,

        .. MATH::

            p_k \\{ p_\\mu/z_\\mu \\} = \\sum_{\\nu : \\nu^k = \\mu } p_{\\nu}/z_{\\nu}

        Since `(p_\\mu/z_\\mu)_{\\mu}` is a basis for the symmetric
        functions, these four formulas define the symmetric function
        operation `f \\{ g \\}` for any symmetric functions `f` and `g`
        (where `f` has constant term `0`) by expanding `f` in the
        power sum basis and `g` in the dual basis `p_\\mu/z_\\mu`.

        .. SEEALSO:: :meth:`itensor`, :func:`~sage.combinat.partition.partition_power`,
            :meth:`plethysm`

        This operation admits a representation-theoretic interpretation
        in the case where `f` is a Schur function `s_\\lambda` and
        `g` is a homogeneous degree `n` symmetric function with
        nonnegative integral coefficients in the Schur basis.
        The symmetric function `f \\{ g \\}` is the Frobenius
        image of the `S_n`-representation constructed as follows.

        The assumptions on `g` imply that `g` is the Frobenius image of a
        representation `\\rho` of the symmetric group `S_n`:

        .. MATH::

            \\rho : S_n \\to GL_N.

        If the degree `N` of this representation is greater than or equal
        to the number of parts of `\\lambda`, then `f`, which denotes `s_\\lambda`,
        corresponds to the character of some irreducible `GL_N`-representation, say

        .. MATH::

            \\sigma : GL_N \\to GL_M.

        The composition `\\sigma \\circ \\rho : S_n \\to GL_M` is a representation
        of `S_n` whose Frobenius image is precisely `f \\{ g \\}`.

        If `N` is less than the number of parts of `\\lambda`,
        then `f \\{ g \\}` is `0` by definition.

        When `f` is a symmetric function with constant term `\\neq 0`, the
        inner plethysm `f \\{ g \\}` isn't well-defined in the ring of
        symmetric functions. Indeed, it is not clear how to define
        `1 \\{ g \\}`. The most sensible way to get around this probably is
        defining it as the infinite sum `h_0 + h_1 + h_2 + \\cdots` (where
        `h_i` means the `i`-th complete homogeneous symmetric function)
        in the completion of this ring with respect to its grading. This is
        how [SchaThi1994]_ defines `1 \\{ g \\}`. The present method,
        however, sets it to be the sum of `h_i` over all `i` for which the
        `i`-th homogeneous component of `g` is nonzero. This is rather a
        hack than a reasonable definition. Use with caution!

        .. NOTE::

            If a symmetric function `g` is written in the form
            `g = g_0 + g_1 + g_2 + \\cdots` with each `g_i` homogeneous
            of degree `i`, then
            `f \\{ g \\} = f \\{ g_0 \\} + f \\{ g_1 \\} + f \\{ g_2 \\} + \\cdots`
            for every `f` with constant term `0`. But in general, inner
            plethysm is not linear in the second variable.

        REFERENCES:

        .. [King] King, R. Branching rules for `GL_m \\supset \\Sigma_n`
           and the evaluation of inner plethysms.
           J. Math. Phys. 15, 258 (1974) :doi:`10.1063/1.1666632`

        .. [SchaThi1994] Thomas Scharf, Jean-Yves Thibon.
           *A Hopf-algebra approach to inner plethysm*.
           Advances in Mathematics 104 (1994), pp. 30-58.
           ftp://ftp.mathe2.uni-bayreuth.de/axel/papers/scharf:a_hopf_algebra_approach_to_inner_plethysm.ps.gz

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the same
          base ring as ``self``

        OUTPUT: an element of symmetric functions in the parent of ``self``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.schur()
            sage: p = Sym.power()
            sage: h = Sym.complete()
            sage: s([2,1]).inner_plethysm(s([1,1,1]))
            0
            sage: s([2]).inner_plethysm(s([2,1]))
            s[2, 1] + s[3]
            sage: s([1,1]).inner_plethysm(s([2,1]))
            s[1, 1, 1]
            sage: s[2,1].inner_tensor(s[2,1])
            s[1, 1, 1] + s[2, 1] + s[3]

        ::

            sage: f = s([2,1]) + 2*s([3,1])
            sage: f.itensor(f)
            s[1, 1, 1] + s[2, 1] + 4*s[2, 1, 1] + 4*s[2, 2] + s[3] + 4*s[3, 1] + 4*s[4]
            sage: s( h([1,1]).inner_plethysm(f) )
            s[1, 1, 1] + s[2, 1] + 4*s[2, 1, 1] + 4*s[2, 2] + s[3] + 4*s[3, 1] + 4*s[4]

        ::

            sage: s([]).inner_plethysm(s([1,1]) + 2*s([2,1])+s([3]))
            s[2] + s[3]
            sage: [s([]).inner_plethysm(s(la)) for la in Partitions(4)]
            [s[4], s[4], s[4], s[4], s[4]]
            sage: s([3]).inner_plethysm(s([]))
            s[]
            sage: s[1,1,1,1].inner_plethysm(s[2,1])
            0
            sage: s[1,1,1,1].inner_plethysm(2*s[2,1])
            s[3]

        ::

            sage: p[3].inner_plethysm(p[3])
            0
            sage: p[3,3].inner_plethysm(p[3])
            0
            sage: p[3].inner_plethysm(p[1,1,1])
            p[1, 1, 1] + 2*p[3]
            sage: p[4].inner_plethysm(p[1,1,1,1]/24)
            1/24*p[1, 1, 1, 1] + 1/4*p[2, 1, 1] + 1/8*p[2, 2] + 1/4*p[4]
            sage: p[3,3].inner_plethysm(p[1,1,1])
            6*p[1, 1, 1] + 12*p[3]

        TESTS::

            sage: s(0).inner_plethysm(s(0))
            0
            sage: s(1).inner_plethysm(s(0))
            0
            sage: s(0).inner_plethysm(s(1))
            0
            sage: s(1).inner_plethysm(s(1))
            s[]
            sage: s(2).inner_plethysm(s(1))
            2*s[]
            sage: s(1).inner_plethysm(s(2))
            s[]
        """
    def omega(self):
        """
        Return the image of ``self`` under the omega automorphism.

        The *omega automorphism* is defined to be the unique algebra
        endomorphism `\\omega` of the ring of symmetric functions that
        satisfies `\\omega(e_k) = h_k` for all positive integers `k`
        (where `e_k` stands for the `k`-th elementary symmetric
        function, and `h_k` stands for the `k`-th complete homogeneous
        symmetric function). It furthermore is a Hopf algebra
        endomorphism and an involution, and it is also known as the
        *omega involution*. It sends the power-sum symmetric function
        `p_k` to `(-1)^{k-1} p_k` for every positive integer `k`.

        The images of some bases under the omega automorphism are given by

        .. MATH::

            \\omega(e_{\\lambda}) = h_{\\lambda}, \\qquad
            \\omega(h_{\\lambda}) = e_{\\lambda}, \\qquad
            \\omega(p_{\\lambda}) = (-1)^{|\\lambda| - \\ell(\\lambda)}
            p_{\\lambda}, \\qquad
            \\omega(s_{\\lambda}) = s_{\\lambda^{\\prime}},

        where `\\lambda` is any partition, where `\\ell(\\lambda)` denotes
        the length (:meth:`~sage.combinat.partition.Partition.length`)
        of the partition `\\lambda`, where `\\lambda^{\\prime}` denotes the
        conjugate partition
        (:meth:`~sage.combinat.partition.Partition.conjugate`) of
        `\\lambda`, and where the usual notations for bases are used
        (`e` = elementary, `h` = complete homogeneous, `p` = powersum,
        `s` = Schur).

        The default implementation converts to the Schur basis, then
        performs the automorphism and changes back.

        :meth:`omega_involution()` is a synonym for the :meth:`omega()` method.

        EXAMPLES::

            sage: J = SymmetricFunctions(QQ).jack(t=1).P()
            sage: a = J([2,1]) + J([1,1,1])
            sage: a.omega()
            JackP[2, 1] + JackP[3]
            sage: J(0).omega()
            0
            sage: J(1).omega()
            JackP[]

        The forgotten symmetric functions are the images of the monomial
        symmetric functions under omega::

            sage: Sym = SymmetricFunctions(ZZ)
            sage: m = Sym.m()
            sage: f = Sym.f()
            sage: all( f(lam) == m(lam).omega() for lam in Partitions(3) )
            True
            sage: all( m(lam) == f(lam).omega() for lam in Partitions(3) )
            True
        """
    omega_involution = omega
    def theta(self, a):
        """
        Return the image of ``self`` under the theta endomorphism which sends
        `p_k` to `a \\cdot p_k` for every positive integer `k`.

        In general, this is well-defined outside of the powersum basis only
        if the base ring is a `\\QQ`-algebra.

        INPUT:

        - ``a`` -- an element of the base ring

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([2,1]).theta(2)
            2*s[1, 1, 1] + 6*s[2, 1] + 2*s[3]
            sage: p = SymmetricFunctions(QQ).p()
            sage: p([2]).theta(2)
            2*p[2]
            sage: p(0).theta(2)
            0
            sage: p(1).theta(2)
            p[]
        """
    def theta_qt(self, q=None, t=None):
        """
        Return the image of ``self`` under the `q,t`-deformed theta
        endomorphism which sends `p_k` to `\\frac{1-q^k}{1-t^k} \\cdot p_k`
        for all positive integers `k`.

        In general, this is well-defined outside of the powersum basis only
        if the base ring is a `\\QQ`-algebra.

        INPUT:

        - ``q``, ``t`` -- parameters (default: ``None``, in which case 'q'
          and 't' are used)

        EXAMPLES::

            sage: QQqt = QQ['q,t'].fraction_field()
            sage: q,t = QQqt.gens()
            sage: p = SymmetricFunctions(QQqt).p()
            sage: p([2]).theta_qt(q,t)
            -((q^2-1)/(-t^2+1))*p[2]
            sage: p([2,1]).theta_qt(q,t)
            ((q^3-q^2-q+1)/(t^3-t^2-t+1))*p[2, 1]
            sage: p(0).theta_qt(q=1,t=3)
            0
            sage: p([2,1]).theta_qt(q=2,t=3)
            3/16*p[2, 1]
            sage: s = p.realization_of().schur()
            sage: s([3]).theta_qt(q=0)*(1-t)*(1-t^2)*(1-t^3)
            t^3*s[1, 1, 1] + (t^2+t)*s[2, 1] + s[3]
            sage: p(1).theta_qt()
            p[]
        """
    def omega_qt(self, q=None, t=None):
        """
        Return the image of ``self`` under the `q,t`-deformed omega
        automorphism which sends `p_k` to
        `(-1)^{k-1} \\cdot \\frac{1-q^k}{1-t^k} \\cdot p_k` for all positive
        integers `k`.

        In general, this is well-defined outside of the powersum basis only
        if the base ring is a `\\QQ`-algebra.

        If `q = t`, then this is the omega automorphism (:meth:`omega`).

        INPUT:

        - ``q``, ``t`` -- parameters (default: ``None``, in which case
          ``'q'`` and ``'t'`` are used)

        EXAMPLES::

            sage: QQqt = QQ['q,t'].fraction_field()
            sage: q,t = QQqt.gens()
            sage: p = SymmetricFunctions(QQqt).p()
            sage: p[5].omega_qt()
            -((q^5-1)/(-t^5+1))*p[5]
            sage: p[5].omega_qt(q,t)
            -((q^5-1)/(-t^5+1))*p[5]
            sage: p([2]).omega_qt(q,t)
            ((q^2-1)/(-t^2+1))*p[2]
            sage: p([2,1]).omega_qt(q,t)
            -((q^3-q^2-q+1)/(t^3-t^2-t+1))*p[2, 1]
            sage: p([3,2]).omega_qt(5,q)
            -(2976/(q^5-q^3-q^2+1))*p[3, 2]
            sage: p(0).omega_qt()
            0
            sage: p(1).omega_qt()
            p[]
            sage: H = SymmetricFunctions(QQqt).macdonald().H()
            sage: H([1,1]).omega_qt()
            ((2*q^2-2*q*t-2*q+2*t)/(t^3-t^2-t+1))*McdH[1, 1] + ((q-1)/(t-1))*McdH[2]
            sage: H([1,1]).omega_qt(q,t)
            ((2*q^2-2*q*t-2*q+2*t)/(t^3-t^2-t+1))*McdH[1, 1] + ((q-1)/(t-1))*McdH[2]
            sage: H([1,1]).omega_qt(t,q)
            -((t^3-t^2-t+1)/(-q^3+q^2+q-1))*McdH[2]
            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: S = Sym.macdonald().S()
            sage: S([1,1]).omega_qt()
            ((q^2-q*t-q+t)/(t^3-t^2-t+1))*McdS[1, 1] - ((q^2*t-q*t-q+1)/(-t^3+t^2+t-1))*McdS[2]
            sage: s = Sym.schur()
            sage: s(S([1,1]).omega_qt())
            s[2]
        """
    def itensor(self, x):
        '''
        Return the internal (tensor) product of ``self`` and ``x`` in the
        basis of ``self``.

        The internal tensor product can be defined as the linear extension
        of the definition on power sums
        `p_{\\lambda} \\ast p_{\\mu} = \\delta_{\\lambda,\\mu} z_{\\lambda}
        p_{\\lambda}`, where `z_{\\lambda} = (1^{r_1} r_1!) (2^{r_2} r_2!)
        \\cdots` for `\\lambda = (1^{r_1} 2^{r_2} \\cdots )` and where `\\ast`
        denotes the internal tensor product.
        The internal tensor product is also known as the Kronecker product,
        or as the second multiplication on the ring of symmetric functions.

        Note that the internal product of any two homogeneous symmetric
        functions of equal degrees is a homogeneous symmetric function of the
        same degree. On the other hand, the internal product of two homogeneous
        symmetric functions of distinct degrees is `0`.

        .. NOTE::

            The internal product is sometimes referred to as "inner product"
            in the literature, but unfortunately this name is shared by a
            different operation, namely the Hall inner product
            (see :meth:`scalar`).

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the
          same base ring as ``self``

        OUTPUT:

        - the internal product of ``self`` with ``x`` (an element of the
          ring of symmetric functions in the same basis as ``self``)

        The methods :meth:`itensor`, :meth:`internal_product`,
        :meth:`kronecker_product`, :meth:`inner_tensor` are all
        synonyms.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: a = s([2,1])
            sage: b = s([3])
            sage: a.itensor(b)
            s[2, 1]
            sage: c = s([3,2,1])
            sage: c.itensor(c)
            s[1, 1, 1, 1, 1, 1] + 2*s[2, 1, 1, 1, 1] + 3*s[2, 2, 1, 1] + 2*s[2, 2, 2]
             + 4*s[3, 1, 1, 1] + 5*s[3, 2, 1] + 2*s[3, 3] + 4*s[4, 1, 1]
             + 3*s[4, 2] + 2*s[5, 1] + s[6]

        There are few quantitative results pertaining to Kronecker products
        in general, which makes their computation so difficult. Let us test
        a few of them in different bases.

        The Kronecker product of any homogeneous symmetric function `f` of
        degree `n` with the `n`-th complete homogeneous symmetric function
        ``h[n]`` (a.k.a. ``s[n]``) is `f`::

            sage: h = SymmetricFunctions(ZZ).h()
            sage: all( h([5]).itensor(h(p)) == h(p) for p in Partitions(5) )
            True

        The Kronecker product of a Schur function `s_{\\lambda}` with the `n`-th
        elementary symmetric function ``e[n]``, where `n = \\left| \\lambda
        \\right|`, is `s_{\\lambda\'}` (where `\\lambda\'` is the conjugate
        partition of `\\lambda`)::

            sage: F = CyclotomicField(12)
            sage: s = SymmetricFunctions(F).s()
            sage: e = SymmetricFunctions(F).e()
            sage: all( e([5]).itensor(s(p)) == s(p.conjugate()) for p in Partitions(5) )
            True

        The Kronecker product is commutative::

            sage: e = SymmetricFunctions(FiniteField(19)).e()
            sage: m = SymmetricFunctions(FiniteField(19)).m()
            sage: all( all( e(p).itensor(m(q)) == m(q).itensor(e(p)) for q in Partitions(4) )
            ....:      for p in Partitions(4) )
            True

            sage: F = FractionField(QQ[\'q\',\'t\'])
            sage: mq = SymmetricFunctions(F).macdonald().Q()
            sage: mh = SymmetricFunctions(F).macdonald().H()
            sage: all( all( mq(p).itensor(mh(r)) == mh(r).itensor(mq(p))   # long time
            ....:           for r in Partitions(4) )
            ....:      for p in Partitions(3) )
            True

        Let us check (on examples) Proposition 5.2 of Gelfand, Krob, Lascoux, Leclerc,
        Retakh, Thibon, "Noncommutative symmetric functions", :arxiv:`hep-th/9407124`, for
        `r = 2`::

            sage: e = SymmetricFunctions(FiniteField(29)).e()
            sage: s = SymmetricFunctions(FiniteField(29)).s()
            sage: m = SymmetricFunctions(FiniteField(29)).m()
            sage: def tensor_copr(u, v, w):  # computes \\mu ((u \\otimes v) * \\Delta(w)) with
            ....:                            # * meaning Kronecker product and \\mu meaning the
            ....:                            # usual multiplication.
            ....:     result = w.parent().zero()
            ....:     for partition_pair, coeff in w.coproduct():
            ....:         result += coeff * w.parent()(u).itensor(partition_pair[0]) * w.parent()(v).itensor(partition_pair[1])
            ....:     return result
            sage: all( all( all( tensor_copr(e[u], s[v], m[w])   # long time
            ....:                == (e[u] * s[v]).itensor(m[w])
            ....:                for w in Partitions(5) )
            ....:           for v in Partitions(2) )
            ....:      for u in Partitions(3) )
            True

        Some examples from Briand, Orellana, Rosas, "The stability of the Kronecker
        products of Schur functions." :arxiv:`0907.4652`::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: s[2,2].itensor(s[2,2])
            s[1, 1, 1, 1] + s[2, 2] + s[4]
            sage: s[3,2].itensor(s[3,2])
            s[2, 1, 1, 1] + s[2, 2, 1] + s[3, 1, 1] + s[3, 2] + s[4, 1] + s[5]
            sage: s[4,2].itensor(s[4,2])
            s[2, 2, 2] + s[3, 1, 1, 1] + 2*s[3, 2, 1] + s[4, 1, 1] + 2*s[4, 2] + s[5, 1] + s[6]

        An example from p. 220 of Thibon, "Hopf algebras of symmetric functions
        and tensor products of symmetric group representations", International
        Journal of Algebra and Computation, 1991::

            sage: s = SymmetricFunctions(QQbar).s()
            sage: s[2,1].itensor(s[2,1])
            s[1, 1, 1] + s[2, 1] + s[3]

        TESTS::

            sage: s = SymmetricFunctions(QQ).s()
            sage: a = s([8,8])
            sage: a.itensor(a) # long time
            s[4, 4, 4, 4] + s[5, 5, 3, 3] + s[5, 5, 5, 1] + s[6, 4, 4, 2]
             + s[6, 6, 2, 2] + s[6, 6, 4] + s[7, 3, 3, 3] + s[7, 5, 3, 1]
             + s[7, 7, 1, 1] + s[8, 4, 2, 2] + s[8, 4, 4] + s[8, 6, 2]
             + s[8, 8] + s[9, 3, 3, 1] + s[9, 5, 1, 1] + s[10, 2, 2, 2]
             + s[10, 4, 2] + s[10, 6] + s[11, 3, 1, 1] + s[12, 2, 2]
             + s[12, 4] + s[13, 1, 1, 1] + s[14, 2] + s[16]
            sage: s[8].itensor(s[7])
            0
            sage: s(0).itensor(s(0))
            0
            sage: s(1).itensor(s(0))
            0
            sage: s(0).itensor(s(1))
            0
            sage: s(1).itensor(s(1))
            s[]

        Same over the ring of integers::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: a = s([8,8])
            sage: a.itensor(a) # long time
            s[4, 4, 4, 4] + s[5, 5, 3, 3] + s[5, 5, 5, 1] + s[6, 4, 4, 2]
             + s[6, 6, 2, 2] + s[6, 6, 4] + s[7, 3, 3, 3] + s[7, 5, 3, 1]
             + s[7, 7, 1, 1] + s[8, 4, 2, 2] + s[8, 4, 4] + s[8, 6, 2]
             + s[8, 8] + s[9, 3, 3, 1] + s[9, 5, 1, 1] + s[10, 2, 2, 2]
             + s[10, 4, 2] + s[10, 6] + s[11, 3, 1, 1] + s[12, 2, 2]
             + s[12, 4] + s[13, 1, 1, 1] + s[14, 2] + s[16]
            sage: s[8].itensor(s[7])
            0
            sage: s(0).itensor(s(0))
            0
            sage: s(1).itensor(s(0))
            0
            sage: s(0).itensor(s(1))
            0
            sage: s(1).itensor(s(1))
            s[]

        Theorem 2.1 in Bessenrodt, van Willigenburg, :arxiv:`1105.3170v2`::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: all( all( max( r[0] for r in s(p).itensor(s(q)).monomial_coefficients().keys() )
            ....:           == sum( min(p[i], q.get_part(i)) for i in range(len(p)) )
            ....:           for p in Partitions(4) )
            ....:      for q in Partitions(4) )
            True
            sage: all( all( max( len(r) for r in s(p).itensor(s(q)).monomial_coefficients().keys() )
            ....:           == sum( min(p[i], q.conjugate().get_part(i)) for i in range(len(p)) )
            ....:           for p in Partitions(4) )
            ....:      for q in Partitions(4) )
            True

        Check that the basis and ground ring of ``self`` are preserved::

            sage: F = CyclotomicField(12)
            sage: s = SymmetricFunctions(F).s()
            sage: e = SymmetricFunctions(F).e()
            sage: e[3].itensor(s[3])
            e[3]
            sage: s[3].itensor(e[3])
            s[1, 1, 1]
            sage: parent(e[3].itensor(s[3]))
            Symmetric Functions over Cyclotomic Field of order 12 and degree 4 in the elementary basis
            sage: parent(s[3].itensor(e[3]))
            Symmetric Functions over Cyclotomic Field of order 12 and degree 4 in the Schur basis

        .. NOTE::

            The currently existing implementation of this function is
            technically unsatisfactory. It distinguishes the case when the
            base ring is a `\\QQ`-algebra (in which case the Kronecker product
            can be easily computed using the power sum basis) from the case
            where it isn\'t. In the latter, it does a computation using
            universal coefficients, again distinguishing the case when it is
            able to compute the "corresponding" basis of the symmetric function
            algebra over `\\QQ` (using the ``corresponding_basis_over`` hack)
            from the case when it isn\'t (in which case it transforms everything
            into the Schur basis, which is slow).
        '''
    internal_product = itensor
    kronecker_product = itensor
    inner_tensor = itensor
    def reduced_kronecker_product(self, x):
        '''
        Return the reduced Kronecker product of ``self`` and ``x`` in the
        basis of ``self``.

        The reduced Kronecker product is a bilinear map mapping two
        symmetric functions to another, not necessarily preserving degree.
        It can be defined as follows: Let `*` denote the Kronecker product
        (:meth:`itensor`) on the space of symmetric functions. For any
        partitions `\\alpha`, `\\beta`, `\\gamma`, let
        `g^{\\gamma}_{\\alpha, \\beta}` denote the coefficient of the Schur
        function `s_{\\gamma}` in the Kronecker product
        `s_{\\alpha} * s_{\\beta}` (this is called a Kronecker coefficient).
        For every partition
        `\\lambda = (\\lambda_1, \\lambda_2, \\lambda_3, \\ldots)`
        and every integer `n > \\left| \\lambda \\right| + \\lambda_1`, let
        `\\lambda[n]` denote the `n`-completion of `\\lambda` (this is the
        partition
        `(n - \\left| \\lambda \\right|, \\lambda_1, \\lambda_2, \\lambda_3, \\ldots)`;
        see :meth:`~sage.combinat.partition.Partition.t_completion`).
        Then, Theorem 1.2 of [BOR2009]_ shows that for any partitions
        `\\alpha` and `\\beta` and every integer
        `n \\geq \\left|\\alpha\\right| + \\left|\\beta\\right| + \\alpha_1 + \\beta_1`,
        we can write the Kronecker product `s_{\\alpha[n]} * s_{\\beta[n]}`
        in the form

        .. MATH::

            s_{\\alpha[n]} * s_{\\beta[n]} = \\sum_{\\gamma} g^{\\gamma[n]}_{\\alpha[n], \\beta[n]} s_{\\gamma[n]}

        with `\\gamma` ranging over all partitions. The
        coefficients `g^{\\gamma[n]}_{\\alpha[n], \\beta[n]}`
        are independent on `n`. These coefficients
        `g^{\\gamma[n]}_{\\alpha[n], \\beta[n]}` are denoted by
        `\\overline{g}^{\\gamma}_{\\alpha, \\beta}`, and the symmetric
        function

        .. MATH::

            \\sum_{\\gamma} \\overline{g}^{\\gamma}_{\\alpha, \\beta} s_{\\gamma}

        is said to be the *reduced Kronecker product* of `s_{\\alpha}` and
        `s_{\\beta}`. By bilinearity, this extends to a definition of a
        reduced Kronecker product of any two symmetric functions.

        The definition of the reduced Kronecker product goes back to
        Murnaghan, and has recently been studied in [BOR2009]_, [BdVO2012]_
        and other places (our notation
        `\\overline{g}^{\\gamma}_{\\alpha, \\beta}` appears in these two
        sources).

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the
          same base ring as ``self``

        OUTPUT:

        - the reduced Kronecker product of ``self`` with ``x`` (an element
          of the ring of symmetric functions in the same basis as
          ``self``)

        EXAMPLES:

        The example from page 2 of [BOR2009]_::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.schur()
            sage: s[2].reduced_kronecker_product(s[2])
            s[] + s[1] + s[1, 1] + s[1, 1, 1] + 2*s[2] + 2*s[2, 1] + s[2, 2] + s[3] + s[3, 1] + s[4]

        Taking the reduced Kronecker product with `1 = s_{\\emptyset}`
        is the identity map on the ring of symmetric functions::

            sage: all( s[Partition([])].reduced_kronecker_product(s[lam])
            ....:      == s[lam] for i in range(4)
            ....:      for lam in Partitions(i) )
            True

        While reduced Kronecker products are hard to compute in general,
        there is a rule for taking reduced Kronecker products with
        `s_1`. Namely, for every partition `\\lambda`, the reduced
        Kronecker product of `s_{\\lambda}` with `s_1` is
        `\\sum_{\\mu} a_{\\mu} s_{\\mu}`, where the sum runs over all
        partitions `\\mu`, and the coefficient `a_{\\mu}` is defined as the
        number of ways to obtain `\\mu` from `\\lambda` by one of the
        following three operations:

        - Add an addable cell
          (:meth:`~sage.combinat.partition.Partition.addable_cells`) to
          `\\lambda`.
        - Remove a removable cell
          (:meth:`~sage.combinat.partition.Partition.removable_cells`)
          from `\\lambda`.
        - First remove a removable cell from `\\lambda`, then add an
          addable cell to the resulting Young diagram.

        This is, in fact, Proposition 5.15 of [CO2010]_ in an elementary
        wording. We check this for partitions of size `\\leq 4`::

            sage: def mults1(lam):
            ....:     # Reduced Kronecker multiplication by s[1], according
            ....:     # to [CO2010]_.
            ....:     res = s.zero()
            ....:     for mu in lam.up_list():
            ....:         res += s(mu)
            ....:     for mu in lam.down_list():
            ....:         res += s(mu)
            ....:         for nu in mu.up_list():
            ....:             res += s(nu)
            ....:     return res
            sage: all( mults1(lam) == s[1].reduced_kronecker_product(s[lam])
            ....:      for i in range(5) for lam in Partitions(i) )
            True

        Here is the example on page 3 of Christian Gutschwager\'s
        :arxiv:`0912.4411v3`::

            sage: s[1,1].reduced_kronecker_product(s[2])
            s[1] + 2*s[1, 1] + s[1, 1, 1] + s[2] + 2*s[2, 1] + s[2, 1, 1] + s[3] + s[3, 1]

        Example 39 from F. D. Murnaghan, "The analysis of the Kronecker
        product of irreducible representations of the symmetric group",
        American Journal of Mathematics, Vol. 60, No. 3, Jul. 1938::

            sage: s[3].reduced_kronecker_product(s[2,1])
            s[1] + 2*s[1, 1] + 2*s[1, 1, 1] + s[1, 1, 1, 1] + 2*s[2] + 5*s[2, 1] + 4*s[2, 1, 1]
            + s[2, 1, 1, 1] + 3*s[2, 2] + 2*s[2, 2, 1] + 2*s[3] + 5*s[3, 1] + 3*s[3, 1, 1]
            + 3*s[3, 2] + s[3, 2, 1] + 2*s[4] + 3*s[4, 1] + s[4, 1, 1] + s[4, 2] + s[5]
            + s[5, 1]

        TESTS::

            sage: h = SymmetricFunctions(QQ).h()
            sage: (2*h([])).reduced_kronecker_product(3*h([]))
            6*h[]

        Different bases and base rings::

            sage: h = SymmetricFunctions(ZZ).h()
            sage: e = SymmetricFunctions(ZZ).e()
            sage: h(e[2].reduced_kronecker_product(h[2]))
            h[1] + 2*h[1, 1] + h[1, 1, 1] - h[2] + h[2, 1, 1] - h[2, 2]

            sage: F = CyclotomicField(12)
            sage: s = SymmetricFunctions(F).s()
            sage: e = SymmetricFunctions(F).e()
            sage: v = e[2].reduced_kronecker_product(e[2]); v
            e[] + e[1] + 2*e[1, 1] + e[1, 1, 1] + (-1)*e[2] + e[2, 2]
            sage: parent(v)
            Symmetric Functions over Cyclotomic Field of order 12 and degree 4 in the elementary basis

            sage: s = SymmetricFunctions(ZZ).s()
            sage: v = s[1].reduced_kronecker_product(s[1]); parent(v)
            Symmetric Functions over Integer Ring in the Schur basis

        .. TODO::

            This implementation of the reduced Kronecker product is
            painfully slow.
        '''
    def left_padded_kronecker_product(self, x):
        """
        Return the left-padded Kronecker product of ``self`` and ``x`` in
        the basis of ``self``.

        The left-padded Kronecker product is a bilinear map mapping two
        symmetric functions to another, not necessarily preserving degree.
        It can be defined as follows: Let `*` denote the Kronecker product
        (:meth:`itensor`) on the space of symmetric functions. For any
        partitions `\\alpha`, `\\beta`, `\\gamma`, let
        `g^{\\gamma}_{\\alpha, \\beta}` denote the coefficient of the
        complete homogeneous symmetric function `h_{\\gamma}` in the
        Kronecker product `h_{\\alpha} * h_{\\beta}`.
        For every partition
        `\\lambda = (\\lambda_1, \\lambda_2, \\lambda_3, \\ldots)`
        and every integer `n > \\left| \\lambda \\right| + \\lambda_1`, let
        `\\lambda[n]` denote the `n`-completion of `\\lambda` (this is the
        partition
        `(n - \\left| \\lambda \\right|, \\lambda_1, \\lambda_2, \\lambda_3, \\ldots)`;
        see :meth:`~sage.combinat.partition.Partition.t_completion`).
        Then, for any partitions `\\alpha` and `\\beta` and every integer
        `n \\geq \\left|\\alpha\\right| + \\left|\\beta\\right| + \\alpha_1 + \\beta_1`,
        we can write the Kronecker product `h_{\\alpha[n]} * h_{\\beta[n]}`
        in the form

        .. MATH::

            h_{\\alpha[n]} * h_{\\beta[n]} = \\sum_{\\gamma}
            g^{\\gamma[n]}_{\\alpha[n], \\beta[n]} h_{\\gamma[n]}

        with `\\gamma` ranging over all partitions. The
        coefficients `g^{\\gamma[n]}_{\\alpha[n], \\beta[n]}`
        are independent on `n`. These coefficients
        `g^{\\gamma[n]}_{\\alpha[n], \\beta[n]}` are denoted by
        `\\overline{g}^{\\gamma}_{\\alpha, \\beta}`, and the symmetric
        function

        .. MATH::

            \\sum_{\\gamma} \\overline{g}^{\\gamma}_{\\alpha, \\beta} h_{\\gamma}

        is said to be the *left-padded Kronecker product* of `h_{\\alpha}`
        and `h_{\\beta}`. By bilinearity, this extends to a definition of a
        left-padded Kronecker product of any two symmetric functions.

        This notion of left-padded Kronecker product can be lifted to the
        non-commutative symmetric functions
        (:meth:`~sage.combinat.ncsf_qsym.ncsf.NonCommutativeSymmetricFunctions.Bases.ElementMethods.left_padded_kronecker_product`).

        .. WARNING::

            Do not mistake this product for the reduced Kronecker product
            (:meth:`reduced_kronecker_product`), which uses the Schur
            functions instead of the complete homogeneous functions in
            its definition.

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the
          same base ring as ``self``

        OUTPUT:

        - the left-padded Kronecker product of ``self`` with ``x`` (an
          element of the ring of symmetric functions in the same basis
          as ``self``)

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: h = Sym.h()
            sage: h[2,1].left_padded_kronecker_product(h[3])
            h[1, 1, 1, 1] + h[2, 1] + h[2, 1, 1] + h[2, 1, 1, 1] + h[2, 2, 1] + h[3, 2, 1]
            sage: h[2,1].left_padded_kronecker_product(h[1])
            h[1, 1, 1] + h[2, 1] + h[2, 1, 1]
            sage: h[1].left_padded_kronecker_product(h[2,1])
            h[1, 1, 1] + h[2, 1] + h[2, 1, 1]
            sage: h[1,1].left_padded_kronecker_product(h[2])
            h[1, 1] + 2*h[1, 1, 1] + h[2, 1, 1]
            sage: h[1].left_padded_kronecker_product(h[2,1,1])
            h[1, 1, 1, 1] + 2*h[2, 1, 1] + h[2, 1, 1, 1]
            sage: h[2].left_padded_kronecker_product(h[3])
            h[2, 1] + h[2, 1, 1] + h[3, 2]

        Taking the left-padded Kronecker product with `1 = h_{\\emptyset}`
        is the identity map on the ring of symmetric functions::

            sage: all( h[Partition([])].left_padded_kronecker_product(h[lam])
            ....:      == h[lam] for i in range(4)
            ....:      for lam in Partitions(i) )
            True

        Here is a rule for the left-padded Kronecker product of `h_1`
        (this is the same as `h_{(1)}`) with any complete homogeneous
        function: Let `\\lambda` be a partition. Then, the left-padded
        Kronecker product of `h_1` and `h_{\\lambda}` is
        `\\sum_{\\mu} a_{\\mu} h_{\\mu}`, where the sum runs over all
        partitions `\\mu`, and the coefficient `a_{\\mu}` is defined as the
        number of ways to obtain `\\mu` from `\\lambda` by one of the
        following two operations:

        - Insert a `1` into `\\lambda`.
        - Subtract `1` from one of the entries of `\\lambda` (and remove
          the entry if it thus becomes `0`), and insert a `1` into
          `\\lambda`.

        We check this for partitions of size `\\leq 4`::

            sage: def mults1(I):
            ....:     # Left-padded Kronecker multiplication by h[1].
            ....:     res = h[I[:] + [1]]
            ....:     for k in range(len(I)):
            ....:         I2 = I[:]
            ....:         if I2[k] == 1:
            ....:             I2 = I2[:k] + I2[k+1:]
            ....:         else:
            ....:             I2[k] -= 1
            ....:         res += h[sorted(I2 + [1], reverse=True)]
            ....:     return res
            sage: all( mults1(I) == h[1].left_padded_kronecker_product(h[I])
            ....:                == h[I].left_padded_kronecker_product(h[1])
            ....:      for i in range(5) for I in Partitions(i) )
            True

        The left-padded Kronecker product is commutative::

            sage: all( h[lam].left_padded_kronecker_product(h[mu])
            ....:      == h[mu].left_padded_kronecker_product(h[lam])
            ....:      for lam in Partitions(3) for mu in Partitions(3) )
            True

        TESTS::

            sage: h = SymmetricFunctions(QQ).h()
            sage: (2*h([])).left_padded_kronecker_product(3*h([]))
            6*h[]

        Different bases and base rings::

            sage: h = SymmetricFunctions(ZZ).h()
            sage: e = SymmetricFunctions(ZZ).e()
            sage: h(e[2].left_padded_kronecker_product(h[2]))
            h[1, 1] + h[1, 1, 1] - h[2] + h[2, 1, 1] - h[2, 2]

            sage: F = CyclotomicField(12)
            sage: s = SymmetricFunctions(F).s()
            sage: e = SymmetricFunctions(F).e()
            sage: v = e[2].left_padded_kronecker_product(e[2]); v
            e[1, 1] + e[1, 1, 1] + (-1)*e[2] + e[2, 2]
            sage: parent(v)
            Symmetric Functions over Cyclotomic Field of order 12 and degree 4 in the elementary basis

            sage: s = SymmetricFunctions(ZZ).s()
            sage: v = s[1].left_padded_kronecker_product(s[1]); parent(v)
            Symmetric Functions over Integer Ring in the Schur basis
        """
    def internal_coproduct(self):
        """
        Return the inner coproduct of ``self`` in the basis of ``self``.

        The inner coproduct (also known as the Kronecker coproduct, as the
        internal coproduct, or as the second comultiplication on the ring of
        symmetric functions) is a ring homomorphism `\\Delta^\\times` from the
        ring of symmetric functions to the tensor product (over the base
        ring) of this ring with itself. It is uniquely characterized by the
        formula

        .. MATH::

            \\Delta^{\\times}(h_n) = \\sum_{\\lambda \\vdash n} s_{\\lambda}
            \\otimes s_{\\lambda} = \\sum_{\\lambda \\vdash n} h_{\\lambda} \\otimes
            m_{\\lambda} = \\sum_{\\lambda \\vdash n} m_{\\lambda} \\otimes
            h_{\\lambda},

        where `\\lambda \\vdash n` means `\\lambda` is a partition of `n`, and
        `n` is any nonnegative integer. It also satisfies

        .. MATH::

            \\Delta^\\times (p_n) = p_n \\otimes p_n

        for any positive integer `n`. If the base ring is a `\\QQ`-algebra, it
        also satisfies

        .. MATH::

            \\Delta^{\\times}(h_n) = \\sum_{\\lambda \\vdash n} z_{\\lambda}^{-1}
            p_{\\lambda} \\otimes p_{\\lambda},

        where

        .. MATH::

            z_{\\lambda} = \\prod_{i=1}^\\infty i^{m_i(\\lambda)} m_i(\\lambda)!

        with `m_i(\\lambda)` meaning the number of appearances of `i`
        in `\\lambda` (see :meth:`~sage.combinat.sf.sfa.zee`).

        The method :meth:`kronecker_coproduct` is a synonym of
        :meth:`internal_coproduct`.

        EXAMPLES::

            sage: s = SymmetricFunctions(ZZ).s()
            sage: a = s([2,1])
            sage: a.internal_coproduct()
            s[1, 1, 1] # s[2, 1] + s[2, 1] # s[1, 1, 1] + s[2, 1] # s[2, 1] + s[2, 1] # s[3] + s[3] # s[2, 1]

            sage: e = SymmetricFunctions(QQ).e()
            sage: b = e([2])
            sage: b.internal_coproduct()
            e[1, 1] # e[2] + e[2] # e[1, 1] - 2*e[2] # e[2]

        The internal coproduct is adjoint to the internal product with respect
        to the Hall inner product: Any three symmetric functions `f`, `g` and
        `h` satisfy `\\langle f * g, h \\rangle = \\sum_i \\langle f, h^{\\prime}_i
        \\rangle \\langle g, h^{\\prime\\prime}_i \\rangle`, where we write
        `\\Delta^{\\times}(h)` as `\\sum_i h^{\\prime}_i \\otimes
        h^{\\prime\\prime}_i`. Let us check this in degree `4`::

            sage: e = SymmetricFunctions(FiniteField(29)).e()
            sage: s = SymmetricFunctions(FiniteField(29)).s()
            sage: m = SymmetricFunctions(FiniteField(29)).m()
            sage: def tensor_incopr(f, g, h):  # computes \\sum_i \\left< f, h'_i \\right> \\left< g, h''_i \\right>
            ....:     result = h.base_ring().zero()
            ....:     for partition_pair, coeff in h.internal_coproduct():
            ....:         result += coeff * h.parent()(f).scalar(partition_pair[0]) * h.parent()(g).scalar(partition_pair[1])
            ....:     return result
            sage: all( all( all( tensor_incopr(e[u], s[v], m[w]) == (e[u].itensor(s[v])).scalar(m[w])  # long time (10s on sage.math, 2013)
            ....:                for w in Partitions(5) )
            ....:           for v in Partitions(2) )
            ....:      for u in Partitions(3) )
            True

        Let us check the formulas for `\\Delta^{\\times}(h_n)` and
        `\\Delta^{\\times}(p_n)` given in the description of this method::

            sage: e = SymmetricFunctions(QQ).e()
            sage: p = SymmetricFunctions(QQ).p()
            sage: h = SymmetricFunctions(QQ).h()
            sage: s = SymmetricFunctions(QQ).s()
            sage: all( s(h([n])).internal_coproduct() == sum([tensor([s(lam), s(lam)]) for lam in Partitions(n)])
            ....:      for n in range(6) )
            True
            sage: all( h([n]).internal_coproduct() == sum([tensor([h(lam), h(m(lam))]) for lam in Partitions(n)])
            ....:      for n in range(6) )
            True
            sage: all( factorial(n) * h([n]).internal_coproduct()
            ....:      == sum([lam.conjugacy_class_size() * tensor([h(p(lam)), h(p(lam))])
            ....:              for lam in Partitions(n)])
            ....:      for n in range(6) )
            True

        TESTS::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([]).internal_coproduct()
            s[] # s[]
        """
    kronecker_coproduct = internal_coproduct
    def arithmetic_product(self, x):
        '''
        Return the arithmetic product of ``self`` and ``x`` in the
        basis of ``self``.

        The arithmetic product is a binary operation `\\boxdot` on the
        ring of symmetric functions which is bilinear in its two
        arguments and satisfies

        .. MATH::

            p_{\\lambda} \\boxdot p_{\\mu} = \\prod\\limits_{i \\geq 1, j \\geq 1}
            p_{\\mathrm{lcm}(\\lambda_i, \\mu_j)}^{\\mathrm{gcd}(\\lambda_i, \\mu_j)}

        for any two partitions `\\lambda = (\\lambda_1, \\lambda_2, \\lambda_3,
        \\dots )` and `\\mu = (\\mu_1, \\mu_2, \\mu_3, \\dots )` (where `p_{\\nu}`
        denotes the power-sum symmetric function indexed by the partition
        `\\nu`, and `p_i` denotes the `i`-th power-sum symmetric function).
        This is enough to define the arithmetic product if the base ring
        is torsion-free as a `\\ZZ`-module; for all other cases the
        arithmetic product is uniquely determined by requiring it to be
        functorial in the base ring. See
        http://mathoverflow.net/questions/138148/ for a discussion of
        this arithmetic product.

        If `f` and `g` are two symmetric functions which are homogeneous
        of degrees `a` and `b`, respectively, then `f \\boxdot g` is
        homogeneous of degree `ab`.

        The arithmetic product is commutative and associative and has
        unity `e_1 = p_1 = h_1`.

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the
          same base ring as ``self``

        OUTPUT:

        Arithmetic product of ``self`` with ``x``; this is a symmetric
        function over the same base ring as ``self``.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([2]).arithmetic_product(s([2]))
            s[1, 1, 1, 1] + 2*s[2, 2] + s[4]
            sage: s([2]).arithmetic_product(s([1,1]))
            s[2, 1, 1] + s[3, 1]

        The symmetric function ``e[1]`` is the unity for the arithmetic
        product::

            sage: e = SymmetricFunctions(ZZ).e()
            sage: all( e([1]).arithmetic_product(e(q)) == e(q) for q in Partitions(4) )
            True

        The arithmetic product is commutative::

            sage: e = SymmetricFunctions(FiniteField(19)).e()
            sage: m = SymmetricFunctions(FiniteField(19)).m()
            sage: all( all( e(p).arithmetic_product(m(q)) == m(q).arithmetic_product(e(p))  # long time (26s on sage.math, 2013)
            ....:           for q in Partitions(4) )
            ....:      for p in Partitions(4) )
            True

        .. NOTE::

            The currently existing implementation of this function is
            technically unsatisfactory. It distinguishes the case when the
            base ring is a `\\QQ`-algebra (in which case the arithmetic product
            can be easily computed using the power sum basis) from the case
            where it isn\'t. In the latter, it does a computation using
            universal coefficients, again distinguishing the case when it is
            able to compute the "corresponding" basis of the symmetric function
            algebra over `\\QQ` (using the ``corresponding_basis_over`` hack)
            from the case when it isn\'t (in which case it transforms everything
            into the Schur basis, which is slow).
        '''
    def nabla(self, q=None, t=None, power: int = 1):
        """
        Return the value of the nabla operator applied to ``self``.

        The eigenvectors of the nabla operator are the Macdonald polynomials in
        the Ht basis.

        If the parameter ``power`` is an integer then it calculates
        nabla to that integer.  The default value of ``power`` is 1.

        INPUT:

        - ``q``, ``t`` -- parameters (default: ``None``, in which case ``q``
          and ``t`` are used)
        - ``power`` -- (default: ``1``) an integer indicating how many times to
          apply the operator `\\nabla`.  Negative values of ``power``
          indicate powers of `\\nabla^{-1}`.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: p = Sym.power()
            sage: p([1,1]).nabla()
            -(1/2*q*t-1/2*q-1/2*t-1/2)*p[1, 1] + (1/2*q*t-1/2*q-1/2*t+1/2)*p[2]
            sage: p([2,1]).nabla(q=1)
            -(t+1)*p[1, 1, 1] + t*p[2, 1]
            sage: p([2]).nabla(q=1)*p([1]).nabla(q=1)
            -(t+1)*p[1, 1, 1] + t*p[2, 1]
            sage: s = Sym.schur()
            sage: s([2,1]).nabla()
            -(q^3*t+q^2*t^2+q*t^3)*s[1, 1, 1] - (q^2*t+q*t^2)*s[2, 1]
            sage: s([1,1,1]).nabla()
            (q^3+q^2*t+q*t^2+t^3+q*t)*s[1, 1, 1] + (q^2+q*t+t^2+q+t)*s[2, 1] + s[3]
            sage: s([1,1,1]).nabla(t=1)
            (q^3+q^2+2*q+1)*s[1, 1, 1] + (q^2+2*q+2)*s[2, 1] + s[3]
            sage: s(0).nabla()
            0
            sage: s(1).nabla()
            s[]
            sage: s([2,1]).nabla(power=-1)
            -((q+t)/(q^2*t^2))*s[2, 1] + ((q^2+q*t+t^2)/(-q^3*t^3))*s[3]
            sage: (s([2])+s([3])).nabla()
            -q*t*s[1, 1] + (q^3*t^2+q^2*t^3)*s[1, 1, 1] + q^2*t^2*s[2, 1]
        """
    def scalar(self, x, zee=None):
        '''
        Return the standard scalar product between ``self`` and ``x``.

        This is also known as the "Hall inner product" or the
        "Hall scalar product".

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the
          same base ring as ``self``

        - ``zee`` -- an optional function on partitions giving
          the value for the scalar product between `p_{\\mu}` and `p_{\\mu}`
          (default: the standard :meth:`~sage.combinat.sf.sfa.zee` function)

        This is the default implementation that converts both ``self`` and
        ``x`` into either Schur functions (if ``zee`` is not specified) or
        power-sum functions (if ``zee`` is specified) and performs the scalar
        product in that basis.

        EXAMPLES::

            sage: e = SymmetricFunctions(QQ).e()
            sage: h = SymmetricFunctions(QQ).h()
            sage: m = SymmetricFunctions(QQ).m()
            sage: p4 = Partitions(4)
            sage: matrix([ [e(a).scalar(h(b)) for a in p4] for b in p4])
            [ 0  0  0  0  1]
            [ 0  0  0  1  4]
            [ 0  0  1  2  6]
            [ 0  1  2  5 12]
            [ 1  4  6 12 24]
            sage: matrix([ [h(a).scalar(e(b)) for a in p4] for b in p4])
            [ 0  0  0  0  1]
            [ 0  0  0  1  4]
            [ 0  0  1  2  6]
            [ 0  1  2  5 12]
            [ 1  4  6 12 24]
            sage: matrix([ [m(a).scalar(e(b)) for a in p4] for b in p4])
            [-1  2  1 -3  1]
            [ 0  1  0 -2  1]
            [ 0  0  1 -2  1]
            [ 0  0  0 -1  1]
            [ 0  0  0  0  1]
            sage: matrix([ [m(a).scalar(h(b)) for a in p4] for b in p4])
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]

            sage: p = SymmetricFunctions(QQ).p()
            sage: m(p[3,2]).scalar(p[3,2], zee=lambda mu: 2**mu.length())
            4
            sage: m(p[3,2]).scalar(p[2,2,1], lambda mu: 1)
            0
            sage: m[3,2].scalar(h[3,2], zee=lambda mu: 2**mu.length())
            2/3

        TESTS::

            sage: m(1).scalar(h(1))
            1
            sage: m(0).scalar(h(1))
            0
            sage: m(1).scalar(h(0))
            0
            sage: m(0).scalar(h(0))
            0

        Over the integers, too (as long as ``zee`` is not set)::

            sage: Sym = SymmetricFunctions(ZZ)
            sage: m = Sym.m()
            sage: m([2]).scalar(m([2]))
            2
        '''
    def scalar_qt(self, x, q=None, t=None):
        """
        Return the `q,t`-deformed standard Hall-Littlewood scalar product of
        ``self`` and ``x``.

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the same
          base ring as ``self``

        - ``q``, ``t`` -- parameters (default: ``None`` in which case ``q``
          and ``t`` are used)

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: a = s([2,1])
            sage: sp = a.scalar_qt(a); factor(sp)
            (t - 1)^-3 * (q - 1) * (t^2 + t + 1)^-1 * (q^2*t^2 - q*t^2 + q^2 - 2*q*t + t^2 - q + 1)
            sage: sp.parent()
            Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field
            sage: a.scalar_qt(a,q=0)
            (-t^2 - 1)/(t^5 - 2*t^4 + t^3 - t^2 + 2*t - 1)
            sage: a.scalar_qt(a,t=0)
            -q^3 + 2*q^2 - 2*q + 1
            sage: a.scalar_qt(a,5,7) # q=5 and t=7
            490/1539
            sage: (x,y) = var('x,y')                                                    # needs sage.symbolic
            sage: a.scalar_qt(a, q=x, t=y)                                              # needs sage.symbolic
            1/3*(x^3 - 1)/(y^3 - 1) + 2/3*(x - 1)^3/(y - 1)^3
            sage: Rn = QQ['q','t','y','z'].fraction_field()
            sage: (q,t,y,z) = Rn.gens()
            sage: Mac = SymmetricFunctions(Rn).macdonald(q=y,t=z)
            sage: a = Mac._sym.schur()([2,1])
            sage: factor(Mac.P()(a).scalar_qt(Mac.Q()(a),q,t))
            (t - 1)^-3 * (q - 1) * (t^2 + t + 1)^-1 * (q^2*t^2 - q*t^2 + q^2 - 2*q*t + t^2 - q + 1)
            sage: factor(Mac.P()(a).scalar_qt(Mac.Q()(a)))
            (z - 1)^-3 * (y - 1) * (z^2 + z + 1)^-1 * (y^2*z^2 - y*z^2 + y^2 - 2*y*z + z^2 - y + 1)
        """
    def scalar_t(self, x, t=None):
        """
        Return the `t`-deformed standard Hall-Littlewood scalar product of
        ``self`` and ``x``.

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the same
          base ring as ``self``

        - ``t`` -- parameter (default: ``None``, in which case ``t`` is used)

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: a = s([2,1])
            sage: sp = a.scalar_t(a); sp
            (-t^2 - 1)/(t^5 - 2*t^4 + t^3 - t^2 + 2*t - 1)
            sage: sp.parent()
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    scalar_hl = scalar_t
    def scalar_jack(self, x, t=None):
        """
        Return the Jack-scalar product between ``self`` and ``x``.

        This scalar product is defined so that the power sum elements
        `p_{\\mu}` are orthogonal and `\\langle p_{\\mu}, p_{\\mu} \\rangle =
        z_{\\mu} t^{\\ell(\\mu)}`, where `\\ell(\\mu)` denotes the length of
        `\\mu`.

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the
          same base ring as ``self``
        - ``t`` -- an optional parameter (default: ``None`` in which
          case ``t`` is used)

        EXAMPLES::

            sage: p = SymmetricFunctions(QQ['t']).power()
            sage: matrix([[p(mu).scalar_jack(p(nu)) for nu in Partitions(4)] for mu in Partitions(4)])
            [   4*t      0      0      0      0]
            [     0  3*t^2      0      0      0]
            [     0      0  8*t^2      0      0]
            [     0      0      0  4*t^3      0]
            [     0      0      0      0 24*t^4]
            sage: matrix([[p(mu).scalar_jack(p(nu),2) for nu in Partitions(4)] for mu in Partitions(4)])
            [  8   0   0   0   0]
            [  0  12   0   0   0]
            [  0   0  32   0   0]
            [  0   0   0  32   0]
            [  0   0   0   0 384]
            sage: JQ = SymmetricFunctions(QQ['t'].fraction_field()).jack().Q()
            sage: matrix([[JQ(mu).scalar_jack(JQ(nu)) for nu in Partitions(3)] for mu in Partitions(3)])
            [(1/3*t^2 + 1/2*t + 1/6)/t^3                           0                           0]
            [                          0 (1/2*t + 1)/(t^3 + 1/2*t^2)                           0]
            [                          0                           0       6/(t^3 + 3*t^2 + 2*t)]
        """
    def derivative_with_respect_to_p1(self, n: int = 1):
        """
        Return the symmetric function obtained by taking the derivative of
        ``self`` with respect to the power-sum symmetric function `p_1`
        when the expansion of ``self`` in the power-sum basis is considered
        as a polynomial in `p_k`'s (with `k \\geq 1`).

        This is the same as skewing ``self`` by the first power-sum symmetric
        function `p_1`.

        INPUT:

        - ``n`` -- (default: 1) nonnegative integer which determines
          which power of the derivative is taken

        EXAMPLES::

            sage: p = SymmetricFunctions(QQ).p()
            sage: a = p([1,1,1])
            sage: a.derivative_with_respect_to_p1()
            3*p[1, 1]
            sage: a.derivative_with_respect_to_p1(1)
            3*p[1, 1]
            sage: a.derivative_with_respect_to_p1(2)
            6*p[1]
            sage: a.derivative_with_respect_to_p1(3)
            6*p[]

        ::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([3]).derivative_with_respect_to_p1()
            s[2]
            sage: s([2,1]).derivative_with_respect_to_p1()
            s[1, 1] + s[2]
            sage: s([1,1,1]).derivative_with_respect_to_p1()
            s[1, 1]
            sage: s(0).derivative_with_respect_to_p1()
            0
            sage: s(1).derivative_with_respect_to_p1()
            0
            sage: s([1]).derivative_with_respect_to_p1()
            s[]

        Let us check that taking the derivative with respect to ``p[1]``
        is equivalent to skewing by ``p[1]``::

            sage: p1 = s([1])
            sage: all( s(lam).derivative_with_respect_to_p1()
            ....:      == s(lam).skew_by(p1) for lam in Partitions(4) )
            True
        """
    def adams_operator(self, n):
        '''
        Return the image of the symmetric function ``self`` under the
        `n`-th Adams operator.

        The `n`-th Adams operator `\\mathbf{f}_n` is defined to be the
        map from the ring of symmetric functions to itself that sends
        every symmetric function `P(x_1, x_2, x_3, \\ldots)` to
        `P(x_1^n, x_2^n, x_3^n, \\ldots)`. This operator `\\mathbf{f}_n`
        is a Hopf algebra endomorphism, and satisfies

        .. MATH::

            \\mathbf{f}_n m_{(\\lambda_1, \\lambda_2, \\lambda_3, \\ldots)} =
            m_{(n\\lambda_1, n\\lambda_2, n\\lambda_3, \\ldots)}

        for every partition `(\\lambda_1, \\lambda_2, \\lambda_3, \\ldots)`
        (where `m` means the monomial basis). Moreover,
        `\\mathbf{f}_n (p_r) = p_{nr}` for every positive integer `r` (where
        `p_k` denotes the `k`-th powersum symmetric function).

        The `n`-th Adams operator is also called the `n`-th
        Frobenius endomorphism. It is not related to the Frobenius map
        which connects the ring of symmetric functions with the
        representation theory of the symmetric group.

        The `n`-th Adams operator is also the `n`-th Adams operator
        of the `\\Lambda`-ring of symmetric functions over the integers.

        The `n`-th Adams operator can also be described via plethysm:
        Every symmetric function `P` satisfies
        `\\mathbf{f}_n(P) = p_n \\circ P = P \\circ p_n`,
        where `p_n` is the `n`-th powersum symmetric function, and `\\circ`
        denotes (outer) plethysm.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT:

        The result of applying the `n`-th Adams operator (on the ring of
        symmetric functions) to ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(ZZ)
            sage: p = Sym.p()
            sage: h = Sym.h()
            sage: s = Sym.s()
            sage: m = Sym.m()
            sage: s[3].adams_operator(2)
            -s[3, 3] + s[4, 2] - s[5, 1] + s[6]
            sage: m[4,2,1].adams_operator(3)
            m[12, 6, 3]
            sage: p[4,2,1].adams_operator(3)
            p[12, 6, 3]
            sage: h[4].adams_operator(2)
            h[4, 4] - 2*h[5, 3] + 2*h[6, 2] - 2*h[7, 1] + 2*h[8]

        The Adams endomorphisms are multiplicative::

            sage: all( all( s(lam).adams_operator(3) * s(mu).adams_operator(3) # long time
            ....:           == (s(lam) * s(mu)).adams_operator(3)
            ....:           for mu in Partitions(3) )
            ....:      for lam in Partitions(3) )
            True
            sage: all( all( m(lam).adams_operator(2) * m(mu).adams_operator(2)
            ....:           == (m(lam) * m(mu)).adams_operator(2)
            ....:           for mu in Partitions(4) )
            ....:      for lam in Partitions(4) )
            True
            sage: all( all( p(lam).adams_operator(2) * p(mu).adams_operator(2)
            ....:           == (p(lam) * p(mu)).adams_operator(2)
            ....:           for mu in Partitions(3) )
            ....:      for lam in Partitions(4) )
            True

        Being Hopf algebra endomorphisms, the Adams operators
        commute with the antipode::

            sage: all( p(lam).adams_operator(4).antipode()
            ....:      == p(lam).antipode().adams_operator(4)
            ....:      for lam in Partitions(3) )
            True

        Testing the `\\mathbf{f}_n(P) = p_n \\circ P = P \\circ p_n`
        equality (over `\\QQ`, since plethysm is currently not
        defined over `\\ZZ` in Sage)::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.s()
            sage: p = Sym.p()
            sage: all( s(lam).adams_operator(3) == s(lam).plethysm(p[3])
            ....:      == s(p[3].plethysm(s(lam)))
            ....:      for lam in Partitions(4) )
            True

        By Exercise 7.61 in Stanley\'s EC2 [STA]_ (see the errata on his
        website), `\\mathbf{f}_n(h_m)` is a linear combination of
        Schur polynomials (of straight shapes) using coefficients `0`,
        `1` and `-1` only; moreover, all partitions whose Schur
        polynomials occur with coefficient `\\neq 0` in this
        combination have empty `n`-cores. Let us check this on
        examples::

            sage: all( all( all( (coeff == -1 or coeff == 1)
            ....:                and lam.core(n) == Partition([])
            ....:                for lam, coeff in s([m]).adams_operator(n) )
            ....:           for n in range(2, 4) )
            ....:      for m in range(4) )
            True

        .. SEEALSO::

            :meth:`plethysm`

        .. TODO::

            This method is fast on the monomial and the powersum
            bases, while all other bases get converted to the
            monomial basis. For most bases, this is probably the
            quickest way to do, but at least the Schur basis should
            have a better option. (Quoting from Stanley\'s EC2 [STA]_:
            "D. G. Duncan, J. London Math. Soc. 27 (1952), 235-236,
            or Y. M. Chen, A. M. Garsia, and J. B. Remmel, Contemp.
            Math. 34 (1984), 109-153".)
        '''
    frobenius: Incomplete
    def verschiebung(self, n):
        '''
        Return the image of the symmetric function ``self`` under the
        `n`-th Verschiebung operator.

        The `n`-th Verschiebung operator `\\mathbf{V}_n` is defined to be
        the unique algebra endomorphism `V` of the ring of symmetric
        functions that satisfies `V(h_r) = h_{r/n}` for every positive
        integer `r` divisible by `n`, and satisfies `V(h_r) = 0` for
        every positive integer `r` not divisible by `n`. This operator
        `\\mathbf{V}_n` is a Hopf algebra endomorphism. For every
        nonnegative integer `r` with `n \\mid r`, it satisfies

        .. MATH::

            \\mathbf{V}_n(h_r) = h_{r/n},
            \\quad \\mathbf{V}_n(p_r) = n p_{r/n},
            \\quad \\mathbf{V}_n(e_r) = (-1)^{r - r/n} e_{r/n}

        (where `h` is the complete homogeneous basis, `p` is the
        powersum basis, and `e` is the elementary basis). For every
        nonnegative integer `r` with `n \\nmid r`, it satisfes

        .. MATH::

            \\mathbf{V}_n(h_r) = \\mathbf{V}_n(p_r) = \\mathbf{V}_n(e_r) = 0.

        The `n`-th Verschiebung operator is also called the `n`-th
        Verschiebung endomorphism. Its name derives from the Verschiebung
        (German for "shift") endomorphism of the Witt vectors.

        The `n`-th Verschiebung operator is adjoint to the `n`-th
        Adams operator (see :meth:`adams_operator` for its definition)
        with respect to the Hall scalar product (:meth:`scalar`).

        The action of the `n`-th Verschiebung operator on the Schur basis
        can also be computed explicitly. The following (probably clumsier
        than necessary) description can be obtained by solving exercise
        7.61 in Stanley\'s [STA]_.

        Let `\\lambda` be a partition. Let `n` be a positive integer. If
        the `n`-core of `\\lambda` is nonempty, then
        `\\mathbf{V}_n(s_\\lambda) = 0`. Otherwise, the following method
        computes `\\mathbf{V}_n(s_\\lambda)`: Write the partition `\\lambda`
        in the form `(\\lambda_1, \\lambda_2, \\ldots, \\lambda_{ns})` for some
        nonnegative integer `s`. (If `n` does not divide the length of
        `\\lambda`, then this is achieved by adding trailing zeroes to
        `\\lambda`.) Set `\\beta_i = \\lambda_i + ns - i` for every
        `s \\in \\{ 1, 2, \\ldots, ns \\}`. Then,
        `(\\beta_1, \\beta_2, \\ldots, \\beta_{ns})` is a strictly decreasing
        sequence of nonnegative integers. Stably sort the list
        `(1, 2, \\ldots, ns)` in order of (weakly) increasing remainder of
        `-1 - \\beta_i` modulo `n`. Let `\\xi` be the sign of the
        permutation that is used for this sorting. Let `\\psi` be the sign
        of the permutation that is used to stably sort the list
        `(1, 2, \\ldots, ns)` in order of (weakly) increasing remainder of
        `i - 1` modulo `n`. (Notice that `\\psi = (-1)^{n(n-1)s(s-1)/4}`.)
        Then, `\\mathbf{V}_n(s_\\lambda) = \\xi \\psi \\prod_{i = 0}^{n - 1}
        s_{\\lambda^{(i)}}`, where
        `(\\lambda^{(0)}, \\lambda^{(1)}, \\ldots, \\lambda^{(n - 1)})`
        is the `n`-quotient of `\\lambda`.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT:

        The result of applying the `n`-th Verschiebung operator (on the ring of
        symmetric functions) to ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(ZZ)
            sage: p = Sym.p()
            sage: h = Sym.h()
            sage: s = Sym.s()
            sage: m = Sym.m()
            sage: s[3].verschiebung(2)
            0
            sage: s[3].verschiebung(3)
            s[1]
            sage: p[3].verschiebung(3)
            3*p[1]
            sage: m[3,2,1].verschiebung(3)
            -18*m[1, 1] - 3*m[2]
            sage: p[3,2,1].verschiebung(3)
            0
            sage: h[4].verschiebung(2)
            h[2]
            sage: p[2].verschiebung(2)
            2*p[1]
            sage: m[3,2,1].verschiebung(6)
            12*m[1]

        The Verschiebung endomorphisms are multiplicative::

            sage: all( all( s(lam).verschiebung(2) * s(mu).verschiebung(2)
            ....:           == (s(lam) * s(mu)).verschiebung(2)
            ....:           for mu in Partitions(4) )
            ....:      for lam in Partitions(4) )
            True

        Being Hopf algebra endomorphisms, the Verschiebung operators
        commute with the antipode::

            sage: all( p(lam).verschiebung(3).antipode()
            ....:      == p(lam).antipode().verschiebung(3)
            ....:      for lam in Partitions(6) )
            True

        Testing the adjointness between the Adams operators
        `\\mathbf{f}_n` and the Verschiebung operators
        `\\mathbf{V}_n`::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.s()
            sage: p = Sym.p()
            sage: all( all( s(lam).verschiebung(2).scalar(p(mu))
            ....:           == s(lam).scalar(p(mu).adams_operator(2))
            ....:           for mu in Partitions(3) )
            ....:      for lam in Partitions(6) )
            True
        '''
    def bernstein_creation_operator(self, n):
        '''
        Return the image of ``self`` under the `n`-th Bernstein creation
        operator.

        Let `n` be an integer. The `n`-th Bernstein creation operator
        `\\mathbf{B}_n` is defined as the endomorphism of the space
        `Sym` of symmetric functions which sends every `f` to

        .. MATH::

            \\sum_{i \\geq 0} (-1)^i h_{n+i} e_i^\\perp,

        where usual notations are in place (`h` stands for the complete
        homogeneous symmetric functions, `e` for the elementary ones,
        and `e_i^\\perp` means skewing (:meth:`skew_by`) by `e_i`).

        This has been studied in [BBSSZ2012]_, section 2.2, where the
        following rule is given for computing `\\mathbf{B}_n` on a
        Schur function: If `(\\alpha_1, \\alpha_2, \\ldots, \\alpha_n)` is
        an `n`-tuple of integers (positive or not), then

        .. MATH::

            \\mathbf{B}_n s_{(\\alpha_1, \\alpha_2, \\ldots, \\alpha_n)}
            = s_{(n, \\alpha_1, \\alpha_2, \\ldots, \\alpha_n)}.

        Here, `s_{(\\alpha_1, \\alpha_2, \\ldots, \\alpha_n)}` is the
        "Schur function" associated to the `n`-tuple
        `(\\alpha_1, \\alpha_2, \\ldots, \\alpha_n)`, and defined by
        literally applying the Jacobi-Trudi identity, i.e., by

        .. MATH::

            s_{(\\alpha_1, \\alpha_2, \\ldots, \\alpha_n)}
            = \\det \\left( (h_{\\alpha_i - i + j})_{i, j = 1, 2, \\ldots, n} \\right).

        This notion of a Schur function clearly extends the classical
        notion of Schur function corresponding to a partition, but is
        easily reduced to the latter (in fact, for any `n`-tuple
        `\\alpha` of integers, one easily sees that `s_\\alpha` is
        either `0` or minus-plus a Schur function corresponding to a
        partition; and it is easy to determine which of these is the
        case and find the partition by a combinatorial algorithm).

        EXAMPLES:

        Let us check that what this method computes agrees with the
        definition::

            sage: Sym = SymmetricFunctions(ZZ)
            sage: e = Sym.e()
            sage: h = Sym.h()
            sage: s = Sym.s()
            sage: def bernstein_creation_by_def(n, f):
            ....:     # `n`-th Bernstein creation operator applied to `f`
            ....:     # computed according to its definition.
            ....:     res = f.parent().zero()
            ....:     if not f:
            ....:         return res
            ....:     max_degree = max(sum(m) for m, c in f)
            ....:     for i in range(max_degree + 1):
            ....:         if n + i >= 0:
            ....:             res += (-1) ** i * h[n + i] * f.skew_by(e[i])
            ....:     return res
            sage: all( bernstein_creation_by_def(n, s[l]) == s[l].bernstein_creation_operator(n)
            ....:      for n in range(-2, 3) for l in Partitions(4) )
            True
            sage: all( bernstein_creation_by_def(n, s[l]) == s[l].bernstein_creation_operator(n)
            ....:      for n in range(-3, 4) for l in Partitions(3) )
            True
            sage: all( bernstein_creation_by_def(n, e[l]) == e[l].bernstein_creation_operator(n)
            ....:      for n in range(-3, 4) for k in range(3) for l in Partitions(k) )
            True

        Some examples::

            sage: s[3,2].bernstein_creation_operator(3)
            s[3, 3, 2]
            sage: s[3,2].bernstein_creation_operator(1)
            -s[2, 2, 2]
            sage: h[3,2].bernstein_creation_operator(-2)
            h[2, 1]
            sage: h[3,2].bernstein_creation_operator(-1)
            h[2, 1, 1] - h[2, 2] - h[3, 1]
            sage: h[3,2].bernstein_creation_operator(0)
            -h[3, 1, 1] + h[3, 2]
            sage: h[3,2].bernstein_creation_operator(1)
            -h[2, 2, 2] + h[3, 2, 1]
            sage: h[3,2].bernstein_creation_operator(2)
            -h[3, 3, 1] + h[4, 2, 1]
        '''
    def is_schur_positive(self):
        """
        Return ``True`` if and only if ``self`` is Schur positive.

        If `s` is the space of Schur functions over ``self``'s base ring, then
        this is the same as ``self._is_positive(s)``.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: a = s([2,1]) + s([3])
            sage: a.is_schur_positive()
            True
            sage: a = s([2,1]) - s([3])
            sage: a.is_schur_positive()
            False

        ::

            sage: QQx = QQ['x']
            sage: s = SymmetricFunctions(QQx).s()
            sage: x = QQx.gen()
            sage: a = (1+x)*s([2,1])
            sage: a.is_schur_positive()
            True
            sage: a = (1-x)*s([2,1])
            sage: a.is_schur_positive()
            False
            sage: s(0).is_schur_positive()
            True
            sage: s(1+x).is_schur_positive()
            True
        """
    def degree(self):
        """
        Return the degree of ``self`` (which is defined to be `0`
        for the zero element).

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1]) + 3
            sage: z.degree()
            4
            sage: s(1).degree()
            0
            sage: s(0).degree()
            0
        """
    def restrict_degree(self, d, exact: bool = True):
        """
        Return the degree ``d`` component of ``self``.

        INPUT:

        - ``d`` -- positive integer, degree of the terms to be returned

        - ``exact`` -- boolean, if ``True``, returns the terms of degree
          exactly ``d``, otherwise returns all terms of degree less than
          or equal to ``d``

        OUTPUT: the homogeneous component of ``self`` of degree ``d``

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])
            sage: z.restrict_degree(2)
            0
            sage: z.restrict_degree(1)
            s[1]
            sage: z.restrict_degree(3)
            s[1, 1, 1] + s[2, 1]
            sage: z.restrict_degree(3, exact=False)
            s[1] + s[1, 1, 1] + s[2, 1]
            sage: z.restrict_degree(0)
            0
        """
    def restrict_partition_lengths(self, l, exact: bool = True):
        """
        Return the terms of ``self`` labelled by partitions of length ``l``.

        INPUT:

        - ``l`` -- nonnegative integer

        - ``exact`` -- boolean, defaulting to ``True``

        OUTPUT:

        - if ``True``, returns the terms labelled by
          partitions of length precisely ``l``; otherwise returns all terms
          labelled by partitions of length less than or equal to ``l``

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])
            sage: z.restrict_partition_lengths(2)
            s[2, 1]
            sage: z.restrict_partition_lengths(0)
            0
            sage: z.restrict_partition_lengths(2, exact = False)
            s[1] + s[2, 1] + s[4]
        """
    def restrict_parts(self, n):
        """
        Return the terms of ``self`` labelled by partitions `\\lambda` with
        `\\lambda_1 \\leq n`.

        INPUT:

        - ``n`` -- positive integer, to restrict the parts of the partitions
          of the terms to be returned

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: z = s([4]) + s([2,1]) + s([1,1,1]) + s([1])
            sage: z.restrict_parts(2)
            s[1] + s[1, 1, 1] + s[2, 1]
            sage: z.restrict_parts(1)
            s[1] + s[1, 1, 1]
        """
    def expand(self, n, alphabet: str = 'x'):
        """
        Expand the symmetric function ``self`` as a symmetric polynomial
        in ``n`` variables.

        INPUT:

        - ``n`` -- nonnegative integer

        - ``alphabet`` -- (default: ``'x'``) a variable for the expansion

        OUTPUT:

        A monomial expansion of ``self`` in the `n` variables
        labelled ``x0``, ``x1``, ..., ``x{n-1}`` (or just ``x``
        if `n = 1`), where ``x`` is ``alphabet``.

        EXAMPLES::

            sage: J = SymmetricFunctions(QQ).jack(t=2).J()
            sage: J([2,1]).expand(3)
            4*x0^2*x1 + 4*x0*x1^2 + 4*x0^2*x2 + 6*x0*x1*x2 + 4*x1^2*x2 + 4*x0*x2^2 + 4*x1*x2^2
            sage: (2*J([2])).expand(0)
            0
            sage: (3*J([])).expand(0)
            3
        """
    def skew_by(self, x):
        """
        Return the result of skewing ``self`` by ``x``. (Skewing by ``x`` is
        the endomorphism (as additive group) of the ring of symmetric
        functions adjoint to multiplication by ``x`` with respect to the
        Hall inner product.)

        INPUT:

        - ``x`` -- element of the ring of symmetric functions over the same
          base ring as ``self``

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([3,2]).skew_by(s([2]))
            s[2, 1] + s[3]
            sage: s([3,2]).skew_by(s([1,1,1]))
            0
            sage: s([3,2,1]).skew_by(s([2,1]))
            s[1, 1, 1] + 2*s[2, 1] + s[3]

        ::

            sage: p = SymmetricFunctions(QQ).powersum()
            sage: p([4,3,3,2,2,1]).skew_by(p([2,1]))
            4*p[4, 3, 3, 2]
            sage: zee = sage.combinat.sf.sfa.zee
            sage: zee([4,3,3,2,2,1])/zee([4,3,3,2])
            4
            sage: s(0).skew_by(s([1]))
            0
            sage: s(1).skew_by(s([1]))
            0
            sage: s([]).skew_by(s([]))
            s[]
            sage: s([]).skew_by(s[1])
            0

        TESTS::

            sage: f = s[3,2]
            sage: f.skew_by([1])
            Traceback (most recent call last):
            ...
            ValueError: x needs to be a symmetric function

            sage: s = SymmetricFunctions(QQ['t']).s()
            sage: f = s[3,2,1].skew_by(s[2,1]); f
            s[1, 1, 1] + 2*s[2, 1] + s[3]
            sage: f / 2
            1/2*s[1, 1, 1] + s[2, 1] + 1/2*s[3]
            sage: s = SymmetricFunctions(GF(2)).s()
            sage: s[3,2,1].skew_by(s[2,1])
            s[1, 1, 1] + s[3]
        """
    def hl_creation_operator(self, nu, t=None):
        """
        This is the vertex operator that generalizes Jing's operator.

        It is a linear operator that raises the degree by
        `|\\nu|`. This creation operator is a t-analogue of
        multiplication by ``s(nu)`` .

        .. SEEALSO:: Proposition 5 in [SZ2001]_.

        INPUT:

        - ``nu`` -- a partition or a list of integers

        - ``t`` -- (default: ``None``, in which case ``t`` is used) an element
          of the base ring

        REFERENCES:

        .. [SZ2001] \\M. Shimozono, M. Zabrocki,
           Hall-Littlewood vertex operators and generalized Kostka polynomials.
           Adv. Math. 158 (2001), no. 1, 66-85.

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ['t']).s()
            sage: s([2]).hl_creation_operator([3,2])
            s[3, 2, 2] + t*s[3, 3, 1] + t*s[4, 2, 1] + t^2*s[4, 3] + t^2*s[5, 2]

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLQp = Sym.hall_littlewood().Qp()
            sage: s = Sym.s()
            sage: HLQp(s([2]).hl_creation_operator([2]).hl_creation_operator([3]))
            HLQp[3, 2, 2]
            sage: s([2,2]).hl_creation_operator([2,1])
            t*s[2, 2, 2, 1] + t^2*s[3, 2, 1, 1] + t^2*s[3, 2, 2] + t^3*s[3, 3, 1] + t^3*s[4, 2, 1] + t^4*s[4, 3]
            sage: s(1).hl_creation_operator([2,1,1])
            s[2, 1, 1]
            sage: s(0).hl_creation_operator([2,1,1])
            0
            sage: s([3,2]).hl_creation_operator([2,1,1])
            (t^2-t)*s[2, 2, 2, 2, 1] + t^3*s[3, 2, 2, 1, 1]
             + (t^3-t^2)*s[3, 2, 2, 2] + t^3*s[3, 3, 1, 1, 1]
             + t^4*s[3, 3, 2, 1] + t^3*s[4, 2, 1, 1, 1] + t^4*s[4, 2, 2, 1]
             + 2*t^4*s[4, 3, 1, 1] + t^5*s[4, 3, 2] + t^5*s[4, 4, 1]
             + t^4*s[5, 2, 1, 1] + t^5*s[5, 3, 1]
            sage: s([3,2]).hl_creation_operator([-2])
            (-t^2+t)*s[1, 1, 1] + (-t^2+1)*s[2, 1]
            sage: s([3,2]).hl_creation_operator(-2)
            Traceback (most recent call last):
            ...
            ValueError: nu must be a list of integers
            sage: s = SymmetricFunctions(FractionField(ZZ['t'])).schur()
            sage: s[2].hl_creation_operator([3])
            s[3, 2] + t*s[4, 1] + t^2*s[5]

        TESTS::

            sage: s(0).hl_creation_operator([1])
            0
            sage: s.one().hl_creation_operator([2,-1])
            0
        """
    def eval_at_permutation_roots(self, rho):
        """
        Evaluate at eigenvalues of a permutation matrix.

        Evaluate a symmetric function at the eigenvalues of a permutation
        matrix whose cycle structure is ``rho``.  This computation is
        computed by coercing to the power sum basis where the value may
        be computed on the generators.

        This function evaluates an element at the roots of unity

        .. MATH::

            \\Xi_{\\rho_1},\\Xi_{\\rho_2},\\ldots,\\Xi_{\\rho_\\ell}

        where

        .. MATH::

            \\Xi_{m} = 1,\\zeta_m,\\zeta_m^2,\\ldots,\\zeta_m^{m-1}

        and `\\zeta_m` is an `m` root of unity.
        These roots of unity represent the eigenvalues of permutation
        matrix with cycle structure `\\rho`.

        INPUT:

        - ``rho`` -- a partition or a list of nonnegative integers

        OUTPUT: an element of the base ring

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([3,3]).eval_at_permutation_roots([6])
            0
            sage: s([3,3]).eval_at_permutation_roots([3])
            1
            sage: s([3,3]).eval_at_permutation_roots([1])
            0
            sage: s([3,3]).eval_at_permutation_roots([3,3])
            4
            sage: s([3,3]).eval_at_permutation_roots([1,1,1,1,1])
            175
            sage: (s[1]+s[2]+s[3]).eval_at_permutation_roots([3,2])
            2
        """
    def character_to_frobenius_image(self, n):
        """
        Interpret ``self`` as a `GL_n` character and then take the Frobenius
        image of this character of the permutation matrices `S_n` which
        naturally sit inside of `GL_n`.

        To know the value of this character at a permutation of cycle structure
        `\\rho` the symmetric function ``self`` is evaluated at the
        eigenvalues of a permutation of cycle structure `\\rho`.  The
        Frobenius image is then defined as
        `\\sum_{\\rho \\vdash n} f[ \\Xi_\\rho ] p_\\rho/z_\\rho`.

        .. SEEALSO::

            :meth:`eval_at_permutation_roots`

        INPUT:

        - ``n`` -- nonnegative integer to interpret ``self`` as
          a character of `GL_n`

        OUTPUT: a symmetric function of degree ``n``

        EXAMPLES::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s([1,1]).character_to_frobenius_image(5)
            s[3, 1, 1] + s[4, 1]
            sage: s([2,1]).character_to_frobenius_image(5)
            s[2, 2, 1] + 2*s[3, 1, 1] + 2*s[3, 2] + 3*s[4, 1] + s[5]
            sage: s([2,2,2]).character_to_frobenius_image(3)
            s[3]
            sage: s([2,2,2]).character_to_frobenius_image(4)
            s[2, 2] + 2*s[3, 1] + 2*s[4]
            sage: s([2,2,2]).character_to_frobenius_image(5)
            2*s[2, 2, 1] + s[3, 1, 1] + 4*s[3, 2] + 3*s[4, 1] + 2*s[5]
        """
    def principal_specialization(self, n=..., q=None):
        '''
        Return the principal specialization of a symmetric function.

        The *principal specialization* of order `n` at `q`
        is the ring homomorphism `ps_{n,q}` from the ring of
        symmetric functions to another commutative ring `R`
        given by `x_i \\mapsto q^{i-1}` for `i \\in \\{1,\\dots,n\\}`
        and `x_i \\mapsto 0` for `i > n`.
        Here, `q` is a given element of `R`, and we assume that
        the variables of our symmetric functions are
        `x_1, x_2, x_3, \\ldots`.
        (To be more precise, `ps_{n,q}` is a `K`-algebra
        homomorphism, where `K` is the base ring.)
        See Section 7.8 of [EnumComb2]_.

        The *stable principal specialization* at `q` is the ring
        homomorphism `ps_q` from the ring of symmetric functions
        to another commutative ring `R` given by
        `x_i \\mapsto q^{i-1}` for all `i`.
        This is well-defined only if the resulting infinite sums
        converge; thus, in particular, setting `q = 1` in the
        stable principal specialization is an invalid operation.

        INPUT:

        - ``n`` -- (default: ``infinity``) a nonnegative integer or
          ``infinity``, specifying whether to compute the principal
          specialization of order ``n`` or the stable principal
          specialization.

        - ``q`` -- (default: ``None``) the value to use for `q`; the
          default is to create a ring of polynomials in ``q``
          (or a field of rational functions in ``q``) over the
          given coefficient ring.

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).m()
            sage: x = m[1,1]
            sage: x.principal_specialization(3)
            q^3 + q^2 + q

        By default we return a rational function in ``q``.  Sometimes
        it is better to obtain an element of the symbolic ring::

            sage: h = SymmetricFunctions(QQ).h()
            sage: (h[3]+h[2]).principal_specialization(q=var("q"))                      # needs sage.symbolic
            1/((q^2 - 1)*(q - 1)) - 1/((q^3 - 1)*(q^2 - 1)*(q - 1))

        In case ``q`` is in the base ring, it must be passed explicitly::

            sage: R = QQ[\'q,t\']
            sage: Ht = SymmetricFunctions(R).macdonald().Ht()
            sage: Ht[2].principal_specialization()
            Traceback (most recent call last):
            ...
            ValueError: the variable q is in the base ring, pass it explicitly

            sage: Ht[2].principal_specialization(q=R("q"))
            (q^2 + 1)/(q^3 - q^2 - q + 1)

        Note that the principal specialization can be obtained as a plethysm::

            sage: R = QQ[\'q\'].fraction_field()
            sage: s = SymmetricFunctions(R).s()
            sage: one = s.one()
            sage: q = R("q")
            sage: f = s[3,2,2]
            sage: f.principal_specialization(q=q) == f(one/(1-q)).coefficient([])
            True
            sage: f.principal_specialization(n=4, q=q) == f(one*(1-q^4)/(1-q)).coefficient([])
            True

        TESTS::

            sage: m = SymmetricFunctions(QQ).m()
            sage: m.zero().principal_specialization(3)
            0

            sage: x = 5*m[1,1,1] + 3*m[2,1] + 1
            sage: x.principal_specialization(3)
            3*q^5 + 6*q^4 + 5*q^3 + 6*q^2 + 3*q + 1

        Check that the principal specializations in different bases
        are all the same.  When specific implementations for further
        bases are added, this test should be adapted::

            sage: S = SymmetricFunctions(QQ)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: m = S.m(); x = m[2,1]
            sage: len(set([b(x).principal_specialization(n=3) for b in B]))
            1
            sage: len(set([b(x).principal_specialization() for b in B]))
            1
            sage: len(set([b(x).principal_specialization(n=4, q=1) for b in B]))
            1
            sage: len(set([b(x).principal_specialization(n=4, q=2) for b in B]))
            1

        Check that the stable principal specialization at `q = 1`
        raises a :exc:`ValueError`:

            sage: def test_error(x):
            ....:     message = "the stable principal specialization of %s at q=1 should raise a ValueError"
            ....:     try:
            ....:         x.principal_specialization(q=1)
            ....:     except ValueError as e:
            ....:         return(e)
            ....:     except StandardError as e:
            ....:         raise ValueError((message + ", but raised \'%s\' instead") % (x, e))
            ....:     raise ValueError((message + ", but didn\'t") % x)

            sage: set([str(test_error(b(x))) for b in B])
            {\'the stable principal specialization at q=1 is not defined\'}

        Check that specifying `q` which is a removable singularity works::

            sage: S = SymmetricFunctions(QQ)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: m = S.m(); x = m[2,2,1]
            sage: set([b(x).principal_specialization(n=4, q=QQbar.zeta(3)) for b in B])
            {-3}

            sage: S = SymmetricFunctions(GF(3))
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: m = S.m(); x = m[3,2,1]
            sage: set([b(x).principal_specialization(n=4, q=GF(3)(2)) for b in B])
            {1}

            sage: S = SymmetricFunctions(Zmod(4))
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: m = S.m(); x = m[3,2,1]
            sage: set([b(x).principal_specialization(n=4, q=Zmod(4)(2)) for b in B])
            {0}
            sage: y = m[3,1]
            sage: set([b(y).principal_specialization(n=4, q=Zmod(4)(2)) for b in B])
            {2}
            sage: B = [S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: z = m[1,1]
            sage: set([b(z).principal_specialization(n=4) for b in B])
            {q^5 + q^4 + 2*q^3 + q^2 + q}

        Check that parents are correct over `\\mathbb{F}_3`::

            sage: S = SymmetricFunctions(GF(3))
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: lams = [Partition([]), Partition([1]), Partition([2,1])]
            sage: set(b[lam].principal_specialization(n=2, q=GF(3)(0)).parent() for b in B for lam in lams)
            {Finite Field of size 3}
            sage: set(b[lam].principal_specialization(n=2, q=GF(3)(1)).parent() for b in B for lam in lams)
            {Finite Field of size 3}
            sage: set(b[lam].principal_specialization(n=2, q=GF(3)(2)).parent() for b in B for lam in lams)
            {Finite Field of size 3}
            sage: set(b[lam].principal_specialization(n=2).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in q over Finite Field of size 3}
            sage: set(b[lam].principal_specialization().parent() for b in B for lam in lams)
            {Fraction Field of Univariate Polynomial Ring in q over Finite Field of size 3,
             Univariate Polynomial Ring in q over Finite Field of size 3}

            sage: a = S.e()[2,1].principal_specialization(n=2, q=GF(3)(2)); a
            0
            sage: a = S.e()[1,1,1].principal_specialization(n=2); a
            q^3 + 1

            sage: set(b.one().principal_specialization(n=2, q=GF(3)(2)) for b in B)
            {1}
            sage: set(b.one().principal_specialization(n=2, q=GF(3)(1)) for b in B)
            {1}
            sage: set(b.one().principal_specialization(n=2) for b in B)
            {1}
            sage: set(b.one().principal_specialization() for b in B)
            {1}

        Check that parents are correct over the integer ring::

            sage: S = SymmetricFunctions(ZZ)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: lams = [Partition([]), Partition([1]), Partition([2,1])]
            sage: set(b[lam].principal_specialization(n=2, q=0).parent() for b in B for lam in lams)
            {Integer Ring}
            sage: set(b[lam].principal_specialization(n=2, q=1).parent() for b in B for lam in lams)
            {Integer Ring}
            sage: set(b[lam].principal_specialization(n=2, q=2).parent() for b in B for lam in lams)
            {Integer Ring}
            sage: set(b[lam].principal_specialization(n=2).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in q over Integer Ring}
            sage: sorted(set(b[lam].principal_specialization().parent() for b in B for lam in lams), key=str)
            [Fraction Field of Univariate Polynomial Ring in q over Integer Ring,
             Univariate Polynomial Ring in q over Integer Ring,
             Univariate Polynomial Ring in q over Rational Field]

        Check that parents are correct over a polynomial ring::

            sage: P = PolynomialRing(ZZ, "q")
            sage: q = P.gen()
            sage: S = SymmetricFunctions(P)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: lams = [Partition([]), Partition([1]), Partition([2,1])]
            sage: set(b[lam].principal_specialization(n=2, q=P(0)).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in q over Integer Ring}
            sage: set(b[lam].principal_specialization(n=2, q=P(1)).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in q over Integer Ring}
            sage: set(b[lam].principal_specialization(n=2, q=P(2)).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in q over Integer Ring}
            sage: set(b[lam].principal_specialization(n=2, q=q).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in q over Integer Ring}
            sage: sorted(set(b[lam].principal_specialization(q=q).parent() for b in B for lam in lams), key=str)
            [Fraction Field of Univariate Polynomial Ring in q over Integer Ring,
             Univariate Polynomial Ring in q over Integer Ring,
             Univariate Polynomial Ring in q over Rational Field]

            sage: a = S.e()[2,1].principal_specialization(n=2, q=2); a
            6
            sage: a = S.e()[2,1].principal_specialization(n=2, q=q); a
            q^2 + q

            sage: set(b.one().principal_specialization(n=2, q=P(2)) for b in B)
            {1}
            sage: set(b.one().principal_specialization(n=2, q=P(1)) for b in B)
            {1}
            sage: set(b.one().principal_specialization(n=2, q=q) for b in B)
            {1}
            sage: set(b.one().principal_specialization(q=q) for b in B)
            {1}
        '''
    def exponential_specialization(self, t=None, q: int = 1):
        '''
        Return the exponential specialization of a
        symmetric function (when `q = 1`), or the
        `q`-exponential specialization (when `q \\neq 1`).

        The *exponential specialization* `ex` at `t` is a
        `K`-algebra homomorphism from the `K`-algebra of
        symmetric functions to another `K`-algebra `R`.
        It is defined whenever the base ring `K` is a
        `\\QQ`-algebra and `t` is an element of `R`.
        The easiest way to define it is by specifying its
        values on the powersum symmetric functions to be
        `p_1 = t` and `p_n = 0` for `n > 1`.
        Equivalently, on the homogeneous functions it is
        given by `ex(h_n) = t^n / n!`; see Proposition 7.8.4 of
        [EnumComb2]_.

        By analogy, the `q`-exponential specialization is a
        `K`-algebra homomorphism from the `K`-algebra of
        symmetric functions to another `K`-algebra `R` that
        depends on two elements `t` and `q` of `R` for which
        the elements `1 - q^i` for all positive integers `i`
        are invertible.
        It can be defined by specifying its values on the
        complete homogeneous symmetric functions to be

        .. MATH::

            ex_q(h_n) = t^n / [n]_q!,

        where `[n]_q!` is the `q`-factorial.  Equivalently, for
        `q \\neq 1` and a homogeneous symmetric function `f` of
        degree `n`, we have

        .. MATH::

            ex_q(f) = (1-q)^n t^n ps_q(f),

        where `ps_q(f)` is the stable principal specialization of `f`
        (see :meth:`principal_specialization`).
        (See (7.29) in [EnumComb2]_.)

        The limit of `ex_q` as `q \\to 1` is `ex`.

        INPUT:

        - ``t`` -- (default: ``None``) the value to use for `t`;
          the default is to create a ring of polynomials in ``t``

        - ``q`` -- (default: `1`) the value to use for `q`.  If
          ``q`` is ``None``, then a ring (or fraction field) of
          polynomials in ``q`` is created.

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).m()
            sage: (m[2,1]+m[1,1]).exponential_specialization()
            1/2*t^2
            sage: (m[2,1]+m[1,1]).exponential_specialization(q=1)
            1/2*t^2
            sage: m[1,1].exponential_specialization(q=None)
            (q/(q + 1))*t^2
            sage: Qq = PolynomialRing(QQ, "q"); q = Qq.gen()
            sage: m[1,1].exponential_specialization(q=q)
            (q/(q + 1))*t^2
            sage: Qt = PolynomialRing(QQ, "t"); t = Qt.gen()
            sage: m[1,1].exponential_specialization(t=t)
            1/2*t^2
            sage: Qqt = PolynomialRing(QQ, ["q", "t"]); q, t = Qqt.gens()
            sage: m[1,1].exponential_specialization(q=q, t=t)
            q*t^2/(q + 1)

            sage: x = m[3]+m[2,1]+m[1,1,1]
            sage: d = x.homogeneous_degree()
            sage: var("q t")                                                            # needs sage.symbolic
            (q, t)
            sage: factor((x.principal_specialization()*(1-q)^d*t^d))                    # needs sage.symbolic
            t^3/((q^2 + q + 1)*(q + 1))
            sage: factor(x.exponential_specialization(q=q, t=t))                        # needs sage.symbolic
            t^3/((q^2 + q + 1)*(q + 1))

        TESTS::

            sage: m = SymmetricFunctions(QQ).m()
            sage: m.zero().exponential_specialization()
            0

        Check that the exponential specializations in different bases
        are all the same.  When specific implementations for further
        bases are added, this test should be adapted::

            sage: S = SymmetricFunctions(QQ)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: m = S.m(); x = m[3]+m[2,1]+m[1,1,1]
            sage: len(set([b(x).exponential_specialization(q=None, t=None) for b in B]))
            1
            sage: len(set([b(x).exponential_specialization(q=1) for b in B]))
            1
            sage: len(set([b(x).exponential_specialization(q=2) for b in B]))
            1
            sage: len(set([b(x).exponential_specialization(t=2) for b in B]))
            1

        Check that parents are correct over `\\mathbb{F}_3`::

            sage: S = SymmetricFunctions(GF(3))
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: lams = [Partition([]), Partition([1]), Partition([2,1])]
            sage: sorted(set(b[lam].exponential_specialization(q=None).parent() for b in B for lam in lams), key=str)
            [Univariate Polynomial Ring in t over Fraction Field
              of Univariate Polynomial Ring in q over Finite Field of size 3,
             Univariate Polynomial Ring in t over Univariate Polynomial Ring
              in q over Finite Field of size 3]
            sage: P2 = PolynomialRing(GF(3), ["q", "t"])
            sage: q2, t2 = P2.gens()
            sage: sorted(set(b[lam].exponential_specialization(q=q2, t=t2).parent() for b in B for lam in lams), key=str)
            [Fraction Field of Multivariate Polynomial Ring in q, t over Finite Field of size 3,
             Multivariate Polynomial Ring in q, t over Finite Field of size 3]

        Check that parents are correct over `\\QQ` for `q = 1`::

            sage: S = SymmetricFunctions(QQ)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: lams = [Partition([]), Partition([1]), Partition([2,1])]
            sage: set(b[lam].exponential_specialization(q=1).parent() for b in B for lam in lams)
            {Univariate Polynomial Ring in t over Rational Field}
            sage: set(b[lam].exponential_specialization(q=1, t=1).parent() for b in B for lam in lams)
            {Rational Field}
            sage: P2 = PolynomialRing(QQ, ["q", "t"])
            sage: q2, t2 = P2.gens()
            sage: set(b[lam].exponential_specialization(q=1, t=t2).parent() for b in B for lam in lams)
            {Multivariate Polynomial Ring in q, t over Rational Field}

        Check that parents are correct over a polynomial ring::

            sage: P = PolynomialRing(QQ, "q")
            sage: q = P.gen()
            sage: S = SymmetricFunctions(P)
            sage: B = [S.p(), S.m(), S.e(), S.h(), S.s(), S.f()]
            sage: lams = [Partition([]), Partition([1]), Partition([2,1])]
            sage: sorted(set(b[lam].exponential_specialization(q=q).parent() for b in B for lam in lams), key=str)
            [Univariate Polynomial Ring in t over
              Fraction Field of Univariate Polynomial Ring in q over Rational Field,
             Univariate Polynomial Ring in t over Univariate Polynomial Ring
              in q over Rational Field]
            sage: sorted(set(b[lam].exponential_specialization(q=q, t=1).parent() for b in B for lam in lams), key=str)
            [Fraction Field of Univariate Polynomial Ring in q over Rational Field,
             Univariate Polynomial Ring in q over Rational Field]
        '''

class SymmetricFunctionsFunctor(ConstructionFunctor):
    """
    A constructor for algebras of symmetric functions.

    EXAMPLES::

        sage: s = SymmetricFunctions(QQ).s()
        sage: s.construction()
        (SymmetricFunctionsFunctor[Schur], Rational Field)
    """
    rank: int
    def __init__(self, basis, name, *args) -> None:
        """
        Initialize the functor.

        INPUT:

        - ``basis`` -- the basis of the symmetric function algebra
        - ``name`` -- the name of the basis
        - ``args`` -- any further arguments necessary to initialize the basis

        .. WARNING::

            Strictly speaking, this is not necessarily a functor on
            :class:`CommutativeRings`, but rather a functor on
            commutative rings with some distinguished elements.  For
            example, for the Macdonald polynomials, we have to
            specify `q` and `t` in the ring.  Apart from that, the
            codomain of this functor could actually be
            :class:`CommutativeAlgebras` over the given ring, but
            parameterized functors are currently not available.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import SymmetricFunctionsFunctor
            sage: R.<q> = ZZ[]
            sage: qbar = SymmetricFunctions(R).hecke_character()
            sage: SymmetricFunctionsFunctor(qbar, qbar.basis_name(), q)
            SymmetricFunctionsFunctor[Hecke character with q=q]
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: qbar1 = Sym.qbar(q=1/2)
            sage: qbar2 = Sym.qbar(q=1)
            sage: qbar1.construction()[0] == qbar2.construction()[0]
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: F1 = Sym.qbar(q=1/2).construction()[0]
            sage: F2 = Sym.qbar(q=1).construction()[0]
            sage: hash(F1) == hash(F2)
            False
        """

class SymmetricFunctionsFamilyFunctor(SymmetricFunctionsFunctor):
    def __init__(self, basis, family, name, *args) -> None:
        """
        Initialize the functor.

        INPUT:

        - ``basis`` -- the basis of the symmetric function algebra

        .. WARNING::

            Strictly speaking, this is not necessarily a functor on
            :class:`CommutativeRings`, but rather a functor on
            commutative rings with some distinguished elements.  For
            example, for the Macdonald polynomials, we have to
            specify `q` and `t` in the ring.  Apart from that, the
            codomain of this functor could actually be
            :class:`CommutativeAlgebras` over the given ring, but
            parameterized functors are currently not available.

        EXAMPLES::

            sage: from sage.combinat.sf.sfa import SymmetricFunctionsFamilyFunctor
            sage: R.<t> = ZZ[]
            sage: basis = SymmetricFunctions(R).macdonald(q=1).H()
            sage: family = sage.combinat.sf.macdonald.Macdonald
            sage: name = basis.basis_name()
            sage: SymmetricFunctionsFamilyFunctor(basis, family, name, 1, t)
            SymmetricFunctionsFunctor[Macdonald H with q=1]
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: S.<t> = QQ[]
            sage: T.<s> = QQ[]
            sage: PR = SymmetricFunctions(R).jack().P()
            sage: PS = SymmetricFunctions(S).jack().P()
            sage: PT = SymmetricFunctions(T).jack(t=s).P()
            sage: PR.construction()[0] == PS.construction()[0]
            True
            sage: PR.construction()[0] == PT.construction()[0]
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: P1 = SymmetricFunctions(QQ['q','t']).macdonald(q=1).P()
            sage: F1 = P1.construction()[0]
            sage: P2 = SymmetricFunctions(ZZ['t']).macdonald(q=1).P()
            sage: F2 = P2.construction()[0]
            sage: hash(F1) == hash(F2)
            True
        """
