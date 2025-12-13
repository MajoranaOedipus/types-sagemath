from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.rings.valuation.mapped_valuation import FiniteExtensionFromLimitValuation as FiniteExtensionFromLimitValuation
from sage.rings.valuation.valuation import DiscreteValuation as DiscreteValuation
from sage.rings.valuation.value_group import DiscreteValueSemigroup as DiscreteValueSemigroup
from sage.structure.factory import UniqueFactory as UniqueFactory

class PadicValuationFactory(UniqueFactory):
    """
    Create a ``prime``-adic valuation on ``R``.

    INPUT:

    - ``R`` -- a subring of a number field or a subring of a local field in
      characteristic zero

    - ``prime`` -- a prime that does not split, a discrete (pseudo-)valuation,
      a fractional ideal, or ``None`` (default: ``None``)

    EXAMPLES:

    For integers and rational numbers, ``prime`` is just a prime of the
    integers::

        sage: valuations.pAdicValuation(ZZ, 3)
        3-adic valuation

        sage: valuations.pAdicValuation(QQ, 3)
        3-adic valuation

    ``prime`` may be ``None`` for local rings::

        sage: valuations.pAdicValuation(Qp(2))
        2-adic valuation

        sage: valuations.pAdicValuation(Zp(2))
        2-adic valuation

    But it must be specified in all other cases::

        sage: valuations.pAdicValuation(ZZ)
        Traceback (most recent call last):
        ...
        ValueError: prime must be specified for this ring

    It can sometimes be beneficial to define a number field extension as a
    quotient of a polynomial ring (since number field extensions always compute
    an absolute polynomial defining the extension which can be very costly)::

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<a> = NumberField(x^2 + 1)
        sage: R.<x> = K[]
        sage: L.<b> = R.quo(x^2 + a)
        sage: valuations.pAdicValuation(L, 2)
        2-adic valuation

    .. SEEALSO::

        :meth:`NumberField_generic.valuation() <sage.rings.number_field.number_field.NumberField_generic.valuation>`,
        :meth:`Order.valuation() <sage.rings.number_field.order.Order.valuation>`,
        :meth:`pAdicGeneric.valuation() <sage.rings.padics.padic_generic.pAdicGeneric.valuation>`,
        :meth:`RationalField.valuation() <sage.rings.rational_field.RationalField.valuation>`,
        :meth:`IntegerRing_class.valuation() <sage.rings.integer_ring.IntegerRing_class.valuation>`.
    """
    def create_key_and_extra_args(self, R, prime=None, approximants=None):
        """
        Create a unique key identifying the valuation of ``R`` with respect to
        ``prime``.

        EXAMPLES::

            sage: QQ.valuation(2)  # indirect doctest
            2-adic valuation
        """
    def create_key_for_integers(self, R, prime):
        """
        Create a unique key identifying the valuation of ``R`` with respect to
        ``prime``.

        EXAMPLES::

            sage: QQ.valuation(2)  # indirect doctest
            2-adic valuation
        """
    def create_key_for_local_ring(self, R, prime):
        """
        Create a unique key identifying the valuation of ``R`` with respect to
        ``prime``.

        EXAMPLES::

            sage: Qp(2).valuation()  # indirect doctest
            2-adic valuation
        """
    def create_key_and_extra_args_for_number_field(self, R, prime, approximants):
        """
        Create a unique key identifying the valuation of ``R`` with respect to
        ``prime``.

        EXAMPLES::

            sage: GaussianIntegers().valuation(2)  # indirect doctest                   # needs sage.rings.number_field
            2-adic valuation
        """
    def create_key_and_extra_args_for_number_field_from_valuation(self, R, v, prime, approximants):
        """
        Create a unique key identifying the valuation of ``R`` with respect to
        ``v``.

        .. NOTE::

            ``prime``, the original parameter that was passed to
            :meth:`create_key_and_extra_args`, is only used to provide more
            meaningful error messages

        EXAMPLES::

            sage: GaussianIntegers().valuation(ZZ.valuation(2))  # indirect doctest     # needs sage.rings.number_field
            2-adic valuation

        TESTS:

        We can extend to the field of fractions of a quotient ring::

            sage: R.<x> = ZZ[]
            sage: S = R.quo(x^2 + 1)
            sage: v = valuations.pAdicValuation(S, 2)                                   # needs sage.geometry.polyhedron
            sage: R.<x> = QQ[]
            sage: S = R.quo(x^2 + 1)
            sage: v = valuations.pAdicValuation(S, v)                                   # needs sage.geometry.polyhedron
        """
    def create_key_and_extra_args_for_number_field_from_ideal(self, R, I, prime):
        """
        Create a unique key identifying the valuation of ``R`` with respect to
        ``I``.

        .. NOTE::

            ``prime``, the original parameter that was passed to
            :meth:`create_key_and_extra_args`, is only used to provide more
            meaningful error messages

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: GaussianIntegers().valuation(GaussianIntegers().number_field().fractional_ideal(2))  # indirect doctest
            2-adic valuation

        TESTS:

        Verify that :issue:`28976` has been resolved::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^6 - 18*x^4 - 24*x^3 + 27*x^2 + 36*x - 6)
            sage: I = K.fractional_ideal((2, -7/44*a^5 + 19/44*a^4 + 87/44*a^3 - 87/44*a^2 - 5/2*a + 39/22))
            sage: I.norm()
            2
            sage: I in K.primes_above(2)
            True
            sage: K.valuation(I)
            [ 2-adic valuation, v(x + 1) = 1/2 ]-adic valuation

        ::

            sage: # needs sage.rings.number_field
            sage: K.<a, b> = NumberField([x^2 - 2, x^2 + x + 1])
            sage: K.valuation(2)
            2-adic valuation
        """
    def create_object(self, version, key, **extra_args):
        """
        Create a `p`-adic valuation from ``key``.

        EXAMPLES::

            sage: ZZ.valuation(5)  # indirect doctest
            5-adic valuation
        """

