from .set_species import SetSpecies as SetSpecies
from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from .subset_species import SubsetSpeciesStructure as SubsetSpeciesStructure
from sage.arith.misc import factorial as factorial
from sage.combinat.species.misc import accept_size as accept_size

class PartitionSpeciesStructure(GenericSpeciesStructure):
    def __init__(self, parent, labels, list) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.species.partition_species import PartitionSpeciesStructure
            sage: P = species.PartitionSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: s = PartitionSpeciesStructure(P, ['a','b','c'], [[1,2],[3]]); s
            {{'a', 'b'}, {'c'}}
            sage: s == loads(dumps(s))
            True
        """
    def canonical_label(self):
        '''
        EXAMPLES::

            sage: P = species.PartitionSpecies()
            sage: S = P.structures(["a", "b", "c"])
            sage: [s.canonical_label() for s in S]
            [{{\'a\', \'b\', \'c\'}},
             {{\'a\', \'b\'}, {\'c\'}},
             {{\'a\', \'b\'}, {\'c\'}},
             {{\'a\', \'b\'}, {\'c\'}},
             {{\'a\'}, {\'b\'}, {\'c\'}}]
        '''
    def transport(self, perm):
        """
        Return the transport of this set partition along the permutation
        perm. For set partitions, this is the direct product of the
        automorphism groups for each of the blocks.

        EXAMPLES::

            sage: p = PermutationGroupElement((2,3))
            sage: from sage.combinat.species.partition_species import PartitionSpeciesStructure
            sage: a = PartitionSpeciesStructure(None, [2,3,4], [[1,2],[3]]); a
            {{2, 3}, {4}}
            sage: a.transport(p)
            {{2, 4}, {3}}
        """
    def automorphism_group(self):
        """
        Return the group of permutations whose action on this set
        partition leave it fixed.

        EXAMPLES::

            sage: p = PermutationGroupElement((2,3))
            sage: from sage.combinat.species.partition_species import PartitionSpeciesStructure
            sage: a = PartitionSpeciesStructure(None, [2,3,4], [[1,2],[3]]); a
            {{2, 3}, {4}}
            sage: a.automorphism_group()
            Permutation Group with generators [(1,2)]
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

            sage: p = PermutationGroupElement((2,3))
            sage: from sage.combinat.species.partition_species import PartitionSpeciesStructure
            sage: a = PartitionSpeciesStructure(None, [2,3,4], [[1,2],[3]]); a
            {{2, 3}, {4}}
            sage: a.change_labels([1,2,3])
            {{1, 2}, {3}}
        """

class PartitionSpecies(GenericCombinatorialSpecies):
    @staticmethod
    @accept_size
    def __classcall__(cls, *args, **kwds):
        """
        EXAMPLES::

            sage: P = species.PartitionSpecies(); P
            Partition species
        """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of partitions.

        EXAMPLES::

            sage: P = species.PartitionSpecies()
            sage: P.generating_series()[0:5]
            [1, 1, 1, 5/6, 5/8]
            sage: P.isotype_generating_series()[0:5]
            [1, 1, 2, 3, 5]

            sage: P = species.PartitionSpecies()
            sage: P._check()
            True
            sage: P == loads(dumps(P))
            True
        """
PartitionSpecies_class = PartitionSpecies
