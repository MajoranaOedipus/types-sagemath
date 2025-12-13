from .simplicial_set import SimplicialSet_arbitrary as SimplicialSet_arbitrary
from sage.categories.homset import Hom as Hom, Homset as Homset
from sage.categories.morphism import Morphism as Morphism
from sage.categories.simplicial_sets import SimplicialSets as SimplicialSets
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ

class SimplicialSetHomset(Homset):
    """
    A set of morphisms between simplicial sets.

    Once a homset has been constructed in Sage, typically via
    ``Hom(X,Y)`` or ``X.Hom(Y)``, one can use it to construct a
    morphism `f` by specifying a dictionary, the keys of which are the
    nondegenerate simplices in the domain, and the value corresponding
    to `\\sigma` is the simplex `f(\\sigma)` in the codomain.

    EXAMPLES::

        sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
        sage: v = AbstractSimplex(0, name='v')
        sage: w = AbstractSimplex(0, name='w')
        sage: e = AbstractSimplex(1, name='e')
        sage: f = AbstractSimplex(1, name='f')
        sage: X = SimplicialSet({e: (v, w), f: (w, v)})
        sage: Y = SimplicialSet({e: (v, v)})

    Define the homset::

        sage: H = Hom(X, Y)

    Now define a morphism by specifying a dictionary::

        sage: H({v: v, w: v, e: e, f: e})
        Simplicial set morphism:
          From: Simplicial set with 4 non-degenerate simplices
          To:   Simplicial set with 2 non-degenerate simplices
          Defn: [v, w, e, f] --> [v, v, e, e]
    """
    def __call__(self, f, check: bool = True):
        """
        INPUT:

        - ``f`` -- dictionary with keys the simplices of the domain
          and values simplices of the codomain

        - ``check`` -- boolean (default ``True``); pass this to the
          morphism constructor

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: v0 = S1.n_cells(0)[0]
            sage: e = S1.n_cells(1)[0]
            sage: f = {v0: v0, e: v0.apply_degeneracies(0)} # constant map
            sage: Hom(S1, S1)(f)
            Simplicial set endomorphism of S^1
              Defn: Constant map at v_0
        """
    def diagonal_morphism(self):
        """
        Return the diagonal morphism in `\\operatorname{Hom}(S, S \\times S)`.

        EXAMPLES::

            sage: RP2 = simplicial_sets.RealProjectiveSpace(2)                          # needs sage.groups
            sage: Hom(RP2, RP2.product(RP2)).diagonal_morphism()                        # needs sage.groups
            Simplicial set morphism:
              From: RP^2
              To:   RP^2 x RP^2
              Defn: [1, f, f * f] --> [(1, 1), (f, f), (f * f, f * f)]
        """
    def identity(self):
        """
        Return the identity morphism in `\\operatorname{Hom}(S, S)`.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: Hom(S1, S1).identity()
            Simplicial set endomorphism of S^1
              Defn: Identity map
            sage: T = simplicial_sets.Torus()
            sage: Hom(S1, T).identity()
            Traceback (most recent call last):
            ...
            TypeError: identity map is only defined for endomorphism sets
        """
    def constant_map(self, point=None):
        """
        Return the constant map in this homset.

        INPUT:

        - ``point`` -- (default: ``None``) if specified, it must be a 0-simplex
          in the codomain, and it will be the target of the constant map

        If ``point`` is specified, it is the target of the constant
        map. Otherwise, if the codomain is pointed, the target is its
        base point. If the codomain is not pointed and ``point`` is
        not specified, raise an error.

        EXAMPLES::

            sage: S3 = simplicial_sets.Sphere(3)
            sage: T = simplicial_sets.Torus()
            sage: T.n_cells(0)[0].rename('w')
            sage: Hom(S3,T).constant_map()
            Simplicial set morphism:
              From: S^3
              To:   Torus
              Defn: Constant map at w

            sage: S0 = simplicial_sets.Sphere(0)
            sage: v, w = S0.n_cells(0)
            sage: Hom(S3, S0).constant_map(v)
            Simplicial set morphism:
              From: S^3
              To:   S^0
              Defn: Constant map at v_0
            sage: Hom(S3, S0).constant_map(w)
            Simplicial set morphism:
              From: S^3
              To:   S^0
              Defn: Constant map at w_0

        This constant map is not pointed, since it doesn't send the
        base point of `S^3` to the base point of `S^0`::

            sage: Hom(S3, S0).constant_map(w).is_pointed()
            False

        TESTS::

            sage: S0 = S0.unset_base_point()
            sage: Hom(S3, S0).constant_map()
            Traceback (most recent call last):
            ...
            ValueError: codomain is not pointed, so specify a target for the constant map
        """
    def an_element(self):
        """
        Return an element of this homset: a constant map.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: S2 = simplicial_sets.Sphere(2)
            sage: Hom(S2, S1).an_element()
            Simplicial set morphism:
              From: S^2
              To:   S^1
              Defn: Constant map at v_0

            sage: K = simplicial_sets.Simplex(3)
            sage: L = simplicial_sets.Simplex(4)
            sage: d = {K.n_cells(3)[0]: L.n_cells(0)[0].apply_degeneracies(2, 1, 0)}
            sage: Hom(K,L)(d) == Hom(K,L).an_element()
            True
        """
    def __iter__(self):
        '''
        Iterate through all morphisms in this homset.

        This is very slow: it tries all possible targets for the
        maximal nondegenerate simplices and yields those which are
        valid morphisms of simplicial sets. ("Maximal" means
        nondegenerate simplices which are not the faces of other
        nondegenerate simplices.) So if either the domain or the
        codomain has many simplices, the number of possibilities may
        be quite large.

        This is only implemented when the domain is finite.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: T = simplicial_sets.Torus()
            sage: H = Hom(S1, T)
            sage: list(H)
            [Simplicial set morphism:
               From: S^1
               To:   Torus
               Defn: [v_0, sigma_1] --> [(v_0, v_0), (s_0 v_0, sigma_1)],
             Simplicial set morphism:
               From: S^1
               To:   Torus
               Defn: [v_0, sigma_1] --> [(v_0, v_0), (sigma_1, s_0 v_0)],
             Simplicial set morphism:
               From: S^1
               To:   Torus
               Defn: [v_0, sigma_1] --> [(v_0, v_0), (sigma_1, sigma_1)],
             Simplicial set morphism:
               From: S^1
               To:   Torus
               Defn: Constant map at (v_0, v_0)]
            sage: [f.induced_homology_morphism().to_matrix() for f in H]                # needs sage.modules
            [
            [ 1| 0]  [1|0]  [1|0]  [1|0]
            [--+--]  [-+-]  [-+-]  [-+-]
            [ 0|-1]  [0|1]  [0|0]  [0|0]
            [ 0| 1]  [0|0]  [0|1]  [0|0]
            [--+--]  [-+-]  [-+-]  [-+-]
            [ 0| 0], [0|0], [0|0], [0|0]
            ]
        '''

