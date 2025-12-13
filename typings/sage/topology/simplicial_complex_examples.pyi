from .simplicial_complex import SimplicialComplex as SimplicialComplex
from sage.combinat.subset import Subsets as Subsets
from sage.misc.functional import is_even as is_even
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.sets.set import Set as Set
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def facets_for_RP4():
    """
    Return the list of facets for a minimal triangulation of 4-dimensional
    real projective space.

    We use vertices numbered 1 through 16, define two facets, and define
    a certain subgroup `G` of the symmetric group `S_{16}`. Then the set
    of all facets is the `G`-orbit of the two given facets.

    See the description in Example 3.12 in Datta [Dat2007]_.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex_examples import facets_for_RP4
        sage: A = facets_for_RP4()   # long time (1 or 2 seconds)
        sage: SimplicialComplex(A) == simplicial_complexes.RealProjectiveSpace(4) # long time
        True
    """
def facets_for_K3():
    """
    Return the facets for a minimal triangulation of the K3 surface.

    This is a pure simplicial complex of dimension 4 with 16
    vertices and 288 facets. The facets are obtained by constructing a
    few facets and a permutation group `G`, and then computing the
    `G`-orbit of those facets.

    See Casella and Kühnel in [CK2001]_ and Spreer and Kühnel [SK2011]_;
    the construction here uses the labeling from Spreer and Kühnel.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex_examples import facets_for_K3
        sage: A = facets_for_K3()   # long time (a few seconds)
        sage: SimplicialComplex(A) == simplicial_complexes.K3Surface()  # long time
        True
    """
def matching(A, B):
    """
    List of maximal matchings between the sets ``A`` and ``B``.

    A matching is a set of pairs `(a, b) \\in A \\times B` where each `a` and
    `b` appears in at most one pair.  A maximal matching is one which is
    maximal with respect to inclusion of subsets of `A \\times B`.

    INPUT:

    - ``A``, ``B`` -- list, tuple, or indeed anything which can be
      converted to a set

    EXAMPLES::

        sage: from sage.topology.simplicial_complex_examples import matching
        sage: matching([1, 2], [3, 4])
        [{(1, 3), (2, 4)}, {(1, 4), (2, 3)}]
        sage: matching([0, 2], [0])
        [{(0, 0)}, {(2, 0)}]
    """

class UniqueSimplicialComplex(SimplicialComplex, UniqueRepresentation):
    """
    This combines :class:`SimplicialComplex` and
    :class:`UniqueRepresentation`. It is intended to be used to make
    standard examples of simplicial complexes unique. See :issue:`13566`.

    INPUT:

    - the inputs are the same as for a :class:`SimplicialComplex`,
      with one addition and two exceptions. The exceptions are that
      ``is_mutable`` and ``is_immutable`` are ignored: all instances
      of this class are immutable. The addition:

    - ``name`` -- string (optional); the string representation for this complex

    EXAMPLES::

        sage: from sage.topology.simplicial_complex_examples import UniqueSimplicialComplex
        sage: SimplicialComplex([[0, 1]]) is SimplicialComplex([[0, 1]])
        False
        sage: UniqueSimplicialComplex([[0, 1]]) is UniqueSimplicialComplex([[0, 1]])
        True
        sage: UniqueSimplicialComplex([[0, 1]])
        Simplicial complex with vertex set (0, 1) and facets {(0, 1)}
        sage: UniqueSimplicialComplex([[0, 1]], name='The 1-simplex')
        The 1-simplex
    """
    @staticmethod
    def __classcall__(self, maximal_faces=None, name=None, **kwds):
        """
        TESTS::

            sage: from sage.topology.simplicial_complex_examples import UniqueSimplicialComplex
            sage: UniqueSimplicialComplex([[1, 2, 3], [0, 1, 3]]) is UniqueSimplicialComplex([(1, 2, 3), (0, 1, 3)])
            True
            sage: X = UniqueSimplicialComplex([[1, 2, 3], [0, 1, 3]])
            sage: X is UniqueSimplicialComplex(X)
            True

        Testing ``from_characteristic_function``::

            sage: UniqueSimplicialComplex(from_characteristic_function=(lambda x: sum(x) <= 4, range(5)))
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and facets {(0, 4), (0, 1, 2), (0, 1, 3)}
        """
    def __init__(self, maximal_faces=None, name=None, **kwds) -> None:
        """
        TESTS::

            sage: from sage.topology.simplicial_complex_examples import UniqueSimplicialComplex
            sage: UniqueSimplicialComplex([[1, 2, 3], [0, 1, 3]], is_mutable=True).is_mutable()
            False
        """

