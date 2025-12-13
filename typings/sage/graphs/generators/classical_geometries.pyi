from sage.arith.misc import is_prime_power as is_prime_power
from sage.graphs.graph import Graph as Graph
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField

def SymplecticPolarGraph(d, q, algorithm=None):
    """
    Return the Symplectic Polar Graph `Sp(d,q)`.

    The Symplectic Polar Graph `Sp(d,q)` is built from a projective space of
    dimension `d-1` over a field `F_q`, and a symplectic form `f`. Two vertices
    `u,v` are made adjacent if `f(u,v)=0`.

    See the page `on symplectic graphs on Andries Brouwer's website
    <https://www.win.tue.nl/~aeb/graphs/Sp.html>`_.

    INPUT:

    - ``d``, ``q`` -- integers; note that only even values of `d` are accepted
      by the function

    - ``algorithm`` -- string (default: ``None``); if set to ``'gap'``, then the
      computation is carried via GAP library interface, computing totally
      singular subspaces, which is faster for `q>3`.  Otherwise it is done
      directly.

    EXAMPLES:

    Computation of the spectrum of `Sp(6,2)`::

        sage: g = graphs.SymplecticPolarGraph(6, 2)
        sage: g.is_strongly_regular(parameters=True)
        (63, 30, 13, 15)
        sage: set(g.spectrum()) == {-5, 3, 30}                                          # needs sage.rings.number_field
        True

    The parameters of `Sp(4,q)` are the same as of `O(5,q)`, but they are
    not isomorphic if `q` is odd::

        sage: G = graphs.SymplecticPolarGraph(4, 3)
        sage: G.is_strongly_regular(parameters=True)
        (40, 12, 2, 4)

        sage: # needs sage.libs.gap
        sage: O = graphs.OrthogonalPolarGraph(5, 3)
        sage: O.is_strongly_regular(parameters=True)
        (40, 12, 2, 4)
        sage: O.is_isomorphic(G)
        False
        sage: S = graphs.SymplecticPolarGraph(6, 4, algorithm='gap')    # not tested (long time)
        sage: S.is_strongly_regular(parameters=True)                    # not tested (long time)
        (1365, 340, 83, 85)

    TESTS::

        sage: graphs.SymplecticPolarGraph(4,4,algorithm='gap').is_strongly_regular(parameters=True)                     # needs sage.libs.gap
        (85, 20, 3, 5)
        sage: graphs.SymplecticPolarGraph(4,4).is_strongly_regular(parameters=True)     # needs sage.libs.pari
        (85, 20, 3, 5)
        sage: graphs.SymplecticPolarGraph(4,4,algorithm='blah')
        Traceback (most recent call last):
        ...
        ValueError: unknown algorithm!
    """
def AffineOrthogonalPolarGraph(d, q, sign: str = '+'):
    '''
    Return the affine polar graph `VO^+(d,q),VO^-(d,q)` or `VO(d,q)`.

    Affine Polar graphs are built from a `d`-dimensional vector space over
    `F_q`, and a quadratic form which is hyperbolic, elliptic or parabolic
    according to the value of ``sign``.

    Note that `VO^+(d,q),VO^-(d,q)` are strongly regular graphs, while `VO(d,q)`
    is not.

    For more information on Affine Polar graphs, see `Affine Polar Graphs page
    of Andries Brouwer\'s website <https://www.win.tue.nl/~aeb/graphs/VO.html>`_.

    INPUT:

    - ``d`` -- integer; ``d`` must be even if ``sign is not None``, and odd
      otherwise

    - ``q`` -- integer; a power of a prime number, as `F_q` must exist

    - ``sign`` -- string (default: ``\'+\'``); must be equal to ``\'+\'``, ``\'-\'``,
      or ``None`` to compute (respectively) `VO^+(d,q),VO^-(d,q)` or
      `VO(d,q)`

    .. NOTE::

        The graph `VO^\\epsilon(d,q)` is the graph induced by the
        non-neighbors of a vertex in an :meth:`Orthogonal Polar Graph
        <OrthogonalPolarGraph>` `O^\\epsilon(d+2,q)`.

    EXAMPLES:

    The :meth:`Brouwer-Haemers graph <BrouwerHaemersGraph>` is isomorphic to
    `VO^-(4,3)`::

        sage: g = graphs.AffineOrthogonalPolarGraph(4,3,"-")                            # needs sage.libs.gap
        sage: g.is_isomorphic(graphs.BrouwerHaemersGraph())                             # needs sage.libs.gap
        True

    Some examples from `Brouwer\'s table or strongly regular graphs
    <https://www.win.tue.nl/~aeb/graphs/srg/srgtab.html>`_::

        sage: # needs sage.libs.gap
        sage: g = graphs.AffineOrthogonalPolarGraph(6,2,"-"); g
        Affine Polar Graph VO^-(6,2): Graph on 64 vertices
        sage: g.is_strongly_regular(parameters=True)
        (64, 27, 10, 12)
        sage: g = graphs.AffineOrthogonalPolarGraph(6,2,"+"); g
        Affine Polar Graph VO^+(6,2): Graph on 64 vertices
        sage: g.is_strongly_regular(parameters=True)
        (64, 35, 18, 20)

    When ``sign is None``::

        sage: # needs sage.libs.gap
        sage: g = graphs.AffineOrthogonalPolarGraph(5,2,None); g
        Affine Polar Graph VO^-(5,2): Graph on 32 vertices
        sage: g.is_strongly_regular(parameters=True)
        False
        sage: g.is_regular()
        True
        sage: g.is_vertex_transitive()
        True
    '''
