from .developing_valuation import DevelopingValuation as DevelopingValuation
from .valuation import DiscreteValuation as DiscreteValuation, InfiniteDiscretePseudoValuation as InfiniteDiscretePseudoValuation
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method

class InductiveValuation(DevelopingValuation):
    """
    Abstract base class for iterated :mod:`augmented valuations <sage.rings.valuation.augmented_valuation>` on top of a :mod:`Gauss valuation <sage.rings.valuation.gauss_valuation>`.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(5))

    TESTS::

        sage: TestSuite(v).run()                # long time                             # needs sage.geometry.polyhedron
    """
    def is_equivalence_unit(self, f, valuations=None):
        """
        Return whether the polynomial ``f`` is an equivalence unit, i.e., an
        element of :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.effective_degree`
        zero (see [Mac1936II]_ p.497.)

        INPUT:

        - ``f`` -- a polynomial in the domain of this valuation

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R = Zp(2,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.is_equivalence_unit(x)
            False
            sage: v.is_equivalence_unit(S.zero())
            False
            sage: v.is_equivalence_unit(2*x + 1)
            True
        """
    def equivalence_reciprocal(self, f, coefficients=None, valuations=None, check: bool = True):
        """
        Return an equivalence reciprocal of ``f``.

        An equivalence reciprocal of `f` is a polynomial `h` such that `f\\cdot
        h` is equivalent to 1 modulo this valuation (see [Mac1936II]_ p.497.)

        INPUT:

        - ``f`` -- a polynomial in the domain of this valuation which is an
          :meth:`equivalence_unit`

        - ``coefficients`` -- the coefficients of ``f`` in the :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic
          expansion if known (default: ``None``)

        - ``valuations`` -- the valuations of ``coefficients`` if known
          (default: ``None``)

        - ``check`` -- whether or not to check the validity of ``f`` (default:
          ``True``)

        .. WARNING::

            This method may not work over `p`-adic rings due to problems with
            the xgcd implementation there.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R = Zp(3,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: f = 3*x + 2
            sage: h = v.equivalence_reciprocal(f); h
            2 + O(3^5)
            sage: v.is_equivalent(f*h, 1)
            True

        In an extended valuation over an extension field::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v = v.augmentation(x^2 + x + u, 1)
            sage: f = 2*x + u
            sage: h = v.equivalence_reciprocal(f); h
            (u + 1) + O(2^5)
            sage: v.is_equivalent(f*h, 1)
            True

        Extending the valuation once more::

            sage: # needs sage.libs.ntl
            sage: v = v.augmentation((x^2 + x + u)^2 + 2*x*(x^2 + x + u) + 4*x, 3)
            sage: h = v.equivalence_reciprocal(f); h
            (u + 1) + O(2^5)
            sage: v.is_equivalent(f*h, 1)
            True

        TESTS:

        A case that caused problems at some point::

            sage: # needs sage.libs.ntl
            sage: K = Qp(2, 4)
            sage: R.<x> = K[]
            sage: L.<a> = K.extension(x^4 + 4*x^3 + 6*x^2 + 4*x + 2)
            sage: R.<t> = L[]
            sage: v = GaussValuation(R)
            sage: w = v.augmentation(t + 1, 5/16)
            sage: w = w.augmentation(t^4 + (a^8 + a^12 + a^14 + a^16 + a^17 + a^19 + a^20 + a^23)*t^3 + (a^6 + a^9 + a^13 + a^15 + a^18 + a^19 + a^21)*t^2 + a^10*t + 1 + a^4 + a^5 + a^8 + a^13 + a^14 + a^15, 17/8)
            sage: f = a^-15*t^2 + (a^-11 + a^-9 + a^-6 + a^-5 + a^-3 + a^-2)*t + a^-15
            sage: f_ = w.equivalence_reciprocal(f)
            sage: w.reduce(f*f_)
            1
            sage: f = f.parent()([f[0], f[1].add_bigoh(1), f[2]])
            sage: f_ = w.equivalence_reciprocal(f)
            sage: w.reduce(f*f_)
            1
        """
    @cached_method
    def mu(self):
        """
        Return the valuation of :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: v.mu()
            0
        """
    @abstract_method
    def equivalence_unit(self, s, reciprocal: bool = False) -> None:
        """
        Return an equivalence unit of valuation ``s``.

        INPUT:

        - ``s`` -- an element of the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.value_group`

        - ``reciprocal`` -- boolean (default: ``False``); whether or not to
          return the equivalence unit as the :meth:`equivalence_reciprocal` of
          the equivalence unit of valuation ``-s``.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: S.<x> = Qp(3,5)[]
            sage: v = GaussValuation(S)
            sage: v.equivalence_unit(2)
            3^2 + O(3^7)
            sage: v.equivalence_unit(-2)
            3^-2 + O(3^3)

        Note that this might fail for negative ``s`` if the domain is not
        defined over a field::

            sage: v = ZZ.valuation(2)
            sage: R.<x> = ZZ[]
            sage: w = GaussValuation(R, v)
            sage: w.equivalence_unit(1)
            2
            sage: w.equivalence_unit(-1)
            Traceback (most recent call last):
            ...
            ValueError: s must be in the value semigroup of this valuation
            but -1 is not in Additive Abelian Semigroup generated by 1
        """
    @abstract_method
    def augmentation_chain(self) -> None:
        """
        Return a list with the chain of augmentations down to the underlying
        :mod:`Gauss valuation <sage.rings.valuation.gauss_valuation>`.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.augmentation_chain()
            [Gauss valuation induced by 2-adic valuation]
        """
    @abstract_method
    def is_gauss_valuation(self) -> None:
        """
        Return whether this valuation is a Gauss valuation over the domain.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.is_gauss_valuation()
            True
        """
    @abstract_method
    def E(self) -> None:
        """
        Return the ramification index of this valuation over its underlying
        Gauss valuation.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.E()
            1
        """
    @abstract_method
    def F(self) -> None:
        """
        Return the residual degree of this valuation over its Gauss extension.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.F()
            1
        """
    @abstract_method
    def monic_integral_model(self, G) -> None:
        """
        Return a monic integral irreducible polynomial which defines the same
        extension of the base ring of the domain as the irreducible polynomial
        ``G`` together with maps between the old and the new polynomial.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: v.monic_integral_model(5*x^2 + 1/2*x + 1/4)
            (Ring endomorphism of Univariate Polynomial Ring in x over Rational Field
               Defn: x |--> 1/2*x,
             Ring endomorphism of Univariate Polynomial Ring in x over Rational Field
               Defn: x |--> 2*x,
             x^2 + 1/5*x + 1/5)
        """
    @abstract_method
    def element_with_valuation(self, s) -> None:
        """
        Return a polynomial of minimal degree with valuation ``s``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: v.element_with_valuation(-2)
            1/4

        Depending on the base ring, an element of valuation ``s`` might not
        exist::

            sage: R.<x> = ZZ[]
            sage: v = GaussValuation(R, ZZ.valuation(2))
            sage: v.element_with_valuation(-2)
            Traceback (most recent call last):
            ...
            ValueError: s must be in the value semigroup of this valuation
            but -2 is not in Additive Abelian Semigroup generated by 1
        """

