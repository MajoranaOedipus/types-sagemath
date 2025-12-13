from .incidence_structures import IncidenceStructure as IncidenceStructure
from sage.arith.misc import binomial as binomial, integer_floor as integer_floor, is_prime_power as is_prime_power
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.unknown import Unknown as Unknown
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

BlockDesign = IncidenceStructure

def tdesign_params(t, v, k, L):
    """
    Return the design's parameters: `(t, v, b, r , k, L)`. Note that `t` must be
    given.

    EXAMPLES::

        sage: BD = BlockDesign(7, [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]])
        sage: from sage.combinat.designs.block_design import tdesign_params
        sage: tdesign_params(2,7,3,1)
        (2, 7, 7, 3, 3, 1)
    """
def are_hyperplanes_in_projective_geometry_parameters(v, k, lmbda, return_parameters: bool = False):
    """
    Return ``True`` if the parameters ``(v,k,lmbda)`` are the one of hyperplanes in
    a (finite Desarguesian) projective space.

    In other words, test whether there exists a prime power ``q`` and an integer
    ``d`` greater than two such that:

    - `v = (q^{d+1}-1)/(q-1) = q^d + q^{d-1} + ... + 1`
    - `k = (q^d - 1)/(q-1) = q^{d-1} + q^{d-2} + ... + 1`
    - `lmbda = (q^{d-1}-1)/(q-1) = q^{d-2} + q^{d-3} + ... + 1`

    If it exists, such a pair ``(q,d)`` is unique.

    INPUT:

    - ``v``, ``k``, ``lmbda`` -- integers

    OUTPUT:

    - a boolean or, if ``return_parameters`` is set to ``True`` a pair
      ``(True, (q,d))`` or ``(False, (None,None))``.

    EXAMPLES::

        sage: from sage.combinat.designs.block_design import are_hyperplanes_in_projective_geometry_parameters
        sage: are_hyperplanes_in_projective_geometry_parameters(40, 13, 4)
        True
        sage: are_hyperplanes_in_projective_geometry_parameters(40, 13, 4,
        ....:                                                   return_parameters=True)
        (True, (3, 3))
        sage: PG = designs.ProjectiveGeometryDesign(3, 2, GF(3))                        # needs sage.combinat
        sage: PG.is_t_design(return_parameters=True)                                    # needs sage.combinat
        (True, (2, 40, 13, 4))

        sage: are_hyperplanes_in_projective_geometry_parameters(15, 3, 1)
        False
        sage: are_hyperplanes_in_projective_geometry_parameters(15, 3, 1,
        ....:                                                   return_parameters=True)
        (False, (None, None))

    TESTS::

        sage: sgp = lambda q,d: ((q**(d+1)-1)//(q-1), (q**d-1)//(q-1), (q**(d-1)-1)//(q-1))
        sage: for q in [3,4,5,7,8,9,11]:
        ....:     for d in [2,3,4,5]:
        ....:         v,k,l = sgp(q,d)
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v,k,l,True) == (True, (q,d))
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v+1,k,l) is False
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v-1,k,l) is False
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v,k+1,l) is False
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v,k-1,l) is False
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v,k,l+1) is False
        ....:         assert are_hyperplanes_in_projective_geometry_parameters(v,k,l-1) is False
    """