def OrthogonalPolarGraph(m, q, sign: str = '+'):
    '''
    Return the Orthogonal Polar Graph `O^{\\epsilon}(m,q)`.

    For more information on Orthogonal Polar graphs, see the `page of Andries
    Brouwer\'s website <https://www.win.tue.nl/~aeb/graphs/srghub.html>`_.

    INPUT:

    - ``m``, ``q`` -- integers; `q` must be a prime power

    - ``sign`` -- string (default: ``\'+\'``); must be ``\'+\'`` or ``\'-\'`` if `m`
      is even, ``\'+\'`` (default) otherwise

    EXAMPLES::

        sage: # needs sage.libs.gap
        sage: G = graphs.OrthogonalPolarGraph(6,3,"+"); G
        Orthogonal Polar Graph O^+(6, 3): Graph on 130 vertices
        sage: G.is_strongly_regular(parameters=True)
        (130, 48, 20, 16)
        sage: G = graphs.OrthogonalPolarGraph(6,3,"-"); G
        Orthogonal Polar Graph O^-(6, 3): Graph on 112 vertices
        sage: G.is_strongly_regular(parameters=True)
        (112, 30, 2, 10)
        sage: G = graphs.OrthogonalPolarGraph(5,3); G
        Orthogonal Polar Graph O(5, 3): Graph on 40 vertices
        sage: G.is_strongly_regular(parameters=True)
        (40, 12, 2, 4)
        sage: G = graphs.OrthogonalPolarGraph(8,2,"+"); G
        Orthogonal Polar Graph O^+(8, 2): Graph on 135 vertices
        sage: G.is_strongly_regular(parameters=True)
        (135, 70, 37, 35)
        sage: G = graphs.OrthogonalPolarGraph(8,2,"-"); G
        Orthogonal Polar Graph O^-(8, 2): Graph on 119 vertices
        sage: G.is_strongly_regular(parameters=True)
        (119, 54, 21, 27)

    TESTS::

        sage: G = graphs.OrthogonalPolarGraph(4,3,"")                                   # needs sage.libs.gap
        Traceback (most recent call last):
        ...
        ValueError: sign must be equal to either \'-\' or \'+\' when m is even
        sage: G = graphs.OrthogonalPolarGraph(5,3,"-")                                  # needs sage.libs.gap
        Traceback (most recent call last):
        ...
        ValueError: sign must be equal to either \'\' or \'+\' when m is odd
    '''
