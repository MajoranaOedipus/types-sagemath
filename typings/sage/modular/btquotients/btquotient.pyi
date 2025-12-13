from _typeshed import Incomplete
from sage.arith.misc import fundamental_discriminant as fundamental_discriminant, gcd as gcd, kronecker_symbol as kronecker_symbol, xgcd as xgcd
from sage.interfaces.magma import magma as magma
from sage.matrix.constructor import Matrix as Matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.matrix.special import column_matrix as column_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.verbose import verbose as verbose
from sage.modular.arithgroup.congroup_gammaH import GammaH_constructor as GammaH_constructor
from sage.modular.dirichlet import DirichletGroup as DirichletGroup
from sage.quadratic_forms.quadratic_form import QuadraticForm as QuadraticForm
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DoubleCosetReduction(SageObject):
    """
    Edges in the Bruhat-Tits tree are represented by cosets of
    matrices in `GL_2`. Given a matrix `x` in `GL_2`, this
    class computes and stores the data corresponding to the
    double coset representation of `x` in terms of a fundamental
    domain of edges for the action of the arithmetic group `\\Gamma`.

    More precisely:

    Initialized with an element `x` of `GL_2(\\ZZ)`, finds elements
    `\\gamma` in `\\Gamma`, `t` and an edge `e` such that `get=x`. It
    stores these values as members ``gamma``, ``label`` and functions
    ``self.sign()``,  ``self.t()`` and ``self.igamma()``, satisfying:

    - if ``self.sign() == +1``:
      ``igamma() * edge_list[label].rep * t() == x``

    - if ``self.sign() == -1``:
      ``igamma() * edge_list[label].opposite.rep * t() == x``

    It also stores a member called power so that:

        ``p**(2*power) = gamma.reduced_norm()``

    The usual decomposition `get=x` would be:

    - g = gamma / (p ** power)

    - e = edge_list[label]

    - t' = t * p ** power

    Here usual denotes that we have rescaled gamma to have unit
    determinant, and so that the result is honestly an element
    of the arithmetic quaternion group under consideration. In
    practice we store integral multiples and keep track of the
    powers of `p`.

    INPUT:

    - ``Y`` -- BruhatTitsQuotient object in which to work
    - ``x`` -- Something coercible into a matrix in `GL_2(\\ZZ)`. In
      principle we should allow elements in `GL_2(\\QQ_p)`, but it is
      enough to work with integral entries
    - ``extrapow`` -- gets added to the power attribute, and it is
      used for the Hecke action

    EXAMPLES::

        sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
        sage: Y = BruhatTitsQuotient(5, 13)
        sage: x = Matrix(ZZ,2,2,[123,153,1231,1231])
        sage: d = DoubleCosetReduction(Y,x)
        sage: d.sign()
        -1
        sage: d.igamma()*Y._edge_list[d.label - len(Y.get_edge_list())].opposite.rep*d.t() == x
        True
        sage: x = Matrix(ZZ,2,2,[1423,113553,11231,12313])
        sage: d = DoubleCosetReduction(Y,x)
        sage: d.sign()
        1
        sage: d.igamma()*Y._edge_list[d.label].rep*d.t() == x
        True

    AUTHORS:

    - Cameron Franc (2012-02-20)
    - Marc Masdeu
    """
    parity: Incomplete
    label: Incomplete
    gamma: Incomplete
    x: Incomplete
    power: Incomplete
    def __init__(self, Y, x, extrapow: int = 0) -> None:
        """
        Initialize and compute the reduction as a double coset.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
            sage: Y = BruhatTitsQuotient(5, 13)
            sage: x = Matrix(ZZ,2,2,[123,153,1231,1231])
            sage: d = DoubleCosetReduction(Y,x)
            sage: TestSuite(d).run()
        """
    def __eq__(self, other):
        """
        Return ``self == other``.

        TESTS::

            sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
            sage: Y = BruhatTitsQuotient(5, 13)
            sage: x = Matrix(ZZ,2,2,[123,153,1231,1231])
            sage: d1 = DoubleCosetReduction(Y,x)
            sage: d1 == d1
            True
        """
    def __ne__(self, other):
        """
        Return ``self != other``.

        TESTS::

            sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
            sage: Y = BruhatTitsQuotient(5, 13)
            sage: x = Matrix(ZZ,2,2,[123,153,1231,1231])
            sage: d1 = DoubleCosetReduction(Y,x)
            sage: d1 != d1
            False
        """
    def sign(self):
        """
        Return the direction of the edge.

        The Bruhat-Tits quotients are directed graphs but we only store
        half the edges (we treat them more like unordered graphs).
        The sign tells whether the matrix self.x is equivalent to the
        representative in the quotient (sign = +1), or to the
        opposite of one of the representatives (sign = -1).

        OUTPUT:

        an int that is +1 or -1 according to the sign of ``self``

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
            sage: Y = BruhatTitsQuotient(3, 11)
            sage: x = Matrix(ZZ,2,2,[123,153,1231,1231])
            sage: d = DoubleCosetReduction(Y,x)
            sage: d.sign()
            -1
            sage: d.igamma()*Y._edge_list[d.label - len(Y.get_edge_list())].opposite.rep*d.t() == x
            True
            sage: x = Matrix(ZZ,2,2,[1423,113553,11231,12313])
            sage: d = DoubleCosetReduction(Y,x)
            sage: d.sign()
            1
            sage: d.igamma()*Y._edge_list[d.label].rep*d.t() == x
            True
        """
    def igamma(self, embedding=None, scale: int = 1):
        """
        Image under gamma.

        Elements of the arithmetic group can be regarded as elements
        of the global quaternion order, and hence may be represented
        exactly. This function computes the image of such an element
        under the local splitting and returns the corresponding `p`-adic
        approximation.

        INPUT:

        - ``embedding`` -- integer; or a function (default:
          none). If ``embedding`` is None, then the image of
          ``self.gamma`` under the local splitting associated to
          ``self.Y`` is used. If ``embedding`` is an integer, then
          the precision of the local splitting of self.Y is raised
          (if necessary) to be larger than this integer, and this
          new local splitting is used. If a function is passed, then
          map ``self.gamma`` under ``embedding``.
        - ``scale`` -- (default: 1) scaling factor applied to the output

        OUTPUT:

        a 2x2 matrix with `p`-adic entries encoding the image of ``self``
        under the local splitting

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
            sage: Y = BruhatTitsQuotient(7, 11)
            sage: d = DoubleCosetReduction(Y,Matrix(ZZ,2,2,[123,45,88,1]))
            sage: d.igamma()
            [6 + 6*7 + 6*7^2 + 6*7^3 + 6*7^4 + O(7^5)                                   O(7^5)]
            [                                  O(7^5) 6 + 6*7 + 6*7^2 + 6*7^3 + 6*7^4 + O(7^5)]
            sage: d.igamma(embedding = 7)
            [6 + 6*7 + 6*7^2 + 6*7^3 + 6*7^4 + 6*7^5 + 6*7^6 + O(7^7)                                                   O(7^7)]
            [                                                  O(7^7) 6 + 6*7 + 6*7^2 + 6*7^3 + 6*7^4 + 6*7^5 + 6*7^6 + O(7^7)]
        """
    def t(self, prec=None):
        """
        Return the 't part' of the decomposition using the rest of the data.

        INPUT:

        - ``prec`` -- a `p`-adic precision that t will be computed
          to. Defaults to the default working precision of self.

        OUTPUT:

        a 2x2 `p`-adic matrix with entries of
        precision ``prec`` that is the 't-part' of the decomposition of
        self

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import DoubleCosetReduction
            sage: Y = BruhatTitsQuotient(5, 13)
            sage: x = Matrix(ZZ,2,2,[123,153,1231,1232])
            sage: d = DoubleCosetReduction(Y,x)
            sage: t = d.t(20)
            sage: t[1,0].valuation() > 0
            True
        """

