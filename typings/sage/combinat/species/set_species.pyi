from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from sage.arith.misc import factorial as factorial
from sage.combinat.species.misc import accept_size as accept_size
from sage.combinat.species.structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SetSpeciesStructure(GenericSpeciesStructure):
    def canonical_label(self):
        '''
        EXAMPLES::

            sage: S = species.SetSpecies()
            sage: a = S.structures(["a","b","c"]).random_element(); a
            {\'a\', \'b\', \'c\'}
            sage: a.canonical_label()
            {\'a\', \'b\', \'c\'}
        '''
    def transport(self, perm):
        '''
        Return the transport of this set along the permutation perm.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: a = F.structures(["a", "b", "c"]).random_element(); a
            {\'a\', \'b\', \'c\'}
            sage: p = PermutationGroupElement((1,2))                                    # needs sage.groups
            sage: a.transport(p)                                                        # needs sage.groups
            {\'a\', \'b\', \'c\'}
        '''
    def automorphism_group(self):
        '''
        Return the group of permutations whose action on this set leave it
        fixed. For the species of sets, there is only one isomorphism
        class, so every permutation is in its automorphism group.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: a = F.structures(["a", "b", "c"]).random_element(); a
            {\'a\', \'b\', \'c\'}
            sage: a.automorphism_group()                                                # needs sage.groups
            Symmetric group of order 3! as a permutation group
        '''

class SetSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    @staticmethod
    @accept_size
    def __classcall__(cls, *args, **kwds):
        """
        EXAMPLES::

            sage: E = species.SetSpecies(); E
            Set species
        """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of sets.

        EXAMPLES::

            sage: E = species.SetSpecies()
            sage: E.structures([1,2,3]).list()
            [{1, 2, 3}]
            sage: E.isotype_generating_series()[0:4]
            [1, 1, 1, 1]

            sage: S = species.SetSpecies()
            sage: c = S.generating_series()[0:3]
            sage: S._check()
            True
            sage: S == loads(dumps(S))
            True
        """
SetSpecies_class = SetSpecies
