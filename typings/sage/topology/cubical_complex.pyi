from .cell_complex import GenericCellComplex as GenericCellComplex
from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.sage_object import SageObject as SageObject

class Cube(SageObject):
    '''
    Define a cube for use in constructing a cubical complex.

    "Elementary cubes" are products of intervals with integer
    endpoints, each of which is either a unit interval or a degenerate
    (length 0) interval; for example,

    .. MATH::

       [0,1] \\times [3,4] \\times [2,2] \\times [1,2]

    is a 3-dimensional cube (since one of the intervals is degenerate)
    embedded in `\\RR^4`.

    INPUT:

    - ``data`` -- list or tuple of terms of the form ``(i,i+1)`` or
      ``(i,i)`` or ``(i,)``; the last two are degenerate intervals

    OUTPUT: an elementary cube

    Each cube is stored in a standard form: a tuple of tuples, with a
    nondegenerate interval ``[j,j]`` represented by ``(j,j)``, not
    ``(j,)``.  (This is so that for any interval ``I``, ``I[1]`` will
    produce a value, not an :exc:`IndexError`.)

    EXAMPLES::

        sage: from sage.topology.cubical_complex import Cube
        sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]]); C
        [1,2] x [5,5] x [6,7] x [-1,0]
        sage: C.dimension() # number of nondegenerate intervals
        3
        sage: C.nondegenerate_intervals()  # indices of these intervals
        [0, 2, 3]
        sage: C.face(1, upper=False)
        [1,2] x [5,5] x [6,6] x [-1,0]
        sage: C.face(1, upper=True)
        [1,2] x [5,5] x [7,7] x [-1,0]
        sage: Cube(()).dimension()  # empty cube has dimension -1
        -1
    '''
    def __init__(self, data) -> None:
        """
        Define a cube for use in constructing a cubical complex.

        See ``Cube`` for more information.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]]); C # indirect doctest
            [1,2] x [5,5] x [6,7] x [-1,0]
            sage: C == loads(dumps(C))
            True
        """
    def tuple(self):
        """
        The tuple attached to this cube.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]])
            sage: C.tuple()
            ((1, 2), (5, 5), (6, 7), (-1, 0))
        """
    def is_face(self, other):
        """
        Return ``True`` iff this cube is a face of other.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C1 = Cube([[1,2], [5,], [6,7], [-1, 0]])
            sage: C2 = Cube([[1,2], [5,], [6,], [-1, 0]])
            sage: C1.is_face(C2)
            False
            sage: C1.is_face(C1)
            True
            sage: C2.is_face(C1)
            True
        """
    def __getitem__(self, n):
        """
        Return the `n`-th interval in this cube.

        INPUT:

        - ``n`` -- integer

        OUTPUT: tuple representing the `n`-th interval in the cube

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]])
            sage: C[2]
            (6, 7)
            sage: C[1]
            (5, 5)
        """
    def __iter__(self):
        """
        Iterator for the intervals of this cube.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]])
            sage: [x[0] for x in C]
            [1, 5, 6, -1]
        """
    def __add__(self, other):
        """
        Cube obtained by concatenating the underlying tuples of the
        two arguments.

        INPUT:

        - ``other`` -- another cube

        OUTPUT: the product of ``self`` and ``other``, as a Cube

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [3,]])
            sage: D = Cube([[4], [0,1]])
            sage: C.product(D)
            [1,2] x [3,3] x [4,4] x [0,1]

        You can also use ``__add__`` or ``+`` or ``__mul__`` or ``*``::

            sage: D * C
            [4,4] x [0,1] x [1,2] x [3,3]
            sage: D + C * C
            [4,4] x [0,1] x [1,2] x [3,3] x [1,2] x [3,3]
        """
    __mul__ = __add__
    product = __add__
    def nondegenerate_intervals(self):
        """
        The list of indices of nondegenerate intervals of this cube.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]])
            sage: C.nondegenerate_intervals()
            [0, 2, 3]
            sage: C = Cube([[1,], [5,], [6,], [-1,]])
            sage: C.nondegenerate_intervals()
            []
        """
    def dimension(self):
        """
        The dimension of this cube: the number of its nondegenerate intervals.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]])
            sage: C.dimension()
            3
            sage: C = Cube([[1,], [5,], [6,], [-1,]])
            sage: C.dimension()
            0
            sage: Cube([]).dimension()  # empty cube has dimension -1
            -1
        """
    def face(self, n, upper: bool = True):
        '''
        The `n`-th primary face of this cube.

        INPUT:

        - ``n`` -- integer between 0 and one less than the dimension
          of this cube
        - ``upper`` -- boolean (default=True);if ``True``, return the "upper"
          `n`-th primary face; otherwise, return the "lower" `n`-th primary
          face

        OUTPUT: the cube obtained by replacing the `n`-th non-degenerate
        interval with either its upper or lower endpoint.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [5,], [6,7], [-1, 0]]); C
            [1,2] x [5,5] x [6,7] x [-1,0]
            sage: C.face(0)
            [2,2] x [5,5] x [6,7] x [-1,0]
            sage: C.face(0, upper=False)
            [1,1] x [5,5] x [6,7] x [-1,0]
            sage: C.face(1)
            [1,2] x [5,5] x [7,7] x [-1,0]
            sage: C.face(2, upper=False)
            [1,2] x [5,5] x [6,7] x [-1,-1]
            sage: C.face(3)
            Traceback (most recent call last):
            ...
            ValueError: can only compute the n-th face if 0 <= n < dim
        '''
    def faces(self):
        """
        The list of faces (of codimension 1) of this cube.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [3,4]])
            sage: C.faces()
            [[2,2] x [3,4], [1,2] x [4,4], [1,1] x [3,4], [1,2] x [3,3]]
        """
    def faces_as_pairs(self):
        """
        The list of faces (of codimension 1) of this cube, as pairs
        (upper, lower).

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C = Cube([[1,2], [3,4]])
            sage: C.faces_as_pairs()
            [([2,2] x [3,4], [1,1] x [3,4]), ([1,2] x [4,4], [1,2] x [3,3])]
        """
    def alexander_whitney(self, dim):
        """
        Subdivide this cube into pairs of cubes.

        This provides a cubical approximation for the diagonal map
        `K \\to K \\times K`.

        INPUT:

        - ``dim`` -- integer between 0 and one more than the
          dimension of this cube

        OUTPUT:

        - a list containing triples ``(coeff, left, right)``

        This uses the algorithm described by Pilarczyk and Réal [PR2015]_
        on p. 267; the formula is originally due to Serre.  Calling
        this method ``alexander_whitney`` is an abuse of notation,
        since the actual Alexander-Whitney map goes from `C(K \\times
        L) \\to C(K) \\otimes C(L)`, where `C(-)` denotes the associated
        chain complex, but this subdivision of cubes is at the heart
        of it.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C1 = Cube([[0,1], [3,4]])
            sage: C1.alexander_whitney(0)
            [(1, [0,0] x [3,3], [0,1] x [3,4])]
            sage: C1.alexander_whitney(1)
            [(1, [0,1] x [3,3], [1,1] x [3,4]), (-1, [0,0] x [3,4], [0,1] x [4,4])]
            sage: C1.alexander_whitney(2)
            [(1, [0,1] x [3,4], [1,1] x [4,4])]
        """
    def __eq__(self, other):
        """
        Return ``True`` iff this cube is the same as ``other``: that is,
        if they are the product of the same intervals in the same
        order.

        INPUT:

        - ``other`` -- another cube

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C1 = Cube([[1,1], [2,3], [4,5]])
            sage: C2 = Cube([[1], [2,3], [4,5]])
            sage: C3 = Cube([[0], [2,3], [4,5]])
            sage: C1 == C2  # indirect doctest
            True
            sage: C1 == C3  # indirect doctest
            False
        """
    def __ne__(self, other):
        """
        Return ``True`` iff this cube is not equal to ``other``.

        INPUT:

        - ``other`` -- another cube

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C1 = Cube([[1,1], [2,3], [4,5]])
            sage: C2 = Cube([[1], [2,3], [4,5]])
            sage: C3 = Cube([[0], [2,3], [4,5]])
            sage: C1 != C2  # indirect doctest
            False
            sage: C1 != C3  # indirect doctest
            True
        """
    def __lt__(self, other):
        """
        Return ``True`` iff the tuple for this cube is less than that for
        ``other``.

        INPUT:

        - ``other`` -- another cube

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C1 = Cube([[1,1], [2,3], [4,5]])
            sage: C2 = Cube([[1], [2,3], [4,5]])
            sage: C3 = Cube([[0], [2,3], [4,5]])
            sage: C1 < C1
            False
            sage: C1 < C3
            False
            sage: C3 < C1
            True

        Test ``@total_ordering`` by testing other comparisons::

            sage: C1 <= C1
            True
            sage: C1 <= C2
            True
            sage: C1 >= C2
            True
            sage: C1 > C2
            False
            sage: C3 <= C1
            True
            sage: C1 > C3
            True
        """
    def __hash__(self):
        """
        Hash value for this cube.  This computes the hash value of the
        underlying tuple, since this is what's important when testing
        equality.

        EXAMPLES::

            sage: from sage.topology.cubical_complex import Cube
            sage: C1 = Cube([[1,1], [2,3], [4,5]])
            sage: hash(C1) == hash(((1,1),(2,3),(4,5)))
            True
        """

