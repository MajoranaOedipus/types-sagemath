from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.crystals import Crystals as Crystals
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method

class SuperCrystals(Category_singleton):
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.supercrystals import SuperCrystals
            sage: C = SuperCrystals()
            sage: C.super_categories()
            [Category of crystals]
        """
    class ParentMethods:
        def tensor(self, *crystals, **options):
            """
            Return the tensor product of ``self`` with the crystals ``B``.

            EXAMPLES::

                sage: B = crystals.Letters(['A',[1,2]])
                sage: C = crystals.Tableaux(['A',[1,2]], shape = [2,1])
                sage: T = C.tensor(B); T
                Full tensor product of the crystals
                 [Crystal of BKK tableaux of shape [2, 1] of gl(2|3),
                  The crystal of letters for type ['A', [1, 2]]]
                sage: S = B.tensor(C); S
                Full tensor product of the crystals
                 [The crystal of letters for type ['A', [1, 2]],
                  Crystal of BKK tableaux of shape [2, 1] of gl(2|3)]
                sage: G = T.digraph()
                sage: H = S.digraph()
                sage: G.is_isomorphic(H, edge_labels=True)
                True
            """
    class Finite(CategoryWithAxiom):
        class ParentMethods:
            def digraph(self, index_set=None):
                """
                Return the :class:`DiGraph` associated to ``self``.

                EXAMPLES::

                    sage: B = crystals.Letters(['A', [1,3]])
                    sage: G = B.digraph(); G
                    Multi-digraph on 6 vertices
                    sage: Q = crystals.Letters(['Q',3])
                    sage: G = Q.digraph(); G
                    Multi-digraph on 3 vertices
                    sage: G.edges(sort=True)
                    [(1, 2, -1), (1, 2, 1), (2, 3, -2), (2, 3, 2)]

                The edges of the crystal graph are by default colored using
                blue for edge 1, red for edge 2, green for edge 3, and dashed with
                the corresponding color for barred edges. Edge 0 is dotted black::

                    sage: view(G)  # optional - dot2tex graphviz, not tested (opens external window)
                """
            def genuine_highest_weight_vectors(self):
                """
                Return the tuple of genuine highest weight elements of ``self``.

                EXAMPLES::

                    sage: B = crystals.Letters(['A', [1,2]])
                    sage: B.genuine_highest_weight_vectors()
                    (-2,)

                    sage: T = B.tensor(B)
                    sage: T.genuine_highest_weight_vectors()
                    ([-2, -1], [-2, -2])
                    sage: s1, s2 = T.connected_components()
                    sage: s = s1 + s2
                    sage: s.genuine_highest_weight_vectors()
                    ([-2, -1], [-2, -2])
                """
            connected_components_generators = genuine_highest_weight_vectors
            def connected_components(self):
                """
                Return the connected components of ``self`` as subcrystals.

                EXAMPLES::

                    sage: B = crystals.Letters(['A', [1,2]])
                    sage: B.connected_components()
                    [Subcrystal of The crystal of letters for type ['A', [1, 2]]]

                    sage: T = B.tensor(B)
                    sage: T.connected_components()
                    [Subcrystal of Full tensor product of the crystals
                      [The crystal of letters for type ['A', [1, 2]],
                       The crystal of letters for type ['A', [1, 2]]],
                     Subcrystal of Full tensor product of the crystals
                      [The crystal of letters for type ['A', [1, 2]],
                       The crystal of letters for type ['A', [1, 2]]]]
                """
            def genuine_lowest_weight_vectors(self):
                """
                Return the tuple of genuine lowest weight elements of ``self``.

                EXAMPLES::

                    sage: B = crystals.Letters(['A', [1,2]])
                    sage: B.genuine_lowest_weight_vectors()
                    (3,)

                    sage: T = B.tensor(B)
                    sage: T.genuine_lowest_weight_vectors()
                    ([3, 3], [3, 2])
                    sage: s1, s2 = T.connected_components()
                    sage: s = s1 + s2
                    sage: s.genuine_lowest_weight_vectors()
                    ([3, 3], [3, 2])
                """
            def character(self):
                """
                Return the character of ``self``.

                .. TODO::

                    Once the `WeylCharacterRing` is implemented, make this
                    consistent with the implementation in
                    :meth:`sage.categories.classical_crystals.ClassicalCrystals.ParentMethods.character`.

                EXAMPLES::

                    sage: B = crystals.Letters(['A',[1,2]])
                    sage: B.character()
                    B[(1, 0, 0, 0, 0)] + B[(0, 1, 0, 0, 0)] + B[(0, 0, 1, 0, 0)]
                     + B[(0, 0, 0, 1, 0)] + B[(0, 0, 0, 0, 1)]
                """
            @cached_method
            def highest_weight_vectors(self):
                """
                Return the highest weight vectors of ``self``.

                EXAMPLES::

                    sage: B = crystals.Letters(['A', [1,2]])
                    sage: B.highest_weight_vectors()
                    (-2,)

                    sage: T = B.tensor(B)
                    sage: T.highest_weight_vectors()
                    ([-2, -2], [-2, -1])

                We give an example from [BKK2000]_ that has fake
                highest weight vectors::

                    sage: B = crystals.Tableaux(['A', [1,1]], shape=[3,2,1])
                    sage: B.highest_weight_vectors()
                    ([[-2, -2, -2], [-1, -1], [1]],
                     [[-2, -2, -2], [-1, 2], [1]],
                     [[-2, -2, 2], [-1, -1], [1]])
                    sage: B.genuine_highest_weight_vectors()
                    ([[-2, -2, -2], [-1, -1], [1]],)
                """
            @cached_method
            def lowest_weight_vectors(self):
                """
                Return the lowest weight vectors of ``self``.

                EXAMPLES::

                    sage: B = crystals.Letters(['A', [1,2]])
                    sage: B.lowest_weight_vectors()
                    (3,)

                    sage: T = B.tensor(B)
                    sage: sorted(T.lowest_weight_vectors())
                    [[3, 2], [3, 3]]

                We give an example from [BKK2000]_ that has fake
                lowest weight vectors::

                    sage: B = crystals.Tableaux(['A', [1,1]], shape=[3,2,1])
                    sage: sorted(B.lowest_weight_vectors())
                    [[[-2, 1, 2], [-1, 2], [1]],
                     [[-2, 1, 2], [-1, 2], [2]],
                     [[-1, 1, 2], [1, 2], [2]]]
                    sage: B.genuine_lowest_weight_vectors()
                    ([[-1, 1, 2], [1, 2], [2]],)
                """
        class ElementMethods:
            def is_genuine_highest_weight(self, index_set=None):
                '''
                Return whether ``self`` is a genuine highest weight element.

                INPUT:

                - ``index_set`` -- (optional) the index set of the (sub)crystal
                  on which to check

                EXAMPLES::

                    sage: B = crystals.Tableaux([\'A\', [1,1]], shape=[3,2,1])
                    sage: for b in B.highest_weight_vectors():
                    ....:     print("{} {}".format(b, b.is_genuine_highest_weight()))
                    [[-2, -2, -2], [-1, -1], [1]] True
                    [[-2, -2, -2], [-1, 2], [1]] False
                    [[-2, -2, 2], [-1, -1], [1]] False
                    sage: [b for b in B if b.is_genuine_highest_weight([-1,0])]
                    [[[-2, -2, -2], [-1, -1], [1]],
                     [[-2, -2, -2], [-1, -1], [2]],
                     [[-2, -2, -2], [-1, 2], [2]],
                     [[-2, -2, 2], [-1, -1], [2]],
                     [[-2, -2, 2], [-1, 2], [2]],
                     [[-2, -2, -2], [-1, 2], [1]],
                     [[-2, -2, 2], [-1, -1], [1]],
                     [[-2, -2, 2], [-1, 2], [1]]]
                '''
            def is_genuine_lowest_weight(self, index_set=None):
                '''
                Return whether ``self`` is a genuine lowest weight element.

                INPUT:

                - ``index_set`` -- (optional) the index set of the (sub)crystal
                  on which to check

                EXAMPLES::

                    sage: B = crystals.Tableaux([\'A\', [1,1]], shape=[3,2,1])
                    sage: for b in sorted(B.lowest_weight_vectors()):
                    ....:     print("{} {}".format(b, b.is_genuine_lowest_weight()))
                    [[-2, 1, 2], [-1, 2], [1]] False
                    [[-2, 1, 2], [-1, 2], [2]] False
                    [[-1, 1, 2], [1, 2], [2]] True
                    sage: [b for b in B if b.is_genuine_lowest_weight([-1,0])]
                    [[[-2, -1, 1], [-1, 1], [1]],
                     [[-2, -1, 1], [-1, 1], [2]],
                     [[-2, 1, 2], [-1, 1], [2]],
                     [[-2, 1, 2], [-1, 1], [1]],
                     [[-1, -1, 1], [1, 2], [2]],
                     [[-1, -1, 1], [1, 2], [1]],
                     [[-1, 1, 2], [1, 2], [2]],
                     [[-1, 1, 2], [1, 2], [1]]]
                '''
    class TensorProducts(TensorProductsCategory):
        """
        The category of regular crystals constructed by tensor
        product of regular crystals.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: from sage.categories.supercrystals import SuperCrystals
                sage: SuperCrystals().TensorProducts().extra_super_categories()
                [Category of super crystals]
            """
