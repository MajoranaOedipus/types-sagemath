from sage.arith.misc import divisors as divisors, euler_phi as euler_phi
from sage.combinat.species.misc import accept_size as accept_size
from sage.combinat.species.species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from sage.combinat.species.structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CycleSpeciesStructure(GenericSpeciesStructure):
    def canonical_label(self):
        '''
        EXAMPLES::

            sage: P = species.CycleSpecies()
            sage: P.structures(["a","b","c"]).random_element().canonical_label()
            (\'a\', \'b\', \'c\')
        '''
    def permutation_group_element(self):
        '''
        Return this cycle as a permutation group element.

        EXAMPLES::

            sage: F = species.CycleSpecies()
            sage: a = F.structures(["a", "b", "c"])[0]; a
            (\'a\', \'b\', \'c\')
            sage: a.permutation_group_element()                                         # needs sage.groups
            (1,2,3)
        '''
    def transport(self, perm):
        '''
        Return the transport of this structure along the permutation
        perm.

        EXAMPLES::

            sage: F = species.CycleSpecies()
            sage: a = F.structures(["a", "b", "c"])[0]; a
            (\'a\', \'b\', \'c\')
            sage: p = PermutationGroupElement((1,2))                                    # needs sage.groups
            sage: a.transport(p)                                                        # needs sage.groups
            (\'a\', \'c\', \'b\')
        '''
    def automorphism_group(self):
        """
        Return the group of permutations whose action on this structure
        leave it fixed.

        EXAMPLES::

            sage: P = species.CycleSpecies()
            sage: a = P.structures([1, 2, 3, 4])[0]; a
            (1, 2, 3, 4)
            sage: a.automorphism_group()                                                # needs sage.groups
            Permutation Group with generators [(1,2,3,4)]

        ::

            sage: [a.transport(perm) for perm in a.automorphism_group()]                # needs sage.groups
            [(1, 2, 3, 4), (1, 2, 3, 4), (1, 2, 3, 4), (1, 2, 3, 4)]
        """

class CycleSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    @staticmethod
    @accept_size
    def __classcall__(cls, *args, **kwds):
        """
        EXAMPLES::

            sage: C = species.CycleSpecies(); C
            Cyclic permutation species
        """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of cycles.

        EXAMPLES::

            sage: C = species.CycleSpecies(); C
            Cyclic permutation species
            sage: C.structures([1,2,3,4]).list()
            [(1, 2, 3, 4),
             (1, 2, 4, 3),
             (1, 3, 2, 4),
             (1, 3, 4, 2),
             (1, 4, 2, 3),
             (1, 4, 3, 2)]

        TESTS:

        We check to verify that the caching of species is actually
        working.

        ::

            sage: species.CycleSpecies() is species.CycleSpecies()
            True

            sage: P = species.CycleSpecies()
            sage: c = P.generating_series()[:3]
            sage: P._check()
            True
            sage: P == loads(dumps(P))
            True
        """
CycleSpecies_class = CycleSpecies
