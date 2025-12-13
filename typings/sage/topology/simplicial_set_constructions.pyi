from .simplicial_set import AbstractSimplex as AbstractSimplex, SimplicialSet_arbitrary as SimplicialSet_arbitrary, SimplicialSet_finite as SimplicialSet_finite, face_degeneracies as face_degeneracies, standardize_degeneracies as standardize_degeneracies
from .simplicial_set_examples import Empty as Empty, Point as Point
from _typeshed import Incomplete
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.sets.set import Set as Set
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SubSimplicialSet(SimplicialSet_finite, UniqueRepresentation):
    @staticmethod
    def __classcall__(self, data, ambient=None):
        """
        Convert ``data`` from a dict to a tuple.

        TESTS::

            sage: from sage.topology.simplicial_set_constructions import SubSimplicialSet
            sage: K = simplicial_sets.Simplex(2)
            sage: e = K.n_cells(1)[0]
            sage: A = SubSimplicialSet({e: K.faces(e)}, ambient=K)
            sage: B = SubSimplicialSet({e: list(K.faces(e))}, ambient=K)
            sage: A == B
            True
        """
    def __init__(self, data, ambient=None) -> None:
        """
        Return a finite simplicial set as a subsimplicial set of another
        simplicial set.

        This keeps track of the ambient simplicial set and the
        inclusion map from the subcomplex into it.

        INPUT:

        - ``data`` -- the data defining the subset: a dictionary where
          the keys are simplices from the ambient simplicial set and
          the values are their faces.

        - ``ambient`` -- the ambient simplicial set. If omitted, use
          the same simplicial set as the subset and the ambient
          complex.

        EXAMPLES::

            sage: S3 = simplicial_sets.Sphere(3)
            sage: K = simplicial_sets.KleinBottle()
            sage: X = S3.disjoint_union(K)
            sage: Y = X.structure_map(0).image()  # the S3 summand
            sage: Y.inclusion_map()
            Simplicial set morphism:
              From: Simplicial set with 2 non-degenerate simplices
              To:   Disjoint union: (S^3 u Klein bottle)
              Defn: [v_0, sigma_3] --> [v_0, sigma_3]
            sage: Y.ambient_space()
            Disjoint union: (S^3 u Klein bottle)

        TESTS::

            sage: T = simplicial_sets.Torus()
            sage: latex(T.n_skeleton(2))
            S^{1} \\times S^{1}

            sage: T.n_skeleton(1).n_skeleton(1) == T.n_skeleton(1)
            True

            sage: T.n_skeleton(1) is T.n_skeleton(1)
            True
        """
    def inclusion_map(self):
        """
        Return the inclusion map from this subsimplicial set into its
        ambient space.

        EXAMPLES::

            sage: RP6 = simplicial_sets.RealProjectiveSpace(6)                          # needs sage.groups
            sage: K = RP6.n_skeleton(2)                                                 # needs sage.groups
            sage: K.inclusion_map()                                                     # needs sage.groups
            Simplicial set morphism:
              From: Simplicial set with 3 non-degenerate simplices
              To:   RP^6
              Defn: [1, f, f * f] --> [1, f, f * f]

        `RP^6` itself is constructed as a subsimplicial set of
        `RP^\\infty`::

            sage: latex(RP6.inclusion_map())                                            # needs sage.groups
            RP^{6} \\to RP^{\\infty}
        """
    def ambient_space(self):
        """
        Return the simplicial set of which this is a subsimplicial set.

        EXAMPLES::

            sage: T = simplicial_sets.Torus()
            sage: eight = T.wedge_as_subset()
            sage: eight
            Simplicial set with 3 non-degenerate simplices
            sage: eight.fundamental_group()                                             # needs sage.groups
            Finitely presented group < e0, e1 |  >
            sage: eight.ambient_space()
            Torus
        """

