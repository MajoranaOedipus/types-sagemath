from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure

class FunctorialCompositionStructure(GenericSpeciesStructure): ...

class FunctorialCompositionSpecies(GenericCombinatorialSpecies):
    def __init__(self, F, G, min=None, max=None, weight=None) -> None:
        """
        Return the functorial composition of two species.

        EXAMPLES::

            sage: E = species.SetSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: E2 = species.SetSpecies(size=2)
            sage: WP = species.SubsetSpecies()
            sage: P2 = E2*E
            sage: G = WP.functorial_composition(P2)
            sage: G.isotype_generating_series()[0:5]                                    # needs sage.modules
            [1, 1, 2, 4, 11]

            sage: G = species.SimpleGraphSpecies()
            sage: c = G.generating_series()[0:2]
            sage: type(G)
            <class 'sage.combinat.species.functorial_composition_species.FunctorialCompositionSpecies'>
            sage: G == loads(dumps(G))
            True
            sage: G._check()  # False due to isomorphism types not being implemented    # needs sage.modules
            False
        """
    def weight_ring(self):
        """
        Return the weight ring for this species. This is determined by
        asking Sage's coercion model what the result is when you multiply
        (and add) elements of the weight rings for each of the operands.

        EXAMPLES::

            sage: G = species.SimpleGraphSpecies()
            sage: G.weight_ring()
            Rational Field
        """
FunctorialCompositionSpecies_class = FunctorialCompositionSpecies
