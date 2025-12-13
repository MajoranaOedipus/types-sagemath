from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.misc.cachefunc import cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class FiniteCoxeterGroups(CategoryWithAxiom):
    '''
    The category of finite Coxeter groups.

    EXAMPLES::

        sage: CoxeterGroups.Finite()
        Category of finite Coxeter groups
        sage: FiniteCoxeterGroups().super_categories()
        [Category of finite generalized Coxeter groups,
         Category of Coxeter groups]

        sage: G = CoxeterGroups().Finite().example()
        sage: G.cayley_graph(side = "right").plot()
        Graphics object consisting of 40 graphics primitives

    Here are some further examples::

        sage: WeylGroups().Finite().example()
        The symmetric group on {0, ..., 3}

        sage: WeylGroup(["B", 3])
        Weyl Group of type [\'B\', 3] (as a matrix group acting on the ambient space)

    Those other examples will eventually be also in this category::

        sage: SymmetricGroup(4)
        Symmetric group of order 4! as a permutation group
        sage: DihedralGroup(5)
        Dihedral group of order 10 as a permutation group
    '''
    def extra_super_categories(self):
        """
        EXAMPLES::

            sage: CoxeterGroups().Finite().super_categories()
            [Category of finite generalized Coxeter groups,
             Category of Coxeter groups]
        """
    class ParentMethods:
        """
        Ambiguity resolution: the implementation of ``some_elements``
        is preferable to that of :class:`FiniteGroups`. The same holds
        for ``__iter__``, although a breadth first search would be more
        natural; at least this maintains backward compatibility after
        :issue:`13589`.

        TESTS::

            sage: W = FiniteCoxeterGroups().example(3)

            sage: W.some_elements.__module__
            'sage.categories.complex_reflection_or_generalized_coxeter_groups'
            sage: W.__iter__.__module__
            'sage.categories.coxeter_groups'

            sage: W.some_elements()
            [(1,), (2,), (), (1, 2)]
            sage: list(W)
            [(), (1,), (2,), (1, 2), (2, 1), (1, 2, 1)]
        """
        __iter__: Incomplete
        @lazy_attribute
        def w0(self):
            """
            Return the longest element of ``self``.

            This attribute is deprecated, use :meth:`long_element` instead.

            EXAMPLES::

                sage: D8 = FiniteCoxeterGroups().example(8)
                sage: D8.w0
                (1, 2, 1, 2, 1, 2, 1, 2)
                sage: D3 = FiniteCoxeterGroups().example(3)
                sage: D3.w0
                (1, 2, 1)
            """
        def long_element(self, index_set=None, as_word: bool = False):
            """
            Return the longest element of ``self``, or of the
            parabolic subgroup corresponding to the given ``index_set``.

            INPUT:

            - ``index_set`` -- a subset (as a list or iterable) of the
              nodes of the Dynkin diagram; (default: all of them)

            - ``as_word`` -- boolean (default: ``False``); if ``True``, then
              return instead a reduced decomposition of the longest element

            Should this method be called maximal_element? longest_element?

            EXAMPLES::

                sage: D10 = FiniteCoxeterGroups().example(10)
                sage: D10.long_element()
                (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
                sage: D10.long_element([1])
                (1,)
                sage: D10.long_element([2])
                (2,)
                sage: D10.long_element([])
                ()

                sage: D7 = FiniteCoxeterGroups().example(7)
                sage: D7.long_element()
                (1, 2, 1, 2, 1, 2, 1)

            One can require instead a reduced word for w0::

                sage: A3 = CoxeterGroup(['A', 3])
                sage: A3.long_element(as_word=True)
                [1, 2, 1, 3, 2, 1]
            """
        @cached_method
        def bruhat_poset(self, facade: bool = False):
            '''
            Return the Bruhat poset of ``self``.

            .. SEEALSO::

                :meth:`bhz_poset`, :meth:`shard_poset`, :meth:`weak_poset`

            EXAMPLES::

                sage: W = WeylGroup(["A", 2])
                sage: P = W.bruhat_poset()
                sage: P
                Finite poset containing 6 elements
                sage: P.show()

            Here are some typical operations on this poset::

                sage: W = WeylGroup(["A", 3])
                sage: P = W.bruhat_poset()
                sage: u = W.from_reduced_word([3,1])
                sage: v = W.from_reduced_word([3,2,1,2,3])
                sage: P(u) <= P(v)
                True
                sage: len(P.interval(P(u), P(v)))
                10
                sage: P.is_join_semilattice()
                False

            By default, the elements of `P` are aware that they belong
            to `P`::

                sage: P.an_element().parent()
                Finite poset containing 24 elements

            If instead one wants the elements to be plain elements of
            the Coxeter group, one can use the ``facade`` option::

                sage: P = W.bruhat_poset(facade = True)
                sage: P.an_element().parent()
                Weyl Group of type [\'A\', 3] (as a matrix group acting on the ambient space)

            .. SEEALSO:: :func:`Poset` for more on posets and facade posets.

            TESTS::

                sage: [len(WeylGroup(["A", n]).bruhat_poset().cover_relations()) for n in [1,2,3]]
                [1, 8, 58]

            .. TODO::

                - Use the symmetric group in the examples (for nicer
                  output), and print the edges for a stronger test.
                - The constructed poset should be lazy, in order to
                  handle large / infinite Coxeter groups.
            '''
        def shard_poset(self, side: str = 'right'):
            """
            Return the shard intersection order attached to `W`.

            This is a lattice structure on `W`, introduced in [Rea2009]_. It
            contains the noncrossing partition lattice, as the induced lattice
            on the subset of `c`-sortable elements.

            The partial order is given by simultaneous inclusion of inversion sets
            and subgroups attached to every element.

            The precise description used here can be found in [STW2018]_.

            Another implementation for the symmetric groups is
            available as :func:`~sage.combinat.shard_order.shard_poset`.

            .. SEEALSO::

                :meth:`bhz_poset`, :meth:`bruhat_poset`, :meth:`weak_poset`

            EXAMPLES::

                sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
                sage: SH = W.shard_poset(); SH
                Finite lattice containing 24 elements
                sage: SH.is_graded()
                True
                sage: SH.characteristic_polynomial()
                q^3 - 11*q^2 + 23*q - 13
                sage: SH.f_polynomial()
                34*q^3 + 22*q^2 + q
            """
        def bhz_poset(self):
            """
            Return the Bergeron-Hohlweg-Zabrocki partial order on the Coxeter
            group.

            This is a partial order on the elements of a finite
            Coxeter group `W`, which is distinct from the Bruhat
            order, the weak order and the shard intersection order. It
            was defined in [BHZ2005]_.

            This partial order is not a lattice, as there is no unique
            maximal element. It can be succinctly defined as follows.

            Let `u` and `v` be two elements of the Coxeter group `W`. Let
            `S(u)` be the support of `u`. Then `u \\leq v` if and only
            if `v_{S(u)} = u` (here `v = v^I v_I` denotes the usual
            parabolic decomposition with respect to the standard parabolic
            subgroup `W_I`).

            .. SEEALSO::

                :meth:`bruhat_poset`, :meth:`shard_poset`, :meth:`weak_poset`

            EXAMPLES::

                sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
                sage: P = W.bhz_poset(); P
                Finite poset containing 24 elements
                sage: P.relations_number()
                103
                sage: P.chain_polynomial()
                34*q^4 + 90*q^3 + 79*q^2 + 24*q + 1
                sage: len(P.maximal_elements())
                13
            """
        def degrees(self):
            '''
            Return the degrees of the Coxeter group.

            The output is an increasing list of integers.

            EXAMPLES::

                sage: CoxeterGroup([\'A\', 4]).degrees()
                (2, 3, 4, 5)
                sage: CoxeterGroup([\'B\', 4]).degrees()
                (2, 4, 6, 8)
                sage: CoxeterGroup([\'D\', 4]).degrees()
                (2, 4, 4, 6)
                sage: CoxeterGroup([\'F\', 4]).degrees()
                (2, 6, 8, 12)
                sage: CoxeterGroup([\'E\', 8]).degrees()
                (2, 8, 12, 14, 18, 20, 24, 30)
                sage: CoxeterGroup([\'H\', 3]).degrees()
                (2, 6, 10)

                sage: WeylGroup([["A",3], ["A",3], ["B",2]]).degrees()
                (2, 3, 4, 2, 3, 4, 2, 4)

            TESTS::

                sage: CoxeterGroup([\'A\', 4]).degrees()
                (2, 3, 4, 5)
                sage: SymmetricGroup(3).degrees()
                (2, 3)
            '''
        def codegrees(self):
            '''
            Return the codegrees of the Coxeter group.

            These are just the degrees minus 2.

            EXAMPLES::

                sage: CoxeterGroup([\'A\', 4]).codegrees()
                (0, 1, 2, 3)
                sage: CoxeterGroup([\'B\', 4]).codegrees()
                (0, 2, 4, 6)
                sage: CoxeterGroup([\'D\', 4]).codegrees()
                (0, 2, 2, 4)
                sage: CoxeterGroup([\'F\', 4]).codegrees()
                (0, 4, 6, 10)
                sage: CoxeterGroup([\'E\', 8]).codegrees()
                (0, 6, 10, 12, 16, 18, 22, 28)
                sage: CoxeterGroup([\'H\', 3]).codegrees()
                (0, 4, 8)

                sage: WeylGroup([["A",3], ["A",3], ["B",2]]).codegrees()
                (0, 1, 2, 0, 1, 2, 0, 2)
            '''
        @cached_method
        def weak_poset(self, side: str = 'right', facade: bool = False):
            '''
            INPUT:

            - ``side`` -- "left", "right", or "twosided" (default: ``\'right\'``)
            - ``facade`` -- boolean (default: ``False``)

            Returns the left (resp. right) poset for weak order.  In
            this poset, `u` is smaller than `v` if some reduced word
            of `u` is a right (resp. left) factor of some reduced word
            of `v`.

            .. SEEALSO::

                :meth:`bhz_poset`, :meth:`bruhat_poset`, :meth:`shard_poset`

            EXAMPLES::

                sage: W = WeylGroup(["A", 2])
                sage: P = W.weak_poset()
                sage: P
                Finite lattice containing 6 elements
                sage: P.show()

            This poset is in fact a lattice::

                sage: W = WeylGroup(["B", 3])
                sage: P = W.weak_poset(side = "left")
                sage: P.is_lattice()
                True

            so this method has an alias :meth:`weak_lattice`::

                sage: W.weak_lattice(side = "left") is W.weak_poset(side = "left")
                True

            As a bonus feature, one can create the left-right weak
            poset::

                sage: W = WeylGroup(["A",2])
                sage: P = W.weak_poset(side = "twosided")
                sage: P.show()
                sage: len(P.hasse_diagram().edges(sort=False))
                8

            This is the transitive closure of the union of left and
            right order. In this poset, `u` is smaller than `v` if
            some reduced word of `u` is a factor of some reduced word
            of `v`. Note that this is not a lattice::

                sage: P.is_lattice()
                False

            By default, the elements of `P` are aware of that they
            belong to `P`::

                sage: P.an_element().parent()
                Finite poset containing 6 elements

            If instead one wants the elements to be plain elements of
            the Coxeter group, one can use the ``facade`` option::

                sage: P = W.weak_poset(facade = True)
                sage: P.an_element().parent()
                Weyl Group of type [\'A\', 2] (as a matrix group acting on the ambient space)

            .. SEEALSO:: :func:`Poset` for more on posets and facade posets.

            TESTS::

                sage: [len(WeylGroup(["A", n]).weak_poset(side = "right").cover_relations()) for n in [1,2,3]]
                [1, 6, 36]
                sage: [len(WeylGroup(["A", n]).weak_poset(side = "left" ).cover_relations()) for n in [1,2,3]]
                [1, 6, 36]

            .. TODO::

                - Use the symmetric group in the examples (for nicer
                  output), and print the edges for a stronger test.
                - The constructed poset should be lazy, in order to
                  handle large / infinite Coxeter groups.
            '''
        weak_lattice = weak_poset
        def inversion_sequence(self, word):
            '''
            Return the inversion sequence corresponding to the ``word``
            in indices of simple generators of ``self``.

            If ``word`` corresponds to `[w_0,w_1,...w_k]`, the output is
            `[w_0,w_0w_1w_0,\\ldots,w_0w_1\\cdots w_k \\cdots w_1 w_0]`.

            INPUT:

            - ``word`` -- a word in the indices of the simple
              generators of ``self``

            EXAMPLES::

                sage: CoxeterGroup(["A", 2]).inversion_sequence([1,2,1])
                [
                [-1  1]  [ 0 -1]  [ 1  0]
                [ 0  1], [-1  0], [ 1 -1]
                ]

                sage: [t.reduced_word() for t in CoxeterGroup(["A",3]).inversion_sequence([2,1,3,2,1,3])]
                [[2], [1, 2, 1], [2, 3, 2], [1, 2, 3, 2, 1], [3], [1]]
            '''
        def reflections_from_w0(self):
            """
            Return the reflections of ``self`` using the inversion set
            of ``w_0``.

            EXAMPLES::

                sage: WeylGroup(['A',2]).reflections_from_w0()
                [
                [0 1 0]  [0 0 1]  [1 0 0]
                [1 0 0]  [0 1 0]  [0 0 1]
                [0 0 1], [1 0 0], [0 1 0]
                ]

                sage: WeylGroup(['A',3]).reflections_from_w0()
                [
                [0 1 0 0]  [0 0 1 0]  [1 0 0 0]  [0 0 0 1]  [1 0 0 0]  [1 0 0 0]
                [1 0 0 0]  [0 1 0 0]  [0 0 1 0]  [0 1 0 0]  [0 0 0 1]  [0 1 0 0]
                [0 0 1 0]  [1 0 0 0]  [0 1 0 0]  [0 0 1 0]  [0 0 1 0]  [0 0 0 1]
                [0 0 0 1], [0 0 0 1], [0 0 0 1], [1 0 0 0], [0 1 0 0], [0 0 1 0]
                ]
            """
        @cached_method
        def m_cambrian_lattice(self, c, m: int = 1, on_roots: bool = False):
            '''
            Return the `m`-Cambrian lattice on `m`-delta sequences.

            See :arxiv:`1503.00710` and :arxiv:`math/0611106`.

            The `m`-delta sequences are certain `m`-colored minimal
            factorizations of `c` into reflections.

            INPUT:

            - ``c`` -- a Coxeter element of ``self`` (as a tuple, or
              as an element of ``self``)

            - ``m`` -- positive integer (default: 1)

            - ``on_roots`` -- boolean (default: ``False``); if
              ``on_roots`` is ``True``, the lattice is realized on
              roots rather than on reflections. In order for this to
              work, the ElementMethod ``reflection_to_root`` must be
              available.

            EXAMPLES::

                sage: CoxeterGroup(["A",2]).m_cambrian_lattice((1,2))
                Finite lattice containing 5 elements

                sage: CoxeterGroup(["A",2]).m_cambrian_lattice((1,2),2)
                Finite lattice containing 12 elements
            '''
        def cambrian_lattice(self, c, on_roots: bool = False):
            '''
            Return the `c`-Cambrian lattice on delta sequences.

            See :arxiv:`1503.00710` and :arxiv:`math/0611106`.

            Delta sequences are certain 2-colored minimal factorizations
            of `c` into reflections.

            INPUT:

            - ``c`` -- a standard Coxeter element in ``self``
              (as a tuple, or as an element of ``self``)

            - ``on_roots`` -- boolean (default: ``False``); if
              ``on_roots`` is ``True``, the lattice is realized on
              roots rather than on reflections. In order for this to
              work, the ElementMethod ``reflection_to_root`` must be
              available.

            EXAMPLES::

                sage: CoxeterGroup(["A", 2]).cambrian_lattice((1,2))
                Finite lattice containing 5 elements

                sage: CoxeterGroup(["B", 2]).cambrian_lattice((1,2))
                Finite lattice containing 6 elements

                sage: CoxeterGroup(["G", 2]).cambrian_lattice((1,2))
                Finite lattice containing 8 elements
            '''
        def is_real(self):
            """
            Return ``True`` since ``self`` is a real reflection group.

            EXAMPLES::

                sage: CoxeterGroup(['F',4]).is_real()
                True
                sage: CoxeterGroup(['H',4]).is_real()
                True
            """
        def permutahedron(self, point=None, base_ring=None):
            """
            Return the permutahedron of ``self``.

            This is the convex hull of the point ``point`` in the weight
            basis under the action of ``self`` on the underlying vector
            space `V`.

            .. SEEALSO::

                :meth:`~sage.combinat.root_system.reflection_group_real.permutahedron`

            INPUT:

            - ``point`` -- (optional) a point given by its coordinates in
              the weight basis (default: `(1, 1, 1, \\ldots)`)
            - ``base_ring`` -- (optional) the base ring of the polytope

            .. NOTE::

                The result is expressed in the root basis coordinates.

            .. NOTE::

                If function is too slow, switching the base ring to
                :class:`RDF` will almost certainly speed things up.

            EXAMPLES::

                sage: W = CoxeterGroup(['H',3], base_ring=RDF)
                sage: W.permutahedron()
                doctest:warning
                ...
                UserWarning: This polyhedron data is numerically complicated; cdd could not convert between the inexact V and H representation without loss of data. The resulting object might show inconsistencies.
                A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 120 vertices

                sage: W = CoxeterGroup(['I',7])
                sage: W.permutahedron()
                A 2-dimensional polyhedron in AA^2 defined as the convex hull of 14 vertices
                sage: W.permutahedron(base_ring=RDF)
                A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 14 vertices

                sage: W = ReflectionGroup(['A',3])                          # optional - gap3
                sage: W.permutahedron()                                     # optional - gap3
                A 3-dimensional polyhedron in QQ^3 defined as the convex hull
                of 24 vertices

                sage: W = ReflectionGroup(['A',3],['B',2])                  # optional - gap3
                sage: W.permutahedron()                                     # optional - gap3
                A 5-dimensional polyhedron in QQ^5 defined as the convex hull of 192 vertices

            TESTS::

                sage: W = ReflectionGroup(['A',3])                          # optional - gap3
                sage: W.permutahedron([3,5,8])                              # optional - gap3
                A 3-dimensional polyhedron in QQ^3 defined as the convex hull
                of 24 vertices


            .. PLOT::
                :width: 300 px

                W = CoxeterGroup(['I',7])
                p = W.permutahedron()
                sphinx_plot(p)
            """
        def coxeter_poset(self):
            """
            Return the Coxeter poset of ``self``.

            Let `W` be a Coxeter group. The *Coxeter poset* is defined as
            the set of (right) standard cosets `gW_J`, where `J` is a
            subset of the index set `I` of `W`, ordered by reverse inclusion.

            This is equal to the face poset of the :meth:`Coxeter complex
            <coxeter_complex()>`.

            EXAMPLES::

                sage: W = CoxeterGroup(['A', 3])
                sage: P = W.coxeter_poset()
                sage: P
                Finite meet-semilattice containing 75 elements
                sage: P.rank()
                3

                sage: W = WeylGroup(['B', 3])
                sage: P = W.coxeter_poset()
                sage: P
                Finite meet-semilattice containing 147 elements
                sage: P.rank()
                3

                sage: W = CoxeterGroup(['I', 7])
                sage: P = W.coxeter_poset()
                sage: P
                Finite meet-semilattice containing 29 elements
                sage: P.rank()
                2

                sage: W = CoxeterGroup(['H', 3])
                sage: P = W.coxeter_poset()
                sage: P
                Finite meet-semilattice containing 363 elements
                sage: P.rank()
                3

                sage: # optional - gap3
                sage: W = CoxeterGroup(['H', 3], implementation='permutation')
                sage: P = W.coxeter_poset()
                sage: P
                Finite meet-semilattice containing 363 elements
                sage: P.rank()
                3
            """
        def coxeter_complex(self):
            """
            Return the Coxeter complex of ``self``.

            Let `W` be a Coxeter group, and let `X` be the corresponding Tits
            cone, which is constructed as the `W` orbit of the fundamental
            chamber in the reflection representation. The *Coxeter complex*
            of `W` is the simplicial complex `(X \\setminus \\{0\\}) / \\RR_{>0}`.
            The face poset of this simplicial complex is given by the
            :meth:`coxeter_poset()`. When `W` is a finite group, then the
            Coxeter complex is homeomorphic to an `(n-1)`-dimensional sphere,
            where `n` is the rank of `W`.

            EXAMPLES::

                sage: W = CoxeterGroup(['A', 3])
                sage: C = W.coxeter_complex()
                sage: C
                Simplicial complex with 14 vertices and 24 facets
                sage: C.homology()
                {0: 0, 1: 0, 2: Z}

                sage: W = WeylGroup(['B', 3])
                sage: C = W.coxeter_complex()
                sage: C
                Simplicial complex with 26 vertices and 48 facets
                sage: C.homology()
                {0: 0, 1: 0, 2: Z}

                sage: W = CoxeterGroup(['I', 7])
                sage: C = W.coxeter_complex()
                sage: C
                Simplicial complex with 14 vertices and 14 facets
                sage: C.homology()
                {0: 0, 1: Z}

                sage: W = CoxeterGroup(['H', 3])
                sage: C = W.coxeter_complex()
                sage: C
                Simplicial complex with 62 vertices and 120 facets
                sage: C.homology()
                {0: 0, 1: 0, 2: Z}

                sage: # optional - gap3
                sage: W = CoxeterGroup(['H', 3], implementation='permutation')
                sage: C = W.coxeter_complex()
                sage: C
                Simplicial complex with 62 vertices and 120 facets
                sage: C.homology()
                {0: 0, 1: 0, 2: Z}
            """
    class ElementMethods:
        def absolute_length(self):
            '''
            Return the absolute length of ``self``.

            The absolute length is the length of the shortest expression
            of the element as a product of reflections. For finite Coxeter
            groups, the absolute length is the codimension of the
            1-eigenspace of the element (Lemmas 1-3 in [Car1972a]_).

            For permutations in the symmetric groups, the absolute
            length is the size minus the number of its disjoint
            cycles.

            .. SEEALSO::

                :meth:`~sage.categories.coxeter_groups.absolute_le`

            EXAMPLES::

                sage: W = WeylGroup(["A", 3])                                           # needs sage.combinat sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.combinat sage.groups
                sage: (s[1]*s[2]*s[3]).absolute_length()                                # needs sage.combinat sage.groups
                3

                sage: W = SymmetricGroup(4)                                             # needs sage.groups
                sage: s = W.simple_reflections()                                        # needs sage.groups
                sage: (s[3]*s[2]*s[1]).absolute_length()                                # needs sage.combinat sage.groups
                3
            '''
        @cached_in_parent_method
        def bruhat_upper_covers(self):
            '''
            Return all the elements that cover ``self`` in Bruhat order.

            EXAMPLES::

                sage: W = WeylGroup(["A",4])
                sage: w = W.from_reduced_word([3,2])
                sage: print([v.reduced_word() for v in w.bruhat_upper_covers()])
                [[4, 3, 2], [3, 4, 2], [2, 3, 2], [3, 1, 2], [3, 2, 1]]

                sage: W = WeylGroup(["B",6])
                sage: w = W.from_reduced_word([1,2,1,4,5])
                sage: C = w.bruhat_upper_covers()
                sage: len(C)
                9
                sage: print([v.reduced_word() for v in C])
                [[6, 4, 5, 1, 2, 1], [4, 5, 6, 1, 2, 1], [3, 4, 5, 1, 2, 1], [2, 3, 4, 5, 1, 2],
                [1, 2, 3, 4, 5, 1], [4, 5, 4, 1, 2, 1], [4, 5, 3, 1, 2, 1], [4, 5, 2, 3, 1, 2],
                [4, 5, 1, 2, 3, 1]]
                sage: ww = W.from_reduced_word([5,6,5])
                sage: CC = ww.bruhat_upper_covers()
                sage: print([v.reduced_word() for v in CC])
                [[6, 5, 6, 5], [4, 5, 6, 5], [5, 6, 4, 5], [5, 6, 5, 4], [5, 6, 5, 3], [5, 6, 5, 2],
                [5, 6, 5, 1]]

            Recursive algorithm: write `w` for ``self``. If `i` is a
            non-descent of `w`, then the covers of `w` are exactly
            `\\{ws_i, u_1s_i, u_2s_i,..., u_js_i\\}`, where the `u_k`
            are those covers of `ws_i` that have a descent at `i`.
            '''
        def coxeter_knuth_neighbor(self, w):
            """
            Return the Coxeter-Knuth (oriented) neighbors of the reduced word `w` of ``self``.

            INPUT:

            - ``w`` -- reduced word of ``self``

            The Coxeter-Knuth relations are given by `a a+1 a \\sim a+1 a a+1`, `abc \\sim acb`
            if `b<a<c` and `abc \\sim bac` if `a<c<b`. This method returns all neighbors of
            ``w`` under the Coxeter-Knuth relations oriented from left to right.

            EXAMPLES::

                sage: W = WeylGroup(['A',4], prefix='s')
                sage: word = [1,2,1,3,2]
                sage: w = W.from_reduced_word(word)
                sage: w.coxeter_knuth_neighbor(word)
                {(1, 2, 3, 1, 2), (2, 1, 2, 3, 2)}

                sage: word = [1,2,1,3,2,4,3]
                sage: w = W.from_reduced_word(word)
                sage: w.coxeter_knuth_neighbor(word)
                {(1, 2, 1, 3, 4, 2, 3), (1, 2, 3, 1, 2, 4, 3), (2, 1, 2, 3, 2, 4, 3)}

            TESTS::

                sage: W = WeylGroup(['B',4], prefix='s')
                sage: word = [1,2]
                sage: w = W.from_reduced_word(word)
                sage: w.coxeter_knuth_neighbor(word)
                Traceback (most recent call last):
                ...
                NotImplementedError: this has only been implemented in finite type A so far
            """
        def coxeter_knuth_graph(self):
            """
            Return the Coxeter-Knuth graph of type `A`.

            The Coxeter-Knuth graph of type `A` is generated by the Coxeter-Knuth relations which are
            given by `a a+1 a \\sim a+1 a a+1`, `abc \\sim acb` if `b<a<c` and `abc \\sim bac` if `a<c<b`.

            EXAMPLES::

                sage: W = WeylGroup(['A',4], prefix='s')
                sage: w = W.from_reduced_word([1,2,1,3,2])
                sage: D = w.coxeter_knuth_graph()
                sage: D.vertices(sort=True)
                [(1, 2, 1, 3, 2),
                (1, 2, 3, 1, 2),
                (2, 1, 2, 3, 2),
                (2, 1, 3, 2, 3),
                (2, 3, 1, 2, 3)]
                sage: D.edges(sort=True)
                [((1, 2, 1, 3, 2), (1, 2, 3, 1, 2), None),
                ((1, 2, 1, 3, 2), (2, 1, 2, 3, 2), None),
                ((2, 1, 2, 3, 2), (2, 1, 3, 2, 3), None),
                ((2, 1, 3, 2, 3), (2, 3, 1, 2, 3), None)]

                sage: w = W.from_reduced_word([1,3])
                sage: D = w.coxeter_knuth_graph()
                sage: D.vertices(sort=True)
                [(1, 3), (3, 1)]
                sage: D.edges(sort=False)
                []

            TESTS::

                sage: W = WeylGroup(['B',4], prefix='s')
                sage: w = W.from_reduced_word([1,2])
                sage: w.coxeter_knuth_graph()
                Traceback (most recent call last):
                ...
                NotImplementedError: this has only been implemented in finite type A so far
            """
        def is_coxeter_element(self):
            """
            Return whether this is a Coxeter element.

            This is, whether ``self`` has an eigenvalue `e^{2\\pi i/h}`
            where `h` is the Coxeter number.

            .. SEEALSO:: :meth:`~sage.categories.finite_complex_reflection_groups.coxeter_elements`

            EXAMPLES::

                sage: W = CoxeterGroup(['A',2])
                sage: c = prod(W.gens())
                sage: c.is_coxeter_element()
                True
                sage: W.one().is_coxeter_element()
                False

                sage: W = WeylGroup(['G', 2])
                sage: c = prod(W.gens())
                sage: c.is_coxeter_element()
                True
                sage: W.one().is_coxeter_element()
                False
            """
        def covered_reflections_subgroup(self):
            """
            Return the subgroup of `W` generated by the conjugates by `w`
            of the simple reflections indexed by right descents of `w`.

            This is used to compute the shard intersection order on `W`.

            EXAMPLES::

                sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
                sage: len(W.long_element().covered_reflections_subgroup())
                24
                sage: s = W.simple_reflection(1)
                sage: Gs = s.covered_reflections_subgroup()
                sage: len(Gs)
                2
                sage: s in [u.lift() for u in Gs]
                True
                sage: len(W.one().covered_reflections_subgroup())
                1
            """
