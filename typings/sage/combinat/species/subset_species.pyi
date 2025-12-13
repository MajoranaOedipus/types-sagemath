from .set_species import SetSpecies as SetSpecies
from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.arith.misc import factorial as factorial
from sage.combinat.species.misc import accept_size as accept_size
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SubsetSpeciesStructure(GenericSpeciesStructure):
    def canonical_label(self):
        '''
        Return the canonical label of ``self``.

        EXAMPLES::

            sage: P = species.SubsetSpecies()
            sage: S = P.structures(["a", "b", "c"])
            sage: [s.canonical_label() for s in S]
            [{}, {\'a\'}, {\'a\'}, {\'a\'}, {\'a\', \'b\'}, {\'a\', \'b\'}, {\'a\', \'b\'}, {\'a\', \'b\', \'c\'}]
        '''
    def label_subset(self):
        '''
        Return a subset of the labels that "appear" in this structure.

        EXAMPLES::

            sage: P = species.SubsetSpecies()
            sage: S = P.structures(["a", "b", "c"])
            sage: [s.label_subset() for s in S]
            [[], [\'a\'], [\'b\'], [\'c\'], [\'a\', \'b\'], [\'a\', \'c\'], [\'b\', \'c\'], [\'a\', \'b\', \'c\']]
        '''
    def transport(self, perm):
        '''
        Return the transport of this subset along the permutation perm.

        EXAMPLES::

            sage: F = species.SubsetSpecies()
            sage: a = F.structures(["a", "b", "c"])[5]; a
            {\'a\', \'c\'}
            sage: p = PermutationGroupElement((1,2))                                    # needs sage.groups
            sage: a.transport(p)                                                        # needs sage.groups
            {\'b\', \'c\'}
            sage: p = PermutationGroupElement((1,3))                                    # needs sage.groups
            sage: a.transport(p)                                                        # needs sage.groups
            {\'a\', \'c\'}
        '''
    def automorphism_group(self):
        """
        Return the group of permutations whose action on this subset leave
        it fixed.

        EXAMPLES::

            sage: F = species.SubsetSpecies()
            sage: a = F.structures([1,2,3,4])[6]; a
            {1, 3}
            sage: a.automorphism_group()                                                # needs sage.groups
            Permutation Group with generators [(2,4), (1,3)]

        ::

            sage: [a.transport(g) for g in a.automorphism_group()]                      # needs sage.groups
            [{1, 3}, {1, 3}, {1, 3}, {1, 3}]
        """
    def complement(self):
        '''
        Return the complement of ``self``.

        EXAMPLES::

            sage: F = species.SubsetSpecies()
            sage: a = F.structures(["a", "b", "c"])[5]; a
            {\'a\', \'c\'}
            sage: a.complement()
            {\'b\'}
        '''

class SubsetSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    @staticmethod
    @accept_size
    def __classcall__(cls, *args, **kwds):
        """
        EXAMPLES::

            sage: S = species.SubsetSpecies(); S
            Subset species
        """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of subsets.

        EXAMPLES::

            sage: S = species.SubsetSpecies()
            sage: S.generating_series()[0:5]
            [1, 2, 2, 4/3, 2/3]
            sage: S.isotype_generating_series()[0:5]
            [1, 2, 3, 4, 5]

            sage: S = species.SubsetSpecies()
            sage: c = S.generating_series()[0:3]
            sage: S._check()
            True
            sage: S == loads(dumps(S))
            True
        """
SubsetSpecies_class = SubsetSpecies
