from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.category import Category as Category
from sage.categories.complex_reflection_groups import ComplexReflectionGroups as ComplexReflectionGroups
from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.categories.permutation_groups import PermutationGroups as PermutationGroups
from sage.combinat.root_system.cartan_matrix import CartanMatrix as CartanMatrix
from sage.combinat.root_system.reflection_group_element import ComplexReflectionGroupElement as ComplexReflectionGroupElement
from sage.groups.perm_gps.permgroup import PermutationGroup_generic as PermutationGroup_generic
from sage.interfaces.gap3 import gap3 as gap3
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import identity_matrix as identity_matrix
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family
from sage.structure.element import Matrix as Matrix
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ComplexReflectionGroup(UniqueRepresentation, PermutationGroup_generic):
    """
    A complex reflection group given as a permutation group.

    .. SEEALSO::

        :func:`ReflectionGroup`
    """
    def __init__(self, W_types, index_set=None, hyperplane_index_set=None, reflection_index_set=None) -> None:
        """
        TESTS::

            sage: from sage.categories.complex_reflection_groups import ComplexReflectionGroups
            sage: W = ComplexReflectionGroups().example()
            sage: TestSuite(W).run()
        """
    def iteration_tracking_words(self) -> Generator[Incomplete]:
        """
        Return an iterator going through all elements in ``self`` that
        tracks the reduced expressions.

        This can be much slower than using the iteration as a permutation
        group with strong generating set.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: for w in W.iteration_tracking_words(): w
            ()
            (1,4)(2,3)(5,6)
            (1,3)(2,5)(4,6)
            (1,6,2)(3,5,4)
            (1,2,6)(3,4,5)
            (1,5)(2,4)(3,6)
        """
    @cached_method
    def index_set(self):
        """
        Return the index set of the simple reflections of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,4))
            sage: W.index_set()
            (1, 2, 3)
            sage: W = ReflectionGroup((1,1,4), index_set=[1,3,'asdf'])
            sage: W.index_set()
            (1, 3, 'asdf')
            sage: W = ReflectionGroup((1,1,4), index_set=('a', 'b', 'c'))
            sage: W.index_set()
            ('a', 'b', 'c')
        """
    def simple_reflection(self, i):
        """
        Return the ``i``-th simple reflection of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.simple_reflection(1)
            (1,4)(2,3)(5,6)
            sage: W.simple_reflections()
            Finite family {1: (1,4)(2,3)(5,6), 2: (1,3)(2,5)(4,6)}
        """
    def series(self):
        '''
        Return the series of the classification type to which ``self``
        belongs.

        For real reflection groups, these are the Cartan-Killing
        classification types "A","B","C","D","E","F","G","H","I", and
        for complx non-real reflection groups these are the
        Shephard-Todd classification type "ST".

        EXAMPLES::

            sage: ReflectionGroup((1,1,3)).series()
            [\'A\']
            sage: ReflectionGroup((3,1,3)).series()
            [\'ST\']
        '''
    @cached_method
    def hyperplane_index_set(self):
        """
        Return the index set of the hyperplanes of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,4))
            sage: W.hyperplane_index_set()
            (1, 2, 3, 4, 5, 6)
            sage: W = ReflectionGroup((1,1,4), hyperplane_index_set=[1,3,'asdf',7,9,11])
            sage: W.hyperplane_index_set()
            (1, 3, 'asdf', 7, 9, 11)
            sage: W = ReflectionGroup((1,1,4),hyperplane_index_set=('a','b','c','d','e','f'))
            sage: W.hyperplane_index_set()
            ('a', 'b', 'c', 'd', 'e', 'f')
        """
    @cached_method
    def distinguished_reflections(self):
        """
        Return a finite family containing the distinguished reflections
        of ``self`` indexed by :meth:`hyperplane_index_set`.

        These are the reflections in ``self`` acting on the complement
        of the fixed hyperplane `H` as `\\operatorname{exp}(2 \\pi i / n)`,
        where `n` is the order of the reflection subgroup fixing `H`.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.distinguished_reflections()
            Finite family {1: (1,4)(2,3)(5,6), 2: (1,3)(2,5)(4,6), 3: (1,5)(2,4)(3,6)}

            sage: W = ReflectionGroup((1,1,3),hyperplane_index_set=['a','b','c'])
            sage: W.distinguished_reflections()
            Finite family {'a': (1,4)(2,3)(5,6), 'b': (1,3)(2,5)(4,6), 'c': (1,5)(2,4)(3,6)}

            sage: W = ReflectionGroup((3,1,1))
            sage: W.distinguished_reflections()
            Finite family {1: (1,2,3)}

            sage: W = ReflectionGroup((1,1,3),(3,1,2))
            sage: W.distinguished_reflections()
            Finite family {1: (1,6)(2,5)(7,8), 2: (1,5)(2,7)(6,8),
             3: (3,9,15)(4,10,16)(12,17,23)(14,18,24)(20,25,29)(21,22,26)(27,28,30),
             4: (3,11)(4,12)(9,13)(10,14)(15,19)(16,20)(17,21)(18,22)(23,27)(24,28)(25,26)(29,30),
             5: (1,7)(2,6)(5,8),
             6: (3,19)(4,25)(9,11)(10,17)(12,28)(13,15)(14,30)(16,18)(20,27)(21,29)(22,23)(24,26),
             7: (4,21,27)(10,22,28)(11,13,19)(12,14,20)(16,26,30)(17,18,25)(23,24,29),
             8: (3,13)(4,24)(9,19)(10,29)(11,15)(12,26)(14,21)(16,23)(17,30)(18,27)(20,22)(25,28)}
        """
    def distinguished_reflection(self, i):
        """
        Return the ``i``-th distinguished reflection of ``self``.

        These are the reflections in ``self`` acting on the complement
        of the fixed hyperplane `H` as `\\operatorname{exp}(2 \\pi i / n)`,
        where `n` is the order of the reflection subgroup fixing `H`.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.distinguished_reflection(1)
            (1,4)(2,3)(5,6)
            sage: W.distinguished_reflection(2)
            (1,3)(2,5)(4,6)
            sage: W.distinguished_reflection(3)
            (1,5)(2,4)(3,6)

            sage: W = ReflectionGroup((3,1,1),hyperplane_index_set=['a'])
            sage: W.distinguished_reflection('a')
            (1,2,3)

            sage: W = ReflectionGroup((1,1,3),(3,1,2))
            sage: for i in range(W.number_of_reflection_hyperplanes()):
            ....:     W.distinguished_reflection(i+1)
            (1,6)(2,5)(7,8)
            (1,5)(2,7)(6,8)
            (3,9,15)(4,10,16)(12,17,23)(14,18,24)(20,25,29)(21,22,26)(27,28,30)
            (3,11)(4,12)(9,13)(10,14)(15,19)(16,20)(17,21)(18,22)(23,27)(24,28)(25,26)(29,30)
            (1,7)(2,6)(5,8)
            (3,19)(4,25)(9,11)(10,17)(12,28)(13,15)(14,30)(16,18)(20,27)(21,29)(22,23)(24,26)
            (4,21,27)(10,22,28)(11,13,19)(12,14,20)(16,26,30)(17,18,25)(23,24,29)
            (3,13)(4,24)(9,19)(10,29)(11,15)(12,26)(14,21)(16,23)(17,30)(18,27)(20,22)(25,28)
        """
    @cached_method
    def reflection_hyperplanes(self, as_linear_functionals: bool = False, with_order: bool = False):
        """
        Return the list of all reflection hyperplanes of ``self``,
        either as a codimension 1 space, or as its linear functional.

        INPUT:

        - ``as_linear_functionals`` -- boolean (default: ``False``); whether
          to return the hyperplane or its linear functional in the basis
          dual to the given root basis

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: for H in W.reflection_hyperplanes(): H
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 2]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [  1 1/2]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [ 1 -1]

            sage: for H in W.reflection_hyperplanes(as_linear_functionals=True): H
            (1, -1/2)
            (1, -2)
            (1, 1)


            sage: W = ReflectionGroup((2,1,2))
            sage: for H in W.reflection_hyperplanes(): H
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [  1 1/2]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]

            sage: for H in W.reflection_hyperplanes(as_linear_functionals=True): H
            (1, -1)
            (1, -2)
            (0, 1)
            (1, 0)

            sage: for H in W.reflection_hyperplanes(as_linear_functionals=True, with_order=True): H
            ((1, -1), 2)
            ((1, -2), 2)
            ((0, 1), 2)
            ((1, 0), 2)
        """
    def reflection_hyperplane(self, i, as_linear_functional: bool = False, with_order: bool = False):
        """
        Return the ``i``-th reflection hyperplane of ``self``.

        The ``i``-th reflection hyperplane corresponds to the ``i``
        distinguished reflection.

        INPUT:

        - ``i`` -- an index in the index set
        - ``as_linear_functionals`` -- boolean (default: ``False``); whether
          to return the hyperplane or its linear functional in the basis
          dual to the given root basis

        EXAMPLES::

            sage: W = ReflectionGroup((2,1,2))
            sage: W.reflection_hyperplane(3)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]

        One can ask for the result as a linear form::

            sage: W.reflection_hyperplane(3, True)
            (0, 1)
        """
    @cached_method
    def reflection_index_set(self):
        """
        Return the index set of the reflections of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,4))
            sage: W.reflection_index_set()
            (1, 2, 3, 4, 5, 6)
            sage: W = ReflectionGroup((1,1,4), reflection_index_set=[1,3,'asdf',7,9,11])
            sage: W.reflection_index_set()
            (1, 3, 'asdf', 7, 9, 11)
            sage: W = ReflectionGroup((1,1,4), reflection_index_set=('a','b','c','d','e','f'))
            sage: W.reflection_index_set()
            ('a', 'b', 'c', 'd', 'e', 'f')
        """
    @cached_method
    def reflections(self):
        """
        Return a finite family containing the reflections of ``self``,
        indexed by :meth:`self.reflection_index_set`.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.reflections()
            Finite family {1: (1,4)(2,3)(5,6), 2: (1,3)(2,5)(4,6), 3: (1,5)(2,4)(3,6)}

            sage: W = ReflectionGroup((1,1,3),reflection_index_set=['a','b','c'])
            sage: W.reflections()
            Finite family {'a': (1,4)(2,3)(5,6), 'b': (1,3)(2,5)(4,6), 'c': (1,5)(2,4)(3,6)}

            sage: W = ReflectionGroup((3,1,1))
            sage: W.reflections()
            Finite family {1: (1,2,3), 2: (1,3,2)}

            sage: W = ReflectionGroup((1,1,3),(3,1,2))
            sage: W.reflections()
            Finite family {1: (1,6)(2,5)(7,8), 2: (1,5)(2,7)(6,8),
                           3: (3,9,15)(4,10,16)(12,17,23)(14,18,24)(20,25,29)(21,22,26)(27,28,30),
                           4: (3,11)(4,12)(9,13)(10,14)(15,19)(16,20)(17,21)(18,22)(23,27)(24,28)(25,26)(29,30),
                           5: (1,7)(2,6)(5,8),
                           6: (3,19)(4,25)(9,11)(10,17)(12,28)(13,15)(14,30)(16,18)(20,27)(21,29)(22,23)(24,26),
                           7: (4,21,27)(10,22,28)(11,13,19)(12,14,20)(16,26,30)(17,18,25)(23,24,29),
                           8: (3,13)(4,24)(9,19)(10,29)(11,15)(12,26)(14,21)(16,23)(17,30)(18,27)(20,22)(25,28),
                           9: (3,15,9)(4,16,10)(12,23,17)(14,24,18)(20,29,25)(21,26,22)(27,30,28),
                           10: (4,27,21)(10,28,22)(11,19,13)(12,20,14)(16,30,26)(17,25,18)(23,29,24)}
        """
    def reflection(self, i):
        """
        Return the ``i``-th reflection of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.reflection(1)
            (1,4)(2,3)(5,6)
            sage: W.reflection(2)
            (1,3)(2,5)(4,6)
            sage: W.reflection(3)
            (1,5)(2,4)(3,6)

            sage: W = ReflectionGroup((3,1,1),reflection_index_set=['a','b'])
            sage: W.reflection('a')
            (1,2,3)
            sage: W.reflection('b')
            (1,3,2)
        """
    def reflection_character(self):
        """
        Return the reflection characters of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.reflection_character()
            [2, 0, -1]
        """
    @cached_method
    def discriminant(self):
        """
        Return the discriminant of ``self`` in the polynomial ring on
        which the group acts.

        This is the product

        .. MATH::

           \\prod_H \\alpha_H^{e_H},

        where `\\alpha_H` is the linear form of the hyperplane `H` and
        `e_H` is its stabilizer order.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: W.discriminant()
            x0^6 - 3*x0^5*x1 - 3/4*x0^4*x1^2 + 13/2*x0^3*x1^3
             - 3/4*x0^2*x1^4 - 3*x0*x1^5 + x1^6

            sage: W = ReflectionGroup(['B',2])
            sage: W.discriminant()
            x0^6*x1^2 - 6*x0^5*x1^3 + 13*x0^4*x1^4 - 12*x0^3*x1^5 + 4*x0^2*x1^6
        """
    @cached_method
    def discriminant_in_invariant_ring(self, invariants=None):
        """
        Return the discriminant of ``self`` in the invariant ring.

        This is the function `f` in the invariants such that
        `f(F_1(x), \\ldots, F_n(x))` is the discriminant.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3])
            sage: W.discriminant_in_invariant_ring()
            6*t0^3*t1^2 - 18*t0^4*t2 + 9*t1^4 - 36*t0*t1^2*t2 + 24*t0^2*t2^2 - 8*t2^3

            sage: W = ReflectionGroup(['B',3])
            sage: W.discriminant_in_invariant_ring()
            -t0^2*t1^2*t2 + 16*t0^3*t2^2 + 2*t1^3*t2 - 36*t0*t1*t2^2 + 108*t2^3

            sage: W = ReflectionGroup(['H',3])
            sage: W.discriminant_in_invariant_ring()    # long time
            (-829*E(5) - 1658*E(5)^2 - 1658*E(5)^3 - 829*E(5)^4)*t0^15
             + (213700*E(5) + 427400*E(5)^2 + 427400*E(5)^3 + 213700*E(5)^4)*t0^12*t1
             + (-22233750*E(5) - 44467500*E(5)^2 - 44467500*E(5)^3 - 22233750*E(5)^4)*t0^9*t1^2
             + (438750*E(5) + 877500*E(5)^2 + 877500*E(5)^3 + 438750*E(5)^4)*t0^10*t2
             + (1162187500*E(5) + 2324375000*E(5)^2 + 2324375000*E(5)^3 + 1162187500*E(5)^4)*t0^6*t1^3
             + (-74250000*E(5) - 148500000*E(5)^2 - 148500000*E(5)^3 - 74250000*E(5)^4)*t0^7*t1*t2
             + (-28369140625*E(5) - 56738281250*E(5)^2 - 56738281250*E(5)^3 - 28369140625*E(5)^4)*t0^3*t1^4
             + (1371093750*E(5) + 2742187500*E(5)^2 + 2742187500*E(5)^3 + 1371093750*E(5)^4)*t0^4*t1^2*t2
             + (1191796875*E(5) + 2383593750*E(5)^2 + 2383593750*E(5)^3 + 1191796875*E(5)^4)*t0^5*t2^2
             + (175781250000*E(5) + 351562500000*E(5)^2 + 351562500000*E(5)^3 + 175781250000*E(5)^4)*t1^5
             + (131835937500*E(5) + 263671875000*E(5)^2 + 263671875000*E(5)^3 + 131835937500*E(5)^4)*t0*t1^3*t2
             + (-100195312500*E(5) - 200390625000*E(5)^2 - 200390625000*E(5)^3 - 100195312500*E(5)^4)*t0^2*t1*t2^2
             + (395507812500*E(5) + 791015625000*E(5)^2 + 791015625000*E(5)^3 + 395507812500*E(5)^4)*t2^3
        """
    @cached_method
    def is_crystallographic(self):
        """
        Return ``True`` if ``self`` is crystallographic.

        This is, if the field of definition is the rational field.

        .. TODO::

            Make this more robust and do not use the matrix
            representation of the simple reflections.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3)); W
            Irreducible real reflection group of rank 2 and type A2
            sage: W.is_crystallographic()
            True

            sage: W = ReflectionGroup((2,1,3)); W
            Irreducible real reflection group of rank 3 and type B3
            sage: W.is_crystallographic()
            True

            sage: W = ReflectionGroup(23); W
            Irreducible real reflection group of rank 3 and type H3
            sage: W.is_crystallographic()
            False

            sage: W = ReflectionGroup((3,1,3)); W
            Irreducible complex reflection group of rank 3 and type G(3,1,3)
            sage: W.is_crystallographic()
            False

            sage: W = ReflectionGroup((4,2,2)); W
            Irreducible complex reflection group of rank 2 and type G(4,2,2)
            sage: W.is_crystallographic()
            False
        """
    def number_of_irreducible_components(self):
        """
        Return the number of irreducible components of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.number_of_irreducible_components()
            1

            sage: W = ReflectionGroup((1,1,3),(2,1,3))
            sage: W.number_of_irreducible_components()
            2
        """
    def irreducible_components(self):
        """
        Return a list containing the irreducible components of ``self``
        as finite reflection groups.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.irreducible_components()
            [Irreducible real reflection group of rank 2 and type A2]

            sage: W = ReflectionGroup((1,1,3),(2,1,3))
            sage: W.irreducible_components()
            [Irreducible real reflection group of rank 2 and type A2,
            Irreducible real reflection group of rank 3 and type B3]
        """
    @cached_method
    def conjugacy_classes_representatives(self):
        """
        Return the shortest representatives of the conjugacy classes of
        ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: [w.reduced_word() for w in W.conjugacy_classes_representatives()]
            [[], [1], [1, 2]]

            sage: W = ReflectionGroup((1,1,4))
            sage: [w.reduced_word() for w in W.conjugacy_classes_representatives()]
            [[], [1], [1, 3], [1, 2], [1, 3, 2]]

            sage: W = ReflectionGroup((3,1,2))
            sage: [w.reduced_word() for w in W.conjugacy_classes_representatives()]
            [[], [1], [1, 1], [2, 1, 2, 1], [2, 1, 2, 1, 1],
             [2, 1, 1, 2, 1, 1], [2], [1, 2], [1, 1, 2]]

            sage: W = ReflectionGroup(23)
            sage: [w.reduced_word() for w in W.conjugacy_classes_representatives()]
                [[],
                 [1],
                 [1, 2],
                 [1, 3],
                 [2, 3],
                 [1, 2, 3],
                 [1, 2, 1, 2],
                 [1, 2, 1, 2, 3],
                 [1, 2, 1, 2, 3, 2, 1, 2, 3],
                 [1, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3]]
        """
    def conjugacy_classes(self):
        """
        Return the conjugacy classes of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: for C in W.conjugacy_classes(): sorted(C)
            [()]
            [(1,3)(2,5)(4,6), (1,4)(2,3)(5,6), (1,5)(2,4)(3,6)]
            [(1,2,6)(3,4,5), (1,6,2)(3,5,4)]

            sage: W = ReflectionGroup((1,1,4))
            sage: sum(len(C) for C in W.conjugacy_classes()) == W.cardinality()
            True

            sage: W = ReflectionGroup((3,1,2))
            sage: sum(len(C) for C in W.conjugacy_classes()) == W.cardinality()
            True

            sage: W = ReflectionGroup(23)
            sage: sum(len(C) for C in W.conjugacy_classes()) == W.cardinality()
            True
        """
    def rank(self):
        """
        Return the rank of ``self``.

        This is the dimension of the underlying vector space.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.rank()
            2
            sage: W = ReflectionGroup((2,1,3))
            sage: W.rank()
            3
            sage: W = ReflectionGroup((4,1,3))
            sage: W.rank()
            3
            sage: W = ReflectionGroup((4,2,3))
            sage: W.rank()
            3
        """
    @cached_method
    def degrees(self):
        """
        Return the degrees of ``self`` ordered within each irreducible
        component of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,4))
            sage: W.degrees()
            (2, 3, 4)

            sage: W = ReflectionGroup((2,1,4))
            sage: W.degrees()
            (2, 4, 6, 8)

            sage: W = ReflectionGroup((4,1,4))
            sage: W.degrees()
            (4, 8, 12, 16)

            sage: W = ReflectionGroup((4,2,4))
            sage: W.degrees()
            (4, 8, 8, 12)

            sage: W = ReflectionGroup((4,4,4))
            sage: W.degrees()
            (4, 4, 8, 12)

        Examples of reducible types::

            sage: W = ReflectionGroup((1,1,4), (3,1,2)); W
            Reducible complex reflection group of rank 5 and type A3 x G(3,1,2)
            sage: W.degrees()
            (2, 3, 4, 3, 6)

            sage: W = ReflectionGroup((1,1,4), (6,1,12), 23)
            sage: W.degrees()
            (2, 3, 4, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 2, 6, 10)
        """
    @cached_method
    def codegrees(self):
        """
        Return the codegrees of ``self`` ordered within each irreducible
        component of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,4))
            sage: W.codegrees()
            (2, 1, 0)

            sage: W = ReflectionGroup((2,1,4))
            sage: W.codegrees()
            (6, 4, 2, 0)

            sage: W = ReflectionGroup((4,1,4))
            sage: W.codegrees()
            (12, 8, 4, 0)

            sage: W = ReflectionGroup((4,2,4))
            sage: W.codegrees()
            (12, 8, 4, 0)

            sage: W = ReflectionGroup((4,4,4))
            sage: W.codegrees()
            (8, 8, 4, 0)

            sage: W = ReflectionGroup((1,1,4), (3,1,2))
            sage: W.codegrees()
            (2, 1, 0, 3, 0)

            sage: W = ReflectionGroup((1,1,4), (6,1,12), 23)
            sage: W.codegrees()
            (2, 1, 0, 66, 60, 54, 48, 42, 36, 30, 24, 18, 12, 6, 0, 8, 4, 0)
        """
    @cached_method
    def reflection_eigenvalues_family(self):
        """
        Return the reflection eigenvalues of ``self`` as a finite family
        indexed by the class representatives of ``self``.

        OUTPUT: list with entries `k/n` representing the eigenvalue `\\zeta_n^k`

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.reflection_eigenvalues_family()
            Finite family {(): [0, 0], (1,4)(2,3)(5,6): [1/2, 0], (1,6,2)(3,5,4): [1/3, 2/3]}

            sage: W = ReflectionGroup((3,1,2))
            sage: reflection_eigenvalues = W.reflection_eigenvalues_family()
            sage: for elt in sorted(reflection_eigenvalues.keys()):
            ....:     print('%s %s'%(elt, reflection_eigenvalues[elt]))
            () [0, 0]
            (1,3,9)(2,4,10)(6,11,17)(8,12,18)(14,19,23)(15,16,20)(21,22,24) [1/3, 0]
            (1,3,9)(2,16,24)(4,20,21)(5,7,13)(6,12,23)(8,19,17)(10,15,22)(11,18,14) [1/3, 1/3]
            (1,5)(2,6)(3,7)(4,8)(9,13)(10,14)(11,15)(12,16)(17,21)(18,22)(19,20)(23,24) [1/2, 0]
            (1,7,3,13,9,5)(2,8,16,19,24,17)(4,14,20,11,21,18)(6,15,12,22,23,10) [1/6, 2/3]
            (1,9,3)(2,10,4)(6,17,11)(8,18,12)(14,23,19)(15,20,16)(21,24,22) [2/3, 0]
            (1,9,3)(2,20,22)(4,15,24)(5,7,13)(6,18,19)(8,23,11)(10,16,21)(12,14,17) [1/3, 2/3]
            (1,9,3)(2,24,16)(4,21,20)(5,13,7)(6,23,12)(8,17,19)(10,22,15)(11,14,18) [2/3, 2/3]
            (1,13,9,7,3,5)(2,14,24,18,16,11)(4,6,21,23,20,12)(8,22,17,15,19,10) [1/3, 5/6]

            sage: W = ReflectionGroup(23)
            sage: reflection_eigenvalues = W.reflection_eigenvalues_family()
            sage: for elt in sorted(reflection_eigenvalues.keys()):
            ....:     print('%s %s'%(elt, reflection_eigenvalues[elt]))
            () [0, 0, 0]
            (1,8,4)(2,21,3)(5,10,11)(6,18,17)(7,9,12)(13,14,15)(16,23,19)(20,25,26)(22,24,27)(28,29,30) [1/3, 2/3, 0]
            (1,16)(2,5)(4,7)(6,9)(8,10)(11,13)(12,14)(17,20)(19,22)(21,24)(23,25)(26,28)(27,29) [1/2, 0, 0]
            (1,16)(2,9)(3,18)(4,10)(5,6)(7,8)(11,14)(12,13)(17,24)(19,25)(20,21)(22,23)(26,29)(27,28) [1/2, 1/2, 0]
            (1,16)(2,17)(3,18)(4,19)(5,20)(6,21)(7,22)(8,23)(9,24)(10,25)(11,26)(12,27)(13,28)(14,29)(15,30) [1/2, 1/2, 1/2]
            (1,19,20,2,7)(3,6,11,13,9)(4,5,17,22,16)(8,12,15,14,10)(18,21,26,28,24)(23,27,30,29,25) [1/5, 4/5, 0]
            (1,20,7,19,2)(3,11,9,6,13)(4,17,16,5,22)(8,15,10,12,14)(18,26,24,21,28)(23,30,25,27,29) [2/5, 3/5, 0]
            (1,23,26,29,22,16,8,11,14,7)(2,10,4,9,18,17,25,19,24,3)(5,21,27,30,28,20,6,12,15,13) [1/10, 1/2, 9/10]
            (1,24,17,16,9,2)(3,12,13,18,27,28)(4,21,29,19,6,14)(5,25,26,20,10,11)(7,23,30,22,8,15) [1/6, 1/2, 5/6]
            (1,29,8,7,26,16,14,23,22,11)(2,9,25,3,4,17,24,10,18,19)(5,30,6,13,27,20,15,21,28,12) [3/10, 1/2, 7/10]
        """
    @cached_method
    def reflection_eigenvalues(self, w, is_class_representative: bool = False):
        """
        Return the reflection eigenvalue of ``w`` in ``self``.

        INPUT:

        - ``is_class_representative`` -- boolean (default: ``True``) whether to
          compute instead on the conjugacy class representative

        .. SEEALSO:: :meth:`reflection_eigenvalues_family`

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: for w in W:
            ....:     print('%s %s'%(w.reduced_word(), W.reflection_eigenvalues(w)))
            [] [0, 0]
            [2] [1/2, 0]
            [1] [1/2, 0]
            [1, 2] [1/3, 2/3]
            [2, 1] [1/3, 2/3]
            [1, 2, 1] [1/2, 0]
        """
    @cached_method
    def simple_roots(self):
        """
        Return the simple roots of ``self``.

        These are the roots corresponding to the simple reflections.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.simple_roots()
            Finite family {1: (1, 0), 2: (0, 1)}

            sage: W = ReflectionGroup((1,1,4), (2,1,2))
            sage: W.simple_roots()
            Finite family {1: (1, 0, 0, 0, 0), 2: (0, 1, 0, 0, 0), 3: (0, 0, 1, 0, 0), 4: (0, 0, 0, 1, 0), 5: (0, 0, 0, 0, 1)}

            sage: W = ReflectionGroup((3,1,2))
            sage: W.simple_roots()
            Finite family {1: (1, 0), 2: (-1, 1)}

            sage: W = ReflectionGroup((1,1,4), (3,1,2))
            sage: W.simple_roots()
            Finite family {1: (1, 0, 0, 0, 0), 2: (0, 1, 0, 0, 0), 3: (0, 0, 1, 0, 0), 4: (0, 0, 0, 1, 0), 5: (0, 0, 0, -1, 1)}
        """
    def simple_root(self, i):
        """
        Return the simple root with index ``i``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3])
            sage: W.simple_root(1)
            (1, 0, 0)
            sage: W.simple_root(2)
            (0, 1, 0)
            sage: W.simple_root(3)
            (0, 0, 1)

        TESTS::

            sage: W.simple_root(0)
            Traceback (most recent call last):
            ...
            KeyError: 0
        """
    @cached_method
    def simple_coroots(self):
        """
        Return the simple coroots of ``self``.

        These are the coroots corresponding to the simple reflections.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.simple_coroots()
            Finite family {1: (2, -1), 2: (-1, 2)}

            sage: W = ReflectionGroup((1,1,4), (2,1,2))
            sage: W.simple_coroots()
            Finite family {1: (2, -1, 0, 0, 0), 2: (-1, 2, -1, 0, 0), 3: (0, -1, 2, 0, 0), 4: (0, 0, 0, 2, -2), 5: (0, 0, 0, -1, 2)}

            sage: W = ReflectionGroup((3,1,2))
            sage: W.simple_coroots()
            Finite family {1: (-2*E(3) - E(3)^2, 0), 2: (-1, 1)}

            sage: W = ReflectionGroup((1,1,4), (3,1,2))
            sage: W.simple_coroots()
            Finite family {1: (2, -1, 0, 0, 0), 2: (-1, 2, -1, 0, 0), 3: (0, -1, 2, 0, 0), 4: (0, 0, 0, -2*E(3) - E(3)^2, 0), 5: (0, 0, 0, -1, 1)}
        """
    def simple_coroot(self, i):
        """
        Return the simple root with index ``i``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3])
            sage: W.simple_coroot(1)
            (2, -1, 0)
        """
    @cached_method
    def independent_roots(self):
        """
        Return a collection of simple roots generating the underlying
        vector space of ``self``.

        For well-generated groups, these are all simple roots.
        Otherwise, a linearly independent subset of the simple roots is
        chosen.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.independent_roots()
            Finite family {1: (1, 0), 2: (0, 1)}

            sage: W = ReflectionGroup((4,2,3))
            sage: W.simple_roots()
            Finite family {1: (1, 0, 0), 2: (-E(4), 1, 0), 3: (-1, 1, 0), 4: (0, -1, 1)}
            sage: W.independent_roots()
            Finite family {1: (1, 0, 0), 2: (-E(4), 1, 0), 4: (0, -1, 1)}
        """
    @cached_method
    def roots(self):
        """
        Return all roots corresponding to all reflections of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.roots()
            [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1)]

            sage: W = ReflectionGroup((3,1,2))
            sage: W.roots()
            [(1, 0), (-1, 1), (E(3), 0), (-E(3), 1), (0, 1), (1, -1),
             (0, E(3)), (1, -E(3)), (E(3)^2, 0), (-E(3)^2, 1),
             (E(3), -1), (E(3), -E(3)), (0, E(3)^2), (1, -E(3)^2),
             (-1, E(3)), (-E(3), E(3)), (E(3)^2, -1), (E(3)^2, -E(3)),
             (E(3), -E(3)^2), (-E(3)^2, E(3)), (-1, E(3)^2),
             (-E(3), E(3)^2), (E(3)^2, -E(3)^2), (-E(3)^2, E(3)^2)]

            sage: W = ReflectionGroup((4,2,2))
            sage: W.roots()
            [(1, 0), (-E(4), 1), (-1, 1), (-1, 0), (E(4), 1), (1, 1),
             (0, -E(4)), (E(4), -1), (E(4), E(4)), (0, E(4)),
             (E(4), -E(4)), (0, 1), (1, -E(4)), (1, -1), (0, -1),
             (1, E(4)), (-E(4), 0), (-1, E(4)), (E(4), 0), (-E(4), E(4)),
             (-E(4), -1), (-E(4), -E(4)), (-1, -E(4)), (-1, -1)]

            sage: W = ReflectionGroup((1,1,4), (3,1,2))
            sage: W.roots()
            [(1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0),
             (0, 0, 0, 1, 0), (0, 0, 0, -1, 1), (1, 1, 0, 0, 0),
             (0, 1, 1, 0, 0), (1, 1, 1, 0, 0), (-1, 0, 0, 0, 0),
             (0, -1, 0, 0, 0), (0, 0, -1, 0, 0), (-1, -1, 0, 0, 0),
             (0, -1, -1, 0, 0), (-1, -1, -1, 0, 0), (0, 0, 0, E(3), 0),
             (0, 0, 0, -E(3), 1), (0, 0, 0, 0, 1), (0, 0, 0, 1, -1),
             (0, 0, 0, 0, E(3)), (0, 0, 0, 1, -E(3)), (0, 0, 0, E(3)^2, 0),
             (0, 0, 0, -E(3)^2, 1), (0, 0, 0, E(3), -1), (0, 0, 0, E(3), -E(3)),
             (0, 0, 0, 0, E(3)^2), (0, 0, 0, 1, -E(3)^2), (0, 0, 0, -1, E(3)),
             (0, 0, 0, -E(3), E(3)), (0, 0, 0, E(3)^2, -1),
             (0, 0, 0, E(3)^2, -E(3)), (0, 0, 0, E(3), -E(3)^2),
             (0, 0, 0, -E(3)^2, E(3)), (0, 0, 0, -1, E(3)^2),
             (0, 0, 0, -E(3), E(3)^2), (0, 0, 0, E(3)^2, -E(3)^2),
             (0, 0, 0, -E(3)^2, E(3)^2)]
        """
    @cached_method
    def braid_relations(self):
        """
        Return the braid relations of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.braid_relations()
            [[[1, 2, 1], [2, 1, 2]]]

            sage: W = ReflectionGroup((2,1,3))
            sage: W.braid_relations()
            [[[1, 2, 1, 2], [2, 1, 2, 1]], [[1, 3], [3, 1]], [[2, 3, 2], [3, 2, 3]]]

            sage: W = ReflectionGroup((2,2,3))
            sage: W.braid_relations()
            [[[1, 2, 1], [2, 1, 2]], [[1, 3], [3, 1]], [[2, 3, 2], [3, 2, 3]]]
        """
    @cached_method
    def fundamental_invariants(self):
        """
        Return the fundamental invariants of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: W.fundamental_invariants()
            (-2*x0^2 + 2*x0*x1 - 2*x1^2, 6*x0^2*x1 - 6*x0*x1^2)

            sage: W = ReflectionGroup((3,1,2))
            sage: W.fundamental_invariants()
            (x0^3 + x1^3, x0^3*x1^3)
        """
    @cached_method
    def jacobian_of_fundamental_invariants(self, invs=None):
        """
        Return the matrix `[ \\partial_{x_i} F_j ]`, where ``invs`` are
        are any polynomials `F_1,\\ldots,F_n` in `x_1,\\ldots,x_n`.

        INPUT:

        - ``invs`` -- (default: the fundamental invariants) the polynomials
          `F_1, \\ldots, F_n`

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: W.fundamental_invariants()
            (-2*x0^2 + 2*x0*x1 - 2*x1^2, 6*x0^2*x1 - 6*x0*x1^2)

            sage: W.jacobian_of_fundamental_invariants()
            [     -4*x0 + 2*x1       2*x0 - 4*x1]
            [12*x0*x1 - 6*x1^2 6*x0^2 - 12*x0*x1]
        """
    @cached_method
    def primitive_vector_field(self, invs=None):
        """
        Return the primitive vector field of ``self`` is irreducible and
        well-generated.

        The primitive vector field is given as the coefficients (being rational
        functions) in the basis `\\partial_{x_1}, \\ldots, \\partial_{x_n}`.

        This is the partial derivation along the unique invariant of
        degree given by the Coxeter number. It can be computed as the
        row of the inverse of the Jacobian given by the highest degree.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: W.primitive_vector_field()
            (3*x1/(6*x0^2 - 6*x0*x1 - 12*x1^2), 1/(6*x0^2 - 6*x0*x1 - 12*x1^2))
        """
    def apply_vector_field(self, f, vf=None):
        """
        Return a rational function obtained by applying the vector
        field ``vf`` to the rational function ``f``.

        If ``vf`` is not given, the primitive vector field is used.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: for x in W.primitive_vector_field()[0].parent().gens():
            ....:     print(W.apply_vector_field(x))
            3*x1/(6*x0^2 - 6*x0*x1 - 12*x1^2)
            1/(6*x0^2 - 6*x0*x1 - 12*x1^2)
        """
    def cartan_matrix(self):
        """
        Return the Cartan matrix associated with ``self``.

        If ``self`` is crystallographic, the returned Cartan matrix is
        an instance of :class:`CartanMatrix`, and a normal matrix
        otherwise.

        Let `s_1, \\ldots, s_n` be a set of reflections which generate
        ``self`` with associated simple roots `s_1,\\ldots,s_n` and
        simple coroots `s^\\vee_i`. Then the Cartan matrix `C = (c_{ij})`
        is given by `s^\\vee_i(s_j)`. The Cartan matrix completely
        determines the reflection representation if the `s_i` are
        linearly independent.

        EXAMPLES::

            sage: ReflectionGroup(['A',4]).cartan_matrix()
            [ 2 -1  0  0]
            [-1  2 -1  0]
            [ 0 -1  2 -1]
            [ 0  0 -1  2]

            sage: ReflectionGroup(['H',4]).cartan_matrix()
            [              2 E(5)^2 + E(5)^3               0               0]
            [E(5)^2 + E(5)^3               2              -1               0]
            [              0              -1               2              -1]
            [              0               0              -1               2]

            sage: ReflectionGroup(4).cartan_matrix()
            [-2*E(3) - E(3)^2           E(3)^2]
            [         -E(3)^2 -2*E(3) - E(3)^2]

            sage: ReflectionGroup((4,2,2)).cartan_matrix()
            [       2  -2*E(4)       -2]
            [    E(4)        2 1 - E(4)]
            [      -1 1 + E(4)        2]
        """
    def invariant_form(self, brute_force: bool = False):
        '''
        Return the form that is invariant under the action of ``self``.

        This is unique only up to a global scalar on the irreducible
        components.

        INPUT:

        - ``brute_force`` -- if ``True``, the computation is done by
          applying the Reynolds operator; this is, the invariant form
          of `e_i` and `e_j` is computed as the sum
          `\\langle w(e_i), w(e_j)\\rangle`, where
          `\\langle \\cdot, \\cdot\\rangle` is the standard scalar product

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',3])
            sage: F = W.invariant_form(); F
            [   1 -1/2    0]
            [-1/2    1 -1/2]
            [   0 -1/2    1]

        To check that this is indeed the invariant form, see::

            sage: S = W.simple_reflections()
            sage: all( F == S[i].matrix()*F*S[i].matrix().transpose() for i in W.index_set() )
            True

            sage: W = ReflectionGroup([\'B\',3])
            sage: F = W.invariant_form(); F
            [ 1 -1  0]
            [-1  2 -1]
            [ 0 -1  2]
            sage: w = W.an_element().to_matrix()
            sage: w * F * w.transpose().conjugate() == F
            True

            sage: S = W.simple_reflections()
            sage: all( F == S[i].matrix()*F*S[i].matrix().transpose() for i in W.index_set() )
            True

            sage: W = ReflectionGroup((3,1,2))
            sage: F = W.invariant_form(); F
            [1 0]
            [0 1]

            sage: S = W.simple_reflections()
            sage: all( F == S[i].matrix()*F*S[i].matrix().transpose().conjugate() for i in W.index_set() )
            True

        It also worked for badly generated groups::

            sage: W = ReflectionGroup(7)
            sage: W.is_well_generated()
            False

            sage: F = W.invariant_form(); F
            [1 0]
            [0 1]
            sage: S = W.simple_reflections()
            sage: all( F == S[i].matrix()*F*S[i].matrix().transpose().conjugate() for i in W.index_set() )
            True

        And also for reducible types::

            sage: W = ReflectionGroup([\'B\',3],(4,2,3),4,7); W
            Reducible complex reflection group of rank 10 and type B3 x G(4,2,3) x ST4 x ST7
            sage: F = W.invariant_form(); S = W.simple_reflections()
            sage: all( F == S[i].matrix()*F*S[i].matrix().transpose().conjugate() for i in W.index_set() )
            True

        TESTS::

            sage: tests = [[\'A\',3],[\'B\',3],[\'F\',4],(4,2,2),4,7]
            sage: for ty in tests:
            ....:     W = ReflectionGroup(ty)
            ....:     A = W.invariant_form()
            ....:     B = W.invariant_form(brute_force=True)
            ....:     print("{} {}".format(ty, A == B/B[0,0]))
            [\'A\', 3] True
            [\'B\', 3] True
            [\'F\', 4] True
            (4, 2, 2) True
            4 True
            7 True
        '''
    def invariant_form_standardization(self):
        """
        Return the transformation of the space that turns the invariant
        form of ``self`` into the standard scalar product.

        Let `I` be the invariant form of a complex reflection group, and
        let `A` be the Hermitian matrix such that `A^2 = I`. The matrix
        `A` defines a change of basis such that the identity matrix is
        the invariant form. Indeed, we have

        .. MATH::

            (A^{-1} x A) \\mathcal{I} (A^{-1} y A)^* = A^{-1} x I y^* A^{-1}
            = A^{-1} I A^{-1} = \\mathcal{I},

        where `\\mathcal{I}` is the identity matrix.

        EXAMPLES::

            sage: W = ReflectionGroup((4,2,5))
            sage: I = W.invariant_form()
            sage: A = W.invariant_form_standardization()
            sage: A^2 == I
            True

        TESTS::

            sage: W = ReflectionGroup(9)
            sage: A = W.invariant_form_standardization()
            sage: S = W.simple_reflections()
            sage: Ainv = A.inverse()
            sage: T = {i: Ainv * S[i] * A for i in W.index_set()}
            sage: all(T[i] * T[i].conjugate_transpose()
            ....:     == 1 for i in W.index_set() )
            True
        """
    def set_reflection_representation(self, refl_repr=None) -> None:
        '''
        Set the reflection representation of ``self``.

        INPUT:

        - ``refl_repr`` -- dictionary representing the matrices of the
          generators of ``self`` with keys given by the index set, or
          ``None`` to reset to the default reflection representation

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))
            sage: for w in W: w.to_matrix(); print("-----")
            [1 0]
            [0 1]
            -----
            [ 1  1]
            [ 0 -1]
            -----
            [-1  0]
            [ 1  1]
            -----
            [-1 -1]
            [ 1  0]
            -----
            [ 0  1]
            [-1 -1]
            -----
            [ 0 -1]
            [-1  0]
            -----

            sage: W.set_reflection_representation({1: matrix([[0,1,0],[1,0,0],[0,0,1]]), 2: matrix([[1,0,0],[0,0,1],[0,1,0]])})
            sage: for w in W: w.to_matrix(); print("-----")
            [1 0 0]
            [0 1 0]
            [0 0 1]
            -----
            [1 0 0]
            [0 0 1]
            [0 1 0]
            -----
            [0 1 0]
            [1 0 0]
            [0 0 1]
            -----
            [0 0 1]
            [1 0 0]
            [0 1 0]
            -----
            [0 1 0]
            [0 0 1]
            [1 0 0]
            -----
            [0 0 1]
            [0 1 0]
            [1 0 0]
            -----
            sage: W.set_reflection_representation()
        '''
    def fake_degrees(self):
        '''
        Return the list of the fake degrees associated to ``self``.

        The fake degrees are `q`-versions of the degree of the character.
        In particular, they sum to Hilbert series of the coinvariant
        algebra of ``self``.

        .. NOTE::

            The ordering follows the one in Chevie and is not compatible with
            the current implementation of :meth:`irredubile_characters()`.

        EXAMPLES::

            sage: W = ReflectionGroup(12)
            sage: W.fake_degrees()
            [1, q^12, q^11 + q, q^8 + q^4, q^7 + q^5, q^6 + q^4 + q^2,
             q^10 + q^8 + q^6, q^9 + q^7 + q^5 + q^3]

            sage: W = ReflectionGroup(["H",4])
            sage: W.cardinality()
            14400
            sage: sum(fdeg.subs(q=1)**2 for fdeg in W.fake_degrees())
            14400
        '''
    def coxeter_number(self, chi=None):
        '''
        Return the Coxeter number associated to the irreducible character
        chi of the reflection group ``self``.

        The *Coxeter number* of a complex reflection group `W` is the trace
        in a character `\\chi` of `\\sum_t (Id - t)`, where `t` runs over all
        reflections. The result is always an integer.

        When `\\chi` is the reflection representation, the Coxeter number
        is equal to `\\frac{N + N^*}{n}` where `N` is the number of
        reflections, `N^*` is the number of reflection hyperplanes, and
        `n` is the rank of `W`. If `W` is further well-generated, the
        Coxeter number is equal to the highest degree d_n and to the
        order of a Coxeter element `c` of `W`.

        EXAMPLES::

            sage: W = ReflectionGroup(["H",4])
            sage: W.coxeter_number()
            30
            sage: all(W.coxeter_number(chi).is_integer()
            ....:     for chi in W.irreducible_characters())
            True
            sage: W = ReflectionGroup(14)
            sage: W.coxeter_number()
            24
        '''
    class Element(ComplexReflectionGroupElement):
        def conjugacy_class_representative(self):
            """
            Return a representative of the conjugacy class of ``self``.

            EXAMPLES::

                sage: W = ReflectionGroup((1,1,3))
                sage: for w in W:
                ....:     print('%s %s'%(w.reduced_word(), w.conjugacy_class_representative().reduced_word()))
                [] []
                [2] [1]
                [1] [1]
                [1, 2] [1, 2]
                [2, 1] [1, 2]
                [1, 2, 1] [1]
            """
        def conjugacy_class(self):
            """
            Return the conjugacy class of ``self``.

            EXAMPLES::

                sage: W = ReflectionGroup((1,1,3))
                sage: for w in W: sorted(w.conjugacy_class())
                [()]
                [(1,3)(2,5)(4,6), (1,4)(2,3)(5,6), (1,5)(2,4)(3,6)]
                [(1,3)(2,5)(4,6), (1,4)(2,3)(5,6), (1,5)(2,4)(3,6)]
                [(1,2,6)(3,4,5), (1,6,2)(3,5,4)]
                [(1,2,6)(3,4,5), (1,6,2)(3,5,4)]
                [(1,3)(2,5)(4,6), (1,4)(2,3)(5,6), (1,5)(2,4)(3,6)]
            """
        def reflection_length(self, in_unitary_group: bool = False):
            """
            Return the reflection length of ``self``.

            This is the minimal numbers of reflections needed to obtain
            ``self``.

            INPUT:

            - ``in_unitary_group`` -- boolean (default: ``False``); if ``True``,
              the reflection length is computed in the unitary group
              which is the dimension of the move space of ``self``

            EXAMPLES::

                sage: W = ReflectionGroup((1,1,3))
                sage: sorted([t.reflection_length() for t in W])
                [0, 1, 1, 1, 2, 2]

                sage: W = ReflectionGroup((2,1,2))
                sage: sorted([t.reflection_length() for t in W])
                [0, 1, 1, 1, 1, 2, 2, 2]

                sage: W = ReflectionGroup((2,2,2))
                sage: sorted([t.reflection_length() for t in W])
                [0, 1, 1, 2]

                sage: W = ReflectionGroup((3,1,2))
                sage: sorted([t.reflection_length() for t in W])
                [0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            """