class BruhatTitsTree(SageObject, UniqueRepresentation):
    """
    An implementation of the Bruhat-Tits tree for `GL_2(\\QQ_p)`.

    INPUT:

    - ``p`` -- a prime number. The corresponding tree is then `p+1` regular

    EXAMPLES:

    We create the tree for `GL_2(\\QQ_5)`::

        sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
        sage: p = 5
        sage: T = BruhatTitsTree(p)
        sage: m = Matrix(ZZ,2,2,[p**5,p**2,p**3,1+p+p*3])
        sage: e = T.edge(m); e
        [  0  25]
        [625  21]
        sage: v0 = T.origin(e); v0
        [ 25   0]
        [ 21 125]
        sage: v1 = T.target(e); v1
        [ 25   0]
        [ 21 625]
        sage: T.origin(T.opposite(e)) == v1
        True
        sage: T.target(T.opposite(e)) == v0
        True

    A value error is raised if a prime is not passed::

        sage: T = BruhatTitsTree(4)
        Traceback (most recent call last):
        ...
        ValueError: input (4) must be prime

    AUTHORS:

    - Marc Masdeu (2012-02-20)
    """
    def __init__(self, p) -> None:
        """
        Initialize a BruhatTitsTree object for a given prime `p`.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: T = BruhatTitsTree(17)
            sage: TestSuite(T).run()
        """
    def target(self, e, normalized: bool = False):
        """
        Return the target vertex of the edge represented by the
        input matrix e.

        INPUT:

        - ``e`` -- a 2x2 matrix with integer entries

        - ``normalized`` -- boolean (default: ``False``); if True
            then the input matrix is assumed to be normalized

        OUTPUT:

        - ``e`` -- 2x2 integer matrix representing the target of
          the input edge

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: T = BruhatTitsTree(7)
            sage: T.target(Matrix(ZZ,2,2,[1,5,8,9]))
            [1 0]
            [0 1]
        """
    def origin(self, e, normalized: bool = False):
        """
        Return the origin vertex of the edge represented by the
        input matrix e.

        INPUT:

        - ``e`` -- a 2x2 matrix with integer entries

        - ``normalized`` -- boolean (default: ``False``); if True
          then the input matrix M is assumed to be normalized

        OUTPUT: ``e`` -- 2x2 integer matrix

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: T = BruhatTitsTree(7)
            sage: T.origin(Matrix(ZZ,2,2,[1,5,8,9]))
            [1 0]
            [1 7]
        """
    def edge(self, M):
        """
        Normalize a matrix to the correct normalized edge
        representative.

        INPUT:

        - ``M`` -- 2x2 integer matrix

        OUTPUT: ``newM`` -- 2x2 integer matrix

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: T = BruhatTitsTree(3)
            sage: T.edge( Matrix(ZZ,2,2,[0,-1,3,0]) )
            [0 1]
            [3 0]
        """
    def vertex(self, M):
        """
        Normalize a matrix to the corresponding normalized
        vertex representative

        INPUT:

        - ``M`` -- 2x2 integer matrix

        OUTPUT: a 2x2 integer matrix

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 5
            sage: T = BruhatTitsTree(p)
            sage: m = Matrix(ZZ,2,2,[p**5,p**2,p**3,1+p+p*3])
            sage: e = T.edge(m)
            sage: t = m.inverse()*e
            sage: scaling = Qp(p,20)(t.determinant()).sqrt()
            sage: t = 1/scaling * t
            sage: min([t[ii,jj].valuation(p) for ii in range(2) for jj in range(2)]) >= 0
            True
            sage: t[1,0].valuation(p) > 0
            True
        """
    def edges_leaving_origin(self):
        """
        Find normalized representatives for the `p+1` edges
        leaving the origin vertex corresponding to the homothety class
        of `\\ZZ_p^2`. These are cached.

        OUTPUT: list of size `p+1` of 2x2 integer matrices

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: T = BruhatTitsTree(3)
            sage: T.edges_leaving_origin()
            [
            [0 1]  [3 0]  [0 1]  [0 1]
            [3 0], [0 1], [3 1], [3 2]
            ]
        """
    def edge_between_vertices(self, v1, v2, normalized: bool = False):
        """
        Compute the normalized matrix rep. for the edge
        passing between two vertices.

        INPUT:

        - ``v1`` -- 2x2 integer matrix

        - ``v2`` -- 2x2 integer matrix

        - ``normalized`` -- boolean (default: ``False``); whether the
          vertices are normalized

        OUTPUT:

        - 2x2 integer matrix, representing the edge from ``v1`` to
          ``v2``.  If ``v1`` and ``v2`` are not at distance `1`, raise
          a :exc:`ValueError`.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 7
            sage: T = BruhatTitsTree(p)
            sage: v1 = T.vertex(Matrix(ZZ,2,2,[p,0,0,1])); v1
            [7 0]
            [0 1]
            sage: v2 = T.vertex(Matrix(ZZ,2,2,[p,1,0,1])); v2
            [1 0]
            [1 7]
            sage: T.edge_between_vertices(v1,v2)
            Traceback (most recent call last):
            ...
            ValueError: Vertices are not adjacent.

            sage: v3 = T.vertex(Matrix(ZZ,2,2,[1,0,0,1])); v3
            [1 0]
            [0 1]
            sage: T.edge_between_vertices(v1,v3)
            [0 1]
            [1 0]
        """
    def leaving_edges(self, M):
        """
        Return edges leaving a vertex.

        INPUT:

        - ``M`` -- 2x2 integer matrix

        OUTPUT: list of size `p+1` of 2x2 integer matrices

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 7
            sage: T = BruhatTitsTree(p)
            sage: T.leaving_edges(Matrix(ZZ,2,2,[1,0,0,1]))
            [
            [0 1]  [7 0]  [0 1]  [0 1]  [0 1]  [0 1]  [0 1]  [0 1]
            [7 0], [0 1], [7 1], [7 4], [7 5], [7 2], [7 3], [7 6]
            ]
        """
    def opposite(self, e):
        """
        This function returns the edge oriented oppositely to a
        given edge.

        INPUT:

        - ``e`` -- 2x2 integer matrix

        OUTPUT: 2x2 integer matrix

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 7
            sage: T = BruhatTitsTree(p)
            sage: e = Matrix(ZZ,2,2,[1,0,0,1])
            sage: T.opposite(e)
            [0 1]
            [7 0]
            sage: T.opposite(T.opposite(e)) == e
            True
        """
    def entering_edges(self, v):
        """
        This function returns the edges entering a given vertex.

        INPUT:

        - ``v`` -- 2x2 integer matrix

        OUTPUT: list of size `p+1` of 2x2 integer matrices

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 7
            sage: T = BruhatTitsTree(p)
            sage: T.entering_edges(Matrix(ZZ,2,2,[1,0,0,1]))
            [
            [1 0]  [0 1]  [1 0]  [1 0]  [1 0]  [1 0]  [1 0]  [1 0]
            [0 1], [1 0], [1 1], [4 1], [5 1], [2 1], [3 1], [6 1]
            ]
        """
    def subdivide(self, edgelist, level):
        """
        (Ordered) edges of ``self`` may be regarded as open balls in
        `P^1(\\QQ_p)`.  Given a list of edges, this function return a list
        of edges corresponding to the level-th subdivision of the
        corresponding opens.  That is, each open ball of the input is
        broken up into `p^{\\mbox{level}}` subballs of equal radius.

        INPUT:

        - ``edgelist`` -- list of edges

        - ``level`` -- integer

        OUTPUT: list of 2x2 integer matrices

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 3
            sage: T = BruhatTitsTree(p)
            sage: T.subdivide([Matrix(ZZ,2,2,[p,0,0,1])],2)
            [
            [27  0]  [0 9]  [0 9]  [0 3]  [0 3]  [0 3]  [0 3]  [0 3]  [0 3]
            [ 0  1], [3 1], [3 2], [9 1], [9 4], [9 7], [9 2], [9 5], [9 8]
            ]
        """
    def get_balls(self, center: int = 1, level: int = 1):
        """
        Return a decomposition of `P^1(\\QQ_p)` into compact
        open balls.

        Each vertex in the Bruhat-Tits tree gives a decomposition of
        `P^1(\\QQ_p)` into `p+1` open balls. Each of these balls may
        be further subdivided, to get a finer decomposition.

        This function returns the decomposition of `P^1(\\QQ_p)`
        corresponding to ``center`` into `(p+1)p^{\\mbox{level}}` balls.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 2
            sage: T = BruhatTitsTree(p)
            sage: T.get_balls(Matrix(ZZ,2,2,[p,0,0,1]),1)
            [
            [0 1]  [0 1]  [8 0]  [0 4]  [0 2]  [0 2]
            [2 0], [2 1], [0 1], [2 1], [4 1], [4 3]
            ]
        """
    def find_path(self, v, boundary=None):
        """
        Compute a path from a vertex to a given set of so-called
        boundary vertices, whose interior must contain the origin
        vertex.  In the case that the boundary is not specified, it
        computes the geodesic between the given vertex and the origin.
        In the case that the boundary contains more than one vertex,
        it computes the geodesic to some point of the boundary.

        INPUT:

        - ``v`` -- a 2x2 matrix representing a vertex ``boundary``

        - a list of matrices (default: ``None``); if omitted, finds the
          geodesic from ``v`` to the central vertex

        OUTPUT:

        An ordered list of vertices describing the geodesic from
        ``v`` to ``boundary``, followed by the vertex in the boundary
        that is closest to ``v``.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 3
            sage: T = BruhatTitsTree(p)
            sage: T.find_path( Matrix(ZZ,2,2,[p^4,0,0,1]) )
            (
            [[81  0]
            [ 0  1], [27  0]
            [ 0  1], [9 0]
            [0 1], [3 0]      [1 0]
            [0 1]]          , [0 1]
            )
            sage: T.find_path( Matrix(ZZ,2,2,[p^3,0,134,p^2]) )
            (
            [[27  0]
            [ 8  9], [27  0]
            [ 2  3], [27  0]
            [ 0  1], [9 0]
            [0 1], [3 0]      [1 0]
            [0 1]]          , [0 1]
            )
        """
    def find_containing_affinoid(self, z):
        """
        Return the vertex corresponding to the affinoid in the
        `p`-adic upper half plane that a given (unramified!) point
        reduces to.

        INPUT:

        - ``z`` -- an element of an unramified extension of `\\QQ_p`
          that is not contained in `\\QQ_p`

        OUTPUT: a 2x2 integer matrix representing a vertex of ``self``

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: T = BruhatTitsTree(5)
            sage: K.<a> = Qq(5^2,20)
            sage: T.find_containing_affinoid(a)
            [1 0]
            [0 1]
            sage: z = 5*a+3
            sage: v = T.find_containing_affinoid(z).inverse(); v
            [   1    0]
            [-2/5  1/5]

        Note that the translate of ``z`` belongs to the standard
        affinoid. That is, it is a `p`-adic unit and its reduction
        modulo `p` is not in `\\GF{p}`::

            sage: gz = (v[0,0]*z+v[0,1])/(v[1,0]*z+v[1,1]); gz                          # needs sage.rings.padics
            (a + 1) + O(5^19)
            sage: gz.valuation() == 0                                                   # needs sage.rings.padics
            True
        """
    def find_geodesic(self, v1, v2, normalized: bool = True):
        """
        This function computes the geodesic between two vertices.

        INPUT:

        - ``v1`` -- 2x2 integer matrix representing a vertex

        - ``v2`` -- 2x2 integer matrix representing a vertex

        - ``normalized`` -- boolean (default: ``True``)

        OUTPUT:

        An ordered list of 2x2 integer matrices representing the vertices
        of the paths joining ``v1`` and ``v2``.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 3
            sage: T = BruhatTitsTree(p)
            sage: v1 = T.vertex( Matrix(ZZ,2,2,[p^3, 0, 1, p^1]) ); v1
            [27  0]
            [ 1  3]
            sage: v2 = T.vertex( Matrix(ZZ,2,2,[p,2,0,p]) ); v2
            [1 0]
            [6 9]
            sage: T.find_geodesic(v1,v2)
            [
            [27  0]  [27  0]  [9 0]  [3 0]  [1 0]  [1 0]  [1 0]
            [ 1  3], [ 0  1], [0 1], [0 1], [0 1], [0 3], [6 9]
            ]
        """
    def find_covering(self, z1, z2, level: int = 0):
        """
        Compute a covering of `P^1(\\QQ_p)` adapted to a certain
        geodesic in ``self``.

        More precisely, the `p`-adic upper half plane points ``z1``
        and ``z2`` reduce to vertices `v_1`, `v_2`.
        The returned covering consists of all the edges leaving the
        geodesic from `v_1` to `v_2`.

        INPUT:

        - ``z1``, ``z2`` -- unramified algebraic points of h_p

        OUTPUT: list of 2x2 integer matrices representing edges of self

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: from sage.modular.btquotients.btquotient import BruhatTitsTree
            sage: p = 3
            sage: K.<a> = Qq(p^2)
            sage: T = BruhatTitsTree(p)
            sage: z1 = a + a*p
            sage: z2 = 1 + a*p + a*p^2 - p^6
            sage: T.find_covering(z1,z2)
            [
            [0 1]  [3 0]  [0 1]  [0 1]  [0 1]  [0 1]
            [3 0], [0 1], [3 2], [9 1], [9 4], [9 7]
            ]

        .. NOTE::

            This function is used to compute certain Coleman integrals
            on `P^1`. That's why the input consists of two points of
            the `p`-adic upper half plane, but decomposes
            `P^1(\\QQ_p)`. This decomposition is what allows us to
            represent the relevant integrand as a locally analytic
            function. The ``z1`` and ``z2`` appear in the integrand.
        """