def ProjectiveGeometryDesign(n, d, F, algorithm=None, point_coordinates: bool = True, check: bool = True):
    '''
    Return a projective geometry design.

    The projective geometry design `PG_d(n,q)` has for points the lines of
    `\\GF{q}^{n+1}`, and for blocks the `(d+1)`-dimensional subspaces of
    `\\GF{q}^{n+1}`, each of which contains `\\frac {|\\GF{q}|^{d+1}-1} {|\\GF{q}|-1}` lines.
    It is a `2`-design with parameters

    .. MATH::

        v = \\binom{n+1}{1}_q,\\ k = \\binom{d+1}{1}_q,\\ \\lambda =
        \\binom{n-1}{d-1}_q

    where the `q`-binomial coefficient `\\binom{m}{r}_q` is defined by

    .. MATH::

        \\binom{m}{r}_q = \\frac{(q^m - 1)(q^{m-1} - 1) \\cdots (q^{m-r+1}-1)}
              {(q^r-1)(q^{r-1}-1)\\cdots (q-1)}

    .. SEEALSO::

        :func:`AffineGeometryDesign`

    INPUT:

    - ``n`` -- the projective dimension

    - ``d`` -- the dimension of the subspaces which make up the blocks

    - ``F`` -- a finite field or a prime power

    - ``algorithm`` -- set to ``None`` by default, which results in using Sage\'s
      own implementation. In order to use GAP\'s implementation instead (i.e. its
      ``PGPointFlatBlockDesign`` function) set ``algorithm="gap"``. Note that
      GAP\'s "design" package must be available in this case, and that it can be
      installed with the ``gap_packages`` spkg.

    - ``point_coordinates`` -- ``True`` by default. Ignored and assumed to be ``False`` if
      ``algorithm="gap"``. If ``True``, the ground set is indexed by coordinates
      in `\\GF{q}^{n+1}`.  Otherwise the ground set is indexed by integers.

    - ``check`` -- boolean (default: ``True``); whether to check the output

    EXAMPLES:

    The set of `d`-dimensional subspaces in a `n`-dimensional projective space
    forms `2`-designs (or balanced incomplete block designs)::

        sage: PG = designs.ProjectiveGeometryDesign(4, 2, GF(2)); PG                    # needs sage.combinat
        Incidence structure with 31 points and 155 blocks
        sage: PG.is_t_design(return_parameters=True)                                    # needs sage.combinat
        (True, (2, 31, 7, 7))

        sage: PG = designs.ProjectiveGeometryDesign(3, 1, GF(4))                        # needs sage.combinat
        sage: PG.is_t_design(return_parameters=True)                                    # needs sage.combinat
        (True, (2, 85, 5, 1))

    Check with ``F`` being a prime power::

        sage: PG = designs.ProjectiveGeometryDesign(3, 2, 4); PG
        Incidence structure with 85 points and 85 blocks

    Use coordinates::

        sage: PG = designs.ProjectiveGeometryDesign(2, 1, GF(3))
        sage: PG.blocks()[0]
        [(1, 0, 0), (1, 0, 1), (1, 0, 2), (0, 0, 1)]

    Use indexing by integers::

        sage: PG = designs.ProjectiveGeometryDesign(2, 1, GF(3), point_coordinates=0)
        sage: PG.blocks()[0]
        [0, 1, 2, 12]

    Check that the constructor using gap also works::

        sage: BD = designs.ProjectiveGeometryDesign(2, 1, GF(2), algorithm=\'gap\')  # optional - gap_package_design
        sage: BD.is_t_design(return_parameters=True)                               # optional - gap_package_design
        (True, (2, 7, 3, 1))
    '''
def DesarguesianProjectivePlaneDesign(n, point_coordinates: bool = True, check: bool = True):
    """
    Return the Desarguesian projective plane of order ``n`` as a 2-design.

    The Desarguesian projective plane of order `n` can also be defined as the
    projective plane over a field of order `n`. For more information, have a
    look at :wikipedia:`Projective_plane`.

    INPUT:

    - ``n`` -- integer which must be a power of a prime number

    - ``point_coordinates`` -- boolean (default: ``True``); whether to label the
      points with their homogeneous coordinates (default) or with integers

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    .. SEEALSO::

        :func:`ProjectiveGeometryDesign`

    EXAMPLES::

        sage: designs.DesarguesianProjectivePlaneDesign(2)
        (7,3,1)-Balanced Incomplete Block Design
        sage: designs.DesarguesianProjectivePlaneDesign(3)
        (13,4,1)-Balanced Incomplete Block Design
        sage: designs.DesarguesianProjectivePlaneDesign(4)
        (21,5,1)-Balanced Incomplete Block Design
        sage: designs.DesarguesianProjectivePlaneDesign(5)
        (31,6,1)-Balanced Incomplete Block Design
        sage: designs.DesarguesianProjectivePlaneDesign(6)
        Traceback (most recent call last):
        ...
        ValueError: the order of a finite field must be a prime power
    """