pAdicValuation: Incomplete

class pAdicValuation_base(DiscreteValuation):
    """
    Abstract base class for `p`-adic valuations.

    INPUT:

    - ``ring`` -- an integral domain

    - ``p`` -- a rational prime over which this valuation lies, not
      necessarily a uniformizer for the valuation

    EXAMPLES::

        sage: ZZ.valuation(3)
        3-adic valuation

        sage: QQ.valuation(5)
        5-adic valuation

     For `p`-adic rings, ``p`` has to match the `p` of the ring. ::

        sage: v = valuations.pAdicValuation(Zp(3), 2); v
        Traceback (most recent call last):
        ...
        ValueError: prime must be an element of positive valuation

    TESTS::

        sage: TestSuite(ZZ.valuation(3)).run()  # long time                             # needs sage.geometry.polyhedron
        sage: TestSuite(QQ.valuation(5)).run()  # long time                             # needs sage.geometry.polyhedron
        sage: TestSuite(Zp(5).valuation()).run()        # long time                     # needs sage.geometry.polyhedron
    """
    def __init__(self, parent, p) -> None:
        """
        TESTS::

            sage: from sage.rings.padics.padic_valuation import pAdicValuation_base
            sage: isinstance(ZZ.valuation(3), pAdicValuation_base)
            True
        """
    def p(self):
        """
        Return the `p` of this `p`-adic valuation.

        EXAMPLES::

            sage: GaussianIntegers().valuation(2).p()                                   # needs sage.rings.number_field
            2
        """
    def reduce(self, x):
        """
        Reduce ``x`` modulo the ideal of elements of positive valuation.

        INPUT:

        - ``x`` -- an element in the domain of this valuation

        OUTPUT: an element of the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field`

        EXAMPLES::

            sage: v = ZZ.valuation(3)
            sage: v.reduce(4)
            1
        """
    def lift(self, x):
        """
        Lift ``x`` from the residue field to the domain of this valuation.

        INPUT:

        - ``x`` -- an element of the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field`

        EXAMPLES::

            sage: v = ZZ.valuation(3)
            sage: xbar = v.reduce(4)
            sage: v.lift(xbar)
            1
        """
    def is_unramified(self, G, include_steps: bool = False, assume_squarefree: bool = False):
        """
        Return whether ``G`` defines a single unramified extension of the
        completion of the domain of this valuation.

        INPUT:

        - ``G`` -- a monic squarefree polynomial over the domain of this valuation

        - ``include_steps`` -- boolean (default: ``False``); whether to
          include the approximate valuations that were used to determine the
          result in the return value

        - ``assume_squarefree`` -- boolean (default: ``False``); whether to
          assume that ``G`` is square-free over the completion of the domain of
          this valuation. Setting this to ``True`` can significantly improve
          the performance.

        EXAMPLES:

        We consider an extension as unramified if its ramification index is 1.
        Hence, a trivial extension is unramified::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(2)
            sage: v.is_unramified(x)
            True

        If ``G`` remains irreducible in reduction, then it defines an
        unramified extension::

            sage: v.is_unramified(x^2 + x + 1)
            True

        However, even if ``G`` factors, it might define an unramified
        extension::

            sage: v.is_unramified(x^2 + 2*x + 4)                                        # needs sage.geometry.polyhedron
            True
        """
    def is_totally_ramified(self, G, include_steps: bool = False, assume_squarefree: bool = False):
        """
        Return whether ``G`` defines a single totally ramified extension of the
        completion of the domain of this valuation.

        INPUT:

        - ``G`` -- a monic squarefree polynomial over the domain of this valuation

        - ``include_steps`` -- boolean (default: ``False``); where to include
          the valuations produced during the process of checking whether ``G``
          is totally ramified in the return value

        - ``assume_squarefree`` -- boolean (default: ``False``); whether to
          assume that ``G`` is square-free over the completion of the domain of
          this valuation. Setting this to ``True`` can significantly improve
          the performance.

        ALGORITHM:

        This is a simplified version of :meth:`sage.rings.valuation.valuation.DiscreteValuation.mac_lane_approximants`.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: k = Qp(5,4)
            sage: v = k.valuation()
            sage: R.<x> = k[]
            sage: G = x^2 + 1
            sage: v.is_totally_ramified(G)                                              # needs sage.geometry.polyhedron
            False
            sage: G = x + 1
            sage: v.is_totally_ramified(G)
            True
            sage: G = x^2 + 2
            sage: v.is_totally_ramified(G)
            False
            sage: G = x^2 + 5
            sage: v.is_totally_ramified(G)                                              # needs sage.geometry.polyhedron
            True
            sage: v.is_totally_ramified(G, include_steps=True)                          # needs sage.geometry.polyhedron
            (True, [Gauss valuation induced by 5-adic valuation, [ Gauss valuation induced by 5-adic valuation, v((1 + O(5^4))*x) = 1/2 ]])

        We consider an extension as totally ramified if its ramification index
        matches the degree. Hence, a trivial extension is totally ramified::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(2)
            sage: v.is_totally_ramified(x)
            True

        TESTS:

        An example that Sebastian Pauli used at Sage Days 87::

            sage: R = ZpFM(3, 20)
            sage: S.<x> = R[]
            sage: f = x^9 + 9*x^2 + 3
            sage: R.valuation().is_totally_ramified(f)                                  # needs sage.geometry.polyhedron
            True
        """
    def change_domain(self, ring):
        """
        Change the domain of this valuation to ``ring`` if possible.

        EXAMPLES::

            sage: v = ZZ.valuation(2)
            sage: v.change_domain(QQ).domain()
            Rational Field
        """
    def extensions(self, ring):
        """
        Return the extensions of this valuation to ``ring``.

        EXAMPLES::

            sage: v = ZZ.valuation(2)
            sage: v.extensions(GaussianIntegers())                                      # needs sage.rings.number_field
            [2-adic valuation]

        TESTS::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: x = polygen(ZZ, 'x')
            sage: L.<a> = QQ.extension(x^3 - 2)
            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b^2 + 2*b + a)
            sage: M.valuation(2)
            2-adic valuation

        Check that we can extend to a field written as a quotient::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = QQ.extension(x^2 + 1)
            sage: R.<y> = K[]
            sage: L.<b> = R.quo(x^2 + a)
            sage: QQ.valuation(2).extensions(L)
            [2-adic valuation]

        A case where there was at some point an internal error in the
        approximants code::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: L.<a> = NumberField(x^4 + 2*x^3 + 2*x^2 + 8)
            sage: QQ.valuation(2).extensions(L)
            [[ 2-adic valuation, v(x + 2) = 3/2 ]-adic valuation,
             [ 2-adic valuation, v(x) = 1/2 ]-adic valuation]

        A case where the extension was incorrect at some point::

            sage: # needs sage.rings.number_field
            sage: v = QQ.valuation(2)
            sage: L.<a> = NumberField(x^2 + 2)
            sage: M.<b> = L.extension(x^2 + 1)
            sage: w = v.extension(L).extension(M)
            sage: w(w.uniformizer())
            1/4

        A case where the extensions could not be separated at some point::

            sage: # needs sage.rings.number_field
            sage: v = QQ.valuation(2)
            sage: R.<x> = QQ[]
            sage: F = x^48 + 120*x^45 + 56*x^42 + 108*x^36 + 32*x^33 + 40*x^30 + 48*x^27 + 80*x^24 + 112*x^21 + 96*x^18 + 96*x^15 + 24*x^12 + 96*x^9 + 16*x^6 + 96*x^3 + 68
            sage: L.<a> = QQ.extension(F)
            sage: v.extensions(L)
            [[ 2-adic valuation, v(x) = 1/24, v(x^24 + 4*x^18 + 10*x^12 + 12*x^6 + 8*x^3 + 6) = 29/8 ]-adic valuation,
             [ 2-adic valuation, v(x) = 1/24, v(x^24 + 4*x^18 + 2*x^12 + 12*x^6 + 8*x^3 + 6) = 29/8 ]-adic valuation]
        """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: v = GaussianIntegers().valuation(2)                                   # needs sage.rings.number_field
            sage: v.restriction(ZZ)                                                     # needs sage.rings.number_field
            2-adic valuation
        """
    @cached_method
    def value_semigroup(self):
        """
        Return the value semigroup of this valuation.

        EXAMPLES::

            sage: v = GaussianIntegers().valuation(2)                                   # needs sage.rings.number_field
            sage: v.value_semigroup()                                                   # needs sage.rings.number_field
            Additive Abelian Semigroup generated by 1/2
        """

class pAdicValuation_padic(pAdicValuation_base):
    """
    The `p`-adic valuation of a complete `p`-adic ring.

    INPUT:

    - ``R`` -- a `p`-adic ring

    EXAMPLES::

        sage: v = Qp(2).valuation(); v  # indirect doctest
        2-adic valuation

    TESTS::

        sage: TestSuite(v).run()                # long time                             # needs sage.geometry.polyhedron
    """
    def __init__(self, parent) -> None:
        """
        TESTS::

            sage: from sage.rings.padics.padic_valuation import pAdicValuation_padic
            sage: isinstance(Qp(2).valuation(), pAdicValuation_padic)
            True
        """
    def reduce(self, x):
        """
        Reduce ``x`` modulo the ideal of elements of positive valuation.

        INPUT:

        - ``x`` -- an element of the domain of this valuation

        OUTPUT: an element of the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field`

        EXAMPLES::

            sage: R = Zp(3)
            sage: Zp(3).valuation().reduce(R(4))
            1
        """
    def lift(self, x):
        """
        Lift ``x`` from the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field` to the domain of this
        valuation.

        INPUT:

        - ``x`` -- an element of the residue field of this valuation

        EXAMPLES::

            sage: R = Zp(3)
            sage: v = R.valuation()
            sage: xbar = v.reduce(R(4))
            sage: v.lift(xbar)
            1 + O(3^20)
        """
    def uniformizer(self):
        """
        Return a uniformizer of this valuation.

        EXAMPLES::

            sage: v = Zp(3).valuation()
            sage: v.uniformizer()
            3 + O(3^21)
        """
    def element_with_valuation(self, v):
        """
        Return an element of valuation ``v``.

        INPUT:

        - ``v`` -- an element of the :meth:`pAdicValuation_base.value_semigroup` of this valuation

        EXAMPLES::

            sage: R = Zp(3)
            sage: v = R.valuation()
            sage: v.element_with_valuation(3)
            3^3 + O(3^23)

            sage: # needs sage.libs.ntl
            sage: K = Qp(3)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + 3*y + 3)
            sage: L.valuation().element_with_valuation(3/2)
            y^3 + O(y^43)
        """
    def residue_ring(self):
        """
        Return the residue field of this valuation.

        EXAMPLES::

            sage: Qq(9, names='a').valuation().residue_ring()                           # needs sage.libs.ntl
            Finite Field in a0 of size 3^2
        """
    def shift(self, x, s):
        '''
        Shift ``x`` in its expansion with respect to :meth:`uniformizer` by
        ``s`` "digits".

        For nonnegative ``s``, this just returns ``x`` multiplied by a
        power of the uniformizer `\\pi`.

        For negative ``s``, it does the same but when not over a field, it
        drops coefficients in the `\\pi`-adic expansion which have negative
        valuation.

        EXAMPLES::

            sage: R = ZpCA(2)
            sage: v = R.valuation()
            sage: v.shift(R.one(), 1)
            2 + O(2^20)
            sage: v.shift(R.one(), -1)
            O(2^19)

            sage: # needs sage.libs.ntl sage.rings.padics
            sage: S.<y> = R[]
            sage: S.<y> = R.extension(y^3 - 2)
            sage: v = S.valuation()
            sage: v.shift(1, 5)
            y^5 + O(y^60)
        '''
    def simplify(self, x, error=None, force: bool = False):
        """
        Return a simplified version of ``x``.

        Produce an element which differs from ``x`` by an element of
        valuation strictly greater than the valuation of ``x`` (or strictly
        greater than ``error`` if set.)

        INPUT:

        - ``x`` -- an element in the domain of this valuation

        - ``error`` -- a rational, infinity, or ``None`` (default: ``None``),
          the error allowed to introduce through the simplification

        - ``force`` -- ignored

        EXAMPLES::

            sage: R = Zp(2)
            sage: v = R.valuation()
            sage: v.simplify(6)
            2 + O(2^21)
            sage: v.simplify(6, error=0)
            0
        """

class pAdicValuation_int(pAdicValuation_base):
    """
    A `p`-adic valuation on the integers or the rationals.

    EXAMPLES::

        sage: v = ZZ.valuation(3); v
        3-adic valuation

    TESTS::

        sage: TestSuite(v).run()                # long time                             # needs sage.geometry.polyhedron
    """
    def uniformizer(self):
        """
        Return a uniformizer of this `p`-adic valuation, i.e., `p` as an
        element of the domain.

        EXAMPLES::

            sage: v = ZZ.valuation(3)
            sage: v.uniformizer()
            3
        """
    def residue_ring(self):
        """
        Return the residue field of this valuation.

        EXAMPLES::

            sage: v = ZZ.valuation(3)
            sage: v.residue_ring()
            Finite Field of size 3
        """
    def simplify(self, x, error=None, force: bool = False, size_heuristic_bound: int = 32):
        """
        Return a simplified version of ``x``.

        Produce an element which differs from ``x`` by an element of
        valuation strictly greater than the valuation of ``x`` (or strictly
        greater than ``error`` if set.)

        INPUT:

        - ``x`` -- an element in the domain of this valuation

        - ``error`` -- a rational, infinity, or ``None`` (default: ``None``),
          the error allowed to introduce through the simplification

        - ``force`` -- ignored

        - ``size_heuristic_bound`` -- when ``force`` is not set, the expected
          factor by which the ``x`` need to shrink to perform an actual
          simplification (default: 32)

        EXAMPLES::

            sage: v = ZZ.valuation(2)
            sage: v.simplify(6, force=True)
            2
            sage: v.simplify(6, error=0, force=True)
            0

        In this example, the usual rational reconstruction misses a good answer
        for some moduli (because the absolute value of the numerator is not
        bounded by the square root of the modulus)::

            sage: v = QQ.valuation(2)
            sage: v.simplify(110406, error=16, force=True)
            562/19
            sage: Qp(2, 16)(110406).rational_reconstruction()
            Traceback (most recent call last):
            ...
            ArithmeticError: rational reconstruction of 55203 (mod 65536) does not exist
        """
    def inverse(self, x, precision):
        """
        Return an approximate inverse of ``x``.

        The element returned is such that the product differs from 1 by an
        element of valuation at least ``precision``.

        INPUT:

        - ``x`` -- an element in the domain of this valuation

        - ``precision`` -- a rational or infinity

        EXAMPLES::

            sage: v = ZZ.valuation(2)
            sage: x = 3
            sage: y = v.inverse(3, 2); y
            3
            sage: x*y - 1
            8

        This might not be possible for elements of positive valuation::

            sage: v.inverse(2, 2)
            Traceback (most recent call last):
            ...
            ValueError: element has no approximate inverse in this ring

        Unless the precision is very small::

            sage: v.inverse(2, 0)
            1
        """

class pAdicFromLimitValuation(FiniteExtensionFromLimitValuation, pAdicValuation_base):
    """
    A `p`-adic valuation on a number field or a subring thereof, i.e., a
    valuation that extends the `p`-adic valuation on the integers.

    EXAMPLES::

        sage: v = GaussianIntegers().valuation(3); v                                    # needs sage.rings.number_field
        3-adic valuation

    TESTS::

        sage: TestSuite(v).run(skip='_test_shift')      # long time                     # needs sage.rings.number_field

    The ``_test_shift`` test fails because the parent of the shift is
    incorrect, see :issue:`23971`::

        sage: v.shift(1, -1).parent()                                                   # needs sage.rings.number_field
        Number Field in I with defining polynomial x^2 + 1 with I = 1*I
    """
    def __init__(self, parent, approximant, G, approximants) -> None:
        """
        TESTS::

            sage: v = GaussianIntegers().valuation(3)                                   # needs sage.rings.number_field
            sage: from sage.rings.padics.padic_valuation import pAdicFromLimitValuation
            sage: isinstance(v, pAdicFromLimitValuation)                                # needs sage.rings.number_field
            True
        """
    def extensions(self, ring):
        """
        Return the extensions of this valuation to ``ring``.

        EXAMPLES::

            sage: v = GaussianIntegers().valuation(3)                                   # needs sage.rings.number_field
            sage: v.extensions(v.domain().fraction_field())                             # needs sage.rings.number_field
            [3-adic valuation]
        """