class CubicalComplex(GenericCellComplex):
    '''
    Define a cubical complex.

    INPUT:

    - ``maximal_faces`` -- set of maximal faces
    - ``maximality_check`` -- boolean (default: ``True``); see below

    OUTPUT: a cubical complex

    ``maximal_faces`` should be a list or tuple or set (or anything
    which may be converted to a set) of "cubes": instances of the
    class :class:`Cube`, or lists or tuples suitable for conversion to
    cubes.  These cubes are the maximal cubes in the complex.

    In addition, ``maximal_faces`` may be a cubical complex, in which
    case that complex is returned.  Also, ``maximal_faces`` may
    instead be any object which has a ``_cubical_`` method (e.g., a
    simplicial complex); then that method is used to convert the
    object to a cubical complex.

    If ``maximality_check`` is True, check that each maximal face is,
    in fact, maximal. In this case, when producing the internal
    representation of the cubical complex, omit those that are not.
    It is highly recommended that this be True; various methods for
    this class may fail if faces which are claimed to be maximal are
    in fact not.

    EXAMPLES:

    The empty complex, consisting of one cube, the empty cube::

        sage: CubicalComplex()
        Cubical complex with 0 vertices and 1 cube

    A "circle" (four edges connecting the vertices (0,2), (0,3),
    (1,2), and (1,3))::

        sage: S1 = CubicalComplex([([0,0], [2,3]), ([0,1], [3,3]),
        ....:                      ([0,1], [2,2]), ([1,1], [2,3])]); S1
        Cubical complex with 4 vertices and 8 cubes
        sage: S1.homology()                                                             # needs sage.modules
        {0: 0, 1: Z}

    A set of five points and its product with ``S1``::

        sage: pts = CubicalComplex([([0],), ([3],), ([6],), ([-12],), ([5],)])
        sage: pts
        Cubical complex with 5 vertices and 5 cubes
        sage: pts.homology()                                                            # needs sage.modules
        {0: Z x Z x Z x Z}
        sage: X = S1.product(pts); X
        Cubical complex with 20 vertices and 40 cubes
        sage: X.homology()                                                              # needs sage.modules
        {0: Z x Z x Z x Z, 1: Z^5}

    Converting a simplicial complex to a cubical complex::

        sage: S2 = simplicial_complexes.Sphere(2)
        sage: C2 = CubicalComplex(S2)
        sage: all(C2.homology(n) == S2.homology(n) for n in range(3))                   # needs sage.modules
        True

    You can get the set of maximal cells or a dictionary of all cells::

        sage: X.maximal_cells() # random: order may depend on the version of Python
        {[0,0] x [2,3] x [-12,-12], [0,1] x [3,3] x [5,5], [0,1] x [2,2] x [3,3], [0,1] x [2,2] x [0,0], [0,1] x [3,3] x [6,6], [1,1] x [2,3] x [0,0], [0,1] x [2,2] x [-12,-12], [0,0] x [2,3] x [6,6], [1,1] x [2,3] x [-12,-12], [1,1] x [2,3] x [5,5], [0,1] x [2,2] x [5,5], [0,1] x [3,3] x [3,3], [1,1] x [2,3] x [3,3], [0,0] x [2,3] x [5,5], [0,1] x [3,3] x [0,0], [1,1] x [2,3] x [6,6], [0,1] x [2,2] x [6,6], [0,0] x [2,3] x [0,0], [0,0] x [2,3] x [3,3], [0,1] x [3,3] x [-12,-12]}
        sage: sorted(X.maximal_cells())
        [[0,0] x [2,3] x [-12,-12],
         [0,0] x [2,3] x [0,0],
         [0,0] x [2,3] x [3,3],
         [0,0] x [2,3] x [5,5],
         [0,0] x [2,3] x [6,6],
         [0,1] x [2,2] x [-12,-12],
         [0,1] x [2,2] x [0,0],
         [0,1] x [2,2] x [3,3],
         [0,1] x [2,2] x [5,5],
         [0,1] x [2,2] x [6,6],
         [0,1] x [3,3] x [-12,-12],
         [0,1] x [3,3] x [0,0],
         [0,1] x [3,3] x [3,3],
         [0,1] x [3,3] x [5,5],
         [0,1] x [3,3] x [6,6],
         [1,1] x [2,3] x [-12,-12],
         [1,1] x [2,3] x [0,0],
         [1,1] x [2,3] x [3,3],
         [1,1] x [2,3] x [5,5],
         [1,1] x [2,3] x [6,6]]
        sage: S1.cells()
        {-1: set(),
         0: {[0,0] x [2,2], [0,0] x [3,3], [1,1] x [2,2], [1,1] x [3,3]},
         1: {[0,0] x [2,3], [0,1] x [2,2], [0,1] x [3,3], [1,1] x [2,3]}}

    Chain complexes, homology, and cohomology::

        sage: T = S1.product(S1); T
        Cubical complex with 16 vertices and 64 cubes
        sage: T.chain_complex()                                                         # needs sage.modules
        Chain complex with at most 3 nonzero terms over Integer Ring
        sage: T.homology(base_ring=QQ)                                                  # needs sage.modules
        {0: Vector space of dimension 0 over Rational Field,
         1: Vector space of dimension 2 over Rational Field,
         2: Vector space of dimension 1 over Rational Field}
        sage: RP2 = cubical_complexes.RealProjectivePlane()
        sage: RP2.cohomology(dim=[1, 2], base_ring=GF(2))                               # needs sage.modules
        {1: Vector space of dimension 1 over Finite Field of size 2,
         2: Vector space of dimension 1 over Finite Field of size 2}

    Joins are not implemented::

        sage: S1.join(S1)
        Traceback (most recent call last):
        ...
        NotImplementedError: joins are not implemented for cubical complexes

    Therefore, neither are cones or suspensions.
    '''
    def __init__(self, maximal_faces=None, maximality_check: bool = True) -> None:
        """
        Define a cubical complex.  See ``CubicalComplex`` for more
        documentation.

        EXAMPLES::

            sage: X = CubicalComplex([([0,0], [2,3]), ([0,1], [3,3]), ([0,1], [2,2]), ([1,1], [2,3])]); X
            Cubical complex with 4 vertices and 8 cubes
            sage: X == loads(dumps(X))
            True
        """
    def maximal_cells(self):
        """
        The set of maximal cells (with respect to inclusion) of this
        cubical complex.

        OUTPUT: set of maximal cells

        This just returns the set of cubes used in defining the
        cubical complex, so if the complex was defined with no
        maximality checking, none is done here, either.

        EXAMPLES::

            sage: interval = cubical_complexes.Cube(1)
            sage: interval
            Cubical complex with 2 vertices and 3 cubes
            sage: interval.maximal_cells()
            {[0,1]}
            sage: interval.product(interval).maximal_cells()
            {[0,1] x [0,1]}
        """
    def __eq__(self, other):
        """
        Return ``True`` if the set of maximal cells is the same for
        ``self`` and ``other``.

        INPUT:

        - ``other`` -- another cubical complex

        EXAMPLES::

            sage: I1 = cubical_complexes.Cube(1)
            sage: I2 = cubical_complexes.Cube(1)
            sage: I1.product(I2) == I2.product(I1)
            True
            sage: I1.product(I2.product(I2)) == I2.product(I1.product(I1))
            True
            sage: S1 = cubical_complexes.Sphere(1)
            sage: I1.product(S1) == S1.product(I1)
            False
        """
    def __ne__(self, other):
        """
        Return ``True`` if ``self`` and ``other`` are not equal.

        INPUT:

        - ``other`` -- another cubical complex

        EXAMPLES::

            sage: I1 = cubical_complexes.Cube(1)
            sage: I2 = cubical_complexes.Cube(1)
            sage: I1.product(I2) != I2.product(I1)
            False
            sage: I1.product(I2.product(I2)) != I2.product(I1.product(I1))
            False
            sage: S1 = cubical_complexes.Sphere(1)
            sage: I1.product(S1) != S1.product(I1)
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: I1 = cubical_complexes.Cube(1)
            sage: I2 = cubical_complexes.Cube(1)
            sage: hash(I1) == hash(I2)
            True
            sage: hash(I1.product(I1)) == hash(I2.product(I1))
            True
        """
    def is_subcomplex(self, other):
        """
        Return ``True`` if ``self`` is a subcomplex of ``other``.

        INPUT:

        - ``other`` -- a cubical complex

        Each maximal cube of ``self`` must be a face of a maximal cube
        of ``other`` for this to be True.

        EXAMPLES::

            sage: S1 = cubical_complexes.Sphere(1)
            sage: C0 = cubical_complexes.Cube(0)
            sage: C1 = cubical_complexes.Cube(1)
            sage: cyl = S1.product(C1)
            sage: end = S1.product(C0)
            sage: end.is_subcomplex(cyl)
            True
            sage: cyl.is_subcomplex(end)
            False

        The embedding of the cubical complex is important here::

            sage: C2 = cubical_complexes.Cube(2)
            sage: C1.is_subcomplex(C2)
            False
            sage: C1.product(C0).is_subcomplex(C2)
            True

        ``C1`` is not a subcomplex of ``C2`` because it's not embedded
        in `\\RR^2`.  On the other hand, ``C1 x C0`` is a face of
        ``C2``.  Look at their maximal cells::

            sage: C1.maximal_cells()
            {[0,1]}
            sage: C2.maximal_cells()
            {[0,1] x [0,1]}
            sage: C1.product(C0).maximal_cells()
            {[0,1] x [0,0]}
        """
    def cells(self, subcomplex=None):
        """
        The cells of this cubical complex, in the form of a dictionary:
        the keys are integers, representing dimension, and the value
        associated to an integer d is the list of d-cells.

        If the optional argument ``subcomplex`` is present, then
        return only the faces which are *not* in the subcomplex.

        INPUT:

        - ``subcomplex`` -- a subcomplex of this cubical complex (default:
          ``None``)

        OUTPUT: dictionary; the cells of this complex not contained in
        ``subcomplex``

        EXAMPLES::

            sage: S2 = cubical_complexes.Sphere(2)
            sage: sorted(S2.cells()[2])
            [[0,0] x [0,1] x [0,1],
             [0,1] x [0,0] x [0,1],
             [0,1] x [0,1] x [0,0],
             [0,1] x [0,1] x [1,1],
             [0,1] x [1,1] x [0,1],
             [1,1] x [0,1] x [0,1]]
        """
    def n_cubes(self, n, subcomplex=None):
        """
        The set of cubes of dimension n of this cubical complex.
        If the optional argument ``subcomplex`` is present, then
        return the ``n``-dimensional cubes which are *not* in the
        subcomplex.

        INPUT:

        - ``n`` -- integer; dimension
        - ``subcomplex`` -- a subcomplex of this cubical complex (default:
          ``None``)

        OUTPUT: set; cells in dimension ``n``

        EXAMPLES::

            sage: C = cubical_complexes.Cube(3)
            sage: C.n_cubes(3)
            {[0,1] x [0,1] x [0,1]}
            sage: sorted(C.n_cubes(2))
            [[0,0] x [0,1] x [0,1],
             [0,1] x [0,0] x [0,1],
             [0,1] x [0,1] x [0,0],
             [0,1] x [0,1] x [1,1],
             [0,1] x [1,1] x [0,1],
             [1,1] x [0,1] x [0,1]]
        """
    def chain_complex(self, subcomplex=None, augmented: bool = False, verbose: bool = False, check: bool = False, dimensions=None, base_ring=..., cochain: bool = False):
        """
        The chain complex associated to this cubical complex.

        INPUT:

        - ``dimensions`` -- if ``None``, compute the chain complex in all
          dimensions.  If a list or tuple of integers, compute the
          chain complex in those dimensions, setting the chain groups
          in all other dimensions to zero.  NOT IMPLEMENTED YET: this
          function always returns the entire chain complex
        - ``base_ring`` -- commutative ring (default: ZZ)
        - ``subcomplex`` -- a subcomplex of this cubical complex (default: empty).
          Compute the chain complex relative to this subcomplex.
        - ``augmented`` -- boolean (default: ``False``); if ``True``, return
          the augmented chain complex (that is, include a class in dimension
          `-1` corresponding to the empty cell).  This is ignored if
          ``dimensions`` is specified.
        - ``cochain`` -- boolean (default: ``False``); if ``True``, return the
          cochain complex (that is, the dual of the chain complex).
        - ``verbose`` -- boolean (default: ``False``); if ``True``, print some
          messages as the chain complex is computed.
        - ``check`` -- boolean (default: ``False``); if ``True``, make sure
          that the chain complex is actually a chain complex: the differentials
          are composable and their product is zero.

        .. NOTE::

           If subcomplex is nonempty, then the argument ``augmented``
           has no effect: the chain complex relative to a nonempty
           subcomplex is zero in dimension `-1`.

        EXAMPLES::

            sage: # needs sage.modules
            sage: S2 = cubical_complexes.Sphere(2)
            sage: S2.chain_complex()
            Chain complex with at most 3 nonzero terms over Integer Ring
            sage: Prod = S2.product(S2); Prod
            Cubical complex with 64 vertices and 676 cubes
            sage: Prod.chain_complex()
            Chain complex with at most 5 nonzero terms over Integer Ring
            sage: Prod.chain_complex(base_ring=QQ)
            Chain complex with at most 5 nonzero terms over Rational Field
            sage: C1 = cubical_complexes.Cube(1)
            sage: S0 = cubical_complexes.Sphere(0)
            sage: C1.chain_complex(subcomplex=S0)
            Chain complex with at most 1 nonzero terms over Integer Ring
            sage: C1.homology(subcomplex=S0)
            {0: 0, 1: Z}

        Check that :issue:`32203` has been fixed::

            sage: # needs sage.modules
            sage: Square = CubicalComplex([([0,1],[0,1])])
            sage: EdgesLTR = CubicalComplex([([0,0],[0,1]),([0,1],[1,1]),([1,1],[0,1])])
            sage: EdgesLBR = CubicalComplex([([0,0],[0,1]),([0,1],[0,0]),([1,1],[0,1])])
            sage: Square.homology(subcomplex=EdgesLTR)[2] == Square.homology(subcomplex=EdgesLBR)[2]
            True
        """
    def alexander_whitney(self, cube, dim_left):
        """
        Subdivide ``cube`` in this cubical complex into pairs of cubes.

        See :meth:`Cube.alexander_whitney` for more details. This
        method just calls that one.

        INPUT:

        - ``cube`` -- a cube in this cubical complex
        - ``dim`` -- integer between 0 and one more than the
          dimension of this cube

        OUTPUT: list containing triples ``(coeff, left, right)``

        EXAMPLES::

            sage: C = cubical_complexes.Cube(3)
            sage: c = list(C.n_cubes(3))[0]; c
            [0,1] x [0,1] x [0,1]
            sage: C.alexander_whitney(c, 1)
            [(1, [0,1] x [0,0] x [0,0], [1,1] x [0,1] x [0,1]),
             (-1, [0,0] x [0,1] x [0,0], [0,1] x [1,1] x [0,1]),
             (1, [0,0] x [0,0] x [0,1], [0,1] x [0,1] x [1,1])]
        """
    def n_skeleton(self, n):
        """
        The n-skeleton of this cubical complex.

        INPUT:

        - ``n`` -- nonnegative integer; dimension

        OUTPUT: cubical complex

        EXAMPLES::

            sage: S2 = cubical_complexes.Sphere(2)
            sage: C3 = cubical_complexes.Cube(3)
            sage: S2 == C3.n_skeleton(2)
            True
        """
    def graph(self):
        """
        The 1-skeleton of this cubical complex, as a graph.

        EXAMPLES::

            sage: cubical_complexes.Sphere(2).graph()
            Graph on 8 vertices
        """
    def is_pure(self):
        """
        Return ``True`` iff this cubical complex is pure: that is,
        all of its maximal faces have the same dimension.

        .. WARNING::

           This may give the wrong answer if the cubical complex
           was constructed with ``maximality_check`` set to False.

        EXAMPLES::

            sage: S4 = cubical_complexes.Sphere(4)
            sage: S4.is_pure()
            True
            sage: C = CubicalComplex([([0,0], [3,3]), ([1,2], [4,5])])
            sage: C.is_pure()
            False
        """
    def join(self, other) -> None:
        """
        The join of this cubical complex with another one.

        NOT IMPLEMENTED.

        INPUT:

        - ``other`` -- another cubical complex

        EXAMPLES::

            sage: C1 = cubical_complexes.Cube(1)
            sage: C1.join(C1)
            Traceback (most recent call last):
            ...
            NotImplementedError: joins are not implemented for cubical complexes
        """
    def cone(self) -> None:
        """
        The cone on this cubical complex.

        NOT IMPLEMENTED

        The cone is the complex formed by taking the join of the
        original complex with a one-point complex (that is, a
        0-dimensional cube).  Since joins are not implemented for
        cubical complexes, neither are cones.

        EXAMPLES::

            sage: C1 = cubical_complexes.Cube(1)
            sage: C1.cone()
            Traceback (most recent call last):
            ...
            NotImplementedError: cones are not implemented for cubical complexes
        """
    def suspension(self, n: int = 1) -> None:
        """
        The suspension of this cubical complex.

        NOT IMPLEMENTED

        INPUT:

        - ``n`` -- positive integer (default: 1); suspend this many times

        The suspension is the complex formed by taking the join of the
        original complex with a two-point complex (the 0-sphere).
        Since joins are not implemented for cubical complexes, neither
        are suspensions.

        EXAMPLES::

            sage: C1 = cubical_complexes.Cube(1)
            sage: C1.suspension()
            Traceback (most recent call last):
            ...
            NotImplementedError: suspensions are not implemented for cubical complexes
        """
    def product(self, other):
        """
        Return the product of this cubical complex with another one.

        INPUT:

        - ``other`` -- another cubical complex

        EXAMPLES::

            sage: RP2 = cubical_complexes.RealProjectivePlane()
            sage: S1 = cubical_complexes.Sphere(1)
            sage: RP2.product(S1).homology()[1] # long time: 5 seconds
            Z x C2
        """
    def disjoint_union(self, other):
        """
        The disjoint union of this cubical complex with another one.

        INPUT:

        - ``right`` -- the other cubical complex (the right-hand factor)

        Algorithm: first embed both complexes in d-dimensional
        Euclidean space.  Then embed in (1+d)-dimensional space,
        calling the new axis `x`, and putting the first complex at
        `x=0`, the second at `x=1`.

        EXAMPLES::

            sage: S1 = cubical_complexes.Sphere(1)
            sage: S2 = cubical_complexes.Sphere(2)
            sage: S1.disjoint_union(S2).homology()                                      # needs sage.modules
            {0: Z, 1: Z, 2: Z}
        """
    def wedge(self, other):
        """
        The wedge (one-point union) of this cubical complex with
        another one.

        INPUT:

        - ``right`` -- the other cubical complex (the right-hand factor)

        Algorithm: if ``self`` is embedded in `d` dimensions and
        ``other`` in `n` dimensions, embed them in `d+n` dimensions:
        ``self`` using the first `d` coordinates, ``other`` using the
        last `n`, translating them so that they have the origin as a
        common vertex.

        .. NOTE::

            This operation is not well-defined if ``self`` or
            ``other`` is not path-connected.

        EXAMPLES::

            sage: S1 = cubical_complexes.Sphere(1)
            sage: S2 = cubical_complexes.Sphere(2)
            sage: S1.wedge(S2).homology()                                               # needs sage.modules
            {0: 0, 1: Z, 2: Z}
        """
    def connected_sum(self, other):
        """
        Return the connected sum of ``self`` with ``other``.

        INPUT:

        - ``other`` -- another cubical complex

        OUTPUT: the connected sum ``self # other``

        .. warning::

           This does not check that ``self`` and ``other`` are manifolds, only
           that their facets all have the same dimension.  Since a
           (more or less) random facet is chosen from each complex and
           then glued together, this method may return random
           results if applied to non-manifolds, depending on which
           facet is chosen.

        EXAMPLES::

            sage: T = cubical_complexes.Torus()
            sage: S2 = cubical_complexes.Sphere(2)
            sage: T.connected_sum(S2).cohomology() == T.cohomology()                    # needs sage.modules
            True
            sage: RP2 = cubical_complexes.RealProjectivePlane()
            sage: T.connected_sum(RP2).homology(1)                                      # needs sage.modules
            Z x Z x C2
            sage: RP2.connected_sum(RP2).connected_sum(RP2).homology(1)                 # needs sage.modules
            Z x Z x C2
        """
    @cached_method
    def algebraic_topological_model(self, base_ring=None):
        '''
        Algebraic topological model for this cubical complex with
        coefficients in ``base_ring``.

        The term "algebraic topological model" is defined by Pilarczyk
        and Réal [PR2015]_.

        INPUT:

        - ``base_ring`` -- coefficient ring (default: ``QQ``); must be a field

        Denote by `C` the chain complex associated to this cubical
        complex. The algebraic topological model is a chain complex
        `M` with zero differential, with the same homology as `C`,
        along with chain maps `\\pi: C \\to M` and `\\iota: M \\to C`
        satisfying `\\iota \\pi = 1_M` and `\\pi \\iota` chain homotopic
        to `1_C`. The chain homotopy `\\phi` must satisfy

        - `\\phi \\phi = 0`,
        - `\\pi \\phi = 0`,
        - `\\phi \\iota = 0`.

        Such a chain homotopy is called a *chain contraction*.

        OUTPUT: a pair consisting of

        - chain contraction ``phi`` associated to `C`, `M`, `\\pi`, and
          `\\iota`
        - the chain complex `M`

        Note that from the chain contraction ``phi``, one can recover the
        chain maps `\\pi` and `\\iota` via ``phi.pi()`` and
        ``phi.iota()``. Then one can recover `C` and `M` from, for
        example, ``phi.pi().domain()`` and ``phi.pi().codomain()``,
        respectively.

        EXAMPLES::

            sage: # needs sage.modules
            sage: RP2 = cubical_complexes.RealProjectivePlane()
            sage: phi, M = RP2.algebraic_topological_model(GF(2))
            sage: M.homology()
            {0: Vector space of dimension 1 over Finite Field of size 2,
             1: Vector space of dimension 1 over Finite Field of size 2,
             2: Vector space of dimension 1 over Finite Field of size 2}
            sage: T = cubical_complexes.Torus()
            sage: phi, M = T.algebraic_topological_model(QQ)
            sage: M.homology()
            {0: Vector space of dimension 1 over Rational Field,
             1: Vector space of dimension 2 over Rational Field,
             2: Vector space of dimension 1 over Rational Field}
        '''

