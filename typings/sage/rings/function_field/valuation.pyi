from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.rational_field import QQ as QQ
from sage.rings.valuation.mapped_valuation import FiniteExtensionFromLimitValuation as FiniteExtensionFromLimitValuation, MappedValuation_base as MappedValuation_base
from sage.rings.valuation.trivial_valuation import TrivialValuation as TrivialValuation
from sage.rings.valuation.valuation import DiscretePseudoValuation as DiscretePseudoValuation, DiscreteValuation as DiscreteValuation, InfiniteDiscretePseudoValuation as InfiniteDiscretePseudoValuation, NegativeInfiniteDiscretePseudoValuation as NegativeInfiniteDiscretePseudoValuation
from sage.structure.factory import UniqueFactory as UniqueFactory

class FunctionFieldValuationFactory(UniqueFactory):
    """
    Create a valuation on ``domain`` corresponding to ``prime``.

    INPUT:

    - ``domain`` -- a function field

    - ``prime`` -- a place of the function field, a valuation on a subring, or
      a valuation on another function field together with information for
      isomorphisms to and from that function field

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: v = K.valuation(1); v  # indirect doctest
        (x - 1)-adic valuation
        sage: v(x)
        0
        sage: v(x - 1)
        1

    See :meth:`sage.rings.function_field.function_field.FunctionField.valuation` for further examples.
    """
    def create_key_and_extra_args(self, domain, prime):
        """
        Create a unique key which identifies the valuation given by ``prime``
        on ``domain``.

        TESTS:

        We specify a valuation on a function field by two different means and
        get the same object::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x - 1)  # indirect doctest

            sage: R.<x> = QQ[]
            sage: w = GaussValuation(R, valuations.TrivialValuation(QQ)).augmentation(x - 1, 1)
            sage: K.valuation(w) is v
            True

        The normalization is, however, not smart enough, to unwrap
        substitutions that turn out to be trivial::

            sage: w = GaussValuation(R, QQ.valuation(2))
            sage: w = K.valuation(w)
            sage: w is K.valuation((w, K.hom([~K.gen()]), K.hom([~K.gen()])))
            False
        """
    def create_key_and_extra_args_from_place(self, domain, generator):
        """
        Create a unique key which identifies the valuation at the place
        specified by ``generator``.

        TESTS:

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(1/x)  # indirect doctest
        """
    def create_key_and_extra_args_from_valuation(self, domain, valuation):
        """
        Create a unique key which identifies the valuation which extends
        ``valuation``.

        TESTS:

            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = QQ[]
            sage: w = GaussValuation(R, valuations.TrivialValuation(QQ)).augmentation(x - 1, 1)
            sage: v = K.valuation(w) # indirect doctest

        Check that :issue:`25294` has been resolved::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + 1/x^3*y + 2/x^4)                            # needs sage.rings.function_field
            sage: v = K.valuation(x)                                                    # needs sage.rings.function_field
            sage: v.extensions(L)                                                       # needs sage.rings.function_field
            [[ (x)-adic valuation, v(y) = 1 ]-adic valuation
               (in Function field in y defined by y^3 + x*y + 2*x^2 after y |--> 1/x^2*y),
             [ (x)-adic valuation, v(y) = 1/2 ]-adic valuation
               (in Function field in y defined by y^3 + x*y + 2*x^2 after y |--> 1/x^2*y)]
        """
    def create_key_and_extra_args_from_valuation_on_isomorphic_field(self, domain, valuation, to_valuation_domain, from_valuation_domain):
        """
        Create a unique key which identifies the valuation which is
        ``valuation`` after mapping through ``to_valuation_domain``.

        TESTS::

            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + y + x^3)                                    # needs sage.rings.function_field
            sage: v = K.valuation(1/x)                                                  # needs sage.rings.function_field
            sage: w = v.extension(L)  # indirect doctest                                # needs sage.rings.function_field
        """
    def create_object(self, version, key, **extra_args):
        """
        Create the valuation specified by ``key``.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = QQ[]
            sage: w = valuations.GaussValuation(R, QQ.valuation(2))
            sage: v = K.valuation(w); v  # indirect doctest
            2-adic valuation
        """