def NonisotropicOrthogonalPolarGraph(m, q, sign: str = '+', perp=None):
    '''
    Return the Graph `NO^{\\epsilon,\\perp}_{m}(q)`.

    Let the vectorspace of dimension `m` over `F_q` be endowed with a
    nondegenerate quadratic form `F`, of type ``sign`` for `m` even.

    * `m` even: assume further that `q=2` or `3`. Returns the graph of the
      points (in the underlying projective space) `x` satisfying `F(x)=1`, with
      adjacency given by orthogonality w.r.t. `F`. Parameter ``perp`` is
      ignored.

    * `m` odd: if ``perp`` is not ``None``, then we assume that `q=5` and return
      the graph of the points `x` satisfying `F(x)=\\pm 1` if ``sign="+"``,
      respectively `F(x) \\in \\{2,3\\}` if ``sign="-"``, with adjacency given by
      orthogonality w.r.t. `F` (cf. Sect 7.D of [BL1984]_). Otherwise return
      the graph of nongenerate hyperplanes of type ``sign``, adjacent whenever
      the intersection is degenerate (cf. Sect. 7.C of [BL1984]_).
      Note that for `q=2` one will get a complete graph.

    For more information, see Sect. 9.9 of [BH2012]_ and [BL1984]_. Note that
    the `page of Andries Brouwer\'s website
    <https://www.win.tue.nl/~aeb/graphs/srghub.html>`_ uses different notation.

    INPUT:

    - ``m`` -- integer;  half the dimension of the underlying vectorspace

    - ``q`` -- a power of a prime number, the size of the underlying field

    - ``sign`` -- string (default: ``\'+\'``); must be either ``\'+\'`` or ``\'-\'``

    EXAMPLES:

    `NO^-(4,2)` is isomorphic to Petersen graph::

        sage: g = graphs.NonisotropicOrthogonalPolarGraph(4,2,\'-\'); g                   # needs sage.libs.gap
        NO^-(4, 2): Graph on 10 vertices
        sage: g.is_strongly_regular(parameters=True)                                    # needs sage.libs.gap
        (10, 3, 0, 1)

    `NO^-(6,2)` and `NO^+(6,2)`::

        sage: # needs sage.libs.gap
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(6,2,\'-\')
        sage: g.is_strongly_regular(parameters=True)
        (36, 15, 6, 6)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(6,2,\'+\'); g
        NO^+(6, 2): Graph on 28 vertices
        sage: g.is_strongly_regular(parameters=True)
        (28, 15, 6, 10)

    `NO^+(8,2)`::

        sage: g = graphs.NonisotropicOrthogonalPolarGraph(8,2,\'+\')                      # needs sage.libs.gap
        sage: g.is_strongly_regular(parameters=True)                                    # needs sage.libs.gap
        (120, 63, 30, 36)

    Wilbrink\'s graphs for `q=5`::

        sage: # needs sage.libs.gap
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(5,5,perp=1)
        sage: g.is_strongly_regular(parameters=True)    # long time
        (325, 60, 15, 10)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(5,5,\'-\',perp=1)
        sage: g.is_strongly_regular(parameters=True)    # long time
        (300, 65, 10, 15)

    Wilbrink\'s graphs::

        sage: # needs sage.libs.gap
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(5,4,\'+\')
        sage: g.is_strongly_regular(parameters=True)
        (136, 75, 42, 40)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(5,4,\'-\')
        sage: g.is_strongly_regular(parameters=True)
        (120, 51, 18, 24)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(7,4,\'+\'); g        # not tested (long time)
        NO^+(7, 4): Graph on 2080 vertices
        sage: g.is_strongly_regular(parameters=True)                         # not tested (long time)
        (2080, 1071, 558, 544)

    TESTS::

        sage: # needs sage.libs.gap
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(4,2); g
        NO^+(4, 2): Graph on 6 vertices
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(4,3,\'-\')
        sage: g.is_strongly_regular(parameters=True)
        (15, 6, 1, 3)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(3,5,\'-\',perp=1); g
        NO^-,perp(3, 5): Graph on 10 vertices
        sage: g.is_strongly_regular(parameters=True)
        (10, 3, 0, 1)

        sage: # long time, needs sage.libs.gap
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(6,3,\'+\')
        sage: g.is_strongly_regular(parameters=True)
        (117, 36, 15, 9)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(6,3,\'-\'); g
        NO^-(6, 3): Graph on 126 vertices
        sage: g.is_strongly_regular(parameters=True)
        (126, 45, 12, 18)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(5,5,\'-\')
        sage: g.is_strongly_regular(parameters=True)
        (300, 104, 28, 40)
        sage: g = graphs.NonisotropicOrthogonalPolarGraph(5,5,\'+\')
        sage: g.is_strongly_regular(parameters=True)
        (325, 144, 68, 60)

        sage: g = graphs.NonisotropicOrthogonalPolarGraph(6,4,\'+\')
        Traceback (most recent call last):
        ...
        ValueError: for m even q must be 2 or 3
    '''
def UnitaryPolarGraph(m, q, algorithm: str = 'gap'):
    """
    Return the Unitary Polar Graph `U(m,q)`.

    For more information on Unitary Polar graphs, see the `page of Andries
    Brouwer's website <https://www.win.tue.nl/~aeb/graphs/srghub.html>`_.

    INPUT:

    - ``m``, ``q`` -- integers; `q` must be a prime power

    - ``algorithm`` -- string (default: ``'gap'``); if set to ``'gap'`` then the
      computation is carried via GAP library interface, computing totally
      singular subspaces, which is faster for large examples (especially with
      `q>2`). Otherwise it is done directly.

    EXAMPLES::

        sage: # needs sage.libs.gap
        sage: G = graphs.UnitaryPolarGraph(4,2); G
        Unitary Polar Graph U(4, 2); GQ(4, 2): Graph on 45 vertices
        sage: G.is_strongly_regular(parameters=True)
        (45, 12, 3, 3)
        sage: graphs.UnitaryPolarGraph(5,2).is_strongly_regular(parameters=True)
        (165, 36, 3, 9)
        sage: graphs.UnitaryPolarGraph(6,2)     # not tested (long time)
        Unitary Polar Graph U(6, 2): Graph on 693 vertices

    TESTS::

        sage: graphs.UnitaryPolarGraph(4,3, algorithm='gap').is_strongly_regular(parameters=True)   # needs sage.libs.gap
        (280, 36, 8, 4)
        sage: graphs.UnitaryPolarGraph(4,3).is_strongly_regular(parameters=True)                    # needs sage.libs.gap
        (280, 36, 8, 4)
        sage: graphs.UnitaryPolarGraph(4,3, algorithm='foo')
        Traceback (most recent call last):
        ...
        ValueError: unknown algorithm!
    """
def NonisotropicUnitaryPolarGraph(m, q):
    """
    Return the Graph `NU(m,q)`.

    This returns the graph on nonisotropic, with respect to a nondegenerate
    Hermitean form, points of the `(m-1)`-dimensional projective space over
    `F_q`, with points adjacent whenever they lie on a tangent (to the set of
    isotropic points) line.  For more information, see Sect. 9.9 of [BH2012]_
    and series C14 in [Hub1975]_.

    INPUT:

    - ``m``, ``q`` -- integers; `q` must be a prime power

    EXAMPLES::

        sage: g = graphs.NonisotropicUnitaryPolarGraph(5,2); g                          # needs sage.libs.gap
        NU(5, 2): Graph on 176 vertices
        sage: g.is_strongly_regular(parameters=True)                                    # needs sage.libs.gap
        (176, 135, 102, 108)

    TESTS::

        sage: graphs.NonisotropicUnitaryPolarGraph(4,2).is_strongly_regular(parameters=True)        # needs sage.libs.gap
        (40, 27, 18, 18)
        sage: graphs.NonisotropicUnitaryPolarGraph(4,3).is_strongly_regular(parameters=True)  # long time, needs sage.libs.gap
        (540, 224, 88, 96)
        sage: graphs.NonisotropicUnitaryPolarGraph(6,6)
        Traceback (most recent call last):
        ...
        ValueError: q must be a prime power
    """