class FiniteInductiveValuation(InductiveValuation, DiscreteValuation):
    """
    Abstract base class for iterated :mod:`augmented valuations <sage.rings.valuation.augmented_valuation>`
    on top of a :mod:`Gauss valuation <sage.rings.valuation.gauss_valuation>` which is a discrete valuation,
    i.e., the last key polynomial has finite valuation.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
    """
    def __init__(self, parent, phi) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
            sage: from sage.rings.valuation.inductive_valuation import FiniteInductiveValuation
            sage: isinstance(v, FiniteInductiveValuation)
            True
        """
    def extensions(self, other):
        """
        Return the extensions of this valuation to ``other``.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: v = GaussValuation(R, valuations.TrivialValuation(ZZ))
            sage: K.<x> = FunctionField(QQ)
            sage: v.extensions(K)
            [Trivial valuation on Rational Field]
        """

class NonFinalInductiveValuation(FiniteInductiveValuation, DiscreteValuation):
    """
    Abstract base class for iterated :mod:`augmented valuations <sage.rings.valuation.augmented_valuation>`
    on top of a :mod:`Gauss valuation <sage.rings.valuation.gauss_valuation>` which can be extended further
    through :meth:`augmentation`.

    EXAMPLES::

        sage: # needs sage.libs.ntl
        sage: R.<u> = Qq(4,5)
        sage: S.<x> = R[]
        sage: v = GaussValuation(S)
        sage: v = v.augmentation(x^2 + x + u, 1)
    """
    def __init__(self, parent, phi) -> None:
        """
        TESTS::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v = v.augmentation(x^2 + x + u, 1)
            sage: from sage.rings.valuation.inductive_valuation import NonFinalInductiveValuation
            sage: isinstance(v, NonFinalInductiveValuation)
            True
        """
    def augmentation(self, phi, mu, check: bool = True):
        """
        Return the inductive valuation which extends this valuation by mapping
        ``phi`` to ``mu``.

        INPUT:

        - ``phi`` -- a polynomial in the domain of this valuation; this must be
          a key polynomial, see :meth:`is_key` for properties of key
          polynomials.

        - ``mu`` -- a rational number or infinity, the valuation of ``phi`` in
          the extended valuation

        - ``check`` -- boolean (default: ``True``); whether or not to check
          the correctness of the parameters

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v = v.augmentation(x^2 + x + u, 1)
            sage: v = v.augmentation((x^2 + x + u)^2 + 2*x*(x^2 + x + u) + 4*x, 3)
            sage: v
            [ Gauss valuation induced by 2-adic valuation,
              v((1 + O(2^5))*x^2 + (1 + O(2^5))*x + u + O(2^5)) = 1,
              v((1 + O(2^5))*x^4
                + (2^2 + O(2^6))*x^3
                + (1 + (u + 1)*2 + O(2^5))*x^2
                + ((u + 1)*2^2 + O(2^6))*x
                + (u + 1) + (u + 1)*2 + (u + 1)*2^2 + (u + 1)*2^3 + (u + 1)*2^4 + O(2^5)) = 3 ]

        TESTS:

        Make sure that we do not make the assumption that the degrees of the
        key polynomials are strictly increasing::

            sage: v_K = QQ.valuation(3)
            sage: A.<t> = QQ[]
            sage: v0 = GaussValuation(A,v_K)

            sage: v1 = v0.augmentation(t, 1/12)
            sage: v2 = v1.augmentation(t^12 + 3, 7/6)
            sage: v3 = v2.augmentation(t^12 + 3*t^2 + 3, 9/4)
            sage: v4 = v1.augmentation(t^12 + 3*t^2 + 3, 9/4)
            sage: v3 <= v4 and v3 >= v4
            True

        .. SEEALSO::

            :mod:`~sage.rings.valuation.augmented_valuation`
        """
    def mac_lane_step(self, G, principal_part_bound=None, assume_squarefree: bool = False, assume_equivalence_irreducible: bool = False, report_degree_bounds_and_caches: bool = False, coefficients=None, valuations=None, check: bool = True, allow_equivalent_key: bool = True):
        """
        Perform an approximation step towards the squarefree monic non-constant
        integral polynomial ``G`` which is not an :meth:`equivalence unit <InductiveValuation.is_equivalence_unit>`.

        This performs the individual steps that are used in
        :meth:`~sage.rings.valuation.valuation.DiscreteValuation.mac_lane_approximants`.

        INPUT:

        - ``G`` -- a squarefree monic non-constant integral polynomial ``G``
          which is not an :meth:`equivalence unit <InductiveValuation.is_equivalence_unit>`

        - ``principal_part_bound`` -- integer or ``None`` (default:
          ``None``), a bound on the length of the principal part, i.e., the
          section of negative slope, of the Newton polygon of ``G``

        - ``assume_squarefree`` -- whether or not to assume that ``G`` is
          squarefree (default: ``False``)

        - ``assume_equivalence_irreducible`` -- whether or not to assume that
          ``G`` is equivalence irreducible (default: ``False``)

        - ``report_degree_bounds_and_caches`` -- whether or not to include internal state with the returned value (used by :meth:`~sage.rings.valuation.valuation.DiscreteValuation.mac_lane_approximants` to speed up sequential calls)

        - ``coefficients`` -- the coefficients of ``G`` in the :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic expansion if known (default: ``None``)

        - ``valuations`` -- the valuations of ``coefficients`` if known
          (default: ``None``)

        - ``check`` -- whether to check that ``G`` is a squarefree monic
          non-constant  integral polynomial and not an :meth:`equivalence unit <InductiveValuation.is_equivalence_unit>`
          (default: ``True``)

        - ``allow_equivalent_key`` -- whether to return valuations which end in
          essentially the same key polynomial as this valuation but have a
          higher valuation assigned to that key polynomial (default: ``True``)

        EXAMPLES:

        We can use this method to perform the individual steps of
        :meth:`~sage.rings.valuation.valuation.DiscreteValuation.mac_lane_approximants`::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(2)
            sage: f = x^36 + 1160/81*x^31 + 9920/27*x^30 + 1040/81*x^26 + 52480/81*x^25 + 220160/81*x^24 - 5120/81*x^21 - 143360/81*x^20 - 573440/81*x^19 + 12451840/81*x^18 - 266240/567*x^16 - 20316160/567*x^15 - 198737920/189*x^14 - 1129840640/81*x^13 - 1907359744/27*x^12 + 8192/81*x^11 + 655360/81*x^10 + 5242880/21*x^9 + 2118123520/567*x^8 + 15460204544/567*x^7 + 6509559808/81*x^6 - 16777216/567*x^2 - 268435456/567*x - 1073741824/567
            sage: v.mac_lane_approximants(f)                                            # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x + 2056) = 23/2 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 11/9 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 2/5, v(x^5 + 4) = 7/2 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3/5, v(x^10 + 8*x^5 + 64) = 7 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3/5, v(x^5 + 8) = 5 ]]

        Starting from the Gauss valuation, a MacLane step branches off with
        some linear key polynomials in the above example::

            sage: v0 = GaussValuation(R, v)
            sage: V1 = sorted(v0.mac_lane_step(f)); V1                                  # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x) = 2/5 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3/5 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 11/9 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3 ]]

        The computation of MacLane approximants would now perform a MacLane
        step on each of these branches, note however, that a direct call to
        this method might produce some unexpected results::

            sage: V1[1].mac_lane_step(f)                                                # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x) = 3/5, v(x^5 + 8) = 5 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3/5, v(x^10 + 8*x^5 + 64) = 7 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 11/9 ]]

        Note how this detected the two augmentations of ``V1[1]`` but also two
        other valuations that we had seen in the previous step and that are
        greater than ``V1[1]``. To ignore such trivial augmentations, we can
        set ``allow_equivalent_key``::

            sage: V1[1].mac_lane_step(f, allow_equivalent_key=False)                    # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x) = 3/5, v(x^5 + 8) = 5 ],
             [ Gauss valuation induced by 2-adic valuation, v(x) = 3/5, v(x^10 + 8*x^5 + 64) = 7 ]]

        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: S.<y> = K[]
            sage: F = y^2 - x^2 - x^3 - 3
            sage: v0 = GaussValuation(K._ring, QQ.valuation(3))
            sage: v1 = v0.augmentation(K._ring.gen(), 1/3)
            sage: mu0 = K.valuation(v1)
            sage: eta0 = GaussValuation(S, mu0)
            sage: eta1 = eta0.mac_lane_step(F)[0]                                       # needs sage.geometry.polyhedron
            sage: eta2 = eta1.mac_lane_step(F)[0]                                       # needs sage.geometry.polyhedron
            sage: eta2                                                                  # needs sage.geometry.polyhedron
            [ Gauss valuation induced by Valuation on rational function field induced by [ Gauss valuation induced by 3-adic valuation, v(x) = 1/3 ], v(y + x) = 2/3 ]

        Check that :issue:`26066` has been resolved::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(2)
            sage: v = GaussValuation(R, v).augmentation(x+1, 1/2)
            sage: f = x^4 - 30*x^2 - 75
            sage: v.mac_lane_step(f)                                                    # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x + 1) = 3/4 ]]
        """
    def is_key(self, phi, explain: bool = False, assume_equivalence_irreducible: bool = False):
        """
        Return whether ``phi`` is a key polynomial for this valuation, i.e.,
        whether it is monic, whether it :meth:`is_equivalence_irreducible`, and
        whether it is :meth:`is_minimal`.

        INPUT:

        - ``phi`` -- a polynomial in the domain of this valuation

        - ``explain`` -- boolean (default: ``False``); if ``True``, return a
          string explaining why ``phi`` is not a key polynomial

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.is_key(x)
            True
            sage: v.is_key(2*x, explain=True)
            (False, 'phi must be monic')
            sage: v.is_key(x^2, explain=True)
            (False, 'phi must be equivalence irreducible')
            sage: w = v.augmentation(x, 1)
            sage: w.is_key(x + 1, explain = True)
            (False, 'phi must be minimal')
        """
    def is_minimal(self, f, assume_equivalence_irreducible: bool = False):
        """
        Return whether the polynomial ``f`` is minimal with respect to this
        valuation.

        A polynomial `f` is minimal with respect to `v` if it is not a constant
        and any nonzero polynomial `h` which is `v`-divisible by `f` has at
        least the degree of `f`.

        A polynomial `h` is `v`-divisible by `f` if there is a polynomial `c`
        such that `fc` :meth:`~sage.rings.valuation.valuation.DiscretePseudoValuation.is_equivalent` to `h`.

        ALGORITHM:

        Based on Theorem 9.4 of [Mac1936II]_.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4, 5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.is_minimal(x + 1)
            True
            sage: w = v.augmentation(x, 1)
            sage: w.is_minimal(x + 1)
            False

        TESTS::

            sage: # needs sage.libs.ntl
            sage: K = Qp(2, 10)
            sage: R.<x> = K[]
            sage: vp = K.valuation()
            sage: v0 = GaussValuation(R, vp)
            sage: v1 = v0.augmentation(x, 1/4)
            sage: v2 = v1.augmentation(x^4 + 2, 5/4)
            sage: v2.is_minimal(x^5 + x^4 + 2)
            False

        Polynomials which are equivalent to the key polynomial are minimal if
        and only if they have the same degree as the key polynomial::

            sage: v2.is_minimal(x^4 + 2)                                                # needs sage.libs.ntl
            True
            sage: v2.is_minimal(x^4 + 4)                                                # needs sage.libs.ntl
            False
        """
    def is_equivalence_irreducible(self, f, coefficients=None, valuations=None):
        """
        Return whether the polynomial ``f`` is equivalence-irreducible, i.e.,
        whether its :meth:`equivalence_decomposition` is trivial.

        ALGORITHM:

        We use the same algorithm as in :meth:`equivalence_decomposition` we
        just do not lift the result to key polynomials.

        INPUT:

        - ``f`` -- a non-constant polynomial in the domain of this valuation

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.is_equivalence_irreducible(x)
            True
            sage: v.is_equivalence_irreducible(x^2)
            False
            sage: v.is_equivalence_irreducible(x^2 + 2)
            False
        """
    def equivalence_decomposition(self, f, assume_not_equivalence_unit: bool = False, coefficients=None, valuations=None, compute_unit: bool = True, degree_bound=None):
        """
        Return an equivalence decomposition of ``f``, i.e., a polynomial
        `g(x)=e(x)\\prod_i \\phi_i(x)` with `e(x)` an :meth:`equivalence unit
        <InductiveValuation.is_equivalence_unit>` and the `\\phi_i` :meth:`key
        polynomials <is_key>` such that ``f`` :meth:`~sage.rings.valuation.valuation.DiscretePseudoValuation.is_equivalent` to `g`.

        INPUT:

        - ``f`` -- a nonzero polynomial in the domain of this valuation

        - ``assume_not_equivalence_unit`` -- whether or not to assume that
          ``f`` is not an :meth:`equivalence unit <InductiveValuation.is_equivalence_unit>`
          (default: ``False``)

        - ``coefficients`` -- the coefficients of ``f`` in the
          :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.phi`-adic
          expansion if known (default: ``None``)

        - ``valuations`` -- the valuations of ``coefficients`` if known
          (default: ``None``)

        - ``compute_unit`` -- whether or not to compute the unit part of the
          decomposition (default: ``True``)

        - ``degree_bound`` -- a bound on the degree of the
          :meth:`_equivalence_reduction` of ``f`` (default: ``None``)

        ALGORITHM:

        We use the algorithm described in Theorem 4.4 of [Mac1936II]_. After
        removing all factors `\\phi` from a polynomial `f`, there is an
        equivalence unit `R` such that `Rf` has valuation zero. Now `Rf` can be
        factored as `\\prod_i \\alpha_i` over the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field`. Lifting
        all `\\alpha_i` to key polynomials `\\phi_i` gives `Rf=\\prod_i R_i f_i`
        for suitable equivalence units `R_i` (see :meth:`lift_to_key`). Taking
        `R'` an :meth:`~InductiveValuation.equivalence_reciprocal` of `R`, we have `f` equivalent
        to `(R'\\prod_i R_i)\\prod_i\\phi_i`.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.equivalence_decomposition(S.zero())
            Traceback (most recent call last):
            ...
            ValueError: equivalence decomposition of zero is not defined
            sage: v.equivalence_decomposition(S.one())
            1 + O(2^10)
            sage: v.equivalence_decomposition(x^2+2)
            ((1 + O(2^10))*x)^2
            sage: v.equivalence_decomposition(x^2+1)
            ((1 + O(2^10))*x + 1 + O(2^10))^2

        A polynomial that is an equivalence unit, is returned as the unit part
        of a :class:`~sage.structure.factorization.Factorization`, leading to a unit
        non-minimal degree::

            sage: w = v.augmentation(x, 1)                                              # needs sage.libs.ntl
            sage: F = w.equivalence_decomposition(x^2+1); F                             # needs sage.libs.ntl
            (1 + O(2^10))*x^2 + 1 + O(2^10)
            sage: F.unit()                                                              # needs sage.libs.ntl
            (1 + O(2^10))*x^2 + 1 + O(2^10)

        However, if the polynomial has a non-unit factor, then the unit might
        be replaced by a factor of lower degree::

            sage: f = x * (x^2 + 1)                                                     # needs sage.libs.ntl
            sage: F = w.equivalence_decomposition(f); F                                 # needs sage.libs.ntl
            (1 + O(2^10))*x
            sage: F.unit()                                                              # needs sage.libs.ntl
            1 + O(2^10)

        Examples over an iterated unramified extension::

            sage: # needs sage.libs.ntl
            sage: v = v.augmentation(x^2 + x + u, 1)
            sage: v = v.augmentation((x^2 + x + u)^2 + 2*x*(x^2 + x + u) + 4*x, 3)
            sage: v.equivalence_decomposition(x)
            (1 + O(2^10))*x
            sage: F = v.equivalence_decomposition( v.phi() )
            sage: len(F)
            1
            sage: F = v.equivalence_decomposition( v.phi() * (x^4 + 4*x^3 + (7 + 2*u)*x^2 + (8 + 4*u)*x + 1023 + 3*u) )
            sage: len(F)
            2

        TESTS::

            sage: # needs sage.geometry.polyhedron sage.groups sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K1.<pi> = NumberField(x^3 - 2)
            sage: K.<alpha> = K1.galois_closure()
            sage: R.<x> = K[]
            sage: vp = QQ.valuation(2)
            sage: vp = vp.extension(K)
            sage: v0 = GaussValuation(R, vp)
            sage: G = x^36 + 36*x^35 + 630*x^34 + 7144*x^33 + 59055*x^32 + 379688*x^31 +1978792*x^30 + 8604440*x^29 + 31895428*x^28 + 102487784*x^27 + 289310720*x^26 + 725361352*x^25 + 1629938380*x^24 + 3307417800*x^23 + 6098786184*x^22+10273444280*x^21 + 15878121214*x^20 + 22596599536*x^19 + 29695703772*x^18 +36117601976*x^17 + 40722105266*x^16 + 42608585080*x^15 + 41395961848*x^14 +37344435656*x^13 + 31267160756*x^12 + 24271543640*x^11 + 17439809008*x^10 + 11571651608*x^9 + 7066815164*x^8 + 3953912472*x^7 + 2013737432*x^6 + 925014888*x^5 + 378067657*x^4 + 134716588*x^3 + 40441790*x^2 + 9532544*x + 1584151
            sage: v1 = v0.mac_lane_step(G)[0]
            sage: V = v1.mac_lane_step(G)
            sage: v2 = V[0]
            sage: F = v2.equivalence_decomposition(G); F
            (x^4 + 2*alpha + 1)^3 * (x^4 + 1/2*alpha^4 + alpha + 1)^3 * (x^4 + 1/2*alpha^4 + 3*alpha + 1)^3
            sage: v2.is_equivalent(F.prod(), G)
            True

        Check that :issue:`33422` is fixed::

            sage: R.<x> = QQ[]
            sage: v_7 = QQ.valuation(7)
            sage: v0 = GaussValuation(R, v_7)
            sage: v1 = v0.augmentation(x, 3/2)
            sage: v2 = v1.augmentation(x^2-686, 7/2)
            sage: f = x^4 - 8001504*x^2 - 592815428352
            sage: F = v2.equivalence_decomposition(f); F
            x^4 - 343/2*x^2 + 1294139
            sage: v2.is_equivalent(F.prod(), f)
            True
        """
    def minimal_representative(self, f):
        """
        Return a minimal representative for ``f``, i.e., a pair `e, a` such
        that ``f`` :meth:`~sage.rings.valuation.valuation.DiscretePseudoValuation.is_equivalent` to `e a`, `e` is an
        :meth:`equivalence unit <InductiveValuation.is_equivalence_unit>`, and `a` :meth:`is_minimal` and monic.

        INPUT:

        - ``f`` -- a nonzero polynomial which is not an equivalence unit

        OUTPUT: a factorization which has `e` as its unit and `a` as its unique factor

        ALGORITHM:

        We use the algorithm described in the proof of Lemma 4.1 of [Mac1936II]_.
        In the expansion `f=\\sum_i f_i\\phi^i` take `e=f_i` for the largest `i`
        with `f_i\\phi^i` minimal (see :meth:`~sage.rings.valuation.developing_valuation.DevelopingValuation.effective_degree`).
        Let `h` be the :meth:`~InductiveValuation.equivalence_reciprocal` of `e` and take `a` given
        by the terms of minimal valuation in the expansion of `e f`.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.minimal_representative(x + 2)
            (1 + O(2^10))*x

            sage: # needs sage.libs.ntl
            sage: v = v.augmentation(x, 1)
            sage: v.minimal_representative(x + 2)
            (1 + O(2^10))*x + 2 + O(2^11)
            sage: f = x^3 + 6*x + 4
            sage: F = v.minimal_representative(f); F
            (2 + 2^2 + O(2^11)) * ((1 + O(2^10))*x + 2 + O(2^11))
            sage: v.is_minimal(F[0][0])
            True
            sage: v.is_equivalent(F.prod(), f)
            True
        """
    @abstract_method
    def lift_to_key(self, F) -> None:
        """
        Lift the irreducible polynomial ``F`` from the
        :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_ring`
        to a key polynomial over this valuation.

        INPUT:

        - ``F`` -- an irreducible non-constant monic polynomial in
          :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_ring`
          of this valuation

        OUTPUT:

        A polynomial `f` in the domain of this valuation which is a key
        polynomial for this valuation and which is such that an
        :meth:`augmentation` with this polynomial adjoins a root of ``F`` to
        the resulting :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_ring`.

        More specifically, if ``F`` is not the generator of the residue ring,
        then multiplying ``f`` with the :meth:`~InductiveValuation.equivalence_reciprocal` of the
        :meth:`~InductiveValuation.equivalence_unit` of the valuation of ``f``, produces a unit
        which reduces to ``F``.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<u> = Qq(4,10)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: y = v.residue_ring().gen()
            sage: u0 = v.residue_ring().base_ring().gen()
            sage: f = v.lift_to_key(y^2 + y + u0); f
            (1 + O(2^10))*x^2 + (1 + O(2^10))*x + u + O(2^10)
        """

class FinalInductiveValuation(InductiveValuation):
    """
    Abstract base class for an inductive valuation which cannot be augmented further.

    TESTS::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, valuations.TrivialValuation(QQ))
        sage: w = v.augmentation(x^2 + x + 1, infinity)
        sage: from sage.rings.valuation.inductive_valuation import FinalInductiveValuation
        sage: isinstance(w, FinalInductiveValuation)
        True
    """

class InfiniteInductiveValuation(FinalInductiveValuation, InfiniteDiscretePseudoValuation):
    """
    Abstract base class for an inductive valuation which is not discrete, i.e.,
    which assigns infinite valuation to its last key polynomial.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(2))
        sage: w = v.augmentation(x^2 + x + 1, infinity)
    """
    def __init__(self, parent, base_valuation) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, infinity)
            sage: from sage.rings.valuation.inductive_valuation import InfiniteInductiveValuation
            sage: isinstance(w, InfiniteInductiveValuation)
            True
        """
    def change_domain(self, ring):
        """
        Return this valuation over ``ring``.

        EXAMPLES:

        We can turn an infinite valuation into a valuation on the quotient::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = v.augmentation(x^2 + x + 1, infinity)
            sage: w.change_domain(R.quo(x^2 + x + 1))
            2-adic valuation
        """
