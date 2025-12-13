from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.homset import Hom as Hom, Homset as Homset
from sage.categories.morphism import Morphism as Morphism
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class Crystals(Category_singleton):
    """
    The category of crystals.

    See :mod:`sage.combinat.crystals.crystals` for an introduction to crystals.

    EXAMPLES::

        sage: C = Crystals()
        sage: C
        Category of crystals
        sage: C.super_categories()
        [Category of... enumerated sets]
        sage: C.example()
        Highest weight crystal of type A_3 of highest weight omega_1

    Parents in this category should implement the following methods:

    - either an attribute ``_cartan_type`` or a method ``cartan_type``

    - ``module_generators``: a list (or container) of distinct elements
      which generate the crystal using `f_i`

    Furthermore, their elements ``x`` should implement the following
    methods:

    - ``x.e(i)`` (returning `e_i(x)`)

    - ``x.f(i)`` (returning `f_i(x)`)

    - ``x.epsilon(i)`` (returning `\\varepsilon_i(x)`)

    - ``x.phi(i)`` (returning `\\varphi_i(x)`)

    EXAMPLES::

        sage: from sage.misc.abstract_method import abstract_methods_of_class
        sage: abstract_methods_of_class(Crystals().element_class)
        {'optional': [], 'required': ['e', 'epsilon', 'f', 'phi', 'weight']}

    TESTS::

        sage: TestSuite(C).run()
        sage: B = Crystals().example()
        sage: TestSuite(B).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          running ._test_stembridge_local_axioms() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_enumerated_set_contains() . . . pass
        running ._test_enumerated_set_iter_cardinality() . . . pass
        running ._test_enumerated_set_iter_list() . . . pass
        running ._test_eq() . . . pass
        running ._test_fast_iter() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
        running ._test_stembridge_local_axioms() . . . pass
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Crystals().super_categories()
            [Category of enumerated sets]
        """
    def example(self, choice: str = 'highwt', **kwds):
        """
        Return an example of a crystal, as per
        :meth:`Category.example()
        <sage.categories.category.Category.example>`.

        INPUT:

        - ``choice`` -- string (default: ``'highwt'``); can be either ``'highwt'``
          for the highest weight crystal of type A, or ``'naive'`` for an
          example of a broken crystal

        - ``**kwds`` -- keyword arguments passed onto the constructor for the
          chosen crystal

        EXAMPLES::

            sage: Crystals().example(choice='highwt', n=5)
            Highest weight crystal of type A_5 of highest weight omega_1
            sage: Crystals().example(choice='naive')
            A broken crystal, defined by digraph, of dimension five.
        """
    class MorphismMethods:
        @cached_method
        def is_isomorphism(self):
            """
            Check if ``self`` is a crystal isomorphism.

            EXAMPLES::

                sage: B = crystals.Tableaux(['C',2], shape=[1,1])
                sage: C = crystals.Tableaux(['C',2], ([2,1], [1,1]))
                sage: psi = B.crystal_morphism(C.module_generators[1:], codomain=C)
                sage: psi.is_isomorphism()
                False
            """
        @cached_method
        def is_embedding(self):
            """
            Check if ``self`` is an injective crystal morphism.

            EXAMPLES::

                sage: B = crystals.Tableaux(['C',2], shape=[1,1])
                sage: C = crystals.Tableaux(['C',2], ([2,1], [1,1]))
                sage: psi = B.crystal_morphism(C.module_generators[1:], codomain=C)
                sage: psi.is_embedding()
                True

                sage: C = crystals.Tableaux(['A',2], shape=[2,1])
                sage: B = crystals.infinity.Tableaux(['A',2])
                sage: La = RootSystem(['A',2]).weight_lattice().fundamental_weights()
                sage: W = crystals.elementary.T(['A',2], La[1]+La[2])
                sage: T = W.tensor(B)
                sage: mg = T(W.module_generators[0], B.module_generators[0])
                sage: psi = Hom(C,T)([mg])
                sage: psi.is_embedding()
                True
            """
        @cached_method
        def is_strict(self):
            """
            Check if ``self`` is a strict crystal morphism.

            EXAMPLES::

                sage: B = crystals.Tableaux(['C',2], shape=[1,1])
                sage: C = crystals.Tableaux(['C',2], ([2,1], [1,1]))
                sage: psi = B.crystal_morphism(C.module_generators[1:], codomain=C)
                sage: psi.is_strict()
                True
            """
    class ParentMethods:
        def an_element(self):
            """
            Return an element of ``self``.

                sage: C = crystals.Letters(['A', 5])
                sage: C.an_element()
                1
            """
        @cached_method
        def weight_lattice_realization(self):
            '''
            Return the weight lattice realization used to express weights
            in ``self``.

            This default implementation uses the ambient space of the
            root system for (non relabelled) finite types and the
            weight lattice otherwise. This is a legacy from when
            ambient spaces were partially implemented, and may be
            changed in the future.

            For affine types, this returns the extended weight lattice
            by default.

            EXAMPLES::

                sage: C = crystals.Letters([\'A\', 5])
                sage: C.weight_lattice_realization()
                Ambient space of the Root system of type [\'A\', 5]
                sage: K = crystals.KirillovReshetikhin([\'A\',2,1], 1, 1)
                sage: K.weight_lattice_realization()
                Weight lattice of the Root system of type [\'A\', 2, 1]

            TESTS:

            Check that crystals have the correct weight lattice realization::

                sage: A = crystals.KirillovReshetikhin([\'A\',2,1], 1, 1).affinization()
                sage: A.weight_lattice_realization()
                Extended weight lattice of the Root system of type [\'A\', 2, 1]

                sage: B = crystals.AlcovePaths([\'A\',2,1],[1,0,0])
                sage: B.weight_lattice_realization()
                Extended weight lattice of the Root system of type [\'A\', 2, 1]

                sage: C = crystals.AlcovePaths("B3",[1,0,0])
                sage: C.weight_lattice_realization()
                Ambient space of the Root system of type [\'B\', 3]

                sage: M = crystals.infinity.NakajimaMonomials([\'A\',3,2])
                sage: M.weight_lattice_realization()
                Extended weight lattice of the Root system of type [\'B\', 2, 1]^*
                sage: M = crystals.infinity.NakajimaMonomials([\'A\',2])
                sage: M.weight_lattice_realization()
                Ambient space of the Root system of type [\'A\', 2]
                sage: A = CartanMatrix([[2,-3],[-3,2]])
                sage: M = crystals.infinity.NakajimaMonomials(A)
                sage: M.weight_lattice_realization()
                Weight lattice of the Root system of type Dynkin diagram of rank 2

                sage: Y = crystals.infinity.GeneralizedYoungWalls(3)
                sage: Y.weight_lattice_realization()
                Extended weight lattice of the Root system of type [\'A\', 3, 1]
            '''
        def cartan_type(self):
            """
            Return the Cartan type of the crystal.

            EXAMPLES::

                sage: C = crystals.Letters(['A',2])
                sage: C.cartan_type()
                ['A', 2]
            """
        @cached_method
        def index_set(self):
            """
            Return the index set of the Dynkin diagram underlying the crystal.

            EXAMPLES::

                sage: C = crystals.Letters(['A', 5])
                sage: C.index_set()
                (1, 2, 3, 4, 5)
            """
        def Lambda(self):
            """
            Return the fundamental weights in the weight lattice
            realization for the root system associated with the crystal

            EXAMPLES::

                sage: C = crystals.Letters(['A', 5])
                sage: C.Lambda()
                Finite family {1: (1, 0, 0, 0, 0, 0), 2: (1, 1, 0, 0, 0, 0), 3: (1, 1, 1, 0, 0, 0), 4: (1, 1, 1, 1, 0, 0), 5: (1, 1, 1, 1, 1, 0)}
            """
        def __iter__(self, index_set=None, max_depth=...):
            """
            Return an iterator over the elements of ``self``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the index set; if ``None``
              then use the index set of the crystal

            - ``max_depth`` -- (default: infinity) the maximum depth to build

            The iteration order is not specified except that, if
            ``max_depth`` is finite, then the iteration goes depth by
            depth.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2,1],[-1,0,1])
                sage: C.__iter__.__module__
                'sage.categories.crystals'
                sage: g = C.__iter__()
                sage: for _ in range(5): next(g)
                (-Lambda[0] + Lambda[2],)
                (Lambda[1] - Lambda[2],)
                (Lambda[0] - Lambda[1] + delta,)
                (Lambda[0] - Lambda[1],)
                (Lambda[1] - Lambda[2] + delta,)

                sage: sorted(C.__iter__(index_set=[1,2]), key=str)
                [(-Lambda[0] + Lambda[2],),
                 (Lambda[0] - Lambda[1],),
                 (Lambda[1] - Lambda[2],)]

                sage: sorted(C.__iter__(max_depth=1), key=str)
                [(-Lambda[0] + Lambda[2],),
                 (Lambda[0] - Lambda[1] + delta,),
                 (Lambda[1] - Lambda[2],)]
            """
        def subcrystal(self, index_set=None, generators=None, max_depth=..., direction: str = 'both', contained=None, virtualization=None, scaling_factors=None, cartan_type=None, category=None):
            """
            Construct the subcrystal from ``generators`` using `e_i` and/or
            `f_i` for all `i` in ``index_set``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the index set; if ``None``
              then use the index set of the crystal

            - ``generators`` -- (default: ``None``) the list of generators; if
              ``None`` then use the module generators of the crystal

            - ``max_depth`` -- (default: infinity) the maximum depth to build

            - ``direction`` -- (default: ``'both'``) the direction to build
              the subcrystal; it can be one of the following:

              - ``'both'`` -- using both `e_i` and `f_i`
              - ``'upper'`` -- using `e_i`
              - ``'lower'`` -- using `f_i`

            - ``contained`` -- (optional) a set or function defining the
              containment in the subcrystal

            - ``virtualization``, ``scaling_factors`` -- (optional)
              dictionaries whose key `i` corresponds to the sets `\\sigma_i`
              and `\\gamma_i` respectively used to define virtual crystals; see
              :class:`~sage.combinat.crystals.virtual_crystal.VirtualCrystal`

            - ``cartan_type`` -- (optional) specify the Cartan type of the
              subcrystal

            - ``category`` -- (optional) specify the category of the subcrystal

            EXAMPLES::

                sage: C = crystals.KirillovReshetikhin(['A',3,1], 1, 2)
                sage: S = list(C.subcrystal(index_set=[1,2])); S
                [[[1, 1]], [[1, 2]], [[2, 2]], [[1, 3]], [[2, 3]], [[3, 3]]]
                sage: C.cardinality()
                10
                sage: len(S)
                6
                sage: list(C.subcrystal(index_set=[1,3], generators=[C(1,4)]))
                [[[1, 4]], [[2, 4]], [[1, 3]], [[2, 3]]]
                sage: list(C.subcrystal(index_set=[1,3], generators=[C(1,4)], max_depth=1))
                [[[1, 4]], [[2, 4]], [[1, 3]]]
                sage: list(C.subcrystal(index_set=[1,3], generators=[C(1,4)], direction='upper'))
                [[[1, 4]], [[1, 3]]]
                sage: list(C.subcrystal(index_set=[1,3], generators=[C(1,4)], direction='lower'))
                [[[1, 4]], [[2, 4]]]

                sage: G = C.subcrystal(index_set=[1,2,3]).digraph()
                sage: GA = crystals.Tableaux('A3', shape=[2]).digraph()
                sage: G.is_isomorphic(GA, edge_labels=True)
                True

            We construct the subcrystal which contains the necessary data
            to construct the corresponding dual equivalence graph::

                sage: C = crystals.Tableaux(['A',5], shape=[3,3])
                sage: is_wt0 = lambda x: all(x.epsilon(i) == x.phi(i) for i in x.parent().index_set())
                sage: def check(x):
                ....:     if is_wt0(x):
                ....:         return True
                ....:     for i in x.parent().index_set()[:-1]:
                ....:         L = [x.e(i), x.e_string([i,i+1]), x.f(i), x.f_string([i,i+1])]
                ....:         if any(y is not None and is_wt0(y) for y in L):
                ....:             return True
                ....:     return False
                sage: wt0 = [x for x in C if is_wt0(x)]
                sage: S = C.subcrystal(contained=check, generators=wt0)
                sage: S.module_generators[0]
                [[1, 3, 5], [2, 4, 6]]
                sage: S.module_generators[0].e(2).e(3).f(2).f(3)
                [[1, 2, 5], [3, 4, 6]]

            An example of a type `B_2` virtual crystal inside of a
            type `A_3` ambient crystal::

                sage: A = crystals.Tableaux(['A',3], shape=[2,1,1])
                sage: S = A.subcrystal(virtualization={1:[1,3], 2:[2]},
                ....:                  scaling_factors={1:1,2:1}, cartan_type=['B',2])
                sage: B = crystals.Tableaux(['B',2], shape=[1])
                sage: S.digraph().is_isomorphic(B.digraph(), edge_labels=True)
                True

            TESTS:

            Check that :issue:`23942` is fixed::

                sage: B = crystals.infinity.Tableaux(['A',2])
                sage: S = B.subcrystal(max_depth=3, category=HighestWeightCrystals())
                sage: S.category()
                Category of finite highest weight crystals

                sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,3)
                sage: S = K.subcrystal(index_set=[1,3], category=HighestWeightCrystals())
                sage: S.category()
                Category of finite highest weight crystals
            """
        def crystal_morphism(self, on_gens, codomain=None, cartan_type=None, index_set=None, generators=None, automorphism=None, virtualization=None, scaling_factors=None, category=None, check: bool = True):
            '''
            Construct a crystal morphism from ``self`` to another crystal
            ``codomain``.

            INPUT:

            - ``on_gens`` -- a function or list that determines the image
              of the generators (if given a list, then this uses the order
              of the generators of the domain) of ``self`` under the
              crystal morphism
            - ``codomain`` -- (default: ``self``) the codomain of the morphism
            - ``cartan_type`` -- (optional) the Cartan type of the morphism;
              the default is the Cartan type of ``self``
            - ``index_set`` -- (optional) the index set of the morphism;
              the default is the index set of the Cartan type
            - ``generators`` -- (optional) the generators to define the
              morphism; the default is the generators of ``self``
            - ``automorphism`` -- (optional) the automorphism to perform the
              twisting
            - ``virtualization`` -- (optional) a dictionary whose keys are
              in the index set of the domain and whose values are lists of
              entries in the index set of the codomain; the default is the
              identity dictionary
            - ``scaling_factors`` -- (optional) a dictionary whose keys are
              in the index set of the domain and whose values are scaling
              factors for the weight, `\\varepsilon` and `\\varphi`; the
              default are all scaling factors to be one
            - ``category`` -- (optional) the category for the crystal morphism;
              the default is the category of :class:`Crystals`.
            - ``check`` -- boolean (default: ``True``); check if the crystal
              morphism is valid

            .. SEEALSO::

                For more examples, see
                :class:`sage.categories.crystals.CrystalHomset`.

            EXAMPLES:

            We construct the natural embedding of a crystal using tableaux
            into the tensor product of single boxes via the reading word::

                sage: B = crystals.Tableaux([\'A\',2], shape=[2,1])
                sage: F = crystals.Tableaux([\'A\',2], shape=[1])
                sage: T = crystals.TensorProduct(F, F, F)
                sage: mg = T.highest_weight_vectors()[2]; mg
                [[[1]], [[2]], [[1]]]
                sage: psi = B.crystal_morphism([mg], codomain=T); psi
                [\'A\', 2] Crystal morphism:
                  From: The crystal of tableaux of type [\'A\', 2] and shape(s) [[2, 1]]
                  To:   Full tensor product of the crystals
                         [The crystal of tableaux of type [\'A\', 2] and shape(s) [[1]],
                          The crystal of tableaux of type [\'A\', 2] and shape(s) [[1]],
                          The crystal of tableaux of type [\'A\', 2] and shape(s) [[1]]]
                  Defn: [[1, 1], [2]] |--> [[[1]], [[2]], [[1]]]
                sage: b = B.module_generators[0]
                sage: b.pp()
                  1  1
                  2
                sage: psi(b)
                [[[1]], [[2]], [[1]]]
                sage: psi(b.f(2))
                [[[1]], [[3]], [[1]]]
                sage: psi(b.f_string([2,1,1]))
                [[[2]], [[3]], [[2]]]
                sage: lw = b.to_lowest_weight()[0]
                sage: lw.pp()
                  2  3
                  3
                sage: psi(lw)
                [[[3]], [[3]], [[2]]]
                sage: psi(lw) == mg.to_lowest_weight()[0]
                True

            We now take the other isomorphic highest weight component
            in the tensor product::

                sage: mg = T.highest_weight_vectors()[1]; mg
                [[[2]], [[1]], [[1]]]
                sage: psi = B.crystal_morphism([mg], codomain=T)
                sage: psi(lw)
                [[[3]], [[2]], [[3]]]

            We construct a crystal morphism of classical crystals using a
            Kirillov-Reshetikhin crystal::

                sage: B = crystals.Tableaux([\'D\', 4], shape=[1,1])
                sage: K = crystals.KirillovReshetikhin([\'D\',4,1], 2,2)
                sage: K.module_generators
                [[], [[1], [2]], [[1, 1], [2, 2]]]
                sage: v = K.module_generators[1]
                sage: psi = B.crystal_morphism([v], codomain=K, category=FiniteCrystals())
                sage: psi
                [\'D\', 4] -> [\'D\', 4, 1] Virtual Crystal morphism:
                  From: The crystal of tableaux of type [\'D\', 4] and shape(s) [[1, 1]]
                  To:   Kirillov-Reshetikhin crystal of type [\'D\', 4, 1] with (r,s)=(2,2)
                  Defn: [[1], [2]] |--> [[1], [2]]
                sage: b = B.module_generators[0]
                sage: psi(b)
                [[1], [2]]
                sage: psi(b.to_lowest_weight()[0])
                [[-2], [-1]]

            We can define crystal morphisms using a different set of
            generators. For example, we construct an example using the
            lowest weight vector::

                sage: B = crystals.Tableaux([\'A\',2], shape=[1])
                sage: La = RootSystem([\'A\',2]).weight_lattice().fundamental_weights()
                sage: T = crystals.elementary.T([\'A\',2], La[2])
                sage: Bp = T.tensor(B)
                sage: C = crystals.Tableaux([\'A\',2], shape=[2,1])
                sage: x = C.module_generators[0].f_string([1,2])
                sage: psi = Bp.crystal_morphism([x], generators=Bp.lowest_weight_vectors())
                sage: psi(Bp.highest_weight_vector())
                [[1, 1], [2]]

            We can also use a dictionary to specify the generators and
            their images::

                sage: psi = Bp.crystal_morphism({Bp.lowest_weight_vectors()[0]: x})
                sage: psi(Bp.highest_weight_vector())
                [[1, 1], [2]]

            We construct a twisted crystal morphism induced from the diagram
            automorphism of type `A_3^{(1)}`::

                sage: La = RootSystem([\'A\',3,1]).weight_lattice(extended=True).fundamental_weights()
                sage: B0 = crystals.GeneralizedYoungWalls(3, La[0])
                sage: B1 = crystals.GeneralizedYoungWalls(3, La[1])
                sage: phi = B0.crystal_morphism(B1.module_generators, automorphism={0:1, 1:2, 2:3, 3:0})
                sage: phi
                [\'A\', 3, 1] Twisted Crystal morphism:
                  From: Highest weight crystal of generalized Young walls of Cartan type [\'A\', 3, 1] and highest weight Lambda[0]
                  To:   Highest weight crystal of generalized Young walls of Cartan type [\'A\', 3, 1] and highest weight Lambda[1]
                  Defn: [] |--> []
                sage: x = B0.module_generators[0].f_string([0,1,2,3]); x
                [[0, 3], [1], [2]]
                sage: phi(x)
                [[], [1, 0], [2], [3]]

            We construct a virtual crystal morphism from type `G_2` into
            type `D_4`::

                sage: D = crystals.Tableaux([\'D\',4], shape=[1,1])
                sage: G = crystals.Tableaux([\'G\',2], shape=[1])
                sage: psi = G.crystal_morphism(D.module_generators,
                ....:                          virtualization={1:[2],2:[1,3,4]},
                ....:                          scaling_factors={1:1, 2:1})
                sage: for x in G:
                ....:     ascii_art(x, psi(x), sep=\'  |-->  \')
                ....:     print("")
                             1
                  1  |-->    2
                <BLANKLINE>
                             1
                  2  |-->    3
                <BLANKLINE>
                             2
                  3  |-->   -3
                <BLANKLINE>
                             3
                  0  |-->   -3
                <BLANKLINE>
                             3
                 -3  |-->   -2
                <BLANKLINE>
                            -3
                 -2  |-->   -1
                <BLANKLINE>
                            -2
                 -1  |-->   -1
            '''
        def digraph(self, subset=None, index_set=None):
            '''
            Return the :class:`DiGraph` associated to ``self``.

            INPUT:

            - ``subset`` -- (optional) a subset of vertices for
              which the digraph should be constructed

            - ``index_set`` -- (optional) the index set to draw arrows

            EXAMPLES::

                sage: C = Crystals().example(5)
                sage: C.digraph()
                Digraph on 6 vertices

            The edges of the crystal graph are by default colored using
            blue for edge 1, red for edge 2, and green for edge 3::

                sage: C = Crystals().example(3)
                sage: G = C.digraph()
                sage: view(G)  # optional - dot2tex graphviz, not tested (opens external window)

            One may also overwrite the colors::

                sage: C = Crystals().example(3)
                sage: G = C.digraph()
                sage: G.set_latex_options(color_by_label = {1:"red", 2:"purple", 3:"blue"})
                sage: view(G)  # optional - dot2tex graphviz, not tested (opens external window)

            Or one may add colors to yet unspecified edges::

                sage: C = Crystals().example(4)
                sage: G = C.digraph()
                sage: C.cartan_type()._index_set_coloring[4]="purple"
                sage: view(G)  # optional - dot2tex graphviz, not tested (opens external window)

            Here is an example of how to take the top part up to a
            given depth of an infinite dimensional crystal::

                sage: C = CartanType([\'C\',2,1])
                sage: La = C.root_system().weight_lattice().fundamental_weights()
                sage: T = crystals.HighestWeight(La[0])
                sage: S = T.subcrystal(max_depth=3)
                sage: G = T.digraph(subset=S); G
                Digraph on 5 vertices
                sage: G.vertices(sort=True, key=str)
                [(-Lambda[0] + 2*Lambda[1] - delta,),
                 (1/2*Lambda[0] + Lambda[1] - Lambda[2] - 1/2*delta, -1/2*Lambda[0] + Lambda[1] - 1/2*delta),
                 (1/2*Lambda[0] - Lambda[1] + Lambda[2] - 1/2*delta, -1/2*Lambda[0] + Lambda[1] - 1/2*delta),
                 (Lambda[0] - 2*Lambda[1] + 2*Lambda[2] - delta,),
                 (Lambda[0],)]

            Here is a way to construct a picture of a Demazure crystal using
            the ``subset`` option::

                sage: B = crystals.Tableaux([\'A\',2], shape=[2,1])
                sage: t = B.highest_weight_vector()
                sage: D = B.demazure_subcrystal(t, [2,1])
                sage: list(D)
                [[[1, 1], [2]], [[1, 2], [2]], [[1, 1], [3]],
                 [[1, 3], [2]], [[1, 3], [3]]]
                sage: view(D)  # optional - dot2tex graphviz, not tested (opens external window)

            We can also choose to display particular arrows using the
            ``index_set`` option::

                sage: C = crystals.KirillovReshetikhin([\'D\',4,1], 2, 1)
                sage: G = C.digraph(index_set=[1,3])
                sage: len(G.edges(sort=False))
                20
                sage: view(G)  # optional - dot2tex graphviz, not tested (opens external window)

            TESTS:

            We check that infinite crystals raise an error (:issue:`21986`)::

                sage: B = crystals.infinity.Tableaux([\'A\',2])
                sage: B.digraph()
                Traceback (most recent call last):
                ...
                NotImplementedError: crystals not known to be finite
                 must specify either the subset or depth
                sage: B.digraph(depth=10)
                Digraph on 161 vertices

            .. TODO:: Add more tests.
            '''
        def latex_file(self, filename) -> None:
            """
            Export a file, suitable for pdflatex, to ``filename``.

            This requires
            a proper installation of ``dot2tex``. For more
            information see the documentation for ``self.latex()``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', 5])
                sage: fn = tmp_filename(ext='.tex')
                sage: C.latex_file(fn)
            """
        latex: Incomplete
        def metapost(self, filename, thicklines: bool = False, labels: bool = True, scaling_factor: float = 1.0, tallness: float = 1.0) -> None:
            """
            Export a file, suitable for MetaPost, to ``filename``.

            Root operators `e(1)` or `f(1)` move along red lines, `e(2)` or `f(2)`
            along green. The highest weight is in the lower left. Vertices with
            the same weight are kept close together. The concise labels on the
            nodes are strings introduced by Berenstein and Zelevinsky and
            Littelmann; see Littelmann's paper Cones, Crystals, Patterns,
            sections 5 and 6.

            For Cartan types B2 or C2, the pattern has the form

            `a_2 a_3 a_4 a_1`

            where `c*a_2 = a_3 = 2*a_4 = 0` and `a_1=0`, with `c=2` for B2, `c=1` for C2.
            Applying `e(2)` `a_1` times, `e(1)` `a_2` times, `e(2)` `a_3` times, `e(1)` `a_4` times
            returns to the highest weight. (Observe that Littelmann writes the
            roots in opposite of the usual order, so our `e(1)` is his `e(2)` for
            these Cartan types.) For type A2, the pattern has the form

            `a_3 a_2 a_1`

            where applying `e(1)` `a_3` times, `e(2)` `a_2` times then `e(1)` `a_1` times
            returns to the highest weight. These data determine the vertex and
            may be translated into a Gelfand-Tsetlin pattern or tableau.

            INPUT:

            - ``filename`` -- name of the output file, e.g., ``'filename.mp'``

            - ``thicklines`` -- boolean (default: ``True``); for thicker edges

            - ``labels`` -- boolean (default: ``False``); whether to suppress
              labeling of the vertices

            - ``scaling_factor`` -- (default: ``1.0``) increasing or decreasing the
              scaling factor changes the size of the image

            - ``tallness`` -- (default: ``1.0``) increasing makes the image taller
              without increasing the width

            EXAMPLES::

                sage: C = crystals.Letters(['A', 2])
                sage: C.metapost(tmp_filename())

            ::

                sage: C = crystals.Letters(['A', 5])
                sage: C.metapost(tmp_filename())
                Traceback (most recent call last):
                ...
                NotImplementedError
            """
        def dot_tex(self):
            '''
            Return a dot_tex string representation of ``self``.

            EXAMPLES::

                sage: C = crystals.Letters([\'A\',2])
                sage: C.dot_tex()
                \'digraph G { \\n  node [ shape=plaintext ];\\n  N_0 [ label = " ", texlbl = "$1$" ];\\n  N_1 [ label = " ", texlbl = "$2$" ];\\n  N_2 [ label = " ", texlbl = "$3$" ];\\n  N_0 -> N_1 [ label = " ", texlbl = "1" ];\\n  N_1 -> N_2 [ label = " ", texlbl = "2" ];\\n}\'
            '''
        def plot(self, **options):
            """
            Return the plot of ``self`` as a directed graph.

            EXAMPLES::

                sage: C = crystals.Letters(['A', 5])
                sage: print(C.plot())
                Graphics object consisting of 17 graphics primitives
            """
        def plot3d(self, **options):
            """
            Return the 3-dimensional plot of ``self`` as a directed graph.

            EXAMPLES::

                sage: C = crystals.KirillovReshetikhin(['A',3,1],2,1)
                sage: print(C.plot3d())
                Graphics3d Object
            """
        def tensor(self, *crystals, **options):
            """
            Return the tensor product of ``self`` with the crystals ``B``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', 3])
                sage: B = crystals.infinity.Tableaux(['A', 3])
                sage: T = C.tensor(C, B); T
                Full tensor product of the crystals
                 [The crystal of letters for type ['A', 3],
                  The crystal of letters for type ['A', 3],
                  The infinity crystal of tableaux of type ['A', 3]]
                sage: tensor([C, C, B]) is T
                True

                sage: C = crystals.Letters(['A',2])
                sage: T = C.tensor(C, C, generators=[[C(2),C(1),C(1)],[C(1),C(2),C(1)]]); T
                The tensor product of the crystals
                 [The crystal of letters for type ['A', 2],
                  The crystal of letters for type ['A', 2],
                  The crystal of letters for type ['A', 2]]
                sage: T.module_generators
                ([2, 1, 1], [1, 2, 1])
            """
        def direct_sum(self, X):
            """
            Return the direct sum of ``self`` with ``X``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',2], shape=[2,1])
                sage: C = crystals.Letters(['A',2])
                sage: B.direct_sum(C)
                Direct sum of the crystals Family
                (The crystal of tableaux of type ['A', 2] and shape(s) [[2, 1]],
                 The crystal of letters for type ['A', 2])

            As a shorthand, we can use ``+``::

                sage: B + C
                Direct sum of the crystals Family
                (The crystal of tableaux of type ['A', 2] and shape(s) [[2, 1]],
                 The crystal of letters for type ['A', 2])
            """
        __add__ = direct_sum
        def connected_components_generators(self) -> None:
            """
            Return a tuple of generators for each of the connected components
            of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',2], shape=[2,1])
                sage: C = crystals.Letters(['A',2])
                sage: T = crystals.TensorProduct(B,C)
                sage: T.connected_components_generators()
                ([[[1, 1], [2]], 1], [[[1, 2], [2]], 1], [[[1, 2], [3]], 1])
            """
        def connected_components(self):
            """
            Return the connected components of ``self`` as subcrystals.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',2], shape=[2,1])
                sage: C = crystals.Letters(['A',2])
                sage: T = crystals.TensorProduct(B,C)
                sage: T.connected_components()
                [Subcrystal of Full tensor product of the crystals
                 [The crystal of tableaux of type ['A', 2] and shape(s) [[2, 1]],
                  The crystal of letters for type ['A', 2]],
                 Subcrystal of Full tensor product of the crystals
                 [The crystal of tableaux of type ['A', 2] and shape(s) [[2, 1]],
                  The crystal of letters for type ['A', 2]],
                 Subcrystal of Full tensor product of the crystals
                 [The crystal of tableaux of type ['A', 2] and shape(s) [[2, 1]],
                  The crystal of letters for type ['A', 2]]]
            """
        def number_of_connected_components(self):
            """
            Return the number of connected components of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',2], shape=[2,1])
                sage: C = crystals.Letters(['A',2])
                sage: T = crystals.TensorProduct(B,C)
                sage: T.number_of_connected_components()
                3
            """
        def is_connected(self):
            """
            Return ``True`` if ``self`` is a connected crystal.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',2], shape=[2,1])
                sage: C = crystals.Letters(['A',2])
                sage: T = crystals.TensorProduct(B,C)
                sage: B.is_connected()
                True
                sage: T.is_connected()
                False
            """
    class ElementMethods:
        @cached_method
        def index_set(self):
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).index_set()
                (1, 2, 3, 4, 5)
            """
        def cartan_type(self):
            """
            Return the Cartan type associated to ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', 5])
                sage: C(1).cartan_type()
                ['A', 5]
            """
        @abstract_method
        def e(self, i) -> None:
            """
            Return `e_i` of ``self`` if it exists or ``None`` otherwise.

            This method should be implemented by the element class of
            the crystal.

            EXAMPLES::

                sage: C = Crystals().example(5)
                sage: x = C[2]; x
                3
                sage: x.e(1), x.e(2), x.e(3)
                (None, 2, None)
            """
        @abstract_method
        def f(self, i) -> None:
            """
            Return `f_i` of ``self`` if it exists or ``None`` otherwise.

            This method should be implemented by the element class of
            the crystal.

            EXAMPLES::

                sage: C = Crystals().example(5)
                sage: x = C[1]; x
                2
                sage: x.f(1), x.f(2), x.f(3)
                (None, 3, None)
            """
        @abstract_method
        def epsilon(self, i) -> None:
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).epsilon(1)
                0
                sage: C(2).epsilon(1)
                1
            """
        @abstract_method
        def phi(self, i) -> None:
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).phi(1)
                1
                sage: C(2).phi(1)
                0
            """
        @abstract_method
        def weight(self) -> None:
            """
            Return the weight of this crystal element.

            This method should be implemented by the element class of
            the crystal.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).weight()
                (1, 0, 0, 0, 0, 0)
            """
        def phi_minus_epsilon(self, i):
            """
            Return `\\varphi_i - \\varepsilon_i` of ``self``.

            There are sometimes better implementations using the
            weight for this. It is used for reflections along a string.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).phi_minus_epsilon(1)
                1
            """
        def Epsilon(self):
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(0).Epsilon()
                (0, 0, 0, 0, 0, 0)
                sage: C(1).Epsilon()
                (0, 0, 0, 0, 0, 0)
                sage: C(2).Epsilon()
                (1, 0, 0, 0, 0, 0)
            """
        def Phi(self):
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(0).Phi()
                (0, 0, 0, 0, 0, 0)
                sage: C(1).Phi()
                (1, 0, 0, 0, 0, 0)
                sage: C(2).Phi()
                (1, 1, 0, 0, 0, 0)
            """
        def f_string(self, list):
            """
            Applies `f_{i_r} \\cdots f_{i_1}` to ``self`` for ``list`` as
            `[i_1, ..., i_r]`

            EXAMPLES::

                sage: C = crystals.Letters(['A',3])
                sage: b = C(1)
                sage: b.f_string([1,2])
                3
                sage: b.f_string([2,1])
            """
        def e_string(self, list):
            """
            Applies `e_{i_r} \\cdots e_{i_1}` to ``self`` for ``list`` as
            `[i_1, ..., i_r]`

            EXAMPLES::

                sage: C = crystals.Letters(['A',3])
                sage: b = C(3)
                sage: b.e_string([2,1])
                1
                sage: b.e_string([1,2])
            """
        def s(self, i):
            """
            Return the reflection of ``self`` along its `i`-string.

            EXAMPLES::

                sage: C = crystals.Tableaux(['A',2], shape=[2,1])
                sage: b = C(rows=[[1,1],[3]])
                sage: b.s(1)
                [[2, 2], [3]]
                sage: b = C(rows=[[1,2],[3]])
                sage: b.s(2)
                [[1, 2], [3]]
                sage: T = crystals.Tableaux(['A',2],shape=[4])
                sage: t = T(rows=[[1,2,2,2]])
                sage: t.s(1)
                [[1, 1, 1, 2]]
            """
        def is_highest_weight(self, index_set=None):
            """
            Return ``True`` if ``self`` is a highest weight.

            Specifying the option ``index_set`` to be a subset `I` of the
            index set of the underlying crystal, finds all highest
            weight vectors for arrows in `I`.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).is_highest_weight()
                True
                sage: C(2).is_highest_weight()
                False
                sage: C(2).is_highest_weight(index_set = [2,3,4,5])
                True
            """
        def is_lowest_weight(self, index_set=None):
            """
            Return ``True`` if ``self`` is a lowest weight.
            Specifying the option ``index_set`` to be a subset `I` of the
            index set of the underlying crystal, finds all lowest
            weight vectors for arrows in `I`.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C(1).is_lowest_weight()
                False
                sage: C(6).is_lowest_weight()
                True
                sage: C(4).is_lowest_weight(index_set = [1,3])
                True
            """
        def to_highest_weight(self, index_set=None):
            """
            Return the highest weight element `u` and a list `[i_1,...,i_k]`
            such that ``self`` `= f_{i_1} ... f_{i_k} u`, where `i_1,...,i_k` are
            elements in ``index_set``.

            By default the ``index_set`` is assumed to be
            the full index set of ``self``.

            EXAMPLES::

                sage: T = crystals.Tableaux(['A',3], shape = [1])
                sage: t = T(rows = [[3]])
                sage: t.to_highest_weight()
                [[[1]], [2, 1]]
                sage: T = crystals.Tableaux(['A',3], shape = [2,1])
                sage: t = T(rows = [[1,2],[4]])
                sage: t.to_highest_weight()
                [[[1, 1], [2]], [1, 3, 2]]
                sage: t.to_highest_weight(index_set = [3])
                [[[1, 2], [3]], [3]]
                sage: K = crystals.KirillovReshetikhin(['A',3,1],2,1)
                sage: t = K(rows=[[2],[3]]); t.to_highest_weight(index_set=[1])
                [[[1], [3]], [1]]
                sage: t.to_highest_weight()
                Traceback (most recent call last):
                ...
                ValueError: this is not a highest weight crystal
            """
        def to_lowest_weight(self, index_set=None):
            """
            Return the lowest weight element `u` and a list `[i_1,...,i_k]`
            such that ``self`` `= e_{i_1} ... e_{i_k} u`, where `i_1,...,i_k` are
            elements in ``index_set``.

            By default the ``index_set`` is assumed to be the full index
            set of ``self``.

            EXAMPLES::

                sage: T = crystals.Tableaux(['A',3], shape = [1])
                sage: t = T(rows = [[3]])
                sage: t.to_lowest_weight()
                [[[4]], [3]]
                sage: T = crystals.Tableaux(['A',3], shape = [2,1])
                sage: t = T(rows = [[1,2],[4]])
                sage: t.to_lowest_weight()
                [[[3, 4], [4]], [1, 2, 2, 3]]
                sage: t.to_lowest_weight(index_set = [3])
                [[[1, 2], [4]], []]
                sage: K = crystals.KirillovReshetikhin(['A',3,1],2,1)
                sage: t = K.module_generator(); t
                [[1], [2]]
                sage: t.to_lowest_weight(index_set=[1,2,3])
                [[[3], [4]], [2, 1, 3, 2]]
                sage: t.to_lowest_weight()
                Traceback (most recent call last):
                ...
                ValueError: this is not a highest weight crystal
            """
        def all_paths_to_highest_weight(self, index_set=None) -> Generator[Incomplete]:
            '''
            Iterate over all paths to the highest weight from ``self``
            with respect to ``index_set``.

            INPUT:

            - ``index_set`` -- (optional) a subset of the index set of ``self``

            EXAMPLES::

                sage: B = crystals.infinity.Tableaux("A2")
                sage: b0 = B.highest_weight_vector()
                sage: b = b0.f_string([1, 2, 1, 2])
                sage: L = b.all_paths_to_highest_weight()
                sage: list(L)
                [[2, 1, 2, 1], [2, 2, 1, 1]]

                sage: Y = crystals.infinity.GeneralizedYoungWalls(3)
                sage: y0 = Y.highest_weight_vector()
                sage: y = y0.f_string([0, 1, 2, 3, 2, 1, 0])
                sage: list(y.all_paths_to_highest_weight())
                [[0, 1, 2, 3, 2, 1, 0],
                 [0, 1, 3, 2, 2, 1, 0],
                 [0, 3, 1, 2, 2, 1, 0],
                 [0, 3, 2, 1, 1, 0, 2],
                 [0, 3, 2, 1, 1, 2, 0]]

                sage: B = crystals.Tableaux("A3", shape=[4,2,1])
                sage: b0 = B.highest_weight_vector()
                sage: b = b0.f_string([1, 1, 2, 3])
                sage: list(b.all_paths_to_highest_weight())
                [[1, 3, 2, 1], [3, 1, 2, 1], [3, 2, 1, 1]]
            '''
        def subcrystal(self, index_set=None, max_depth=..., direction: str = 'both', contained=None, cartan_type=None, category=None):
            """
            Construct the subcrystal generated by ``self`` using `e_i` and/or
            `f_i` for all `i` in ``index_set``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the index set; if ``None``
              then use the index set of the crystal

            - ``max_depth`` -- (default: infinity) the maximum depth to build

            - ``direction`` -- (default: ``'both'``) the direction to build
              the subcrystal; it can be one of the following:

              - ``'both'`` -- using both `e_i` and `f_i`
              - ``'upper'`` -- using `e_i`
              - ``'lower'`` -- using `f_i`

            - ``contained`` -- (optional) a set (or function) defining the
              containment in the subcrystal

            - ``cartan_type`` -- (optional) specify the Cartan type of the
              subcrystal

            - ``category`` -- (optional) specify the category of the subcrystal

            .. SEEALSO::

                - :meth:`Crystals.ParentMethods.subcrystal()`

            EXAMPLES::

                sage: C = crystals.KirillovReshetikhin(['A',3,1], 1, 2)
                sage: elt = C(1,4)
                sage: list(elt.subcrystal(index_set=[1,3]))
                [[[1, 4]], [[2, 4]], [[1, 3]], [[2, 3]]]
                sage: list(elt.subcrystal(index_set=[1,3], max_depth=1))
                [[[1, 4]], [[2, 4]], [[1, 3]]]
                sage: list(elt.subcrystal(index_set=[1,3], direction='upper'))
                [[[1, 4]], [[1, 3]]]
                sage: list(elt.subcrystal(index_set=[1,3], direction='lower'))
                [[[1, 4]], [[2, 4]]]

            TESTS:

            Check that :issue:`23942` is fixed::

                sage: K = crystals.KirillovReshetikhin(['A',2,1], 1,1)
                sage: cat = HighestWeightCrystals().Finite()
                sage: S = K.module_generator().subcrystal(index_set=[1,2], category=cat)
                sage: S.category()
                Category of finite highest weight crystals
            """
        def tensor(self, *elts):
            """
            Return the tensor product of ``self`` with the crystal
            elements ``elts``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', 3])
                sage: B = crystals.infinity.Tableaux(['A', 3])
                sage: c = C[0]
                sage: b = B.highest_weight_vector()
                sage: t = c.tensor(c, b)
                sage: ascii_art(t)
                          1  1  1
                1 # 1 #   2  2
                          3
                sage: tensor([c, c, b]) == t
                True
                sage: ascii_art(tensor([b, b, c]))
                  1  1  1     1  1  1
                  2  2    #   2  2    # 1
                  3           3
            """
    class SubcategoryMethods:
        """
        Methods for all subcategories.
        """
        def TensorProducts(self):
            """
            Return the full subcategory of objects of ``self`` constructed
            as tensor products.

            .. SEEALSO::

                - :class:`.tensor.TensorProductsCategory`
                - :class:`~.covariant_functorial_construction.RegressiveCovariantFunctorialConstruction`.

            EXAMPLES::

                sage: HighestWeightCrystals().TensorProducts()
                Category of tensor products of highest weight crystals
            """
    class TensorProducts(TensorProductsCategory):
        """
        The category of crystals constructed by tensor product of crystals.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: Crystals().TensorProducts().extra_super_categories()
                [Category of crystals]
            """
    Finite: Incomplete

class CrystalMorphism(Morphism):
    """
    A crystal morphism.

    INPUT:

    - ``parent`` -- a homset
    - ``cartan_type`` -- (optional) a Cartan type; the default is the
      Cartan type of the domain
    - ``virtualization`` -- (optional) a dictionary whose keys are in
      the index set of the domain and whose values are lists of entries
      in the index set of the codomain
    - ``scaling_factors`` -- (optional) a dictionary whose keys are in
      the index set of the domain and whose values are scaling factors
      for the weight, `\\varepsilon` and `\\varphi`
    """
    def __init__(self, parent, cartan_type=None, virtualization=None, scaling_factors=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: H = Hom(B, B)
            sage: psi = H.an_element()
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: psi = Hom(B, B).an_element()
            sage: psi.cartan_type()
            ['A', 2]
        """
    def is_injective(self):
        """
        Return if ``self`` is an injective crystal morphism.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: psi = Hom(B, B).an_element()
            sage: psi.is_injective()
            False
        """
    @cached_method
    def is_surjective(self):
        """
        Check if ``self`` is a surjective crystal morphism.

        EXAMPLES::

            sage: B = crystals.Tableaux(['C',2], shape=[1,1])
            sage: C = crystals.Tableaux(['C',2], ([2,1], [1,1]))
            sage: psi = B.crystal_morphism(C.module_generators[1:], codomain=C)
            sage: psi.is_surjective()
            False
            sage: im_gens = [None, B.module_generators[0]]
            sage: psi = C.crystal_morphism(im_gens, codomain=B)
            sage: psi.is_surjective()
            True

            sage: C = crystals.Tableaux(['A',2], shape=[2,1])
            sage: B = crystals.infinity.Tableaux(['A',2])
            sage: La = RootSystem(['A',2]).weight_lattice().fundamental_weights()
            sage: W = crystals.elementary.T(['A',2], La[1]+La[2])
            sage: T = W.tensor(B)
            sage: mg = T(W.module_generators[0], B.module_generators[0])
            sage: psi = Hom(C,T)([mg])
            sage: psi.is_surjective()
            False
        """
    def __call__(self, x, *args, **kwds):
        """
        Apply this map to ``x``. We need to do special processing
        for ``None``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: F = crystals.Tableaux(['A',2], shape=[1])
            sage: T = crystals.TensorProduct(F, F, F)
            sage: H = Hom(T, B)
            sage: b = B.module_generators[0]
            sage: psi = H((None, b, b, None), generators=T.highest_weight_vectors())
            sage: psi(None)                                                             # needs sage.symbolic
            sage: [psi(v) for v in T.highest_weight_vectors()]
            [None, [[1, 1], [2]], [[1, 1], [2]], None]
        """
    def virtualization(self):
        """
        Return the virtualization sets `\\sigma_i`.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi = B.crystal_morphism(C.module_generators)
            sage: psi.virtualization()
            Finite family {1: (1,), 2: (2,), 3: (3, 4)}
        """
    def scaling_factors(self):
        """
        Return the scaling factors `\\gamma_i`.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi = B.crystal_morphism(C.module_generators)
            sage: psi.scaling_factors()
            Finite family {1: 2, 2: 2, 3: 1}
        """