FunctionFieldValuation: Incomplete

class FunctionFieldValuation_base(DiscretePseudoValuation):
    """
    Abstract base class for any discrete (pseudo-)valuation on a function
    field.

    TESTS::

        sage: K.<x> = FunctionField(QQ)
        sage: v = K.valuation(x)  # indirect doctest
        sage: from sage.rings.function_field.valuation import FunctionFieldValuation_base
        sage: isinstance(v, FunctionFieldValuation_base)
        True
    """

class DiscreteFunctionFieldValuation_base(DiscreteValuation):
    """
    Base class for discrete valuations on function fields.

    TESTS::

        sage: K.<x> = FunctionField(QQ)
        sage: v = K.valuation(x)  # indirect doctest
        sage: from sage.rings.function_field.valuation import DiscreteFunctionFieldValuation_base
        sage: isinstance(v, DiscreteFunctionFieldValuation_base)
        True
    """
    def extensions(self, L):
        """
        Return the extensions of this valuation to ``L``.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)                                          # needs sage.rings.function_field
            sage: v.extensions(L)                                                       # needs sage.rings.function_field
            [(x)-adic valuation]

        TESTS:

        Valuations over the infinite place::

            sage: v = K.valuation(1/x)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - 1/(x^2 + 1))                                # needs sage.rings.function_field
            sage: sorted(v.extensions(L), key=str)                                      # needs sage.rings.function_field
            [[ Valuation at the infinite place, v(y + 1/x) = 3 ]-adic valuation,
             [ Valuation at the infinite place, v(y - 1/x) = 3 ]-adic valuation]

        Iterated extensions over the infinite place::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + y + x^3)
            sage: v = K.valuation(1/x)
            sage: w = v.extension(L)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: w.extension(M)                # not implemented
            Traceback (most recent call last):
            ...
            NotImplementedError

        A case that caused some trouble at some point::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(v)

            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - x^4 - 1)                                    # needs sage.rings.function_field
            sage: v.extensions(L)                                                       # needs sage.rings.function_field
            [2-adic valuation]

        Test that this works in towers::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y - x)
            sage: R.<z> = L[]
            sage: L.<z> = L.extension(z - y)
            sage: v = K.valuation(x)
            sage: v.extensions(L)
            [(x)-adic valuation]
        """

class RationalFunctionFieldValuation_base(FunctionFieldValuation_base):
    """
    Base class for valuations on rational function fields.

    TESTS::

        sage: K.<x> = FunctionField(GF(2))
        sage: v = K.valuation(x)  # indirect doctest
        sage: from sage.rings.function_field.valuation import RationalFunctionFieldValuation_base
        sage: isinstance(v, RationalFunctionFieldValuation_base)
        True
    """
    @cached_method
    def element_with_valuation(self, s):
        """
        Return an element with valuation ``s``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 6)
            sage: v = K.valuation(2)
            sage: R.<x> = K[]
            sage: w = GaussValuation(R, v).augmentation(x, 1/123)
            sage: K.<x> = FunctionField(K)
            sage: w = w.extension(K)
            sage: w.element_with_valuation(122/123)
            2/x
            sage: w.element_with_valuation(1)
            2
        """

class ClassicalFunctionFieldValuation_base(DiscreteFunctionFieldValuation_base):
    """
    Base class for discrete valuations on rational function fields that come
    from points on the projective line.

    TESTS::

        sage: K.<x> = FunctionField(GF(5))
        sage: v = K.valuation(x)  # indirect doctest
        sage: from sage.rings.function_field.valuation import ClassicalFunctionFieldValuation_base
        sage: isinstance(v, ClassicalFunctionFieldValuation_base)
        True
    """

