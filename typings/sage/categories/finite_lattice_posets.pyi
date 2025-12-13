from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom

class FiniteLatticePosets(CategoryWithAxiom):
    """
    The category of finite lattices, i.e. finite partially ordered
    sets which are also lattices.

    EXAMPLES::

        sage: FiniteLatticePosets()
        Category of finite lattice posets
        sage: FiniteLatticePosets().super_categories()
        [Category of lattice posets, Category of finite posets]
        sage: FiniteLatticePosets().example()
        NotImplemented

    .. SEEALSO::

        :class:`FinitePosets`, :class:`LatticePosets`, :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

    TESTS::

        sage: C = FiniteLatticePosets()
        sage: C is FiniteLatticePosets().Finite()
        True
        sage: TestSuite(C).run()
    """
    class ParentMethods:
        def join_irreducibles(self):
            """
            Return the join-irreducible elements of this finite lattice.

            A *join-irreducible element* of ``self`` is an element
            `x` that is not minimal and that can not be written as
            the join of two elements different from `x`.

            EXAMPLES::

                sage: L = LatticePoset({0:[1,2],1:[3],2:[3,4],3:[5],4:[5]})             # needs sage.graphs sage.modules
                sage: L.join_irreducibles()                                             # needs sage.graphs sage.modules
                [1, 2, 4]

            .. SEEALSO::

                - Dual function: :meth:`meet_irreducibles`
                - Other: :meth:`~sage.combinat.posets.lattices.FiniteLatticePoset.double_irreducibles`,
                  :meth:`join_irreducibles_poset`
            """
        def join_irreducibles_poset(self):
            """
            Return the poset of join-irreducible elements of this finite lattice.

            A *join-irreducible element* of ``self`` is an element `x`
            that is not minimal and can not be written as the join of two
            elements different from `x`.

            EXAMPLES::

                sage: L = LatticePoset({0:[1,2,3],1:[4],2:[4],3:[4]})                   # needs sage.graphs sage.modules
                sage: L.join_irreducibles_poset()                                       # needs sage.graphs sage.modules
                Finite poset containing 3 elements

            .. SEEALSO::

                - Dual function: :meth:`meet_irreducibles_poset`
                - Other: :meth:`join_irreducibles`
            """
        def meet_irreducibles(self):
            """
            Return the meet-irreducible elements of this finite lattice.

            A *meet-irreducible element* of ``self`` is an element
            `x` that is not maximal and that can not be written as
            the meet of two elements different from `x`.

            EXAMPLES::

                sage: L = LatticePoset({0:[1,2],1:[3],2:[3,4],3:[5],4:[5]})             # needs sage.graphs sage.modules
                sage: L.meet_irreducibles()                                             # needs sage.graphs sage.modules
                [1, 3, 4]

            .. SEEALSO::

                - Dual function: :meth:`join_irreducibles`
                - Other: :meth:`~sage.combinat.posets.lattices.FiniteLatticePoset.double_irreducibles`,
                  :meth:`meet_irreducibles_poset`
            """
        def meet_irreducibles_poset(self):
            """
            Return the poset of join-irreducible elements of this finite lattice.

            A *meet-irreducible element* of ``self`` is an element `x`
            that is not maximal and can not be written as the meet of two
            elements different from `x`.

            EXAMPLES::

                sage: L = LatticePoset({0:[1,2,3],1:[4],2:[4],3:[4]})                   # needs sage.graphs sage.modules
                sage: L.join_irreducibles_poset()                                       # needs sage.graphs sage.modules
                Finite poset containing 3 elements

            .. SEEALSO::

                - Dual function: :meth:`join_irreducibles_poset`
                - Other: :meth:`meet_irreducibles`
            """
        def irreducibles_poset(self):
            """
            Return the poset of meet- or join-irreducibles of the lattice.

            A *join-irreducible* element of a lattice is an element with
            exactly one lower cover. Dually a *meet-irreducible* element
            has exactly one upper cover.

            This is the smallest poset with completion by cuts being
            isomorphic to the lattice. As a special case this returns
            one-element poset from one-element lattice.

            .. SEEALSO::

                :meth:`~sage.combinat.posets.posets.FinitePoset.completion_by_cuts`.

            EXAMPLES::

                sage: # needs sage.combinat sage.graphs sage.modules
                sage: L = LatticePoset({1: [2, 3, 4], 2: [5, 6], 3: [5],
                ....:                   4: [6], 5: [9, 7], 6: [9, 8], 7: [10],
                ....:                   8: [10], 9: [10], 10: [11]})
                sage: L_ = L.irreducibles_poset()
                sage: sorted(L_)
                [2, 3, 4, 7, 8, 9, 10, 11]
                sage: L_.completion_by_cuts().is_isomorphic(L)
                True

            TESTS::

                sage: LatticePoset().irreducibles_poset()                               # needs sage.graphs
                Finite poset containing 0 elements
                sage: posets.ChainPoset(1).irreducibles_poset()                         # needs sage.graphs
                Finite poset containing 1 elements
            """
        def is_lattice_morphism(self, f, codomain):
            '''
            Return whether ``f`` is a morphism of posets from ``self``
            to ``codomain``.

            A map `f : P \\to Q` is a poset morphism if

            .. MATH::

                x \\leq y \\Rightarrow f(x) \\leq f(y)

            for all `x,y \\in P`.

            INPUT:

            - ``f`` -- a function from ``self`` to ``codomain``
            - ``codomain`` -- a lattice

            EXAMPLES:

            We build the boolean lattice of `\\{2,2,3\\}` and the
            lattice of divisors of `60`, and check that the map
            `b \\mapsto 5 \\prod_{x\\in b} x` is a morphism of lattices::

                sage: D = LatticePoset((divisors(60), attrcall("divides")))             # needs sage.graphs sage.modules
                sage: B = LatticePoset((Subsets([2,2,3]), attrcall("issubset")))        # needs sage.graphs sage.modules
                sage: def f(b): return D(5*prod(b))
                sage: B.is_lattice_morphism(f, D)                                       # needs sage.graphs sage.modules
                True

            We construct the boolean lattice `B_2`::

                sage: B = posets.BooleanLattice(2)                                      # needs sage.graphs
                sage: B.cover_relations()                                               # needs sage.graphs
                [[0, 1], [0, 2], [1, 3], [2, 3]]

            And the same lattice with new top and bottom elements
            numbered respectively `-1` and `3`::

                sage: G = DiGraph({-1:[0], 0:[1,2], 1:[3], 2:[3], 3:[4]})               # needs sage.graphs
                sage: L = LatticePoset(G)                                               # needs sage.graphs sage.modules
                sage: L.cover_relations()                                               # needs sage.graphs sage.modules
                [[-1, 0], [0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]

                sage: f = {B(0): L(0), B(1): L(1), B(2): L(2), B(3): L(3)}.__getitem__  # needs sage.graphs sage.modules
                sage: B.is_lattice_morphism(f, L)                                       # needs sage.graphs sage.modules
                True

                sage: f = {B(0): L(-1),B(1): L(1), B(2): L(2), B(3): L(3)}.__getitem__  # needs sage.graphs sage.modules
                sage: B.is_lattice_morphism(f, L)                                       # needs sage.graphs sage.modules
                False

                sage: f = {B(0): L(0), B(1): L(1), B(2): L(2), B(3): L(4)}.__getitem__  # needs sage.graphs sage.modules
                sage: B.is_lattice_morphism(f, L)                                       # needs sage.graphs sage.modules
                False

            .. SEEALSO::

                :meth:`~sage.categories.finite_posets.FinitePosets.ParentMethods.is_poset_morphism`
            '''