def UnitaryDualPolarGraph(m, q):
    """
    Return the Dual Unitary Polar Graph `U(m,q)`.

    For more information on Unitary Dual Polar graphs, see [BCN1989]_ and
    Sect. 2.3.1 of [Coh1981]_.

    INPUT:

    - ``m``, ``q`` -- integers; `q` must be a prime power

    EXAMPLES:

    The point graph of a generalized quadrangle (see
    :wikipedia:`Generalized_quadrangle`, [PT2009]_) of order (8,4)::

        sage: G = graphs.UnitaryDualPolarGraph(5,2); G  # long time                     # needs sage.libs.gap
        Unitary Dual Polar Graph DU(5, 2); GQ(8, 4): Graph on 297 vertices
        sage: G.is_strongly_regular(parameters=True)    # long time                     # needs sage.libs.gap
        (297, 40, 7, 5)

    Another way to get the  generalized quadrangle of order (2,4)::

        sage: G = graphs.UnitaryDualPolarGraph(4,2); G                                  # needs sage.libs.gap
        Unitary Dual Polar Graph DU(4, 2); GQ(2, 4): Graph on 27 vertices
        sage: G.is_isomorphic(graphs.OrthogonalPolarGraph(6,2,'-'))                     # needs sage.libs.gap
        True

    A bigger graph::

        sage: G = graphs.UnitaryDualPolarGraph(6,2); G   # not tested (long time)
        Unitary Dual Polar Graph DU(6, 2): Graph on 891 vertices
        sage: G.is_distance_regular(parameters=True)     # not tested (long time)
        ([42, 40, 32, None], [None, 1, 5, 21])

    TESTS::

        sage: graphs.UnitaryDualPolarGraph(6,6)                                         # needs sage.libs.gap
        Traceback (most recent call last):
        ...
        GAPError: Error, <subfield> must be a prime or a finite field
    """
def SymplecticDualPolarGraph(m, q):
    """
    Return the Symplectic Dual Polar Graph `DSp(m,q)`.

    For more information on Symplectic Dual Polar graphs, see [BCN1989]_ and
    Sect. 2.3.1 of [Coh1981]_.

    INPUT:

    - ``m``, ``q`` -- integers; `q` must be a prime power, and `m` must be even

    EXAMPLES::

        sage: G = graphs.SymplecticDualPolarGraph(6,3); G       # not tested (long time)
        Symplectic Dual Polar Graph DSp(6, 3): Graph on 1120 vertices
        sage: G.is_distance_regular(parameters=True)            # not tested (long time)
        ([39, 36, 27, None], [None, 1, 4, 13])

    TESTS::

        sage: G = graphs.SymplecticDualPolarGraph(6,2); G                               # needs sage.libs.gap
        Symplectic Dual Polar Graph DSp(6, 2): Graph on 135 vertices
        sage: G.is_distance_regular(parameters=True)                                    # needs sage.libs.gap
        ([14, 12, 8, None], [None, 1, 3, 7])
        sage: graphs.SymplecticDualPolarGraph(6,6)                                      # needs sage.libs.gap
        Traceback (most recent call last):
        ...
        GAPError: Error, <subfield> must be a prime or a finite field
    """
def TaylorTwographDescendantSRG(q, clique_partition: bool = False):
    """
    Return the descendant graph of the Taylor's two-graph for `U_3(q)`, `q` odd.

    This is a strongly regular graph with parameters
    `(v,k,\\lambda,\\mu)=(q^3, (q^2+1)(q-1)/2, (q-1)^3/4-1, (q^2+1)(q-1)/4)`
    obtained as a two-graph descendant of the
    :func:`Taylor's two-graph <sage.combinat.designs.twographs.taylor_twograph>` `T`.
    This graph admits a partition into cliques of size `q`, which are useful in
    :func:`~sage.graphs.graph_generators.GraphGenerators.TaylorTwographSRG`,
    a strongly regular graph on `q^3+1` vertices in the
    Seidel switching class of `T`, for which we need `(q^2+1)/2` cliques.
    The cliques are the `q^2` lines on `v_0` of the projective plane containing
    the unital for `U_3(q)`, and intersecting the unital (i.e. the vertices of
    the graph and the point we remove) in `q+1` points. This is all taken from
    §7E of [BL1984]_.

    INPUT:

    - ``q`` -- a power of an odd prime number

    - ``clique_partition`` -- boolean (default: ``False``); when set to
      ``True``, return `q^2-1` cliques of size `q` with empty pairwise
      intersection. (Removing all of them leaves a clique, too), and the point
      removed from the unital.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: g = graphs.TaylorTwographDescendantSRG(3); g
        Taylor two-graph descendant SRG: Graph on 27 vertices
        sage: g.is_strongly_regular(parameters=True)
        (27, 10, 1, 5)
        sage: from sage.combinat.designs.twographs import taylor_twograph
        sage: T = taylor_twograph(3)                            # long time
        sage: g.is_isomorphic(T.descendant(T.ground_set()[1]))  # long time
        True
        sage: g = graphs.TaylorTwographDescendantSRG(5)         # not tested (long time)
        sage: g.is_strongly_regular(parameters=True)            # not tested (long time)
        (125, 52, 15, 26)

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: g,l,_ = graphs.TaylorTwographDescendantSRG(3, clique_partition=True)
        sage: all(g.is_clique(x) for x in l)
        True
        sage: graphs.TaylorTwographDescendantSRG(4)
        Traceback (most recent call last):
        ...
        ValueError: q must be an odd prime power
        sage: graphs.TaylorTwographDescendantSRG(6)
        Traceback (most recent call last):
        ...
        ValueError: q must be an odd prime power
    """
