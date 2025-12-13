from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.combinat.combinat import CombinatorialObject as CombinatorialObject
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent

class GenericSpeciesStructure(CombinatorialObject):
    def __init__(self, parent, labels, list) -> None:
        """
        This is a base class from which the classes for the structures inherit.

        EXAMPLES::

            sage: from sage.combinat.species.structure import GenericSpeciesStructure
            sage: a = GenericSpeciesStructure(None, [2,3,4], [1,2,3])
            sage: a
            [2, 3, 4]
            sage: a.parent() is None
            True
            sage: a == loads(dumps(a))
            True
        """
    def parent(self):
        """
        Return the species that this structure is associated with.

        EXAMPLES::

            sage: L = species.LinearOrderSpecies()
            sage: a,b = L.structures([1,2])
            sage: a.parent()
            Linear order species
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: T = species.BinaryTreeSpecies()
            sage: t = T.structures([1,2,3])[0]; t
            1*(2*3)
            sage: t[0], t[1][0]
            (1, 2)
            sage: t[0] == t[1][0]
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: T = species.BinaryTreeSpecies()
            sage: t = T.structures([1,2,3])[0]; t
            1*(2*3)
            sage: t[0], t[1][0]
            (1, 2)
            sage: t[0] != t[1][0]
            True
        """
    def labels(self):
        '''
        Return the labels used for this structure.

        .. NOTE::

            This includes labels which may not "appear" in this
            particular structure.

        EXAMPLES::

            sage: P = species.SubsetSpecies()
            sage: s = P.structures(["a", "b", "c"]).random_element()
            sage: s.labels()
            [\'a\', \'b\', \'c\']
        '''
    def change_labels(self, labels):
        '''
        Return a relabelled structure.

        INPUT:

        - ``labels`` -- list of labels

        OUTPUT:

        A structure with the `i`-th label of ``self`` replaced with the `i`-th
        label of the list.

        EXAMPLES::

            sage: P = species.SubsetSpecies()
            sage: S = P.structures(["a", "b", "c"])
            sage: [s.change_labels([1,2,3]) for s in S]
            [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
        '''
    def is_isomorphic(self, x):
        """
        EXAMPLES::

            sage: S = species.SetSpecies()
            sage: a = S.structures([1,2,3]).random_element(); a
            {1, 2, 3}
            sage: b = S.structures(['a','b','c']).random_element(); b
            {'a', 'b', 'c'}
            sage: a.is_isomorphic(b)
            True
        """
SpeciesStructure = GenericSpeciesStructure

class SpeciesStructureWrapper(GenericSpeciesStructure):
    def __init__(self, parent, s, **options) -> None:
        '''
        This is a class for the structures of species such as the sum
        species that do not provide "additional" structure.  For example,
        if you have the sum `C` of species `A` and `B`,
        then a structure of `C` will either be either something from `A` or `B`.
        Instead of just returning one of these directly, a "wrapper" is
        put around them so that they have their parent is `C` rather than `A` or
        `B`::

            sage: X = species.SingletonSpecies()
            sage: X2 = X+X
            sage: s = X2.structures([1]).random_element(); s
            1
            sage: s.parent()
            Sum of (Singleton species) and (Singleton species)
            sage: from sage.combinat.species.structure import SpeciesStructureWrapper
            sage: issubclass(type(s), SpeciesStructureWrapper)
            True

        EXAMPLES::

            sage: E = species.SetSpecies(); B = E+E
            sage: s = B.structures([1,2,3]).random_element()
            sage: s.parent()
            Sum of (Set species) and (Set species)
            sage: s == loads(dumps(s))
            True
        '''
    def __getattr__(self, attr):
        """
        EXAMPLES::

            sage: E = species.SetSpecies(); B = E+E
            sage: s = B.structures([1,2,3]).random_element()
            sage: s
            {1, 2, 3}
        """
    def transport(self, perm):
        """
        EXAMPLES::

            sage: P = species.PartitionSpecies()
            sage: s = (P+P).structures([1,2,3])[1]; s                                   # needs sage.libs.flint
            {{1, 3}, {2}}
            sage: s.transport(PermutationGroupElement((2,3)))                           # needs sage.groups sage.libs.flint
            {{1, 2}, {3}}
        """
    def canonical_label(self):
        """
        EXAMPLES::

            sage: P = species.PartitionSpecies()
            sage: s = (P+P).structures([1,2,3])[1]; s                                   # needs sage.libs.flint
            {{1, 3}, {2}}
            sage: s.canonical_label()                                                   # needs sage.libs.flint
            {{1, 2}, {3}}
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

            sage: X = species.SingletonSpecies()
            sage: X2 = X+X
            sage: s = X2.structures([1]).random_element(); s
            1
            sage: s.change_labels(['a'])
            'a'
        """