def q3_minus_one_matrix(K):
    """
    Return a companion matrix in `GL(3, K)` whose multiplicative order is `q^3 - 1`.

    This function is used in :func:`HughesPlane`.

    EXAMPLES::

        sage: from sage.combinat.designs.block_design import q3_minus_one_matrix
        sage: m = q3_minus_one_matrix(GF(3))
        sage: m.multiplicative_order() == 3**3 - 1
        True

        sage: m = q3_minus_one_matrix(GF(4, 'a'))
        sage: m.multiplicative_order() == 4**3 - 1
        True

        sage: m = q3_minus_one_matrix(GF(5))
        sage: m.multiplicative_order() == 5**3 - 1
        True

        sage: m = q3_minus_one_matrix(GF(9, 'a'))
        sage: m.multiplicative_order() == 9**3 - 1
        True
    """
def normalize_hughes_plane_point(p, q):
    """
    Return the normalized form of point ``p`` as a 3-tuple.

    In the Hughes projective plane over the finite field `K`, all triples `(xk,
    yk, zk)` with `k \\in K` represent the same point (where the multiplication
    is over the nearfield built from `K`). This function chooses a canonical
    representative among them.

    This function is used in :func:`HughesPlane`.

    INPUT:

    - ``p`` -- point with the coordinates `(x,y,z)` (a list, a vector, a tuple...)

    - ``q`` -- cardinality of the underlying finite field

    EXAMPLES::

        sage: from sage.combinat.designs.block_design import normalize_hughes_plane_point
        sage: K = FiniteField(9,'x')
        sage: x = K.gen()
        sage: normalize_hughes_plane_point((x, x + 1, x), 9)
        (1, x, 1)
        sage: normalize_hughes_plane_point(vector((x,x,x)), 9)
        (1, 1, 1)
        sage: zero = K.zero()
        sage: normalize_hughes_plane_point((2*x + 2, zero, zero), 9)
        (1, 0, 0)
        sage: one = K.one()
        sage: normalize_hughes_plane_point((2*x, one, zero), 9)
        (2*x, 1, 0)
    """
def HughesPlane(q2, check: bool = True):
    """
    Return the Hughes projective plane of order ``q2``.

    Let `q` be an odd prime, the Hughes plane of order `q^2` is a finite
    projective plane of order `q^2` introduced by D. Hughes in [Hu57]_. Its
    construction is as follows.

    Let `K = GF(q^2)` be a finite field with `q^2` elements and `F = GF(q)
    \\subset K` be its unique subfield with `q` elements. We define a twisted
    multiplication on `K` as

    .. MATH::

        x \\circ y =
        \\begin{cases}
        x\\ y & \\text{if y is a square in K}\\\\\n        x^q\\ y & \\text{otherwise}
        \\end{cases}

    The points of the Hughes plane are the triples `(x, y, z)` of points in `K^3
    \\backslash \\{0,0,0\\}` up to the equivalence relation `(x,y,z) \\sim (x \\circ
    k, y \\circ k, z \\circ k)` where `k \\in K`.

    For `a = 1` or `a \\in (K \\backslash F)` we define a block `L(a)` as the set of
    triples `(x,y,z)` so that `x + a \\circ y + z = 0`. The rest of the blocks
    are obtained by letting act the group `GL(3, F)` by its standard action.

    For more information, see :wikipedia:`Hughes_plane` and [We07].

    .. SEEALSO::

        :func:`DesarguesianProjectivePlaneDesign` to build the Desarguesian
        projective planes

    INPUT:

    - ``q2`` -- an even power of an odd prime number

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: H = designs.HughesPlane(9); H
        (91,10,1)-Balanced Incomplete Block Design

    We prove in the following computations that the Desarguesian plane ``H`` is
    not Desarguesian. Let us consider the two triangles `(0,1,10)` and `(57, 70,
    59)`. We show that the intersection points `D_{0,1} \\cap D_{57,70}`,
    `D_{1,10} \\cap D_{70,59}` and `D_{10,0} \\cap D_{59,57}` are on the same line
    while `D_{0,70}`, `D_{1,59}` and `D_{10,57}` are not concurrent::

        sage: blocks = H.blocks()
        sage: line = lambda p,q: next(b for b in blocks if p in b and q in b)

        sage: b_0_1 = line(0, 1)
        sage: b_1_10 = line(1, 10)
        sage: b_10_0 = line(10, 0)
        sage: b_57_70 = line(57, 70)
        sage: b_70_59 = line(70, 59)
        sage: b_59_57 = line(59, 57)

        sage: set(b_0_1).intersection(b_57_70)
        {2}
        sage: set(b_1_10).intersection(b_70_59)
        {73}
        sage: set(b_10_0).intersection(b_59_57)
        {60}

        sage: line(2, 73) == line(73, 60)
        True

        sage: b_0_57 = line(0, 57)
        sage: b_1_70 = line(1, 70)
        sage: b_10_59 = line(10, 59)

        sage: p = set(b_0_57).intersection(b_1_70)
        sage: q = set(b_1_70).intersection(b_10_59)
        sage: p == q
        False

    TESTS:

    Some wrong input::

        sage: designs.HughesPlane(5)
        Traceback (most recent call last):
        ...
        EmptySetError: No Hughes plane of non-square order exists.

        sage: designs.HughesPlane(16)
        Traceback (most recent call last):
        ...
        EmptySetError: No Hughes plane of even order exists.

    Check that it works for non-prime `q`::

        sage: designs.HughesPlane(3**4)    # not tested - 10 secs
        (6643,82,1)-Balanced Incomplete Block Design
    """