def Sphere(n):
    """
    A minimal triangulation of the `n`-dimensional sphere.

    INPUT:

    - ``n`` -- positive integer

    EXAMPLES::

        sage: simplicial_complexes.Sphere(2)
        Minimal triangulation of the 2-sphere
        sage: simplicial_complexes.Sphere(5).homology()                                 # needs sage.modules
        {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: Z}
        sage: [simplicial_complexes.Sphere(n).euler_characteristic() for n in range(6)]
        [2, 0, 2, 0, 2, 0]
        sage: [simplicial_complexes.Sphere(n).f_vector() for n in range(6)]
        [[1, 2],
         [1, 3, 3],
         [1, 4, 6, 4],
         [1, 5, 10, 10, 5],
         [1, 6, 15, 20, 15, 6],
         [1, 7, 21, 35, 35, 21, 7]]
    """
def Simplex(n):
    """
    An `n`-dimensional simplex, as a simplicial complex.

    INPUT:

    - ``n`` -- nonnegative integer

    OUTPUT: the simplicial complex consisting of the `n`-simplex
    on vertices `(0, 1, ..., n)` and all of its faces.

    EXAMPLES::

        sage: simplicial_complexes.Simplex(3)
        The 3-simplex
        sage: simplicial_complexes.Simplex(5).euler_characteristic()
        1
    """
def Torus():
    """
    A minimal triangulation of the torus.

    This is a simplicial complex with 7 vertices, 21 edges and 14
    faces. It is the unique triangulation of the torus with 7
    vertices, and has been found by Möbius in 1861.

    This is also the combinatorial structure of the Császár
    polyhedron (see :wikipedia:`Császár_polyhedron`).

    EXAMPLES::

        sage: T = simplicial_complexes.Torus()
        sage: T.homology(1)                                                             # needs sage.modules
        Z x Z
        sage: T.f_vector()
        [1, 7, 21, 14]

    TESTS::

        sage: T.flip_graph().is_isomorphic(graphs.HeawoodGraph())
        True

    REFERENCES:

    - [Lut2002]_
    """
def RealProjectivePlane():
    """
    A minimal triangulation of the real projective plane.

    EXAMPLES::

        sage: P = simplicial_complexes.RealProjectivePlane()
        sage: Q = simplicial_complexes.ProjectivePlane()
        sage: P == Q
        True

        sage: # needs sage.modules
        sage: P.cohomology(1)
        0
        sage: P.cohomology(2)
        C2
        sage: P.cohomology(1, base_ring=GF(2))
        Vector space of dimension 1 over Finite Field of size 2
        sage: P.cohomology(2, base_ring=GF(2))
        Vector space of dimension 1 over Finite Field of size 2
    """
ProjectivePlane = RealProjectivePlane

def KleinBottle():
    """
    A minimal triangulation of the Klein bottle, as presented for example
    in Davide Cervone's thesis [Cer1994]_.

    EXAMPLES::

        sage: simplicial_complexes.KleinBottle()
        Minimal triangulation of the Klein bottle
    """
def SurfaceOfGenus(g, orientable: bool = True):
    """
    A surface of genus `g`.

    INPUT:

    - ``g`` -- nonnegative integer; the desired genus

    - ``orientable`` -- boolean (default: ``True``); if
      ``True``, return an orientable surface, and if ``False``,
      return a non-orientable surface.

    In the orientable case, return a sphere if `g` is zero, and
    otherwise return a `g`-fold connected sum of a torus with itself.

    In the non-orientable case, raise an error if `g` is zero.  If
    `g` is positive, return a `g`-fold connected sum of a
    real projective plane with itself.

    EXAMPLES::

        sage: simplicial_complexes.SurfaceOfGenus(2)
        Triangulation of an orientable surface of genus 2
        sage: simplicial_complexes.SurfaceOfGenus(1, orientable=False)
        Triangulation of a non-orientable surface of genus 1
    """
def MooreSpace(q):
    """
    Triangulation of the mod `q` Moore space.

    INPUT:

    - ``q`` -- integer; at least 2

    This is a simplicial complex with simplices of dimension 0, 1,
    and 2, such that its reduced homology is isomorphic to
    `\\\\ZZ/q\\\\ZZ` in dimension 1, zero otherwise.

    If `q=2`, this is the real projective plane.  If `q>2`, then
    construct it as follows: start with a triangle with vertices
    1, 2, 3.  We take a `3q`-gon forming a `q`-fold cover of the
    triangle, and we form the resulting complex as an
    identification space of the `3q`-gon.  To triangulate this
    identification space, put `q` vertices `A_0`, ..., `A_{q-1}`,
    in the interior, each of which is connected to 1, 2, 3 (two
    facets each: `[1, 2, A_i]`, `[2, 3, A_i]`).  Put `q` more
    vertices in the interior: `B_0`, ..., `B_{q-1}`, with facets
    `[3, 1, B_i]`, `[3, B_i, A_i]`, `[1, B_i, A_{i+1}]`, `[B_i,
    A_i, A_{i+1}]`.  Then triangulate the interior polygon with
    vertices `A_0`, `A_1`, ..., `A_{q-1}`.

    EXAMPLES::

        sage: simplicial_complexes.MooreSpace(2)
        Minimal triangulation of the real projective plane
        sage: simplicial_complexes.MooreSpace(3).homology()[1]                          # needs sage.modules
        C3
        sage: simplicial_complexes.MooreSpace(4).suspension().homology()[2]             # needs sage.modules
        C4
        sage: simplicial_complexes.MooreSpace(8)
        Triangulation of the mod 8 Moore space
    """
