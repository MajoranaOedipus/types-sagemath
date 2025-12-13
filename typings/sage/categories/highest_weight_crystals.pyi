from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.crystals import CrystalHomset as CrystalHomset, CrystalMorphismByGenerators as CrystalMorphismByGenerators, Crystals as Crystals
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method

class HighestWeightCrystals(Category_singleton):
    """
    The category of highest weight crystals.

    A crystal is highest weight if it is acyclic; in particular, every
    connected component has a unique highest weight element, and that
    element generate the component.

    EXAMPLES::

        sage: C = HighestWeightCrystals()
        sage: C
        Category of highest weight crystals
        sage: C.super_categories()
        [Category of crystals]
        sage: C.example()
        Highest weight crystal of type A_3 of highest weight omega_1

    TESTS::

        sage: TestSuite(C).run()
        sage: B = HighestWeightCrystals().example()
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

            sage: HighestWeightCrystals().super_categories()
            [Category of crystals]
        """
    def example(self):
        """
        Return an example of highest weight crystals, as per
        :meth:`Category.example`.

        EXAMPLES::

            sage: B = HighestWeightCrystals().example(); B
            Highest weight crystal of type A_3 of highest weight omega_1
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of highest weight crystals defines no
        additional structure: it only guarantees the existence of a
        unique highest weight element in each component.

        .. SEEALSO:: :meth:`Category.additional_structure`

        .. TODO:: Should this category be a :class:`CategoryWithAxiom`?

        EXAMPLES::

            sage: HighestWeightCrystals().additional_structure()
        """
    class ParentMethods:
        @cached_method
        def highest_weight_vectors(self):
            """
            Return the highest weight vectors of ``self``.

            This default implementation selects among the module
            generators those that are highest weight, and caches the result.
            A crystal element `b` is highest weight if `e_i(b)=0` for all `i` in the
            index set.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C.highest_weight_vectors()
                (1,)

            ::

                sage: C = crystals.Letters(['A',2])
                sage: T = crystals.TensorProduct(C, C, C, generators=[[C(2),C(1),C(1)],
                ....:                                                 [C(1),C(2),C(1)]])
                sage: T.highest_weight_vectors()
                ([2, 1, 1], [1, 2, 1])
            """
        def highest_weight_vector(self):
            """
            Return the highest weight vector if there is a single one;
            otherwise, raises an error.

            Caveat: this assumes that :meth:`.highest_weight_vectors`
            returns a list or tuple.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C.highest_weight_vector()
                1
            """
        @cached_method
        def lowest_weight_vectors(self):
            """
            Return the lowest weight vectors of ``self``.

            This default implementation selects among all elements of the crystal
            those that are lowest weight, and cache the result.
            A crystal element `b` is lowest weight if `f_i(b)=0` for all `i` in the
            index set.

            EXAMPLES::

                sage: C = crystals.Letters(['A',5])
                sage: C.lowest_weight_vectors()
                (6,)

            ::

                sage: C = crystals.Letters(['A',2])
                sage: T = crystals.TensorProduct(C, C, C,generators=[[C(2),C(1),C(1)],
                ....:                                                [C(1),C(2),C(1)]])
                sage: T.lowest_weight_vectors()
                ([3, 2, 3], [3, 3, 2])
            """
        def __iter__(self, index_set=None, max_depth=...):
            """
            Return the iterator of ``self``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the index set; if ``None``
              then use the index set of the crystal

            - ``max_depth`` -- (default: infinity) the maximum depth to build

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2,1],[0,1,0])
                sage: sorted([p for p in C.__iter__(max_depth=3)], key=str)
                [(-Lambda[0] + 2*Lambda[2] - delta,),
                 (-Lambda[0] + Lambda[1] + 1/2*Lambda[2] - delta, Lambda[0] - 1/2*Lambda[2]),
                 (1/2*Lambda[0] + Lambda[1] - Lambda[2] - 1/2*delta, -1/2*Lambda[0] + Lambda[2] - 1/2*delta),
                 (2*Lambda[0] - Lambda[2],),
                 (Lambda[0] - Lambda[1] + Lambda[2],),
                 (Lambda[1],)]
                sage: [p for p in C.__iter__(index_set=[0, 1], max_depth=3)]
                [(Lambda[1],), (Lambda[0] - Lambda[1] + Lambda[2],), (-Lambda[0] + 2*Lambda[2] - delta,)]
            """
        @cached_method
        def q_dimension(self, q=None, prec=None, use_product: bool = False):
            """
            Return the `q`-dimension of ``self``.

            Let `B(\\lambda)` denote a highest weight crystal. Recall that
            the degree of the `\\mu`-weight space of `B(\\lambda)` (under
            the principal gradation) is equal to
            `\\langle \\rho^{\\vee}, \\lambda - \\mu \\rangle` where
            `\\langle \\rho^{\\vee}, \\alpha_i \\rangle = 1` for all `i \\in I`
            (in particular, take `\\rho^{\\vee} = \\sum_{i \\in I} h_i`).

            The `q`-dimension of a highest weight crystal `B(\\lambda)` is
            defined as

            .. MATH::

                \\dim_q B(\\lambda) := \\sum_{j \\geq 0} \\dim(B_j) q^j,

            where `B_j` denotes the degree `j` portion of `B(\\lambda)`. This
            can be expressed as the product

            .. MATH::

                \\dim_q B(\\lambda) = \\prod_{\\alpha^{\\vee} \\in \\Delta_+^{\\vee}}
                \\left( \\frac{1 - q^{\\langle \\lambda + \\rho, \\alpha^{\\vee}
                \\rangle}}{1 - q^{\\langle \\rho, \\alpha^{\\vee} \\rangle}}
                \\right)^{\\mathrm{mult}\\, \\alpha},

            where `\\Delta_+^{\\vee}` denotes the set of positive coroots.
            Taking the limit as `q \\to 1` gives the dimension of `B(\\lambda)`.
            For more information, see [Ka1990]_ Section 10.10.

            INPUT:

            - ``q`` -- the (generic) parameter `q`

            - ``prec`` -- (default: ``None``) the precision of the power
              series ring to use if the crystal is not known to be finite
              (i.e. the number of terms returned).
              If ``None``, then the result is returned as a lazy power series.

            - ``use_product`` -- boolean (default: ``False``); if we have a
              finite crystal and ``True``, use the product formula

            EXAMPLES::

                sage: C = crystals.Tableaux(['A',2], shape=[2,1])
                sage: qdim = C.q_dimension(); qdim
                q^4 + 2*q^3 + 2*q^2 + 2*q + 1
                sage: qdim(1)
                8
                sage: len(C) == qdim(1)
                True
                sage: C.q_dimension(use_product=True) == qdim
                True
                sage: C.q_dimension(prec=20)
                q^4 + 2*q^3 + 2*q^2 + 2*q + 1
                sage: C.q_dimension(prec=2)
                2*q + 1

                sage: R.<t> = QQ[]
                sage: C.q_dimension(q=t^2)
                t^8 + 2*t^6 + 2*t^4 + 2*t^2 + 1

                sage: C = crystals.Tableaux(['A',2], shape=[5,2])
                sage: C.q_dimension()
                q^10 + 2*q^9 + 4*q^8 + 5*q^7 + 6*q^6 + 6*q^5
                 + 6*q^4 + 5*q^3 + 4*q^2 + 2*q + 1

                sage: C = crystals.Tableaux(['B',2], shape=[2,1])
                sage: qdim = C.q_dimension(); qdim
                q^10 + 2*q^9 + 3*q^8 + 4*q^7 + 5*q^6 + 5*q^5
                 + 5*q^4 + 4*q^3 + 3*q^2 + 2*q + 1
                sage: qdim == C.q_dimension(use_product=True)
                True

                sage: C = crystals.Tableaux(['D',4], shape=[2,1])
                sage: C.q_dimension()
                q^16 + 2*q^15 + 4*q^14 + 7*q^13 + 10*q^12 + 13*q^11
                 + 16*q^10 + 18*q^9 + 18*q^8 + 18*q^7 + 16*q^6 + 13*q^5
                 + 10*q^4 + 7*q^3 + 4*q^2 + 2*q + 1

            We check with a finite tensor product::

                sage: TP = crystals.TensorProduct(C, C)
                sage: TP.cardinality()
                25600
                sage: qdim = TP.q_dimension(use_product=True); qdim # long time
                q^32 + 2*q^31 + 8*q^30 + 15*q^29 + 34*q^28 + 63*q^27 + 110*q^26
                 + 175*q^25 + 276*q^24 + 389*q^23 + 550*q^22 + 725*q^21
                 + 930*q^20 + 1131*q^19 + 1362*q^18 + 1548*q^17 + 1736*q^16
                 + 1858*q^15 + 1947*q^14 + 1944*q^13 + 1918*q^12 + 1777*q^11
                 + 1628*q^10 + 1407*q^9 + 1186*q^8 + 928*q^7 + 720*q^6
                 + 498*q^5 + 342*q^4 + 201*q^3 + 117*q^2 + 48*q + 26
                sage: qdim(1) # long time
                25600
                sage: TP.q_dimension() == qdim # long time
                True

            The `q`-dimensions of infinite crystals are returned
            as formal power series::

                sage: C = crystals.LSPaths(['A',2,1], [1,0,0])
                sage: C.q_dimension(prec=5)
                1 + q + 2*q^2 + 2*q^3 + 4*q^4 + O(q^5)
                sage: C.q_dimension(prec=10)
                1 + q + 2*q^2 + 2*q^3 + 4*q^4 + 5*q^5 + 7*q^6
                 + 9*q^7 + 13*q^8 + 16*q^9 + O(q^10)
                sage: qdim = C.q_dimension(); qdim
                1 + q + 2*q^2 + 2*q^3 + 4*q^4 + 5*q^5 + 7*q^6 + O(q^7)
                sage: qdim[:16]
                [1, 1, 2, 2, 4, 5, 7, 9, 13, 16, 22, 27, 36, 44, 57, 70]
            """
        connected_components_generators = highest_weight_vectors
        def digraph(self, subset=None, index_set=None, depth=None):
            """
            Return the DiGraph associated to ``self``.

            INPUT:

            - ``subset`` -- (optional) a subset of vertices for
              which the digraph should be constructed

            - ``index_set`` -- (optional) the index set to draw arrows

            - ``depth`` -- the depth to draw; optional only for finite crystals

            EXAMPLES::

                sage: T = crystals.Tableaux(['A',2], shape=[2,1])
                sage: T.digraph()
                Digraph on 8 vertices
                sage: S = T.subcrystal(max_depth=2)
                sage: len(S)
                5
                sage: G = T.digraph(subset=list(S))
                sage: G.is_isomorphic(T.digraph(depth=2), edge_labels=True)
                True

            TESTS:

            The following example demonstrates the speed improvement.
            The speedup in non-affine types is small however::

                sage: depth = 5
                sage: C = crystals.AlcovePaths(['A',2,1], [1,1,0])
                sage: general_digraph = Crystals().parent_class.digraph
                sage: S = C.subcrystal(max_depth=depth, direction='lower')
                sage: %timeit C.digraph(depth=depth) # not tested
                10 loops, best of 3: 48.9 ms per loop
                sage: %timeit general_digraph(C, subset=S) # not tested
                10 loops, best of 3: 96.5 ms per loop
                sage: G1 = C.digraph(depth=depth)
                sage: G2 = general_digraph(C, subset=S)
                sage: G1.is_isomorphic(G2, edge_labels=True)
                True
            """
    class ElementMethods:
        def string_parameters(self, word=None):
            '''
            Return the string parameters of ``self`` corresponding to the
            reduced word ``word``.

            Given a reduced expression `w = s_{i_1} \\cdots s_{i_k}`,
            the string parameters of `b \\in B` corresponding to `w`
            are `(a_1, \\ldots, a_k)` such that

            .. MATH::

                \\begin{aligned}
                e_{i_m}^{a_m} \\cdots e_{i_1}^{a_1} b & \\neq 0 \\\\\n                e_{i_m}^{a_m+1} \\cdots e_{i_1}^{a_1} b & = 0
                \\end{aligned}

            for all `1 \\leq m \\leq k`.

            For connected components isomorphic to `B(\\lambda)` or
            `B(\\infty)`, if `w = w_0` is the longest element of the
            Weyl group, then the path determined by the string
            parametrization terminates at the highest weight vector.

            INPUT:

            - ``word`` -- a word in the alphabet of the index set; if not
              specified and we are in finite type, then this will be some
              reduced expression for the long element determined by the
              Weyl group

            EXAMPLES::

                sage: B = crystals.infinity.NakajimaMonomials([\'A\',3])
                sage: mg = B.highest_weight_vector()
                sage: w0 = [1,2,1,3,2,1]
                sage: mg.string_parameters(w0)
                [0, 0, 0, 0, 0, 0]
                sage: mg.f_string([1]).string_parameters(w0)
                [1, 0, 0, 0, 0, 0]
                sage: mg.f_string([1,1,1]).string_parameters(w0)
                [3, 0, 0, 0, 0, 0]
                sage: mg.f_string([1,1,1,2,2]).string_parameters(w0)
                [1, 2, 2, 0, 0, 0]
                sage: mg.f_string([1,1,1,2,2]) == mg.f_string([1,1,2,2,1])
                True
                sage: x = mg.f_string([1,1,1,2,2,1,3,3,2,1,1,1])
                sage: x.string_parameters(w0)
                [4, 1, 1, 2, 2, 2]
                sage: x.string_parameters([3,2,1,3,2,3])
                [2, 3, 7, 0, 0, 0]
                sage: x == mg.f_string([1]*7 + [2]*3 + [3]*2)
                True

            ::

                sage: B = crystals.infinity.Tableaux("A5")
                sage: b = B(rows=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,6,6,6,6,6,6],
                ....:             [2,2,2,2,2,2,2,2,2,4,5,5,5,6],
                ....:             [3,3,3,3,3,3,3,5],
                ....:             [4,4,4,6,6,6],
                ....:             [5,6]])
                sage: b.string_parameters([1,2,1,3,2,1,4,3,2,1,5,4,3,2,1])
                [0, 1, 1, 1, 1, 0, 4, 4, 3, 0, 11, 10, 7, 7, 6]

                sage: B = crystals.infinity.Tableaux("G2")
                sage: b = B(rows=[[1,1,1,1,1,3,3,0,-3,-3,-2,-2,-1,-1,-1,-1],[2,3,3,3]])
                sage: b.string_parameters([2,1,2,1,2,1])
                [5, 13, 11, 15, 4, 4]
                sage: b.string_parameters([1,2,1,2,1,2])
                [7, 12, 15, 8, 10, 0]

            ::

                sage: C = crystals.Tableaux([\'C\',2], shape=[2,1])
                sage: mg = C.highest_weight_vector()
                sage: lw = C.lowest_weight_vectors()[0]
                sage: lw.string_parameters([1,2,1,2])
                [1, 2, 3, 1]
                sage: lw.string_parameters([2,1,2,1])
                [1, 3, 2, 1]
                sage: lw.e_string([2,1,1,1,2,2,1]) == mg
                True
                sage: lw.e_string([1,2,2,1,1,1,2]) == mg
                True

            TESTS::

                sage: B = crystals.infinity.NakajimaMonomials([\'B\',3])
                sage: mg = B.highest_weight_vector()
                sage: mg.string_parameters()
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                sage: w0 = WeylGroup([\'B\',3]).long_element().reduced_word()
                sage: def f_word(params):
                ....:     return reversed([index for i, index in enumerate(w0)
                ....:                      for _ in range(params[i])])
                sage: all(mg.f_string( f_word(x.value.string_parameters(w0)) ) == x.value
                ....:     for x in B.subcrystal(max_depth=4))
                True

                sage: B = crystals.infinity.NakajimaMonomials([\'A\',2,1])
                sage: mg = B.highest_weight_vector()
                sage: mg.string_parameters()
                Traceback (most recent call last):
                ...
                ValueError: the word must be specified because the
                 Weyl group is not finite
            '''
    class TensorProducts(TensorProductsCategory):
        """
        The category of highest weight crystals constructed by tensor
        product of highest weight crystals.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: HighestWeightCrystals().TensorProducts().extra_super_categories()
                [Category of highest weight crystals]
            """
        class ParentMethods:
            """
            Implement operations on tensor products of crystals.
            """
            @cached_method
            def highest_weight_vectors(self):
                """
                Return the highest weight vectors of ``self``.

                This works by using a backtracing algorithm since if
                `b_2 \\otimes b_1` is highest weight then `b_1` is
                highest weight.

                EXAMPLES::

                    sage: C = crystals.Tableaux(['D',4], shape=[2,2])
                    sage: D = crystals.Tableaux(['D',4], shape=[1])
                    sage: T = crystals.TensorProduct(D, C)
                    sage: T.highest_weight_vectors()
                    ([[[1]], [[1, 1], [2, 2]]],
                     [[[3]], [[1, 1], [2, 2]]],
                     [[[-2]], [[1, 1], [2, 2]]])
                    sage: L = filter(lambda x: x.is_highest_weight(), T)
                    sage: tuple(L) == T.highest_weight_vectors()
                    True

                TESTS:

                We check this works with Kashiwara's convention for
                tensor products::

                    sage: C = crystals.Tableaux(['B',3], shape=[2,2])
                    sage: D = crystals.Tableaux(['B',3], shape=[1])
                    sage: T = crystals.TensorProduct(D, C)
                    sage: T.options(convention='Kashiwara')
                    sage: T.highest_weight_vectors()
                    ([[[1, 1], [2, 2]], [[1]]],
                     [[[1, 1], [2, 2]], [[3]]],
                     [[[1, 1], [2, 2]], [[-2]]])
                    sage: T.options._reset()
                    sage: T.highest_weight_vectors()
                    ([[[1]], [[1, 1], [2, 2]]],
                     [[[3]], [[1, 1], [2, 2]]],
                     [[[-2]], [[1, 1], [2, 2]]])
                """
            def highest_weight_vectors_iterator(self) -> Generator[Incomplete, None, Incomplete]:
                '''
                Iterate over the highest weight vectors of ``self``.

                This works by using a backtracing algorithm since if
                `b_2 \\otimes b_1` is highest weight then `b_1` is
                highest weight.

                EXAMPLES::

                    sage: C = crystals.Tableaux([\'D\',4], shape=[2,2])
                    sage: D = crystals.Tableaux([\'D\',4], shape=[1])
                    sage: T = crystals.TensorProduct(D, C)
                    sage: tuple(T.highest_weight_vectors_iterator())
                    ([[[1]], [[1, 1], [2, 2]]],
                     [[[3]], [[1, 1], [2, 2]]],
                     [[[-2]], [[1, 1], [2, 2]]])
                    sage: L = filter(lambda x: x.is_highest_weight(), T)
                    sage: tuple(L) == tuple(T.highest_weight_vectors_iterator())
                    True

                TESTS:

                We check this works with Kashiwara\'s convention for
                tensor products::

                    sage: C = crystals.Tableaux([\'B\',3], shape=[2,2])
                    sage: D = crystals.Tableaux([\'B\',3], shape=[1])
                    sage: T = crystals.TensorProduct(D, C)
                    sage: T.options(convention=\'Kashiwara\')
                    sage: tuple(T.highest_weight_vectors_iterator())
                    ([[[1, 1], [2, 2]], [[1]]],
                     [[[1, 1], [2, 2]], [[3]]],
                     [[[1, 1], [2, 2]], [[-2]]])
                    sage: T.options._reset()
                    sage: tuple(T.highest_weight_vectors_iterator())
                    ([[[1]], [[1, 1], [2, 2]]],
                     [[[3]], [[1, 1], [2, 2]]],
                     [[[-2]], [[1, 1], [2, 2]]])

                This currently is not implemented for infinite crystals::

                    sage: P = RootSystem([\'A\',3,1]).weight_lattice(extended=True)
                    sage: M = crystals.NakajimaMonomials(P.fundamental_weight(0))
                    sage: T = tensor([M, M])
                    sage: list(T.highest_weight_vectors_iterator())
                    Traceback (most recent call last):
                    ...
                    NotImplementedError: not implemented for infinite crystals

                Check that :issue:`30493` is fixed::

                    sage: CW = CartanType("G", 2)
                    sage: C = crystals.Letters(CW)
                    sage: C.highest_weight_vectors()
                    (1,)
                    sage: T = crystals.TensorProduct(C)
                    sage: T.highest_weight_vectors()
                    ([1],)
                '''

