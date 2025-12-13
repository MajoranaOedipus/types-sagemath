from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.combinat.species.misc import accept_size as accept_size
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PermutationSpeciesStructure(GenericSpeciesStructure):
    def canonical_label(self):
        '''
        EXAMPLES::

            sage: P = species.PermutationSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.

            sage: S = P.structures(["a", "b", "c"])
            sage: [s.canonical_label() for s in S]
            [[\'a\', \'b\', \'c\'],
             [\'b\', \'a\', \'c\'],
             [\'b\', \'a\', \'c\'],
             [\'b\', \'c\', \'a\'],
             [\'b\', \'c\', \'a\'],
             [\'b\', \'a\', \'c\']]
        '''
    def permutation_group_element(self):
        '''
        Return ``self`` as a permutation group element.

        EXAMPLES::

            sage: p = PermutationGroupElement((2,3,4))
            sage: P = species.PermutationSpecies()
            sage: a = P.structures(["a", "b", "c", "d"])[2]; a
            [\'a\', \'c\', \'b\', \'d\']
            sage: a.permutation_group_element()
            (2,3)
        '''
    def transport(self, perm):
        '''
        Return the transport of this structure along the permutation
        perm.

        EXAMPLES::

            sage: p = PermutationGroupElement((2,3,4))
            sage: P = species.PermutationSpecies()
            sage: a = P.structures(["a", "b", "c", "d"])[2]; a
            [\'a\', \'c\', \'b\', \'d\']
            sage: a.transport(p)
            [\'a\', \'d\', \'c\', \'b\']
        '''
    def automorphism_group(self):
        '''
        Return the group of permutations whose action on this structure
        leave it fixed.

        EXAMPLES::

            sage: set_random_seed(0)
            sage: p = PermutationGroupElement((2,3,4))
            sage: P = species.PermutationSpecies()
            sage: a = P.structures(["a", "b", "c", "d"])[2]; a
            [\'a\', \'c\', \'b\', \'d\']
            sage: a.automorphism_group()
            Permutation Group with generators [(2,3), (1,4)]

        ::

            sage: [a.transport(perm) for perm in a.automorphism_group()]
            [[\'a\', \'c\', \'b\', \'d\'],
             [\'a\', \'c\', \'b\', \'d\'],
             [\'a\', \'c\', \'b\', \'d\'],
             [\'a\', \'c\', \'b\', \'d\']]
        '''

class PermutationSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    @staticmethod
    @accept_size
    def __classcall__(cls, *args, **kwds):
        """
        EXAMPLES::

            sage: P = species.PermutationSpecies(); P
            Permutation species
        """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of permutations.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: P.generating_series()[0:5]
            [1, 1, 1, 1, 1]
            sage: P.isotype_generating_series()[0:5]
            [1, 1, 2, 3, 5]

            sage: P = species.PermutationSpecies()
            sage: c = P.generating_series()[0:3]
            sage: P._check()
            True
            sage: P == loads(dumps(P))
            True
        """
PermutationSpecies_class = PermutationSpecies