def ComplexProjectivePlane():
    """
    A minimal triangulation of the complex projective plane.

    This was constructed by Kühnel and Banchoff [KB1983]_.

    EXAMPLES::

        sage: C = simplicial_complexes.ComplexProjectivePlane()
        sage: C.f_vector()
        [1, 9, 36, 84, 90, 36]
        sage: C.homology(2)                                                             # needs sage.modules
        Z
        sage: C.homology(4)                                                             # needs sage.modules
        Z
    """
def QuaternionicProjectivePlane():
    """
    Return a pure simplicial complex of dimension 8 with 490 facets.

    .. WARNING::

        This was proven to be a triangulation of the projective plane
        `HP^2` over the ring of quaternions by Gorodkov in 2016 [Gor2016]_.

    This simplicial complex has the same homology as `HP^2`. Its
    automorphism group is isomorphic to the alternating group `A_5`
    and acts transitively on vertices.

    This is defined here using the description in [BK1992]_. This
    article deals with three different triangulations. This procedure
    returns the only one which has a transitive group of automorphisms.

    EXAMPLES::

        sage: HP2 = simplicial_complexes.QuaternionicProjectivePlane(); HP2             # needs sage.groups
        Simplicial complex with 15 vertices and 490 facets
        sage: HP2.f_vector()                                                            # needs sage.groups
        [1, 15, 105, 455, 1365, 3003, 4515, 4230, 2205, 490]

    Checking its automorphism group::

        sage: HP2.automorphism_group().is_isomorphic(AlternatingGroup(5))               # needs sage.groups
        True
    """
def PoincareHomologyThreeSphere():
    """
    A triangulation of the Poincaré homology 3-sphere.

    This is a manifold whose integral homology is identical to the
    ordinary 3-sphere, but it is not simply connected. In particular,
    its fundamental group is the binary icosahedral group, which has
    order 120. The triangulation given here has 16 vertices and is
    due to Björner and Lutz [BL2000]_.

    EXAMPLES::

        sage: S3 = simplicial_complexes.Sphere(3)
        sage: Sigma3 = simplicial_complexes.PoincareHomologyThreeSphere()
        sage: S3.homology() == Sigma3.homology()                                        # needs sage.modules
        True
        sage: Sigma3.fundamental_group().cardinality()  # long time                     # needs sage.groups
        120
    """