class HighestWeightCrystalMorphism(CrystalMorphismByGenerators):
    """
    A virtual crystal morphism whose domain is a highest weight crystal.

    INPUT:

    - ``parent`` -- a homset
    - ``on_gens`` -- a function or list that determines the image of the
      generators (if given a list, then this uses the order of the
      generators of the domain) of the domain under ``self``
    - ``cartan_type`` -- (optional) a Cartan type; the default is the
      Cartan type of the domain
    - ``virtualization`` -- (optional) a dictionary whose keys are
      in the index set of the domain and whose values are lists of
      entries in the index set of the codomain
    - ``scaling_factors`` -- (optional) a dictionary whose keys are in
      the index set of the domain and whose values are scaling factors
      for the weight, `\\varepsilon` and `\\varphi`
    - ``gens`` -- (optional) a list of generators to define the morphism;
      the default is to use the highest weight vectors of the crystal
    - ``check`` -- boolean (default: ``True``); check if the crystal morphism
      is valid
    """
    def __init__(self, parent, on_gens, cartan_type=None, virtualization=None, scaling_factors=None, gens=None, check: bool = True) -> None:
        """
        Construct a crystal morphism.

        TESTS::

            sage: B = crystals.infinity.Tableaux(['B',2])
            sage: C = crystals.infinity.NakajimaMonomials(['B',2])
            sage: psi = B.crystal_morphism(C.module_generators)

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: H = Hom(B, C)
            sage: psi = H(C.module_generators)
        """

class HighestWeightCrystalHomset(CrystalHomset):
    """
    The set of crystal morphisms from a highest weight crystal to
    another crystal.

    .. SEEALSO::

        See :class:`sage.categories.crystals.CrystalHomset` for more
        information.
    """
    def __init__(self, X, Y, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: B = crystals.Tableaux(['A', 2], shape=[2,1])
            sage: H = Hom(B, B)
            sage: B = crystals.infinity.Tableaux(['B',2])
            sage: H = Hom(B, B)
        """
    Element = HighestWeightCrystalMorphism