class SpeciesWrapper(Parent):
    def __init__(self, species, labels, iterator, generating_series, name, structure_class) -> None:
        '''
        This is a abstract base class for the set of structures of a
        species as well as the set of isotypes of the species.

        .. NOTE::

            One typically does not use :class:`SpeciesWrapper`
            directly, but instead instantiates one of its subclasses:
            :class:`StructuresWrapper` or :class:`IsotypesWrapper`.

        EXAMPLES::

            sage: from sage.combinat.species.structure import SpeciesWrapper
            sage: F = species.SetSpecies()
            sage: S = SpeciesWrapper(F, [1,2,3], "_structures", "generating_series", \'Structures\', None)
            sage: S
            Structures for Set species with labels [1, 2, 3]
            sage: S.list()
            [{1, 2, 3}]
            sage: S.cardinality()
            1
        '''
    def __eq__(self, other) -> bool:
        '''
        EXAMPLES::

            sage: from sage.combinat.species.structure import SpeciesWrapper
            sage: F = species.SetSpecies()
            sage: S = SpeciesWrapper(F, [1,2,3], "_structures", "generating_series", \'Structures\', None)
            sage: S == SpeciesWrapper(F, [1,2,3], "_structures", "generating_series", \'Structures\', None)
            True
        '''
    def __ne__(self, other) -> bool:
        '''
        EXAMPLES::

            sage: from sage.combinat.species.structure import SpeciesWrapper
            sage: F = species.SetSpecies()
            sage: S = SpeciesWrapper(F, [1,2,3], "_structures", "generating_series", \'Structures\', None)
            sage: S != SpeciesWrapper(F, [1,2,3], "_structures", "generating_series", \'Structures\', None)
            False
        '''
    def labels(self):
        """
        Return the labels used on these structures.  If `X` is the
        species, then :meth:`labels` returns the preimage of these
        structures under the functor `X`.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: F.structures([1,2,3]).labels()
            [1, 2, 3]
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: F.structures([1,2,3]).list()
            [{1, 2, 3}]
        """
    def cardinality(self):
        """
        Return the number of structures in this set.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: F.structures([1,2,3]).cardinality()
            1
        """

class StructuresWrapper(SpeciesWrapper):
    def __init__(self, species, labels, structure_class) -> None:
        """
        A base class for the set of structures of a species with given
        set of labels.  An object of this type is returned when you
        call the :meth:`structures` method of a species.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: S = F.structures([1,2,3])
            sage: S == loads(dumps(S))
            True
        """

class IsotypesWrapper(SpeciesWrapper):
    def __init__(self, species, labels, structure_class) -> None:
        """
        A base class for the set of isotypes of a species with given
        set of labels.  An object of this type is returned when you
        call the :meth:`isotypes` method of a species.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: S = F.isotypes([1,2,3])
            sage: S == loads(dumps(S))
            True
        """

class SimpleStructuresWrapper(SpeciesWrapper):
    def __init__(self, species, labels, structure_class) -> None:
        """
        .. warning::

            This is deprecated and currently not used for anything.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: S = F.structures([1,2,3])
            sage: S == loads(dumps(S))
            True
        """

class SimpleIsotypesWrapper(SpeciesWrapper):
    def __init__(self, species, labels, structure_class) -> None:
        """
        .. warning::

            This is deprecated and currently not used for anything.

        EXAMPLES::

            sage: F = species.SetSpecies()
            sage: S = F.structures([1,2,3])
            sage: S == loads(dumps(S))
            True
        """