def projective_plane_to_OA(pplane, pt=None, check: bool = True):
    """
    Return the orthogonal array built from the projective plane ``pplane``.

    The orthogonal array `OA(n+1,n,2)` is obtained from the projective plane
    ``pplane`` by removing the point ``pt`` and the `n+1` lines that pass
    through it`. These `n+1` lines form the `n+1` groups while the remaining
    `n^2+n` lines form the transversals.

    INPUT:

    - ``pplane`` -- a projective plane as a 2-design

    - ``pt`` -- a point in the projective plane ``pplane``; if it is not provided,
      then it is set to `n^2 + n`

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: from sage.combinat.designs.block_design import projective_plane_to_OA
        sage: p2 = designs.DesarguesianProjectivePlaneDesign(2, point_coordinates=False)
        sage: projective_plane_to_OA(p2)
        [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
        sage: p3 = designs.DesarguesianProjectivePlaneDesign(3, point_coordinates=False)
        sage: projective_plane_to_OA(p3)
        [[0, 0, 0, 0],
         [0, 1, 2, 1],
         [0, 2, 1, 2],
         [1, 0, 2, 2],
         [1, 1, 1, 0],
         [1, 2, 0, 1],
         [2, 0, 1, 1],
         [2, 1, 0, 2],
         [2, 2, 2, 0]]

        sage: pp = designs.DesarguesianProjectivePlaneDesign(16, point_coordinates=False)
        sage: _ = projective_plane_to_OA(pp, pt=0)
        sage: _ = projective_plane_to_OA(pp, pt=3)
        sage: _ = projective_plane_to_OA(pp, pt=7)
    """
def projective_plane(n, check: bool = True, existence: bool = False):
    '''
    Return a projective plane of order ``n`` as a 2-design.

    A finite projective plane is a 2-design with `n^2+n+1` lines (or blocks) and
    `n^2+n+1` points. For more information on finite projective planes, see the
    :wikipedia:`Projective_plane#Finite_projective_planes`.

    If no construction is possible, then the function raises a :exc:`EmptySetError`,
    whereas if no construction is available, the function raises a
    :exc:`NotImplementedError`.

    INPUT:

    - ``n`` -- the finite projective plane\'s order

    EXAMPLES::

        sage: # needs sage.schemes
        sage: designs.projective_plane(2)
        (7,3,1)-Balanced Incomplete Block Design
        sage: designs.projective_plane(3)
        (13,4,1)-Balanced Incomplete Block Design
        sage: designs.projective_plane(4)
        (21,5,1)-Balanced Incomplete Block Design
        sage: designs.projective_plane(5)
        (31,6,1)-Balanced Incomplete Block Design
        sage: designs.projective_plane(6)
        Traceback (most recent call last):
        ...
        EmptySetError: By the Bruck-Ryser theorem, no projective plane of order 6 exists.
        sage: designs.projective_plane(10)
        Traceback (most recent call last):
        ...
        EmptySetError: No projective plane of order 10 exists by
        C. Lam, L. Thiel and S. Swiercz "The nonexistence of finite
        projective planes of order 10" (1989), Canad. J. Math.
        sage: designs.projective_plane(12)
        Traceback (most recent call last):
        ...
        NotImplementedError: If such a projective plane exists,
        we do not know how to build it.
        sage: designs.projective_plane(14)
        Traceback (most recent call last):
        ...
        EmptySetError: By the Bruck-Ryser theorem, no projective plane of order 14 exists.

    TESTS::

        sage: # needs sage.schemes
        sage: designs.projective_plane(2197, existence=True)
        True
        sage: designs.projective_plane(6, existence=True)
        False
        sage: designs.projective_plane(10, existence=True)
        False
        sage: designs.projective_plane(12, existence=True)
        Unknown
    '''