def TaylorTwographSRG(q):
    """
    Return a strongly regular graph from the Taylor's two-graph for `U_3(q)`,
    `q` odd

    This is a strongly regular graph with parameters
    `(v,k,\\lambda,\\mu)=(q^3+1, q(q^2+1)/2, (q^2+3)(q-1)/4, (q^2+1)(q+1)/4)`
    in the Seidel switching class of
    :func:`Taylor two-graph <sage.combinat.designs.twographs.taylor_twograph>`.
    Details are in §7E of [BL1984]_.

    INPUT:

    - ``q`` -- a power of an odd prime number

    .. SEEALSO::

        * :meth:`~sage.graphs.graph_generators.GraphGenerators.TaylorTwographDescendantSRG`

    EXAMPLES::

        sage: t = graphs.TaylorTwographSRG(3); t                                        # needs sage.rings.finite_rings
        Taylor two-graph SRG: Graph on 28 vertices
        sage: t.is_strongly_regular(parameters=True)                                    # needs sage.rings.finite_rings
        (28, 15, 6, 10)
    """
def AhrensSzekeresGeneralizedQuadrangleGraph(q, dual: bool = False):
    """
    Return the collinearity graph of the generalized quadrangle `AS(q)`, or of
    its dual

    Let `q` be an odd prime power.  `AS(q)` is a generalized quadrangle
    (:wikipedia:`Generalized_quadrangle`) of
    order `(q-1,q+1)`, see 3.1.5 in [PT2009]_. Its points are elements
    of `F_q^3`, and lines are sets of size `q` of the form

    * `\\{ (\\sigma, a, b) \\mid \\sigma\\in F_q \\}`
    * `\\{ (a, \\sigma, b) \\mid \\sigma\\in F_q \\}`
    * `\\{ (c \\sigma^2 - b \\sigma + a, -2 c \\sigma + b, \\sigma) \\mid \\sigma\\in F_q \\}`,

    where `a`, `b`, `c` are arbitrary elements of `F_q`.

    INPUT:

    - ``q`` -- a power of an odd prime number

    - ``dual`` -- boolean (default: ``False``); whether to return the
      collinearity graph of `AS(q)` or of the dual `AS(q)` (when ``True``)

    EXAMPLES::

        sage: g = graphs.AhrensSzekeresGeneralizedQuadrangleGraph(5); g
        AS(5); GQ(4, 6): Graph on 125 vertices
        sage: g.is_strongly_regular(parameters=True)
        (125, 28, 3, 7)
        sage: g = graphs.AhrensSzekeresGeneralizedQuadrangleGraph(5, dual=True); g
        AS(5)*; GQ(6, 4): Graph on 175 vertices
        sage: g.is_strongly_regular(parameters=True)
        (175, 30, 5, 5)
    """