class SimplicialSetMorphism(Morphism):
    def __init__(self, data=None, domain=None, codomain=None, constant=None, identity: bool = False, check: bool = True) -> None:
        """
        Return a morphism of simplicial sets.

        INPUT:

        - ``data`` -- (optional) dictionary defining the map
        - ``domain`` -- simplicial set
        - ``codomain`` -- simplicial set
        - ``constant`` -- (default: ``None``) if not ``None``, then this should
          be a vertex in the codomain, in which case return the
          constant map with this vertex as the target
        - ``identity`` -- boolean (default: ``False``); if ``True``, return the
          identity morphism
        - ``check`` -- boolean (default: ``True``); if ``True``, check
          that this is actually a morphism: it commutes with the face maps

        So to define a map, you must specify ``domain`` and
        ``codomain``. If the map is constant, specify the target (a
        vertex in the codomain) as ``constant``. If the map is the
        identity map, specify ``identity=True``. Otherwise, pass a
        dictionary, ``data``.  The keys of the dictionary are the
        nondegenerate simplices of the domain, the corresponding
        values are simplices in the codomain.

        In fact, the keys in ``data`` do not need to include all of
        the nondegenerate simplices, only those which are not faces of
        other nondegenerate simplices: if `\\sigma` is a face of
        `\\tau`, then the image of `\\sigma` need not be specified.

        EXAMPLES::

            sage: from sage.topology.simplicial_set_morphism import SimplicialSetMorphism
            sage: K = simplicial_sets.Simplex(1)
            sage: S1 = simplicial_sets.Sphere(1)
            sage: v0 = K.n_cells(0)[0]
            sage: v1 = K.n_cells(0)[1]
            sage: e01 = K.n_cells(1)[0]
            sage: w = S1.n_cells(0)[0]
            sage: sigma = S1.n_cells(1)[0]

            sage: f = {v0: w, v1: w, e01: sigma}
            sage: SimplicialSetMorphism(f, K, S1)
            Simplicial set morphism:
              From: 1-simplex
              To:   S^1
              Defn: [(0,), (1,), (0, 1)] --> [v_0, v_0, sigma_1]

        The same map can be defined as follows::

            sage: H = Hom(K, S1)
            sage: H(f)
            Simplicial set morphism:
              From: 1-simplex
              To:   S^1
              Defn: [(0,), (1,), (0, 1)] --> [v_0, v_0, sigma_1]

        Also, this map can be defined by specifying where the
        1-simplex goes; the vertices then go where they have to, to
        satisfy the condition `d_i \\circ f = f \\circ d_i`::

            sage: H = Hom(K, S1)
            sage: H({e01: sigma})
            Simplicial set morphism:
              From: 1-simplex
              To:   S^1
              Defn: [(0,), (1,), (0, 1)] --> [v_0, v_0, sigma_1]

        A constant map::

            sage: g = {e01: w.apply_degeneracies(0)}
            sage: SimplicialSetMorphism(g, K, S1)
            Simplicial set morphism:
              From: 1-simplex
              To:   S^1
              Defn: Constant map at v_0

        The same constant map::

            sage: SimplicialSetMorphism(domain=K, codomain=S1, constant=w)
            Simplicial set morphism:
              From: 1-simplex
              To:   S^1
              Defn: Constant map at v_0

        An identity map::

            sage: SimplicialSetMorphism(domain=K, codomain=K, identity=True)
            Simplicial set endomorphism of 1-simplex
              Defn: Identity map

        Defining a map by specifying it on only some of the simplices
        in the domain::

            sage: S5 = simplicial_sets.Sphere(5)
            sage: s = S5.n_cells(5)[0]
            sage: one = S5.Hom(S5)({s: s})
            sage: one
            Simplicial set endomorphism of S^5
              Defn: Identity map

        TESTS:

        A non-map::

            sage: h = {w: v0, sigma: e01}
            sage: SimplicialSetMorphism(h, S1, K)
            Traceback (most recent call last):
            ...
            ValueError: the dictionary does not define a map of simplicial sets

        Another non-map::

            sage: h = {w: v0, v0: w, sigma: e01}
            sage: SimplicialSetMorphism(h, S1, K)
            Traceback (most recent call last):
            ...
            ValueError: at least one simplex in the defining dictionary is not in the domain

        A non-identity map::

            sage: SimplicialSetMorphism(domain=K, codomain=S1, identity=True)
            Traceback (most recent call last):
            ...
            TypeError: identity map is only defined for endomorphism sets

        An improperly partially defined map::

            sage: h = {w: v0}
            sage: SimplicialSetMorphism(h, S1, K)
            Traceback (most recent call last):
            ...
            ValueError: the image of at least one simplex in the domain is not defined
        """
    def __eq__(self, other):
        """
        Two morphisms are equal iff their domains are the same, their
        codomains are the same, and their defining dictionaries are
        the same.

        EXAMPLES::

            sage: S = simplicial_sets.Sphere(1)
            sage: T = simplicial_sets.Torus()
            sage: T_c = T.constant_map() * T.base_point_map()
            sage: S_c = S.constant_map() * S.base_point_map()
            sage: T_c == S_c
            True
            sage: T.constant_map() == S.constant_map()
            False
            sage: K = simplicial_sets.Sphere(1)
            sage: K.constant_map() == S.constant_map()
            False

            sage: Point = simplicial_sets.Point()
            sage: f = Point._map_from_empty_set()
            sage: Empty = f.domain()
            sage: g = Empty.constant_map()
            sage: f == g
            True
        """
    def __ne__(self, other):
        """
        The negation of ``__eq__``.

        EXAMPLES::

            sage: S0 = simplicial_sets.Sphere(0)
            sage: v,w = S0.n_cells(0)
            sage: H = Hom(S0, S0)
            sage: H({v:v, w:w}) != H({v:w, w:v})
            True
            sage: H({v:v, w:w}) != H({w:w, v:v})
            False
        """
    def __call__(self, x):
        """
        Return the image of ``x`` under this morphism.

        INPUT:

        - ``x`` -- a simplex of the domain

        EXAMPLES::

            sage: K = simplicial_sets.Simplex(1)
            sage: S1 = simplicial_sets.Sphere(1)
            sage: v0 = K.n_cells(0)[0]
            sage: v1 = K.n_cells(0)[1]
            sage: e01 = K.n_cells(1)[0]
            sage: w = S1.n_cells(0)[0]
            sage: sigma = S1.n_cells(1)[0]
            sage: d = {v0: w, v1: w, e01: sigma}
            sage: f = Hom(K, S1)(d)
            sage: f(e01) # indirect doctest
            sigma_1

            sage: one = Hom(S1, S1).identity()
            sage: e = S1.n_cells(1)[0]
            sage: one(e) == e
            True

            sage: B = AbelianGroup([2]).nerve()                                         # needs sage.groups
            sage: c = B.constant_map()                                                  # needs sage.groups
            sage: c(B.n_cells(2)[0])                                                    # needs sage.groups
            s_1 s_0 *
        """
    def image(self):
        """
        Return the image of this morphism as a subsimplicial set of the
        codomain.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: T = S1.product(S1)
            sage: K = T.factor(0, as_subset=True)
            sage: f = S1.Hom(T)({S1.n_cells(0)[0]: K.n_cells(0)[0],
            ....:                S1.n_cells(1)[0]: K.n_cells(1)[0]}); f
            Simplicial set morphism:
              From: S^1
              To:   S^1 x S^1
              Defn: [v_0, sigma_1] --> [(v_0, v_0), (sigma_1, s_0 v_0)]
            sage: f.image()
            Simplicial set with 2 non-degenerate simplices
            sage: f.image().homology()                                                  # needs sage.modules
            {0: 0, 1: Z}

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: B.constant_map().image()
            Point
            sage: Hom(B,B).identity().image() == B
            True
        """
    def is_identity(self):
        """
        Return ``True`` if this morphism is an identity map.

        EXAMPLES::

            sage: K = simplicial_sets.Simplex(1)
            sage: v0 = K.n_cells(0)[0]
            sage: v1 = K.n_cells(0)[1]
            sage: e01 = K.n_cells(1)[0]
            sage: L = simplicial_sets.Simplex(2).n_skeleton(1)
            sage: w0 = L.n_cells(0)[0]
            sage: w1 = L.n_cells(0)[1]
            sage: w2 = L.n_cells(0)[2]
            sage: f01 = L.n_cells(1)[0]
            sage: f02 = L.n_cells(1)[1]
            sage: f12 = L.n_cells(1)[2]

            sage: d = {v0:w0, v1:w1, e01:f01}
            sage: f = K.Hom(L)(d)
            sage: f.is_identity()
            False
            sage: d = {w0:v0, w1:v1, w2:v1, f01:e01, f02:e01, f12: v1.apply_degeneracies(0,)}
            sage: g = L.Hom(K)(d)
            sage: (g*f).is_identity()
            True
            sage: (f*g).is_identity()
            False
            sage: (f*g).induced_homology_morphism().to_matrix(1)                        # needs sage.modules
            [0]

            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)                          # needs sage.groups
            sage: RP5.n_skeleton(2).inclusion_map().is_identity()                       # needs sage.groups
            False
            sage: RP5.n_skeleton(5).inclusion_map().is_identity()                       # needs sage.groups
            True

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: Hom(B,B).identity().is_identity()
            True
            sage: Hom(B,B).constant_map().is_identity()
            False
        """
    def is_surjective(self):
        """
        Return ``True`` if this map is surjective.

        EXAMPLES::

            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)                          # needs sage.groups
            sage: RP2 = RP5.n_skeleton(2)                                               # needs sage.groups
            sage: RP2.inclusion_map().is_surjective()                                   # needs sage.groups
            False

            sage: RP5_2 = RP5.quotient(RP2)                                             # needs sage.groups
            sage: RP5_2.quotient_map().is_surjective()                                  # needs sage.groups
            True

            sage: K = RP5_2.pullback(RP5_2.quotient_map(), RP5_2.base_point_map())      # needs sage.groups
            sage: f = K.universal_property(RP2.inclusion_map(), RP2.constant_map())     # needs sage.groups
            sage: f.is_surjective()                                                     # needs sage.groups
            True
        """
    def is_injective(self):
        """
        Return ``True`` if this map is injective.

        EXAMPLES::

            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)                          # needs sage.groups
            sage: RP2 = RP5.n_skeleton(2)                                               # needs sage.groups
            sage: RP2.inclusion_map().is_injective()                                    # needs sage.groups
            True

            sage: RP5_2 = RP5.quotient(RP2)                                             # needs sage.groups
            sage: RP5_2.quotient_map().is_injective()                                   # needs sage.groups
            False

            sage: K = RP5_2.pullback(RP5_2.quotient_map(), RP5_2.base_point_map())      # needs sage.groups
            sage: f = K.universal_property(RP2.inclusion_map(), RP2.constant_map())     # needs sage.groups
            sage: f.is_injective()                                                      # needs sage.groups
            True
        """
    def is_bijective(self):
        """
        Return ``True`` if this map is bijective.

        EXAMPLES::

            sage: RP5 = simplicial_sets.RealProjectiveSpace(5)                          # needs sage.groups
            sage: RP2 = RP5.n_skeleton(2)                                               # needs sage.groups
            sage: RP2.inclusion_map().is_bijective()                                    # needs sage.groups
            False

            sage: RP5_2 = RP5.quotient(RP2)                                             # needs sage.groups
            sage: RP5_2.quotient_map().is_bijective()                                   # needs sage.groups
            False

            sage: K = RP5_2.pullback(RP5_2.quotient_map(), RP5_2.base_point_map())      # needs sage.groups
            sage: f = K.universal_property(RP2.inclusion_map(), RP2.constant_map())     # needs sage.groups
            sage: f.is_bijective()                                                      # needs sage.groups
            True
        """
    def is_pointed(self):
        """
        Return ``True`` if this is a pointed map.

        That is, return ``True`` if the domain and codomain are
        pointed and this morphism preserves the base point.

        EXAMPLES::

            sage: S0 = simplicial_sets.Sphere(0)
            sage: f = Hom(S0,S0).identity()
            sage: f.is_pointed()
            True
            sage: v = S0.n_cells(0)[0]
            sage: w = S0.n_cells(0)[1]
            sage: g = Hom(S0,S0)({v:v, w:v})
            sage: g.is_pointed()
            True
            sage: t = Hom(S0,S0)({v:w, w:v})
            sage: t.is_pointed()
            False
        """
    def is_constant(self):
        """
        Return ``True`` if this morphism is a constant map.

        EXAMPLES::

            sage: K = simplicial_sets.KleinBottle()
            sage: S4 = simplicial_sets.Sphere(4)
            sage: c = Hom(K, S4).constant_map()
            sage: c.is_constant()
            True
            sage: X = S4.n_skeleton(3) # a point
            sage: X.inclusion_map().is_constant()
            True
            sage: eta = simplicial_sets.HopfMap()
            sage: eta.is_constant()
            False
        """
    def pushout(self, *others):
        """
        Return the pushout of this morphism along with ``others``.

        INPUT:

        - ``others`` -- morphisms of simplicial sets, the domains of
          which must all equal that of ``self``

        This returns the pushout as a simplicial set. See
        :class:`sage.topology.simplicial_set_constructions.PushoutOfSimplicialSets`
        for more documentation and examples.

        EXAMPLES::

            sage: T = simplicial_sets.Torus()
            sage: K = simplicial_sets.KleinBottle()
            sage: init_T = T._map_from_empty_set()
            sage: init_K = K._map_from_empty_set()
            sage: D = init_T.pushout(init_K); D  # the disjoint union as a pushout
            Pushout of maps:
              Simplicial set morphism:
                From: Empty simplicial set
                To:   Torus
                Defn: [] --> []
              Simplicial set morphism:
                From: Empty simplicial set
                To:   Klein bottle
                Defn: [] --> []
        """
    def pullback(self, *others):
        """
        Return the pullback of this morphism along with ``others``.

        INPUT:

        - ``others`` -- morphisms of simplicial sets, the codomains of
          which must all equal that of ``self``

        This returns the pullback as a simplicial set. See
        :class:`sage.topology.simplicial_set_constructions.PullbackOfSimplicialSets`
        for more documentation and examples.

        EXAMPLES::

            sage: T = simplicial_sets.Torus()
            sage: K = simplicial_sets.KleinBottle()
            sage: term_T = T.constant_map()
            sage: term_K = K.constant_map()
            sage: P = term_T.pullback(term_K); P  # the product as a pullback
            Pullback of maps:
              Simplicial set morphism:
                From: Torus
                To:   Point
                Defn: Constant map at *
              Simplicial set morphism:
                From: Klein bottle
                To:   Point
                Defn: Constant map at *
        """
    def equalizer(self, other):
        """
        Return the equalizer of this map with ``other``.

        INPUT:

        - ``other`` -- a morphism with the same domain and codomain as this map

        If the two maps are `f, g: X \\to Y`, then the equalizer `P` is
        constructed as the pullback ::

            P ----> X
            |       |
            V       V
            X --> X x Y

        where the two maps `X \\to X \\times Y` are `(1,f)` and `(1,g)`.

        EXAMPLES::

            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: w = AbstractSimplex(0, name='w')
            sage: x = AbstractSimplex(0, name='x')
            sage: evw = AbstractSimplex(1, name='vw')
            sage: evx = AbstractSimplex(1, name='vx')
            sage: ewx = AbstractSimplex(1, name='wx')
            sage: X = SimplicialSet({evw: (w, v), evx: (x, v)})
            sage: Y = SimplicialSet({evw: (w, v), evx: (x, v), ewx: (x, w)})

        Here `X` is a wedge of two 1-simplices (a horn, that is), and
        `Y` is the boundary of a 2-simplex. The map `f` includes the
        two 1-simplices into `Y`, while the map `g` maps both
        1-simplices to the same edge in `Y`. ::

            sage: f = Hom(X, Y)({v:v, w:w, x:x, evw:evw, evx:evx})
            sage: g = Hom(X, Y)({v:v, w:x, x:x, evw:evx, evx:evx})
            sage: P = f.equalizer(g)
            sage: P
            Pullback of maps:
              Simplicial set morphism:
                From: Simplicial set with 5 non-degenerate simplices
                To:   Simplicial set with 5 non-degenerate simplices x Simplicial set with 6 non-degenerate simplices
                Defn: [v, w, x, vw, vx] --> [(v, v), (w, w), (x, x), (vw, vw), (vx, vx)]
              Simplicial set morphism:
                From: Simplicial set with 5 non-degenerate simplices
                To:   Simplicial set with 5 non-degenerate simplices x Simplicial set with 6 non-degenerate simplices
                Defn: [v, w, x, vw, vx] --> [(v, v), (w, x), (x, x), (vw, vx), (vx, vx)]
        """
    def coequalizer(self, other):
        """
        Return the coequalizer of this map with ``other``.

        INPUT:

        - ``other`` -- a morphism with the same domain and codomain as this map

        If the two maps are `f, g: X \\to Y`, then the coequalizer `P` is
        constructed as the pushout ::

            X v Y --> Y
              |       |
              V       V
              Y ----> P

        where the upper left corner is the coproduct of `X` and `Y`
        (the wedge if they are pointed, the disjoint union otherwise),
        and the two maps `X \\amalg Y \\to Y` are `f \\amalg 1` and `g
        \\amalg 1`.

        EXAMPLES::

            sage: L = simplicial_sets.Simplex(2)
            sage: pt = L.n_cells(0)[0]
            sage: e = L.n_cells(1)[0]
            sage: K = L.subsimplicial_set([e])
            sage: f = K.inclusion_map()
            sage: v,w = K.n_cells(0)
            sage: g = Hom(K,L)({v:pt, w:pt, e:pt.apply_degeneracies(0)})
            sage: P = f.coequalizer(g); P
            Pushout of maps:
              Simplicial set morphism:
                From: Disjoint union: (Simplicial set with 3 non-degenerate simplices u 2-simplex)
                To:   2-simplex
                Defn: ...
              Simplicial set morphism:
                From: Disjoint union: (Simplicial set with 3 non-degenerate simplices u 2-simplex)
                To:   2-simplex
                Defn: ...
        """
    def mapping_cone(self):
        """
        Return the mapping cone defined by this map.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: v_0, sigma_1 = S1.nondegenerate_simplices()
            sage: K = simplicial_sets.Simplex(2).n_skeleton(1)

        The mapping cone will be a little smaller if we use only
        pointed simplicial sets. `S^1` is already pointed, but not
        `K`. ::

            sage: L = K.set_base_point(K.n_cells(0)[0])
            sage: u,v,w = L.n_cells(0)
            sage: e,f,g = L.n_cells(1)
            sage: h = L.Hom(S1)({u:v_0, v:v_0, w:v_0, e:sigma_1,
            ....:                f:v_0.apply_degeneracies(0), g:sigma_1})
            sage: h
            Simplicial set morphism:
              From: Simplicial set with 6 non-degenerate simplices
              To:   S^1
              Defn: [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]
                    --> [v_0, v_0, v_0, sigma_1, s_0 v_0, sigma_1]
            sage: h.induced_homology_morphism().to_matrix()                             # needs sage.modules
            [1|0]
            [-+-]
            [0|2]
            sage: X = h.mapping_cone()
            sage: X.homology() == simplicial_sets.RealProjectiveSpace(2).homology()     # needs sage.groups sage.modules
            True
        """
    def product(self, *others):
        """
        Return the product of this map with ``others``.

        - ``others`` -- morphisms of simplicial sets

        If the relevant maps are `f_i: X_i \\to Y_i`, this returns the
        natural map `\\prod X_i \\to \\prod Y_i`.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: f = Hom(S1,S1).identity()
            sage: f.product(f).is_bijective()
            True
            sage: g = S1.constant_map(S1)
            sage: g.product(g).is_bijective()
            False
        """
    def coproduct(self, *others):
        """
        Return the coproduct of this map with ``others``.

        - ``others`` -- morphisms of simplicial sets

        If the relevant maps are `f_i: X_i \\to Y_i`, this returns the
        natural map `\\amalg X_i \\to \\amalg Y_i`.

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: f = Hom(S1,S1).identity()
            sage: f.coproduct(f).is_bijective()
            True
            sage: g = S1.constant_map(S1)
            sage: g.coproduct(g).is_bijective()
            False
        """
    def suspension(self, n: int = 1):
        """
        Return the `n`-th suspension of this morphism of simplicial sets.

        INPUT:

        - ``n`` -- nonnegative integer (default: 1)

        EXAMPLES::

            sage: eta = simplicial_sets.HopfMap()
            sage: mc_susp_eta = eta.suspension().mapping_cone()
            sage: susp_mc_eta = eta.mapping_cone().suspension()
            sage: mc_susp_eta.homology() == susp_mc_eta.homology()                      # needs sage.modules
            True

        This uses reduced suspensions if the original morphism is
        pointed, unreduced otherwise. So for example, if a constant
        map is not pointed, its suspension is not a constant map::

            sage: L = simplicial_sets.Simplex(1)
            sage: L.constant_map().is_pointed()
            False
            sage: f = L.constant_map().suspension()
            sage: f.is_constant()
            False

            sage: K = simplicial_sets.Sphere(3)
            sage: K.constant_map().is_pointed()
            True
            sage: g = K.constant_map().suspension()
            sage: g.is_constant()
            True

            sage: h = K.identity().suspension()
            sage: h.is_identity()
            True
        """
    def n_skeleton(self, n, domain=None, codomain=None):
        """
        Return the restriction of this morphism to the n-skeleta of the
        domain and codomain

        INPUT:

        - ``n`` -- the dimension

        - ``domain`` -- (optional) the domain. Specify this to
          explicitly specify the domain; otherwise, Sage will attempt
          to compute it. Specifying this can be useful if the domain
          is built as a pushout or pullback, so trying to compute it
          may lead to computing the `n`-skeleton of a map, causing an
          infinite recursion. (Users should not have to specify this,
          but it may be useful for developers.)

        - ``codomain`` -- (optional) the codomain

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = groups.misc.MultiplicativeAbelian([2])
            sage: B = simplicial_sets.ClassifyingSpace(G)
            sage: one = Hom(B,B).identity()
            sage: one.n_skeleton(3)
            Simplicial set endomorphism of Simplicial set with 4 non-degenerate simplices
              Defn: Identity map
            sage: c = Hom(B,B).constant_map()
            sage: c.n_skeleton(3)
            Simplicial set endomorphism of Simplicial set with 4 non-degenerate simplices
              Defn: Constant map at 1

            sage: K = simplicial_sets.Simplex(2)
            sage: L = K.subsimplicial_set(K.n_cells(0)[:2])
            sage: L.nondegenerate_simplices()
            [(0,), (1,)]
            sage: L.inclusion_map()
            Simplicial set morphism:
              From: Simplicial set with 2 non-degenerate simplices
              To:   2-simplex
              Defn: [(0,), (1,)] --> [(0,), (1,)]
            sage: L.inclusion_map().n_skeleton(1)
            Simplicial set morphism:
              From: Simplicial set with 2 non-degenerate simplices
              To:   Simplicial set with 6 non-degenerate simplices
              Defn: [(0,), (1,)] --> [(0,), (1,)]
        """
    def associated_chain_complex_morphism(self, base_ring=..., augmented: bool = False, cochain: bool = False):
        """
        Return the associated chain complex morphism of ``self``.

        INPUT:

        - ``base_ring`` -- default ``ZZ``
        - ``augmented`` -- boolean (default: ``False``); if ``True``,
          return the augmented complex
        - ``cochain`` -- boolean (default: ``False``); if ``True``,
          return the cochain complex

        EXAMPLES::

            sage: S1 = simplicial_sets.Sphere(1)
            sage: v0 = S1.n_cells(0)[0]
            sage: e = S1.n_cells(1)[0]
            sage: f = {v0: v0, e: v0.apply_degeneracies(0)} # constant map
            sage: g = Hom(S1, S1)(f)
            sage: g.associated_chain_complex_morphism().to_matrix()                     # needs sage.modules
            [1|0]
            [-+-]
            [0|0]
        """
    def induced_homology_morphism(self, base_ring=None, cohomology: bool = False):
        """
        Return the map in (co)homology induced by this map.

        INPUT:

        - ``base_ring`` -- must be a field (default: ``QQ``)

        - ``cohomology`` -- boolean (default: ``False``); if
          ``True``, the map induced in cohomology rather than homology

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.topology.simplicial_set import AbstractSimplex, SimplicialSet
            sage: v = AbstractSimplex(0, name='v')
            sage: w = AbstractSimplex(0, name='w')
            sage: e = AbstractSimplex(1, name='e')
            sage: f = AbstractSimplex(1, name='f')
            sage: X = SimplicialSet({e: (v, w), f: (w, v)})
            sage: Y = SimplicialSet({e: (v, v)})
            sage: H = Hom(X, Y)
            sage: f = H({v: v, w: v, e: e, f: e})
            sage: g = f.induced_homology_morphism()
            sage: g.to_matrix()
            [1|0]
            [-+-]
            [0|2]
            sage: g3 = f.induced_homology_morphism(base_ring=GF(3), cohomology=True)
            sage: g3.to_matrix()
            [1|0]
            [-+-]
            [0|2]
        """