def AffineGeometryDesign(n, d, F, point_coordinates: bool = True, check: bool = True):
    """
    Return an affine geometry design.

    The affine geometry design `AG_d(n,q)` is the 2-design whose blocks are the
    `d`-vector subspaces in `\\GF{q}^n`. It has parameters

    .. MATH::

        v = q^n,\\ k = q^d,\\ \\lambda = \\binom{n-1}{d-1}_q

    where the `q`-binomial coefficient `\\binom{m}{r}_q` is defined by

    .. MATH::

        \\binom{m}{r}_q = \\frac{(q^m - 1)(q^{m-1} - 1) \\cdots (q^{m-r+1}-1)}
              {(q^r-1)(q^{r-1}-1)\\cdots (q-1)}

    .. SEEALSO::

        :func:`ProjectiveGeometryDesign`

    INPUT:

    - ``n`` -- integer; the Euclidean dimension. The number of points of the
      design is `v=|\\GF{q}^n|`

    - ``d`` -- integer; the dimension of the (affine) subspaces of `\\GF{q}^n`
      which make up the blocks

    - ``F`` -- a finite field or a prime power

    - ``point_coordinates`` -- boolean (default: ``True``); whether we use
      coordinates in `\\GF{q}^n` or plain integers for the points of the design

    - ``check`` -- boolean (default: ``True``); whether to check the output

    EXAMPLES::

        sage: # needs sage.combinat
        sage: BD = designs.AffineGeometryDesign(3, 1, GF(2))
        sage: BD.is_t_design(return_parameters=True)
        (True, (2, 8, 2, 1))
        sage: BD = designs.AffineGeometryDesign(3, 2, GF(4))
        sage: BD.is_t_design(return_parameters=True)
        (True, (2, 64, 16, 5))
        sage: BD = designs.AffineGeometryDesign(4, 2, GF(3))
        sage: BD.is_t_design(return_parameters=True)
        (True, (2, 81, 9, 13))

    With ``F`` an integer instead of a finite field::

        sage: BD = designs.AffineGeometryDesign(3, 2, 4)
        sage: BD.is_t_design(return_parameters=True)
        (True, (2, 64, 16, 5))

    Testing the option ``point_coordinates``::

        sage: designs.AffineGeometryDesign(3, 1, GF(2),
        ....:                              point_coordinates=True).blocks()[0]
        [(0, 0, 0), (0, 0, 1)]
        sage: designs.AffineGeometryDesign(3, 1, GF(2),
        ....:                              point_coordinates=False).blocks()[0]
        [0, 1]
    """
def CremonaRichmondConfiguration():
    """
    Return the Cremona-Richmond configuration.

    The Cremona-Richmond configuration is a set system whose incidence graph
    is equal to the
    :meth:`~sage.graphs.graph_generators.GraphGenerators.TutteCoxeterGraph`. It
    is a generalized quadrangle of parameters `(2,2)`.

    For more information, see the
    :wikipedia:`Cremona-Richmond_configuration`.

    EXAMPLES::

        sage: H = designs.CremonaRichmondConfiguration(); H                             # needs networkx
        Incidence structure with 15 points and 15 blocks
        sage: g = graphs.TutteCoxeterGraph()                                            # needs networkx
        sage: H.incidence_graph().is_isomorphic(g)                                      # needs networkx
        True
    """