def T2starGeneralizedQuadrangleGraph(q, dual: bool = False, hyperoval=None, field=None, check_hyperoval: bool = True):
    """
    Return the collinearity graph of the generalized quadrangle `T_2^*(q)`, or
    of its dual

    Let `q=2^k` and `\\Theta=PG(3,q)`.  `T_2^*(q)` is a generalized quadrangle
    (:wikipedia:`Generalized_quadrangle`)
    of order `(q-1,q+1)`, see 3.1.3 in [PT2009]_. Fix a plane `\\Pi \\subset
    \\Theta` and a
    `hyperoval <http://en.wikipedia.org/wiki/Oval_(projective_plane)#Even_q>`__
    `O \\subset \\Pi`. The points of `T_2^*(q):=T_2^*(O)` are the points of
    `\\Theta` outside `\\Pi`, and the lines are the lines of `\\Theta` outside
    `\\Pi` that meet `\\Pi` in a point of `O`.

    INPUT:

    - ``q`` -- a power of two

    - ``dual`` -- boolean (default: ``False``); whether to return the graph of
      `T_2^*(O)` or of the dual `T_2^*(O)` (when ``True``)

    - ``hyperoval`` -- a hyperoval (i.e. a complete 2-arc; a set of points in
      the plane meeting every line in 0 or 2 points) in the plane of points with
      0th coordinate 0 in `PG(3,q)` over the field ``field``. Each point of
      ``hyperoval`` must be a length 4 vector over ``field`` with 1st non-0
      coordinate equal to 1. By default, ``hyperoval`` and ``field`` are not
      specified, and constructed on the fly. In particular, ``hyperoval`` we
      build is the classical one, i.e. a conic with the point of intersection of
      its tangent lines.

    - ``field`` -- an instance of a finite field of order `q`, must be provided
      if ``hyperoval`` is provided

    - ``check_hyperoval`` -- boolean (default: ``True``); whether to check
      ``hyperoval`` for correctness or not

    EXAMPLES:

    using the built-in construction::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: g = graphs.T2starGeneralizedQuadrangleGraph(4); g
        T2*(O,4); GQ(3, 5): Graph on 64 vertices
        sage: g.is_strongly_regular(parameters=True)
        (64, 18, 2, 6)
        sage: g = graphs.T2starGeneralizedQuadrangleGraph(4, dual=True); g
        T2*(O,4)*; GQ(5, 3): Graph on 96 vertices
        sage: g.is_strongly_regular(parameters=True)
        (96, 20, 4, 4)

    supplying your own hyperoval::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: F = GF(4,'b')
        sage: O = [vector(F,(0,0,0,1)),vector(F,(0,0,1,0))] + [vector(F, (0,1,x^2,x))
        ....:                                                  for x in F]
        sage: g = graphs.T2starGeneralizedQuadrangleGraph(4, hyperoval=O, field=F); g
        T2*(O,4); GQ(3, 5): Graph on 64 vertices
        sage: g.is_strongly_regular(parameters=True)
        (64, 18, 2, 6)

    TESTS::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: F = GF(4,'b')  # repeating a point...
        sage: O = [vector(F,(0,1,0,0)),vector(F,(0,0,1,0))]+[vector(F, (0,1,x^2,x)) for x in F]
        sage: graphs.T2starGeneralizedQuadrangleGraph(4, hyperoval=O, field=F)
        Traceback (most recent call last):
        ...
        RuntimeError: incorrect hyperoval size
        sage: O = [vector(F,(0,1,1,0)),vector(F,(0,0,1,0))]+[vector(F, (0,1,x^2,x)) for x in F]
        sage: graphs.T2starGeneralizedQuadrangleGraph(4, hyperoval=O, field=F)
        Traceback (most recent call last):
        ...
        RuntimeError: incorrect hyperoval
    """
def HaemersGraph(q, hyperoval=None, hyperoval_matching=None, field=None, check_hyperoval: bool = True):
    """
    Return the Haemers graph obtained from `T_2^*(q)^*`.

    Let `q` be a power of 2. In Sect. 8.A of [BL1984]_ one finds a construction
    of a strongly regular graph with parameters `(q^2(q+2),q^2+q-1,q-2,q)` from
    the graph of `T_2^*(q)^*`, constructed by
    :func:`~sage.graphs.graph_generators.GraphGenerators.T2starGeneralizedQuadrangleGraph`,
    by redefining adjacencies in the way specified by an arbitrary
    ``hyperoval_matching`` of the points (i.e. partitioning into size two parts)
    of ``hyperoval`` defining `T_2^*(q)^*`.

    While [BL1984]_ gives the construction in geometric terms, it can be
    formulated, and is implemented, in graph-theoretic ones, of re-adjusting the
    edges. Namely, `G=T_2^*(q)^*` has a partition into `q+2` independent sets
    `I_k` of size `q^2` each. Each vertex in `I_j` is adjacent to `q` vertices
    from `I_k`. Each `I_k` is paired to some `I_{k'}`, according to
    ``hyperoval_matching``. One adds edges `(s,t)` for `s,t \\in I_k` whenever
    `s` and `t` are adjacent to some `u \\in I_{k'}`, and removes all the edges
    between `I_k` and `I_{k'}`.

    INPUT:

    - ``q`` -- a power of two

    - ``hyperoval_matching`` -- if ``None`` (default), pair each `i`-th point of
      ``hyperoval`` with `(i+1)`-th. Otherwise, specifies the pairing
      in the format `((i_1,i'_1),(i_2,i'_2),...)`.

    - ``hyperoval`` -- a hyperoval defining `T_2^*(q)^*`. If ``None`` (default),
      the classical hyperoval obtained from a conic is used. See the
      documentation of
      :func:`~sage.graphs.graph_generators.GraphGenerators.T2starGeneralizedQuadrangleGraph`,
      for more information.

    - ``field`` -- an instance of a finite field of order `q`, must be provided
      if ``hyperoval`` is provided

    - ``check_hyperoval`` -- boolean (default: ``True``); whether to check
      ``hyperoval`` for correctness or not

    EXAMPLES:

    using the built-in constructions::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: g = graphs.HaemersGraph(4); g
        Haemers(4): Graph on 96 vertices
        sage: g.is_strongly_regular(parameters=True)
        (96, 19, 2, 4)

    supplying your own hyperoval_matching::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: g = graphs.HaemersGraph(4, hyperoval_matching=((0,5),(1,4),(2,3))); g
        Haemers(4): Graph on 96 vertices
        sage: g.is_strongly_regular(parameters=True)
        (96, 19, 2, 4)

    TESTS::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: F = GF(4,'b')  # repeating a point...
        sage: O = [vector(F,(0,1,0,0)),vector(F,(0,0,1,0))]+[vector(F, (0,1,x^2,x)) for x in F]
        sage: graphs.HaemersGraph(4, hyperoval=O, field=F)
        Traceback (most recent call last):
        ...
        RuntimeError: incorrect hyperoval size
        sage: O = [vector(F,(0,1,1,0)),vector(F,(0,0,1,0))]+[vector(F, (0,1,x^2,x)) for x in F]
        sage: graphs.HaemersGraph(4, hyperoval=O, field=F)
        Traceback (most recent call last):
        ...
        RuntimeError: incorrect hyperoval

        sage: g = graphs.HaemersGraph(8); g             # not tested (long time)        # needs sage.rings.finite_rings
        Haemers(8): Graph on 640 vertices
        sage: g.is_strongly_regular(parameters=True)    # not tested (long time)        # needs sage.rings.finite_rings
        (640, 71, 6, 8)
    """