class IrreducibleComplexReflectionGroup(ComplexReflectionGroup):
    class Element(ComplexReflectionGroup.Element):
        def is_coxeter_element(self, which_primitive: int = 1, is_class_representative: bool = False):
            """
            Return ``True`` if ``self`` is a Coxeter element.

            This is, whether ``self`` has an eigenvalue that is a
            primitive `h`-th root of unity.

            INPUT:

            - ``which_primitive`` -- (default: ``1``) for which power of
              the first primitive ``h``-th root of unity to look as a
              reflection eigenvalue for a regular element

            - ``is_class_representative`` -- boolean (default: ``True``); whether
              to compute instead on the conjugacy class representative

            .. SEEALSO::

                :meth:`~IrreducibleComplexReflectionGroup.coxeter_element`
                :meth:`~sage.categories.finite_complex_reflection_groups.coxeter_elements`

            EXAMPLES::

                sage: W = ReflectionGroup((1,1,3))
                sage: for w in W:
                ....:     print('%s %s'%(w.reduced_word(), w.is_coxeter_element()))
                [] False
                [2] False
                [1] False
                [1, 2] True
                [2, 1] True
                [1, 2, 1] False
            """
        def is_h_regular(self, is_class_representative: bool = False):
            """
            Return whether ``self`` is regular.

            This is if ``self`` has an eigenvector with eigenvalue `h`
            and which does not lie in any reflection hyperplane.
            Here, `h` denotes the Coxeter number.

            EXAMPLES::

                sage: W = ReflectionGroup((1,1,3))
                sage: for w in W:
                ....:     print('%s %s'%(w.reduced_word(), w.is_h_regular()))
                [] False
                [2] False
                [1] False
                [1, 2] True
                [2, 1] True
                [1, 2, 1] False
            """
        def is_regular(self, h, is_class_representative: bool = False):
            '''
            Return whether ``self`` is regular.

            This is, if ``self`` has an eigenvector with eigenvalue of order
            ``h`` and which does not lie in any reflection hyperplane.

            INPUT:

            - ``h`` -- the order of the eigenvalue
            - ``is_class_representative`` -- boolean (default: ``True``); whether
              to compute instead on the conjugacy class representative

            EXAMPLES::

                sage: W = ReflectionGroup((1,1,3))
                sage: h = W.coxeter_number()
                sage: for w in W:
                ....:     print("{} {}".format(w.reduced_word(), w.is_regular(h)))
                [] False
                [2] False
                [1] False
                [1, 2] True
                [2, 1] True
                [1, 2, 1] False

                sage: W = ReflectionGroup(23); h = W.coxeter_number()
                sage: for w in W:
                ....:     if w.is_regular(h):
                ....:         w.reduced_word()
                [1, 2, 3]
                [2, 1, 3]
                [1, 3, 2]
                [3, 2, 1]
                [2, 1, 2, 3, 2]
                [2, 3, 2, 1, 2]
                [1, 2, 1, 2, 3, 2, 1]
                [1, 2, 3, 2, 1, 2, 1]
                [1, 2, 1, 2, 3, 2, 1, 2, 3]
                [2, 1, 2, 1, 3, 2, 1, 2, 3]
                [2, 1, 2, 3, 2, 1, 2, 1, 3]
                [1, 2, 3, 2, 1, 2, 1, 3, 2]
                [3, 2, 1, 2, 1, 3, 2, 1, 2]
                [1, 2, 1, 2, 1, 3, 2, 1, 2]
                [2, 3, 2, 1, 2, 1, 3, 2, 1]
                [2, 1, 2, 1, 3, 2, 1, 2, 1]
                [2, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3]
                [1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3]
                [1, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3]
                [1, 2, 1, 2, 3, 2, 1, 2, 1, 3, 2]
                [1, 2, 3, 2, 1, 2, 1, 3, 2, 1, 2]
                [2, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1]
                [2, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3]
                [1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3]

            Check that :issue:`25478` is fixed::

                sage: W = ReflectionGroup(["A",5])
                sage: w = W.from_reduced_word([1,2,3,5])
                sage: w.is_regular(4)
                False
                sage: W = ReflectionGroup(["A",3])
                sage: len([w for w in W if w.is_regular(w.order())])
                18
            '''

def multi_partitions(n, S, i=None):
    """
    Return all vectors as lists of the same length as ``S`` whose
    standard inner product with ``S`` equals ``n``.

    EXAMPLES::

        sage: from sage.combinat.root_system.reflection_group_complex import multi_partitions
        sage: multi_partitions(10, [2,3,3,4])
        [[5, 0, 0, 0],
         [3, 0, 0, 1],
         [2, 2, 0, 0],
         [2, 1, 1, 0],
         [2, 0, 2, 0],
         [1, 0, 0, 2],
         [0, 2, 0, 1],
         [0, 1, 1, 1],
         [0, 0, 2, 1]]
    """
@cached_function
def power(f, k):
    """
    Return `f^k` and caching all intermediate results.

    Speeds the computation if one has to compute `f^k`'s for many
    values of `k`.

    EXAMPLES::

        sage: P.<x,y,z> = PolynomialRing(QQ)
        sage: f = -2*x^2 + 2*x*y - 2*y^2 + 2*y*z - 2*z^2
        sage: all( f^k == power(f,k) for k in range(20) )
        True
    """