class InducedRationalFunctionFieldValuation_base(FunctionFieldValuation_base):
    """
    Base class for function field valuation induced by a valuation on the
    underlying polynomial ring.

    TESTS::

        sage: K.<x> = FunctionField(QQ)
        sage: v = K.valuation(x^2 + 1) # indirect doctest
    """
    def __init__(self, parent, base_valuation) -> None:
        """
        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x) # indirect doctest
            sage: from sage.rings.function_field.valuation import InducedRationalFunctionFieldValuation_base
            sage: isinstance(v, InducedRationalFunctionFieldValuation_base)
            True
        """
    def uniformizer(self):
        """
        Return a uniformizing element for this valuation.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.valuation(x).uniformizer()
            x
        """
    def lift(self, F):
        """
        Return a lift of ``F`` to the domain of this valuation such
        that :meth:`reduce` returns the original element.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x)
            sage: v.lift(0)
            0
            sage: v.lift(1)
            1
        """
    def value_group(self):
        """
        Return the value group of this valuation.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.valuation(x).value_group()
            Additive Abelian Group generated by 1
        """
    def reduce(self, f):
        """
        Return the reduction of ``f`` in :meth:`residue_ring`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x^2 + 1)
            sage: v.reduce(x)                                                           # needs sage.rings.number_field
            u1
        """
    def extensions(self, L):
        """
        Return all extensions of this valuation to ``L`` which has a larger
        constant field than the domain of this valuation.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x^2 + 1)
            sage: L.<x> = FunctionField(GaussianIntegers().fraction_field())
            sage: v.extensions(L)  # indirect doctest
            [(x - I)-adic valuation, (x + I)-adic valuation]
        """
    def residue_ring(self):
        """
        Return the residue field of this valuation.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.valuation(x).residue_ring()
            Rational Field
        """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.valuation(x).restriction(QQ)
            Trivial valuation on Rational Field
        """
    def simplify(self, f, error=None, force: bool = False):
        """
        Return a simplified version of ``f``.

        Produce an element which differs from ``f`` by an element of
        valuation strictly greater than the valuation of ``f`` (or strictly
        greater than ``error`` if set.)

        If ``force`` is not set, then expensive simplifications may be avoided.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(2)
            sage: f = (x + 1)/(x - 1)

        As the coefficients of this fraction are small, we do not simplify as
        this could be very costly in some cases::

            sage: v.simplify(f)
            (x + 1)/(x - 1)

        However, simplification can be forced::

            sage: v.simplify(f, force=True)
            3
        """

class FiniteRationalFunctionFieldValuation(InducedRationalFunctionFieldValuation_base, ClassicalFunctionFieldValuation_base, RationalFunctionFieldValuation_base):
    """
    Valuation of a finite place of a function field.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: v = K.valuation(x + 1); v  # indirect doctest
        (x + 1)-adic valuation

    A finite place with residual degree::

        sage: w = K.valuation(x^2 + 1); w
        (x^2 + 1)-adic valuation

    A finite place with ramification::

        sage: K.<t> = FunctionField(GF(3))
        sage: L.<x> = FunctionField(K)
        sage: u = L.valuation(x^3 - t); u
        (x^3 + 2*t)-adic valuation

    A finite place with residual degree and ramification::

        sage: q = L.valuation(x^6 - t); q
        (x^6 + 2*t)-adic valuation
    """
    def __init__(self, parent, base_valuation) -> None:
        """
        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(x + 1)
            sage: from sage.rings.function_field.valuation import FiniteRationalFunctionFieldValuation
            sage: isinstance(v, FiniteRationalFunctionFieldValuation)
            True
        """

class NonClassicalRationalFunctionFieldValuation(InducedRationalFunctionFieldValuation_base, RationalFunctionFieldValuation_base):
    """
    Valuation induced by a valuation on the underlying polynomial ring which is
    non-classical.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: v = GaussValuation(QQ['x'], QQ.valuation(2))
        sage: w = K.valuation(v); w  # indirect doctest
        2-adic valuation
    """
    def __init__(self, parent, base_valuation) -> None:
        """
        TESTS:

        There is some support for discrete pseudo-valuations on rational
        function fields in the code. However, since these valuations must send
        elements to `-\\infty`, they are not supported yet::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(QQ['x'], QQ.valuation(2)).augmentation(x, infinity)
            sage: K.<x> = FunctionField(QQ)
            sage: w = K.valuation(v)
            sage: from sage.rings.function_field.valuation import NonClassicalRationalFunctionFieldValuation
            sage: isinstance(w, NonClassicalRationalFunctionFieldValuation)
            True
        """
    def residue_ring(self):
        """
        Return the residue field of this valuation.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: v = valuations.GaussValuation(QQ['x'], QQ.valuation(2))
            sage: w = K.valuation(v)
            sage: w.residue_ring()
            Rational function field in x over Finite Field of size 2

            sage: R.<x> = QQ[]
            sage: vv = v.augmentation(x, 1)
            sage: w = K.valuation(vv)
            sage: w.residue_ring()
            Rational function field in x over Finite Field of size 2

            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + 2*x)                                        # needs sage.rings.function_field
            sage: w.extension(L).residue_ring()                                         # needs sage.rings.function_field
            Function field in u2 defined by u2^2 + x

        TESTS:

        This still works for pseudo-valuations::

            sage: R.<x> = QQ[]
            sage: v = valuations.GaussValuation(R, QQ.valuation(2))
            sage: vv = v.augmentation(x, infinity)
            sage: K.<x> = FunctionField(QQ)
            sage: w = K.valuation(vv)
            sage: w.residue_ring()
            Finite Field of size 2
        """

class FunctionFieldFromLimitValuation(FiniteExtensionFromLimitValuation, DiscreteFunctionFieldValuation_base):
    """
    A valuation on a finite extensions of function fields `L=K[y]/(G)` where `K` is
    another function field.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - (x^2 + x + 1))                                  # needs sage.rings.function_field
        sage: v = K.valuation(x - 1)  # indirect doctest                                # needs sage.rings.function_field
        sage: w = v.extension(L); w                                                     # needs sage.rings.function_field
        (x - 1)-adic valuation
    """
    def __init__(self, parent, approximant, G, approximants) -> None:
        """
        TESTS::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - (x^2 + x + 1))
            sage: v = K.valuation(x - 1) # indirect doctest
            sage: w = v.extension(L)
            sage: from sage.rings.function_field.valuation import FunctionFieldFromLimitValuation
            sage: isinstance(w, FunctionFieldFromLimitValuation)
            True
        """
    def scale(self, scalar):
        """
        Return this valuation scaled by ``scalar``.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - (x^2 + x + 1))
            sage: v = K.valuation(x - 1) # indirect doctest
            sage: w = v.extension(L)
            sage: 3*w
            3 * (x - 1)-adic valuation
        """

class FunctionFieldMappedValuation_base(FunctionFieldValuation_base, MappedValuation_base):
    """
    A valuation on a function field which relies on a ``base_valuation`` on an
    isomorphic function field.

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2))
        sage: v = K.valuation(1/x); v
        Valuation at the infinite place
    """
    def __init__(self, parent, base_valuation, to_base_valuation_domain, from_base_valuation_domain) -> None:
        """
        TESTS::

            sage: K.<x> = FunctionField(GF(2))
            sage: v = K.valuation(1/x)
            sage: from sage.rings.function_field.valuation import FunctionFieldMappedValuation_base
            sage: isinstance(v, FunctionFieldMappedValuation_base)
            True
        """
    def scale(self, scalar):
        """
        Return this valuation scaled by ``scalar``.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + y + x^3)                                    # needs sage.rings.function_field
            sage: v = K.valuation(1/x)
            sage: w = v.extension(L)                                                    # needs sage.rings.function_field
            sage: 3*w                                                                   # needs sage.rings.function_field
            3 * (x)-adic valuation (in Rational function field in x over Finite Field of size 2 after x |--> 1/x)
        """
    def is_discrete_valuation(self):
        """
        Return whether this is a discrete valuation.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^4 - 1)
            sage: v = K.valuation(1/x)
            sage: w0,w1 = v.extensions(L)
            sage: w0.is_discrete_valuation()
            True
        """

class FunctionFieldMappedValuationRelative_base(FunctionFieldMappedValuation_base):
    """
    A valuation on a function field which relies on a ``base_valuation`` on an
    isomorphic function field and which is such that the map from and to the
    other function field is the identity on the constant field.

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2))
        sage: v = K.valuation(1/x); v
        Valuation at the infinite place
    """
    def __init__(self, parent, base_valuation, to_base_valuation_domain, from_base_valuation_domain) -> None:
        """
        TESTS::

            sage: K.<x> = FunctionField(GF(2))
            sage: v = K.valuation(1/x)
            sage: from sage.rings.function_field.valuation import FunctionFieldMappedValuationRelative_base
            sage: isinstance(v, FunctionFieldMappedValuationRelative_base)
            True
        """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: K.valuation(1/x).restriction(GF(2))
            Trivial valuation on Finite Field of size 2
        """