def CossidentePenttilaGraph(q):
    """
    Return the Cossidente-Penttila
    `((q^3+1)(q+1)/2,(q^2+1)(q-1)/2,(q-3)/2,(q-1)^2/2)`-strongly regular graph

    For each odd prime power `q`, one can partition the points of the
    `O_6^-(q)`-generalized quadrangle `GQ(q,q^2)` into two parts, so that on any
    of them the induced subgraph of the point graph of the GQ has parameters as
    above [CP2005]_.

    Directly following the construction in [CP2005]_ is not efficient, as one
    then needs to construct the dual `GQ(q^2,q)`. Thus we describe here a more
    efficient approach that we came up with, following a suggestion by
    T.Penttila. Namely, this partition is invariant under the subgroup
    `H=\\Omega_3(q^2)<O_6^-(q)`. We build the appropriate `H`, which leaves the
    form `B(X,Y,Z)=XY+Z^2` invariant, and pick up two orbits of `H` on the
    `F_q`-points. One them is `B`-isotropic, and we take the representative
    `(1:0:0)`. The other one corresponds to the points of `PG(2,q^2)` that have
    all the lines on them either missing the conic specified by `B`, or
    intersecting the conic in two points. We take `(1:1:e)` as the
    representative. It suffices to pick `e` so that `e^2+1` is not a square in
    `F_{q^2}`. Indeed, The conic can be viewed as the union of `\\{(0:1:0)\\}` and
    `\\{(1:-t^2:t) | t \\in F_{q^2}\\}`.  The coefficients of a generic line on
    `(1:1:e)` are `[1:-1-eb:b]`, for `-1\\neq eb`.  Thus, to make sure the
    intersection with the conic is always even, we need that the discriminant of
    `1+(1+eb)t^2+tb=0` never vanishes, and this is if and only if `e^2+1` is not
    a square. Further, we need to adjust `B`, by multiplying it by appropriately
    chosen `\\nu`, so that `(1:1:e)` becomes isotropic under the relative trace
    norm `\\nu B(X,Y,Z)+(\\nu B(X,Y,Z))^q`. The latter is used then to define the
    graph.

    INPUT:

    - ``q`` -- an odd prime power

    EXAMPLES:

    For `q=3` one gets Sims-Gewirtz graph. ::

        sage: G = graphs.CossidentePenttilaGraph(3)     # optional - gap_package_grape
        sage: G.is_strongly_regular(parameters=True)    # optional - gap_package_grape
        (56, 10, 0, 2)

    For `q>3` one gets new graphs. ::

        sage: G = graphs.CossidentePenttilaGraph(5)     # optional - gap_package_grape
        sage: G.is_strongly_regular(parameters=True)    # optional - gap_package_grape
        (378, 52, 1, 8)

    TESTS::

        sage: G = graphs.CossidentePenttilaGraph(7)     # optional - gap_package_grape, long time
        sage: G.is_strongly_regular(parameters=True)    # optional - gap_package_grape, long time
        (1376, 150, 2, 18)
        sage: graphs.CossidentePenttilaGraph(2)
        Traceback (most recent call last):
        ...
        ValueError: q(=2) must be an odd prime power
    """
