from .set import Set as Set, Set_add_sub_operators as Set_add_sub_operators, Set_base as Set_base, Set_boolean_operators as Set_boolean_operators
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.subset import uniq as uniq
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import Expression as Expression
from sage.structure.parent import Parent as Parent, Set_generic as Set_generic
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ConditionSet(Set_generic, Set_base, Set_boolean_operators, Set_add_sub_operators, UniqueRepresentation):
    """
    Set of elements of a universe that satisfy given predicates.

    INPUT:

    - ``universe`` -- set

    - ``*predicates`` -- callables

    - ``vars`` or ``names`` -- (default: inferred from ``predicates`` if any predicate is
      an element of a :class:`~sage.symbolic.callable.CallableSymbolicExpressionRing_class`)
      variables or names of variables

    - ``category`` -- (default: inferred from ``universe``) a category

    EXAMPLES::

        sage: Evens = ConditionSet(ZZ, is_even); Evens
        { x ∈ Integer Ring : <function is_even at 0x...>(x) }
        sage: 2 in Evens
        True
        sage: 3 in Evens
        False
        sage: 2.0 in Evens
        True

        sage: Odds = ConditionSet(ZZ, is_odd); Odds
        { x ∈ Integer Ring : <function is_odd at 0x...>(x) }
        sage: EvensAndOdds = Evens | Odds; EvensAndOdds
        Set-theoretic union of
         { x ∈ Integer Ring : <function is_even at 0x...>(x) } and
         { x ∈ Integer Ring : <function is_odd at 0x...>(x) }
        sage: 5 in EvensAndOdds
        True
        sage: 7/2 in EvensAndOdds
        False

        sage: var('y')                                                                  # needs sage.symbolic
        y
        sage: SmallOdds = ConditionSet(ZZ, is_odd, abs(y) <= 11, vars=[y]); SmallOdds   # needs sage.symbolic
        { y ∈ Integer Ring : abs(y) <= 11, <function is_odd at 0x...>(y) }

        sage: # needs sage.geometry.polyhedron
        sage: P = polytopes.cube(); P
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        sage: P.rename('P')
        sage: P_inter_B = ConditionSet(P, lambda x: x.norm() < 1.2); P_inter_B
        { x ∈ P : <function <lambda> at 0x...>(x) }
        sage: vector([1, 0, 0]) in P_inter_B
        True
        sage: vector([1, 1, 1]) in P_inter_B                                            # needs sage.symbolic
        False

        sage: # needs sage.symbolic
        sage: predicate(x, y, z) = sqrt(x^2 + y^2 + z^2) < 1.2; predicate
        (x, y, z) |--> sqrt(x^2 + y^2 + z^2) < 1.20000000000000
        sage: P_inter_B_again = ConditionSet(P, predicate); P_inter_B_again             # needs sage.geometry.polyhedron
        { (x, y, z) ∈ P : sqrt(x^2 + y^2 + z^2) < 1.20000000000000 }
        sage: vector([1, 0, 0]) in P_inter_B_again                                      # needs sage.geometry.polyhedron
        True
        sage: vector([1, 1, 1]) in P_inter_B_again                                      # needs sage.geometry.polyhedron
        False

    Iterating over subsets determined by predicates::

        sage: Odds = ConditionSet(ZZ, is_odd); Odds
        { x ∈ Integer Ring : <function is_odd at 0x...>(x) }
        sage: list(Odds.iterator_range(stop=6))
        [1, -1, 3, -3, 5, -5]

        sage: R = IntegerModRing(8)
        sage: R_primes = ConditionSet(R, is_prime); R_primes
        { x ∈ Ring of integers modulo 8 : <function is_prime at 0x...>(x) }
        sage: R_primes.is_finite()
        True
        sage: list(R_primes)
        [2, 6]

    Using ``ConditionSet`` without predicates provides a way of attaching variable names
    to a set::

        sage: Z3 = ConditionSet(ZZ^3, vars=['x', 'y', 'z']); Z3                         # needs sage.modules
        { (x, y, z) ∈ Ambient free module of rank 3
                       over the principal ideal domain Integer Ring }
        sage: Z3.variable_names()                                                       # needs sage.modules
        ('x', 'y', 'z')
        sage: Z3.arguments()                                                            # needs sage.modules sage.symbolic
        (x, y, z)

        sage: Q4.<a, b, c, d> = ConditionSet(QQ^4); Q4                                  # needs sage.modules sage.symbolic
        { (a, b, c, d) ∈ Vector space of dimension 4 over Rational Field }
        sage: Q4.variable_names()                                                       # needs sage.modules sage.symbolic
        ('a', 'b', 'c', 'd')
        sage: Q4.arguments()                                                            # needs sage.modules sage.symbolic
        (a, b, c, d)

    TESTS::

        sage: TestSuite(P_inter_B).run(skip='_test_pickling')  # cannot pickle lambdas  # needs sage.geometry.polyhedron
        sage: TestSuite(P_inter_B_again).run()                                          # needs sage.geometry.polyhedron sage.symbolic
    """
    @staticmethod
    def __classcall_private__(cls, universe, *predicates, vars=None, names=None, category=None):
        '''
        Normalize init arguments.

        TESTS::

            sage: ConditionSet(ZZ, names=["x"]) is ConditionSet(ZZ, names=x)                        # needs sage.symbolic
            True
            sage: ConditionSet(RR, x > 0, names=x) is ConditionSet(RR, (x > 0).function(x))         # needs sage.symbolic
            True
        '''
    def __init__(self, universe, *predicates, names=None, category=None) -> None:
        """
        TESTS::

            sage: Evens = ConditionSet(ZZ, is_even); Evens
            { x ∈ Integer Ring : <function is_even at 0x...>(x) }
            sage: TestSuite(Evens).run()
        """
    @cached_method
    def arguments(self):
        """
        Return the variables of ``self`` as elements of the symbolic ring.

        EXAMPLES::

            sage: Odds = ConditionSet(ZZ, is_odd); Odds
            { x ∈ Integer Ring : <function is_odd at 0x...>(x) }
            sage: args = Odds.arguments(); args                                         # needs sage.symbolic
            (x,)
            sage: args[0].parent()                                                      # needs sage.symbolic
            Symbolic Ring
        """
    def ambient(self):
        """
        Return the universe of ``self``.

        EXAMPLES::

            sage: Evens = ConditionSet(ZZ, is_even); Evens
            { x ∈ Integer Ring : <function is_even at 0x...>(x) }
            sage: Evens.ambient()
            Integer Ring
        """
    def intersection(self, X):
        """
        Return the intersection of ``self`` and ``X``.

        EXAMPLES::

            sage: # needs sage.modules sage.symbolic
            sage: in_small_oblong(x, y) = x^2 + 3 * y^2 <= 42
            sage: SmallOblongUniverse = ConditionSet(QQ^2, in_small_oblong)
            sage: SmallOblongUniverse
            { (x, y) ∈ Vector space of dimension 2
                                over Rational Field : x^2 + 3*y^2 <= 42 }
            sage: parity_check(x, y) = abs(sin(pi/2*(x + y))) < 1/1000
            sage: EvenUniverse = ConditionSet(ZZ^2, parity_check); EvenUniverse
            { (x, y) ∈ Ambient free module of rank 2 over the principal ideal
                       domain Integer Ring : abs(sin(1/2*pi*x + 1/2*pi*y)) < (1/1000) }
            sage: SmallOblongUniverse & EvenUniverse
            { (x, y) ∈ Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1 0]
            [0 1] : x^2 + 3*y^2 <= 42, abs(sin(1/2*pi*x + 1/2*pi*y)) < (1/1000) }

        Combining two ``ConditionSet``s with different formal variables works correctly.
        The formal variables of the intersection are taken from ``self``::

            sage: # needs sage.modules sage.symbolic
            sage: SmallMirrorUniverse = ConditionSet(QQ^2, in_small_oblong,
            ....:                                    vars=(y, x))
            sage: SmallMirrorUniverse
            { (y, x) ∈ Vector space of dimension 2
                               over Rational Field : 3*x^2 + y^2 <= 42 }
            sage: SmallOblongUniverse & SmallMirrorUniverse
            { (x, y) ∈ Vector space of dimension 2
                               over Rational Field : x^2 + 3*y^2 <= 42 }
            sage: SmallMirrorUniverse & SmallOblongUniverse
            { (y, x) ∈ Vector space of dimension 2
                               over Rational Field : 3*x^2 + y^2 <= 42 }
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        TESTS::

            sage: Odds = ConditionSet(ZZ, is_odd); Odds
            { x ∈ Integer Ring : <function is_odd at 0x...>(x) }
            sage: list(Odds.iterator_range(stop=6))
            [1, -1, 3, -3, 5, -5]
        """