class CubicalComplexExamples:
    '''
    Some examples of cubical complexes.

    Here are the available examples; you can also type
    "cubical_complexes."  and hit TAB to get a list::

        Sphere
        Torus
        RealProjectivePlane
        KleinBottle
        SurfaceOfGenus
        Cube

    EXAMPLES::

        sage: cubical_complexes.Torus()  # indirect doctest
        Cubical complex with 16 vertices and 64 cubes
        sage: cubical_complexes.Cube(7)
        Cubical complex with 128 vertices and 2187 cubes
        sage: cubical_complexes.Sphere(7)
        Cubical complex with 256 vertices and 6560 cubes
    '''
    def Sphere(self, n):
        """
        A cubical complex representation of the `n`-dimensional sphere,
        formed by taking the boundary of an `(n+1)`-dimensional cube.

        INPUT:

        - ``n`` -- nonnegative integer; the dimension of the sphere

        EXAMPLES::

            sage: cubical_complexes.Sphere(7)
            Cubical complex with 256 vertices and 6560 cubes
        """
    def Torus(self):
        """
        A cubical complex representation of the torus, obtained by
        taking the product of the circle with itself.

        EXAMPLES::

            sage: cubical_complexes.Torus()
            Cubical complex with 16 vertices and 64 cubes
        """
    def RealProjectivePlane(self):
        """
        A cubical complex representation of the real projective plane.
        This is taken from the examples from CHomP, the Computational
        Homology Project: http://chomp.rutgers.edu/.

        EXAMPLES::

            sage: cubical_complexes.RealProjectivePlane()
            Cubical complex with 21 vertices and 81 cubes
        """
    def KleinBottle(self):
        """
        A cubical complex representation of the Klein bottle, formed
        by taking the connected sum of the real projective plane with
        itself.

        EXAMPLES::

            sage: cubical_complexes.KleinBottle()
            Cubical complex with 42 vertices and 168 cubes
        """
    def SurfaceOfGenus(self, g, orientable: bool = True):
        """
        A surface of genus `g` as a cubical complex.

        INPUT:

        - ``g`` -- nonnegative integer; the genus
        - ``orientable`` -- boolean (default: ``True``); whether the surface
          should be orientable

        In the orientable case, return a sphere if `g` is zero, and
        otherwise return a `g`-fold connected sum of a torus with
        itself.

        In the non-orientable case, raise an error if `g` is zero.  If
        `g` is positive, return a `g`-fold connected sum of a
        real projective plane with itself.

        EXAMPLES::

            sage: cubical_complexes.SurfaceOfGenus(2)
            Cubical complex with 32 vertices and 134 cubes
            sage: cubical_complexes.SurfaceOfGenus(1, orientable=False)
            Cubical complex with 21 vertices and 81 cubes
        """
    def Cube(self, n):
        """
        A cubical complex representation of an `n`-dimensional cube.

        INPUT:

        - ``n`` -- nonnegative integer; the dimension

        EXAMPLES::

            sage: cubical_complexes.Cube(0)
            Cubical complex with 1 vertex and 1 cube
            sage: cubical_complexes.Cube(3)
            Cubical complex with 8 vertices and 27 cubes
        """

cubical_complexes: Incomplete