class Vertex(SageObject):
    """
    This is a structure to represent vertices of quotients of the
    Bruhat-Tits tree.  It is useful to enrich the representation of
    the vertex as a matrix with extra data.

    INPUT:

    - ``p`` -- prime integer

    - ``label`` -- integer which uniquely identifies this vertex

    - ``rep`` -- a 2x2 matrix in reduced form representing this
      vertex

    - ``leaving_edges`` -- (default: empty list) list of edges
      leaving this vertex

    - ``entering_edges`` -- (default: empty list) list of edges
      entering this vertex

    - ``determinant`` -- (default: ``None``) the determinant of ``rep``,
      if known

    - ``valuation`` -- (default: ``None``) the valuation of the
      determinant of ``rep``, if known

    EXAMPLES::

        sage: from sage.modular.btquotients.btquotient import Vertex
        sage: v1 = Vertex(5,0,Matrix(ZZ,2,2,[1,2,3,18]))
        sage: v1.rep
        [ 1  2]
        [ 3 18]
        sage: v1.entering_edges
        []

    AUTHORS:

    - Marc Masdeu (2012-02-20)
    """
    p: Incomplete
    label: Incomplete
    rep: Incomplete
    determinant: Incomplete
    valuation: Incomplete
    parity: Incomplete
    leaving_edges: Incomplete
    entering_edges: Incomplete
    def __init__(self, p, label, rep, leaving_edges=None, entering_edges=None, determinant=None, valuation=None) -> None:
        """
        This initializes a structure to represent vertices of
        quotients of the Bruhat-Tits tree. It is useful to enrich the
        representation of the vertex as a matrix with extra data.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import Vertex
            sage: Y = BruhatTitsQuotient(5,13)
            sage: v1 = Vertex(5,0,Matrix(ZZ,2,2,[1,2,3,18]))
            sage: TestSuite(v1).run()
        """
    def __eq__(self, other):
        """
        Return ``self == other``.

        TESTS::

            sage: from sage.modular.btquotients.btquotient import Vertex
            sage: v1 = Vertex(7,0,Matrix(ZZ,2,2,[1,2,3,18]))
            sage: v1 == v1
            True
        """
    def __ne__(self, other):
        """
        Return ``self != other``.

        TESTS::

            sage: from sage.modular.btquotients.btquotient import Vertex
            sage: v1 = Vertex(7,0,Matrix(ZZ,2,2,[1,2,3,18]))
            sage: v1 != v1
            False
        """

