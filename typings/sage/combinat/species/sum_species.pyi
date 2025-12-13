from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import SpeciesStructureWrapper as SpeciesStructureWrapper
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SumSpeciesStructure(SpeciesStructureWrapper): ...

class SumSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    def __init__(self, F, G, min=None, max=None, weight=None) -> None:
        """
        Return the sum of two species.

        EXAMPLES::

            sage: S = species.PermutationSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: A = S+S
            sage: A.generating_series()[:5]
            [2, 2, 2, 2, 2]

            sage: P = species.PermutationSpecies()
            sage: F = P + P
            sage: F._check()                                                            # needs sage.libs.flint
            True
            sage: F == loads(dumps(F))
            True

        TESTS::

            sage: A = species.SingletonSpecies() + species.SingletonSpecies()
            sage: B = species.SingletonSpecies() + species.SingletonSpecies()
            sage: C = species.SingletonSpecies() + species.SingletonSpecies(min=2)
            sage: A is B
            True
            sage: (A is C) or (A == C)
            False
        """
    def left_summand(self):
        """
        Return the left summand of this species.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: F = P + P*P
            sage: F.left_summand()
            Permutation species
        """
    def right_summand(self):
        """
        Return the right summand of this species.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: F = P + P*P
            sage: F.right_summand()
            Product of (Permutation species) and (Permutation species)
        """
    def weight_ring(self):
        """
        Return the weight ring for this species. This is determined by
        asking Sage's coercion model what the result is when you add
        elements of the weight rings for each of the operands.

        EXAMPLES::

            sage: S = species.SetSpecies()
            sage: C = S+S
            sage: C.weight_ring()
            Rational Field

        ::

            sage: S = species.SetSpecies(weight=QQ['t'].gen())
            sage: C = S + S
            sage: C.weight_ring()
            Univariate Polynomial Ring in t over Rational Field
        """
SumSpecies_class = SumSpecies