class PullbackOfSimplicialSets(SimplicialSet_arbitrary, UniqueRepresentation):
    @staticmethod
    def __classcall_private__(self, maps=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import PullbackOfSimplicialSets
            sage: S2 = simplicial_sets.Sphere(2)
            sage: one = S2.Hom(S2).identity()
            sage: PullbackOfSimplicialSets([one, one]) == PullbackOfSimplicialSets((one, one))
            True
        """
    def __init__(self, maps=None) -> None:
        """
        Return the pullback obtained from the morphisms ``maps``.

        INPUT:

        - ``maps`` -- list or tuple of morphisms of simplicial sets

        If only a single map `f: X \\to Y` is given, then return
        `X`. If no maps are given, return the one-point simplicial
        set. Otherwise, given a simplicial set `Y` and maps `f_i: X_i
        \\to Y` for `0 \\leq i \\leq m`, construct the pullback `P`: see
        :wikipedia:`Pullback_(category_theory)`. This is constructed
        as pullbacks of sets for each set of `n`-simplices, so `P_n`
        is the subset of the product `\\prod (X_i)_n` consisting of
        those elements `(x_i)` for which `f_i(x_i) = f_j(x_j)` for all
        `i`, `j`.

        This is pointed if the maps `f_i` are.

        EXAMPLES:

        The pullback of a quotient map by a subsimplicial set and the
        base point map gives a simplicial set isomorphic to the
        original subcomplex::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: K = RP5.quotient(RP5.n_skeleton(2))
            sage: X = K.pullback(K.quotient_map(), K.base_point_map())
            sage: X.homology() == RP5.n_skeleton(2).homology()                          # needs sage.modules
            True

        Pullbacks of identity maps::

            sage: S2 = simplicial_sets.Sphere(2)
            sage: one = S2.Hom(S2).identity()
            sage: P = S2.pullback(one, one)
            sage: P.homology()                                                          # needs sage.modules
            {0: 0, 1: 0, 2: Z}

        The pullback is constructed in terms of the product -- of
        course, the product is a special case of the pullback -- and
        the simplices are named appropriately::

            sage: P.nondegenerate_simplices()
            [(v_0, v_0), (sigma_2, sigma_2)]
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        The `n`-skeleton of the pullback is computed as the pullback
        of the `n`-skeleta of the component simplicial sets.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: one = Hom(B,B).identity()
            sage: c = Hom(B,B).constant_map()
            sage: P = B.pullback(one, c)
            sage: P.n_skeleton(2)
            Pullback of maps:
              Simplicial set endomorphism of Simplicial set with 3 non-degenerate simplices
                Defn: Identity map
              Simplicial set endomorphism of Simplicial set with 3 non-degenerate simplices
                Defn: Constant map at 1
            sage: P.n_skeleton(3).homology()                                            # needs sage.modules
            {0: 0, 1: C2, 2: 0, 3: Z}
        """
    def defining_map(self, i):
        """
        Return the `i`-th map defining the pullback.

        INPUT:

        - ``i`` -- integer

        If this pullback was constructed as ``Y.pullback(f_0, f_1, ...)``,
        this returns `f_i`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: K = RP5.quotient(RP5.n_skeleton(2))
            sage: Y = K.pullback(K.quotient_map(), K.base_point_map())
            sage: Y.defining_map(1)
            Simplicial set morphism:
              From: Point
              To:   Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
              Defn: Constant map at *
            sage: Y.defining_map(0).domain()
            RP^5
        """

class PullbackOfSimplicialSets_finite(PullbackOfSimplicialSets, SimplicialSet_finite):
    """
    The pullback of finite simplicial sets obtained from ``maps``.

    When the simplicial sets involved are all finite, there are more
    methods available to the resulting pullback, as compared to case
    when some of the components are infinite: the structure maps from
    the pullback and the pullback's universal property: see
    :meth:`structure_map` and :meth:`universal_property`.
    """
    @staticmethod
    def __classcall_private__(self, maps=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import PullbackOfSimplicialSets_finite
            sage: S2 = simplicial_sets.Sphere(2)
            sage: one = S2.Hom(S2).identity()
            sage: PullbackOfSimplicialSets_finite([one, one]) == PullbackOfSimplicialSets_finite((one, one))
            True
        """
    def __init__(self, maps=None) -> None:
        """
        Return the pullback obtained from the morphisms ``maps``.

        See :class:`PullbackOfSimplicialSets` for more information.

        INPUT:

        - ``maps`` -- list or tuple of morphisms of simplicial sets

        EXAMPLES::

            sage: eta = simplicial_sets.HopfMap()
            sage: S3 = eta.domain()
            sage: S2 = eta.codomain()
            sage: c = Hom(S2,S2).constant_map()
            sage: S2.pullback(eta, c).is_finite()
            True

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: one = Hom(B,B).identity()
            sage: c = Hom(B,B).constant_map()
            sage: B.pullback(one, c).is_finite()
            False

        TESTS::

            sage: P = simplicial_sets.Point()
            sage: P.pullback(P.constant_map(), P.constant_map())
            Pullback of maps:
              Simplicial set endomorphism of Point
                Defn: Identity map
              Simplicial set endomorphism of Point
                Defn: Identity map
        """
    def structure_map(self, i):
        """
        Return the `i`-th projection map of the pullback.

        INPUT:

        - ``i`` -- integer

        If this pullback `P` was constructed as ``Y.pullback(f_0, f_1,
        ...)``, where `f_i: X_i \\to Y`, then there are structure maps
        `\\bar{f}_i: P \\to X_i`. This method constructs `\\bar{f}_i`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: K = RP5.quotient(RP5.n_skeleton(2))
            sage: Y = K.pullback(K.quotient_map(), K.base_point_map())
            sage: Y.structure_map(0)
            Simplicial set morphism:
              From: Pullback of maps:
              Simplicial set morphism:
                From: RP^5
                To:   Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
                Defn: [1, f, f * f, f * f * f, f * f * f * f, f * f * f * f * f]
                      --> [*, s_0 *, s_1 s_0 *, f * f * f, f * f * f * f, f * f * f * f * f]
              Simplicial set morphism:
                From: Point
                To:   Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
                Defn: Constant map at *
              To:   RP^5
              Defn: [(1, *), (f, s_0 *), (f * f, s_1 s_0 *)] --> [1, f, f * f]
            sage: Y.structure_map(1).codomain()
            Point

        These maps are also accessible via :meth:`projection_map`::

            sage: Y.projection_map(1).codomain()                                        # needs sage.groups
            Point
        """
    projection_map = structure_map
    def universal_property(self, *maps):
        '''
        Return the map induced by ``maps``.

        INPUT:

        - ``maps`` -- maps from a simplicial set `Z` to the "factors"
          `X_i` forming the pullback

        If the pullback `P` is formed by maps `f_i: X_i \\to Y`, then
        given maps `g_i: Z \\to X_i` such that `f_i g_i = f_j g_j` for
        all `i`, `j`, then there is a unique map `g: Z \\to P` making
        the appropriate diagram commute. This constructs that map.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: T = S1.product(S1)
            sage: K = T.factor(0, as_subset=True)
            sage: f = S1.Hom(T)({S1.n_cells(0)[0]: K.n_cells(0)[0],
            ....:                S1.n_cells(1)[0]: K.n_cells(1)[0]})
            sage: P = S1.product(T)
            sage: P.universal_property(S1.Hom(S1).identity(), f)
            Simplicial set morphism:
              From: S^1
              To:   S^1 x S^1 x S^1
              Defn: [v_0, sigma_1] --> [(v_0, (v_0, v_0)), (sigma_1, (sigma_1, s_0 v_0))]
        '''

class Factors:
    """
    Classes which inherit from this should define a ``_factors``
    attribute for their instances, and this class accesses that
    attribute. This is used by :class:`ProductOfSimplicialSets`,
    :class:`WedgeOfSimplicialSets`, and
    :class:`DisjointUnionOfSimplicialSets`.
    """
    def factors(self):
        """
        Return the factors involved in this construction of simplicial sets.

        EXAMPLES::

            sage: S2 = simplicial_sets.Sphere(2)
            sage: S3 = simplicial_sets.Sphere(3)
            sage: S2.wedge(S3).factors() == (S2, S3)
            True
            sage: S2.product(S3).factors()[0]
            S^2
        """
    def factor(self, i):
        """
        Return the `i`-th factor of this construction of simplicial sets.

        INPUT:

        - ``i`` -- integer; the index of the factor

        EXAMPLES::

            sage: S2 = simplicial_sets.Sphere(2)
            sage: S3 = simplicial_sets.Sphere(3)
            sage: K = S2.disjoint_union(S3)
            sage: K.factor(0)
            S^2

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: X = B.wedge(S3, B)
            sage: X.factor(1)
            S^3
            sage: X.factor(2)
            Classifying space of Multiplicative Abelian group isomorphic to C2
        """

class ProductOfSimplicialSets(PullbackOfSimplicialSets, Factors):
    @staticmethod
    def __classcall__(cls, factors=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import ProductOfSimplicialSets
            sage: S2 = simplicial_sets.Sphere(2)
            sage: ProductOfSimplicialSets([S2, S2]) == ProductOfSimplicialSets((S2, S2))
            True
        """
    def __init__(self, factors=None) -> None:
        """
        Return the product of simplicial sets.

        INPUT:

        - ``factors`` -- list or tuple of simplicial sets

        Return the product of the simplicial sets in ``factors``.

        If `X` and `Y` are simplicial sets, then their product `X
        \\times Y` is defined to be the simplicial set with
        `n`-simplices `X_n \\times Y_n`.  Therefore the simplices in
        the product have the form `(s_I \\sigma, s_J \\tau)`, where `s_I
        = s_{i_1} ... s_{i_p}` and `s_J = s_{j_1} ... s_{j_q}` are
        composites of degeneracy maps, written in decreasing order.
        Such a simplex is nondegenerate if the indices `I` and `J` are
        disjoint. Therefore if `\\sigma` and `\\tau` are nondegenerate
        simplices of dimensions `m` and `n`, in the product they will
        lead to nondegenerate simplices up to dimension `m+n`, and no
        further.

        This extends in the more or less obvious way to products with
        more than two factors: with three factors, a simplex `(s_I
        \\sigma, s_J \\tau, s_K \\rho)` is nondegenerate if `I \\cap J
        \\cap K` is empty, etc.

        If a simplicial set is constructed as a product, the factors
        are recorded and are accessible via the method
        :meth:`Factors.factors`. If it is constructed as a product and then
        copied, this information is lost.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: w = AbstractSimplex(0, name='w')
            sage: e = AbstractSimplex(1, name='e')
            sage: X = SimplicialSet({e: (v, w)})
            sage: square = X.product(X)

        ``square`` is now the standard triangulation of the square: 4
        vertices, 5 edges (the four on the border plus the diagonal),
        2 triangles::

            sage: square.f_vector()
            [4, 5, 2]

            sage: S1 = simplicial_sets.Sphere(1)
            sage: T = S1.product(S1)
            sage: T.homology(reduced=False)                                             # needs sage.modules
            {0: Z, 1: Z x Z, 2: Z}

        Since ``S1`` is pointed, so is ``T``::

            sage: S1.is_pointed()
            True
            sage: S1.base_point()
            v_0
            sage: T.is_pointed()
            True
            sage: T.base_point()
            (v_0, v_0)

            sage: S2 = simplicial_sets.Sphere(2)
            sage: S3 = simplicial_sets.Sphere(3)
            sage: Z = S2.product(S3)
            sage: Z.homology()                                                          # needs sage.modules
            {0: 0, 1: 0, 2: Z, 3: Z, 4: 0, 5: Z}

        Products involving infinite simplicial sets::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: B.rename('RP^oo')
            sage: X = B.product(B); X
            RP^oo x RP^oo
            sage: X.n_cells(1)
            [(f, f), (f, s_0 1), (s_0 1, f)]
            sage: X.homology(range(3), base_ring=GF(2))                                 # needs sage.modules
            {0: Vector space of dimension 0 over Finite Field of size 2,
             1: Vector space of dimension 2 over Finite Field of size 2,
             2: Vector space of dimension 3 over Finite Field of size 2}
            sage: Y = B.product(S2)
            sage: Y.homology(range(5), base_ring=GF(2))                                 # needs sage.modules
            {0: Vector space of dimension 0 over Finite Field of size 2,
             1: Vector space of dimension 1 over Finite Field of size 2,
             2: Vector space of dimension 2 over Finite Field of size 2,
             3: Vector space of dimension 2 over Finite Field of size 2,
             4: Vector space of dimension 2 over Finite Field of size 2}
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        In the finite case, this returns the ordinary `n`-skeleton. In
        the infinite case, it computes the `n`-skeleton of the product
        of the `n`-skeleta of the factors.

        EXAMPLES::

            sage: S2 = simplicial_sets.Sphere(2)
            sage: S3 = simplicial_sets.Sphere(3)
            sage: S2.product(S3).n_skeleton(2)
            Simplicial set with 2 non-degenerate simplices

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: X = B.product(B)
            sage: X.n_skeleton(2)
            Simplicial set with 13 non-degenerate simplices
        """
    def factor(self, i, as_subset: bool = False):
        """
        Return the `i`-th factor of the product.

        INPUT:

        - ``i`` -- integer; the index of the factor

        - ``as_subset`` -- boolean (default: ``False``)

        If ``as_subset`` is ``True``, return the `i`-th factor as a
        subsimplicial set of the product, identifying it with its
        product with the base point in each other factor. As a
        subsimplicial set, it comes equipped with an inclusion
        map. This option will raise an error if any factor does not
        have a base point.

        If ``as_subset`` is ``False``, return the `i`-th factor in
        its original form as a simplicial set.

        EXAMPLES::

            sage: S2 = simplicial_sets.Sphere(2)
            sage: S3 = simplicial_sets.Sphere(3)
            sage: K = S2.product(S3)
            sage: K.factor(0)
            S^2

            sage: K.factor(0, as_subset=True)
            Simplicial set with 2 non-degenerate simplices
            sage: K.factor(0, as_subset=True).homology()                                # needs sage.modules
            {0: 0, 1: 0, 2: Z}

            sage: K.factor(0) is S2
            True
            sage: K.factor(0, as_subset=True) is S2
            False
        """

class ProductOfSimplicialSets_finite(ProductOfSimplicialSets, PullbackOfSimplicialSets_finite):
    """
    The product of finite simplicial sets.

    When the factors are all finite, there are more methods available
    for the resulting product, as compared to products with infinite
    factors: projection maps, the wedge as a subcomplex, and the fat
    wedge as a subcomplex. See :meth:`projection_map`,
    :meth:`wedge_as_subset`, and :meth:`fat_wedge_as_subset`
    """
    def __init__(self, factors=None) -> None:
        """
        Return the product of finite simplicial sets.

        See :class:`ProductOfSimplicialSets` for more information.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: e = AbstractSimplex(1)
            sage: X = SimplicialSet({e: (v, v)})
            sage: W = X.product(X, X)
            sage: W.homology()                                                          # needs sage.groups
            {0: 0, 1: Z x Z x Z, 2: Z x Z x Z, 3: Z}
            sage: W.is_pointed()
            False

            sage: X = X.set_base_point(v)
            sage: w = AbstractSimplex(0, name='w')
            sage: f = AbstractSimplex(1)
            sage: Y = SimplicialSet({f: (v,w)}, base_point=w)
            sage: Z = Y.product(X)
            sage: Z.is_pointed()
            True
            sage: Z.base_point()
            (w, v)
        """
    def projection_map(self, i):
        """
        Return the map projecting onto the `i`-th factor.

        INPUT:

        - ``i`` -- integer; the index of the projection map

        EXAMPLES::

            sage: T = simplicial_sets.Torus()
            sage: f_0 = T.projection_map(0)
            sage: f_1 = T.projection_map(1)

            sage: # needs sage.modules
            sage: m_0 = f_0.induced_homology_morphism().to_matrix(1)  # matrix in dim 1
            sage: m_1 = f_1.induced_homology_morphism().to_matrix(1)
            sage: m_0.rank()
            1
            sage: m_0 == m_1
            False
        """
    def wedge_as_subset(self):
        """
        Return the wedge as a subsimplicial set of this product of pointed
        simplicial sets.

        This will raise an error if any factor is not pointed.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: e = AbstractSimplex(1, name='e')
            sage: w = AbstractSimplex(0, name='w')
            sage: f = AbstractSimplex(1, name='f')
            sage: X = SimplicialSet({e: (v, v)}, base_point=v)
            sage: Y = SimplicialSet({f: (w, w)}, base_point=w)
            sage: P = X.product(Y)
            sage: W = P.wedge_as_subset()
            sage: W.nondegenerate_simplices()
            [(v, w), (e, s_0 w), (s_0 v, f)]
            sage: W.homology()                                                          # needs sage.modules
            {0: 0, 1: Z x Z}
        """
    def fat_wedge_as_subset(self):
        """
        Return the fat wedge as a subsimplicial set of this product of
        pointed simplicial sets.

        The fat wedge consists of those terms where at least one
        factor is the base point. Thus with two factors this is the
        ordinary wedge, but with more factors, it is larger.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: X = S1.product(S1, S1)
            sage: W = X.fat_wedge_as_subset()
            sage: W.homology()                                                          # needs sage.modules
            {0: 0, 1: Z x Z x Z, 2: Z x Z x Z}
        """

class PushoutOfSimplicialSets(SimplicialSet_arbitrary, UniqueRepresentation):
    @staticmethod
    def __classcall_private__(cls, maps=None, vertex_name=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import PushoutOfSimplicialSets
            sage: S2 = simplicial_sets.Sphere(2)
            sage: one = S2.Hom(S2).identity()
            sage: PushoutOfSimplicialSets([one, one]) == PushoutOfSimplicialSets((one, one))
            True
        """
    def __init__(self, maps=None, vertex_name=None) -> None:
        """
        Return the pushout obtained from the morphisms ``maps``.

        INPUT:

        - ``maps`` -- list or tuple of morphisms of simplicial sets
        - ``vertex_name`` -- (default: ``None``)

        If only a single map `f: X \\to Y` is given, then return
        `Y`. If no maps are given, return the empty simplicial
        set. Otherwise, given a simplicial set `X` and maps `f_i: X
        \\to Y_i` for `0 \\leq i \\leq m`, construct the pushout `P`: see
        :wikipedia:`Pushout_(category_theory)`. This is constructed as
        pushouts of sets for each set of `n`-simplices, so `P_n` is
        the disjoint union of the sets `(Y_i)_n`, with elements
        `f_i(x)` identified for `n`-simplex `x` in `X`.

        Simplices in the pushout are given names as follows: if a
        simplex comes from a single `Y_i`, it inherits its
        name. Otherwise it must come from a simplex (or several) in
        `X`, and then it inherits one of those names, and it should be
        the first alphabetically. For example, if vertices `v`, `w`,
        and `z` in `X` are glued together, then the resulting vertex
        in the pushout will be called `v`.

        Base points are taken care of automatically: if each of the
        maps `f_i` is pointed, so is the pushout. If `X` is a point or
        if `X` is nonempty and any of the spaces `Y_i` is a point, use
        those for the base point. In all of these cases, if
        ``vertex_name`` is ``None``, generate the name of the base
        point automatically; otherwise, use ``vertex_name`` for its
        name.

        In all other cases, the pushout is not pointed.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: a = AbstractSimplex(0, name='a')
            sage: b = AbstractSimplex(0, name='b')
            sage: c = AbstractSimplex(0, name='c')
            sage: e0 = AbstractSimplex(1, name='e_0')
            sage: e1 = AbstractSimplex(1, name='e_1')
            sage: e2 = AbstractSimplex(1, name='e_2')
            sage: X = SimplicialSet({e2: (b, a)})
            sage: Y0 = SimplicialSet({e2: (b,a), e0: (c,b), e1: (c,a)})
            sage: Y1 = simplicial_sets.Simplex(0)
            sage: f0_data = {a:a, b:b, e2: e2}
            sage: v = Y1.n_cells(0)[0]
            sage: f1_data = {a:v, b:v, e2:v.apply_degeneracies(0)}
            sage: f0 = X.Hom(Y0)(f0_data)
            sage: f1 = X.Hom(Y1)(f1_data)
            sage: P = X.pushout(f0, f1)
            sage: P.nondegenerate_simplices()
            [a, c, e_0, e_1]

        There are defining maps `f_i: X \\to Y_i` and structure maps
        `\\bar{f}_i: Y_i \\to P`; the latter are only implemented in
        Sage when each `Y_i` is finite. ::

            sage: P.defining_map(0) == f0
            True
            sage: P.structure_map(1)
            Simplicial set morphism:
              From: 0-simplex
              To:   Pushout of maps:
              Simplicial set morphism:
                From: Simplicial set with 3 non-degenerate simplices
                To:   Simplicial set with 6 non-degenerate simplices
                Defn: [a, b, e_2] --> [a, b, e_2]
              Simplicial set morphism:
                From: Simplicial set with 3 non-degenerate simplices
                To:   0-simplex
                Defn: Constant map at (0,)
              Defn: Constant map at a
            sage: P.structure_map(0).domain() == Y0
            True
            sage: P.structure_map(0).codomain() == P
            True

        An inefficient way of constructing a suspension for an
        unpointed set: take the pushout of two copies of the inclusion
        map `X \\to CX`::

            sage: T = simplicial_sets.Torus()
            sage: T = T.unset_base_point()
            sage: CT = T.cone()
            sage: inc = CT.base_as_subset().inclusion_map()
            sage: P = T.pushout(inc, inc)
            sage: P.homology()                                                          # needs sage.modules
            {0: 0, 1: 0, 2: Z x Z, 3: Z}
            sage: len(P.nondegenerate_simplices())
            20

        It is more efficient to construct the suspension as the
        quotient `CX/X`::

            sage: len(CT.quotient(CT.base_as_subset()).nondegenerate_simplices())
            8

        It is more efficient still if the original simplicial set has
        a base point::

            sage: T = simplicial_sets.Torus()
            sage: len(T.suspension().nondegenerate_simplices())
            6

            sage: S1 = simplicial_sets.Sphere(1)
            sage: pt = simplicial_sets.Point()
            sage: bouquet = pt.pushout(S1.base_point_map(),
            ....:                      S1.base_point_map(),
            ....:                      S1.base_point_map())
            sage: bouquet.homology(1)                                                   # needs sage.modules
            Z x Z x Z
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        The `n`-skeleton of the pushout is computed as the pushout
        of the `n`-skeleta of the component simplicial sets.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: K = B.n_skeleton(3)
            sage: Q = K.pushout(K.inclusion_map(), K.constant_map())
            sage: Q.n_skeleton(5).homology()                                            # needs sage.modules
            {0: 0, 1: 0, 2: 0, 3: 0, 4: Z, 5: Z}

        Of course, computing the `n`-skeleton and then taking homology
        need not yield the same answer as asking for homology through
        dimension `n`, since the latter computation will use the
        `(n+1)`-skeleton::

            sage: Q.homology(range(6))                                                  # needs sage.groups sage.modules
            {0: 0, 1: 0, 2: 0, 3: 0, 4: Z, 5: C2}
        """
    def defining_map(self, i):
        """
        Return the `i`-th map defining the pushout.

        INPUT:

        - ``i`` -- integer

        If this pushout was constructed as ``X.pushout(f_0, f_1, ...)``,
        this returns `f_i`.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: T = simplicial_sets.Torus()
            sage: X = S1.wedge(T)  # a pushout
            sage: X.defining_map(0)
            Simplicial set morphism:
              From: Point
              To:   S^1
              Defn: Constant map at v_0
            sage: X.defining_map(1).domain()
            Point
            sage: X.defining_map(1).codomain()
            Torus
        """

class PushoutOfSimplicialSets_finite(PushoutOfSimplicialSets, SimplicialSet_finite):
    """
    The pushout of finite simplicial sets obtained from ``maps``.

    When the simplicial sets involved are all finite, there are more
    methods available to the resulting pushout, as compared to case
    when some of the components are infinite: the structure maps to the
    pushout and the pushout's universal property: see
    :meth:`structure_map` and :meth:`universal_property`.
    """
    @staticmethod
    def __classcall_private__(cls, maps=None, vertex_name=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import PushoutOfSimplicialSets_finite
            sage: S2 = simplicial_sets.Sphere(2)
            sage: one = S2.Hom(S2).identity()
            sage: PushoutOfSimplicialSets_finite([one, one]) == PushoutOfSimplicialSets_finite((one, one))
            True
        """
    def __init__(self, maps=None, vertex_name=None) -> None:
        """
        Return the pushout obtained from the morphisms ``maps``.

        See :class:`PushoutOfSimplicialSets` for more information.

        INPUT:

        - ``maps`` -- list or tuple of morphisms of simplicial sets
        - ``vertex_name`` -- (default: ``None``)

        EXAMPLES::

            sage: from sage.topology.simplicial_set_constructions import PushoutOfSimplicialSets_finite
            sage: T = simplicial_sets.Torus()
            sage: S2 = simplicial_sets.Sphere(2)
            sage: PushoutOfSimplicialSets_finite([T.base_point_map(), S2.base_point_map()]).n_cells(0)[0]
            *
            sage: PushoutOfSimplicialSets_finite([T.base_point_map(), S2.base_point_map()], vertex_name='v').n_cells(0)[0]
            v
        """
    def structure_map(self, i):
        """
        Return the `i`-th structure map of the pushout.

        INPUT:

        - ``i`` -- integer

        If this pushout `Z` was constructed as ``X.pushout(f_0, f_1, ...)``,
        where `f_i: X \\to Y_i`, then there are structure maps
        `\\bar{f}_i: Y_i \\to Z`. This method constructs `\\bar{f}_i`.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: T = simplicial_sets.Torus()
            sage: X = S1.disjoint_union(T)  # a pushout
            sage: X.structure_map(0)
            Simplicial set morphism:
              From: S^1
              To:   Disjoint union: (S^1 u Torus)
              Defn: [v_0, sigma_1] --> [v_0, sigma_1]
            sage: X.structure_map(1).domain()
            Torus
            sage: X.structure_map(1).codomain()
            Disjoint union: (S^1 u Torus)
        """
    def universal_property(self, *maps):
        '''
        Return the map induced by ``maps``.

        INPUT:

        - ``maps`` -- maps "factors" `Y_i` forming the pushout to a
          fixed simplicial set `Z`

        If the pushout `P` is formed by maps `f_i: X \\to Y_i`, then
        given maps `g_i: Y_i \\to Z` such that `g_i f_i = g_j f_j` for
        all `i`, `j`, then there is a unique map `g: P \\to Z` making
        the appropriate diagram commute. This constructs that map.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name=\'v\')
            sage: w = AbstractSimplex(0, name=\'w\')
            sage: x = AbstractSimplex(0, name=\'x\')
            sage: evw = AbstractSimplex(1, name=\'vw\')
            sage: evx = AbstractSimplex(1, name=\'vx\')
            sage: ewx = AbstractSimplex(1, name=\'wx\')
            sage: X = SimplicialSet({evw: (w, v), evx: (x, v)})
            sage: Y_0 = SimplicialSet({evw: (w, v), evx: (x, v), ewx: (x, w)})
            sage: Y_1 = SimplicialSet({evx: (x, v)})

            sage: f_0 = Hom(X, Y_0)({v:v, w:w, x:x, evw:evw, evx:evx})
            sage: f_1 = Hom(X, Y_1)({v:v, w:v, x:x,
            ....:                    evw:v.apply_degeneracies(0), evx:evx})
            sage: P = X.pushout(f_0, f_1)

            sage: one = Hom(Y_1, Y_1).identity()
            sage: g = Hom(Y_0, Y_1)({v:v, w:v, x:x,
            ....:                    evw:v.apply_degeneracies(0), evx:evx, ewx:evx})
            sage: P.universal_property(g, one)
            Simplicial set morphism:
              From: Pushout of maps:
              Simplicial set morphism:
                From: Simplicial set with 5 non-degenerate simplices
                To:   Simplicial set with 6 non-degenerate simplices
                Defn: [v, w, x, vw, vx] --> [v, w, x, vw, vx]
              Simplicial set morphism:
                From: Simplicial set with 5 non-degenerate simplices
                To:   Simplicial set with 3 non-degenerate simplices
                Defn: [v, w, x, vw, vx] --> [v, v, x, s_0 v, vx]
              To:   Simplicial set with 3 non-degenerate simplices
              Defn: [v, x, vx, wx] --> [v, x, vx, vx]
        '''

class QuotientOfSimplicialSet(PushoutOfSimplicialSets):
    def __init__(self, inclusion, vertex_name: str = '*') -> None:
        """
        Return the quotient of a simplicial set by a subsimplicial set.

        INPUT:

        - ``inclusion`` -- inclusion map of a subcomplex (=
          subsimplicial set) of a simplicial set
        - ``vertex_name`` -- string (default: ``'*'``)

        A subcomplex `A` comes equipped with the inclusion map `A \\to
        X` to its ambient complex `X`, and this constructs the
        quotient `X/A`, collapsing `A` to a point. The resulting point
        is called ``vertex_name``, which is ``'*'`` by default.

        When the simplicial sets involved are finite, there is a
        :meth:`QuotientOfSimplicialSet_finite.quotient_map` method available.

        EXAMPLES::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: RP2 = RP5.n_skeleton(2)
            sage: RP5_2 = RP5.quotient(RP2); RP5_2
            Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
            sage: RP5_2.quotient_map()
            Simplicial set morphism:
              From: RP^5
              To:   Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
              Defn: [1, f, f * f, f * f * f, f * f * f * f, f * f * f * f * f]
                    --> [*, s_0 *, s_1 s_0 *, f * f * f, f * f * f * f, f * f * f * f * f]
        """
    def ambient(self):
        """
        Return the ambient space.

        That is, if this quotient is `K/L`, return `K`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: RP2 = RP5.n_skeleton(2)
            sage: RP5_2 = RP5.quotient(RP2)
            sage: RP5_2.ambient()
            RP^5

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: K = B.n_skeleton(3)
            sage: Q = B.quotient(K)
            sage: Q.ambient()
            Classifying space of Multiplicative Abelian group isomorphic to C2
        """
    def subcomplex(self):
        """
        Return the subcomplex space associated to this quotient.

        That is, if this quotient is `K/L`, return `L`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: RP2 = RP5.n_skeleton(2)
            sage: RP5_2 = RP5.quotient(RP2)
            sage: RP5_2.subcomplex()
            Simplicial set with 3 non-degenerate simplices

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: K = B.n_skeleton(3)
            sage: Q = B.quotient(K)
            sage: Q.subcomplex()
            Simplicial set with 4 non-degenerate simplices
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        The `n`-skeleton of the quotient is computed as the quotient
        of the `n`-skeleta.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: K = B.n_skeleton(3)
            sage: Q = B.quotient(K)
            sage: Q.n_skeleton(6)
            Quotient: (Simplicial set with 7
                       non-degenerate simplices/Simplicial set with 4
                                                non-degenerate simplices)
            sage: Q.n_skeleton(6).homology()                                            # needs sage.modules
            {0: 0, 1: 0, 2: 0, 3: 0, 4: Z, 5: C2, 6: 0}
        """

class QuotientOfSimplicialSet_finite(QuotientOfSimplicialSet, PushoutOfSimplicialSets_finite):
    """
    The quotient of finite simplicial sets.

    When the simplicial sets involved are finite, there is a
    :meth:`quotient_map` method available.
    """
    def __init__(self, inclusion, vertex_name: str = '*') -> None:
        """
        Return the quotient of a simplicial set by a subsimplicial set.

        See :class:`QuotientOfSimplicialSet` for more information.

        EXAMPLES::

            sage: # needs sage.groups
            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)
            sage: RP2 = RP5.n_skeleton(2)
            sage: RP5_2 = RP5.quotient(RP2); RP5_2
            Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
            sage: RP5_2.quotient_map()
            Simplicial set morphism:
              From: RP^5
              To:   Quotient: (RP^5/Simplicial set with 3 non-degenerate simplices)
              Defn: [1, f, f * f, f * f * f, f * f * f * f, f * f * f * f * f]
                    --> [*, s_0 *, s_1 s_0 *, f * f * f, f * f * f * f, f * f * f * f * f]
        """
    def quotient_map(self):
        """
        Return the quotient map from the original simplicial set to the
        quotient.

        EXAMPLES::

            sage: K = simplicial_sets.Simplex(1)
            sage: S1 = K.quotient(K.n_skeleton(0))
            sage: q = S1.quotient_map()
            sage: q
            Simplicial set morphism:
              From: 1-simplex
              To:   Quotient: (1-simplex/Simplicial set with 2 non-degenerate simplices)
              Defn: [(0,), (1,), (0, 1)] --> [*, *, (0, 1)]
            sage: q.domain() == K
            True
            sage: q.codomain() == S1
            True
        """

class SmashProductOfSimplicialSets_finite(QuotientOfSimplicialSet_finite, Factors):
    @staticmethod
    def __classcall__(cls, factors=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import SmashProductOfSimplicialSets_finite as Smash
            sage: S2 = simplicial_sets.Sphere(2)
            sage: Smash([S2, S2]) == Smash((S2, S2))
            True
        """
    def __init__(self, factors=None) -> None:
        """
        Return the smash product of finite pointed simplicial sets.

        INPUT:

        - ``factors`` -- list or tuple of simplicial sets

        Return the smash product of the simplicial sets in
        ``factors``: the smash product `X \\wedge Y` is defined to be
        the quotient `(X \\times Y) / (X \\vee Y)`, where `X \\vee Y` is
        the wedge sum.

        Each element of ``factors`` must be finite and pointed. (As of
        July 2016, constructing the wedge as a subcomplex of the
        product is only possible in Sage for finite simplicial sets.)

        EXAMPLES::

            sage: T = simplicial_sets.Torus()
            sage: S2 = simplicial_sets.Sphere(2)
            sage: T.smash_product(S2).homology() == T.suspension(2).homology()          # needs sage.modules
            True
        """

class WedgeOfSimplicialSets(PushoutOfSimplicialSets, Factors):
    @staticmethod
    def __classcall__(cls, factors=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import WedgeOfSimplicialSets
            sage: S2 = simplicial_sets.Sphere(2)
            sage: WedgeOfSimplicialSets([S2, S2]) == WedgeOfSimplicialSets((S2, S2))
            True
        """
    def __init__(self, factors=None) -> None:
        """
        Return the wedge sum of pointed simplicial sets.

        INPUT:

        - ``factors`` -- list or tuple of simplicial sets

        Return the wedge of the simplicial sets in ``factors``: the
        wedge sum `X \\vee Y` is formed by taking the disjoint
        union of `X` and `Y` and identifying their base points. In
        this construction, the new base point is renamed '*'.

        The wedge comes equipped with maps to and from each factor, or
        actually, maps from each factor, and maps to simplicial sets
        isomorphic to each factor. The codomains of the latter maps
        are quotients of the wedge, not identical to the original
        factors.

        EXAMPLES::

            sage: CP2 = simplicial_sets.ComplexProjectiveSpace(2)
            sage: K = simplicial_sets.KleinBottle()
            sage: W = CP2.wedge(K)
            sage: W.homology()                                                          # needs sage.modules
            {0: 0, 1: Z x C2, 2: Z, 3: 0, 4: Z}

            sage: W.inclusion_map(1)
            Simplicial set morphism:
              From: Klein bottle
              To:   Wedge: (CP^2 v Klein bottle)
              Defn: [Delta_{0,0}, Delta_{1,0}, Delta_{1,1}, Delta_{1,2}, Delta_{2,0}, Delta_{2,1}]
                    --> [*, Delta_{1,0}, Delta_{1,1}, Delta_{1,2}, Delta_{2,0}, Delta_{2,1}]

            sage: W.projection_map(0).domain()
            Wedge: (CP^2 v Klein bottle)
            sage: W.projection_map(0).codomain() # copy of CP^2
            Quotient: (Wedge: (CP^2 v Klein bottle)/Simplicial set with 6 non-degenerate simplices)
            sage: W.projection_map(0).codomain().homology()                             # needs sage.modules
            {0: 0, 1: 0, 2: Z, 3: 0, 4: Z}

        An error occurs if any of the factors is not pointed::

            sage: CP2.wedge(simplicial_sets.Simplex(1))
            Traceback (most recent call last):
            ...
            ValueError: the simplicial sets must be pointed
        """
    summands: Incomplete
    summand: Incomplete

class WedgeOfSimplicialSets_finite(WedgeOfSimplicialSets, PushoutOfSimplicialSets_finite):
    """
    The wedge sum of finite pointed simplicial sets.
    """
    def __init__(self, factors=None) -> None:
        """
        Return the wedge sum of finite pointed simplicial sets.

        INPUT:

        - ``factors`` -- tuple of simplicial sets

        If there are no factors, a point is returned.

        See :class:`WedgeOfSimplicialSets` for more information.

        EXAMPLES::

            sage: from sage.topology.simplicial_set_constructions import WedgeOfSimplicialSets_finite
            sage: K = simplicial_sets.Simplex(3)
            sage: WedgeOfSimplicialSets_finite((K,K))
            Traceback (most recent call last):
            ...
            ValueError: the simplicial sets must be pointed
        """
    def inclusion_map(self, i):
        """
        Return the inclusion map of the `i`-th factor.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: S2 = simplicial_sets.Sphere(2)
            sage: W = S1.wedge(S2, S1)
            sage: W.inclusion_map(1)
            Simplicial set morphism:
              From: S^2
              To:   Wedge: (S^1 v S^2 v S^1)
              Defn: [v_0, sigma_2] --> [*, sigma_2]
            sage: W.inclusion_map(0).domain()
            S^1
            sage: W.inclusion_map(2).domain()
            S^1
        """
    def projection_map(self, i):
        """
        Return the projection map onto the `i`-th factor.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: S2 = simplicial_sets.Sphere(2)
            sage: W = S1.wedge(S2, S1)
            sage: W.projection_map(1)
            Simplicial set morphism:
              From: Wedge: (S^1 v S^2 v S^1)
              To:   Quotient: (Wedge: (S^1 v S^2 v S^1)/Simplicial set with
                                                        3 non-degenerate simplices)
              Defn: [*, sigma_1, sigma_1, sigma_2] --> [*, s_0 *, s_0 *, sigma_2]
            sage: W.projection_map(1).image().homology(1)                               # needs sage.modules
            0
            sage: W.projection_map(1).image().homology(2)                               # needs sage.modules
            Z
        """

class DisjointUnionOfSimplicialSets(PushoutOfSimplicialSets, Factors):
    @staticmethod
    def __classcall__(cls, factors=None):
        """
        TESTS::

            sage: from sage.topology.simplicial_set_constructions import DisjointUnionOfSimplicialSets
            sage: from sage.topology.simplicial_set_examples import Empty
            sage: S2 = simplicial_sets.Sphere(2)
            sage: DisjointUnionOfSimplicialSets([S2, S2]) == DisjointUnionOfSimplicialSets((S2, S2))
            True
            sage: DisjointUnionOfSimplicialSets([S2, Empty(), S2, Empty()]) == DisjointUnionOfSimplicialSets((S2, S2))
            True
        """
    def __init__(self, factors=None) -> None:
        """
        Return the disjoint union of simplicial sets.

        INPUT:

        - ``factors`` -- list or tuple of simplicial sets

        Discard any factors which are empty and return the disjoint
        union of the remaining simplicial sets in ``factors``.  The
        disjoint union comes equipped with a map from each factor, as
        long as all of the factors are finite.

        EXAMPLES::

            sage: CP2 = simplicial_sets.ComplexProjectiveSpace(2)
            sage: K = simplicial_sets.KleinBottle()
            sage: W = CP2.disjoint_union(K)
            sage: W.homology()                                                          # needs sage.modules
            {0: Z, 1: Z x C2, 2: Z, 3: 0, 4: Z}

            sage: W.inclusion_map(1)
            Simplicial set morphism:
              From: Klein bottle
              To:   Disjoint union: (CP^2 u Klein bottle)
              Defn: [Delta_{0,0}, Delta_{1,0}, Delta_{1,1}, Delta_{1,2}, Delta_{2,0}, Delta_{2,1}]
                    --> [Delta_{0,0}, Delta_{1,0}, Delta_{1,1}, Delta_{1,2}, Delta_{2,0}, Delta_{2,1}]
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        The `n`-skeleton of the disjoint union is computed as the
        disjoint union of the `n`-skeleta of the component simplicial
        sets.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: T = simplicial_sets.Torus()
            sage: X = B.disjoint_union(T)
            sage: X.n_skeleton(3).homology()                                            # needs sage.modules
            {0: Z, 1: Z x Z x C2, 2: Z, 3: Z}
        """
    summands: Incomplete
    summand: Incomplete

class DisjointUnionOfSimplicialSets_finite(DisjointUnionOfSimplicialSets, PushoutOfSimplicialSets_finite):
    """
    The disjoint union of finite simplicial sets.
    """
    def __init__(self, factors=None) -> None:
        """
        Return the disjoint union of finite simplicial sets.

        INPUT:

        - ``factors`` -- tuple of simplicial sets

        Return the disjoint union of the simplicial sets in
        ``factors``.  The disjoint union comes equipped with a map
        from each factor. If there are no factors, this returns the
        empty simplicial set.

        EXAMPLES::

            sage: from sage.topology.simplicial_set_constructions import DisjointUnionOfSimplicialSets_finite
            sage: from sage.topology.simplicial_set_examples import Empty
            sage: S = simplicial_sets.Sphere(4)
            sage: DisjointUnionOfSimplicialSets_finite((S,S,S))
            Disjoint union: (S^4 u S^4 u S^4)
            sage: DisjointUnionOfSimplicialSets_finite([Empty(), Empty()]) == Empty()
            True
        """
    def inclusion_map(self, i):
        """
        Return the inclusion map of the `i`-th factor.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: S2 = simplicial_sets.Sphere(2)
            sage: W = S1.disjoint_union(S2, S1)
            sage: W.inclusion_map(1)
            Simplicial set morphism:
              From: S^2
              To:   Disjoint union: (S^1 u S^2 u S^1)
              Defn: [v_0, sigma_2] --> [v_0, sigma_2]
            sage: W.inclusion_map(0).domain()
            S^1
            sage: W.inclusion_map(2).domain()
            S^1
        """

class ConeOfSimplicialSet(SimplicialSet_arbitrary, UniqueRepresentation):
    def __init__(self, base) -> None:
        """
        Return the unreduced cone on a finite simplicial set.

        INPUT:

        - ``base`` -- return the cone on this simplicial set

        Add a point `*` (which will become the base point) and for
        each simplex `\\sigma` in ``base``, add both `\\sigma` and a
        simplex made up of `*` and `\\sigma` (topologically, form the
        join of `*` and `\\sigma`).

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: e = AbstractSimplex(1, name='e')
            sage: X = SimplicialSet({e: (v, v)})
            sage: CX = X.cone() # indirect doctest
            sage: CX.nondegenerate_simplices()
            [*, v, (v,*), e, (e,*)]
            sage: CX.base_point()
            *
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        In the case when the cone is infinite, the `n`-skeleton of the
        cone is computed as the `n`-skeleton of the cone of the
        `n`-skeleton.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: X = B.disjoint_union(B)
            sage: CX = B.cone()
            sage: CX.n_skeleton(3).homology()                                           # needs sage.modules
            {0: 0, 1: 0, 2: 0, 3: Z}
        """

class ConeOfSimplicialSet_finite(ConeOfSimplicialSet, SimplicialSet_finite):
    def __init__(self, base) -> None:
        """
        Return the unreduced cone on a finite simplicial set.

        INPUT:

        - ``base`` -- return the cone on this simplicial set

        Add a point `*` (which will become the base point) and for
        each simplex `\\sigma` in ``base``, add both `\\sigma` and a
        simplex made up of `*` and `\\sigma` (topologically, form the
        join of `*` and `\\sigma`).

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: e = AbstractSimplex(1, name='e')
            sage: X = SimplicialSet({e: (v, v)})
            sage: CX = X.cone() # indirect doctest
            sage: CX.nondegenerate_simplices()
            [*, v, (v,*), e, (e,*)]
            sage: CX.base_point()
            *
        """
    def base_as_subset(self):
        """
        If this is the cone `CX` on `X`, return `X` as a subsimplicial set.

        EXAMPLES::

            sage: # needs sage.groups
            sage: X = simplicial_sets.RealProjectiveSpace(4).unset_base_point()
            sage: Y = X.cone()
            sage: Y.base_as_subset()
            Simplicial set with 5 non-degenerate simplices
            sage: Y.base_as_subset() == X
            True
        """
    def map_from_base(self):
        """
        If this is the cone `CX` on `X`, return the inclusion map from `X`.

        EXAMPLES::

            sage: X = simplicial_sets.Simplex(2).n_skeleton(1)
            sage: Y = X.cone()
            sage: Y.map_from_base()
            Simplicial set morphism:
              From: Simplicial set with 6 non-degenerate simplices
              To:   Cone of Simplicial set with 6 non-degenerate simplices
              Defn: [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]
                    --> [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]
        """

class ReducedConeOfSimplicialSet(QuotientOfSimplicialSet):
    def __init__(self, base) -> None:
        """
        Return the reduced cone on a simplicial set.

        INPUT:

        - ``base`` -- return the cone on this simplicial set

        Start with the unreduced cone: take ``base`` and add a point
        `*` (which will become the base point) and for each simplex
        `\\sigma` in ``base``, add both `\\sigma` and a simplex made up
        of `*` and `\\sigma` (topologically, form the join of `*` and
        `\\sigma`).

        Now reduce: take the quotient by the 1-simplex connecting the
        old base point to the new one.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: e = AbstractSimplex(1, name='e')
            sage: X = SimplicialSet({e: (v, v)})
            sage: X = X.set_base_point(v)
            sage: CX = X.cone()  # indirect doctest
            sage: CX.nondegenerate_simplices()
            [*, e, (e,*)]
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        In the case when the cone is infinite, the `n`-skeleton of the
        cone is computed as the `n`-skeleton of the cone of the
        `n`-skeleton.

        EXAMPLES::

            sage: G = groups.misc.MultiplicativeAbelian([2])                            # needs sage.groups
            sage: B = simplicial_sets.ClassifyingSpace(G)                               # needs sage.groups
            sage: B.cone().n_skeleton(3).homology()                                     # needs sage.groups sage.modules
            {0: 0, 1: 0, 2: 0, 3: Z}
        """

class ReducedConeOfSimplicialSet_finite(ReducedConeOfSimplicialSet, QuotientOfSimplicialSet_finite):
    def __init__(self, base) -> None:
        """
        Return the reduced cone on a simplicial set.

        INPUT:

        - ``base`` -- return the cone on this simplicial set

        Start with the unreduced cone: take ``base`` and add a point
        `*` (which will become the base point) and for each simplex
        `\\sigma` in ``base``, add both `\\sigma` and a simplex made up
        of `*` and `\\sigma` (topologically, form the join of `*` and
        `\\sigma`).

        Now reduce: take the quotient by the 1-simplex connecting the
        old base point to the new one.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: e = AbstractSimplex(1, name='e')
            sage: X = SimplicialSet({e: (v, v)})
            sage: X = X.set_base_point(v)
            sage: CX = X.cone()  # indirect doctest
            sage: CX.nondegenerate_simplices()
            [*, e, (e,*)]
        """
    def map_from_base(self):
        """
        If this is the cone `\\tilde{C}X` on `X`, return the map from `X`.

        The map is defined to be the composite `X \\to CX \\to
        \\tilde{C}X`.  This is used by the
        :class:`SuspensionOfSimplicialSet_finite` class to construct
        the reduced suspension: take the quotient of the reduced cone
        by the image of `X` therein.

        EXAMPLES::

            sage: S3 = simplicial_sets.Sphere(3)
            sage: CS3 = S3.cone()
            sage: CS3.map_from_base()
            Simplicial set morphism:
              From: S^3
              To:   Reduced cone of S^3
              Defn: [v_0, sigma_3] --> [*, sigma_3]
        """

class SuspensionOfSimplicialSet(SimplicialSet_arbitrary, UniqueRepresentation):
    def __init__(self, base) -> None:
        """
        Return the (reduced) suspension of a simplicial set.

        INPUT:

        - ``base`` -- return the suspension of this simplicial set

        If this simplicial set ``X=base`` is not pointed, or if it is
        itself an unreduced suspension, return the unreduced
        suspension: the quotient `CX/X`, where `CX` is the (ordinary,
        unreduced) cone on `X`. If `X` is pointed, then use the
        reduced cone instead, and so return the reduced suspension.

        We use `S` to denote unreduced suspension, `\\Sigma` for
        reduced suspension.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: B.suspension()
            Sigma(Classifying space of Multiplicative Abelian group isomorphic to C2)
            sage: B.suspension().n_skeleton(3).homology()                               # needs sage.modules
            {0: 0, 1: 0, 2: C2, 3: 0}

        If ``X`` is finite, the suspension comes with a quotient map
        from the cone::

            sage: S3 = simplicial_sets.Sphere(3)
            sage: S4 = S3.suspension()
            sage: S4.quotient_map()
            Simplicial set morphism:
              From: Reduced cone of S^3
              To:   Sigma(S^3)
              Defn: [*, sigma_3, (sigma_3,*)] --> [*, s_2 s_1 s_0 *, (sigma_3,*)]

        TESTS::

            sage: S3.suspension() == S3.suspension()
            True
            sage: S3.suspension() == simplicial_sets.Sphere(3).suspension()
            False
            sage: B.suspension() == B.suspension()                                      # needs sage.groups
            True
        """
    def n_skeleton(self, n):
        """
        Return the `n`-skeleton of this simplicial set.

        That is, the simplicial set generated by all nondegenerate
        simplices of dimension at most `n`.

        INPUT:

        - ``n`` -- the dimension

        In the case when the suspension is infinite, the `n`-skeleton
        of the suspension is computed as the `n`-skeleton of the
        suspension of the `n`-skeleton.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: SigmaB = B.suspension()
            sage: SigmaB.n_skeleton(4).homology(base_ring=GF(2))                        # needs sage.modules
            {0: Vector space of dimension 0 over Finite Field of size 2,
             1: Vector space of dimension 0 over Finite Field of size 2,
             2: Vector space of dimension 1 over Finite Field of size 2,
             3: Vector space of dimension 1 over Finite Field of size 2,
             4: Vector space of dimension 1 over Finite Field of size 2}
        """
    def __repr_or_latex__(self, output_type=None):
        """
        Print representation, for either :meth:`_repr_` or :meth:`_latex_`.

        INPUT:

        - ``output_type`` -- either ``'latex'`` for LaTeX output or
          anything else for ``str`` output

        We use `S` to denote unreduced suspension, `\\Sigma` for
        reduced suspension.

        EXAMPLES::

            sage: T = simplicial_sets.Torus()
            sage: K = T.suspension(10)
            sage: K.__repr_or_latex__()
            'Sigma^10(Torus)'
            sage: K.__repr_or_latex__('latex')
            '\\\\Sigma^{10}(S^{1} \\\\times S^{1})'
        """

class SuspensionOfSimplicialSet_finite(SuspensionOfSimplicialSet, QuotientOfSimplicialSet_finite):
    """
    The (reduced) suspension of a finite simplicial set.

    See :class:`SuspensionOfSimplicialSet` for more information.
    """
    def __init__(self, base) -> None:
        """
        INPUT:

        - ``base`` -- return the suspension of this finite simplicial set

        See :class:`SuspensionOfSimplicialSet` for more information.

        EXAMPLES::

            sage: X = simplicial_sets.Sphere(3)
            sage: X.suspension(2)
            Sigma^2(S^3)
            sage: Y = X.unset_base_point()
            sage: Y.suspension(2)
            S^2(Simplicial set with 2 non-degenerate simplices)
        """
