from .set_species import SetSpecies as SetSpecies
from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from sage.arith.misc import factorial as factorial
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CharacteristicSpeciesStructure(GenericSpeciesStructure):
    def canonical_label(self):
        '''
        EXAMPLES::

            sage: F = species.CharacteristicSpecies(3)
            sage: a = F.structures(["a", "b", "c"]).random_element(); a
            {\'a\', \'b\', \'c\'}
            sage: a.canonical_label()
            {\'a\', \'b\', \'c\'}
        '''
    def transport(self, perm):
        '''
        Return the transport of this structure along the permutation ``perm``.

        EXAMPLES::

            sage: F = species.CharacteristicSpecies(3)
            sage: a = F.structures(["a", "b", "c"]).random_element(); a
            {\'a\', \'b\', \'c\'}
            sage: p = PermutationGroupElement((1,2))                                    # needs sage.groups
            sage: a.transport(p)                                                        # needs sage.groups
            {\'a\', \'b\', \'c\'}
        '''
    def automorphism_group(self):
        '''
        Return the group of permutations whose action on this structure
        leave it fixed. For the characteristic species, there is only one
        structure, so every permutation is in its automorphism group.

        EXAMPLES::

            sage: F = species.CharacteristicSpecies(3)
            sage: a = F.structures(["a", "b", "c"]).random_element(); a
            {\'a\', \'b\', \'c\'}
            sage: a.automorphism_group()                                                # needs sage.groups
            Symmetric group of order 3! as a permutation group
        '''

class CharacteristicSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    def __init__(self, n, min=None, max=None, weight=None) -> None:
        """
        Return the characteristic species of order `n`.

        This species has exactly one structure on a set of size `n`
        and no structures on sets of any other size.

        EXAMPLES::

            sage: X = species.CharacteristicSpecies(1)
            sage: X.structures([1]).list()
            [1]
            sage: X.structures([1,2]).list()
            []
            sage: X.generating_series()[0:4]
            [0, 1, 0, 0]
            sage: X.isotype_generating_series()[0:4]
            [0, 1, 0, 0]
            sage: X.cycle_index_series()[0:4]                                           # needs sage.modules
            [0, p[1], 0, 0]

            sage: F = species.CharacteristicSpecies(3)
            sage: c = F.generating_series()[0:4]
            sage: F._check()
            True
            sage: F == loads(dumps(F))
            True

        TESTS::

            sage: S1 = species.CharacteristicSpecies(1)
            sage: S2 = species.CharacteristicSpecies(1)
            sage: S3 = species.CharacteristicSpecies(2)
            sage: S4 = species.CharacteristicSpecies(2, weight=2)
            sage: S1 is S2
            True
            sage: S1 == S3
            False
        """
CharacteristicSpecies_class = CharacteristicSpecies

class EmptySetSpecies(CharacteristicSpecies):
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the empty set species.

        This species has exactly one structure on the empty set. It is
        the same (and is implemented) as ``CharacteristicSpecies(0)``.

        EXAMPLES::

            sage: X = species.EmptySetSpecies()
            sage: X.structures([]).list()
            [{}]
            sage: X.structures([1,2]).list()
            []
            sage: X.generating_series()[0:4]
            [1, 0, 0, 0]
            sage: X.isotype_generating_series()[0:4]
            [1, 0, 0, 0]
            sage: X.cycle_index_series()[0:4]                                           # needs sage.modules
            [p[], 0, 0, 0]

        TESTS::

            sage: E1 = species.EmptySetSpecies()
            sage: E2 = species.EmptySetSpecies()
            sage: E1 is E2
            True

            sage: E = species.EmptySetSpecies()
            sage: E._check()
            True
            sage: E == loads(dumps(E))
            True
        """
EmptySetSpecies_class = EmptySetSpecies

class SingletonSpecies(CharacteristicSpecies):
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Return the species of singletons.

        This species has exactly one structure on a set of size `1`. It
        is the same (and is implemented) as ``CharacteristicSpecies(1)``.

        EXAMPLES::

            sage: X = species.SingletonSpecies()
            sage: X.structures([1]).list()
            [1]
            sage: X.structures([1,2]).list()
            []
            sage: X.generating_series()[0:4]
            [0, 1, 0, 0]
            sage: X.isotype_generating_series()[0:4]
            [0, 1, 0, 0]
            sage: X.cycle_index_series()[0:4]                                           # needs sage.modules
            [0, p[1], 0, 0]

        TESTS::

            sage: S1 = species.SingletonSpecies()
            sage: S2 = species.SingletonSpecies()
            sage: S1 is S2
            True

            sage: S = species.SingletonSpecies()
            sage: S._check()
            True
            sage: S == loads(dumps(S))
            True
        """
SingletonSpecies_class = SingletonSpecies
