from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups as GeneralizedCoxeterGroups
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.misc.call import attrcall as attrcall
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

class CoxeterGroups(Category_singleton):
    '''
    The category of Coxeter groups.

    A *Coxeter group* is a group `W` with a distinguished (finite)
    family of involutions `(s_i)_{i\\in I}`, called the *simple
    reflections*, subject to relations of the form `(s_is_j)^{m_{i,j}} = 1`.

    `I` is the *index set* of `W` and `|I|` is the *rank* of `W`.

    See :wikipedia:`Coxeter_group` for details.

    EXAMPLES::

        sage: C = CoxeterGroups(); C
        Category of Coxeter groups
        sage: C.super_categories()
        [Category of generalized Coxeter groups]

        sage: W = C.example(); W
        The symmetric group on {0, ..., 3}

        sage: W.simple_reflections()
        Finite family {0: (1, 0, 2, 3), 1: (0, 2, 1, 3), 2: (0, 1, 3, 2)}

    Here are some further examples::

        sage: FiniteCoxeterGroups().example()
        The 5-th dihedral group of order 10
        sage: FiniteWeylGroups().example()
        The symmetric group on {0, ..., 3}
        sage: WeylGroup(["B", 3])                                                       # needs sage.combinat sage.groups
        Weyl Group of type [\'B\', 3] (as a matrix group acting on the ambient space)

        sage: S4 = SymmetricGroup(4); S4                                                # needs sage.groups
        Symmetric group of order 4! as a permutation group
        sage: S4 in CoxeterGroups().Finite()                                            # needs sage.groups
        True

    Those will eventually be also in this category::

        sage: DihedralGroup(5)                                                          # needs sage.groups
        Dihedral group of order 10 as a permutation group

    .. TODO:: add a demo of usual computations on Coxeter groups.

    .. SEEALSO::

        - :mod:`sage.combinat.root_system`
        - :class:`WeylGroups`
        - :class:`GeneralizedCoxeterGroups`

    .. WARNING::

        It is assumed that morphisms in this category preserve the
        distinguished choice of simple reflections. In particular,
        subobjects in this category are parabolic subgroups. In this
        sense, this category might be better named ``Coxeter
        Systems``. In the long run we might want to have two distinct
        categories, one for Coxeter groups (with morphisms being just
        group morphisms) and one for Coxeter systems::

            sage: CoxeterGroups().is_full_subcategory(Groups())
            False
            sage: from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups
            sage: CoxeterGroups().is_full_subcategory(GeneralizedCoxeterGroups())
            True

    TESTS::

        sage: W = CoxeterGroups().example()
        sage: TestSuite(W).run()
    '''
    def super_categories(self):
        """
        EXAMPLES::

            sage: CoxeterGroups().super_categories()
            [Category of generalized Coxeter groups]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, all the structure Coxeter groups have in addition to
        groups (simple reflections, ...) is already defined in the
        super category.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: CoxeterGroups().additional_structure()
        """
    Finite: Incomplete
    Algebras: Incomplete
    class ParentMethods:
        @abstract_method
        def coxeter_matrix(self) -> None:
            """
            Return the Coxeter matrix associated to ``self``.

            EXAMPLES::

                sage: G = WeylGroup(['A', 3])                                           # needs sage.combinat sage.groups
                sage: G.coxeter_matrix()                                                # needs sage.combinat sage.groups
                [1 3 2]
                [3 1 3]
                [2 3 1]
            """
        @cached_method
        def index_set(self):
            """
            Return the index set of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = CoxeterGroup([[1,3],[3,1]])
                sage: W.index_set()
                (1, 2)
                sage: W = CoxeterGroup([[1,3],[3,1]], index_set=['x', 'y'])
                sage: W.index_set()
                ('x', 'y')
                sage: W = CoxeterGroup(['H', 3])
                sage: W.index_set()
                (1, 2, 3)
            """
        def coxeter_diagram(self):
            """
            Return the Coxeter diagram of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.graphs sage.groups
                sage: W = CoxeterGroup(['H', 3], implementation='reflection')
                sage: G = W.coxeter_diagram(); G
                Graph on 3 vertices
                sage: G.edges(sort=True)
                [(1, 2, 3), (2, 3, 5)]
                sage: CoxeterGroup(G) is W
                True
                sage: G = Graph([(0, 1, 3), (1, 2, oo)])
                sage: W = CoxeterGroup(G)
                sage: W.coxeter_diagram() == G
                True
                sage: CoxeterGroup(W.coxeter_diagram()) is W
                True
            """
        def coxeter_type(self):
            """
            Return the Coxeter type of ``self``.

            EXAMPLES::

                sage: W = CoxeterGroup(['H', 3])                                        # needs sage.combinat sage.groups
                sage: W.coxeter_type()                                                  # needs sage.combinat sage.groups
                Coxeter type of ['H', 3]
            """
        def braid_relations(self):
            '''
            Return the braid relations of ``self`` as a list of reduced
            words of the braid relations.

            EXAMPLES::

                sage: W = WeylGroup(["A", 2])                                           # needs sage.combinat sage.groups
                sage: W.braid_relations()                                               # needs sage.combinat sage.groups
                [[[1, 2, 1], [2, 1, 2]]]

                sage: W = WeylGroup(["B", 3])                                           # needs sage.combinat sage.groups
                sage: W.braid_relations()                                               # needs sage.combinat sage.groups
                [[[1, 2, 1], [2, 1, 2]], [[1, 3], [3, 1]], [[2, 3, 2, 3], [3, 2, 3, 2]]]
            '''
        def braid_group_as_finitely_presented_group(self):
            '''
            Return the associated braid group.

            EXAMPLES::

                sage: W = CoxeterGroup([\'A\', 2])                                        # needs sage.combinat sage.groups
                sage: W.braid_group_as_finitely_presented_group()                       # needs sage.combinat sage.groups
                Finitely presented group < S1, S2 | S1*S2*S1*S2^-1*S1^-1*S2^-1 >

                sage: W = WeylGroup([\'B\', 2])                                           # needs sage.combinat sage.groups
                sage: W.braid_group_as_finitely_presented_group()                       # needs sage.combinat sage.groups
                Finitely presented group < S1, S2 | (S1*S2)^2*(S1^-1*S2^-1)^2 >

                sage: W = ReflectionGroup([\'B\',3], index_set=["AA","BB","5"])  # optional - gap3
                sage: W.braid_group_as_finitely_presented_group()              # optional - gap3
                Finitely presented group < SAA, SBB, S5 |
                 (SAA*SBB)^2*(SAA^-1*SBB^-1)^2, SAA*S5*SAA^-1*S5^-1,
                 SBB*S5*SBB*S5^-1*SBB^-1*S5^-1 >
            '''
        def braid_orbit_iter(self, word) -> Generator[Incomplete]:
            """
            Iterate over the braid orbit of a word ``word`` of indices.

            The input word does not need to be a reduced expression of
            an element.

            INPUT:

            - ``word`` -- list (or iterable) of indices in
              ``self.index_set()``

            OUTPUT:

            all lists that can be obtained from
            ``word`` by replacements of braid relations

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: sorted(W.braid_orbit_iter([0, 1, 2, 1]))                          # needs sage.combinat sage.graphs
                [[0, 1, 2, 1], [0, 2, 1, 2], [2, 0, 1, 2]]
            """
        def braid_orbit(self, word):
            '''
            Return the braid orbit of a word ``word`` of indices.

            The input word does not need to be a reduced expression of
            an element.

            INPUT:

            - ``word`` -- a list (or iterable) of indices in
              ``self.index_set()``

            OUTPUT:

            a list of all lists that can be obtained from
            ``word`` by replacements of braid relations

            See :meth:`braid_relations` for the definition of braid
            relations.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0] * s[1] * s[2] * s[1]
                sage: word = w.reduced_word(); word
                [0, 1, 2, 1]

                sage: sorted(W.braid_orbit(word))                                       # needs sage.combinat sage.graphs
                [[0, 1, 2, 1], [0, 2, 1, 2], [2, 0, 1, 2]]

                sage: sorted(W.braid_orbit([2,1,1,2,1]))                                # needs sage.combinat sage.graphs
                [[1, 2, 1, 1, 2], [2, 1, 1, 2, 1], [2, 1, 2, 1, 2], [2, 2, 1, 2, 2]]

                sage: # optional - gap3
                sage: W = ReflectionGroup([\'A\',3], index_set=["AA","BB","5"])
                sage: w = W.long_element()
                sage: W.braid_orbit(w.reduced_word())
                [[\'BB\', \'5\', \'AA\', \'BB\', \'5\', \'AA\'],
                 [\'5\', \'BB\', \'5\', \'AA\', \'BB\', \'5\'],
                 [\'BB\', \'AA\', \'BB\', \'5\', \'BB\', \'AA\'],
                 [\'AA\', \'5\', \'BB\', \'AA\', \'5\', \'BB\'],
                 [\'5\', \'AA\', \'BB\', \'AA\', \'5\', \'BB\'],
                 [\'AA\', \'BB\', \'5\', \'AA\', \'BB\', \'AA\'],
                 [\'AA\', \'BB\', \'AA\', \'5\', \'BB\', \'AA\'],
                 [\'AA\', \'BB\', \'5\', \'BB\', \'AA\', \'BB\'],
                 [\'BB\', \'AA\', \'5\', \'BB\', \'AA\', \'5\'],
                 [\'BB\', \'5\', \'AA\', \'BB\', \'AA\', \'5\'],
                 [\'AA\', \'5\', \'BB\', \'5\', \'AA\', \'BB\'],
                 [\'5\', \'BB\', \'AA\', \'5\', \'BB\', \'5\'],
                 [\'5\', \'BB\', \'AA\', \'BB\', \'5\', \'BB\'],
                 [\'5\', \'AA\', \'BB\', \'5\', \'AA\', \'BB\'],
                 [\'BB\', \'5\', \'BB\', \'AA\', \'BB\', \'5\'],
                 [\'BB\', \'AA\', \'5\', \'BB\', \'5\', \'AA\']]

            .. TODO::

                The result should be full featured finite enumerated set
                (e.g., counting can be done much faster than iterating).

            .. SEEALSO::

                :meth:`.reduced_words`
            '''
        def __iter__(self):
            '''
            Return an iterator over the elements of this Coxeter group.

            EXAMPLES::

                sage: D5 = FiniteCoxeterGroups().example(5)
                sage: sorted(list(D5)) # indirect doctest (but see :meth:`._test_enumerated_set_iter_list`)
                [(),
                 (1,),
                 (1, 2),
                 (1, 2, 1),
                 (1, 2, 1, 2),
                 (1, 2, 1, 2, 1),
                 (2,),
                 (2, 1),
                 (2, 1, 2),
                 (2, 1, 2, 1)]

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 2, 1])
                sage: g = iter(W)
                sage: next(g)
                [1 0 0]
                [0 1 0]
                [0 0 1]
                sage: next(g)
                [-1  1  1]
                [ 0  1  0]
                [ 0  0  1]
                sage: next(g)
                [ 1  0  0]
                [ 1 -1  1]
                [ 0  0  1]
            '''
        def weak_order_ideal(self, predicate, side: str = 'right', category=None):
            '''
            Return a weak order ideal defined by a predicate.

            INPUT:

            - ``predicate`` -- a predicate on the elements of ``self`` defining an
              weak order ideal in ``self``
            - ``side`` -- ``\'left\'`` or ``\'right\'`` (default: ``\'right\'``)

            OUTPUT: an enumerated set

            EXAMPLES::

                sage: D6 = FiniteCoxeterGroups().example(5)
                sage: I = D6.weak_order_ideal(predicate=lambda w: w.length() <= 3)
                sage: I.cardinality()
                7
                sage: list(I)
                [(), (1,), (2,), (1, 2), (2, 1), (1, 2, 1), (2, 1, 2)]

            We now consider an infinite Coxeter group::

                sage: W = WeylGroup(["A",1,1])                                          # needs sage.groups sage.rings.number_field
                sage: I = W.weak_order_ideal(predicate=lambda w: w.length() <= 2)       # needs sage.groups sage.rings.number_field
                sage: list(iter(I))                                                     # needs sage.groups sage.rings.number_field
                [
                [1 0]  [-1  2]  [ 1  0]  [ 3 -2]  [-1  2]
                [0 1], [ 0  1], [ 2 -1], [ 2 -1], [-2  3]
                ]

            Even when the result is finite, some features of
            :class:`FiniteEnumeratedSets` are not available::

                sage: I.cardinality()  # todo: not implemented
                5
                sage: list(I)          # todo: not implemented

            unless this finiteness is explicitly specified::

                sage: I = W.weak_order_ideal(predicate=lambda w: w.length() <= 2,       # needs sage.groups sage.rings.number_field
                ....:                        category=FiniteEnumeratedSets())
                sage: I.cardinality()                                                   # needs sage.groups sage.rings.number_field
                5
                sage: list(I)                                                           # needs sage.groups sage.rings.number_field
                [
                [1 0]  [-1  2]  [ 1  0]  [ 3 -2]  [-1  2]
                [0 1], [ 0  1], [ 2 -1], [ 2 -1], [-2  3]
                ]

            .. rubric:: Background

            The weak order is returned as a :class:`RecursivelyEnumeratedSet_forest`.
            This is achieved by assigning to each element `u1` of the
            ideal a single ancestor `u=u1 s_i`, where `i` is the
            smallest descent of `u`.

            This allows for iterating through the elements in
            roughly Constant Amortized Time and constant memory
            (taking the operations and size of the generated objects
            as constants).

            TESTS:

            We iterate over each level (i.e., breadth-first-search in the
            search forest), see :issue:`19926`::

                sage: W = CoxeterGroup([\'A\',2])                                         # needs sage.groups sage.rings.number_field
                sage: [x.length() for x in W]                                           # needs sage.groups sage.rings.number_field
                [0, 1, 1, 2, 2, 3]
            '''
        @cached_method
        def coxeter_element(self):
            """
            Return a Coxeter element.

            The result is the product of the simple reflections, in some order.

            .. NOTE::

                This implementation is shared with well generated
                complex reflection groups. It would be nicer to put it
                in some joint super category; however, in the current
                state of the art, there is none where it is clear that
                this is the right construction for obtaining a Coxeter
                element.

                In this context, this is an element having a regular
                eigenvector (a vector not contained in any reflection
                hyperplane of ``self``).

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: CoxeterGroup(['A', 4]).coxeter_element().reduced_word()
                [1, 2, 3, 4]
                sage: CoxeterGroup(['B', 4]).coxeter_element().reduced_word()
                [1, 2, 3, 4]
                sage: CoxeterGroup(['D', 4]).coxeter_element().reduced_word()
                [1, 2, 4, 3]
                sage: CoxeterGroup(['F', 4]).coxeter_element().reduced_word()
                [1, 2, 3, 4]
                sage: CoxeterGroup(['E', 8]).coxeter_element().reduced_word()
                [1, 3, 2, 4, 5, 6, 7, 8]
                sage: CoxeterGroup(['H', 3]).coxeter_element().reduced_word()
                [1, 2, 3]

            This method is also used for well generated finite complex
            reflection groups::

                sage: W = ReflectionGroup((1,1,4))          # optional - gap3
                sage: W.coxeter_element().reduced_word()    # optional - gap3
                [1, 2, 3]

                sage: W = ReflectionGroup((2,1,4))          # optional - gap3
                sage: W.coxeter_element().reduced_word()    # optional - gap3
                [1, 2, 3, 4]

                sage: W = ReflectionGroup((4,1,4))          # optional - gap3
                sage: W.coxeter_element().reduced_word()    # optional - gap3
                [1, 2, 3, 4]

                sage: W = ReflectionGroup((4,4,4))          # optional - gap3
                sage: W.coxeter_element().reduced_word()    # optional - gap3
                [1, 2, 3, 4]

            TESTS::

                sage: WeylGroup(['A', 4]).coxeter_element().reduced_word()              # needs sage.combinat sage.groups
                [1, 2, 3, 4]
                sage: SymmetricGroup(3).coxeter_element()                               # needs sage.groups
                (1,3,2)
            """
        @cached_method
        def standard_coxeter_elements(self):
            """
            Return all standard Coxeter elements in ``self``.

            This is the set of all elements in ``self`` obtained from any
            product of the simple reflections in ``self``.

            .. NOTE::

                - ``self`` is assumed to be well-generated.
                - This works even beyond real reflection groups, but the conjugacy
                  class is not unique and we only obtain one such class.

            EXAMPLES::

                sage: W = ReflectionGroup(4)                 # optional - gap3
                sage: sorted(W.standard_coxeter_elements())  # optional - gap3
                [(1,7,6,12,23,20)(2,8,17,24,9,5)(3,16,10,19,15,21)(4,14,11,22,18,13),
                 (1,10,4,12,21,22)(2,11,19,24,13,3)(5,15,7,17,16,23)(6,18,8,20,14,9)]

            TESTS::

                sage: W = SymmetricGroup(3)                                             # needs sage.groups
                sage: sorted(W.standard_coxeter_elements())                             # needs sage.combinat sage.groups
                [(1,2,3), (1,3,2)]

                sage: W = Permutations(3)
                sage: sorted(W.standard_coxeter_elements())                             # needs sage.graphs
                [[2, 3, 1], [3, 1, 2]]

                sage: W = CoxeterGroup(['D', 3])                                        # needs sage.combinat sage.groups
                sage: sorted(W.standard_coxeter_elements())                             # needs sage.combinat sage.groups
                [
                [-1  1  1]  [ 0 -1  1]  [ 0  1 -1]  [ 1 -1 -1]
                [-1  0  1]  [ 1 -1  0]  [ 0  0 -1]  [ 1 -1  0]
                [-1  1  0], [ 0 -1  0], [ 1  0 -1], [ 1  0 -1]
                ]

                sage: W = ColoredPermutations(3,2)                                      # needs sage.combinat
                sage: len(W.standard_coxeter_elements())                                # needs sage.combinat sage.graphs
                2
            """
        def grassmannian_elements(self, side: str = 'right'):
            '''
            Return the left or right Grassmannian elements of ``self``
            as an enumerated set.

            INPUT:

            - ``side`` -- (default: ``\'right\'``) ``\'left\'`` or ``\'right\'``

            EXAMPLES::

                sage: S = CoxeterGroups().example()
                sage: G = S.grassmannian_elements()
                sage: G.cardinality()
                12
                sage: G.list()
                [(0, 1, 2, 3), (1, 0, 2, 3), (0, 2, 1, 3), (0, 1, 3, 2),
                 (2, 0, 1, 3), (1, 2, 0, 3), (0, 3, 1, 2), (0, 2, 3, 1),
                 (3, 0, 1, 2), (1, 3, 0, 2), (1, 2, 3, 0), (2, 3, 0, 1)]
                sage: sorted(tuple(w.descents()) for w in G)
                [(), (0,), (0,), (0,), (1,), (1,), (1,), (1,), (1,), (2,), (2,), (2,)]
                sage: G = S.grassmannian_elements(side = "left")
                sage: G.cardinality()
                12
                sage: sorted(tuple(w.descents(side = "left")) for w in G)
                [(), (0,), (0,), (0,), (1,), (1,), (1,), (1,), (1,), (2,), (2,), (2,)]
            '''
        def fully_commutative_elements(self):
            """
            Return the set of fully commutative elements in this Coxeter group.

            .. SEEALSO::

                :class:`~sage.combinat.fully_commutative_elements.FullyCommutativeElements`

            EXAMPLES::

                sage: CoxeterGroup(['A', 3]).fully_commutative_elements()               # needs sage.combinat sage.groups
                Fully commutative elements of
                 Finite Coxeter group over Integer Ring with Coxeter matrix:
                [1 3 2]
                [3 1 3]
                [2 3 1]
            """
        def simple_projection(self, i, side: str = 'right', length_increasing: bool = True):
            """
            Return the simple projection `\\pi_i` (or `\\overline\\pi_i` if ``length_increasing`` is ``False``).

            INPUT:

            - ``i`` -- an element of the index set of ``self``

            See :meth:`.simple_projections` for the options and for
            the definition of the simple projections.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: W
                The symmetric group on {0, ..., 3}
                sage: s = W.simple_reflections()
                sage: sigma = W.an_element()
                sage: sigma
                (1, 2, 3, 0)
                sage: u0 = W.simple_projection(0)
                sage: d0 = W.simple_projection(0, length_increasing=False)
                sage: sigma.length()
                3
                sage: pi=sigma*s[0]
                sage: pi.length()
                4
                sage: u0(sigma)
                (2, 1, 3, 0)
                sage: pi
                (2, 1, 3, 0)
                sage: u0(pi)
                (2, 1, 3, 0)
                sage: d0(sigma)
                (1, 2, 3, 0)
                sage: d0(pi)
                (1, 2, 3, 0)
            """
        def kazhdan_lusztig_cells(self, side: str = 'left'):
            """
            Compute the left, right, or two-sided Kazhdan-Lusztig cells of
            ``self`` if ``self`` is finite.

            The cells are computed  by using :func:`kazhdan_lusztig_cell()
            <CoxeterGroups.ElementMethods.kazhdan_lusztig_cell()>`.

            As detailed there, installation of the optional package ``coxeter3``
            is recommended (though not required) before using this function
            as it speeds up the computation.

            INPUT:

            - ``side`` -- (default: ``'left'``) either ``'left'``,
              ``'right'``, or ``'two-sided'``

            EXAMPLES:

            We compute the right cells in the Coxeter group of type `A_2`
            below. Note that each Coxeter group may be created with multiple
            implementations, namely, 'reflection' (default), 'permutation',
            'matrix', or 'coxeter3'. The choice of implementation affects the
            representation of elements in the output cells but not the method
            used for the cell computation::

                sage: # needs sage.combinat sage.groups
                sage: W = CoxeterGroup('A2')
                sage: KL_cells = W.kazhdan_lusztig_cells(side='right')
                sage: set([tuple(sorted(C, key=lambda w: w.reduced_word()))
                ....:      for C in KL_cells])
                {(
                [-1  1]  [ 0 -1]
                [ 0  1], [ 1 -1]
                ),
                 (
                [ 0 -1]
                [-1  0]
                ),
                 (
                [1 0]
                [0 1]
                ),
                 (
                [ 1  0]  [-1  1]
                [ 1 -1], [-1  0]
                )}
                sage: len(KL_cells)
                4

                sage: W = CoxeterGroup('A2', implementation='permutation')              # needs sage.combinat sage.groups
                sage: len(W.kazhdan_lusztig_cells(side='right'))                        # needs sage.combinat sage.groups
                4

            We compute the left cells in the Coxeter group of type `A_3`
            below. If the optional package ``coxeter3`` is installed, it
            runs in the background even if the group is not created with
            the ``'coxeter3'`` implementation::

                sage: # optional - coxeter3, needs sage.combinat sage.groups sage.libs.gap sage.modules sage.rings.number_field
                sage: W = CoxeterGroup('A3', implementation='coxeter3')
                sage: KL_cells = W.kazhdan_lusztig_cells()
                sage: set([tuple(sorted(C)) for C in KL_cells])
                {([],),
                 ([1], [2, 1], [3, 2, 1]),
                 ([1, 2], [2], [3, 2]),
                 ([1, 2, 1], [1, 3, 2, 1], [2, 1, 3, 2, 1]),
                 ([1, 2, 1, 3], [1, 2, 3, 2, 1], [2, 3, 2, 1]),
                 ([1, 2, 1, 3, 2], [1, 2, 3, 2], [2, 3, 2]),
                 ([1, 2, 1, 3, 2, 1],),
                 ([1, 2, 3], [2, 3], [3]),
                 ([1, 3], [2, 1, 3]),
                 ([1, 3, 2], [2, 1, 3, 2])}
                sage: len(KL_cells)
                10
                sage: W = CoxeterGroup('A3', implementation='permutation')
                sage: len(W.kazhdan_lusztig_cells())
                10

            Computing the two-sided cells in `B_3`::

                sage: # optional - coxeter3, needs sage.combinat sage.groups sage.libs.gap sage.modules sage.rings.number_field
                sage: W = CoxeterGroup('B3', implementation='coxeter3')
                sage: b3_cells = W.kazhdan_lusztig_cells('two-sided')
                sage: len(b3_cells)
                6
                sage: set([tuple(sorted(C))
                ....:     for C in W.kazhdan_lusztig_cells()])
                {([],),
                 ([1], [1, 2, 3, 2, 1], [2, 1], [2, 3, 2, 1], [3, 2, 1]),
                 ([1, 2], [1, 2, 3, 2], [2], [2, 3, 2], [3, 2]),
                 ([1, 2, 3], [2, 3], [3], [3, 2, 3]),
                 ([2, 1, 2], [2, 3, 2, 1, 2], [3, 2, 1, 2]),
                 ([2, 1, 2, 3], [2, 3, 2, 1, 2, 3], [3, 2, 1, 2, 3]),
                 ([2, 1, 2, 3, 2], [2, 3, 2, 1, 2, 3, 2], [3, 2, 1, 2, 3, 2]),
                 ([2, 1, 2, 3, 2, 1],
                  [2, 3, 2, 1, 2, 3, 2, 1],
                  [3, 2, 1, 2, 3, 2, 1],
                  [3, 2, 3, 2, 1, 2]),
                 ([2, 3, 1], [3, 1], [3, 2, 3, 1]),
                 ([2, 3, 1, 2], [3, 1, 2], [3, 2, 3, 1, 2]),
                 ([2, 3, 1, 2, 3], [3, 1, 2, 3], [3, 2, 3, 1, 2, 3]),
                 ([2, 3, 1, 2, 3, 2],
                  [3, 1, 2, 3, 2],
                  [3, 2, 3, 1, 2, 3, 2],
                  [3, 2, 3, 2],
                  [3, 2, 3, 2, 1, 2, 3, 2]),
                 ([2, 3, 1, 2, 3, 2, 1],
                  [3, 1, 2, 3, 2, 1],
                  [3, 2, 3, 1, 2, 3, 2, 1],
                  [3, 2, 3, 2, 1],
                  [3, 2, 3, 2, 1, 2, 3]),
                 ([3, 2, 3, 2, 1, 2, 3, 2, 1],)}

            TESTS::

                sage: W = CoxeterGroup(['A', 2, 1])                                     # needs sage.combinat sage.groups
                sage: W.kazhdan_lusztig_cells()                                         # needs sage.combinat sage.groups
                Traceback (most recent call last):
                ...
                ValueError: the Coxeter group must be finite to compute Kazhdan--Lusztig cells
            """
        @cached_method
        def simple_projections(self, side: str = 'right', length_increasing: bool = True):
            """
            Return the family of simple projections, also known as 0-Hecke or Demazure operators.

            INPUT:

            - ``self`` -- a Coxeter group `W`
            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
            - ``length_increasing`` -- boolean (default: ``True``); whether
              the operator increases or decreases length

            This returns the simple projections of `W`, as a family.

            To each simple reflection `s_i` of `W`, corresponds a
            *simple projection* `\\pi_i` from `W` to `W` defined by:

                      `\\pi_i(w) = w s_i` if `i` is not a descent of `w`
                      `\\pi_i(w) = w` otherwise.

            The simple projections `(\\pi_i)_{i\\in I}` move elements
            down the right permutohedron, toward the maximal element.
            They satisfy the same braid relations as the simple reflections,
            but are idempotents `\\pi_i^2=\\pi` not involutions `s_i^2 = 1`. As such,
            the simple projections generate the `0`-Hecke monoid.

            By symmetry, one can also define the projections
            `(\\overline\\pi_i)_{i\\in I}` (when the option ``length_increasing`` is False):

                      `\\overline\\pi_i(w) = w s_i` if `i` is a descent of `w`
                      `\\overline\\pi_i(w) = w` otherwise.

            as well as the analogues acting on the left (when the option ``side`` is 'left').

            EXAMPLES::

                sage: W = CoxeterGroups().example(); W
                The symmetric group on {0, ..., 3}
                sage: s = W.simple_reflections()
                sage: sigma = W.an_element(); sigma
                (1, 2, 3, 0)
                sage: pi = W.simple_projections(); pi
                Finite family {0: <function ...<lambda> at ...>,
                               1: <function ...<lambda> at ...>,
                               2: <function ...<lambda> ...>}
                sage: pi[1](sigma)
                (1, 3, 2, 0)
                sage: W.simple_projection(1)(sigma)
                (1, 3, 2, 0)
            """
        def sign_representation(self, base_ring=None):
            '''
            Return the sign representation of ``self`` over ``base_ring``.

            INPUT:

            - ``base_ring`` -- (optional) the base ring; the default is `\\ZZ`

            EXAMPLES::

                sage: W = WeylGroup([\'D\', 4])                                           # needs sage.combinat sage.groups
                sage: W.sign_representation(QQ)                                         # needs sage.combinat sage.groups
                Sign representation of
                 Weyl Group of type [\'D\', 4] (as a matrix group acting on the ambient space)
                 over Rational Field

                sage: # optional - gap3
                sage: W = CoxeterGroup([\'B\',3], implementation="coxeter3")
                sage: W.sign_representation()
                Sign representation of Coxeter group of type [\'B\', 3]
                 implemented by Coxeter3 over Integer Ring
            '''
        def reflection_representation(self, base_ring=None, side: str = 'left'):
            '''
            Return the reflection representation of ``self``.

            This is also the canonical faithful representation of a
            Coxeter group.

            INPUT:

            - ``base_ring`` -- (optional) the base ring; the default is
              the base ring of :meth:`canonical_representation`
            - ``side`` -- ignored

            EXAMPLES::

                sage: W = CoxeterGroup([\'D\', 4])
                sage: W.reflection_representation()
                Reflection representation of Finite Coxeter group over
                 Integer Ring with Coxeter matrix:
                [1 3 2 2]
                [3 1 3 3]
                [2 3 1 2]
                [2 3 2 1]

                sage: W = CoxeterGroup([\'I\', 13])
                sage: W.reflection_representation()
                Reflection representation of Finite Coxeter group over
                 Universal Cyclotomic Field with Coxeter matrix:
                [ 1 13]
                [13  1]

                sage: W = WeylGroup(["B", 3, 1])
                sage: W.reflection_representation(QQ)
                Reflection representation of Weyl Group of type [\'B\', 3, 1]
                 (as a matrix group acting on the root space)
            '''
        def demazure_product(self, Q):
            """
            Return the Demazure product of the list ``Q`` in ``self``.

            INPUT:

            - ``Q`` -- list of elements from the index set of ``self``

            This returns the Coxeter group element that represents the
            composition of 0-Hecke or Demazure operators.

            See :meth:`CoxeterGroups.ParentMethods.simple_projections`.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 2])
                sage: w = W.demazure_product([2,2,1])
                sage: w.reduced_word()
                [2, 1]
                sage: w = W.demazure_product([2,1,2,1,2])
                sage: w.reduced_word()
                [1, 2, 1]

                sage: W = WeylGroup(['B', 2])                                           # needs sage.combinat sage.groups
                sage: w = W.demazure_product([2,1,2,1,2])                               # needs sage.combinat sage.groups
                sage: w.reduced_word()                                                  # needs sage.combinat sage.groups
                [2, 1, 2, 1]
            """
        def bruhat_interval(self, x, y):
            '''
            Return the list of ``t`` such that ``x <= t <= y``.

            EXAMPLES::

                sage: W = WeylGroup("A3", prefix=\'s\')                                   # needs sage.combinat sage.groups
                sage: s1, s2, s3 = W.simple_reflections()                               # needs sage.combinat sage.groups
                sage: W.bruhat_interval(s2, s1*s3*s2*s1*s3)                             # needs sage.combinat sage.groups
                [s1*s2*s3*s2*s1, s2*s3*s2*s1, s3*s1*s2*s1, s1*s2*s3*s1,
                 s1*s2*s3*s2, s3*s2*s1, s2*s3*s1, s2*s3*s2, s1*s2*s1,
                 s3*s1*s2, s1*s2*s3, s2*s1, s3*s2, s2*s3, s1*s2, s2]

                sage: W = WeylGroup([\'A\', 2, 1], prefix=\'s\')                            # needs sage.combinat sage.groups
                sage: s0, s1, s2 = W.simple_reflections()                               # needs sage.combinat sage.groups
                sage: W.bruhat_interval(1, s0*s1*s2)                                    # needs sage.combinat sage.groups
                [s0*s1*s2, s1*s2, s0*s2, s0*s1, s2, s1, s0, 1]
            '''
        def bruhat_interval_poset(self, x, y, facade: bool = False):
            '''
            Return the poset of the Bruhat interval between ``x`` and ``y``
            in Bruhat order.

            EXAMPLES::

                sage: W = WeylGroup("A3", prefix=\'s\')                                   # needs sage.combinat sage.groups
                sage: s1, s2, s3 = W.simple_reflections()                               # needs sage.combinat sage.groups
                sage: W.bruhat_interval_poset(s2, s1*s3*s2*s1*s3)                       # needs sage.combinat sage.groups
                Finite poset containing 16 elements

                sage: W = WeylGroup([\'A\', 2, 1], prefix=\'s\')                            # needs sage.combinat sage.groups
                sage: s0, s1, s2 = W.simple_reflections()                               # needs sage.combinat sage.groups
                sage: W.bruhat_interval_poset(1, s0*s1*s2)                              # needs sage.combinat sage.groups
                Finite poset containing 8 elements

            TESTS::

                sage: W.bruhat_interval_poset(s0*s1*s2, s0*s1*s2)                       # needs sage.combinat sage.groups
                Finite poset containing 1 elements
            '''
        def bruhat_graph(self, x=None, y=None, edge_labels: bool = False):
            '''
            Return the Bruhat graph as a directed graph, with an edge `u \\to v`
            if and only if `u < v` in the Bruhat order, and `u = r \\cdot v`.

            The Bruhat graph `\\Gamma(x,y)`, defined if `x \\leq y` in the
            Bruhat order, has as its vertices the Bruhat interval
            `\\{ t | x \\leq t \\leq y \\}`, and as its edges are the pairs
            `(u, v)` such that `u = r \\cdot v` where `r` is a reflection,
            that is, a conjugate of a simple reflection.

            REFERENCES:

            Carrell, The Bruhat graph of a Coxeter group, a conjecture of Deodhar,
            and rational smoothness of Schubert varieties. Algebraic groups and
            their generalizations: classical methods (University Park, PA, 1991),
            53--61, Proc. Sympos. Pure Math., 56, Part 1, Amer. Math. Soc.,
            Providence, RI, 1994.

            EXAMPLES::

                sage: W = CoxeterGroup([\'H\', 3])                                        # needs sage.combinat sage.graphs sage.groups
                sage: G = W.bruhat_graph(); G                                           # needs sage.combinat sage.graphs sage.groups
                Digraph on 120 vertices

                sage: # needs sage.combinat sage.graphs sage.groups
                sage: W = CoxeterGroup([\'A\', 2, 1])
                sage: s1, s2, s3 = W.simple_reflections()
                sage: W.bruhat_graph(s1, s1*s3*s2*s3)
                Digraph on 6 vertices
                sage: W.bruhat_graph(s1, s3*s2*s3)
                Digraph on 0 vertices

                sage: W = WeylGroup("A3", prefix=\'s\')                                   # needs sage.combinat sage.graphs sage.groups
                sage: s1, s2, s3 = W.simple_reflections()                               # needs sage.combinat sage.graphs sage.groups
                sage: G = W.bruhat_graph(s1*s3, s1*s2*s3*s2*s1); G                      # needs sage.combinat sage.graphs sage.groups
                Digraph on 10 vertices

            Check that the graph has the correct number of edges
            (see :issue:`17744`)::

                sage: len(G.edges(sort=False))                                          # needs sage.combinat sage.graphs sage.groups
                16
            '''
        def canonical_representation(self):
            '''
            Return the canonical faithful representation of ``self``.

            .. SEEALSO::

                To obtain the underlying module with the action, use
                :meth:`reflection_representation`.

            EXAMPLES::

                sage: W = WeylGroup("A3")                                               # needs sage.combinat sage.groups
                sage: W.canonical_representation()                                      # needs sage.combinat sage.groups
                Finite Coxeter group over Integer Ring with Coxeter matrix:
                [1 3 2]
                [3 1 3]
                [2 3 1]
            '''
        def elements_of_length(self, n):
            """
            Return all elements of length `n`.

            EXAMPLES::

                sage: A = AffinePermutationGroup(['A', 2, 1])                           # needs sage.combinat
                sage: [len(list(A.elements_of_length(i))) for i in [0..5]]              # needs sage.combinat
                [1, 3, 6, 9, 12, 15]

                sage: W = CoxeterGroup(['H', 3])                                        # needs sage.combinat sage.groups
                sage: [len(list(W.elements_of_length(i))) for i in range(4)]            # needs sage.combinat sage.groups
                [1, 3, 5, 7]

                sage: W = CoxeterGroup(['A', 2])                                        # needs sage.combinat sage.groups
                sage: [len(list(W.elements_of_length(i))) for i in range(6)]            # needs sage.combinat sage.groups
                [1, 2, 2, 1, 0, 0]
            """
        def random_element_of_length(self, n):
            """
            Return a random element of length ``n`` in ``self``.

            Starts at the identity, then chooses an upper cover at random.

            Not very uniform: actually constructs a uniformly random
            reduced word of length `n`. Thus we most likely get
            elements with lots of reduced words!

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: A = AffinePermutationGroup(['A', 7, 1])
                sage: p = A.random_element_of_length(10)
                sage: p in A
                True
                sage: p.length() == 10
                True

                sage: # needs sage.combinat sage.groups
                sage: W = CoxeterGroup(['A', 4])
                sage: p = W.random_element_of_length(5)
                sage: p in W
                True
                sage: p.length() == 5
                True
            """
    class ElementMethods:
        def has_descent(self, i, side: str = 'right', positive: bool = False) -> bool:
            """
            Return whether `i` is a (left/right) descent of ``self``.

            See :meth:`.descents` for a description of the options.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0] * s[1] * s[2]
                sage: w.has_descent(2)
                True
                sage: [ w.has_descent(i)                for i in [0,1,2] ]
                [False, False, True]
                sage: [ w.has_descent(i, side='left')   for i in [0,1,2] ]
                [True, False, False]
                sage: [ w.has_descent(i, positive=True) for i in [0,1,2] ]
                [True, True, False]

            This default implementation delegates the work to
            :meth:`.has_left_descent` and :meth:`.has_right_descent`.
            """
        def has_right_descent(self, i) -> bool:
            """
            Return whether `i` is a right descent of ``self``.

            EXAMPLES::

                sage: W = CoxeterGroups().example(); W
                The symmetric group on {0, ..., 3}
                sage: w = W.an_element(); w
                (1, 2, 3, 0)
                sage: w.has_right_descent(0)
                False
                sage: w.has_right_descent(1)
                False
                sage: w.has_right_descent(2)
                True
            """
        def has_left_descent(self, i) -> bool:
            """
            Return whether `i` is a left descent of ``self``.

            This default implementation uses that a left descent of
            `w` is a right descent of `w^{-1}`.

            EXAMPLES::

                sage: W = CoxeterGroups().example(); W
                The symmetric group on {0, ..., 3}
                sage: w = W.an_element(); w
                (1, 2, 3, 0)
                sage: w.has_left_descent(0)
                True
                sage: w.has_left_descent(1)
                False
                sage: w.has_left_descent(2)
                False

            TESTS::

                sage: w.has_left_descent.__module__
                'sage.categories.coxeter_groups'
            """
        def first_descent(self, side: str = 'right', index_set=None, positive: bool = False):
            """
            Return the first left (resp. right) descent of self, as
            an element of ``index_set``, or ``None`` if there is none.

            See :meth:`.descents` for a description of the options.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[2]*s[0]
                sage: w.first_descent()
                0
                sage: w = s[0]*s[2]
                sage: w.first_descent()
                0
                sage: w = s[0]*s[1]
                sage: w.first_descent()
                1
            """
        def descents(self, side: str = 'right', index_set=None, positive: bool = False):
            """
            Return the descents of self, as a list of elements of the
            index_set.

            INPUT:

            - ``index_set`` -- a subset (as a list or iterable) of the nodes of the Dynkin diagram;
              (default: all of them)
            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
            - ``positive`` -- boolean (default: ``False``)

            The ``index_set`` option can be used to restrict to the
            parabolic subgroup indexed by ``index_set``.

            If positive is ``True``, then returns the non-descents
            instead

            .. TODO::

                find a better name for ``positive``: complement? non_descent?

            Caveat: the return type may change to some other iterable
            (tuple, ...) in the future. Please use keyword arguments
            also, as the order of the arguments may change as well.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0]*s[1]
                sage: w.descents()
                [1]
                sage: w = s[0]*s[2]
                sage: w.descents()
                [0, 2]

            .. TODO:: side, index_set, positive
            """
        def is_grassmannian(self, side: str = 'right') -> bool:
            """
            Return whether ``self`` is Grassmannian.

            INPUT:

            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)

            An element is Grassmannian if it has at
            most one descent on the right (resp. on the left).

            EXAMPLES::

                sage: W = CoxeterGroups().example(); W
                The symmetric group on {0, ..., 3}
                sage: s = W.simple_reflections()
                sage: W.one().is_grassmannian()
                True
                sage: s[1].is_grassmannian()
                True
                sage: (s[1]*s[2]).is_grassmannian()
                True
                sage: (s[0]*s[1]).is_grassmannian()
                True
                sage: (s[1]*s[2]*s[1]).is_grassmannian()
                False

                sage: (s[0]*s[2]*s[1]).is_grassmannian(side='left')
                False
                sage: (s[0]*s[2]*s[1]).is_grassmannian(side='right')
                True
                sage: (s[0]*s[2]*s[1]).is_grassmannian()
                True
            """
        def is_fully_commutative(self) -> bool:
            """
            Check if ``self`` is a fully-commutative element.

            We use the characterization that an element `w` in a Coxeter
            system `(W,S)` is fully-commutative if and only if for every pair
            of generators `s,t \\in S` for which `m(s,t)>2`, no reduced
            word of `w` contains the 'braid' word `sts...` of length
            `m(s,t)` as a contiguous subword. See [Ste1996]_.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = CoxeterGroup(['A', 3])
                sage: len([1 for w in W if w.is_fully_commutative()])
                14
                sage: W = CoxeterGroup(['B', 3])
                sage: len([1 for w in W if w.is_fully_commutative()])
                24

            TESTS::

                sage: W = CoxeterGroup(matrix(2,2,[1,7,7,1]), index_set='ab')           # needs sage.combinat sage.groups
                sage: len([1 for w in W if w.is_fully_commutative()])                   # needs sage.combinat sage.groups
                13
            """
        def reduced_word_reverse_iterator(self) -> Generator[Incomplete]:
            """
            Return a reverse iterator on a reduced word for ``self``.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: sigma = s[0]*s[1]*s[2]
                sage: rI=sigma.reduced_word_reverse_iterator()
                sage: [i for i in rI]
                [2, 1, 0]
                sage: s[0]*s[1]*s[2]==sigma
                True
                sage: sigma.length()
                3

            .. SEEALSO::

                :meth:`.reduced_word`

            Default implementation: recursively remove the first right
            descent until the identity is reached (see :meth:`.first_descent` and
            :meth:`~sage.categories.complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups.ElementMethods.apply_simple_reflection`).
            """
        def reduced_word(self):
            """
            Return a reduced word for ``self``.

            This is a word `[i_1,i_2,\\ldots,i_k]` of minimal length
            such that
            `s_{i_1} s_{i_2} \\cdots s_{i_k} = \\operatorname{self}`,
            where the `s_i` are the simple reflections.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0]*s[1]*s[2]
                sage: w.reduced_word()
                [0, 1, 2]
                sage: w = s[0]*s[2]
                sage: w.reduced_word()
                [2, 0]

            .. SEEALSO::

                - :meth:`.reduced_words`, :meth:`.reduced_word_reverse_iterator`,
                - :meth:`length`, :meth:`reduced_word_graph`
            """
        def reduced_words_iter(self):
            """
            Iterate over all reduced words for ``self``.

            See :meth:`reduced_word` for the definition of a reduced
            word.

            The algorithm uses the Matsumoto property that any two
            reduced expressions are related by braid relations, see
            Theorem 3.3.1(ii) in [BB2005]_.

            .. SEEALSO::

                :meth:`braid_orbit_iter`

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0] * s[2]
                sage: sorted(w.reduced_words_iter())                                    # needs sage.combinat sage.graphs
                [[0, 2], [2, 0]]
            """
        def reduced_words(self):
            '''
            Return all reduced words for ``self``.

            See :meth:`reduced_word` for the definition of a reduced
            word.

            The algorithm uses the Matsumoto property that any two
            reduced expressions are related by braid relations, see
            Theorem 3.3.1(ii) in [BB2005]_.

            .. SEEALSO::

                :meth:`braid_orbit`

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0] * s[2]
                sage: sorted(w.reduced_words())                                         # needs sage.graphs sage.modules
                [[0, 2], [2, 0]]

                sage: W = WeylGroup([\'E\', 6])                                           # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([2,3,4,2])                                # needs sage.combinat sage.groups
                sage: sorted(w.reduced_words())                                         # needs sage.combinat sage.groups
                [[2, 3, 4, 2], [3, 2, 4, 2], [3, 4, 2, 4]]

                sage: # optional - gap3, needs sage.combinat sage.groups
                sage: W = ReflectionGroup([\'A\',3],
                ....:                     index_set=["AA","BB","5"])
                sage: w = W.long_element()
                sage: w.reduced_words()
                [[\'BB\', \'5\', \'AA\', \'BB\', \'5\', \'AA\'],
                 [\'5\', \'BB\', \'5\', \'AA\', \'BB\', \'5\'],
                 [\'BB\', \'AA\', \'BB\', \'5\', \'BB\', \'AA\'],
                 [\'AA\', \'5\', \'BB\', \'AA\', \'5\', \'BB\'],
                 [\'5\', \'AA\', \'BB\', \'AA\', \'5\', \'BB\'],
                 [\'AA\', \'BB\', \'5\', \'AA\', \'BB\', \'AA\'],
                 [\'AA\', \'BB\', \'AA\', \'5\', \'BB\', \'AA\'],
                 [\'AA\', \'BB\', \'5\', \'BB\', \'AA\', \'BB\'],
                 [\'BB\', \'AA\', \'5\', \'BB\', \'AA\', \'5\'],
                 [\'BB\', \'5\', \'AA\', \'BB\', \'AA\', \'5\'],
                 [\'AA\', \'5\', \'BB\', \'5\', \'AA\', \'BB\'],
                 [\'5\', \'BB\', \'AA\', \'5\', \'BB\', \'5\'],
                 [\'5\', \'BB\', \'AA\', \'BB\', \'5\', \'BB\'],
                 [\'5\', \'AA\', \'BB\', \'5\', \'AA\', \'BB\'],
                 [\'BB\', \'5\', \'BB\', \'AA\', \'BB\', \'5\'],
                 [\'BB\', \'AA\', \'5\', \'BB\', \'5\', \'AA\']]

            .. TODO::

                The result should be full featured finite enumerated set
                (e.g., counting can be done much faster than iterating).

            .. SEEALSO::

                :meth:`.reduced_word`, :meth:`.reduced_word_reverse_iterator`,
                :meth:`length`, :meth:`reduced_word_graph`
            '''
        def support(self):
            """
            Return the support of ``self``, that is the simple reflections that
            appear in the reduced expressions of ``self``.

            OUTPUT: the support of ``self`` as a set of integers

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: w = W.from_reduced_word([1,2,1])
                sage: w.support()
                {1, 2}
            """
        def has_full_support(self) -> bool:
            """
            Return whether ``self`` has full support.

            An element is said to have full support if its support contains
            all simple reflections.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: w = W.from_reduced_word([1,2,1])
                sage: w.has_full_support()
                False
                sage: w = W.from_reduced_word([1,2,1,0,1])
                sage: w.has_full_support()
                True
            """
        def reduced_word_graph(self):
            """
            Return the reduced word graph of ``self``.

            The reduced word graph of an element `w` in a Coxeter group
            is the graph whose vertices are the reduced words for `w`
            (see :meth:`reduced_word` for a definition of this term),
            and which has an `m`-colored edge between two reduced words
            `x` and `y` whenever `x` and `y` differ by exactly one
            length-`m` braid move (with `m \\geq 2`).

            This graph is always connected (a theorem due to Tits) and
            has no multiple edges.

            EXAMPLES::

                sage: # needs sage.combinat sage.graphs sage.groups
                sage: W = WeylGroup(['A', 3], prefix='s')
                sage: w0 = W.long_element()
                sage: G = w0.reduced_word_graph()
                sage: G.num_verts()
                16
                sage: len(w0.reduced_words())
                16
                sage: G.num_edges()
                18
                sage: len([e for e in G.edges(sort=False) if e[2] == 2])
                10
                sage: len([e for e in G.edges(sort=False) if e[2] == 3])
                8

            TESTS::

                sage: p = Permutation([3,2,4,1])
                sage: pp = WeylGroup(['A',3]).from_reduced_word(p.reduced_word())       # needs sage.combinat sage.groups
                sage: pp.reduced_word_graph()                                           # needs sage.combinat sage.graphs sage.groups
                Graph on 3 vertices

                sage: # needs sage.combinat sage.graphs sage.groups
                sage: w1 = W.one()
                sage: G = w1.reduced_word_graph()
                sage: G.num_verts()
                1
                sage: G.num_edges()
                0

            .. SEEALSO::

                :meth:`.reduced_words`, :meth:`.reduced_word_reverse_iterator`,
                :meth:`length`, :meth:`reduced_word`
            """
        def length(self):
            """
            Return the length of ``self``.

            This is the minimal length of
            a product of simple reflections giving ``self``.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: s1 = W.simple_reflection(1)
                sage: s2 = W.simple_reflection(2)
                sage: s1.length()
                1
                sage: (s1*s2).length()
                2
                sage: W = CoxeterGroups().example()
                sage: s = W.simple_reflections()
                sage: w = s[0]*s[1]*s[0]
                sage: w.length()
                3
                sage: W = CoxeterGroups().example()
                sage: R.<x> = ZZ[]
                sage: s = sum(x^w.length() for w in W)
                sage: p = prod(sum(x^i for i in range(j)) for j in range(1, 5))
                sage: s - p
                0

            .. SEEALSO::

                :meth:`.reduced_word`

            .. TODO::

                Should use reduced_word_iterator (or reverse_iterator)
            """
        def reflection_length(self):
            """
            Return the reflection length of ``self``.

            The reflection length is the length of the shortest expression
            of the element as a product of reflections.

            .. SEEALSO::

                :meth:`absolute_length`

            EXAMPLES::

                sage: W = WeylGroup(['A', 3])                                           # needs sage.combinat sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.combinat sage.groups
                sage: (s[1]*s[2]*s[3]).reflection_length()                              # needs sage.combinat sage.groups
                3

                sage: W = SymmetricGroup(4)                                             # needs sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.groups
                sage: (s[3]*s[2]*s[3]).reflection_length()                              # needs sage.combinat sage.groups
                1
            """
        def absolute_length(self):
            '''
            Return the absolute length of ``self``.

            The absolute length is the length of the shortest expression
            of the element as a product of reflections. In general,
            we use Theorem 1.1 in [Dy2001]_.

            .. SEEALSO::

                :meth:`absolute_le`,
                :meth:`absolute_chain`

            EXAMPLES::

                sage: W = WeylGroup(["A", 3])                                           # needs sage.combinat sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.combinat sage.groups
                sage: (s[1]*s[2]*s[3]).absolute_length()                                # needs sage.combinat sage.groups
                3

                sage: W = SymmetricGroup(4)                                             # needs sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.groups
                sage: (s[3]*s[2]*s[1]).absolute_length()                                # needs sage.combinat sage.groups
                3

                sage: W = CoxeterGroup(["A",2,1])
                sage: (r, s, t) = W.simple_reflections()
                sage: (r * s * r * t).absolute_length()
                2
                sage: W.one().absolute_length()
                0
                sage: r.absolute_length()
                1
                sage: (r * s).absolute_length()
                2
                sage: (r * s * r).absolute_length()
                1
                sage: W = CoxeterGroup([\'A\', 3, 1])
                sage: (r, s, t, u) = W.simple_reflections()
                sage: (r * s * t * u).absolute_length()
                4
                sage: (r * s * t * u * s).absolute_length()
                3
            '''
        def absolute_chain(self):
            """
            Return a (saturated) chain in absolute order from ``1``
            to ``self``.

            .. SEEALSO::

                :meth:`absolute_chain_reflections`

            EXAMPLES::

                sage: W = CoxeterGroup(['A', 2, 1])
                sage: (r, s, t) = W.simple_reflections()
                sage: (r * s * r * t).absolute_chain()
                [
                [1 0 0]  [ 0 -1  2]  [ 2  1 -2]
                [0 1 0]  [-1  0  2]  [ 1  2 -2]
                [0 0 1], [ 0  0  1], [ 1  1 -1]
                ]
            """
        def absolute_chain_reflections(self):
            '''
            Return a list of reflection which, when (left) multiplied in order,
            give ``self``.

            This method is based on Theorem 1.1 in [Dy2001]_, combined with
            the strong exchange condition. As an example, if `W` is a type
            `A_2` Coxeter group with simple reflections `a`, `b`, then the
            absolute chain reflections for the element `w = ab` is the list
            `[a, aba]` as `w = (aba) a = ab`.

            .. SEEALSO::

                :meth:`absolute_length`,
                :meth:`absolute_chain`

            EXAMPLES::

                sage: W = CoxeterGroup(["A",2,1])
                sage: W.one().absolute_chain_reflections()
                []
                sage: (r, s, t) = W.simple_reflections()
                sage: r.absolute_chain_reflections()
                [
                [-1  1  1]
                [ 0  1  0]
                [ 0  0  1]
                ]
                sage: (r * s).absolute_chain_reflections()
                [
                [-1  1  1]  [ 0 -1  2]
                [ 0  1  0]  [-1  0  2]
                [ 0  0  1], [ 0  0  1]
                ]
                sage: (r * s * r * t).absolute_chain_reflections()
                [
                [ 0 -1  2]  [-1 -2  4]
                [-1  0  2]  [-2 -1  4]
                [ 0  0  1], [-1 -1  3]
                ]
                sage: W = CoxeterGroup([\'A\', 3, 1])
                sage: (r, s, t, u) = W.simple_reflections()
                sage: (r * s * t * u).absolute_chain_reflections()
                [
                [-1  1  0  1]  [ 0 -1  1  1]  [ 0  0 -1  2]  [-3  2  0  2]
                [ 0  1  0  0]  [-1  0  1  1]  [-1  1 -1  2]  [-2  2  0  1]
                [ 0  0  1  0]  [ 0  0  1  0]  [-1  0  0  2]  [-2  1  1  1]
                [ 0  0  0  1], [ 0  0  0  1], [ 0  0  0  1], [-2  1  0  2]
                ]
                sage: (r * s * t * u * s).absolute_chain_reflections()
                [
                [-1  1  0  1]  [ 0  0 -1  2]  [-3  2  0  2]
                [ 0  1  0  0]  [-1  1 -1  2]  [-2  2  0  1]
                [ 0  0  1  0]  [-1  0  0  2]  [-2  1  1  1]
                [ 0  0  0  1], [ 0  0  0  1], [-2  1  0  2]
                ]
            '''
        def absolute_le(self, other):
            '''
            Return whether ``self`` is smaller than ``other`` in the absolute
            order.

            A general reflection is an element of the form `w s_i w^{-1}`,
            where `s_i` is a simple reflection. The absolute order is defined
            analogously to the weak order but using general reflections rather
            than just simple reflections.

            This partial order can be used to define noncrossing partitions
            associated with this Coxeter group.

            .. SEEALSO::

                :meth:`absolute_length`

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 3])
                sage: s = W.simple_reflections()
                sage: w0 = s[1]
                sage: w1 = s[1]*s[2]*s[3]
                sage: w0.absolute_le(w1)
                True
                sage: w1.absolute_le(w0)
                False
                sage: w1.absolute_le(w1)
                True

            TESTS:

            Check that this is independent of the implementation of the group, see :issue:`34799`::

                sage: # needs sage.combinat sage.groups
                sage: W1 = WeylGroup([\'A\', 2])
                sage: W2 = Permutations(3)
                sage: P = lambda pi: W2(list(pi.to_permutation()))
                sage: d1 = set((P(w1), P(w2)) for w1 in W1 for w2 in W1
                ....:                         if w1.absolute_le(w2))
                sage: d2 = set((w1, w2) for w1 in W2 for w2 in W2
                ....:                   if w1.absolute_le(w2))
                sage: d1 == d2
                True
                sage: sage.combinat.permutation.Permutations.options.mult = "r2l"
                sage: d3 = set((w1, w2)
                ....:          for w1 in W2 for w2 in W2 if w1.absolute_le(w2))
                sage: d1 == d3
                True
                sage: sage.combinat.permutation.Permutations.options._reset()

                sage: # needs sage.combinat sage.groups
                sage: W1 = WeylGroup([\'B\', 2])
                sage: W2 = SignedPermutations(2)
                sage: P = lambda pi: W2(list(pi.to_permutation()))
                sage: d1 = set((P(w1), P(w2))
                ....:          for w1 in W1 for w2 in W1 if w1.absolute_le(w2))
                sage: d2 = set((w1, w2)
                ....:          for w1 in W2 for w2 in W2 if w1.absolute_le(w2))
                sage: d1 == d2
                True
            '''
        def absolute_covers(self) -> Generator[Incomplete]:
            '''
            Return the list of covers of ``self`` in absolute order.

            .. SEEALSO::

                :meth:`absolute_length`

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 3])
                sage: s = W.simple_reflections()
                sage: w0 = s[1]
                sage: w1 = s[1]*s[2]*s[3]
                sage: list(w0.absolute_covers())
                [
                [0 0 1 0]  [0 1 0 0]  [0 1 0 0]  [0 0 0 1]  [0 1 0 0]
                [1 0 0 0]  [1 0 0 0]  [0 0 1 0]  [1 0 0 0]  [0 0 0 1]
                [0 1 0 0]  [0 0 0 1]  [1 0 0 0]  [0 0 1 0]  [0 0 1 0]
                [0 0 0 1], [0 0 1 0], [0 0 0 1], [0 1 0 0], [1 0 0 0]
                ]
            '''
        def canonical_matrix(self):
            '''
            Return the matrix of ``self`` in the canonical faithful
            representation.

            This is an `n`-dimension real faithful essential representation,
            where `n` is the number of generators of the Coxeter group.
            Note that this is not always the most natural matrix
            representation, for instance in type `A_n`.

            EXAMPLES::

                sage: W = WeylGroup(["A", 3])                                           # needs sage.combinat sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.combinat sage.groups
                sage: (s[1]*s[2]*s[3]).canonical_matrix()                               # needs sage.combinat sage.groups
                [ 0  0 -1]
                [ 1  0 -1]
                [ 0  1 -1]
            '''
        def coset_representative(self, index_set, side: str = 'right'):
            """
            Return the unique shortest element of the Coxeter group
            `W` which is in the same left (resp. right) coset as
            ``self``, with respect to the parabolic subgroup `W_I`.

            INPUT:

            - ``index_set`` -- a subset (or iterable) of the nodes of the Dynkin diagram
            - ``side`` -- ``'left'`` or ``'right'``

            EXAMPLES::

                sage: W = CoxeterGroups().example(5)
                sage: s = W.simple_reflections()
                sage: w = s[2]*s[1]*s[3]
                sage: w.coset_representative([]).reduced_word()
                [2, 3, 1]
                sage: w.coset_representative([1]).reduced_word()
                [2, 3]
                sage: w.coset_representative([1,2]).reduced_word()
                [2, 3]
                sage: w.coset_representative([1,3]               ).reduced_word()
                [2]
                sage: w.coset_representative([2,3]               ).reduced_word()
                [2, 1]
                sage: w.coset_representative([1,2,3]             ).reduced_word()
                []
                sage: w.coset_representative([],      side='left').reduced_word()
                [2, 3, 1]
                sage: w.coset_representative([1],     side='left').reduced_word()
                [2, 3, 1]
                sage: w.coset_representative([1,2],   side='left').reduced_word()
                [3]
                sage: w.coset_representative([1,3],   side='left').reduced_word()
                [2, 3, 1]
                sage: w.coset_representative([2,3],   side='left').reduced_word()
                [1]
                sage: w.coset_representative([1,2,3], side='left').reduced_word()
                []
            """
        def apply_simple_projection(self, i, side: str = 'right', length_increasing: bool = True):
            """
            Return the result of the application of the simple
            projection `\\pi_i` (resp. `\\overline\\pi_i`) on ``self``.

            INPUT:

            - ``i`` -- an element of the index set of the Coxeter group
            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
            - ``length_increasing`` -- boolean (default: ``True``);
              specifying the direction of the projection

            See :meth:`CoxeterGroups.ParentMethods.simple_projections`
            for the definition of the simple projections.

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: w = W.an_element()
                sage: w
                (1, 2, 3, 0)
                sage: w.apply_simple_projection(2)
                (1, 2, 3, 0)
                sage: w.apply_simple_projection(2, length_increasing=False)
                (1, 2, 0, 3)

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['C', 4], prefix='s')
                sage: v = W.from_reduced_word([1,2,3,4,3,1])
                sage: v
                s1*s2*s3*s4*s3*s1
                sage: v.apply_simple_projection(2)
                s1*s2*s3*s4*s3*s1*s2
                sage: v.apply_simple_projection(2, side='left')
                s1*s2*s3*s4*s3*s1
                sage: v.apply_simple_projection(1, length_increasing=False)
                s1*s2*s3*s4*s3
            """
        def binary_factorizations(self, predicate=...):
            '''
            Return the set of all the factorizations `self = u v` such
            that `l(self) = l(u) + l(v)`.

            Iterating through this set is Constant Amortized Time
            (counting arithmetic operations in the Coxeter group as
            constant time) complexity, and memory linear in the length
            of ``self``.

            One can pass as optional argument a predicate p such that
            `p(u)` implies `p(u\')` for any `u` left factor of ``self``
            and `u\'` left factor of `u`. Then this returns only the
            factorizations `self = uv` such `p(u)` holds.

            EXAMPLES:

            We construct the set of all factorizations of the maximal
            element of the group::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup([\'A\', 3])
                sage: s = W.simple_reflections()
                sage: w0 = W.from_reduced_word([1,2,3,1,2,1])
                sage: w0.binary_factorizations().cardinality()
                24

            The same number of factorizations, by bounded length::

                sage: [w0.binary_factorizations(                                        # needs sage.combinat sage.groups
                ....:      lambda u: u.length() <= l
                ....:  ).cardinality()
                ....:  for l in [-1,0,1,2,3,4,5,6]]
                [0, 1, 4, 9, 15, 20, 23, 24]

            The number of factorizations of the elements just below
            the maximal element::

                sage: [(s[i]*w0).binary_factorizations().cardinality()                  # needs sage.combinat sage.groups
                ....:  for i in [1,2,3]]
                [12, 12, 12]
                sage: w0.binary_factorizations(lambda u: False).cardinality()           # needs sage.combinat sage.groups
                0

            TESTS::

                sage: w0.binary_factorizations().category()                             # needs sage.combinat sage.groups
                Category of finite enumerated sets

            Check that this is independent of the implementation of the group, see :issue:`34799`::

                sage: # needs sage.combinat sage.groups
                sage: W1 = WeylGroup([\'A\', 3])
                sage: W2 = Permutations(4)
                sage: P = lambda pi: W2(list(pi.to_permutation()))
                sage: d1 = {P(pi): set((P(w[0]), P(w[1]))
                ....:                  for w in pi.binary_factorizations())
                ....:       for pi in W1}
                sage: d2 = {pi: set(pi.binary_factorizations()) for pi in W2}
                sage: d1 == d2
                True
                sage: sage.combinat.permutation.Permutations.options.mult = "r2l"
                sage: d3 = {pi: set(pi.binary_factorizations()) for pi in W2}
                sage: d1 == d3
                True
                sage: sage.combinat.permutation.Permutations.options._reset()
            '''
        @cached_in_parent_method
        def bruhat_lower_covers(self):
            '''
            Return all elements that ``self`` covers in (strong) Bruhat order.

            If ``w = self`` has a descent at `i`, then the elements that
            `w` covers are exactly `\\{ws_i, u_1s_i, u_2s_i,..., u_js_i\\}`,
            where the `u_k` are elements that `ws_i` covers that also
            do not have a descent at `i`.

            EXAMPLES::

                sage: W = WeylGroup(["A", 3])                                           # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,2,3])                                  # needs sage.combinat sage.groups
                sage: print([v.reduced_word() for v in w.bruhat_lower_covers()])        # needs sage.combinat sage.groups
                [[3, 2], [2, 3]]

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 3])
                sage: print([v.reduced_word()
                ....:        for v in W.simple_reflection(1).bruhat_lower_covers()])
                [[]]
                sage: print([v.reduced_word()
                ....:        for v in W.one().bruhat_lower_covers()])
                []
                sage: W = WeylGroup(["B", 4, 1])
                sage: w = W.from_reduced_word([0,2])
                sage: print([v.reduced_word() for v in w.bruhat_lower_covers()])
                [[2], [0]]
                sage: W = WeylGroup("A3", prefix=\'s\', implementation=\'permutation\')
                sage: s1, s2, s3 = W.simple_reflections()
                sage: (s1*s2*s3*s1).bruhat_lower_covers()
                [s2*s1*s3, s1*s2*s1, s1*s2*s3]

            We now show how to construct the Bruhat poset::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 3])
                sage: covers = tuple([u, v]
                ....:                for v in W for u in v.bruhat_lower_covers())
                sage: P = Poset((W, covers), cover_relations=True)                      # needs sage.graphs
                sage: P.show()                                                          # needs sage.graphs sage.plot

            Alternatively, one can just use::

                sage: P = W.bruhat_poset()                                              # needs sage.combinat sage.graphs sage.groups

            The algorithm is taken from Stembridge\'s \'coxeter/weyl\' package for Maple.
            '''
        @cached_in_parent_method
        def bruhat_upper_covers(self):
            """
            Return all elements that cover ``self`` in (strong) Bruhat order.

            The algorithm works recursively, using the 'inverse' of the method described for
            lower covers :meth:`bruhat_lower_covers`. Namely, it runs through all `i` in the
            index set. Let `w` equal ``self``. If `w` has no right descent `i`, then `w s_i` is a cover;
            if `w` has a decent at `i`, then `u_j s_i` is a cover of `w` where `u_j` is a cover
            of `w s_i`.

            EXAMPLES::

                sage: W = WeylGroup(['A', 3, 1], prefix='s')                            # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([1,2,1])                                  # needs sage.combinat sage.groups
                sage: w.bruhat_upper_covers()                                           # needs sage.combinat sage.groups
                [s1*s2*s1*s0, s1*s2*s0*s1, s0*s1*s2*s1, s3*s1*s2*s1, s2*s3*s1*s2, s1*s2*s3*s1]

                sage: W = WeylGroup(['A', 3])                                           # needs sage.combinat sage.groups
                sage: w = W.long_element()                                              # needs sage.combinat sage.groups
                sage: w.bruhat_upper_covers()                                           # needs sage.combinat sage.groups
                []

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 3])
                sage: w = W.from_reduced_word([1,2,1])
                sage: S = [v for v in W if w in v.bruhat_lower_covers()]
                sage: C = w.bruhat_upper_covers()
                sage: set(S) == set(C)
                True
            """
        @cached_in_parent_method
        def bruhat_lower_covers_reflections(self):
            """
            Return all 2-tuples of lower_covers and reflections (``v``, ``r``) where ``v`` is covered by ``self`` and ``r`` is the reflection such that ``self`` = ``v`` ``r``.

            ALGORITHM:

            See :meth:`.bruhat_lower_covers`

            EXAMPLES::

                sage: W = WeylGroup(['A', 3], prefix='s')                               # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,1,2,1])                                # needs sage.combinat sage.groups
                sage: w.bruhat_lower_covers_reflections()                               # needs sage.combinat sage.groups
                [(s1*s2*s1, s1*s2*s3*s2*s1), (s3*s2*s1, s2), (s3*s1*s2, s1)]

            TESTS:

            Check bug discovered in :issue:`32669` is fixed::

                sage: W = CoxeterGroup(['A', 3], implementation='permutation')          # needs sage.combinat sage.groups
                sage: W.w0.bruhat_lower_covers_reflections()                            # needs sage.combinat sage.groups
                [((1,3,7,9)(2,11,6,10)(4,8,5,12), (2,5)(3,9)(4,6)(8,11)(10,12)),
                 ((1,11)(3,10)(4,9)(5,7)(6,12), (1,4)(2,8)(3,5)(7,10)(9,11)),
                 ((1,9,7,3)(2,10,6,11)(4,12,5,8), (1,7)(2,4)(5,6)(8,10)(11,12))]
            """
        def lower_cover_reflections(self, side: str = 'right'):
            """
            Return the reflections ``t`` such that ``self`` covers ``self`` ``t``.

            If ``side`` is 'left', ``self`` covers ``t`` ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 3],prefix='s')
                sage: w = W.from_reduced_word([3,1,2,1])
                sage: w.lower_cover_reflections()
                [s1*s2*s3*s2*s1, s2, s1]
                sage: w.lower_cover_reflections(side='left')
                [s2*s3*s2, s3, s1]
            """
        @cached_in_parent_method
        def bruhat_upper_covers_reflections(self):
            """
            Return all 2-tuples of covers and reflections (``v``, ``r``) where ``v`` covers ``self`` and ``r`` is the reflection such that ``self`` = ``v`` ``r``.

            ALGORITHM:

            See :meth:`.bruhat_upper_covers`

            EXAMPLES::

                sage: W = WeylGroup(['A', 4], prefix='s')                               # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,1,2,1])                                # needs sage.combinat sage.groups
                sage: w.bruhat_upper_covers_reflections()                               # needs sage.combinat sage.groups
                [(s1*s2*s3*s2*s1, s3), (s2*s3*s1*s2*s1, s2*s3*s2),
                 (s3*s4*s1*s2*s1, s4), (s4*s3*s1*s2*s1, s1*s2*s3*s4*s3*s2*s1)]
            """
        def cover_reflections(self, side: str = 'right'):
            """
            Return the set of reflections ``t`` such that ``self`` ``t`` covers ``self``.

            If ``side`` is 'left', ``t`` ``self`` covers ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 4], prefix='s')
                sage: w = W.from_reduced_word([3,1,2,1])
                sage: w.cover_reflections()
                [s3, s2*s3*s2, s4, s1*s2*s3*s4*s3*s2*s1]
                sage: w.cover_reflections(side='left')
                [s4, s2, s1*s2*s1, s3*s4*s3]
            """
        @cached_in_parent_method
        def bruhat_le(self, other):
            '''
            Return whether ``self`` <= ``other`` in the Bruhat order.

            INPUT:

            - ``other`` -- an element of the same Coxeter group

            OUTPUT: boolean

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 3])
                sage: u = W.from_reduced_word([1,2,1])
                sage: v = W.from_reduced_word([1,2,3,2,1])
                sage: u.bruhat_le(u)
                True
                sage: u.bruhat_le(v)
                True
                sage: v.bruhat_le(u)
                False
                sage: v.bruhat_le(v)
                True
                sage: s = W.simple_reflections()
                sage: s[1].bruhat_le(W.one())
                False

            The implementation uses the equivalent condition that any
            reduced word for ``other`` contains a reduced word for
            ``self`` as subword. See Stembridge, A short derivation of
            the Möbius function for the Bruhat order. J. Algebraic
            Combinatoric 25 (2007), no. 2, 141--148, Proposition 1.1.

            Complexity: `O(l * c)`, where `l` is the minimum of the
            lengths of `u` and of `v`, and `c` is the cost of the low
            level methods :meth:`first_descent`, :meth:`has_descent`,
            :meth:`~sage.categories.complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups.ElementMethods.apply_simple_reflection`),
            etc. Those are typically `O(n)`, where `n` is the rank of the
            Coxeter group.

            TESTS:

            We now run consistency tests with permutations and
            :meth:`bruhat_lower_covers`::

                sage: W = WeylGroup(["A", 3])                                           # needs sage.combinat sage.groups
                sage: P4 = Permutations(4)
                sage: def P4toW(w): return W.from_reduced_word(w.reduced_word())
                sage: for u in P4:                                                      # needs sage.combinat sage.groups
                ....:     for v in P4:
                ....:         assert u.bruhat_lequal(v) == P4toW(u).bruhat_le(P4toW(v))

                sage: # needs sage.combinat sage.graphs sage.groups
                sage: W = WeylGroup(["B", 3])
                sage: P = W.bruhat_poset()  # This is built from bruhat_lower_covers
                sage: Q = Poset((W, attrcall("bruhat_le")))     # long time (10s)
                sage: all(u.bruhat_le(v) == P.is_lequal(u,v)    # long time (7s)
                ....:     for u in W for v in W)
                True
                sage: all(P.is_lequal(u,v) == Q.is_lequal(u,v)  # long time (9s)
                ....:     for u in W for v in W)
                True
            '''
        @cached_in_parent_method
        def weak_le(self, other, side: str = 'right'):
            '''
            Perform the comparison between ``self`` and ``other`` in
            weak (Bruhat) order.

            INPUT:

            - ``other`` -- an element of the same Coxeter group
            - ``side`` -- string (default: ``\'right\'``); ``\'left\'`` or ``\'right\'``

            OUTPUT: boolean

            This returns whether `u \\leq v`, where `u` is ``self`` and `v`
            is ``other``, in left (resp. right) weak order, that is if `v`
            can be obtained from `u` by length increasing multiplication by
            simple reflections on the left (resp. right).

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(["A", 3])
                sage: u = W.from_reduced_word([1,2])
                sage: v = W.from_reduced_word([1,2,3,2])
                sage: u.weak_le(u)
                True
                sage: u.weak_le(v)
                True
                sage: v.weak_le(u)
                False
                sage: v.weak_le(v)
                True

            Comparison for left weak order is achieved with the option ``side``::

                sage: u.weak_le(v, side=\'left\')                                         # needs sage.combinat sage.groups
                False

            The implementation uses the equivalent condition that any
            reduced word for `u` is a right (resp. left) prefix of
            some reduced word for `v`.

            Complexity: `O(l * c)`, where `l` is the minimum of the
            lengths of `u` and of `v`, and `c` is the cost of the low
            level methods :meth:`first_descent`, :meth:`has_descent`,
            :meth:`~sage.categories.complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups.ElementMethods.apply_simple_reflection`),
            etc. Those are typically `O(n)`, where `n` is the rank of the
            Coxeter group.

            We now run consistency tests with permutations::

                sage: W = WeylGroup(["A", 3])                                           # needs sage.combinat sage.groups
                sage: P4 = Permutations(4)
                sage: def P4toW(w): return W.from_reduced_word(w.reduced_word())
                sage: for u in P4:              # long time (5s on sage.math, 2011), needs sage.combinat sage.groups
                ....:     for v in P4:
                ....:         assert u.permutohedron_lequal(v) == P4toW(u).weak_le(P4toW(v))
                ....:         assert u.permutohedron_lequal(v, side=\'left\') == P4toW(u).weak_le(P4toW(v), side=\'left\')
            '''
        def weak_covers(self, side: str = 'right', index_set=None, positive: bool = False):
            """
            Return all elements that ``self`` covers in weak order.

            INPUT:

            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
            - ``positive`` -- boolean (default: ``False``)
            - ``index_set`` -- list of indices or None

            OUTPUT: list

            EXAMPLES::

                sage: W = WeylGroup(['A', 3])                                           # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,2,1])                                  # needs sage.combinat sage.groups
                sage: [x.reduced_word() for x in w.weak_covers()]                       # needs sage.combinat sage.groups
                [[3, 2]]

            To obtain instead elements that cover self, set ``positive=True``::

                sage: [x.reduced_word() for x in w.weak_covers(positive=True)]          # needs sage.combinat sage.groups
                [[3, 1, 2, 1], [2, 3, 2, 1]]

            To obtain covers for left weak order, set the option side to 'left'::

                sage: # needs sage.combinat sage.groups
                sage: [x.reduced_word() for x in w.weak_covers(side='left')]
                [[2, 1]]
                sage: w = W.from_reduced_word([3,2,3,1])
                sage: [x.reduced_word() for x in w.weak_covers()]
                [[2, 3, 2], [3, 2, 1]]
                sage: [x.reduced_word() for x in w.weak_covers(side='left')]
                [[3, 2, 1], [2, 3, 1]]

            Covers w.r.t. a parabolic subgroup are obtained with the option ``index_set``::

                sage: [x.reduced_word() for x in w.weak_covers(index_set=[1,2])]        # needs sage.combinat sage.groups
                [[2, 3, 2]]
            """
        def coxeter_sorting_word(self, c):
            """
            Return the ``c``-sorting word of ``self``.

            For a Coxeter element `c` and an element `w`, the `c`-sorting
            word of `w` is the lexicographic minimal reduced expression of
            `w` in the infinite word `c^\\infty`.

            INPUT:

            - ``c`` -- a Coxeter element

            OUTPUT: the ``c``-sorting word of ``self`` as a list of integers

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: c = W.from_reduced_word([0,2,1])
                sage: w = W.from_reduced_word([1,2,1,0,1])
                sage: w.coxeter_sorting_word(c)
                [2, 1, 2, 0, 1]
            """
        def is_coxeter_sortable(self, c, sorting_word=None):
            """
            Return whether ``self`` is ``c``-sortable.

            Given a Coxeter element `c`, an element `w` is `c`-sortable if
            its `c`-sorting word decomposes into a sequence of weakly
            decreasing subwords of `c`.

            INPUT:

            - ``c`` -- a Coxeter element
            - ``sorting_word`` -- sorting word (default: ``None``); used to
              not recompute the `c`-sorting word if already computed

            EXAMPLES::

                sage: W = CoxeterGroups().example()
                sage: c = W.from_reduced_word([0,2,1])
                sage: w = W.from_reduced_word([1,2,1,0,1])
                sage: w.coxeter_sorting_word(c)
                [2, 1, 2, 0, 1]
                sage: w.is_coxeter_sortable(c)
                False
                sage: w = W.from_reduced_word([0,2,1,0,2])
                sage: w.coxeter_sorting_word(c)
                [2, 0, 1, 2, 0]
                sage: w.is_coxeter_sortable(c)
                True

                sage: W = CoxeterGroup(['A', 3])                                        # needs sage.combinat sage.groups
                sage: c = W.from_reduced_word([1,2,3])                                  # needs sage.combinat sage.groups

            Number of `c`-sortable elements in `A_3` (Catalan number)::

                sage: len([w for w in W if w.is_coxeter_sortable(c)])                   # needs sage.rings.number_field
                14

            TESTS::

                sage: W = SymmetricGroup(3)                                             # needs sage.groups
                sage: c = Permutation((1,2,3))
                sage: sorted(w for w in W if w.is_coxeter_sortable(c))                  # needs sage.combinat sage.groups
                [(), (2,3), (1,2), (1,3,2), (1,3)]
            """
        def apply_demazure_product(self, element, side: str = 'right', length_increasing: bool = True):
            """
            Return the Demazure or 0-Hecke product of ``self`` with another Coxeter group element.

            See :meth:`CoxeterGroups.ParentMethods.simple_projections`.

            INPUT:

            - ``element`` -- either an element of the same Coxeter
                group as ``self`` or a tuple or a list (such as a
                reduced word) of elements from the index set of the
                Coxeter group.

            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``); the
                side of ``self`` on which the element should be
                applied. If ``side`` is 'left' then the operation is
                applied on the left.

            - ``length_increasing`` -- boolean (default: ``True``)
                whether to act length increasingly or decreasingly

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['C', 4], prefix='s')
                sage: v = W.from_reduced_word([1,2,3,4,3,1])
                sage: v.apply_demazure_product([1,3,4,3,3])
                s4*s1*s2*s3*s4*s3*s1
                sage: v.apply_demazure_product([1,3,4,3], side='left')
                s3*s4*s1*s2*s3*s4*s2*s3*s1
                sage: v.apply_demazure_product((1,3,4,3), side='left')
                s3*s4*s1*s2*s3*s4*s2*s3*s1
                sage: v.apply_demazure_product(v)
                s2*s3*s4*s1*s2*s3*s4*s2*s3*s2*s1
            """
        def min_demazure_product_greater(self, element):
            """
            Find the unique Bruhat-minimum element ``u`` such that ``v`` `\\le`
            ``w`` * ``u`` where ``v`` is ``self``, ``w`` is ``element`` and
            ``*`` is the Demazure product.

            INPUT:

            - ``element`` -- is either an element of the same Coxeter group as
              ``self`` or a list (such as a reduced word) of elements from the
              index set of the Coxeter group

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 4], prefix='s')
                sage: v = W.from_reduced_word([2,3,4,1,2])
                sage: u = W.from_reduced_word([2,3,2,1])
                sage: v.min_demazure_product_greater(u)
                s4*s2
                sage: v.min_demazure_product_greater([2,3,2,1])
                s4*s2
                sage: v.min_demazure_product_greater((2,3,2,1))
                s4*s2
            """
        def deodhar_factor_element(self, w, index_set):
            """
            Return Deodhar's Bruhat order factoring element.

            INPUT:

            - ``w`` -- an element of the same Coxeter group ``W`` as ``self``
            - ``index_set`` -- a subset of Dynkin nodes defining a parabolic
              subgroup ``W'`` of ``W``

            It is assumed that ``v = self`` and ``w`` are minimum length coset representatives
            for ``W/W'`` such that ``v`` `\\le` ``w`` in Bruhat order.

            OUTPUT:

            Deodhar's element ``f(v,w)`` is the unique element of ``W'`` such that,
            for all ``v'`` and ``w'`` in ``W'``, ``vv'`` `\\le` ``ww'`` in ``W`` if and only if
            ``v'`` `\\le` ``f(v,w) * w'`` in ``W'`` where ``*`` is the Demazure product.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 5], prefix='s')
                sage: v = W.from_reduced_word([5])
                sage: w = W.from_reduced_word([4,5,2,3,1,2])
                sage: v.deodhar_factor_element(w, [1,3,4])
                s3*s1
                sage: W = WeylGroup(['C', 2])
                sage: w = W.from_reduced_word([2,1])
                sage: w.deodhar_factor_element(W.from_reduced_word([2]),[1])
                Traceback (most recent call last):
                ...
                ValueError: [2, 1] is not of minimum length in its coset
                for the parabolic subgroup with index set [1]

            REFERENCES:

            - [Deo1987a]_
            """
        def deodhar_lift_up(self, w, index_set):
            """
            Letting ``v = self``, given a Bruhat relation ``v W'`` `\\le` ``w W'`` among cosets
            with respect to the subgroup ``W'`` given by the Dynkin node subset ``index_set``,
            returns the Bruhat-minimum lift ``x`` of ``wW'`` such that ``v`` `\\le` ``x``.

            INPUT:

            - ``w`` -- an element of the same Coxeter group ``W`` as ``self``
            - ``index_set`` -- a subset of Dynkin nodes defining a parabolic
              subgroup ``W'``

            OUTPUT:

            The unique Bruhat-minimum element ``x`` in ``W`` such that ``x W' = w W'``
            and ``v`` `\\le` ``x``.

            .. SEEALSO:: :meth:`sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.deodhar_lift_down`

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 3], prefix='s')
                sage: v = W.from_reduced_word([1,2,3])
                sage: w = W.from_reduced_word([1,3,2])
                sage: v.deodhar_lift_up(w, [3])
                s1*s2*s3*s2
            """
        def deodhar_lift_down(self, w, index_set):
            """
            Letting ``v = self``, given a Bruhat relation ``v W'`` `\\ge` ``w W'`` among cosets
            with respect to the subgroup ``W'`` given by the Dynkin node subset ``index_set``,
            returns the Bruhat-maximum lift ``x`` of ``wW'`` such that ``v`` `\\ge` ``x``.

            INPUT:

            - ``w`` -- an element of the same Coxeter group ``W`` as ``self``
            - ``index_set`` -- a subset of Dynkin nodes defining a parabolic subgroup ``W'``

            OUTPUT:

            The unique Bruhat-maximum element ``x`` in ``W`` such that ``x W' = w W'``
            and ``v`` `\\ge` ``x``.

            .. SEEALSO:: :meth:`sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.deodhar_lift_up`

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 3], prefix='s')
                sage: v = W.from_reduced_word([1,2,3,2])
                sage: w = W.from_reduced_word([3,2])
                sage: v.deodhar_lift_down(w, [3])
                s2*s3*s2
            """
        @cached_in_parent_method
        def inversions_as_reflections(self):
            """
            Return the set of reflections ``r`` such that ``self`` ``r < self``.

            EXAMPLES::

                sage: W = WeylGroup(['A', 3], prefix='s')                               # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,1,2,1])                                # needs sage.combinat sage.groups
                sage: w.inversions_as_reflections()                                     # needs sage.combinat sage.groups
                [s1, s1*s2*s1, s2, s1*s2*s3*s2*s1]
            """
        def left_inversions_as_reflections(self):
            """
            Return the set of reflections ``r`` such that ``r``  ``self`` < ``self``.

            EXAMPLES::

                sage: W = WeylGroup(['A', 3], prefix='s')                               # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,1,2,1])                                # needs sage.combinat sage.groups
                sage: w.left_inversions_as_reflections()                                # needs sage.combinat sage.groups
                [s1, s3, s1*s2*s3*s2*s1, s2*s3*s2]
            """
        def lower_covers(self, side: str = 'right', index_set=None):
            """
            Return all elements that ``self`` covers in weak order.

            INPUT:

            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
            - ``index_set`` -- list of indices or ``None``

            OUTPUT: list

            EXAMPLES::

                sage: W = WeylGroup(['A', 3])                                           # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([3,2,1])                                  # needs sage.combinat sage.groups
                sage: [x.reduced_word() for x in w.lower_covers()]                      # needs sage.combinat sage.groups
                [[3, 2]]

            To obtain covers for left weak order, set the option side to 'left'::

                sage: [x.reduced_word() for x in w.lower_covers(side='left')]           # needs sage.combinat sage.groups
                [[2, 1]]
                sage: w = W.from_reduced_word([3,2,3,1])                                # needs sage.combinat sage.groups
                sage: [x.reduced_word() for x in w.lower_covers()]                      # needs sage.combinat sage.groups
                [[2, 3, 2], [3, 2, 1]]

            Covers w.r.t. a parabolic subgroup are obtained with the option ``index_set``::

                sage: [x.reduced_word() for x in w.lower_covers(index_set=[1,2])]       # needs sage.combinat sage.groups
                [[2, 3, 2]]
                sage: [x.reduced_word() for x in w.lower_covers(side='left')]           # needs sage.combinat sage.groups
                [[3, 2, 1], [2, 3, 1]]
            """
        def upper_covers(self, side: str = 'right', index_set=None):
            """
            Return all elements that cover ``self`` in weak order.

            INPUT:

            - ``side`` -- ``'left'`` or ``'right'`` (default: ``'right'``)
            - ``index_set`` -- list of indices or ``None``

            OUTPUT: list

            EXAMPLES::

                sage: W = WeylGroup(['A', 3])                                           # needs sage.combinat sage.groups
                sage: w = W.from_reduced_word([2,3])                                    # needs sage.combinat sage.groups
                sage: [x.reduced_word() for x in w.upper_covers()]                      # needs sage.combinat sage.groups
                [[2, 3, 1], [2, 3, 2]]

            To obtain covers for left weak order, set the option ``side`` to 'left'::

                sage: [x.reduced_word() for x in w.upper_covers(side='left')]           # needs sage.combinat sage.groups
                [[1, 2, 3], [2, 3, 2]]

            Covers w.r.t. a parabolic subgroup are obtained with the option ``index_set``::

                sage: [x.reduced_word() for x in w.upper_covers(index_set=[1])]         # needs sage.combinat sage.groups
                [[2, 3, 1]]
                sage: [x.reduced_word()                                                 # needs sage.combinat sage.groups
                ....:  for x in w.upper_covers(side='left', index_set=[1])]
                [[1, 2, 3]]
            """
        def kazhdan_lusztig_cell(self, side: str = 'left'):
            """
            Compute the left, right, or two-sided Kazhdan-Lusztig cell
            containing the element ``self`` depending on the specified ``side``.

            Let `C'` denote the Kazhdan-Lusztig `C^{\\prime}`-basis of the
            Iwahori-Hecke algebra `H` of a Coxeter system `(W,S)`. Two elements
            `x,y` of the Coxeter group `W` are said to lie in the same left
            Kazhdan-Lusztig cell if there exist sequences `x = w_1, w_2, \\ldots,
            w_k = y` and `y = u_1, u_2, \\ldots, u_l = x` such that for all
            `1 \\leq i < k` and all `1 \\leq j < l`, there exist some Coxeter
            generators `s,t \\in S` for which `C'_{w_{i+1}}` appears in
            `C'_s C'_{w_i}` and `C'_{u_{j+1}}` appears in `C'_s C'_{u_j}`
            in `H`.  Right and two-sided Kazhdan-Lusztig cells of `W` are
            defined similarly; see [Lus2013]_.

            In this function, we compute products in the `C^{\\prime}` basis by
            using :class:`IwahoriHeckeAlgebra.Cp`. As mentioned in that class,
            installing the optional package ``coxeter3`` is recommended
            (though not required) before using this function because the
            package speeds up product computations that are sometimes
            computationally infeasible without it.

            INPUT:

            - ``w`` -- an element of ``self``

            - ``side`` -- (default: ``'left'``) the kind of cell to compute;
              must be either ``'left'``, ``'right'``, or ``'two-sided'``

            EXAMPLES:

            We compute the left cell of the generator `s_1` in type `A_3` in
            three different implementations of the Coxeter group. Note that the
            choice of implementation affects the representation of elements in
            the output cell but not the method used for the cell computation::

                sage: W = CoxeterGroup('A3', implementation='permutation')              # needs sage.combinat sage.groups
                sage: s1, s2, s3 = W.simple_reflections()                               # needs sage.combinat sage.groups
                sage: s1.kazhdan_lusztig_cell()                                         # needs sage.combinat sage.groups
                {(1,2,3,12)(4,5,10,11)(6,7,8,9),
                 (1,2,10)(3,6,5)(4,7,8)(9,12,11),
                 (1,7)(2,4)(5,6)(8,10)(11,12)}

            The cell computation uses the optional package ``coxeter3`` in
            the background if available to speed up the computation,
            even in the different implementations::

                sage: # optional - coxeter3, needs sage.combinat sage.groups sage.modules
                sage: W = WeylGroup('A3', prefix='s')
                sage: s1,s2,s3 = W.simple_reflections()
                sage: s1.kazhdan_lusztig_cell()
                {s3*s2*s1, s2*s1, s1}
                sage: W = CoxeterGroup('A3', implementation='coxeter3')
                sage: s1,s2,s3 = W.simple_reflections()
                sage: s1.kazhdan_lusztig_cell()
                {[1], [2, 1], [3, 2, 1]}

            Next, we compute a right cell and a two-sided cell in `A_3`::

                sage: # optional - coxeter3, needs sage.combinat sage.groups sage.modules
                sage: W = CoxeterGroup('A3', implementation='coxeter3')
                sage: s1,s2,s3 = W.simple_reflections()
                sage: w = s1 * s3
                sage: w.kazhdan_lusztig_cell(side='right')
                {[1, 3], [1, 3, 2]}
                sage: w.kazhdan_lusztig_cell(side='two-sided')
                {[1, 3], [1, 3, 2], [2, 1, 3], [2, 1, 3, 2]}

            Some slightly longer computations in `B_4`::

                sage: # optional - coxeter3, needs sage.combinat sage.groups sage.modules
                sage: W = CoxeterGroup('B4', implementation='coxeter3')
                sage: s1,s2,s3,s4 = W.simple_reflections()
                sage: s1.kazhdan_lusztig_cell(side='right')     # long time (4 seconds)
                {[1],
                 [1, 2],
                 [1, 2, 3],
                 [1, 2, 3, 4],
                 [1, 2, 3, 4, 3],
                 [1, 2, 3, 4, 3, 2],
                 [1, 2, 3, 4, 3, 2, 1]}
                sage: (s4*s2*s3*s4).kazhdan_lusztig_cell(side='two-sided')      # long time (8 seconds)
                {[2, 3, 1],
                 [2, 3, 1, 2],
                 [2, 3, 4, 1],
                 [2, 3, 4, 1, 2],
                 [2, 3, 4, 1, 2, 3],
                 [2, 3, 4, 1, 2, 3, 4],
                 [2, 3, 4, 3, 1],
                 [2, 3, 4, 3, 1, 2],
                 ...
                 [4, 3, 4, 2, 3, 4, 1, 2, 3, 4]}
            """
