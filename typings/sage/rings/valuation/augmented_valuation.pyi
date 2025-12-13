from .inductive_valuation import FinalInductiveValuation as FinalInductiveValuation, FiniteInductiveValuation as FiniteInductiveValuation, InductiveValuation as InductiveValuation, InfiniteInductiveValuation as InfiniteInductiveValuation, NonFinalInductiveValuation as NonFinalInductiveValuation
from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.rings.rational_field import QQ as QQ
from sage.structure.factory import UniqueFactory as UniqueFactory

class AugmentedValuationFactory(UniqueFactory):
    """
    Factory for augmented valuations.

    EXAMPLES:

    This factory is not meant to be called directly. Instead,
    :meth:`~sage.rings.valuation.inductive_valuation.NonFinalInductiveValuation.augmentation`
    of a valuation should be called::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(2))
        sage: w = v.augmentation(x, 1)  # indirect doctest

    Note that trivial parts of the augmented valuation might be dropped, so you
    should not rely on ``_base_valuation`` to be the valuation you started
    with::

        sage: ww = w.augmentation(x, 2)
        sage: ww._base_valuation is v
        True
    """
    def create_key(self, base_valuation, phi, mu, check: bool = True):
        """
        Create a key which uniquely identifies the valuation over
        ``base_valuation`` which sends ``phi`` to ``mu``.

        .. NOTE::

            The uniqueness that this factory provides is not why we chose to
            use a factory.  However, it makes pickling and equality checks much
            easier. At the same time, going through a factory makes it easier
            to enforce that all instances correctly inherit methods from the
            parent Hom space.

        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x, 1)  # indirect doctest
            sage: ww = v.augmentation(x, 1)
            sage: w is ww
            True
        """
    def create_object(self, version, key):
        """
        Create the augmented valuation represented by ``key``.

        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)  # indirect doctest
        """

AugmentedValuation: Incomplete