def WittDesign(n):
    """
    INPUT:

    - ``n`` -- integer in `9,10,11,12,21,22,23,24`

    Wraps GAP Design's WittDesign. If ``n=24`` then this function returns the
    large Witt design `W_{24}`, the unique (up to isomorphism) `5-(24,8,1)`
    design. If ``n=12`` then this function returns the small Witt design
    `W_{12}`, the unique (up to isomorphism) `5-(12,6,1)` design.  The other
    values of `n` return a block design derived from these.

    .. NOTE::

        Requires GAP's Design package (included in the gap_packages Sage spkg).

    EXAMPLES::

        sage: # optional - gap_package_design
        sage: BD = designs.WittDesign(9)
        sage: BD.is_t_design(return_parameters=True)
        (True, (2, 9, 3, 1))
        sage: BD
        Incidence structure with 9 points and 12 blocks
        sage: print(BD)
        Incidence structure with 9 points and 12 blocks
    """
def HadamardDesign(n):
    """
    As described in Section 1, p. 10, in [CvL]_. The input n must have the
    property that there is a Hadamard matrix of order `n+1` (and that a
    construction of that Hadamard matrix has been implemented...).

    EXAMPLES::

        sage: # needs sage.combinat sage.modules
        sage: designs.HadamardDesign(7)
        Incidence structure with 7 points and 7 blocks
        sage: print(designs.HadamardDesign(7))
        Incidence structure with 7 points and 7 blocks

    For example, the Hadamard 2-design with `n = 11` is a design whose parameters are `2-(11, 5, 2)`.
    We verify that `NJ = 5J` for this design. ::

        sage: # needs sage.combinat sage.modules
        sage: D = designs.HadamardDesign(11); N = D.incidence_matrix()
        sage: J = matrix(ZZ, 11, 11, [1]*11*11); N*J
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]
        [5 5 5 5 5 5 5 5 5 5 5]

    REFERENCES:

    - [CvL] P. Cameron, J. H. van Lint, Designs, graphs, codes and
      their links, London Math. Soc., 1991.
    """
def Hadamard3Design(n):
    """
    Return the Hadamard 3-design with parameters `3-(n, \\frac n 2, \\frac n 4 - 1)`.

    This is the unique extension of the Hadamard `2`-design (see
    :meth:`HadamardDesign`).  We implement the description from pp. 12 in
    [CvL]_.

    INPUT:

    - ``n`` -- integer; a multiple of 4 such that `n>4`

    EXAMPLES::

        sage: # needs sage.combinat sage.modules
        sage: designs.Hadamard3Design(12)
        Incidence structure with 12 points and 22 blocks

    We verify that any two blocks of the Hadamard `3`-design `3-(8, 4, 1)`
    design meet in `0` or `2` points. More generally, it is true that any two
    blocks of a Hadamard `3`-design meet in `0` or `\\frac{n}{4}` points (for `n
    > 4`).

    ::

        sage: # needs sage.combinat sage.modules
        sage: D = designs.Hadamard3Design(8)
        sage: N = D.incidence_matrix()
        sage: N.transpose()*N
        [4 2 2 2 2 2 2 2 2 2 2 2 2 0]
        [2 4 2 2 2 2 2 2 2 2 2 2 0 2]
        [2 2 4 2 2 2 2 2 2 2 2 0 2 2]
        [2 2 2 4 2 2 2 2 2 2 0 2 2 2]
        [2 2 2 2 4 2 2 2 2 0 2 2 2 2]
        [2 2 2 2 2 4 2 2 0 2 2 2 2 2]
        [2 2 2 2 2 2 4 0 2 2 2 2 2 2]
        [2 2 2 2 2 2 0 4 2 2 2 2 2 2]
        [2 2 2 2 2 0 2 2 4 2 2 2 2 2]
        [2 2 2 2 0 2 2 2 2 4 2 2 2 2]
        [2 2 2 0 2 2 2 2 2 2 4 2 2 2]
        [2 2 0 2 2 2 2 2 2 2 2 4 2 2]
        [2 0 2 2 2 2 2 2 2 2 2 2 4 2]
        [0 2 2 2 2 2 2 2 2 2 2 2 2 4]


    REFERENCES:

    .. [CvL] \\P. Cameron, J. H. van Lint, Designs, graphs, codes and
      their links, London Math. Soc., 1991.
    """
