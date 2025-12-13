from .valuation import DiscretePseudoValuation as DiscretePseudoValuation, DiscreteValuation as DiscreteValuation, InfiniteDiscretePseudoValuation as InfiniteDiscretePseudoValuation
from .valuation_space import DiscretePseudoValuationSpace as DiscretePseudoValuationSpace
from _typeshed import Incomplete
from sage.structure.factory import UniqueFactory as UniqueFactory

class TrivialValuationFactory(UniqueFactory):
    """
    Create a trivial valuation on ``domain``.

    EXAMPLES::

        sage: v = valuations.TrivialValuation(QQ); v
        Trivial valuation on Rational Field
        sage: v(1)
        0
    """
    def __init__(self, clazz, parent, *args, **kwargs) -> None:
        """
        TESTS::

            sage: from sage.rings.valuation.trivial_valuation import TrivialValuationFactory
            sage: isinstance(valuations.TrivialValuation, TrivialValuationFactory)
            True
        """
    def create_key(self, domain):
        """
        Create a key that identifies this valuation.

        EXAMPLES::

            sage: valuations.TrivialValuation(QQ) is valuations.TrivialValuation(QQ) # indirect doctest
            True
        """
    def create_object(self, version, key, **extra_args):
        """
        Create a trivial valuation from ``key``.

        EXAMPLES::

            sage: valuations.TrivialValuation(QQ) # indirect doctest
            Trivial valuation on Rational Field
        """

class TrivialDiscretePseudoValuation_base(DiscretePseudoValuation):
    """
    Base class for code shared by trivial valuations.

    EXAMPLES::

        sage: v = valuations.TrivialPseudoValuation(ZZ); v
        Trivial pseudo-valuation on Integer Ring

    TESTS::

        sage: TestSuite(v).run() # long time
    """
    def uniformizer(self) -> None:
        """
        Return a uniformizing element for this valuation.

        EXAMPLES::

            sage: v = valuations.TrivialPseudoValuation(ZZ)
            sage: v.uniformizer()
            Traceback (most recent call last):
            ...
            ValueError: Trivial valuations do not define a uniformizing element
        """
    def is_trivial(self):
        """
        Return whether this valuation is trivial.

        EXAMPLES::

            sage: v = valuations.TrivialPseudoValuation(QQ)
            sage: v.is_trivial()
            True
        """
    def is_negative_pseudo_valuation(self):
        """
        Return whether this valuation attains the value `-\\infty`.

        EXAMPLES::

            sage: v = valuations.TrivialPseudoValuation(QQ)
            sage: v.is_negative_pseudo_valuation()
            False
        """

class TrivialDiscretePseudoValuation(TrivialDiscretePseudoValuation_base, InfiniteDiscretePseudoValuation):
    """
    The trivial pseudo-valuation that is `\\infty` everywhere.

    EXAMPLES::

        sage: v = valuations.TrivialPseudoValuation(QQ); v
        Trivial pseudo-valuation on Rational Field

    TESTS::

        sage: TestSuite(v).run() # long time
    """
    def __init__(self, parent) -> None:
        """
        TESTS::

            sage: from sage.rings.valuation.trivial_valuation import TrivialDiscretePseudoValuation
            sage: v = valuations.TrivialPseudoValuation(QQ)
            sage: isinstance(v, TrivialDiscretePseudoValuation)
            True
        """
    def value_group(self) -> None:
        """
        Return the value group of this valuation.

        EXAMPLES:

        A trivial discrete pseudo-valuation has no value group::

            sage: v = valuations.TrivialPseudoValuation(QQ)
            sage: v.value_group()
            Traceback (most recent call last):
            ...
            ValueError: The trivial pseudo-valuation that is infinity everywhere does not have a value group.
        """
    def residue_ring(self):
        """
        Return the residue ring of this valuation.

        EXAMPLES::

            sage: valuations.TrivialPseudoValuation(QQ).residue_ring()
            Quotient of Rational Field by the ideal (1)
        """
    def reduce(self, x):
        """
        Reduce ``x`` modulo the positive elements of this valuation.

        EXAMPLES::

            sage: v = valuations.TrivialPseudoValuation(QQ)
            sage: v.reduce(1)
            0
        """
    def lift(self, X):
        """
        Return a lift of ``X`` to the domain of this valuation.

        EXAMPLES::

            sage: v = valuations.TrivialPseudoValuation(QQ)
            sage: v.lift(v.residue_ring().zero())
            0
        """

class TrivialDiscreteValuation(TrivialDiscretePseudoValuation_base, DiscreteValuation):
    """
    The trivial valuation that is zero on nonzero elements.

    EXAMPLES::

        sage: v = valuations.TrivialValuation(QQ); v
        Trivial valuation on Rational Field

    TESTS::

        sage: TestSuite(v).run() # long time
    """
    def __init__(self, parent) -> None:
        """
        TESTS::

            sage: from sage.rings.valuation.trivial_valuation import TrivialDiscreteValuation
            sage: v = valuations.TrivialValuation(QQ)
            sage: isinstance(v, TrivialDiscreteValuation)
            True
        """
    def value_group(self):
        """
        Return the value group of this valuation.

        EXAMPLES:

        A trivial discrete valuation has a trivial value group::

            sage: v = valuations.TrivialValuation(QQ)
            sage: v.value_group()
            Trivial Additive Abelian Group
        """
    def residue_ring(self):
        """
        Return the residue ring of this valuation.

        EXAMPLES::

            sage: valuations.TrivialValuation(QQ).residue_ring()
            Rational Field
        """
    def reduce(self, x):
        """
        Reduce ``x`` modulo the positive elements of this valuation.

        EXAMPLES::

            sage: v = valuations.TrivialValuation(QQ)
            sage: v.reduce(1)
            1
        """
    def lift(self, X):
        """
        Return a lift of ``X`` to the domain of this valuation.

        EXAMPLES::

            sage: v = valuations.TrivialValuation(QQ)
            sage: v.lift(v.residue_ring().zero())
            0
        """
    def extensions(self, ring):
        """
        Return the unique extension of this valuation to ``ring``.

        EXAMPLES::

            sage: v = valuations.TrivialValuation(ZZ)
            sage: v.extensions(QQ)
            [Trivial valuation on Rational Field]
        """

TrivialValuation: Incomplete
TrivialPseudoValuation: Incomplete
