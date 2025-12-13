from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.combinat.species.misc import accept_size as accept_size
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LinearOrderSpeciesStructure(GenericSpeciesStructure):
    def canonical_label(self):
        '''
        EXAMPLES::

            sage: P = species.LinearOrderSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: s = P.structures(["a", "b", "c"]).random_element()
            sage: s.canonical_label()
            [\'a\', \'b\', \'c\']
        '''
    def transport(self, perm):
        '''
        Return the transport of this structure along the permutation
        perm.

        EXAMPLES::

            sage: F = species.LinearOrderSpecies()
            sage: a = F.structures(["a", "b", "c"])[0]; a
            [\'a\', \'b\', \'c\']
            sage: p = PermutationGroupElement((1,2))                                    # needs sage.groups
            sage: a.transport(p)                                                        # needs sage.groups
            [\'b\', \'a\', \'c\']
        '''
    def automorphism_group(self):
        '''
        Return the group of permutations whose action on this structure
        leave it fixed. For the species of linear orders, there is no
        non-trivial automorphism.

        EXAMPLES::

            sage: F = species.LinearOrderSpecies()
            sage: a = F.structures(["a", "b", "c"])[0]; a
            [\'a\', \'b\', \'c\']
            sage: a.automorphism_group()                                                # needs sage.groups
            Symmetric group of order 1! as a permutation group
        '''

class LinearOrderSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    @staticmethod
    @accept_size
    def __classcall__(cls, *args, **kwds):
        """
        EXAMPLES::

            sage: L = species.LinearOrderSpecies(); L
            Linear order species
        """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of linear orders.

        EXAMPLES::

            sage: L = species.LinearOrderSpecies()
            sage: L.generating_series()[0:5]
            [1, 1, 1, 1, 1]

            sage: L = species.LinearOrderSpecies()
            sage: L._check()
            True
            sage: L == loads(dumps(L))
            True
        """
LinearOrderSpecies_class = LinearOrderSpecies