class CrystalMorphismByGenerators(CrystalMorphism):
    """
    A crystal morphism defined by a set of generators which create a virtual
    crystal inside the codomain.

    INPUT:

    - ``parent`` -- a homset
    - ``on_gens`` -- a function or list that determines the image of the
      generators (if given a list, then this uses the order of the
      generators of the domain) of the domain under ``self``
    - ``cartan_type`` -- (optional) a Cartan type; the default is the
      Cartan type of the domain
    - ``virtualization`` -- (optional) a dictionary whose keys are in
      the index set of the domain and whose values are lists of entries
      in the index set of the codomain
    - ``scaling_factors`` -- (optional) a dictionary whose keys are in
      the index set of the domain and whose values are scaling factors
      for the weight, `\\varepsilon` and `\\varphi`
    - ``gens`` -- (optional) a finite list of generators to define the
      morphism; the default is to use the highest weight vectors of the crystal
    - ``check`` -- boolean (default: ``True``); check if the crystal morphism
      is valid

    .. SEEALSO::

        :meth:`sage.categories.crystals.Crystals.ParentMethods.crystal_morphism`
    """
    def __init__(self, parent, on_gens, cartan_type=None, virtualization=None, scaling_factors=None, gens=None, check: bool = True) -> None:
        """
        Construct a virtual crystal morphism.

        TESTS::

            sage: B = crystals.Tableaux(['D',4], shape=[1])
            sage: H = Hom(B, B)
            sage: d = {1:1, 2:2, 3:4, 4:3}
            sage: psi = H(B.module_generators, automorphism=d)

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: H = Hom(B, C)
            sage: psi = H(C.module_generators)
        """
    def __bool__(self) -> bool:
        """
        Return if ``self`` is a nonzero morphism.

        EXAMPLES::

            sage: B = crystals.elementary.Elementary(['A',2], 2)
            sage: H = Hom(B, B)
            sage: psi = H(B.module_generators)
            sage: bool(psi)
            True
            sage: psi = H(lambda x: None)
            sage: bool(psi)
            False
        """
    def to_module_generator(self, x):
        """
        Return a generator ``mg`` and a path of `e_i` and `f_i` operations
        to ``mg``.

        OUTPUT: a tuple consisting of:

        - a module generator,
        - a list of ``'e'`` and ``'f'`` to denote which operation, and
        - a list of matching indices.

        EXAMPLES::

            sage: B = crystals.elementary.Elementary(['A',2], 2)
            sage: psi = B.crystal_morphism(B.module_generators)
            sage: psi.to_module_generator(B(4))
            (0, ['f', 'f', 'f', 'f'], [2, 2, 2, 2])
            sage: psi.to_module_generator(B(-2))
            (0, ['e', 'e'], [2, 2])
        """
    @cached_method
    def im_gens(self):
        """
        Return the image of the generators of ``self`` as a tuple.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: F = crystals.Tableaux(['A',2], shape=[1])
            sage: T = crystals.TensorProduct(F, F, F)
            sage: H = Hom(T, B)
            sage: b = B.highest_weight_vector()
            sage: psi = H((None, b, b, None), generators=T.highest_weight_vectors())
            sage: psi.im_gens()
            (None, [[1, 1], [2]], [[1, 1], [2]], None)
        """
    def image(self):
        """
        Return the image of ``self`` in the codomain as a
        :class:`~sage.combinat.crystals.subcrystal.Subcrystal`.

        .. WARNING::

            This assumes that ``self`` is a strict crystal morphism.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: H = Hom(B, C)
            sage: psi = H(C.module_generators)
            sage: psi.image()
            Virtual crystal of The crystal of tableaux of type ['D', 4] and shape(s) [[2]] of type ['B', 3]
        """

