r"""
Valuations which are defined as limits of valuations.

The discrete valuation of a complete field extends uniquely to a finite field
extension. This is not the case anymore for fields which are not complete with
respect to their discrete valuation. In this case, the extensions essentially
correspond to the factors of the defining polynomial of the extension over the
completion. However, these factors only exist over the completion and this
makes it difficult to write down such valuations with a representation of
finite length.

More specifically, let `v` be a discrete valuation on `K` and let `L=K[x]/(G)`
a finite extension thereof. An extension of `v` to `L` can be represented as a
discrete pseudo-valuation `w'` on `K[x]` which sends `G` to infinity.
However, such `w'` might not be described by an :mod:`augmented valuation <sage.rings.valuation.augmented_valuation>`
over a :mod:`Gauss valuation <sage.rings.valuation.gauss_valuation>` anymore. Instead, we may need to write is as a
limit of augmented valuations.

The classes in this module provide the means of writing down such limits and
resulting valuations on quotients.

AUTHORS:

- Julian Rüth (2016-10-19): initial version

EXAMPLES:

In this function field, the unique place of ``K`` which corresponds to the zero
point has two extensions to ``L``. The valuations corresponding to these
extensions can only be approximated::

    sage: # needs sage.rings.function_field
    sage: K.<x> = FunctionField(QQ)
    sage: R.<y> = K[]
    sage: L.<y> = K.extension(y^2 - x)
    sage: v = K.valuation(1)
    sage: w = v.extensions(L); w
    [[ (x - 1)-adic valuation, v(y + 1) = 1 ]-adic valuation,
     [ (x - 1)-adic valuation, v(y - 1) = 1 ]-adic valuation]

The same phenomenon can be observed for valuations on number fields::

    sage: # needs sage.rings.number_field
    sage: K = QQ
    sage: R.<t> = K[]
    sage: L.<t> = K.extension(t^2 + 1)
    sage: v = QQ.valuation(5)
    sage: w = v.extensions(L); w
    [[ 5-adic valuation, v(t + 2) = 1 ]-adic valuation,
     [ 5-adic valuation, v(t + 3) = 1 ]-adic valuation]

.. NOTE::

    We often rely on approximations of valuations even if we could represent the
    valuation without using a limit. This is done to improve performance as many
    computations already can be done correctly with an approximation::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x)
        sage: v = K.valuation(1/x)
        sage: w = v.extension(L); w
        Valuation at the infinite place
        sage: w._base_valuation._base_valuation._improve_approximation()
        sage: w._base_valuation._base_valuation._approximation
        [ Gauss valuation induced by Valuation at the infinite place,
            v(y) = 1/2, v(y^2 - 1/x) = +Infinity ]

REFERENCES:

Limits of inductive valuations are discussed in [Mac1936I]_ and [Mac1936II]_. An
overview can also be found in Section 4.6 of [Rüt2014]_.
"""
from .valuation import DiscretePseudoValuation as DiscretePseudoValuation, InfiniteDiscretePseudoValuation as InfiniteDiscretePseudoValuation
from _typeshed import Incomplete
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.structure.factory import UniqueFactory as UniqueFactory

class LimitValuationFactory(UniqueFactory):
    """
    Return a limit valuation which sends the polynomial ``G`` to infinity and
    is greater than or equal than ``base_valuation``.

    INPUT:

    - ``base_valuation`` -- a discrete (pseudo-)valuation on a polynomial ring
      which is a discrete valuation on the coefficient ring which can be
      uniquely augmented (possibly only in the limit) to a pseudo-valuation
      that sends ``G`` to infinity.

    - ``G`` -- a squarefree polynomial in the domain of ``base_valuation``

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(2))
        sage: w = valuations.LimitValuation(v, x)
        sage: w(x)
        +Infinity
    """
    def create_key(self, base_valuation, G):
        """
        Create a key from the parameters of this valuation.

        EXAMPLES:

        Note that this does not normalize ``base_valuation`` in any way. It is
        easily possible to create the same limit in two different ways::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = valuations.LimitValuation(v, x)  # indirect doctest
            sage: v = v.augmentation(x, infinity)
            sage: u = valuations.LimitValuation(v, x)
            sage: u == w
            False

        The point here is that this is not meant to be invoked from user code.
        But mostly from other factories which have made sure that the
        parameters are normalized already.
        """
    def create_object(self, version, key):
        """
        Create an object from ``key``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: w = valuations.LimitValuation(v, x^2 + 1)  # indirect doctest
        """

LimitValuation: LimitValuationFactory