class AugmentedValuation_base(InductiveValuation):
    """
    An augmented valuation is a discrete valuation on a polynomial ring. It
    extends another discrete valuation `v` by setting the valuation of a
    polynomial `f` to the minimum of `v(f_i)i\\mu` when writing `f=\\sum_i
    f_i\\phi^i`.

    INPUT:

    - ``v`` -- a :class:`~sage.rings.valuation.inductive_valuation.InductiveValuation` on a polynomial ring

    - ``phi`` -- a :meth:`key polynomial <sage.rings.valuation.inductive_valuation.NonFinalInductiveValuation.is_key>` over ``v``

    - ``mu`` -- a rational number such that ``mu > v(phi)`` or ``infinity``

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: K.<u> = CyclotomicField(5)
        sage: R.<x> = K[]
        sage: v = GaussValuation(R, K.valuation(2))
        sage: w = v.augmentation(x, 1/2); w  # indirect doctest
        [ Gauss valuation induced by 2-adic valuation, v(x) = 1/2 ]
        sage: ww = w.augmentation(x^4 + 2*x^2 + 4*u, 3); ww
        [ Gauss valuation induced by 2-adic valuation, v(x) = 1/2, v(x^4 + 2*x^2 + 4*u) = 3 ]

    TESTS::

        sage: # needs sage.rings.number_field
        sage: TestSuite(w).run()    # long time
        sage: TestSuite(ww).run()   # long time
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        TESTS::

            sage: # needs sage.libs.ntl
            sage: K.<u> = Qq(4, 5)
            sage: R.<x> = K[]
            sage: v = GaussValuation(R)
            sage: from sage.rings.valuation.augmented_valuation import AugmentedValuation
            sage: w = AugmentedValuation(v, x, 1/2)
            sage: from sage.rings.valuation.augmented_valuation import AugmentedValuation_base
            sage: isinstance(w, AugmentedValuation_base)
            True
            sage: TestSuite(w).run()            # long time                             # needs sage.numerical.mip
        """
    @cached_method
    def equivalence_unit(self, s, reciprocal: bool = False):
        """
        Return an equivalence unit of minimal degree and valuation ``s``.

        INPUT:

        - ``s`` -- a rational number

        - ``reciprocal`` -- boolean (default: ``False``); whether or not to
          return the equivalence unit as the :meth:`~sage.rings.valuation.inductive_valuation.InductiveValuation.equivalence_reciprocal`
          of the equivalence unit of valuation ``-s``.

        OUTPUT:

        A polynomial in the domain of this valuation which
        :meth:`~sage.rings.valuation.inductive_valuation.InductiveValuation.is_equivalence_unit` for this valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1)
            sage: w.equivalence_unit(0)
            1 + O(2^5)
            sage: w.equivalence_unit(-4)
            2^-4 + O(2)

        Since an equivalence unit is of effective degree zero, `\\phi` must not
        divide it. Therefore, its valuation is in the value group of the base
        valuation::

            sage: w = v.augmentation(x, 1/2)                                            # needs sage.libs.ntl
            sage: w.equivalence_unit(3/2)                                               # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            ValueError: 3/2 is not in the value semigroup of 2-adic valuation
            sage: w.equivalence_unit(1)                                                 # needs sage.libs.ntl
            2 + O(2^6)

        An equivalence unit might not be integral, even if ``s >= 0``::

            sage: w = v.augmentation(x, 3/4)                                            # needs sage.libs.ntl
            sage: ww = w.augmentation(x^4 + 8, 5)                                       # needs sage.libs.ntl
            sage: ww.equivalence_unit(1/2)                                              # needs sage.libs.ntl
            (2^-1 + O(2^4))*x^2
        """
    @cached_method
    def element_with_valuation(self, s):
        """
        Create an element of minimal degree and of valuation ``s``.

        INPUT:

        - ``s`` -- a rational number in the value group of this valuation

        OUTPUT: an element in the domain of this valuation

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.element_with_valuation(0)
            1 + O(2^5)
            sage: w.element_with_valuation(1/2)
            (1 + O(2^5))*x^2 + (1 + O(2^5))*x + u + O(2^5)
            sage: w.element_with_valuation(1)
            2 + O(2^6)
            sage: c = w.element_with_valuation(-1/2); c
            (2^-1 + O(2^4))*x^2 + (2^-1 + O(2^4))*x + u*2^-1 + O(2^4)
            sage: w(c)
            -1/2
            sage: w.element_with_valuation(1/3)
            Traceback (most recent call last):
            ...
            ValueError: s must be in the value group of the valuation
            but 1/3 is not in Additive Abelian Group generated by 1/2.
        """
    def augmentation_chain(self):
        """
        Return a list with the chain of augmentations down to the underlying :mod:`Gauss valuation <sage.rings.valuation.gauss_valuation>`.

        .. NOTE::

            This method runs in time linear in the length of the chain (though
            the printed representation might seem to indicate that it takes
            quadratic time to construct the chain.)

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x, 1)
            sage: w.augmentation_chain()
            [[ Gauss valuation induced by 2-adic valuation, v(x) = 1 ],
             Gauss valuation induced by 2-adic valuation]

        For performance reasons, (and to simplify the underlying
        implementation,) trivial augmentations might get dropped. You should
        not rely on :meth:`augmentation_chain` to contain all the steps that
        you specified to create the current valuation::

            sage: ww = w.augmentation(x, 2)
            sage: ww.augmentation_chain()
            [[ Gauss valuation induced by 2-adic valuation, v(x) = 2 ],
             Gauss valuation induced by 2-adic valuation]
        """
    @cached_method
    def psi(self):
        """
        Return the minimal polynomial of the residue field extension of this valuation.

        OUTPUT: a polynomial in the residue ring of the base valuation

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.psi()
            x^2 + x + u0
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: ww.psi()
            x + 1
        """
    @cached_method
    def E(self):
        """
        Return the ramification index of this valuation over its underlying
        Gauss valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1)
            sage: w.E()
            1
            sage: w = v.augmentation(x, 1/2)
            sage: w.E()
            2
        """
    @cached_method
    def F(self):
        """
        Return the degree of the residue field extension of this valuation
        over the underlying Gauss valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1)
            sage: w.F()
            2
            sage: w = v.augmentation(x, 1/2)
            sage: w.F()
            1
        """
    def extensions(self, ring):
        """
        Return the extensions of this valuation to ``ring``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: w.extensions(GaussianIntegers().fraction_field()['x'])                # needs sage.rings.number_field
            [[ Gauss valuation induced by 2-adic valuation, v(x^2 + x + 1) = 1 ]]
        """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = GaussianIntegers().fraction_field()
            sage: R.<x> = K[]
            sage: v = GaussValuation(R, K.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: w.restriction(QQ['x'])                                                # needs sage.libs.singular
            [ Gauss valuation induced by 2-adic valuation, v(x^2 + x + 1) = 1 ]
        """
    def uniformizer(self):
        """
        Return a uniformizing element for this valuation.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)

            sage: w.uniformizer()
            2
        """
    def is_gauss_valuation(self):
        """
        Return whether this valuation is a Gauss valuation.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)

            sage: w.is_gauss_valuation()
            False
        """
    def monic_integral_model(self, G):
        """
        Return a monic integral irreducible polynomial which defines the same
        extension of the base ring of the domain as the irreducible polynomial
        ``G`` together with maps between the old and the new polynomial.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: w.monic_integral_model(5*x^2 + 1/2*x + 1/4)
            (Ring endomorphism of Univariate Polynomial Ring in x over Rational Field
               Defn: x |--> 1/2*x,
             Ring endomorphism of Univariate Polynomial Ring in x over Rational Field
               Defn: x |--> 2*x,
             x^2 + 1/5*x + 1/5)
        """
    def is_trivial(self):
        """
        Return whether this valuation is trivial, i.e., zero outside of zero.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: w.is_trivial()
            False
        """
    def scale(self, scalar):
        """
        Return this valuation scaled by ``scalar``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: 3*w # indirect doctest
            [ Gauss valuation induced by 3 * 2-adic valuation, v(x^2 + x + 1) = 3 ]
        """
    def is_negative_pseudo_valuation(self):
        """
        Return whether this valuation attains `-\\infty`.

        EXAMPLES:

        No element in the domain of an augmented valuation can have valuation
        `-\\infty`, so this method always returns ``False``::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
            sage: w = v.augmentation(x, infinity)
            sage: w.is_negative_pseudo_valuation()
            False
        """
    def change_domain(self, ring):
        """
        Return this valuation over ``ring``.

        EXAMPLES:

        We can change the domain of an augmented valuation even if there is no coercion between rings::

            sage: # needs sage.rings.number_field
            sage: R.<x> = GaussianIntegers()[]
            sage: v = GaussValuation(R, GaussianIntegers().valuation(2))
            sage: v = v.augmentation(x, 1)
            sage: v.change_domain(QQ['x'])
            [ Gauss valuation induced by 2-adic valuation, v(x) = 1 ]
        """

class FinalAugmentedValuation(AugmentedValuation_base, FinalInductiveValuation):
    """
    An augmented valuation which can not be augmented anymore, either because
    it augments a trivial valuation or because it is infinite.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
        sage: w = v.augmentation(x, 1)
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
            sage: w = v.augmentation(x, 1)
            sage: from sage.rings.valuation.augmented_valuation import FinalAugmentedValuation
            sage: isinstance(w, FinalAugmentedValuation)
            True
        """
    @cached_method
    def residue_ring(self):
        """
        Return the residue ring of this valuation, i.e., the elements of
        nonnegative valuation modulo the elements of positive valuation.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))

            sage: w = v.augmentation(x, 1)
            sage: w.residue_ring()
            Rational Field

            sage: w = v.augmentation(x^2 + x + 1, infinity)
            sage: w.residue_ring()                                                      # needs sage.rings.number_field
            Number Field in u1 with defining polynomial x^2 + x + 1

        An example with a non-trivial base valuation::

            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, infinity)
            sage: w.residue_ring()                                                      # needs sage.rings.finite_rings
            Finite Field in u1 of size 2^2

        Since trivial extensions of finite fields are not implemented, the
        resulting ring might be identical to the residue ring of the underlying
        valuation::

            sage: w = v.augmentation(x, infinity)
            sage: w.residue_ring()
            Finite Field of size 2

        TESTS:

        We avoid clashes in generator names::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x^2 + 2)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + x^2)
            sage: w = v.extension(L)
            sage: w.residue_field()
            Number Field in uu1 with defining polynomial y^2 - 2 over its base field
            sage: w.residue_field().base_field()
            Number Field in u1 with defining polynomial x^2 + 2
        """
    def reduce(self, f, check: bool = True, degree_bound=None, coefficients=None, valuations=None):
        """
        Reduce ``f`` module this valuation.

        INPUT:

        - ``f`` -- an element in the domain of this valuation

        - ``check`` -- whether or not to check whether ``f`` has nonnegative
          valuation (default: ``True``)

        - ``degree_bound`` -- an a-priori known bound on the degree of the
          result which can speed up the computation (default: not set)

        - ``coefficients`` -- the coefficients of ``f`` as produced by
          :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.coefficients`
          or ``None`` (default: ``None``); this can be used to speed up the
          computation when the expansion of ``f`` is already known from a
          previous computation.

        - ``valuations`` -- the valuations of ``coefficients`` or ``None``
          (default: ``None``); ignored

        OUTPUT:

        an element of the :meth:`residue_ring` of this valuation, the reduction
        modulo the ideal of elements of positive valuation

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))

            sage: w = v.augmentation(x, 1)
            sage: w.reduce(x^2 + x + 1)
            1

            sage: w = v.augmentation(x^2 + x + 1, infinity)
            sage: w.reduce(x)                                                           # needs sage.rings.number_field
            u1

        TESTS:

        Cases with non-trivial base valuation::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.reduce(x)
            x
            sage: v.reduce(S(u))
            u0
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.reduce(S.one())
            1
            sage: w.reduce(S(2))
            0
            sage: w.reduce(S(u))
            u0
            sage: w.reduce(x)  # this gives the generator of the residue field extension of w over v
            u1
            sage: f = (x^2 + x + u)^2 / 2
            sage: w.reduce(f)
            x
            sage: w.reduce(f + x + 1)
            x + u1 + 1
            sage: # needs sage.libs.ntl
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: g = ((x^2 + x + u)^2 + 2)^3 / 2^5
            sage: ww.reduce(g)
            x
            sage: ww.reduce(f)
            1
            sage: ww.is_equivalent(f, 1)
            True
            sage: ww.reduce(f * g)
            x
            sage: ww.reduce(f + g)
            x + 1
        """
    def lift(self, F):
        """
        Return a polynomial which reduces to ``F``.

        INPUT:

        - ``F`` -- an element of the :meth:`residue_ring`

        ALGORITHM:

        We simply undo the steps performed in :meth:`reduce`.

        OUTPUT: a polynomial in the domain of the valuation with reduction ``F``

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))

            sage: w = v.augmentation(x, 1)
            sage: w.lift(1/2)
            1/2

            sage: w = v.augmentation(x^2 + x + 1, infinity)
            sage: w.lift(w.residue_ring().gen())                                        # needs sage.rings.number_field
            x

        A case with non-trivial base valuation::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, infinity)
            sage: w.lift(w.residue_ring().gen())                                        # needs sage.rings.number_field
            (1 + O(2^10))*x

        TESTS:

        Verify that :issue:`30305` has been resolved::

            sage: # needs sage.rings.number_field
            sage: R.<T> = QQ[]
            sage: K.<zeta> = NumberField(T^2 + T + 1)
            sage: R.<x> = K[]
            sage: v0 = GaussValuation(R, valuations.TrivialValuation(K))
            sage: v = v0.augmentation(x^2 + x + 2, 1)
            sage: v.lift(v.reduce(x)) == x
            True
        """

class NonFinalAugmentedValuation(AugmentedValuation_base, NonFinalInductiveValuation):
    """
    An augmented valuation which can be augmented further.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(2))
        sage: w = v.augmentation(x^2 + x + 1, 1)
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: from sage.rings.valuation.augmented_valuation import NonFinalAugmentedValuation
            sage: isinstance(w, NonFinalAugmentedValuation)
            True
        """
    @cached_method
    def residue_ring(self):
        """
        Return the residue ring of this valuation, i.e., the elements of
        nonnegative valuation modulo the elements of positive valuation.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, 1)
            sage: w.residue_ring()                                                      # needs sage.rings.finite_rings
            Univariate Polynomial Ring in x over Finite Field in u1 of size 2^2

        Since trivial valuations of finite fields are not implemented, the
        resulting ring might be identical to the residue ring of the underlying
        valuation::

            sage: w = v.augmentation(x, 1)
            sage: w.residue_ring()
            Univariate Polynomial Ring in x over Finite Field of size 2 (using ...)
        """
    def reduce(self, f, check: bool = True, degree_bound=None, coefficients=None, valuations=None):
        """
        Reduce ``f`` module this valuation.

        INPUT:

        - ``f`` -- an element in the domain of this valuation

        - ``check`` -- whether or not to check whether ``f`` has nonnegative
          valuation (default: ``True``)

        - ``degree_bound`` -- an a-priori known bound on the degree of the
          result which can speed up the computation (default: not set)

        - ``coefficients`` -- the coefficients of ``f`` as produced by
          :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.coefficients`
          or ``None`` (default: ``None``); this can be used to speed up the
          computation when the expansion of ``f`` is already known from a
          previous computation.

        - ``valuations`` -- the valuations of ``coefficients`` or ``None``
          (default: ``None``)

        OUTPUT:

        an element of the :meth:`residue_ring` of this valuation, the reduction
        modulo the ideal of elements of positive valuation

        ALGORITHM:

        We follow the algorithm given in the proof of Theorem 12.1 of [Mac1936I]_:
        If ``f`` has positive valuation, the reduction is simply zero.
        Otherwise, let `f=\\sum f_i\\phi^i` be the expansion of `f`, as computed
        by
        :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.coefficients`.
        Since the valuation is zero, the exponents `i` must all be multiples of
        `\\tau`, the index the value group of the base valuation in the value
        group of this valuation.  Hence, there is an
        :meth:`~sage.rings.valuation.inductive_valuation.InductiveValuation.equivalence_unit`
        `Q` with the same valuation as `\\phi^\\tau`. Let `Q'` be its
        :meth:`~sage.rings.valuation.inductive_valuation.InductiveValuation.equivalence_reciprocal`.
        Now, rewrite each term `f_i\\phi^{i\\tau}=(f_iQ^i)(\\phi^\\tau Q^{-1})^i`;
        it turns out that the second factor in this expression is a lift of the
        generator of the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field`.
        The reduction of the first factor can be computed recursively.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.reduce(x)
            x
            sage: v.reduce(S(u))
            u0
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.reduce(S.one())
            1
            sage: w.reduce(S(2))
            0
            sage: w.reduce(S(u))
            u0
            sage: w.reduce(x)  # this gives the generator of the residue field extension of w over v
            u1
            sage: f = (x^2 + x + u)^2 / 2
            sage: w.reduce(f)
            x
            sage: w.reduce(f + x + 1)
            x + u1 + 1
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: g = ((x^2 + x + u)^2 + 2)^3 / 2^5
            sage: ww.reduce(g)
            x
            sage: ww.reduce(f)
            1
            sage: ww.is_equivalent(f, 1)
            True
            sage: ww.reduce(f * g)
            x
            sage: ww.reduce(f + g)
            x + 1
        """
    def lift(self, F, report_coefficients: bool = False):
        """
        Return a polynomial which reduces to ``F``.

        INPUT:

        - ``F`` -- an element of the :meth:`residue_ring`

        - ``report_coefficients`` -- whether to return the coefficients of the
          :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic
          expansion or the actual polynomial (default: ``False``, i.e., return
          the polynomial)

        OUTPUT:

        A polynomial in the domain of the valuation with reduction ``F``, monic
        if ``F`` is monic.

        ALGORITHM:

        Since this is the inverse of :meth:`reduce`, we only have to go backwards
        through the algorithm described there.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: y = w.residue_ring().gen()
            sage: u1 = w.residue_ring().base().gen()
            sage: w.lift(1)
            1 + O(2^10)
            sage: w.lift(0)
            0
            sage: w.lift(u1)
            (1 + O(2^10))*x
            sage: w.reduce(w.lift(y)) == y
            True
            sage: w.reduce(w.lift(y + u1 + 1)) == y + u1 + 1
            True
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: y = ww.residue_ring().gen()
            sage: u2 = ww.residue_ring().base().gen()
            sage: ww.reduce(ww.lift(y)) == y
            True
            sage: ww.reduce(ww.lift(1)) == 1
            True
            sage: ww.reduce(ww.lift(y + 1)) == y +  1
            True

        A more complicated example::

            sage: # needs sage.libs.ntl
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1)
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2*x*(x^2 + x + u) + 4*x, 3)
            sage: u = ww.residue_ring().base().gen()
            sage: F = ww.residue_ring()(u); F
            u2
            sage: f = ww.lift(F); f
            (2^-1 + O(2^9))*x^2 + (2^-1 + O(2^9))*x + u*2^-1 + O(2^9)
            sage: F == ww.reduce(f)
            True
        """
    def lift_to_key(self, F, check: bool = True):
        """
        Lift the irreducible polynomial ``F`` to a key polynomial.

        INPUT:

        - ``F`` -- an irreducible non-constant polynomial in the
          :meth:`residue_ring` of this valuation

        - ``check`` -- whether or not to check correctness of ``F`` (default:
          ``True``)

        OUTPUT:

        A polynomial `f` in the domain of this valuation which is a key
        polynomial for this valuation and which, for a suitable equivalence
        unit `R`, satisfies that the reduction of `Rf` is ``F``

        ALGORITHM:

        We follow the algorithm described in Theorem 13.1 [Mac1936I]_ which, after
        a :meth:`lift` of ``F``, essentially shifts the valuations of all terms
        in the `\\phi`-adic expansion up and then kills the leading coefficient.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: y = w.residue_ring().gen()
            sage: f = w.lift_to_key(y + 1); f
            (1 + O(2^10))*x^4 + (2 + O(2^11))*x^3 + (1 + u*2 + O(2^10))*x^2 + (u*2 + O(2^11))*x + (u + 1) + u*2 + O(2^10)
            sage: w.is_key(f)
            True

        A more complicated example::

            sage: # needs sage.libs.ntl
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1)
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2*x*(x^2 + x + u) + 4*x, 3)
            sage: u = ww.residue_ring().base().gen()
            sage: y = ww.residue_ring().gen()
            sage: f = ww.lift_to_key(y^3+y+u)
            sage: f.degree()
            12
            sage: ww.is_key(f)
            True
        """

class FiniteAugmentedValuation(AugmentedValuation_base, FiniteInductiveValuation):
    """
    A finite augmented valuation, i.e., an augmented valuation which is
    discrete, or equivalently an augmented valuation which assigns to its last
    key polynomial a finite valuation.

    EXAMPLES::

        sage: # needs sage.libs.ntl
        sage: R.<u> = Qq(4, 5)
        sage: S.<x> = R[]
        sage: v = GaussValuation(S)
        sage: w = v.augmentation(x^2 + x + u, 1/2)
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: from sage.rings.valuation.augmented_valuation import FiniteAugmentedValuation
            sage: isinstance(w, FiniteAugmentedValuation)
            True
        """
    @cached_method
    def value_group(self):
        """
        Return the value group of this valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.value_group()
            Additive Abelian Group generated by 1/2
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: ww.value_group()
            Additive Abelian Group generated by 1/6
        """
    def value_semigroup(self):
        """
        Return the value semigroup of this valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Zq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.value_semigroup()
            Additive Abelian Semigroup generated by 1/2
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: ww.value_semigroup()
            Additive Abelian Semigroup generated by 1/2, 5/3
        """
    def valuations(self, f, coefficients=None, call_error: bool = False) -> Generator[Incomplete]:
        """
        Return the valuations of the `f_i\\phi^i` in the expansion `f=\\sum_i
        f_i\\phi^i`.

        INPUT:

        - ``f`` -- a polynomial in the domain of this valuation

        - ``coefficients`` -- the coefficients of ``f`` as produced by
          :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.coefficients`
          or ``None`` (default: ``None``); this can be used to speed up the
          computation when the expansion of ``f`` is already known from a
          previous computation.

        - ``call_error`` -- whether or not to speed up the computation by
          assuming that the result is only used to compute the valuation of
          ``f`` (default: ``False``)

        OUTPUT:

        An iterator over rational numbers (or infinity) `[v(f_0), v(f_1\\phi), \\dots]`

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: list(w.valuations( x^2 + 1 ))
            [0, 1/2]
            sage: ww = w.augmentation((x^2 + x + u)^2 + 2, 5/3)
            sage: list(ww.valuations( ((x^2 + x + u)^2 + 2)^3 ))
            [+Infinity, +Infinity, +Infinity, 5]
        """
    def simplify(self, f, error=None, force: bool = False, effective_degree=None, size_heuristic_bound: int = 32, phiadic: bool = False):
        """
        Return a simplified version of ``f``.

        Produce an element which differs from ``f`` by an element of valuation
        strictly greater than the valuation of ``f`` (or strictly greater than
        ``error`` if set.)

        INPUT:

        - ``f`` -- an element in the domain of this valuation

        - ``error`` -- a rational, infinity, or ``None`` (default: ``None``),
          the error allowed to introduce through the simplification

        - ``force`` -- whether or not to simplify ``f`` even if there is
          heuristically no change in the coefficient size of ``f`` expected
          (default: ``False``)

        - ``effective_degree`` -- when set, assume that coefficients beyond
          ``effective_degree`` in the :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic development can be
          safely dropped (default: ``None``)

        - ``size_heuristic_bound`` -- when ``force`` is not set, the expected
          factor by which the coefficients need to shrink to perform an actual
          simplification (default: 32)

        - ``phiadic`` -- whether to simplify the coefficients in the
          `\\phi`-adic expansion recursively. This often times leads to huge
          coefficients in the `x`-adic expansion (default: ``False``, i.e., use
          an `x`-adic expansion.)

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.simplify(x^10/2 + 1, force=True)
            (u + 1)*2^-1 + O(2^4)

        Check that :issue:`25607` has been resolved, i.e., the coefficients
        in the following example are small::

            sage: # needs sage.libs.ntl sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 + 6)
            sage: R.<x> = K[]
            sage: v = GaussValuation(R, K.valuation(2))
            sage: v = v.augmentation(x, 3/2)
            sage: v = v.augmentation(x^2 + 8, 13/4)
            sage: v = v.augmentation(x^4 + 16*x^2 + 32*x + 64, 20/3)
            sage: F.<x> = FunctionField(K)
            sage: S.<y> = F[]
            sage: v = F.valuation(v)
            sage: G = y^2 - 2*x^5 + 8*x^3 + 80*x^2 + 128*x + 192
            sage: v.mac_lane_approximants(G)
            [[ Gauss valuation induced by
               Valuation on rational function field induced by
                 [ Gauss valuation induced by 2-adic valuation, v(x) = 3/2,
                   v(x^2 + 8) = 13/4, v(x^4 + 16*x^2 + 32*x + 64) = 20/3 ],
               v(y + 4*x + 8) = 31/8 ]]
        """
    def lower_bound(self, f):
        """
        Return a lower bound of this valuation at ``f``.

        Use this method to get an approximation of the valuation of ``f``
        when speed is more important than accuracy.

        ALGORITHM:

        The main cost of evaluation is the computation of the
        :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.coefficients`
        of the :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic
        expansion of ``f`` (which often leads to coefficient bloat.) So unless
        :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`
        is trivial, we fall back to valuation which this valuation augments
        since it is guaranteed to be smaller everywhere.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.lower_bound(x^2 + x + u)
            0
        """
    def upper_bound(self, f):
        """
        Return an upper bound of this valuation at ``f``.

        Use this method to get an approximation of the valuation of ``f``
        when speed is more important than accuracy.

        ALGORITHM:

        Any entry of :meth:`valuations` serves as an upper bound. However,
        computation of the :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic
        expansion of ``f`` is quite costly.
        Therefore, we produce an upper bound on the last entry of
        :meth:`valuations`, namely the valuation of the leading coefficient of
        ``f`` plus the valuation of the appropriate power of :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, 1/2)
            sage: w.upper_bound(x^2 + x + u)
            1/2
        """

class FinalFiniteAugmentedValuation(FiniteAugmentedValuation, FinalAugmentedValuation):
    """
    An augmented valuation which is discrete, i.e., which assigns a finite
    valuation to its last key polynomial, but which can not be further
    augmented.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
        sage: w = v.augmentation(x, 1)
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
            sage: w = v.augmentation(x, 1)
            sage: from sage.rings.valuation.augmented_valuation import FinalFiniteAugmentedValuation
            sage: isinstance(w, FinalFiniteAugmentedValuation)
            True
        """

class NonFinalFiniteAugmentedValuation(FiniteAugmentedValuation, NonFinalAugmentedValuation):
    """
    An augmented valuation which is discrete, i.e., which assigns a finite
    valuation to its last key polynomial, and which can be augmented further.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(2))
        sage: w = v.augmentation(x, 1)
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x, 1)
            sage: from sage.rings.valuation.augmented_valuation import NonFinalFiniteAugmentedValuation
            sage: isinstance(w, NonFinalFiniteAugmentedValuation)
            True
        """

class InfiniteAugmentedValuation(FinalAugmentedValuation, InfiniteInductiveValuation):
    """
    An augmented valuation which is infinite, i.e., which assigns valuation
    infinity to its last key polynomial (and which can therefore not be
    augmented further.)

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(2))
        sage: w = v.augmentation(x, infinity)
    """
    def __init__(self, parent, v, phi, mu) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x, infinity)
            sage: from sage.rings.valuation.augmented_valuation import InfiniteAugmentedValuation
            sage: isinstance(w, InfiniteAugmentedValuation)
            True
        """
    @cached_method
    def value_group(self):
        """
        Return the value group of this valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x, infinity)
            sage: w.value_group()
            Additive Abelian Group generated by 1
        """
    @cached_method
    def value_semigroup(self):
        """
        Return the value semigroup of this valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Zq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x, infinity)
            sage: w.value_semigroup()
            Additive Abelian Semigroup generated by 1
        """
    def valuations(self, f, coefficients=None, call_error: bool = False) -> Generator[Incomplete]:
        """
        Return the valuations of the `f_i\\phi^i` in the expansion `f=\\sum_i
        f_i\\phi^i`.

        INPUT:

        - ``f`` -- a polynomial in the domain of this valuation

        - ``coefficients`` -- the coefficients of ``f`` as produced by
          :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.coefficients`
          or ``None`` (default: ``None``); this can be used to speed up the
          computation when the expansion of ``f`` is already known from a
          previous computation.

        - ``call_error`` -- whether or not to speed up the computation by
          assuming that the result is only used to compute the valuation of
          ``f`` (default: ``False``)

        OUTPUT:

        An iterator over rational numbers (or infinity) `[v(f_0), v(f_1\\phi), \\dots]`

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x, infinity)
            sage: list(w.valuations(x^2 + 1))
            [0, +Infinity, +Infinity]
        """
    def simplify(self, f, error=None, force: bool = False, effective_degree=None):
        """
        Return a simplified version of ``f``.

        Produce an element which differs from ``f`` by an element of valuation
        strictly greater than the valuation of ``f`` (or strictly greater than
        ``error`` if set.)

        INPUT:

        - ``f`` -- an element in the domain of this valuation

        - ``error`` -- a rational, infinity, or ``None`` (default: ``None``),
          the error allowed to introduce through the simplification

        - ``force`` -- whether or not to simplify ``f`` even if there is
          heuristically no change in the coefficient size of ``f`` expected
          (default: ``False``)

        - ``effective_degree`` -- ignored; for compatibility with other
          ``simplify`` methods

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, infinity)
            sage: w.simplify(x^10/2 + 1, force=True)
            (u + 1)*2^-1 + O(2^4)
        """
    def lower_bound(self, f):
        """
        Return a lower bound of this valuation at ``f``.

        Use this method to get an approximation of the valuation of ``f``
        when speed is more important than accuracy.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, infinity)
            sage: w.lower_bound(x^2 + x + u)
            +Infinity
        """
    def upper_bound(self, f):
        """
        Return an upper bound of this valuation at ``f``.

        Use this method to get an approximation of the valuation of ``f``
        when speed is more important than accuracy.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: w = v.augmentation(x^2 + x + u, infinity)
            sage: w.upper_bound(x^2 + x + u)
            +Infinity
        """