class Edge(SageObject):
    """
    This is a structure to represent edges of quotients of the
    Bruhat-Tits tree. It is useful to enrich the representation of an
    edge as a matrix with extra data.

    INPUT:

    - ``p`` -- prime integer

    - ``label`` -- integer which uniquely identifies this edge

    - ``rep`` -- a 2x2 matrix in reduced form representing this edge

    - ``origin`` -- the origin vertex of ``self``

    - ``target`` -- the target vertex of ``self``

    - ``links`` -- (default: empty list) list of elements of
      `\\Gamma` which identify different edges in the Bruhat-Tits tree
      which are equivalent to ``self``

    - ``opposite`` -- (default: ``None``) the edge opposite to ``self``

    - ``determinant`` -- (default: ``None``) the determinant of ``rep``,
      if known

    - ``valuation`` -- (default: ``None``) the valuation of the
      determinant of ``rep``, if known

    EXAMPLES::

        sage: from sage.modular.btquotients.btquotient import Edge, Vertex
        sage: v1 = Vertex(7,0,Matrix(ZZ,2,2,[1,2,3,18]))
        sage: v2 = Vertex(7,0,Matrix(ZZ,2,2,[3,2,1,18]))
        sage: e1 = Edge(7,0,Matrix(ZZ,2,2,[1,2,3,18]),v1,v2)
        sage: e1.rep
        [ 1  2]
        [ 3 18]

    AUTHORS:

    - Marc Masdeu (2012-02-20)
    """
    p: Incomplete
    label: Incomplete
    rep: Incomplete
    origin: Incomplete
    target: Incomplete
    links: Incomplete
    opposite: Incomplete
    determinant: Incomplete
    valuation: Incomplete
    parity: Incomplete
    def __init__(self, p, label, rep, origin, target, links=None, opposite=None, determinant=None, valuation=None) -> None:
        """
        Representation for edges of quotients of the Bruhat-Tits
        tree. It is useful to enrich the representation of an edge as
        a matrix with extra data.

        EXAMPLES::

            sage: from sage.modular.btquotients.btquotient import Edge
            sage: Y = BruhatTitsQuotient(5,11)
            sage: el = Y.get_edge_list()
            sage: e1 = el.pop()
            sage: e2 = Edge(5,e1.label,e1.rep,e1.origin,e1.target)
            sage: TestSuite(e2).run()
        """
    def __eq__(self, other):
        """
        Return ``self == other``.

        TESTS::

            sage: from sage.modular.btquotients.btquotient import Edge,Vertex
            sage: v1 = Vertex(7,0,Matrix(ZZ,2,2,[1,2,3,18]))
            sage: v2 = Vertex(7,0,Matrix(ZZ,2,2,[3,2,1,18]))
            sage: e1 = Edge(7,0,Matrix(ZZ,2,2,[1,2,3,18]),v1,v2)
            sage: e1 == e1
            True
        """
    def __ne__(self, other):
        """
        Return ``self != other``.

        TESTS::

            sage: from sage.modular.btquotients.btquotient import Edge,Vertex
            sage: v1 = Vertex(7,0,Matrix(ZZ,2,2,[1,2,3,18]))
            sage: v2 = Vertex(7,0,Matrix(ZZ,2,2,[3,2,1,18]))
            sage: e1 = Edge(7,0,Matrix(ZZ,2,2,[1,2,3,18]),v1,v2)
            sage: e1 != e1
            False
        """