class CrystalHomset(Homset):
    '''
    The set of crystal morphisms from one crystal to another.

    An `U_q(\\mathfrak{g})` `I`-crystal morphism `\\Psi : B \\to C` is a map
    `\\Psi : B \\cup \\{ 0 \\} \\to C \\cup \\{ 0 \\}` such that:

    - `\\Psi(0) = 0`.
    - If `b \\in B` and `\\Psi(b) \\in C`, then
      `\\mathrm{wt}(\\Psi(b)) = \\mathrm{wt}(b)`,
      `\\varepsilon_i(\\Psi(b)) = \\varepsilon_i(b)`, and
      `\\varphi_i(\\Psi(b)) = \\varphi_i(b)` for all `i \\in I`.
    - If `b, b^{\\prime} \\in B`, `\\Psi(b), \\Psi(b^{\\prime}) \\in C` and
      `f_i b = b^{\\prime}`, then `f_i \\Psi(b) = \\Psi(b^{\\prime})` and
      `\\Psi(b) = e_i \\Psi(b^{\\prime})` for all `i \\in I`.

    If the Cartan type is unambiguous, it is suppressed from the notation.

    We can also generalize the definition of a crystal morphism by considering
    a map of `\\sigma` of the (now possibly different) Dynkin diagrams
    corresponding to `B` and `C` along with scaling factors
    `\\gamma_i \\in \\ZZ` for `i \\in I`. Let `\\sigma_i` denote the orbit of
    `i` under `\\sigma`. We write objects for `B` as `X` with
    corresponding objects of `C` as `\\widehat{X}`.
    Then a *virtual* crystal morphism `\\Psi` is a map such that
    the following holds:

    - `\\Psi(0) = 0`.
    - If `b \\in B` and `\\Psi(b) \\in C`, then for all `j \\in \\sigma_i`:

    .. MATH::

        \\varepsilon_i(b) = \\frac{1}{\\gamma_j} \\widehat{\\varepsilon}_j(\\Psi(b)),
        \\quad \\varphi_i(b) = \\frac{1}{\\gamma_j} \\widehat{\\varphi}_j(\\Psi(b)),
        \\quad \\mathrm{wt}(\\Psi(b)) = \\sum_i c_i \\sum_{j \\in \\sigma_i} \\gamma_j
        \\widehat{\\Lambda}_j,

    where `\\mathrm{wt}(b) = \\sum_i c_i \\Lambda_i`.

    - If `b, b^{\\prime} \\in B`, `\\Psi(b), \\Psi(b^{\\prime}) \\in C` and
      `f_i b = b^{\\prime}`, then independent of the ordering of `\\sigma_i`
      we have:

      .. MATH::

          \\Psi(b^{\\prime}) = e_i \\Psi(b) =
              \\prod_{j \\in \\sigma_i} \\widehat{e}_j^{\\gamma_i} \\Psi(b), \\quad
          \\Psi(b^{\\prime}) = f_i \\Psi(b) =
              \\prod_{j \\in \\sigma_i} \\widehat{f}_j^{\\gamma_i} \\Psi(b).

    If `\\gamma_i = 1` for all `i \\in I` and the Dynkin diagrams are
    the same, then we call `\\Psi` a *twisted* crystal morphism.

    INPUT:

    - ``X`` -- the domain
    - ``Y`` -- the codomain
    - ``category`` -- (optional) the category of the crystal morphisms

    .. SEEALSO::

        For the construction of an element of the homset, see
        :class:`CrystalMorphismByGenerators` and
        :meth:`~sage.categories.crystals.Crystals.ParentMethods.crystal_morphism`.

    EXAMPLES:

    We begin with the natural embedding of `B(2\\Lambda_1)` into
    `B(\\Lambda_1) \\otimes B(\\Lambda_1)` in type `A_1`::

        sage: B = crystals.Tableaux([\'A\',1], shape=[2])
        sage: F = crystals.Tableaux([\'A\',1], shape=[1])
        sage: T = crystals.TensorProduct(F, F)
        sage: v = T.highest_weight_vectors()[0]; v
        [[[1]], [[1]]]
        sage: H = Hom(B, T)
        sage: psi = H([v])
        sage: b = B.highest_weight_vector(); b
        [[1, 1]]
        sage: psi(b)
        [[[1]], [[1]]]
        sage: b.f(1)
        [[1, 2]]
        sage: psi(b.f(1))
        [[[1]], [[2]]]

    We now look at the decomposition of `B(\\Lambda_1) \\otimes B(\\Lambda_1)`
    into `B(2\\Lambda_1) \\oplus B(0)`::

        sage: B0 = crystals.Tableaux([\'A\',1], shape=[])
        sage: D = crystals.DirectSum([B, B0])
        sage: H = Hom(T, D)
        sage: psi = H(D.module_generators)
        sage: psi
        [\'A\', 1] Crystal morphism:
          From: Full tensor product of the crystals
           [The crystal of tableaux of type [\'A\', 1] and shape(s) [[1]],
            The crystal of tableaux of type [\'A\', 1] and shape(s) [[1]]]
          To:   Direct sum of the crystals Family
           (The crystal of tableaux of type [\'A\', 1] and shape(s) [[2]],
            The crystal of tableaux of type [\'A\', 1] and shape(s) [[]])
          Defn: [[[1]], [[1]]] |--> [[1, 1]]
                [[[2]], [[1]]] |--> []
        sage: psi.is_isomorphism()
        True

    We can always construct the trivial morphism which sends
    everything to `0`::

        sage: Binf = crystals.infinity.Tableaux([\'B\', 2])
        sage: B = crystals.Tableaux([\'B\',2], shape=[1])
        sage: H = Hom(Binf, B)
        sage: psi = H(lambda x: None)
        sage: psi(Binf.highest_weight_vector())

    For Kirillov-Reshetikhin crystals, we consider the map to the
    corresponding classical crystal::

        sage: K = crystals.KirillovReshetikhin([\'D\',4,1], 2,1)
        sage: B = K.classical_decomposition()
        sage: H = Hom(K, B)
        sage: psi = H(lambda x: x.lift(), cartan_type=[\'D\',4])
        sage: L = [psi(mg) for mg in K.module_generators]; L
        [[], [[1], [2]]]
        sage: all(x.parent() == B for x in L)
        True

    Next we consider a type `D_4` crystal morphism where we twist by
    `3 \\leftrightarrow 4`::

        sage: B = crystals.Tableaux([\'D\',4], shape=[1])
        sage: H = Hom(B, B)
        sage: d = {1:1, 2:2, 3:4, 4:3}
        sage: psi = H(B.module_generators, automorphism=d)
        sage: b = B.highest_weight_vector()
        sage: b.f_string([1,2,3])
        [[4]]
        sage: b.f_string([1,2,4])
        [[-4]]
        sage: psi(b.f_string([1,2,3]))
        [[-4]]
        sage: psi(b.f_string([1,2,4]))
        [[4]]

    We construct the natural virtual embedding of a type `B_3` into a type
    `D_4` crystal::

        sage: B = crystals.Tableaux([\'B\',3], shape=[1])
        sage: C = crystals.Tableaux([\'D\',4], shape=[2])
        sage: H = Hom(B, C)
        sage: psi = H(C.module_generators)
        sage: psi
        [\'B\', 3] -> [\'D\', 4] Virtual Crystal morphism:
          From: The crystal of tableaux of type [\'B\', 3] and shape(s) [[1]]
          To:   The crystal of tableaux of type [\'D\', 4] and shape(s) [[2]]
          Defn: [[1]] |--> [[1, 1]]
        sage: for b in B: print("{} |--> {}".format(b, psi(b)))
        [[1]] |--> [[1, 1]]
        [[2]] |--> [[2, 2]]
        [[3]] |--> [[3, 3]]
        [[0]] |--> [[3, -3]]
        [[-3]] |--> [[-3, -3]]
        [[-2]] |--> [[-2, -2]]
        [[-1]] |--> [[-1, -1]]
    '''
    def __init__(self, X, Y, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: B = crystals.Tableaux(['A', 2], shape=[2,1])
            sage: H = Hom(B, B)
            sage: Binf = crystals.infinity.Tableaux(['B',2])
            sage: H = Hom(Binf, B)
        """
    def __call__(self, on_gens, cartan_type=None, index_set=None, generators=None, automorphism=None, virtualization=None, scaling_factors=None, check: bool = True):
        """
        Construct a crystal morphism.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A', 2], shape=[2,1])
            sage: H = Hom(B, B)
            sage: psi = H(B.module_generators)

            sage: F = crystals.Tableaux(['A',3], shape=[1])
            sage: T = crystals.TensorProduct(F, F, F)
            sage: H = Hom(B, T)
            sage: v = T.highest_weight_vectors()[2]
            sage: psi = H([v], cartan_type=['A',2])
        """
    Element = CrystalMorphismByGenerators
