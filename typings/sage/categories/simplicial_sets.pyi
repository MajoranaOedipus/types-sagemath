from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.categories.sets_cat import Sets as Sets
from sage.functions.generalized import sign as sign
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class SimplicialSets(Category_singleton):
    """
    The category of simplicial sets.

    A simplicial set `X` is a collection of sets `X_i`, indexed by
    the nonnegative integers, together with maps

    .. math::

        d_i: X_n \\to X_{n-1}, \\quad 0 \\leq i \\leq n \\quad \\text{(face maps)} \\\\\n        s_j: X_n \\to X_{n+1}, \\quad 0 \\leq j \\leq n \\quad \\text{(degeneracy maps)}

    satisfying the *simplicial identities*:

    .. math::

        d_i d_j &= d_{j-1} d_i \\quad \\text{if } i<j \\\\\n        d_i s_j &= s_{j-1} d_i \\quad \\text{if } i<j \\\\\n        d_j s_j &= 1 = d_{j+1} s_j \\\\\n        d_i s_j &= s_{j} d_{i-1} \\quad \\text{if } i>j+1 \\\\\n        s_i s_j &= s_{j+1} s_{i} \\quad \\text{if } i \\leq j

    Morphisms are sequences of maps `f_i : X_i \\to Y_i` which commute
    with the face and degeneracy maps.

    EXAMPLES::

        sage: from sage.categories.simplicial_sets import SimplicialSets
        sage: C = SimplicialSets(); C
        Category of simplicial sets

    TESTS::

        sage: TestSuite(C).run()
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.simplicial_sets import SimplicialSets
            sage: SimplicialSets().super_categories()
            [Category of sets]
        """
    class ParentMethods:
        def is_finite(self):
            """
            Return ``True`` if this simplicial set is finite, i.e., has a
            finite number of nondegenerate simplices.

            EXAMPLES::

                sage: simplicial_sets.Torus().is_finite()                               # needs sage.graphs
                True
                sage: C5 = groups.misc.MultiplicativeAbelian([5])                       # needs sage.graphs sage.groups
                sage: simplicial_sets.ClassifyingSpace(C5).is_finite()                  # needs sage.graphs sage.groups
                False
            """
        def is_pointed(self):
            """
            Return ``True`` if this simplicial set is pointed, i.e., has a
            base point.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
                sage: v = AbstractSimplex(0)
                sage: w = AbstractSimplex(0)
                sage: e = AbstractSimplex(1)
                sage: X = SimplicialSet({e: (v, w)})
                sage: Y = SimplicialSet({e: (v, w)}, base_point=w)
                sage: X.is_pointed()
                False
                sage: Y.is_pointed()
                True
            """
        def set_base_point(self, point):
            '''
            Return a copy of this simplicial set in which the base point is
            set to ``point``.

            INPUT:

            - ``point`` -- a 0-simplex in this simplicial set

            EXAMPLES::

                sage: # needs sage.graphs
                sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
                sage: v = AbstractSimplex(0, name=\'v_0\')
                sage: w = AbstractSimplex(0, name=\'w_0\')
                sage: e = AbstractSimplex(1)
                sage: X = SimplicialSet({e: (v, w)})
                sage: Y = SimplicialSet({e: (v, w)}, base_point=w)
                sage: Y.base_point()
                w_0
                sage: X_star = X.set_base_point(w)
                sage: X_star.base_point()
                w_0
                sage: Y_star = Y.set_base_point(v)
                sage: Y_star.base_point()
                v_0

            TESTS::

                sage: X.set_base_point(e)                                               # needs sage.graphs
                Traceback (most recent call last):
                ...
                ValueError: the "point" is not a zero-simplex
                sage: pt = AbstractSimplex(0)                                           # needs sage.graphs
                sage: X.set_base_point(pt)                                              # needs sage.graphs
                Traceback (most recent call last):
                ...
                ValueError: the point is not a simplex in this simplicial set
            '''
    class Homsets(HomsetsCategory):
        class Endset(CategoryWithAxiom):
            class ParentMethods:
                def one(self):
                    """
                    Return the identity morphism in `\\operatorname{Hom}(S, S)`.

                    EXAMPLES::

                        sage: T = simplicial_sets.Torus()                               # needs sage.graphs
                        sage: Hom(T, T).identity()                                      # needs sage.graphs
                        Simplicial set endomorphism of Torus
                          Defn: Identity map
                    """
    class Finite(CategoryWithAxiom):
        """
        Category of finite simplicial sets.

        The objects are simplicial sets with finitely many
        non-degenerate simplices.
        """
    class SubcategoryMethods:
        def Pointed(self):
            """
            A simplicial set is *pointed* if it has a distinguished base
            point.

            EXAMPLES::

                sage: from sage.categories.simplicial_sets import SimplicialSets
                sage: SimplicialSets().Pointed().Finite()
                Category of finite pointed simplicial sets
                sage: SimplicialSets().Finite().Pointed()
                Category of finite pointed simplicial sets
            """
    class Pointed(CategoryWithAxiom):
        class ParentMethods:
            def base_point(self):
                """
                Return this simplicial set's base point.

                EXAMPLES::

                    sage: # needs sage.graphs
                    sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
                    sage: v = AbstractSimplex(0, name='*')
                    sage: e = AbstractSimplex(1)
                    sage: S1 = SimplicialSet({e: (v, v)}, base_point=v)
                    sage: S1.is_pointed()
                    True
                    sage: S1.base_point()
                    *
                """
            def base_point_map(self, domain=None):
                """
                Return a map from a one-point space to this one, with image the
                base point.

                This raises an error if this simplicial set does not have a
                base point.

                INPUT:

                - ``domain`` -- (default: ``None``) use this to specify a
                  particular one-point space as the domain. The default
                  behavior is to use the
                  :func:`sage.topology.simplicial_set.Point` function to use a
                  standard one-point space.

                EXAMPLES::

                    sage: # needs sage.graphs
                    sage: T = simplicial_sets.Torus()
                    sage: f = T.base_point_map(); f
                    Simplicial set morphism:
                      From: Point
                      To:   Torus
                      Defn: Constant map at (v_0, v_0)
                    sage: S3 = simplicial_sets.Sphere(3)
                    sage: g = S3.base_point_map()
                    sage: f.domain() == g.domain()
                    True
                    sage: RP3 = simplicial_sets.RealProjectiveSpace(3)                  # needs sage.groups
                    sage: temp = simplicial_sets.Simplex(0)
                    sage: pt = temp.set_base_point(temp.n_cells(0)[0])
                    sage: h = RP3.base_point_map(domain=pt)                             # needs sage.groups
                    sage: f.domain() == h.domain()                                      # needs sage.groups
                    False

                    sage: C5 = groups.misc.MultiplicativeAbelian([5])                   # needs sage.graphs sage.groups
                    sage: BC5 = simplicial_sets.ClassifyingSpace(C5)                    # needs sage.graphs sage.groups
                    sage: BC5.base_point_map()                                          # needs sage.graphs sage.groups
                    Simplicial set morphism:
                      From: Point
                      To:   Classifying space of Multiplicative Abelian group isomorphic to C5
                      Defn: Constant map at 1
                """
            def fundamental_group(self, simplify: bool = True):
                """
                Return the fundamental group of this pointed simplicial set.

                INPUT:

                - ``simplify`` -- boolean (default: ``True``); if
                  ``False``, then return a presentation of the group
                  in terms of generators and relations. If ``True``,
                  the default, simplify as much as GAP is able to.

                Algorithm: we compute the edge-path group -- see
                Section 19 of [Kan1958]_ and
                :wikipedia:`Fundamental_group`. Choose a spanning tree
                for the connected component of the 1-skeleton
                containing the base point, and then the group's
                generators are given by the non-degenerate
                edges. There are two types of relations: `e=1` if `e`
                is in the spanning tree, and for every 2-simplex, if
                its faces are `e_0`, `e_1`, and `e_2`, then we impose
                the relation `e_0 e_1^{-1} e_2 = 1`, where we first
                set `e_i=1` if `e_i` is degenerate.

                EXAMPLES::

                    sage: S1 = simplicial_sets.Sphere(1)                                # needs sage.graphs
                    sage: eight = S1.wedge(S1)                                          # needs sage.graphs
                    sage: eight.fundamental_group()  # free group on 2 generators       # needs sage.graphs sage.groups
                    Finitely presented group < e0, e1 |  >

                The fundamental group of a disjoint union of course depends on
                the choice of base point::

                    sage: T = simplicial_sets.Torus()                                   # needs sage.graphs
                    sage: K = simplicial_sets.KleinBottle()                             # needs sage.graphs
                    sage: X = T.disjoint_union(K)                                       # needs sage.graphs

                    sage: # needs sage.graphs
                    sage: X_0 = X.set_base_point(X.n_cells(0)[0])
                    sage: X_0.fundamental_group().is_abelian()                          # needs sage.groups
                    True
                    sage: X_1 = X.set_base_point(X.n_cells(0)[1])
                    sage: X_1.fundamental_group().is_abelian()                          # needs sage.groups
                    False

                    sage: RP3 = simplicial_sets.RealProjectiveSpace(3)                  # needs sage.graphs sage.groups
                    sage: RP3.fundamental_group()                                       # needs sage.graphs sage.groups
                    Finitely presented group < e | e^2 >

                Compute the fundamental group of some classifying spaces::

                    sage: C5 = groups.misc.MultiplicativeAbelian([5])                   # needs sage.graphs sage.groups
                    sage: BC5 = C5.nerve()                                              # needs sage.graphs sage.groups
                    sage: BC5.fundamental_group()                                       # needs sage.graphs sage.groups
                    Finitely presented group < e0 | e0^5 >

                    sage: # needs sage.graphs sage.groups
                    sage: Sigma3 = groups.permutation.Symmetric(3)
                    sage: BSigma3 = Sigma3.nerve()
                    sage: pi = BSigma3.fundamental_group(); pi
                    Finitely presented group < e1, e2 | e2^2, e1^3, (e2*e1)^2 >
                    sage: pi.order()
                    6
                    sage: pi.is_abelian()
                    False

                The sphere has a trivial fundamental group::

                    sage: S2 = simplicial_sets.Sphere(2)                                # needs sage.graphs
                    sage: S2.fundamental_group()                                        # needs sage.graphs sage.groups
                    Finitely presented group <  |  >
                """
            def universal_cover_map(self):
                """
                Return the universal covering map of the simplicial set.

                It requires the fundamental group to be finite.

                EXAMPLES::

                    sage: RP2 = simplicial_sets.RealProjectiveSpace(2)                  # needs sage.graphs sage.groups
                    sage: phi = RP2.universal_cover_map(); phi                          # needs sage.graphs sage.groups gap_package_polenta
                    Simplicial set morphism:
                      From: Simplicial set with 6 non-degenerate simplices
                      To:   RP^2
                      Defn: [(1, 1), (1, e), (f, 1), (f, e), (f * f, 1), (f * f, e)]
                            --> [1, 1, f, f, f * f, f * f]
                    sage: phi.domain().face_data()                                      # needs sage.graphs sage.groups gap_package_polenta
                        {(1, 1): None,
                         (1, e): None,
                         (f, 1): ((1, e), (1, 1)),
                         (f, e): ((1, 1), (1, e)),
                         (f * f, 1): ((f, e), s_0 (1, 1), (f, 1)),
                         (f * f, e): ((f, 1), s_0 (1, e), (f, e))}
                """
            def covering_map(self, character):
                '''
                Return the covering map associated to a character.

                The character is represented by a dictionary that assigns an
                element of a finite group to each nondegenerate 1-dimensional
                cell. It should correspond to an epimorphism from the fundamental
                group.

                INPUT:

                - ``character`` -- dictionary

                EXAMPLES::

                    sage: # needs sage.graphs sage.groups
                    sage: S1 = simplicial_sets.Sphere(1)
                    sage: S1_ = simplicial_sets.Sphere(1)
                    sage: S1_.n_cells(1)[0].rename("sigma_1\'")
                    sage: W = S1.wedge(S1_)
                    sage: G = CyclicPermutationGroup(3)
                    sage: a, b = W.n_cells(1)
                    sage: C = W.covering_map({a : G.gen(0), b : G.one()}); C
                    Simplicial set morphism:
                      From: Simplicial set with 9 non-degenerate simplices
                      To:   Wedge: (S^1 v S^1)
                      Defn: [(*, ()), (*, (1,2,3)), (*, (1,3,2)), (sigma_1\', ()),
                             (sigma_1\', (1,2,3)), (sigma_1\', (1,3,2)), (sigma_1, ()),
                             (sigma_1, (1,2,3)), (sigma_1, (1,3,2))]
                            --> [*, *, *, sigma_1\', sigma_1\', sigma_1\', sigma_1, sigma_1, sigma_1]
                    sage: C.domain()
                    Simplicial set with 9 non-degenerate simplices
                    sage: C.domain().face_data()
                    {(*, ()): None,
                     (*, (1,2,3)): None,
                     (*, (1,3,2)): None,
                     (sigma_1\', ()): ((*, ()), (*, ())),
                     (sigma_1\', (1,2,3)): ((*, (1,2,3)), (*, (1,2,3))),
                     (sigma_1\', (1,3,2)): ((*, (1,3,2)), (*, (1,3,2))),
                     (sigma_1, ()): ((*, (1,2,3)), (*, ())),
                     (sigma_1, (1,2,3)): ((*, (1,3,2)), (*, (1,2,3))),
                     (sigma_1, (1,3,2)): ((*, ()), (*, (1,3,2)))}
                '''
            def cover(self, character):
                '''
                Return the cover of the simplicial set associated to a character
                of the fundamental group.

                The character is represented by a dictionary, that assigns an
                element of a finite group to each nondegenerate 1-dimensional
                cell. It should correspond to an epimorphism from the fundamental
                group.

                INPUT:

                - ``character`` -- dictionary

                EXAMPLES::

                    sage: # needs sage.graphs sage.groups
                    sage: S1 = simplicial_sets.Sphere(1)
                    sage: S1_ = simplicial_sets.Sphere(1)
                    sage: S1_.n_cells(1)[0].rename("sigma_1\'")
                    sage: W = S1.wedge(S1_)
                    sage: G = CyclicPermutationGroup(3)
                    sage: (a, b) = W.n_cells(1)
                    sage: C = W.cover({a : G.gen(0), b : G.gen(0)^2})
                    sage: C.face_data()
                    {(*, ()): None,
                     (*, (1,2,3)): None,
                     (*, (1,3,2)): None,
                     (sigma_1\', ()): ((*, (1,3,2)), (*, ())),
                     (sigma_1\', (1,2,3)): ((*, ()), (*, (1,2,3))),
                     (sigma_1\', (1,3,2)): ((*, (1,2,3)), (*, (1,3,2))),
                     (sigma_1, ()): ((*, (1,2,3)), (*, ())),
                     (sigma_1, (1,2,3)): ((*, (1,3,2)), (*, (1,2,3))),
                     (sigma_1, (1,3,2)): ((*, ()), (*, (1,3,2)))}
                    sage: C.homology(1)                                                 # needs sage.modules
                    Z x Z x Z x Z
                    sage: C.fundamental_group()
                    Finitely presented group < e0, e1, e2, e3 |  >
                '''
            def universal_cover(self):
                """
                Return the universal cover of the simplicial set.
                The fundamental group must be finite in order to ensure that the
                universal cover is a simplicial set of finite type.

                EXAMPLES::

                    sage: # needs sage.graphs sage.groups
                    sage: RP3 = simplicial_sets.RealProjectiveSpace(3)
                    sage: C = RP3.universal_cover(); C
                    Simplicial set with 8 non-degenerate simplices
                    sage: C.face_data()  # needs gap_package_polenta
                    {(1, 1): None,
                     (1, e): None,
                     (f, 1): ((1, e), (1, 1)),
                     (f, e): ((1, 1), (1, e)),
                     (f * f, 1): ((f, e), s_0 (1, 1), (f, 1)),
                     (f * f, e): ((f, 1), s_0 (1, e), (f, e)),
                     (f * f * f, 1): ((f * f, e), s_0 (f, 1), s_1 (f, 1), (f * f, 1)),
                     (f * f * f, e): ((f * f, 1), s_0 (f, e), s_1 (f, e), (f * f, e))}
                    sage: C.fundamental_group()
                    Finitely presented group <  |  >

                TESTS::

                    sage: RP2 = simplicial_sets.RealProjectiveSpace(2)
                    sage: S3 = simplicial_sets.Sphere(3)
                    sage: X = S3.wedge(RP2)
                    sage: XU = X.universal_cover()
                    sage: [XU.homology(i) for i in range(5)]
                    [0, 0, Z, Z x Z, 0]

                """
            def twisted_chain_complex(self, twisting_operator=None, dimensions=None, augmented: bool = False, cochain: bool = False, verbose: bool = False, subcomplex=None, check: bool = False):
                """
                Return the normalized chain complex twisted by some operator.

                A twisting operator is a map from the set of simplices to some algebra.
                The differentials are then twisted by this operator.

                INPUT:

                - ``twisting_operator`` -- dictionary, associating the twist of each
                  simplex. If it is not given, the canonical one (associated to the
                  laurent polynomial ring abelianization of the fundamental group, ignoring
                  torsion) is used.

                - ``dimensions`` -- if ``None``, compute the chain complex in all
                  dimensions.  If a list or tuple of integers, compute the
                  chain complex in those dimensions, setting the chain groups
                  in all other dimensions to zero.

                - ``augmented`` -- boolean (default: ``False``); if ``True``,
                  return the augmented chain complex (that is, include a class
                  in dimension `-1` corresponding to the empty cell).

                - ``cochain`` -- boolean (default: ``False``); if ``True``,
                  return the cochain complex (that is, the dual of the chain
                  complex).

                - ``verbose`` -- boolean (default: ``False``); ignored

                - ``subcomplex`` -- (default: ``None``) if present,
                  compute the chain complex relative to this subcomplex

                - ``check`` -- boolean (default: ``False``); if ``True``, make
                  sure that the chain complex is actually a chain complex:
                  the differentials are composable and their product is zero.

                The normalized chain complex of a simplicial set is isomorphic
                to the chain complex obtained by modding out by degenerate
                simplices, and the latter is what is actually constructed
                here.

                EXAMPLES::

                    sage: # needs sage.graphs
                    sage: W = simplicial_sets.Sphere(1).wedge(simplicial_sets.Sphere(2))
                    sage: W.nondegenerate_simplices()
                    [*, sigma_1, sigma_2]
                    sage: s1 = W.nondegenerate_simplices()[1]
                    sage: L.<t> = LaurentPolynomialRing(QQ)
                    sage: tw = {s1:t}
                    sage: ChC = W.twisted_chain_complex(tw)
                    sage: ChC.differential(1)
                    [-1 + t]
                    sage: ChC.differential(2)
                    [0]

                ::

                    sage: # needs sage.graphs
                    sage: X = simplicial_sets.Torus()
                    sage: C = X.twisted_chain_complex()
                    sage: C.differential(1)
                    [      f2 - 1 f1*f2^-1 - 1       f1 - 1]
                    sage: C.differential(2)
                    [       1 f1*f2^-1]
                    [      f2        1]
                    [      -1       -1]
                    sage: C.differential(3)
                    []

                ::

                    sage: # needs sage.graphs
                    sage: Y = simplicial_sets.RealProjectiveSpace(2)
                    sage: C = Y.twisted_chain_complex()
                    sage: C.differential(1)
                    [-1 + F1]
                    sage: C.differential(2)
                    [1 + F1]
                    sage: C.differential(3)
                    []
                """
            def twisted_homology(self, n, reduced: bool = False):
                '''
                The `n`-th twisted homology module of the simplicial set with respect to
                the abelianization of the fundamental_group.

                It is a module over a polynomial ring, including relations to make some
                variables the multiplicative inverses of others.

                INPUT:

                - ``n`` -- positive integer

                - ``reduced`` -- boolean (default: ``False``); if set to True,
                  the presentation matrix will be reduced

                EXAMPLES::

                    sage: # needs sage.graphs
                    sage: X = simplicial_sets.Sphere(1).wedge(simplicial_sets.Sphere(2))
                    sage: X.twisted_homology(1)
                    Quotient module by Submodule of Ambient free module of rank 0 over the integral domain Multivariate Polynomial Ring in f1, f1inv over Integer Ring
                    Generated by the rows of the matrix:
                    []
                    sage: X.twisted_homology(2)
                    Quotient module by Submodule of Ambient free module of rank 1 over the integral domain Multivariate Polynomial Ring in f1, f1inv over Integer Ring
                    Generated by the rows of the matrix:
                    [f1*f1inv - 1]

                ::

                    sage: # needs sage.graphs
                    sage: Y = simplicial_sets.Torus()
                    sage: Y.twisted_homology(1)
                    Quotient module by Submodule of Ambient free module of rank 5 over the integral domain Multivariate Polynomial Ring in f1, f1inv, f2, f2inv over Integer Ring
                    Generated by the rows of the matrix:
                    [           1            0            0            0            0]
                    [           0            1            0            0            0]
                    [           0            0            1            0            0]
                    [           0            0            0            1            0]
                    [           0            0            0            0            1]
                    [f1*f1inv - 1            0            0            0            0]
                    [           0 f1*f1inv - 1            0            0            0]
                    [           0            0 f1*f1inv - 1            0            0]
                    [           0            0            0 f1*f1inv - 1            0]
                    [           0            0            0            0 f1*f1inv - 1]
                    [f2*f2inv - 1            0            0            0            0]
                    [           0 f2*f2inv - 1            0            0            0]
                    [           0            0 f2*f2inv - 1            0            0]
                    [           0            0            0 f2*f2inv - 1            0]
                    [           0            0            0            0 f2*f2inv - 1]
                    sage: Y.twisted_homology(2)
                    Quotient module by Submodule of Ambient free module of rank 0 over the integral domain Multivariate Polynomial Ring in f1, f1inv, f2, f2inv over Integer Ring
                    Generated by the rows of the matrix:
                    []
                    sage: Y.twisted_homology(1, reduced=True)
                    Quotient module by Submodule of Ambient free module of rank 5 over the integral domain Multivariate Polynomial Ring in f1, f1inv, f2, f2inv over Integer Ring
                    Generated by the rows of the matrix:
                    [1 0 0 0 0]
                    [0 1 0 0 0]
                    [0 0 1 0 0]
                    [0 0 0 1 0]
                    [0 0 0 0 1]

                TESTS::

                    sage: # needs sage.graphs
                    sage: X = simplicial_sets.PresentationComplex(groups.presentation.FGAbelian((3,2)))
                    sage: TW2 = X.twisted_homology(2, reduced=True)
                    sage: M = TW2.relations_matrix()
                    sage: from sage.libs.singular.function import singular_function
                    sage: vdim = singular_function("vdim")
                    sage: vdim(M.T, ring=M.base_ring())
                    // ** considering the image in Q[...]
                    // ** _ is no standard basis
                    5
                    sage: X.universal_cover().homology(2)
                    Z^5
                    sage: from sage.libs.singular.function import singular_function
                '''
            def is_simply_connected(self):
                """
                Return ``True`` if this pointed simplicial set is simply connected.

                .. WARNING::

                    Determining simple connectivity is not always
                    possible, because it requires determining when a
                    group, as given by generators and relations, is
                    trivial. So this conceivably may give a false
                    negative in some cases.

                EXAMPLES::

                    sage: # needs sage.graphs sage.groups
                    sage: T = simplicial_sets.Torus()
                    sage: T.is_simply_connected()
                    False
                    sage: T.suspension().is_simply_connected()
                    True
                    sage: simplicial_sets.KleinBottle().is_simply_connected()
                    False

                    sage: # needs sage.graphs
                    sage: S2 = simplicial_sets.Sphere(2)
                    sage: S3 = simplicial_sets.Sphere(3)
                    sage: (S2.wedge(S3)).is_simply_connected()                          # needs sage.groups
                    True
                    sage: X = S2.disjoint_union(S3)
                    sage: X = X.set_base_point(X.n_cells(0)[0])
                    sage: X.is_simply_connected()
                    False

                    sage: C3 = groups.misc.MultiplicativeAbelian([3])                   # needs sage.graphs sage.groups
                    sage: BC3 = simplicial_sets.ClassifyingSpace(C3)                    # needs sage.graphs sage.groups
                    sage: BC3.is_simply_connected()                                     # needs sage.graphs sage.groups
                    False
                """
            def connectivity(self, max_dim=None):
                """
                Return the connectivity of this pointed simplicial set.

                INPUT:

                - ``max_dim`` -- specify a maximum dimension through
                  which to check. This is required if this simplicial
                  set is simply connected and not finite.

                The dimension of the first nonzero homotopy group. If
                simply connected, this is the same as the dimension of
                the first nonzero homology group.

                .. WARNING::

                   See the warning for the :meth:`is_simply_connected` method.

                The connectivity of a contractible space is ``+Infinity``.

                EXAMPLES::

                    sage: # needs sage.graphs sage.groups
                    sage: simplicial_sets.Sphere(3).connectivity()
                    2
                    sage: simplicial_sets.Sphere(0).connectivity()
                    -1
                    sage: K = simplicial_sets.Simplex(4)
                    sage: K = K.set_base_point(K.n_cells(0)[0])
                    sage: K.connectivity()
                    +Infinity
                    sage: X = simplicial_sets.Torus().suspension(2)
                    sage: X.connectivity()
                    2

                    sage: C2 = groups.misc.MultiplicativeAbelian([2])                   # needs sage.graphs sage.groups
                    sage: BC2 = simplicial_sets.ClassifyingSpace(C2)                    # needs sage.graphs sage.groups
                    sage: BC2.connectivity()                                            # needs sage.graphs sage.groups
                    0
                """
        class Finite(CategoryWithAxiom):
            class ParentMethods:
                def unset_base_point(self):
                    """
                    Return a copy of this simplicial set in which the base point has
                    been forgotten.

                    EXAMPLES::

                        sage: # needs sage.graphs
                        sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
                        sage: v = AbstractSimplex(0, name='v_0')
                        sage: w = AbstractSimplex(0, name='w_0')
                        sage: e = AbstractSimplex(1)
                        sage: Y = SimplicialSet({e: (v, w)}, base_point=w)
                        sage: Y.is_pointed()
                        True
                        sage: Y.base_point()
                        w_0
                        sage: Z = Y.unset_base_point()
                        sage: Z.is_pointed()
                        False
                    """
                def fat_wedge(self, n):
                    """
                    Return the `n`-th fat wedge of this pointed simplicial set.

                    This is the subcomplex of the `n`-fold product `X^n`
                    consisting of those points in which at least one
                    factor is the base point. Thus when `n=2`, this is the
                    wedge of the simplicial set with itself, but when `n`
                    is larger, the fat wedge is larger than the `n`-fold
                    wedge.

                    EXAMPLES::

                        sage: # needs sage.graphs
                        sage: S1 = simplicial_sets.Sphere(1)
                        sage: S1.fat_wedge(0)
                        Point
                        sage: S1.fat_wedge(1)
                        S^1
                        sage: S1.fat_wedge(2).fundamental_group()                       # needs sage.groups
                        Finitely presented group < e0, e1 |  >
                        sage: S1.fat_wedge(4).homology()                                # needs sage.modules
                        {0: 0, 1: Z x Z x Z x Z, 2: Z^6, 3: Z x Z x Z x Z}
                    """
                def smash_product(self, *others):
                    """
                    Return the smash product of this simplicial set with ``others``.

                    INPUT:

                    - ``others`` -- one or several simplicial sets

                    EXAMPLES::

                        sage: # needs sage.graphs sage.groups
                        sage: S1 = simplicial_sets.Sphere(1)
                        sage: RP2 = simplicial_sets.RealProjectiveSpace(2)
                        sage: X = S1.smash_product(RP2)
                        sage: X.homology(base_ring=GF(2))                               # needs sage.modules
                        {0: Vector space of dimension 0 over Finite Field of size 2,
                         1: Vector space of dimension 0 over Finite Field of size 2,
                         2: Vector space of dimension 1 over Finite Field of size 2,
                         3: Vector space of dimension 1 over Finite Field of size 2}

                        sage: T = S1.product(S1)                                        # needs sage.graphs sage.groups
                        sage: X = T.smash_product(S1)                                   # needs sage.graphs sage.groups
                        sage: X.homology(reduced=False)                                 # needs sage.graphs sage.groups sage.modules
                        {0: Z, 1: 0, 2: Z x Z, 3: Z}
                    """