def Nowhere0WordsTwoWeightCodeGraph(q, hyperoval=None, field=None, check_hyperoval: bool = True):
    """
    Return the subgraph of nowhere 0 words from two-weight code of projective
    plane hyperoval.

    Let `q=2^k` and `\\Pi=PG(2,q)`.  Fix a
    `hyperoval <http://en.wikipedia.org/wiki/Oval_(projective_plane)#Even_q>`__
    `O \\subset \\Pi`. Let `V=F_q^3` and `C` the two-weight 3-dimensional linear
    code over `F_q` with words `c(v)` obtained from `v\\in V` by computing

    .. MATH::

        c(v)=(\\langle v,o_1 \\rangle,...,\\langle v,o_{q+2} \\rangle), o_j \\in O.

    `C` contains `q(q-1)^2/2` words without 0 entries. The subgraph of the
    strongly regular graph of `C` induced on the latter words is also strongly
    regular, assuming `q>4`. This is a construction due to A.E.Brouwer
    [Bro2016]_, and leads to graphs with parameters also given by a construction
    in [HHL2009]_.  According to [Bro2016]_, these two constructions are likely
    to produce isomorphic graphs.

    INPUT:

    - ``q`` -- a power of two

    - ``hyperoval`` -- a hyperoval (i.e. a complete 2-arc; a set of points in
      the plane meeting every line in 0 or 2 points) in `PG(2,q)` over the field
      ``field``.  Each point of ``hyperoval`` must be a length 3 vector over
      ``field`` with 1st non-0 coordinate equal to 1. By default, ``hyperoval``
      and ``field`` are not specified, and constructed on the fly. In
      particular, ``hyperoval`` we build is the classical one, i.e. a conic with
      the point of intersection of its tangent lines.

    - ``field`` -- an instance of a finite field of order `q`; must be provided
      if ``hyperoval`` is provided

    - ``check_hyperoval`` -- boolean (default: ``True``); whether to check
      ``hyperoval`` for correctness or not

    .. SEEALSO::

        - :func:`~sage.graphs.strongly_regular_db.is_nowhere0_twoweight`

    EXAMPLES:

    using the built-in construction::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: g = graphs.Nowhere0WordsTwoWeightCodeGraph(8); g
        Nowhere0WordsTwoWeightCodeGraph(8): Graph on 196 vertices
        sage: g.is_strongly_regular(parameters=True)
        (196, 60, 14, 20)
        sage: g = graphs.Nowhere0WordsTwoWeightCodeGraph(16)  # not tested (long time)
        sage: g.is_strongly_regular(parameters=True)          # not tested (long time)
        (1800, 728, 268, 312)

    supplying your own hyperoval::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: F = GF(8)
        sage: O = [vector(F,(0,0,1)),vector(F,(0,1,0))] + [vector(F, (1,x^2,x))
        ....:                                              for x in F]
        sage: g = graphs.Nowhere0WordsTwoWeightCodeGraph(8,hyperoval=O,field=F); g
        Nowhere0WordsTwoWeightCodeGraph(8): Graph on 196 vertices
        sage: g.is_strongly_regular(parameters=True)
        (196, 60, 14, 20)

    TESTS::

        sage: # needs sage.combinat sage.rings.finite_rings
        sage: F = GF(8)  # repeating a point...
        sage: O = [vector(F,(1,0,0)),vector(F,(0,1,0))]+[vector(F, (1,x^2,x)) for x in F]
        sage: graphs.Nowhere0WordsTwoWeightCodeGraph(8,hyperoval=O,field=F)
        Traceback (most recent call last):
        ...
        RuntimeError: incorrect hyperoval size
        sage: O = [vector(F,(1,1,0)),vector(F,(0,1,0))]+[vector(F, (1,x^2,x)) for x in F]
        sage: graphs.Nowhere0WordsTwoWeightCodeGraph(8,hyperoval=O,field=F)
        Traceback (most recent call last):
        ...
        RuntimeError: incorrect hyperoval
    """
def OrthogonalDualPolarGraph(e, d, q):
    """
    Return the dual polar graph on `GO^e(n,q)` of diameter `d`.

    The value of `n` is determined by `d` and `e`.

    The graph is distance-regular with classical parameters `(d, q, 0, q^e)`.

    INPUT:

    - ``e`` -- integer; type of the orthogonal polar space to consider;
      must be `-1, 0` or  `1`

    - ``d`` -- integer; diameter of the graph

    - ``q`` -- integer; prime power; order of the finite field over which to
      build the polar space

    EXAMPLES::

        sage: # needs sage.libs.gap
        sage: G = graphs.OrthogonalDualPolarGraph(1,3,2)
        sage: G.is_distance_regular(True)
        ([7, 6, 4, None], [None, 1, 3, 7])
        sage: G = graphs.OrthogonalDualPolarGraph(0,3,3)        # long time
        sage: G.is_distance_regular(True)                       # long time
        ([39, 36, 27, None], [None, 1, 4, 13])
        sage: G.order()                                         # long time
        1120

    REFERENCES:

    See [BCN1989]_ pp. 274-279 or [VDKT2016]_ p. 22.

    TESTS::

        sage: # needs sage.libs.gap
        sage: G = graphs.OrthogonalDualPolarGraph(0,3,2)
        sage: G.is_distance_regular(True)
        ([14, 12, 8, None], [None, 1, 3, 7])
        sage: G = graphs.OrthogonalDualPolarGraph(-1,3,2)       # long time
        sage: G.is_distance_regular(True)                       # long time
        ([28, 24, 16, None], [None, 1, 3, 7])
        sage: G = graphs.OrthogonalDualPolarGraph(1,3,4)
        sage: G.is_distance_regular(True)
        ([21, 20, 16, None], [None, 1, 5, 21])
        sage: G = graphs.OrthogonalDualPolarGraph(1,4,2)
        sage: G.is_distance_regular(True)
        ([15, 14, 12, 8, None], [None, 1, 3, 7, 15])
    """
