from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from .structure import GenericSpeciesStructure as GenericSpeciesStructure
from .subset_species import SubsetSpecies as SubsetSpecies
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ProductSpeciesStructure(GenericSpeciesStructure):
    def __init__(self, parent, labels, subset, left, right) -> None:
        """
        TESTS::

            sage: S = species.SetSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: F = S * S
            sage: a = F.structures(['a','b','c']).random_element()
            sage: a == loads(dumps(a))
            True
        """
    def transport(self, perm):
        """
        EXAMPLES::

            sage: # needs sage.groups
            sage: p = PermutationGroupElement((2,3))
            sage: S = species.SetSpecies()
            sage: F = S * S
            sage: a = F.structures(['a','b','c'])[4]; a
            {'a', 'b'}*{'c'}
            sage: a.transport(p)
            {'a', 'c'}*{'b'}
        """
    def canonical_label(self):
        """
        EXAMPLES::

            sage: S = species.SetSpecies()
            sage: F = S * S
            sage: S = F.structures(['a','b','c']).list(); S
            [{}*{'a', 'b', 'c'},
             {'a'}*{'b', 'c'},
             {'b'}*{'a', 'c'},
             {'c'}*{'a', 'b'},
             {'a', 'b'}*{'c'},
             {'a', 'c'}*{'b'},
             {'b', 'c'}*{'a'},
             {'a', 'b', 'c'}*{}]

        ::

            sage: F.isotypes(['a','b','c']).cardinality()
            4
            sage: [s.canonical_label() for s in S]
            [{}*{'a', 'b', 'c'},
             {'a'}*{'b', 'c'},
             {'a'}*{'b', 'c'},
             {'a'}*{'b', 'c'},
             {'a', 'b'}*{'c'},
             {'a', 'b'}*{'c'},
             {'a', 'b'}*{'c'},
             {'a', 'b', 'c'}*{}]
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

            sage: S = species.SetSpecies()
            sage: F = S * S
            sage: a = F.structures(['a','b','c'])[0]; a
            {}*{'a', 'b', 'c'}
            sage: a.change_labels([1,2,3])
            {}*{1, 2, 3}
        """
    def automorphism_group(self):
        """
        EXAMPLES::

            sage: # needs sage.groups
            sage: p = PermutationGroupElement((2,3))
            sage: S = species.SetSpecies()
            sage: F = S * S
            sage: a = F.structures([1,2,3,4])[1]; a
            {1}*{2, 3, 4}
            sage: a.automorphism_group()
            Permutation Group with generators [(2,3), (2,3,4)]

        ::

            sage: [a.transport(g) for g in a.automorphism_group()]                      # needs sage.groups
            [{1}*{2, 3, 4},
             {1}*{2, 3, 4},
             {1}*{2, 3, 4},
             {1}*{2, 3, 4},
             {1}*{2, 3, 4},
             {1}*{2, 3, 4}]

        ::

            sage: a = F.structures([1,2,3,4])[8]; a                                     # needs sage.groups
            {2, 3}*{1, 4}
            sage: [a.transport(g) for g in a.automorphism_group()]                      # needs sage.groups
            [{2, 3}*{1, 4}, {2, 3}*{1, 4}, {2, 3}*{1, 4}, {2, 3}*{1, 4}]
        """

class ProductSpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    def __init__(self, F, G, min=None, max=None, weight=None) -> None:
        """
        EXAMPLES::

            sage: X = species.SingletonSpecies()
            sage: A = X*X
            sage: A.generating_series()[0:4]
            [0, 0, 1, 0]

            sage: P = species.PermutationSpecies()
            sage: F = P * P; F
            Product of (Permutation species) and (Permutation species)
            sage: F == loads(dumps(F))
            True
            sage: F._check()                                                            # needs sage.libs.flint
            True

        TESTS::

            sage: X = species.SingletonSpecies()
            sage: X*X is X*X
            True
        """
    def left_factor(self):
        """
        Return the left factor of this product.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: X = species.SingletonSpecies()
            sage: F = P*X
            sage: F.left_factor()
            Permutation species
        """
    def right_factor(self):
        """
        Return the right factor of this product.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: X = species.SingletonSpecies()
            sage: F = P*X
            sage: F.right_factor()
            Singleton species
        """
    def weight_ring(self):
        """
        Return the weight ring for this species. This is determined by
        asking Sage's coercion model what the result is when you multiply
        (and add) elements of the weight rings for each of the operands.

        EXAMPLES::

            sage: S = species.SetSpecies()
            sage: C = S*S
            sage: C.weight_ring()
            Rational Field

        ::

            sage: S = species.SetSpecies(weight=QQ['t'].gen())
            sage: C = S*S
            sage: C.weight_ring()
            Univariate Polynomial Ring in t over Rational Field

        ::

            sage: S = species.SetSpecies()
            sage: C = (S*S).weighted(QQ['t'].gen())
            sage: C.weight_ring()
            Univariate Polynomial Ring in t over Rational Field
        """
ProductSpecies_class = ProductSpecies
