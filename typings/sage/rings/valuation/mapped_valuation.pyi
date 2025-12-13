from .valuation import DiscretePseudoValuation as DiscretePseudoValuation, DiscreteValuation as DiscreteValuation
from sage.misc.abstract_method import abstract_method as abstract_method

class MappedValuation_base(DiscretePseudoValuation):
    '''
    A valuation which is implemented through another proxy "base" valuation.

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x)
        sage: v = K.valuation(0)
        sage: w = v.extension(L); w
        (x)-adic valuation

    TESTS::

        sage: TestSuite(w).run()                # long time                             # needs sage.rings.function_field
    '''
    def __init__(self, parent, base_valuation) -> None:
        """
        .. TODO::

            It is annoying that we have to wrap any possible method on
            ``base_valuation`` in this class. It would be nice if this would
            somehow be done automagically, e.g., by adding annotations to the
            methods in ``base_valuation`` that explain which parameters and
            return values need to be mapped and how.

        TESTS::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^2 + 1)
            sage: v = K.valuation(0)
            sage: w = v.extension(L); w
            (x)-adic valuation
            sage: from sage.rings.valuation.mapped_valuation import MappedValuation_base
            sage: isinstance(w, MappedValuation_base)
            True
        """
    def residue_ring(self):
        """
        Return the residue ring of this valuation.

        EXAMPLES::

            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)                                          # needs sage.rings.number_field
            sage: v = valuations.pAdicValuation(QQ, 2)
            sage: v.extension(L).residue_ring()                                         # needs sage.rings.number_field
            Finite Field of size 2
        """
    def uniformizer(self):
        """
        Return a uniformizing element of this valuation.

        EXAMPLES::

            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)                                          # needs sage.rings.number_field
            sage: v = valuations.pAdicValuation(QQ, 2)
            sage: v.extension(L).uniformizer()                                          # needs sage.rings.number_field
            t + 1
        """
    def reduce(self, f):
        """
        Return the reduction of ``f`` in the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field` of this valuation.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - (x - 2))
            sage: v = K.valuation(0)
            sage: w = v.extension(L)
            sage: w.reduce(y)
            u1
        """
    def lift(self, F):
        """
        Lift ``F`` from the :meth:`~sage.rings.valuation.valuation_space.DiscretePseudoValuationSpace.ElementMethods.residue_field`
        of this valuation into its domain.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: v = K.valuation(2)
            sage: w = v.extension(L)
            sage: w.lift(w.residue_field().gen())
            y
        """
    def simplify(self, x, error=None, force: bool = False):
        """
        Return a simplified version of ``x``.

        Produce an element which differs from ``x`` by an element of
        valuation strictly greater than the valuation of ``x`` (or strictly
        greater than ``error`` if set.)

        If ``force`` is not set, then expensive simplifications may be avoided.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: v = K.valuation(0)
            sage: w = v.extensions(L)[0]

        As :meth:`_relative_size` misses the bloated term ``x^32``, the
        following term does not get simplified::

            sage: w.simplify(y + x^32)                                                  # needs sage.rings.function_field
            y + x^32

        In this case the simplification can be forced but this should not
        happen as a default as the recursive simplification can be quite
        costly::

            sage: w.simplify(y + x^32, force=True)                                      # needs sage.rings.function_field
            y
        """
    def element_with_valuation(self, s):
        """
        Return an element with valuation ``s``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = valuations.pAdicValuation(QQ, 5)
            sage: u,uu = v.extensions(L)
            sage: u.element_with_valuation(1)
            5
        """

class FiniteExtensionFromInfiniteValuation(MappedValuation_base, DiscreteValuation):
    """
    A valuation on a quotient of the form `L=K[x]/(G)` with an irreducible `G`
    which is internally backed by a pseudo-valuations on `K[x]` which sends `G`
    to infinity.

    INPUT:

    - ``parent`` -- the containing valuation space (usually the space of
      discrete valuations on `L`)

    - ``base_valuation`` -- an infinite valuation on `K[x]` which takes `G` to
      infinity

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x)
        sage: v = K.valuation(0)
        sage: w = v.extension(L); w
        (x)-adic valuation
    """
    def __init__(self, parent, base_valuation) -> None:
        """
        TESTS::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: v = K.valuation(0)
            sage: w = v.extension(L)
            sage: from sage.rings.valuation.mapped_valuation import FiniteExtensionFromInfiniteValuation
            sage: isinstance(w, FiniteExtensionFromInfiniteValuation)
            True
            sage: TestSuite(w).run()            # long time
        """
    def restriction(self, ring):
        """
        Return the restriction of this valuation to ``ring``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = valuations.pAdicValuation(QQ, 2)
            sage: w = v.extension(L)
            sage: w.restriction(K) is v
            True
        """
    def simplify(self, x, error=None, force: bool = False):
        """
        Return a simplified version of ``x``.

        Produce an element which differs from ``x`` by an element of
        valuation strictly greater than the valuation of ``x`` (or strictly
        greater than ``error`` if set.)

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = valuations.pAdicValuation(QQ, 5)
            sage: u,uu = v.extensions(L)
            sage: f = 125*t + 1
            sage: u.simplify(f, error=u(f), force=True)
            1
        """
    def lower_bound(self, x):
        """
        Return a lower bound of this valuation at ``x``.

        Use this method to get an approximation of the valuation of ``x``
        when speed is more important than accuracy.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = valuations.pAdicValuation(QQ, 5)
            sage: u,uu = v.extensions(L)
            sage: u.lower_bound(t + 2)
            0
            sage: u(t + 2)
            1
        """
    def upper_bound(self, x):
        """
        Return an upper bound of this valuation at ``x``.

        Use this method to get an approximation of the valuation of ``x``
        when speed is more important than accuracy.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QQ
            sage: R.<t> = K[]
            sage: L.<t> = K.extension(t^2 + 1)
            sage: v = valuations.pAdicValuation(QQ, 5)
            sage: u,uu = v.extensions(L)
            sage: u.upper_bound(t + 2) >= 1
            True
            sage: u(t + 2)
            1
        """

class FiniteExtensionFromLimitValuation(FiniteExtensionFromInfiniteValuation):
    """
    An extension of a valuation on a finite field extensions `L=K[x]/(G)` which
    is induced by an infinite limit valuation on `K[x]`.

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x)
        sage: v = K.valuation(1)
        sage: w = v.extensions(L); w
        [[ (x - 1)-adic valuation, v(y + 1) = 1 ]-adic valuation,
         [ (x - 1)-adic valuation, v(y - 1) = 1 ]-adic valuation]

    TESTS::

        sage: TestSuite(w[0]).run()             # long time                             # needs sage.rings.function_field
        sage: TestSuite(w[1]).run()             # long time                             # needs sage.rings.function_field
    """
    def __init__(self, parent, approximant, G, approximants) -> None:
        """
        EXAMPLES:

        Note that this implementation is also used when the underlying limit is
        only taken over a finite sequence of valuations::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: v = K.valuation(2)
            sage: w = v.extension(L); w
            (x - 2)-adic valuation
            sage: from sage.rings.valuation.mapped_valuation import FiniteExtensionFromLimitValuation
            sage: isinstance(w, FiniteExtensionFromLimitValuation)
            True
        """