class RationalFunctionFieldMappedValuation(FunctionFieldMappedValuationRelative_base, RationalFunctionFieldValuation_base):
    """
    Valuation on a rational function field that is implemented after a map to
    an isomorphic rational function field.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: R.<x> = QQ[]
        sage: w = GaussValuation(R, QQ.valuation(2)).augmentation(x, 1)
        sage: w = K.valuation(w)
        sage: v = K.valuation((w, K.hom([~K.gen()]), K.hom([~K.gen()]))); v
        Valuation on rational function field induced by
        [ Gauss valuation induced by 2-adic valuation, v(x) = 1 ]
        (in Rational function field in x over Rational Field after x |--> 1/x)
    """
    def __init__(self, parent, base_valuation, to_base_valuation_doain, from_base_valuation_domain) -> None:
        """
        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<x> = QQ[]
            sage: w = GaussValuation(R, QQ.valuation(2)).augmentation(x, 1)
            sage: w = K.valuation(w)
            sage: v = K.valuation((w, K.hom([~K.gen()]), K.hom([~K.gen()])))
            sage: from sage.rings.function_field.valuation import RationalFunctionFieldMappedValuation
            sage: isinstance(v, RationalFunctionFieldMappedValuation)
            True
        """

class InfiniteRationalFunctionFieldValuation(FunctionFieldMappedValuationRelative_base, RationalFunctionFieldValuation_base, ClassicalFunctionFieldValuation_base):
    """
    Valuation of the infinite place of a function field.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: v = K.valuation(1/x)  # indirect doctest
    """
    def __init__(self, parent) -> None:
        """
        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(1/x)  # indirect doctest
            sage: from sage.rings.function_field.valuation import InfiniteRationalFunctionFieldValuation
            sage: isinstance(v, InfiniteRationalFunctionFieldValuation)
            True
        """

class FunctionFieldExtensionMappedValuation(FunctionFieldMappedValuationRelative_base):
    """
    A valuation on a finite extensions of function fields `L=K[y]/(G)` where `K` is
    another function field which redirects to another ``base_valuation`` on an
    isomorphism function field `M=K[y]/(H)`.

    The isomorphisms must be trivial on ``K``.

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2))
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 + y + x^3)                                        # needs sage.rings.function_field
        sage: v = K.valuation(1/x)
        sage: w = v.extension(L)                                                        # needs sage.rings.function_field

        sage: w(x)                                                                      # needs sage.rings.function_field
        -1
        sage: w(y)                                                                      # needs sage.rings.function_field
        -3/2
        sage: w.uniformizer()                                                           # needs sage.rings.function_field
        1/x^2*y

    TESTS::

        sage: from sage.rings.function_field.valuation import FunctionFieldExtensionMappedValuation
        sage: isinstance(w, FunctionFieldExtensionMappedValuation)                      # needs sage.rings.function_field
        True
    """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 + y + x^3)
            sage: v = K.valuation(1/x)
            sage: w = v.extension(L)
            sage: w.restriction(K) is v
            True
        """