def RealProjectiveSpace(n):
    """
    A triangulation of `\\Bold{R}P^n` for any `n \\geq 0`.

    INPUT:

    - ``n`` -- integer; the dimension of the real projective space
      to construct

    The first few cases are pretty trivial:

    - `\\Bold{R}P^0` is a point.

    - `\\Bold{R}P^1` is a circle, triangulated as the boundary of a
      single 2-simplex.

    - `\\Bold{R}P^2` is the real projective plane, here given its
      minimal triangulation with 6 vertices, 15 edges, and 10
      triangles.

    - `\\Bold{R}P^3`: any triangulation has at least 11 vertices by
      a result of Walkup [Wal1970]_; this function returns a
      triangulation with 11 vertices, as given by Lutz [Lut2005]_.

    - `\\Bold{R}P^4`: any triangulation has at least 16 vertices by
      a result of Walkup; this function returns a triangulation
      with 16 vertices as given by Lutz; see also Datta [Dat2007]_,
      Example 3.12.

    - `\\Bold{R}P^n`: Lutz has found a triangulation of
      `\\Bold{R}P^5` with 24 vertices, but it does not seem to have
      been published.  Kühnel [Kuh1987]_ has described a triangulation of
      `\\Bold{R}P^n`, in general, with `2^{n+1}-1` vertices; see
      also Datta, Example 3.21.  This triangulation is presumably
      not minimal, but it seems to be the best in the published
      literature as of this writing.  So this function returns it
      when `n > 4`.

    ALGORITHM: For `n < 4`, these are constructed explicitly by
    listing the facets.  For `n = 4`, this is constructed by
    specifying 16 vertices, two facets, and a certain subgroup `G`
    of the symmetric group `S_{16}`.  Then the set of all facets
    is the `G`-orbit of the two given facets.  This is implemented
    here by explicitly listing all of the facets; the facets
    can be computed by the function :func:`~sage.homology.simplicial_complex.facets_for_RP4`, but
    running the function takes a few seconds.

    For `n > 4`, the construction is as follows: let `S` denote
    the simplicial complex structure on the `n`-sphere given by
    the first barycentric subdivision of the boundary of an
    `(n+1)`-simplex.  This has a simplicial antipodal action: if
    `V` denotes the vertices in the boundary of the simplex, then
    the vertices in its barycentric subdivision `S` correspond to
    nonempty proper subsets `U` of `V`, and the antipodal action
    sends any subset `U` to its complement.  One can show that
    modding out by this action results in a triangulation for
    `\\Bold{R}P^n`.  To find the facets in this triangulation, find
    the facets in `S`.  These are identified in pairs to form
    `\\Bold{R}P^n`, so choose a representative from each pair: for
    each facet in `S`, replace any vertex in `S` containing 0 with
    its complement.

    Of course these complexes increase in size pretty quickly as
    `n` increases.

    EXAMPLES::

        sage: P3 = simplicial_complexes.RealProjectiveSpace(3)
        sage: P3.f_vector()
        [1, 11, 51, 80, 40]
        sage: P3.homology()                                                             # needs sage.modules
        {0: 0, 1: C2, 2: 0, 3: Z}
        sage: P4 = simplicial_complexes.RealProjectiveSpace(4)
        sage: P4.f_vector()
        [1, 16, 120, 330, 375, 150]
        sage: P4.homology() # long time
        {0: 0, 1: C2, 2: 0, 3: C2, 4: 0}
        sage: P5 = simplicial_complexes.RealProjectiveSpace(5)  # long time (44s on sage.math, 2012)
        sage: P5.f_vector()  # long time
        [1, 63, 903, 4200, 8400, 7560, 2520]

    The following computation can take a long time -- over half an
    hour. ::

        sage: P5.homology()  # not tested
        {0: 0, 1: C2, 2: 0, 3: C2, 4: 0, 5: Z}
        sage: simplicial_complexes.RealProjectiveSpace(2).dimension()
        2
        sage: P3.dimension()
        3
        sage: P4.dimension() # long time
        4
        sage: P5.dimension() # long time
        5
    """
def K3Surface():
    """
    Return a minimal triangulation of the K3 surface.

    This is a pure simplicial complex of dimension 4 with 16 vertices
    and 288 facets. It was constructed by Casella and Kühnel
    in [CK2001]_. The construction here uses the labeling from
    Spreer and Kühnel [SK2011]_.

    EXAMPLES::

        sage: K3 = simplicial_complexes.K3Surface(); K3
        Minimal triangulation of the K3 surface
        sage: K3.f_vector()
        [1, 16, 120, 560, 720, 288]

    This simplicial complex is implemented just by listing all 288
    facets. The list of facets can be computed by the function
    :func:`~sage.homology.simplicial_complex.facets_for_K3`, but running the function takes a few
    seconds.
    """
def BarnetteSphere():
    """
    Return Barnette's triangulation of the 3-sphere.

    This is a pure simplicial complex of dimension 3 with 8
    vertices and 19 facets, which is a non-polytopal triangulation
    of the 3-sphere. It was constructed by Barnette in
    [Bar1970]_. The construction here uses the labeling from De
    Loera, Rambau and Santos [DLRS2010]_. Another reference is chapter
    III.4 of Ewald [Ewa1996]_.

    EXAMPLES::

        sage: BS = simplicial_complexes.BarnetteSphere(); BS
        Barnette's triangulation of the 3-sphere
        sage: BS.f_vector()
        [1, 8, 27, 38, 19]

    TESTS:

    Checks that this is indeed the same Barnette Sphere as the one
    given on page 87 of [Ewa1996]_.::

        sage: BS2 = SimplicialComplex([[1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 5, 6],
        ....:                          [1, 2, 4, 7], [1, 3, 4, 7], [3, 4, 6, 7],
        ....:                          [3, 5, 6, 7], [1, 2, 5, 7], [2, 5, 6, 7],
        ....:                          [2, 4, 6, 7], [1, 2, 3, 8], [2, 3, 4, 8],
        ....:                          [3, 4, 5, 8], [4, 5, 6, 8], [1, 2, 6, 8],
        ....:                          [1, 5, 6, 8], [1, 3, 5, 8], [2, 4, 6, 8],
        ....:                          [1, 3, 5, 7]])
        sage: BS.is_isomorphic(BS2)
        True
    """
