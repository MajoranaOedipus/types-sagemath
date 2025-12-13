from .partition_species import PartitionSpecies as PartitionSpecies
from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CompositionSpeciesStructure(GenericSpeciesStructure):
    def __init__(self, parent, labels, pi, f, gs) -> None:
        """
        TESTS::

            sage: E = species.SetSpecies(); C = species.CycleSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: L = E(C)
            sage: a = L.structures(['a','b','c']).random_element()                      # needs sage.libs.flint
            sage: a == loads(dumps(a))                                                  # needs sage.libs.flint
            True
        """
    def transport(self, perm):
        """
        EXAMPLES::

            sage: p = PermutationGroupElement((2,3))                                    # needs sage.groups
            sage: E = species.SetSpecies(); C = species.CycleSpecies()
            sage: L = E(C)
            sage: S = L.structures(['a','b','c']).list()                                # needs sage.libs.flint
            sage: a = S[2]; a                                                           # needs sage.libs.flint
            F-structure: {{'a', 'c'}, {'b'}}; G-structures: (('a', 'c'), ('b'))
            sage: a.transport(p)                                                        # needs sage.groups sage.libs.flint
            F-structure: {{'a', 'b'}, {'c'}}; G-structures: (('a', 'c'), ('b'))
        """
    def change_labels(self, labels):
        """
        Return a relabelled structure.

        INPUT:

        - ``labels`` -- list of labels

        OUTPUT:

        A structure with the `i`-th label of ``self`` replaced with the `i`-th
        label of the list.

        EXAMPLES::

            sage: E = species.SetSpecies(); C = species.CycleSpecies()
            sage: L = E(C)
            sage: S = L.structures(['a','b','c']).list()                                # needs sage.libs.flint
            sage: a = S[2]; a                                                           # needs sage.libs.flint
            F-structure: {{'a', 'c'}, {'b'}}; G-structures: (('a', 'c'), ('b'))
            sage: a.change_labels([1,2,3])                                              # needs sage.libs.flint
            F-structure: {{1, 3}, {2}}; G-structures: [(1, 3), (2)]
        """

class CompositionSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    def __init__(self, F, G, min=None, max=None, weight=None) -> None:
        """
        Return the composition of two species.

        EXAMPLES::

            sage: E = species.SetSpecies()
            sage: C = species.CycleSpecies()
            sage: S = E(C)
            sage: S.generating_series()[:5]
            [1, 1, 1, 1, 1]
            sage: E(C) is S
            True

        TESTS::

            sage: E = species.SetSpecies(); C = species.CycleSpecies()
            sage: L = E(C)
            sage: c = L.generating_series()[:3]
            sage: L._check()  #False due to isomorphism types not being implemented     # needs sage.libs.flint
            False
            sage: L == loads(dumps(L))
            True
        """
    def weight_ring(self):
        """
        Return the weight ring for this species. This is determined by
        asking Sage's coercion model what the result is when you multiply
        (and add) elements of the weight rings for each of the operands.

        EXAMPLES::

            sage: E = species.SetSpecies(); C = species.CycleSpecies()
            sage: L = E(C)
            sage: L.weight_ring()
            Rational Field
        """
CompositionSpecies_class = CompositionSpecies