class LimitValuation_generic(DiscretePseudoValuation):
    """
    Base class for limit valuations.

    A limit valuation is realized as an approximation of a valuation and means
    to improve that approximation when necessary.

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x)
        sage: v = K.valuation(0)
        sage: w = v.extension(L)
        sage: w._base_valuation
        [ Gauss valuation induced by (x)-adic valuation, v(y) = 1/2 , … ]

    The currently used approximation can be found in the ``_approximation``
    field::

        sage: w._base_valuation._approximation                                          # needs sage.rings.function_field
        [ Gauss valuation induced by (x)-adic valuation, v(y) = 1/2 ]

    TESTS::

        sage: from sage.rings.valuation.limit_valuation import LimitValuation_generic
        sage: isinstance(w._base_valuation, LimitValuation_generic)                     # needs sage.rings.function_field
        True
        sage: TestSuite(w._base_valuation).run()        # long time                     # needs sage.rings.function_field
    """
    def __init__(self, parent, approximation) -> None:
        """
        TESTS::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<i> = QQ.extension(x^2 + 1)
            sage: v = K.valuation(2)
            sage: from sage.rings.valuation.limit_valuation import LimitValuation_generic
            sage: isinstance(v._base_valuation, LimitValuation_generic)
            True
        """
    def reduce(self, f, check: bool = True):
        """
        Return the reduction of ``f`` as an element of the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_ring`.

        INPUT:

        - ``f`` -- an element in the domain of this valuation of nonnegative
          valuation

        - ``check`` -- whether or not to check that ``f`` has nonnegative
          valuation (default: ``True``)

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - (x - 1))
            sage: v = K.valuation(0)
            sage: w = v.extension(L)
            sage: w.reduce(y)  # indirect doctest
            u1
        """

class MacLaneLimitValuation(LimitValuation_generic, InfiniteDiscretePseudoValuation):
    """
    A limit valuation that is a pseudo-valuation on polynomial ring `K[x]`
    which sends a square-free polynomial `G` to infinity.

    This uses the MacLane algorithm to compute the next element in the limit.

    It starts from a first valuation ``approximation`` which has a unique
    augmentation that sends `G` to infinity and whose uniformizer must be a
    uniformizer of the limit and whose residue field must contain the residue
    field of the limit.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<i> = QQ.extension(x^2 + 1)
        sage: v = K.valuation(2)
        sage: u = v._base_valuation; u
        [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 , … ]
    """
    def __init__(self, parent, approximation, G) -> None:
        """
        TESTS::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<i> = QQ.extension(x^2 + 1)
            sage: v = K.valuation(2)
            sage: u = v._base_valuation
            sage: from sage.rings.valuation.limit_valuation import MacLaneLimitValuation
            sage: isinstance(u, MacLaneLimitValuation)
            True
        """
    def extensions(self, ring):
        """
        Return the extensions of this valuation to ``ring``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: v = GaussianIntegers().valuation(2)
            sage: u = v._base_valuation
            sage: u.extensions(QQ['x'])
            [[ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 , … ]]
        """
    def lift(self, F):
        """
        Return a lift of ``F`` from the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_ring` to the domain of
        this valuation.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^4 - x^2 - 2*x - 1)
            sage: v = K.valuation(1)
            sage: w = v.extensions(L)[1]; w
            [ (x - 1)-adic valuation, v(y^2 - 2) = 1 ]-adic valuation
            sage: s = w.reduce(y); s
            u1
            sage: w.lift(s)  # indirect doctest
            y
        """
    def uniformizer(self):
        """
        Return a uniformizing element for this valuation.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: v = K.valuation(0)
            sage: w = v.extension(L)
            sage: w.uniformizer()  # indirect doctest
            y
        """
    def residue_ring(self):
        """
        Return the residue ring of this valuation, which is always a field.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: w = v.extension(L)
            sage: w.residue_ring()
            Finite Field of size 2
        """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: w = v.extension(L)
            sage: w._base_valuation.restriction(K)
            2-adic valuation
        """
    def value_semigroup(self):
        """
        Return the value semigroup of this valuation.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(5)
            sage: u,uu = v.extensions(L)
            sage: u.value_semigroup()
            Additive Abelian Semigroup generated by -1, 1
        """
    def element_with_valuation(self, s):
        """
        Return an element with valuation ``s``.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: u = v.extension(L)
            sage: u.element_with_valuation(1/2)
            t + 1
        """
    def simplify(self, f, error=None, force: bool = False):
        """
        Return a simplified version of ``f``.

        Produce an element which differs from ``f`` by an element of valuation
        strictly greater than the valuation of ``f`` (or strictly greater than
        ``error`` if set.)

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: u = v.extension(L)
            sage: u.simplify(t + 1024, force=True)
            t
        """
    def lower_bound(self, f):
        """
        Return a lower bound of this valuation at ``x``.

        Use this method to get an approximation of the valuation of ``x``
        when speed is more important than accuracy.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: u = v.extension(L)
            sage: u.lower_bound(1024*t + 1024)
            10
            sage: u(1024*t + 1024)
            21/2
        """
    def upper_bound(self, f):
        """
        Return an upper bound of this valuation at ``x``.

        Use this method to get an approximation of the valuation of ``x``
        when speed is more important than accuracy.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: u = v.extension(L)
            sage: u.upper_bound(1024*t + 1024)
            21/2
            sage: u(1024*t + 1024)
            21/2
        """
    def is_negative_pseudo_valuation(self):
        """
        Return whether this valuation attains `-\\infty`.

        EXAMPLES:

        For a Mac Lane limit valuation, this is never the case, so this
        method always returns ``False``::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = QQ.valuation(2)
            sage: u = v.extension(L)
            sage: u.is_negative_pseudo_valuation()
            False
        """