def BrucknerGrunbaumSphere():
    """
    Return Bruckner and Grunbaum's triangulation of the 3-sphere.

    This is a pure simplicial complex of dimension 3 with 8
    vertices and 20 facets, which is a non-polytopal triangulation
    of the 3-sphere. It appeared first in [Br1910]_ and was studied in
    [GrS1967]_.

    It is defined here as the link of any vertex in the unique minimal
    triangulation of the complex projective plane, see chapter 4 of
    [Kuh1995]_.

    EXAMPLES::

        sage: BGS = simplicial_complexes.BrucknerGrunbaumSphere(); BGS
        Bruckner and Grunbaum's triangulation of the 3-sphere
        sage: BGS.f_vector()
        [1, 8, 28, 40, 20]
    """
def NotIConnectedGraphs(n, i):
    """
    The simplicial complex of all graphs on `n` vertices which are
    not `i`-connected.

    Fix an integer `n>0` and consider the set of graphs on `n`
    vertices.  View each graph as its set of edges, so it is a
    subset of a set of size `n` choose 2.  A graph is
    `i`-connected if, for any `j<i`, if any `j` vertices are
    removed along with the edges emanating from them, then the
    graph remains connected.  Now fix `i`: it is clear that if `G`
    is not `i`-connected, then the same is true for any graph
    obtained from `G` by deleting edges. Thus the set of all
    graphs which are not `i`-connected, viewed as a set of subsets
    of the `n` choose 2 possible edges, is closed under taking
    subsets, and thus forms a simplicial complex.  This function
    produces that simplicial complex.

    INPUT:

    - ``n``, ``i`` -- nonnegative integers with `i` at most `n`

    See Dumas et al. [DHSW2003]_ for information on computing its homology
    by computer, and see Babson et al. [BBLSW1999]_ for theory.  For
    example, Babson et al. show that when `i=2`, the reduced homology of
    this complex is nonzero only in dimension `2n-5`, where it is
    free abelian of rank `(n-2)!`.

    EXAMPLES::

        sage: NICG52 = simplicial_complexes.NotIConnectedGraphs(5, 2)
        sage: NICG52.f_vector()
        [1, 10, 45, 120, 210, 240, 140, 20]
        sage: NICG52.homology(5).ngens()                                                # needs sage.modules
        6
    """
def MatchingComplex(n):
    """
    The matching complex of graphs on `n` vertices.

    Fix an integer `n>0` and consider a set `V` of `n` vertices.
    A 'partial matching' on `V` is a graph formed by edges so that
    each vertex is in at most one edge.  If `G` is a partial
    matching, then so is any graph obtained by deleting edges from
    `G`.  Thus the set of all partial matchings on `n` vertices,
    viewed as a set of subsets of the `n` choose 2 possible edges,
    is closed under taking subsets, and thus forms a simplicial
    complex called the 'matching complex'.  This function produces
    that simplicial complex.

    INPUT:

    - ``n`` -- positive integer

    See Dumas et al. [DHSW2003]_ for information on computing its homology
    by computer, and see Wachs [Wac2003]_ for an expository article about
    the theory.  For example, the homology of these complexes seems to
    have only mod 3 torsion, and this has been proved for the
    bottom non-vanishing homology group for the matching complex `M_n`.

    EXAMPLES::

        sage: M = simplicial_complexes.MatchingComplex(7)
        sage: H = M.homology(); H                                                       # needs sage.modules
        {0: 0, 1: C3, 2: Z^20}
        sage: H[2].ngens()                                                              # needs sage.modules
        20
        sage: M8 = simplicial_complexes.MatchingComplex(8)
        sage: M8.homology(2)                    # long time (6s on sage.math, 2012), needs sage.modules
        Z^132
    """
def ChessboardComplex(n, i):
    """
    The chessboard complex for an `n \\times i` chessboard.

    Fix integers `n, i > 0` and consider sets `V` of `n` vertices
    and `W` of `i` vertices.  A 'partial matching' between `V` and
    `W` is a graph formed by edges `(v, w)` with `v \\in V` and `w
    \\in W` so that each vertex is in at most one edge.  If `G` is
    a partial matching, then so is any graph obtained by deleting
    edges from `G`.  Thus the set of all partial matchings on `V`
    and `W`, viewed as a set of subsets of the `n+i` choose 2
    possible edges, is closed under taking subsets, and thus forms
    a simplicial complex called the 'chessboard complex'.  This
    function produces that simplicial complex.  (It is called the
    chessboard complex because such graphs also correspond to ways
    of placing rooks on an `n` by `i` chessboard so that none of
    them are attacking each other.)

    INPUT:

    - ``n``, ``i`` -- positive integers

    See Dumas et al. [DHSW2003]_ for information on computing its homology
    by computer, and see Wachs [Wac2003]_ for an expository article about
    the theory.

    EXAMPLES::

        sage: C = simplicial_complexes.ChessboardComplex(5, 5)
        sage: C.f_vector()
        [1, 25, 200, 600, 600, 120]
        sage: simplicial_complexes.ChessboardComplex(3, 3).homology()                   # needs sage.modules
        {0: 0, 1: Z x Z x Z x Z, 2: 0}
    """
