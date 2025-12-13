from sage.categories.action import Action as Action
from sage.categories.homset import Homset as Homset
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DiscretePseudoValuationSpace(UniqueRepresentation, Homset):
    """
    The space of discrete pseudo-valuations on ``domain``.

    EXAMPLES::

        sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
        sage: H = DiscretePseudoValuationSpace(QQ)
        sage: QQ.valuation(2) in H
        True

    .. NOTE::

        We do not distinguish between the space of discrete valuations and the
        space of discrete pseudo-valuations. This is entirely for practical
        reasons: We would like to model the fact that every discrete valuation
        is also a discrete pseudo-valuation. At first, it seems to be
        sufficient to make sure that the ``in`` operator works which can
        essentially be achieved by overriding ``_element_constructor_`` of
        the space of discrete pseudo-valuations to accept discrete valuations
        by just returning them. Currently, however, if one does not change the
        parent of an element in ``_element_constructor_`` to ``self``, then
        one cannot register that conversion as a coercion. Consequently, the
        operators ``<=`` and ``>=`` cannot be made to work between discrete
        valuations and discrete pseudo-valuations on the same domain (because
        the implementation only calls ``_richcmp`` if both operands have the
        same parent.) Of course, we could override ``__ge__`` and  ``__le__``
        but then we would likely run into other surprises.
        So in the end, we went for a single homspace for all discrete
        valuations (pseudo or not) as this makes the implementation much
        easier.

    .. TODO::

        The comparison problem might be fixed by :issue:`22029` or similar.

    TESTS::

        sage: TestSuite(H).run() # long time
    """
    def __init__(self, domain) -> None:
        """
        TESTS::

            sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
            sage: isinstance(QQ.valuation(2).parent(), DiscretePseudoValuationSpace)
            True
        """
    def __contains__(self, x) -> bool:
        """
        Return whether ``x`` is a valuation in this space.

        EXAMPLES::

            sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
            sage: H = DiscretePseudoValuationSpace(QQ)
            sage: H.an_element() in H
            True
            sage: QQ.valuation(2) in H
            True
        """
    def __call__(self, x):
        """
        Create an element in this space from ``x``.

        EXAMPLES::

            sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
            sage: H = DiscretePseudoValuationSpace(QQ)
            sage: H(QQ.valuation(2))
            2-adic valuation
        """
    class ElementMethods:
        """
        Provides methods for discrete pseudo-valuations that are added
        automatically to valuations in this space.

        EXAMPLES:

        Here is an example of a method that is automagically added to a
        discrete valuation::

            sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
            sage: H = DiscretePseudoValuationSpace(QQ)
            sage: QQ.valuation(2).is_discrete_pseudo_valuation() # indirect doctest
            True

        The methods will be provided even if the concrete type is not created
        with ``__make_element_class__``::

            sage: from sage.rings.valuation.valuation import DiscretePseudoValuation
            sage: m = DiscretePseudoValuation(H)
            sage: m.parent() is H
            True
            sage: m.is_discrete_pseudo_valuation()
            True

        However, the category framework advises you to use inheritance::

            sage: m._test_category()
            Traceback (most recent call last):
            ...
            AssertionError: False is not true

        Using ``__make_element_class__``, makes your concrete valuation inherit
        from this class::

            sage: m = H.__make_element_class__(DiscretePseudoValuation)(H)
            sage: m._test_category()
        """
        def is_discrete_pseudo_valuation(self):
            """
            Return whether this valuation is a discrete pseudo-valuation.

            EXAMPLES::

                sage: QQ.valuation(2).is_discrete_pseudo_valuation()
                True
            """
        @abstract_method
        def is_discrete_valuation(self) -> None:
            """
            Return whether this valuation is a discrete valuation, i.e.,
            whether it is a :meth:`discrete pseudo valuation
            <is_discrete_pseudo_valuation>` that only sends zero to `\\infty`.

            EXAMPLES::

                sage: QQ.valuation(2).is_discrete_valuation()
                True
            """
        def is_negative_pseudo_valuation(self):
            """
            Return whether this valuation is a discrete pseudo-valuation that
            does attain `-\\infty`, i.e., it is non-trivial and its domain
            contains an element with valuation `\\infty` that has an inverse.

            EXAMPLES::

                sage: QQ.valuation(2).is_negative_pseudo_valuation()
                False
            """
        @cached_method
        def is_trivial(self):
            """
            Return whether this valuation is trivial, i.e., whether it is
            constant `\\infty` or constant zero for everything but the zero
            element.

            Subclasses need to override this method if they do not implement
            :meth:`uniformizer`.

            EXAMPLES::

                sage: QQ.valuation(7).is_trivial()
                False
            """
        @abstract_method
        def uniformizer(self) -> None:
            """
            Return an element in the domain which has positive valuation and
            generates the value group of this valuation.

            EXAMPLES::

                sage: QQ.valuation(11).uniformizer()
                11

            Trivial valuations have no uniformizer::

                sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
                sage: v = DiscretePseudoValuationSpace(QQ).an_element()
                sage: v.is_trivial()
                True
                sage: v.uniformizer()
                Traceback (most recent call last):
                ...
                ValueError: Trivial valuations do not define a uniformizing element
            """
        @cached_method
        def value_group(self):
            """
            Return the value group of this discrete pseudo-valuation, the
            discrete additive subgroup of the rational numbers which is
            generated by the valuation of the :meth:`uniformizer`.

            EXAMPLES::

                sage: QQ.valuation(2).value_group()
                Additive Abelian Group generated by 1

            A pseudo-valuation that is `\\infty` everywhere, does not have a
            value group::

                sage: from sage.rings.valuation.valuation_space import DiscretePseudoValuationSpace
                sage: v = DiscretePseudoValuationSpace(QQ).an_element()
                sage: v.value_group()
                Traceback (most recent call last):
                ...
                ValueError: The trivial pseudo-valuation that is infinity everywhere does not have a value group.
            """
        def value_semigroup(self):
            """
            Return the value semigroup of this discrete pseudo-valuation, the
            additive subsemigroup of the rational numbers which is generated by
            the valuations of the elements in the domain.

            EXAMPLES:

            Most commonly, in particular over fields, the semigroup is the
            group generated by the valuation of the uniformizer::

                sage: G = QQ.valuation(2).value_semigroup(); G
                Additive Abelian Semigroup generated by -1, 1
                sage: G in AdditiveMagmas().AdditiveAssociative().AdditiveUnital().AdditiveInverse()
                True

            If the domain is a discrete valuation ring, then the semigroup
            consists of the positive elements of the :meth:`value_group`::

                sage: Zp(2).valuation().value_semigroup()
                Additive Abelian Semigroup generated by 1

            The semigroup can have a more complicated structure when the
            uniformizer is not in the domain::

                sage: v = ZZ.valuation(2)
                sage: R.<x> = ZZ[]
                sage: w = GaussValuation(R, v)
                sage: u = w.augmentation(x, 5/3)
                sage: u.value_semigroup()
                Additive Abelian Semigroup generated by 1, 5/3
            """
        def element_with_valuation(self, s):
            """
            Return an element in the domain of this valuation with valuation
            ``s``.

            EXAMPLES::

                sage: v = ZZ.valuation(2)
                sage: v.element_with_valuation(10)
                1024
            """
        @abstract_method
        def residue_ring(self) -> None:
            """
            Return the residue ring of this valuation, i.e., the elements of
            nonnegative valuation modulo the elements of positive valuation.
            EXAMPLES::

                sage: QQ.valuation(2).residue_ring()
                Finite Field of size 2
                sage: valuations.TrivialValuation(QQ).residue_ring()
                Rational Field

            Note that a residue ring always exists, even when a residue field
            may not::

                sage: valuations.TrivialPseudoValuation(QQ).residue_ring()
                Quotient of Rational Field by the ideal (1)
                sage: valuations.TrivialValuation(ZZ).residue_ring()
                Integer Ring
                sage: GaussValuation(ZZ['x'], ZZ.valuation(2)).residue_ring()
                Univariate Polynomial Ring in x over Finite Field of size 2...
            """
        def residue_field(self):
            """
            Return the residue field of this valuation, i.e., the field of
            fractions of the :meth:`residue_ring`, the elements of nonnegative
            valuation modulo the elements of positive valuation.

            EXAMPLES::

                sage: QQ.valuation(2).residue_field()
                Finite Field of size 2
                sage: valuations.TrivialValuation(QQ).residue_field()
                Rational Field

                sage: valuations.TrivialValuation(ZZ).residue_field()
                Rational Field
                sage: GaussValuation(ZZ['x'], ZZ.valuation(2)).residue_field()
                Rational function field in x over Finite Field of size 2
            """
        @abstract_method
        def reduce(self, x) -> None:
            """
            Return the image of ``x`` in the :meth:`residue_ring` of this
            valuation.

            EXAMPLES::

                sage: v = QQ.valuation(2)
                sage: v.reduce(2)
                0
                sage: v.reduce(1)
                1
                sage: v.reduce(1/3)
                1
                sage: v.reduce(1/2)
                Traceback (most recent call last):
                ...
                ValueError: reduction is only defined for elements of nonnegative valuation
            """
        @abstract_method
        def lift(self, X) -> None:
            """
            Return a lift of ``X`` in the domain which reduces down to ``X``
            again via :meth:`reduce`.

            EXAMPLES::

                sage: v = QQ.valuation(2)
                sage: v.lift(v.residue_ring().one())
                1
            """
        def extension(self, ring):
            """
            Return the unique extension of this valuation to ``ring``.

            EXAMPLES::

                sage: v = ZZ.valuation(2)
                sage: w = v.extension(QQ)
                sage: w.domain()
                Rational Field
            """
        def extensions(self, ring):
            """
            Return the extensions of this valuation to ``ring``.

            EXAMPLES::

                sage: v = ZZ.valuation(2)
                sage: v.extensions(QQ)
                [2-adic valuation]
            """
        def restriction(self, ring):
            """
            Return the restriction of this valuation to ``ring``.

            EXAMPLES::

                sage: v = QQ.valuation(2)
                sage: w = v.restriction(ZZ)
                sage: w.domain()
                Integer Ring
            """
        def change_domain(self, ring):
            """
            Return this valuation over ``ring``.

            Unlike :meth:`extension` or :meth:`restriction`, this might not be
            completely sane mathematically. It is essentially a conversion of
            this valuation into another space of valuations.

            EXAMPLES::

                sage: v = QQ.valuation(3)
                sage: v.change_domain(ZZ)
                3-adic valuation
            """
        def scale(self, scalar):
            """
            Return this valuation scaled by ``scalar``.

            INPUT:

            - ``scalar`` -- a nonnegative rational number or infinity

            EXAMPLES::

                sage: v = ZZ.valuation(3)
                sage: w = v.scale(3)
                sage: w(3)
                3

            Scaling can also be done through multiplication with a scalar::

                sage: w/3 == v
                True

            Multiplication by zero produces the trivial discrete valuation::

                sage: w = 0*v
                sage: w(3)
                0
                sage: w(0)
                +Infinity

            Multiplication by infinity produces the trivial discrete
            pseudo-valuation::

                sage: w = infinity*v
                sage: w(3)
                +Infinity
                sage: w(0)
                +Infinity
            """
        def separating_element(self, others):
            """
            Return an element in the domain of this valuation which has
            positive valuation with respect to this valuation but negative
            valuation with respect to the valuations in ``others``.

            EXAMPLES::

                sage: v2 = QQ.valuation(2)
                sage: v3 = QQ.valuation(3)
                sage: v5 = QQ.valuation(5)
                sage: v2.separating_element([v3,v5])
                4/15
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

                sage: v = ZZ.valuation(2)
                sage: v.shift(1, 10)
                1024
                sage: v.shift(11, -1)
                5

            For some rings, there is no clear `\\pi`-adic expansion. In this
            case, this method performs negative shifts by iterated division by
            the uniformizer and substraction of a lift of the reduction::

                sage: R.<x> = ZZ[]
                sage: v = ZZ.valuation(2)
                sage: w = GaussValuation(R, v)
                sage: w.shift(x, 1)
                2*x
                sage: w.shift(2*x, -1)
                x
                sage: w.shift(x + 2*x^2, -1)
                x^2
            '''
        def simplify(self, x, error=None, force: bool = False):
            """
            Return a simplified version of ``x``.

            Produce an element which differs from ``x`` by an element of
            valuation strictly greater than the valuation of ``x`` (or strictly
            greater than ``error`` if set.)

            If ``force`` is not set, then expensive simplifications may be avoided.

            EXAMPLES::

                sage: v = ZZ.valuation(2)
                sage: v.simplify(6, force=True)
                2
                sage: v.simplify(6, error=0, force=True)
                0
            """
        def lower_bound(self, x):
            """
            Return a lower bound of this valuation at ``x``.

            Use this method to get an approximation of the valuation of ``x``
            when speed is more important than accuracy.

            EXAMPLES::

                sage: v = ZZ.valuation(2)
                sage: v.lower_bound(2^10)
                10
            """
        def upper_bound(self, x):
            """
            Return an upper bound of this valuation at ``x``.

            Use this method to get an approximation of the valuation of ``x``
            when speed is more important than accuracy.

            EXAMPLES::

                sage: v = ZZ.valuation(2)
                sage: v.upper_bound(2^10)
                10
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

            Of course this always works over fields::

                sage: v = QQ.valuation(2)
                sage: v.inverse(2, 2)
                1/2
            """

class ScaleAction(Action):
    """
    Action of integers, rationals and the infinity ring on valuations by
    scaling it.

    EXAMPLES::

        sage: v = QQ.valuation(5)
        sage: from operator import mul
        sage: v.parent().get_action(ZZ, mul, self_on_left=False)
        Left action by Integer Ring on Discrete pseudo-valuations on Rational Field
    """