class BruhatTitsQuotient(SageObject, UniqueRepresentation):
    """
    This function computes the quotient of the Bruhat-Tits tree
    by an arithmetic quaternionic group. The group in question is the
    group of norm 1 elements in an Eichler `\\ZZ[1/p]`-order of some (tame)
    level inside of a definite quaternion algebra that is unramified
    at the prime `p`. Note that this routine relies in Magma in the case
    `p = 2` or when `N^{+} > 1`.

    INPUT:

    - ``p`` -- a prime number

    - ``Nminus`` -- squarefree integer divisible by an odd number of
      distinct primes and relatively prime to p. This is the
      discriminant of the definite quaternion algebra that one is
      quotienting by.

    - ``Nplus`` -- integer coprime to pNminus (default: 1). This is
      the tame level. It need not be squarefree! If Nplus is not 1
      then the user currently needs magma installed due to sage's
      inability to compute well with nonmaximal Eichler orders in
      rational (definite) quaternion algebras.

    - ``character`` -- a Dirichlet character (default: ``None``) of modulus
      `pN^-N^+`

    - ``use_magma`` -- boolean (default: ``False``); if True, uses Magma
      for quaternion arithmetic

    - ``magma_session`` -- (default: ``None``) if specified, the Magma session
      to use

    EXAMPLES:

    Here is an example without a Dirichlet character::

        sage: X = BruhatTitsQuotient(13, 19)
        sage: X.genus()
        19
        sage: G = X.get_graph(); G
        Multi-graph on 4 vertices

    And an example with a Dirichlet character::

        sage: f = DirichletGroup(6)[1]
        sage: X = BruhatTitsQuotient(3,2*5*7,character = f)
        sage: X.genus()
        5

    .. NOTE::

        A sage implementation of Eichler orders in rational quaternions
        algebras would remove the dependency on magma.

    AUTHORS:

    - Marc Masdeu (2012-02-20)
    """
    @staticmethod
    def __classcall__(cls, p, Nminus, Nplus: int = 1, character=None, use_magma: bool = False, seed=None, magma_session=None):
        """
        Ensure that a canonical BruhatTitsQuotient is created.

        EXAMPLES::

            sage: BruhatTitsQuotient(3,17) is BruhatTitsQuotient(3,17,1)
            True
        """
    def __init__(self, p, Nminus, Nplus: int = 1, character=None, use_magma: bool = False, seed=None, magma_session=None) -> None:
        """
        Compute the quotient of the Bruhat-Tits tree by an arithmetic
        quaternionic group.

        EXAMPLES::

            sage: Y = BruhatTitsQuotient(19,11)
            sage: TestSuite(Y).run()
        """
    __hash__: Incomplete
    def __eq__(self, other):
        """
        Compare ``self`` with ``other``.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,13)
            sage: Y = BruhatTitsQuotient(p = 5, Nminus = 13, Nplus=1,seed = 1231)
            sage: X == Y
            True
        """
    def __ne__(self, other):
        """
        Compare ``self`` with ``other``.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,13)
            sage: Y = BruhatTitsQuotient(p = 5, Nminus = 13, Nplus=1,seed = 1231)
            sage: X != Y
            False
        """
    def get_vertex_dict(self):
        """
        This function returns the vertices of the quotient viewed as
        a dict.

        OUTPUT: a Python dict with the vertices of the quotient

        EXAMPLES::

            sage: X = BruhatTitsQuotient(37,3)
            sage: X.get_vertex_dict()
            {[1 0]
            [0 1]: Vertex of Bruhat-Tits tree for p = 37, [ 1  0]
            [ 0 37]: Vertex of Bruhat-Tits tree for p = 37}
        """
    def get_vertex_list(self):
        """
        Return a list of the vertices of the quotient.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(37,3)
            sage: X.get_vertex_list()
            [Vertex of Bruhat-Tits tree for p = 37, Vertex of Bruhat-Tits tree for p = 37]
        """
    def get_edge_list(self):
        """
        Return a list of ``Edge`` which represent a fundamental
        domain inside the Bruhat-Tits tree for the quotient.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(37,3)
            sage: len(X.get_edge_list())
            8
        """
    def get_list(self):
        """
        Return a list of ``Edge`` which represent a fundamental
        domain inside the Bruhat-Tits tree for the quotient,
        together with a list of the opposite edges. This is used
        to work with automorphic forms.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(37,3)
            sage: len(X.get_list())
            16
        """
    def get_nontorsion_generators(self):
        """
        Use a fundamental domain in the Bruhat-Tits tree, and
        certain gluing data for boundary vertices, in order to compute
        a collection of generators for the nontorsion part
        of the arithmetic quaternionic group that one is quotienting by.
        This is analogous to using a polygonal rep. of a compact real
        surface to present its fundamental domain.

        OUTPUT:

        - A generating list of elements of an arithmetic
          quaternionic group.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,13)
            sage: len(X.get_nontorsion_generators())
            3
        """
    @cached_method
    def get_generators(self):
        """
        Use a fundamental domain in the Bruhat-Tits tree, and
        certain gluing data for boundary vertices, in order to compute
        a collection of generators for the arithmetic quaternionic
        group that one is quotienting by. This is analogous to using a
        polygonal rep. of a compact real surface to present its
        fundamental domain.

        OUTPUT:

        - A generating list of elements of an arithmetic
          quaternionic group.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,2)
            sage: len(X.get_generators())
            2
        """
    @lazy_attribute
    def e3(self):
        """
        Compute the `e_3` invariant defined by the formula

        .. MATH::

           e_k =\\prod_{\\ell\\mid pN^-}\\left(1-\\left(\\frac{-3}{\\ell}\\right)\\right)\\prod_{\\ell \\| N^+}\\left(1+\\left(\\frac{-3}{\\ell}\\right)\\right)\\prod_{\\ell^2\\mid N^+} \\nu_\\ell(3)

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(31,3)
            sage: X.e3
            1
        """
    @lazy_attribute
    def e4(self):
        """
        Compute the `e_4` invariant defined by the formula

        .. MATH::

           e_k =\\prod_{\\ell\\mid pN^-}\\left(1-\\left(\\frac{-k}{\\ell}\\right)\\right)\\prod_{\\ell \\| N^+}\\left(1+\\left(\\frac{-k}{\\ell}\\right)\\right)\\prod_{\\ell^2\\mid N^+} \\nu_\\ell(k)

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(31,3)
            sage: X.e4
            2
        """
    @lazy_attribute
    def mu(self):
        """
        Compute the mu invariant of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(29,3)
            sage: X.mu
            2
        """
    @cached_method
    def get_num_verts(self):
        """
        Return the number of vertices in the quotient using the formula
        `V = 2(\\mu/12 + e_3/3 + e_4/4)`.

        OUTPUT:

        - An integer (the number of vertices)

        EXAMPLES::

            sage: X = BruhatTitsQuotient(29,11)
            sage: X.get_num_verts()
            4
        """
    @cached_method
    def get_num_ordered_edges(self):
        """
        Return the number of ordered edges `E` in the quotient using
        the formula relating the genus `g` with the number of vertices `V`
        and that of unordered edges `E/2`: `E = 2(g + V - 1)`.

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,2)
            sage: X.get_num_ordered_edges()
            2
        """
    def genus_no_formula(self):
        """
        Compute the genus of the quotient from the data of the
        quotient graph. This should agree with self.genus().

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,2*3*29)
            sage: X.genus_no_formula()
            17
            sage: X.genus_no_formula() == X.genus()
            True
        """
    @cached_method
    def genus(self):
        """
        Compute the genus of the quotient graph using a formula
        This should agree with self.genus_no_formula().

        Compute the genus of the Shimura curve
        corresponding to this quotient via Cerednik-Drinfeld. It is
        computed via a formula and not in terms of the quotient graph.

        INPUT:

        - ``level`` -- integer (default: ``None``); a level. By default, use that
          of ``self``.

        - ``Nplus`` -- integer (default: ``None``); a conductor. By default, use
          that of ``self``.

        OUTPUT: integer equal to the genus

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,2*5*31)
            sage: X.genus()
            21
            sage: X.genus() == X.genus_no_formula()
            True
        """
    @cached_method
    def dimension_harmonic_cocycles(self, k, lev=None, Nplus=None, character=None):
        """
        Compute the dimension of the space of harmonic cocycles
        of weight `k` on ``self``.

        OUTPUT: integer equal to the dimension

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,7)
            sage: [X.dimension_harmonic_cocycles(k) for k in range(2,20,2)]
            [1, 4, 4, 8, 8, 12, 12, 16, 16]

            sage: X = BruhatTitsQuotient(2,5) # optional - magma
            sage: [X.dimension_harmonic_cocycles(k) for k in range(2,40,2)] # optional - magma
            [0, 1, 3, 1, 3, 5, 3, 5, 7, 5, 7, 9, 7, 9, 11, 9, 11, 13, 11]

            sage: X = BruhatTitsQuotient(7, 2 * 3 * 5)
            sage: X.dimension_harmonic_cocycles(4)
            12
            sage: X = BruhatTitsQuotient(7, 2 * 3 * 5 * 11 * 13)
            sage: X.dimension_harmonic_cocycles(2)
            481
            sage: X.dimension_harmonic_cocycles(4)
            1440
        """
    def Nplus(self):
        """
        Return the tame level `N^+`.

        OUTPUT: integer equal to `N^+`

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7,1)
            sage: X.Nplus()
            1
        """
    def Nminus(self):
        """
        Return the discriminant of the relevant definite
        quaternion algebra.

        OUTPUT:

        An integer equal to `N^-`.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: X.Nminus()
            7
        """
    @cached_method
    def level(self):
        """
        Return `p N^-`, which is the discriminant of the
        indefinite quaternion algebra that is uniformed by
        Cerednik-Drinfeld.

        OUTPUT:

        An integer equal to `p N^-`.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: X.level()
            35
        """
    def prime(self):
        """
        Return the prime one is working with.

        OUTPUT: integer equal to the fixed prime `p`

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: X.prime()
            5
        """
    def get_graph(self):
        """
        Return the quotient graph (and compute it if needed).

        OUTPUT: a graph representing the quotient of the Bruhat-Tits tree

        EXAMPLES::

            sage: X = BruhatTitsQuotient(11,5)
            sage: X.get_graph()
            Multi-graph on 2 vertices
        """
    def get_fundom_graph(self):
        """
        Return the fundamental domain (and computes it if needed).

        OUTPUT: a fundamental domain for the action of `\\Gamma`

        EXAMPLES::

            sage: X = BruhatTitsQuotient(11,5)
            sage: X.get_fundom_graph()
            Graph on 24 vertices
        """
    def plot(self, *args, **kwargs):
        """
        Plot the quotient graph.

        OUTPUT: a plot of the quotient graph

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,23)
            sage: X.plot()                                                              # needs sage.plot
            Graphics object consisting of 17 graphics primitives
        """
    def plot_fundom(self, *args, **kwargs):
        """
        Plot a fundamental domain.

        OUTPUT: a plot of the fundamental domain

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,23)
            sage: X.plot_fundom()                                                       # needs sage.plot
            Graphics object consisting of 88 graphics primitives
        """
    def is_admissible(self, D) -> bool:
        """
        Test whether the imaginary quadratic field of
        discriminant `D` embeds in the quaternion algebra. It
        furthermore tests the Heegner hypothesis in this setting
        (e.g., is `p` inert in the field, etc).

        INPUT:

        - ``D`` -- integer whose squarefree part will define the
          quadratic field

        OUTPUT: boolean describing whether the quadratic field is admissible

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: [X.is_admissible(D) for D in range(-1,-20,-1)]
            [False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False]
        """
    @cached_method
    def get_extra_embedding_matrices(self):
        """
        Return a list of  matrices representing the different embeddings.

        .. NOTE::

           The precision is very low (currently set to 5 digits),
           since these embeddings are only used to apply a character.

        EXAMPLES:

        This portion of the code is only relevant when working with a
        nontrivial Dirichlet character. If there is no such character
        then the code returns an empty list. Even if the character is
        not trivial it might return an empty list::

            sage: f = DirichletGroup(6)[1]
            sage: X = BruhatTitsQuotient(3,2*5*7,character = f)
            sage: X.get_extra_embedding_matrices()
            []

        ::

            sage: f = DirichletGroup(6)[1]
            sage: X = BruhatTitsQuotient(5,2,3, character = f, use_magma=True) # optional - magma
            sage: X.get_extra_embedding_matrices() # optional - magma
            [
            [1 0 2 0]
            [0 0 2 0]
            [0 0 0 0]
            [1 2 2 0]
            ]
        """
    def get_embedding_matrix(self, prec=None, exact: bool = False):
        """
        Return the matrix of the embedding.

        INPUT:

        - ``exact`` -- boolean (default: ``False``); if ``True``, return an
          embedding into a matrix algebra with coefficients in a
          number field. Otherwise, embed into matrices over `p`-adic
          numbers.

        - ``prec`` -- integer (default: ``None``); if specified, return the
          matrix with precision ``prec``. Otherwise, return the
          cached matrix (with the current working precision).

        OUTPUT: a 4x4 matrix representing the embedding

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,2*3*5)
            sage: X.get_embedding_matrix(4)
            [                      1 + O(7^4)         5 + 2*7 + 3*7^3 + O(7^4) 4 + 5*7 + 6*7^2 + 6*7^3 + O(7^4)       6 + 3*7^2 + 4*7^3 + O(7^4)]
            [                          O(7^4)                           O(7^4)                   3 + 7 + O(7^4) 1 + 6*7 + 3*7^2 + 2*7^3 + O(7^4)]
            [                          O(7^4)         2 + 5*7 + 6*7^3 + O(7^4) 3 + 5*7 + 6*7^2 + 6*7^3 + O(7^4)         3 + 3*7 + 3*7^2 + O(7^4)]
            [                      1 + O(7^4) 3 + 4*7 + 6*7^2 + 3*7^3 + O(7^4)                   3 + 7 + O(7^4) 1 + 6*7 + 3*7^2 + 2*7^3 + O(7^4)]
            sage: X.get_embedding_matrix(3)
            [                      1 + O(7^4)         5 + 2*7 + 3*7^3 + O(7^4) 4 + 5*7 + 6*7^2 + 6*7^3 + O(7^4)       6 + 3*7^2 + 4*7^3 + O(7^4)]
            [                          O(7^4)                           O(7^4)                   3 + 7 + O(7^4) 1 + 6*7 + 3*7^2 + 2*7^3 + O(7^4)]
            [                          O(7^4)         2 + 5*7 + 6*7^3 + O(7^4) 3 + 5*7 + 6*7^2 + 6*7^3 + O(7^4)         3 + 3*7 + 3*7^2 + O(7^4)]
            [                      1 + O(7^4) 3 + 4*7 + 6*7^2 + 3*7^3 + O(7^4)                   3 + 7 + O(7^4) 1 + 6*7 + 3*7^2 + 2*7^3 + O(7^4)]
            sage: X.get_embedding_matrix(5)
            [                              1 + O(7^5)         5 + 2*7 + 3*7^3 + 6*7^4 + O(7^5) 4 + 5*7 + 6*7^2 + 6*7^3 + 6*7^4 + O(7^5)       6 + 3*7^2 + 4*7^3 + 5*7^4 + O(7^5)]
            [                                  O(7^5)                                   O(7^5)                           3 + 7 + O(7^5)   1 + 6*7 + 3*7^2 + 2*7^3 + 7^4 + O(7^5)]
            [                                  O(7^5)         2 + 5*7 + 6*7^3 + 5*7^4 + O(7^5) 3 + 5*7 + 6*7^2 + 6*7^3 + 6*7^4 + O(7^5)         3 + 3*7 + 3*7^2 + 5*7^4 + O(7^5)]
            [                              1 + O(7^5)         3 + 4*7 + 6*7^2 + 3*7^3 + O(7^5)                           3 + 7 + O(7^5)   1 + 6*7 + 3*7^2 + 2*7^3 + 7^4 + O(7^5)]
        """
    def embed_quaternion(self, g, exact: bool = False, prec=None):
        """
        Embed the quaternion element ``g`` into a matrix algebra.

        INPUT:

        - ``g`` -- a column vector of size `4` whose entries represent a
          quaternion in our basis

        - ``exact`` -- boolean (default: ``False``); if True, tries to embed
          ``g`` into a matrix algebra over a number field. If ``False``,
          the target is the matrix algebra over `\\QQ_p`.

        OUTPUT:

        A 2x2 matrix with coefficients in `\\QQ_p` if ``exact`` is
        False, or a number field if ``exact`` is True.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,2)
            sage: l = X.get_units_of_order()
            sage: len(l)
            12
            sage: l[3] # random
            [-1]
            [ 0]
            [ 1]
            [ 1]
            sage: u = X.embed_quaternion(l[3]); u # random
            [    O(7) 3 + O(7)]
            [2 + O(7) 6 + O(7)]
            sage: X._increase_precision(5)
            sage: v = X.embed_quaternion(l[3]); v # random
            [                7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             3 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
            [            2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6) 6 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)]
            sage: u == v
            True
        """
    embed = embed_quaternion
    def get_embedding(self, prec=None):
        """
        Return a function which embeds quaternions into a matrix
        algebra.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,3)
            sage: f = X.get_embedding(prec = 4)
            sage: b = Matrix(ZZ,4,1,[1,2,3,4])
            sage: f(b)
            [2 + 3*5 + 2*5^2 + 4*5^3 + O(5^4)       3 + 2*5^2 + 4*5^3 + O(5^4)]
            [        5 + 5^2 + 3*5^3 + O(5^4)           4 + 5 + 2*5^2 + O(5^4)]
        """
    def get_edge_stabilizers(self):
        """
        Compute the stabilizers in the arithmetic group of all
        edges in the Bruhat-Tits tree within a fundamental domain for
        the quotient graph. The stabilizers of an edge and its
        opposite are equal, and so we only store half the data.

        OUTPUT:

        A list of lists encoding edge stabilizers. It contains one
        entry for each edge. Each entry is a list of data
        corresponding to the group elements in the stabilizer of the
        edge. The data consists of: (0) a column matrix representing
        a quaternion, (1) the power of `p` that one needs to divide
        by in order to obtain a quaternion of norm 1, and hence an
        element of the arithmetic group `\\Gamma`, (2) a boolean that
        is only used to compute spaces of modular forms.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,2)
            sage: s = X.get_edge_stabilizers()
            sage: len(s) == X.get_num_ordered_edges()/2
            True
            sage: len(s[0])
            3
        """
    def get_stabilizers(self):
        """
        Compute the stabilizers in the arithmetic group of all
        edges in the Bruhat-Tits tree within a fundamental domain for
        the quotient graph. This is similar to get_edge_stabilizers, except
        that here we also store the stabilizers of the opposites.

        OUTPUT:

        A list of lists encoding edge stabilizers. It contains one
        entry for each edge. Each entry is a list of data
        corresponding to the group elements in the stabilizer of the
        edge. The data consists of: (0) a column matrix representing
        a quaternion, (1) the power of `p` that one needs to divide
        by in order to obtain a quaternion of norm 1, and hence an
        element of the arithmetic group `\\Gamma`, (2) a boolean that
        is only used to compute spaces of modular forms.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,5)
            sage: s = X.get_stabilizers()
            sage: len(s) == X.get_num_ordered_edges()
            True
            sage: gamma = X.embed_quaternion(s[1][0][0][0],prec = 20)
            sage: v = X.get_edge_list()[0].rep
            sage: X._BT.edge(gamma*v) == v
            True
        """
    def get_vertex_stabs(self):
        """
        This function computes the stabilizers in the arithmetic
        group of all vertices in the Bruhat-Tits tree within a
        fundamental domain for the quotient graph.

        OUTPUT:

        A list of vertex stabilizers. Each vertex stabilizer is a
        finite cyclic subgroup, so we return generators for these
        subgroups.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(13,2)
            sage: S = X.get_vertex_stabs()
            sage: gamma = X.embed_quaternion(S[0][0][0],prec = 20)
            sage: v = X.get_vertex_list()[0].rep
            sage: X._BT.vertex(gamma*v) == v
            True
        """
    def get_quaternion_algebra(self):
        """
        Return the underlying quaternion algebra.

        OUTPUT: the underlying definite quaternion algebra

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: X.get_quaternion_algebra()
            Quaternion Algebra (-1, -7) with base ring Rational Field
        """
    def get_eichler_order(self, magma: bool = False, force_computation: bool = False):
        """
        Return the underlying Eichler order of level `N^+`.

        OUTPUT: an Eichler order

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: X.get_eichler_order()
            Order of Quaternion Algebra (-1, -7) with base ring Rational Field with basis (1/2 + 1/2*j, 1/2*i + 1/2*k, j, k)
        """
    def get_maximal_order(self, magma: bool = False, force_computation: bool = False):
        """
        Return the underlying maximal order containing the
        Eichler order.

        OUTPUT: a maximal order

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: X.get_maximal_order()
            Order of Quaternion Algebra (-1, -7) with base ring Rational Field with basis (1/2 + 1/2*j, 1/2*i + 1/2*k, j, k)
        """
    def get_splitting_field(self):
        """
        Return a quadratic field that splits the quaternion
        algebra attached to ``self``. Currently requires Magma.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,11)
            sage: X.get_splitting_field()
            Traceback (most recent call last):
            ...
            NotImplementedError: Sage does not know yet how to work with the kind of orders that you are trying to use. Try installing Magma first and set it up so that Sage can use it.

        If we do have Magma installed, then it works::

            sage: X = BruhatTitsQuotient(5,11,use_magma=True) # optional - magma
            sage: X.get_splitting_field() # optional - magma
            Number Field in a with defining polynomial x^2 + 11
        """
    def get_eichler_order_basis(self):
        """
        Return a basis for the global Eichler order.

        OUTPUT: basis for the underlying Eichler order of level Nplus

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,11)
            sage: X.get_eichler_order_basis()
            [1/2 + 1/2*j, 1/2*i + 1/2*k, j, k]
        """
    def get_eichler_order_quadform(self):
        """
        This function return the norm form for the underlying
        Eichler order of level ``Nplus``. Required for finding elements in
        the arithmetic subgroup Gamma.

        OUTPUT: the norm form of the underlying Eichler order

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,11)
            sage: X.get_eichler_order_quadform()
            Quadratic form in 4 variables over Integer Ring with coefficients:
            [ 3 0 11 0 ]
            [ * 3 0 11 ]
            [ * * 11 0 ]
            [ * * * 11 ]
        """
    def get_eichler_order_quadmatrix(self):
        """
        This function returns the matrix of the quadratic form of
        the underlying Eichler order in the fixed basis.

        OUTPUT: a 4x4 integral matrix describing the norm form

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,11)
            sage: X.get_eichler_order_quadmatrix()
            [ 6  0 11  0]
            [ 0  6  0 11]
            [11  0 22  0]
            [ 0 11  0 22]
        """
    @cached_method
    def get_units_of_order(self):
        """
        Return the units of the underlying Eichler
        `\\ZZ`-order. This is a finite group since the order lives in a
        definite quaternion algebra over `\\QQ`.

        OUTPUT:

        A list of elements of the global Eichler `\\ZZ`-order of
        level `N^+`.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,11)
            sage: X.get_units_of_order()
            [
            [ 0]  [-2]
            [-2]  [ 0]
            [ 0]  [ 1]
            [ 1], [ 0]
            ]
        """
    def fundom_rep(self, v1):
        """
        Find an equivalent vertex in the fundamental domain.

        INPUT:

        - ``v1`` -- a 2x2 matrix representing a normalized vertex

        OUTPUT: a ``Vertex`` equivalent to ``v1``, in the fundamental domain

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,7)
            sage: M = Matrix(ZZ,2,2,[1,3,2,7])
            sage: M.set_immutable()
            sage: X.fundom_rep(M)
            Vertex of Bruhat-Tits tree for p = 3
        """
    def B_one(self):
        """
        Return the coordinates of `1` in the basis for the
        quaternion order.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,11)
            sage: v,pow = X.B_one()
            sage: X._conv(v) == 1
            True
        """
    def harmonic_cocycle_from_elliptic_curve(self, E, prec=None):
        """
        Return a harmonic cocycle with the same Hecke eigenvalues as ``E``.

        Given an elliptic curve `E` having a conductor `N` of the form `pN^-N^+`,
        return the harmonic cocycle over ``self`` which is attached to ``E`` via
        modularity. The result is only well-defined up to scaling.

        INPUT:

        - ``E`` -- an elliptic curve over the rational numbers

        - ``prec`` -- (default: ``None``) if specified, the harmonic cocycle will take values
          in `\\QQ_p` with precision ``prec``. Otherwise it will take values in `\\ZZ`.

        OUTPUT: a harmonic cocycle attached via modularity to the given elliptic curve

        EXAMPLES::

            sage: E = EllipticCurve('21a1')
            sage: X = BruhatTitsQuotient(7,3)
            sage: f = X.harmonic_cocycle_from_elliptic_curve(E,10)
            sage: T29 = f.parent().hecke_operator(29)
            sage: T29(f) == E.ap(29) * f
            True
            sage: E = EllipticCurve('51a1')
            sage: X = BruhatTitsQuotient(3,17)
            sage: f = X.harmonic_cocycle_from_elliptic_curve(E,20)
            sage: T31 = f.parent().hecke_operator(31)
            sage: T31(f) == E.ap(31) * f
            True
        """
    def harmonic_cocycles(self, k, prec=None, basis_matrix=None, base_field=None):
        """
        Compute the space of harmonic cocycles of a given even weight ``k``.

        INPUT:

        - ``k`` -- integer; the weight. It must be even.

        - ``prec`` -- integer (default: ``None``); if specified, the
          precision for the coefficient module

        - ``basis_matrix`` -- a matrix (default: ``None``)

        - ``base_field`` -- a ring (default: ``None``)

        OUTPUT: a space of harmonic cocycles

        EXAMPLES::

            sage: X = BruhatTitsQuotient(31,7)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: H
            Space of harmonic cocycles of weight 2 on Quotient of the Bruhat Tits tree of GL_2(QQ_31) with discriminant 7 and level 1
            sage: H.basis()[0]
            Harmonic cocycle with values in Sym^0 Q_31^2
        """
    def padic_automorphic_forms(self, U, prec=None, t=None, R=None, overconvergent: bool = False):
        """
        The module of (quaternionic) `p`-adic automorphic forms over ``self``.

        INPUT:

        - ``U`` -- a distributions module or an integer. If ``U`` is a
          distributions module then this creates the relevant space of
          automorphic forms. If ``U`` is an integer then the coefficients
          are the (`U-2`)nd power of the symmetric representation of
          `GL_2(\\QQ_p)`.

        - ``prec`` -- a precision (default: ``None``). if not ``None`` should
          be a positive integer

        - ``t`` -- (default: ``None``) the number of additional moments to store. If ``None``, determine
          it automatically from ``prec``, ``U`` and the ``overconvergent`` flag

        - ``R`` -- (default: ``None``) if specified, coefficient field of the automorphic forms.
          If not specified it defaults to the base ring of the distributions ``U``, or to `\\QQ_p`
          with the working precision ``prec``.

        - ``overconvergent`` -- boolean (default: ``False``); if ``True``, will construct overconvergent
          `p`-adic automorphic forms. Otherwise it constructs the finite dimensional space of
          `p`-adic automorphic forms which is isomorphic to the space of harmonic cocycles.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(11,5)
            sage: X.padic_automorphic_forms(2,prec=10)
            Space of automorphic forms on Quotient of the Bruhat Tits tree of GL_2(QQ_11) with discriminant 5 and level 1 with values in Sym^0 Q_11^2
        """