def RandomComplex(n, d, p: float = 0.5):
    """
    A random `d`-dimensional simplicial complex on `n` vertices.

    INPUT:

    - ``n`` -- number of vertices

    - ``d`` -- dimension of the complex

    - ``p`` -- floating point number between 0 and 1 (default: 0.5)

    A random `d`-dimensional simplicial complex on `n` vertices,
    as defined for example by Meshulam and Wallach [MW2009]_, is
    constructed as follows: take `n` vertices and include all of
    the simplices of dimension strictly less than `d`, and then for each
    possible simplex of dimension `d`, include it with probability `p`.

    EXAMPLES::

        sage: X = simplicial_complexes.RandomComplex(6, 2); X
        Random 2-dimensional simplicial complex on 6 vertices
        sage: len(list(X.vertices()))
        6

    If `d` is too large (if `d+1 > n`, so that there are no
    `d`-dimensional simplices), then return the simplicial complex
    with a single `(n+1)`-dimensional simplex::

        sage: simplicial_complexes.RandomComplex(6, 12)
        The 5-simplex
    """
def SumComplex(n, A):
    """
    The sum complexes of Linial, Meshulam, and Rosenthal [LMR2010]_.

    If `k+1` is the cardinality of `A`, then this returns a
    `k`-dimensional simplicial complex `X_A` with vertices
    `\\ZZ/(n)`, and facets given by all `k+1`-tuples `(x_0, x_1,
    ..., x_k)` such that the sum `\\sum x_i` is in `A`. See the
    paper by Linial, Meshulam, and Rosenthal [LMR2010]_, in which
    they prove various results about these complexes; for example,
    if `n` is prime, then `X_A` is rationally acyclic, and if in
    addition `A` forms an arithmetic progression in `\\ZZ/(n)`,
    then `X_A` is `\\ZZ`-acyclic. Throughout their paper, they
    assume that `n` and `k` are relatively prime, but the
    construction makes sense in general.

    In addition to the results from the cited paper, these
    complexes can have large torsion, given the number of
    vertices; for example, if `n=10`, and `A=\\{0, 1, 2, 3, 6\\}`, then
    `H_3(X_A)` is cyclic of order 2728, and there is a
    4-dimensional complex on 13 vertices with `H_3` having a
    cyclic summand of order

    .. MATH::

        706565607945 = 3 \\cdot 5 \\cdot 53 \\cdot 79 \\cdot 131
        \\cdot 157 \\cdot 547.

    See the examples.

    INPUT:

    - ``n`` -- positive integer

    - ``A`` -- a subset of `\\ZZ/(n)`

    EXAMPLES::

        sage: S = simplicial_complexes.SumComplex(10, [0, 1, 2, 3, 6]); S
        Sum complex on vertices Z/10Z associated to {0, 1, 2, 3, 6}
        sage: S.homology()                                                              # needs sage.modules
        {0: 0, 1: 0, 2: 0, 3: C2728, 4: 0}
        sage: factor(2728)
        2^3 * 11 * 31

        sage: S = simplicial_complexes.SumComplex(11, [0, 1, 3]); S
        Sum complex on vertices Z/11Z associated to {0, 1, 3}
        sage: S.homology(1)                                                             # needs sage.modules
        C23
        sage: S = simplicial_complexes.SumComplex(11, [0, 1, 2, 3, 4, 7]); S
        Sum complex on vertices Z/11Z associated to {0, 1, 2, 3, 4, 7}
        sage: S.homology()                      # long time                             # needs sage.modules
        {0: 0, 1: 0, 2: 0, 3: 0, 4: C645679, 5: 0}
        sage: factor(645679)
        23 * 67 * 419

        sage: S = simplicial_complexes.SumComplex(13, [0, 1, 3]); S
        Sum complex on vertices Z/13Z associated to {0, 1, 3}
        sage: S.homology(1)                                                             # needs sage.modules
        C159
        sage: factor(159)
        3 * 53
        sage: S = simplicial_complexes.SumComplex(13, [0, 1, 2, 5]); S
        Sum complex on vertices Z/13Z associated to {0, 1, 2, 5}
        sage: S.homology()                      # long time                             # needs sage.modules
        {0: 0, 1: 0, 2: C146989209, 3: 0}
        sage: factor(1648910295)
        3^2 * 5 * 53 * 521 * 1327
        sage: S = simplicial_complexes.SumComplex(13, [0, 1, 2, 3, 5]); S
        Sum complex on vertices Z/13Z associated to {0, 1, 2, 3, 5}
        sage: S.homology()                      # long time                             # needs sage.modules
        {0: 0, 1: 0, 2: 0, 3: C3 x C237 x C706565607945, 4: 0}
        sage: factor(706565607945)                                                      # needs sage.libs.pari
        3 * 5 * 53 * 79 * 131 * 157 * 547

        sage: S = simplicial_complexes.SumComplex(17, [0, 1, 4]); S
        Sum complex on vertices Z/17Z associated to {0, 1, 4}
        sage: S.homology(1)                                                             # needs sage.modules
        C140183
        sage: factor(140183)
        103 * 1361
        sage: S = simplicial_complexes.SumComplex(19, [0, 1, 4]); S
        Sum complex on vertices Z/19Z associated to {0, 1, 4}
        sage: S.homology(1)                                                             # needs sage.modules
        C5670599
        sage: factor(5670599)
        11 * 191 * 2699
        sage: S = simplicial_complexes.SumComplex(31, [0, 1, 4]); S
        Sum complex on vertices Z/31Z associated to {0, 1, 4}
        sage: S.homology(1)                     # long time                             # needs sage.modules
        C5 x C5 x C5 x C5 x C26951480558170926865
        sage: factor(26951480558170926865)                                              # needs sage.libs.pari
        5 * 311 * 683 * 1117 * 11657 * 1948909
    """
def RandomTwoSphere(n):
    """
    Return a random triangulation of the 2-dimensional sphere with `n`
    vertices.

    INPUT:

    - ``n`` -- integer

    OUTPUT:

    A random triangulation of the sphere chosen uniformly among
    the *rooted* triangulations on `n` vertices. Because some
    triangulations have nontrivial automorphism groups, this may
    not be equal to the uniform distribution among unrooted
    triangulations.

    ALGORITHM:

    The algorithm is taken from [PS2006]_, section 2.1.

    Starting from a planar tree (represented by its contour as a
    sequence of vertices), one first performs local closures, until no
    one is possible. A local closure amounts to replace in the cyclic
    contour word a sequence ``in1, in2, in3, lf, in3`` by
    ``in1, in3``. After all local closures are done, one has reached
    the partial closure, as in [PS2006]_, figure 5 (a).

    Then one has to perform complete closure by adding two more
    vertices, in order to reach the situation of [PS2006]_, figure 5
    (b). For this, it is necessary to find inside the final contour
    one of the two subsequences ``lf, in, lf``.

    At every step of the algorithm, newly created triangles are added
    in a simplicial complex.

    This algorithm is implemented in
    :meth:`~sage.graphs.generators.random.RandomTriangulation`, which
    creates an embedded graph. The triangles of the simplicial
    complex are recovered from this embedded graph.

    EXAMPLES::

        sage: G = simplicial_complexes.RandomTwoSphere(6); G
        Simplicial complex with vertex set (0, 1, 2, 3, 4, 5) and 8 facets
        sage: G.homology()                                                              # needs sage.modules
        {0: 0, 1: 0, 2: Z}
        sage: G.is_pure()
        True
        sage: fg = G.flip_graph(); fg
        Graph on 8 vertices
        sage: fg.is_planar() and fg.is_regular(3)
        True
    """
def ShiftedComplex(generators):
    """
    Return the smallest shifted simplicial complex containing ``generators``
    as faces.

    Let `V` be a set of vertices equipped with a total order.  The
    'componentwise partial ordering' on k-subsets of `V` is defined as
    follows: if `A = \\{a_1 < \\cdots < a_k\\}` and `B = \\{b_1 < \\cdots < b_k\\}`,
    then `A \\leq_C B` iff `a_i \\leq b_i` for all `i`.  A simplicial complex
    `X` on vertex set `[n]` is *shifted* if its faces form an order ideal
    under the componentwise partial ordering, i.e., if `B \\in X` and
    `A \\leq_C B` then `A \\in X`.  Shifted complexes of dimension 1 are also
    known as threshold graphs.

    .. NOTE::

        This method assumes that `V` consists of positive integers
        with the natural ordering.

    INPUT:

    - ``generators`` -- list of generators of the order ideal, which may
      be lists, tuples or simplices

    EXAMPLES::

        sage: # needs sage.combinat
        sage: X = simplicial_complexes.ShiftedComplex([Simplex([1, 6]), (2, 4), [8]])
        sage: sorted(X.facets())
        [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (7,), (8,)]
        sage: X = simplicial_complexes.ShiftedComplex([[2, 3, 5]])
        sage: sorted(X.facets())
        [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (2, 3, 4), (2, 3, 5)]
        sage: X = simplicial_complexes.ShiftedComplex([[1, 3, 5], [2, 6]])
        sage: sorted(X.facets())
        [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 6), (2, 6)]
    """
def RudinBall():
    """
    Return the non-shellable ball constructed by Rudin.

    This complex is a non-shellable triangulation of the 3-ball
    with 14 vertices and 41 facets, constructed by Rudin in
    [Rud1958]_.

    EXAMPLES::

        sage: R = simplicial_complexes.RudinBall(); R
        Rudin ball
        sage: R.f_vector()
        [1, 14, 66, 94, 41]
        sage: R.homology()                                                              # needs sage.modules
        {0: 0, 1: 0, 2: 0, 3: 0}
        sage: R.is_cohen_macaulay()                                                     # needs sage.modules
        True
    """
def ZieglerBall():
    """
    Return the non-shellable ball constructed by Ziegler.

    This complex is a non-shellable triangulation of the 3-ball
    with 10 vertices and 21 facets, constructed by Ziegler in
    [Zie1998]_ and the smallest such complex known.

    EXAMPLES::

        sage: Z = simplicial_complexes.ZieglerBall(); Z
        Ziegler ball
        sage: Z.f_vector()
        [1, 10, 38, 50, 21]
        sage: Z.homology()                                                              # needs sage.modules
        {0: 0, 1: 0, 2: 0, 3: 0}
        sage: Z.is_cohen_macaulay()                                                     # needs sage.modules
        True
    """
def DunceHat():
    """
    Return the minimal triangulation of the dunce hat given by Hachimori
    [Hac2016]_.

    This is a standard example of a space that is contractible
    but not collapsible.

    EXAMPLES::

        sage: D = simplicial_complexes.DunceHat(); D
        Minimal triangulation of the dunce hat
        sage: D.f_vector()
        [1, 8, 24, 17]
        sage: D.homology()                                                              # needs sage.modules
        {0: 0, 1: 0, 2: 0}
        sage: D.is_cohen_macaulay()                                                     # needs sage.modules
        True
    """
def FareyMap(p):
    """
    Return a discrete surface associated with `PSL(2, \\GF(p))`.

    INPUT:

    - ``p`` -- a prime number

    The vertices are the nonzero pairs `(x,y)` in `\\GF(p)^2` modulo
    the identification of `(-x, -y)` with `(x,y)`.

    The triangles are the images of the base triangle ((1,0),(0,1),(1,1))
    under the action of `PSL(2, \\GF(p))`.

    For `p = 3`, the result is a tetrahedron, for `p = 5` an icosahedron,
    and for `p = 7` a triangulation of the Klein quartic of genus `3`.

    As a Riemann surface, this is the quotient of the upper half plane
    by the principal congruence subgroup `\\Gamma(p)`.

    EXAMPLES::

        sage: S5 = simplicial_complexes.FareyMap(5); S5                                 # needs sage.groups
        Simplicial complex with 12 vertices and 20 facets
        sage: S5.automorphism_group().cardinality()                                     # needs sage.groups
        120

        sage: S7 = simplicial_complexes.FareyMap(7); S7                                 # needs sage.groups
        Simplicial complex with 24 vertices and 56 facets
        sage: S7.f_vector()                                                             # needs sage.groups
        [1, 24, 84, 56]

    REFERENCES:

    - [ISS2019] Ioannis Ivrissimtzis, David Singerman and James Strudwick,
      *From Farey Fractions to the Klein Quartic and Beyond*.
      :arxiv:`1909.08568`
    """
def GenusSix():
    """
    Return a triangulated surface of genus 6.

    This is triangulated with 12 vertices, 66 edges and 44 faces. Each
    vertex is neighbour to all other vertices.

    It appears as number `58` in the classification of Altshuler,
    Bokowski and Schuchert in [ABS96]_, where it is the unique surface
    with the largest symmetry group, of order 12. This article refers
    for this surface to Ringel.

    EXAMPLES::

        sage: S = simplicial_complexes.GenusSix()
        sage: S.automorphism_group().cardinality()                                      # needs sage.groups
        12
        sage: S.betti()                                                                 # needs sage.modules
        {0: 1, 1: 12, 2: 1}
        sage: S.f_vector()
        [1, 12, 66, 44]

    REFERENCES:

    .. [ABS96] Amos Altshule, Jürgen Bokowski and Peter Schuchert,
               *Neighborly 2-Manifolds with 12 Vertices*,
               Journal of Combinatorial Theory, Series A, 75, 148-162 (1996),
               :doi:`10.1006/jcta.1996.0069`
    """
