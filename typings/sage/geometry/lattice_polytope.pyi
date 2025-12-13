import sage.geometry.abc
from _typeshed import Incomplete
from collections.abc import Hashable
from sage.features import PythonModule as PythonModule
from sage.features.databases import DatabaseReflexivePolytopes as DatabaseReflexivePolytopes
from sage.features.palp import PalpExecutable as PalpExecutable
from sage.geometry.cone import integral_length as integral_length
from sage.geometry.convex_set import ConvexSet_compact as ConvexSet_compact
from sage.geometry.point_collection import PointCollection as PointCollection, read_palp_point_collection as read_palp_point_collection
from sage.geometry.toric_lattice import ToricLattice as ToricLattice, ToricLattice_generic as ToricLattice_generic
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set_generic as Set_generic
from sage.structure.all import Sequence as Sequence
from sage.structure.element import Matrix as Matrix
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class SetOfAllLatticePolytopesClass(Set_generic):
    def __call__(self, x):
        """
        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: lattice_polytope.SetOfAllLatticePolytopesClass().__call__(o)
            3-d reflexive polytope in 3-d lattice M
        """

SetOfAllLatticePolytopes: Incomplete

def LatticePolytope(data, compute_vertices: bool = True, n: int = 0, lattice=None):
    """
    Construct a lattice polytope.

    INPUT:

    - ``data`` -- points spanning the lattice polytope, specified as one of:

        * a :class:`point collection
          <sage.geometry.point_collection.PointCollection>` (this is the
          preferred input and it is the quickest and the most memory efficient
          one);

        * an iterable of iterables (for example, a list of vectors)
          defining the point coordinates;

        * a file with matrix data, opened for reading, or

        * a filename of such a file, see
          :func:`~sage.geometry.point_collection.read_palp_point_collection`
          for the file format;

    - ``compute_vertices`` -- boolean (default: ``True``); if ``True``, the
      convex hull of the given points will be computed for determining
      vertices. Otherwise, the given points must be vertices.

    - ``n`` -- integer (default: 0); if ``data`` is a name of a file,
      that contains data blocks for several polytopes, the ``n``-th block
      will be used

    - ``lattice`` -- the ambient lattice of the polytope. If not given, a
      suitable lattice will be determined automatically, most likely the
      :class:`toric lattice <sage.geometry.toric_lattice.ToricLatticeFactory>`
      `M` of the appropriate dimension.

    OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

    EXAMPLES::

        sage: points = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
        sage: p = LatticePolytope(points)
        sage: p
        3-d reflexive polytope in 3-d lattice M
        sage: p.vertices()
        M( 1,  0,  0),
        M( 0,  1,  0),
        M( 0,  0,  1),
        M(-1,  0,  0),
        M( 0, -1,  0),
        M( 0,  0, -1)
        in 3-d lattice M

    We draw a pretty picture of the polytope in 3-dimensional space::

        sage: p.plot3d().show()                                                         # needs palp sage.plot

    Now we add an extra point, which is in the interior of the
    polytope...

    ::

        sage: points.append((0,0,0))
        sage: p = LatticePolytope(points)
        sage: p.nvertices()
        6

    You can suppress vertex computation for speed but this can lead to
    mistakes::

        sage: p = LatticePolytope(points, compute_vertices=False)
        ...
        sage: p.nvertices()
        7

    Given points must be in the lattice::

        sage: LatticePolytope([[1/2], [3/2]])
        Traceback (most recent call last):
        ...
        ValueError: points
        [[1/2], [3/2]]
        are not in 1-d lattice M!

    But it is OK to create polytopes of non-maximal dimension::


        sage: p = LatticePolytope([(1,0,0), (0,1,0), (0,0,0),
        ....:       (-1,0,0), (0,-1,0), (0,0,0), (0,0,0)])
        sage: p
        2-d lattice polytope in 3-d lattice M
        sage: p.vertices()
        M(-1,  0, 0),
        M( 0, -1, 0),
        M( 1,  0, 0),
        M( 0,  1, 0)
        in 3-d lattice M

    An empty lattice polytope can be considered as well::

        sage: p = LatticePolytope([], lattice=ToricLattice(3).dual()); p
        -1-d lattice polytope in 3-d lattice M
        sage: p.lattice_dim()
        3
        sage: p.npoints()
        0
        sage: p.nfacets()
        0
        sage: p.points()
        Empty collection
        in 3-d lattice M
        sage: p.faces()                                                                 # needs sage.graphs
        ((-1-d lattice polytope in 3-d lattice M,),)
    """
def ReflexivePolytope(dim, n):
    '''
    Return the `n`-th 2- or 3-dimensional reflexive polytope.

    .. NOTE::

        #. Numeration starts with zero: `0 \\leq n \\leq 15` for `{\\rm dim} = 2`
           and `0 \\leq n \\leq 4318` for `{\\rm dim} = 3`.

        #. During the first call, all reflexive polytopes of requested
           dimension are loaded and cached for future use, so the first
           call for 3-dimensional polytopes can take several seconds,
           but all consecutive calls are fast.

        #. Equivalent to ``ReflexivePolytopes(dim)[n]`` but checks bounds
           first.

    EXAMPLES:

    The 3rd 2-dimensional polytope is "the diamond"::

        sage: ReflexivePolytope(2, 3)
        2-d reflexive polytope #3 in 2-d lattice M
        sage: lattice_polytope.ReflexivePolytope(2,3).vertices()
        M( 1,  0),
        M( 0,  1),
        M( 0, -1),
        M(-1,  0)
        in 2-d lattice M

    There are 16 reflexive polygons and numeration starts with 0::

        sage: ReflexivePolytope(2,16)
        Traceback (most recent call last):
        ...
        ValueError: there are only 16 reflexive polygons!

    It is not possible to load a 4-dimensional polytope in this way::

        sage: ReflexivePolytope(4,16)
        Traceback (most recent call last):
        ...
        NotImplementedError: only 2- and 3-dimensional reflexive polytopes are available!
    '''
def ReflexivePolytopes(dim):
    """
    Return the sequence of all 2- or 3-dimensional reflexive polytopes.

    .. NOTE::

        During the first call the database is loaded and cached for
        future use, so repetitive calls will return the same object in
        memory.

    INPUT:

    - ``dim`` -- integer (2 or 3); dimension of required reflexive polytopes

    OUTPUT: list of lattice polytopes

    EXAMPLES:

    There are 16 reflexive polygons::

        sage: len(ReflexivePolytopes(2))
        16

    It is not possible to load 4-dimensional polytopes in this way::

        sage: ReflexivePolytopes(4)
        Traceback (most recent call last):
        ...
        NotImplementedError: only 2- and 3-dimensional reflexive polytopes are available!
    """
def is_LatticePolytope(x):
    """
    Check if ``x`` is a lattice polytope.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    - ``True`` if ``x`` is a :class:`lattice polytope <LatticePolytopeClass>`,
      ``False`` otherwise.

    EXAMPLES::

        sage: from sage.geometry.lattice_polytope import is_LatticePolytope
        sage: is_LatticePolytope(1)
        doctest:warning...
        DeprecationWarning: is_LatticePolytope is deprecated, use isinstance instead
        See https://github.com/sagemath/sage/issues/34307 for details.
        False
        sage: p = LatticePolytope([(1,0), (0,1), (-1,-1)])
        sage: p                                                                         # needs palp
        2-d reflexive polytope #0 in 2-d lattice M
        sage: is_LatticePolytope(p)
        True
    """

class LatticePolytopeClass(ConvexSet_compact, Hashable, sage.geometry.abc.LatticePolytope):
    """
    Create a lattice polytope.

    .. WARNING::

        This class does not perform any checks of correctness of input nor
        does it convert input into the standard representation. Use
        :func:`LatticePolytope` to construct lattice polytopes.

    Lattice polytopes are immutable, but they cache most of the returned values.

    INPUT:

    The input can be either:

    - ``points`` -- :class:`~sage.geometry.point_collection.PointCollection`

    - ``compute_vertices`` -- boolean

    or (these parameters must be given as keywords):

    - ``ambient`` -- ambient structure, this polytope *must be a face of*
      ``ambient``

    - ``ambient_vertex_indices`` -- increasing list or tuple of integers,
      indices of vertices of ``ambient`` generating this polytope

    - ``ambient_facet_indices`` -- increasing list or tuple of integers,
      indices of facets of ``ambient`` generating this polytope

    OUTPUT: lattice polytope

    .. NOTE::

        Every polytope has an ambient structure. If it was not specified, it is
        this polytope itself.
    """
    def __init__(self, points=None, compute_vertices=None, ambient=None, ambient_vertex_indices=None, ambient_facet_indices=None) -> None:
        """
        Construct a lattice polytope.

        See :func:`LatticePolytope` for documentation.

        TESTS::

            sage: LatticePolytope([(1,2,3), (4,5,6)]) # indirect test
            1-d lattice polytope in 3-d lattice M
            sage: TestSuite(_).run()
        """
    def __contains__(self, point) -> bool:
        """
        Check if ``point`` is contained in ``self``.

        See :meth:`_contains` (which is called by this function) for
        documentation.

        TESTS::

            sage: p = lattice_polytope.cross_polytope(2)
            sage: (1,0) in p
            True
            sage: [1,0] in p
            True
            sage: (-2,0) in p
            False
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` with ``other``.

        INPUT:

        - ``other`` -- anything

        .. NOTE::

            Two lattice polytopes are equal if they have the same vertices
            listed in the same order.

        TESTS::

            sage: p1 = LatticePolytope([(1,0), (0,1), (-1,-1)])
            sage: p2 = LatticePolytope([(1,0), (0,1), (-1,-1)])
            sage: p3 = LatticePolytope([(0,1), (1,0), (-1,-1)])
            sage: p1 == p1
            True
            sage: p1 == p2
            True
            sage: p1 is p2
            False
            sage: p1 == p3
            False
            sage: p1 == 0
            False
            sage: p1 < p2
            False
            sage: p2 < p1
            False
            sage: p1 < p3
            False
            sage: p3 < p1
            True
            sage: p1 <= p2
            True
            sage: p2 <= p1
            True
            sage: p1 <= p3
            False
            sage: p3 <= p1
            True
            sage: p1 > p2
            False
            sage: p2 > p1
            False
            sage: p1 > p3
            True
            sage: p3 > p1
            False
            sage: p1 >= p2
            True
            sage: p2 >= p1
            True
            sage: p1 >= p3
            True
            sage: p3 >= p1
            False
        """
    @cached_method
    def __hash__(self):
        """
        Return the hash of ``self``.

        OUTPUT: integer

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: hash(o) == hash(o)
            True
        """
    def __reduce__(self):
        """
        Reduction function. Does not store data that can be relatively fast
        recomputed.

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.vertices() == loads(o.dumps()).vertices()
            True
        """
    @cached_method
    def adjacent(self):
        """
        Return faces adjacent to ``self`` in the ambient face lattice.

        Two *distinct* faces `F_1` and `F_2` of the same face lattice are
        **adjacent** if all of the following conditions hold:

        * `F_1` and `F_2` have the same dimension `d`;

        * `F_1` and `F_2` share a facet of dimension `d-1`;

        * `F_1` and `F_2` are facets of some face of dimension `d+1`, unless
          `d` is the dimension of the ambient structure.

        OUTPUT: :class:`tuple` of :class:`lattice polytopes <LatticePolytopeClass>`

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.adjacent()                                                          # needs sage.graphs
            ()
            sage: face = o.faces(1)[0]                                                  # needs sage.graphs
            sage: face.adjacent()                                                       # needs sage.graphs
            (1-d face of 3-d reflexive polytope in 3-d lattice M,
             1-d face of 3-d reflexive polytope in 3-d lattice M,
             1-d face of 3-d reflexive polytope in 3-d lattice M,
             1-d face of 3-d reflexive polytope in 3-d lattice M)
        """
    def affine_transform(self, a: int = 1, b: int = 0):
        """
        Return a*P+b, where P is this lattice polytope.

        .. NOTE::

            #. While ``a`` and ``b`` may be rational, the final result
               must be a lattice polytope, i.e. all vertices must be integral.

            #. If the transform (restricted to this polytope) is
               bijective, facial structure will be preserved, e.g. the
               first facet of the image will be spanned by the images
               of vertices which span the first facet of the original
               polytope.

        INPUT:

        - ``a`` -- (default: 1) rational scalar or matrix

        - ``b`` -- (default: 0) rational scalar or vector, scalars are
          interpreted as vectors with the same components

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(2)
            sage: o.vertices()
            M( 1,  0),
            M( 0,  1),
            M(-1,  0),
            M( 0, -1)
            in 2-d lattice M
            sage: o.affine_transform(2).vertices()
            M( 2,  0),
            M( 0,  2),
            M(-2,  0),
            M( 0, -2)
            in 2-d lattice M
            sage: o.affine_transform(1,1).vertices()
            M(2, 1),
            M(1, 2),
            M(0, 1),
            M(1, 0)
            in 2-d lattice M
            sage: o.affine_transform(b=1).vertices()
            M(2, 1),
            M(1, 2),
            M(0, 1),
            M(1, 0)
            in 2-d lattice M
            sage: o.affine_transform(b=(1, 0)).vertices()
            M(2,  0),
            M(1,  1),
            M(0,  0),
            M(1, -1)
            in 2-d lattice M
            sage: a = matrix(QQ, 2, [1/2, 0, 0, 3/2])
            sage: o.polar().vertices()
            N( 1,  1),
            N( 1, -1),
            N(-1, -1),
            N(-1,  1)
            in 2-d lattice N
            sage: o.polar().affine_transform(a, (1/2, -1/2)).vertices()
            M(1,  1),
            M(1, -2),
            M(0, -2),
            M(0,  1)
            in 2-d lattice M

        While you can use rational transformation, the result must be integer::

            sage: o.affine_transform(a)
            Traceback (most recent call last):
            ...
            ValueError: points
            [(1/2, 0), (0, 3/2), (-1/2, 0), (0, -3/2)]
            are not in 2-d lattice M!
        """
    linear_transformation = affine_transform
    def ambient(self):
        """
        Return the ambient structure of ``self``.

        OUTPUT: lattice polytope containing ``self`` as a face

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.ambient()
            3-d reflexive polytope in 3-d lattice M
            sage: o.ambient() is o
            True

            sage: # needs sage.graphs
            sage: face = o.faces(1)[0]
            sage: face
            1-d face of 3-d reflexive polytope in 3-d lattice M
            sage: face.ambient()
            3-d reflexive polytope in 3-d lattice M
            sage: face.ambient() is o
            True
        """
    def ambient_facet_indices(self):
        """
        Return indices of facets of the ambient polytope containing ``self``.

        OUTPUT: increasing :class:`tuple` of integers

        EXAMPLES:

        The polytope itself is not contained in any of its facets::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.ambient_facet_indices()
            ()

        But each of its other faces is contained in one or more facets::

            sage: # needs sage.graphs
            sage: face = o.faces(1)[0]
            sage: face.ambient_facet_indices()
            (4, 5)
            sage: face.vertices()
            M(1, 0, 0),
            M(0, 1, 0)
            in 3-d lattice M
            sage: o.facets()[face.ambient_facet_indices()[0]].vertices()
            M(1, 0,  0),
            M(0, 1,  0),
            M(0, 0, -1)
            in 3-d lattice M
        """
    @cached_method
    def ambient_point_indices(self):
        """
        Return indices of points of the ambient polytope contained in this one.

        OUTPUT:

        - :class:`tuple` of integers, the order corresponds to the order of
          points of this polytope.

        EXAMPLES::

            sage: cube = lattice_polytope.cross_polytope(3).polar()
            sage: face = cube.facets()[0]                                               # needs sage.graphs
            sage: face.ambient_point_indices()                                          # needs palp sage.graphs
            (4, 5, 6, 7, 8, 9, 10, 11, 12)
            sage: cube.points(face.ambient_point_indices()) == face.points()            # needs palp sage.graphs
            True
        """
    @cached_method
    def ambient_ordered_point_indices(self):
        """
        Return indices of points of the ambient polytope contained in this one.

        OUTPUT:

        - :class:`tuple` of integers such that ambient points in this order are
          geometrically ordered, e.g. for an edge points will appear from one
          end point to the other.

        EXAMPLES::

            sage: cube = lattice_polytope.cross_polytope(3).polar()
            sage: face = cube.facets()[0]                                               # needs sage.graphs
            sage: face.ambient_ordered_point_indices()                                  # needs palp sage.graphs
            (5, 8, 4, 9, 10, 11, 6, 12, 7)
            sage: cube.points(face.ambient_ordered_point_indices())                     # needs palp sage.graphs
            N(-1, -1, -1),
            N(-1, -1,  0),
            N(-1, -1,  1),
            N(-1,  0, -1),
            N(-1,  0,  0),
            N(-1,  0,  1),
            N(-1,  1, -1),
            N(-1,  1,  0),
            N(-1,  1,  1)
            in 3-d lattice N
        """
    def ambient_vertex_indices(self):
        """
        Return indices of vertices of the ambient structure generating ``self``.

        OUTPUT: increasing :class:`tuple` of integers

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.ambient_vertex_indices()
            (0, 1, 2, 3, 4, 5)
            sage: face = o.faces(1)[0]                                                  # needs sage.graphs
            sage: face.ambient_vertex_indices()                                         # needs sage.graphs
            (0, 1)
        """
    @cached_method
    def boundary_point_indices(self):
        """
        Return indices of (relative) boundary lattice points of this polytope.

        OUTPUT: increasing :class:`tuple` of integers

        EXAMPLES:

        All points but the origin are on the boundary of this square::

            sage: square = lattice_polytope.cross_polytope(2).polar()
            sage: square.points()                                                       # needs palp
            N( 1,  1),
            N( 1, -1),
            N(-1, -1),
            N(-1,  1),
            N(-1,  0),
            N( 0, -1),
            N( 0,  0),
            N( 0,  1),
            N( 1,  0)
            in 2-d lattice N
            sage: square.boundary_point_indices()                                       # needs palp
            (0, 1, 2, 3, 4, 5, 7, 8)

        For an edge the boundary is formed by the end points::

            sage: face = square.edges()[0]                                              # needs sage.graphs
            sage: face.points()                                                         # needs sage.graphs
            N(-1, -1),
            N(-1,  1),
            N(-1,  0)
            in 2-d lattice N
            sage: face.boundary_point_indices()                                         # needs sage.graphs
            (0, 1)
        """
    def boundary_points(self):
        """
        Return (relative) boundary lattice points of this polytope.

        OUTPUT: a :class:`point collection <PointCollection>`

        EXAMPLES:

        All points but the origin are on the boundary of this square::

            sage: square = lattice_polytope.cross_polytope(2).polar()
            sage: square.boundary_points()                                              # needs palp
            N( 1,  1),
            N( 1, -1),
            N(-1, -1),
            N(-1,  1),
            N(-1,  0),
            N( 0, -1),
            N( 0,  1),
            N( 1,  0)
            in 2-d lattice N

        For an edge the boundary is formed by the end points::

            sage: face = square.edges()[0]                                              # needs sage.graphs
            sage: face.boundary_points()                                                # needs sage.graphs
            N(-1, -1),
            N(-1,  1)
            in 2-d lattice N
        """
    def contains(self, *args):
        """
        Check if a given point is contained in ``self``.

        INPUT:

        - an attempt will be made to convert all arguments into a
          single element of the ambient space of ``self``; if it fails,
          ``False`` will be returned

        OUTPUT:

        - ``True`` if the given point is contained in ``self``, ``False``
          otherwise

        EXAMPLES::

            sage: p = lattice_polytope.cross_polytope(2)
            sage: p.contains(p.lattice()(1,0))
            True
            sage: p.contains((1,0))
            True
            sage: p.contains(1,0)
            True
            sage: p.contains((2,0))
            False
        """
    @cached_method
    def dim(self):
        """
        Return the dimension of this polytope.

        EXAMPLES:

        We create a 3-dimensional octahedron and check its dimension::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.dim()
            3

        Now we create a 2-dimensional diamond in a 3-dimensional space::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.dim()
            2
            sage: p.lattice_dim()
            3
        """
    def distances(self, point=None):
        """
        Return the matrix of distances for this polytope or distances for
        the given point.

        The matrix of distances m gives distances m[i,j] between the `i`-th
        facet (which is also the `i`-th vertex of the polar polytope in the
        reflexive case) and `j`-th point of this polytope.

        If point is specified, integral distances from the point to all
        facets of this polytope will be computed.

        EXAMPLES: The matrix of distances for a 3-dimensional octahedron::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.distances()                                                         # needs palp
            [2 0 0 0 2 2 1]
            [2 2 0 0 0 2 1]
            [2 2 2 0 0 0 1]
            [2 0 2 0 2 0 1]
            [0 0 2 2 2 0 1]
            [0 0 0 2 2 2 1]
            [0 2 0 2 0 2 1]
            [0 2 2 2 0 0 1]

        Distances from facets to the point (1,2,3)::

            sage: o.distances([1,2,3])
            (-3, 1, 7, 3, 1, -5, -1, 5)

        It is OK to use RATIONAL coordinates::

            sage: o.distances([1,2,3/2])
            (-3/2, 5/2, 11/2, 3/2, -1/2, -7/2, 1/2, 7/2)
            sage: o.distances([1,2,sqrt(2)])                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unable to convert sqrt(2) to an element of Rational Field

        Now we create a non-spanning polytope::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.distances()                                                         # needs palp
            [2 2 0 0 1]
            [2 0 0 2 1]
            [0 0 2 2 1]
            [0 2 2 0 1]
            sage: p.distances((1/2, 3, 0))                                              # needs palp
            (9/2, -3/2, -5/2, 7/2)

        This point is not even in the affine subspace of the polytope::

            sage: p.distances((1, 1, 1))                                                # needs palp
            (3, 1, -1, 1)
        """
    @cached_method
    def dual(self):
        """
        Return the dual face under face duality of polar reflexive polytopes.

        This duality extends the correspondence between vertices and facets.

        OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

        EXAMPLES::

            sage: # needs sage.graphs
            sage: o = lattice_polytope.cross_polytope(4)
            sage: e = o.edges()[0]; e
            1-d face of 4-d reflexive polytope in 4-d lattice M
            sage: ed = e.dual(); ed
            2-d face of 4-d reflexive polytope in 4-d lattice N
            sage: ed.ambient() is e.ambient().polar()
            True
            sage: e.ambient_vertex_indices() == ed.ambient_facet_indices()
            True
            sage: e.ambient_facet_indices() == ed.ambient_vertex_indices()
            True
        """
    @cached_method
    def dual_lattice(self):
        """
        Return the dual of the ambient lattice of ``self``.

        OUTPUT:

        - a lattice. If possible (that is, if :meth:`lattice` has a
          ``dual()`` method), the dual lattice is returned. Otherwise,
          `\\ZZ^n` is returned, where `n` is the dimension of ``self``.

        EXAMPLES::

            sage: LatticePolytope([(1,0)]).dual_lattice()
            2-d lattice N
            sage: LatticePolytope([], lattice=ZZ^3).dual_lattice()
            Ambient free module of rank 3
            over the principal ideal domain Integer Ring
        """
    def edges(self):
        """
        Return edges (faces of dimension 1) of ``self``.

        OUTPUT: :class:`tuple` of :class:`lattice polytopes <LatticePolytopeClass>`

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.edges()                                                             # needs sage.graphs
            (1-d face of 3-d reflexive polytope in 3-d lattice M,
            ...
             1-d face of 3-d reflexive polytope in 3-d lattice M)
            sage: len(o.edges())                                                        # needs sage.graphs
            12
        """
    @cached_method
    def face_lattice(self):
        """
        Return the face lattice of ``self``.

        This lattice will have the empty polytope as the bottom and this
        polytope itself as the top.

        OUTPUT:

        - :class:`finite poset <sage.combinat.posets.posets.FinitePoset>` of
          :class:`lattice polytopes <LatticePolytopeClass>`.

        EXAMPLES:

        Let's take a look at the face lattice of a square::

            sage: square = LatticePolytope([(0,0), (1,0), (1,1), (0,1)])
            sage: L = square.face_lattice(); L                                          # needs sage.graphs
            Finite lattice containing 10 elements with distinguished linear extension

        To see all faces arranged by dimension, you can do this::

            sage: for level in L.level_sets(): print(level)                             # needs sage.graphs
            [-1-d face of 2-d lattice polytope in 2-d lattice M]
            [0-d face of 2-d lattice polytope in 2-d lattice M,
             0-d face of 2-d lattice polytope in 2-d lattice M,
             0-d face of 2-d lattice polytope in 2-d lattice M,
             0-d face of 2-d lattice polytope in 2-d lattice M]
            [1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M]
            [2-d lattice polytope in 2-d lattice M]

        For a particular face you can look at its actual vertices... ::

            sage: face = L.level_sets()[1][0]                                           # needs sage.graphs
            sage: face.vertices()                                                       # needs sage.graphs
            M(0, 0)
            in 2-d lattice M

        ... or you can see the index of the vertex of the original polytope that
        corresponds to the above one::

            sage: face.ambient_vertex_indices()                                         # needs sage.graphs
            (0,)
            sage: square.vertex(0)
            M(0, 0)

        An alternative to extracting faces from the face lattice is to use
        :meth:`faces` method::

            sage: face is square.faces(dim=0)[0]                                        # needs sage.graphs
            True

        The advantage of working with the face lattice directly is that you
        can (relatively easily) get faces that are related to the given one::

            sage: face = L.level_sets()[1][0]                                           # needs sage.graphs
            sage: D = L.hasse_diagram()                                                 # needs sage.graphs
            sage: sorted(D.neighbors(face))                                             # needs sage.graphs
            [-1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M]

        However, you can achieve some of this functionality using
        :meth:`facets`, :meth:`facet_of`, and :meth:`adjacent` methods::

            sage: # needs sage.graphs
            sage: face = square.faces(0)[0]
            sage: face
            0-d face of 2-d lattice polytope in 2-d lattice M
            sage: face.vertices()
            M(0, 0)
            in 2-d lattice M
            sage: face.facets()
            (-1-d face of 2-d lattice polytope in 2-d lattice M,)
            sage: face.facet_of()
            (1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M)
            sage: face.adjacent()
            (0-d face of 2-d lattice polytope in 2-d lattice M,
             0-d face of 2-d lattice polytope in 2-d lattice M)
            sage: face.adjacent()[0].vertices()
            M(1, 0)
            in 2-d lattice M

        Note that if ``p`` is a face of ``superp``, then the face
        lattice of ``p`` consists of (appropriate) faces of ``superp``::

            sage: # needs sage.graphs
            sage: superp = LatticePolytope([(1,2,3,4), (5,6,7,8),
            ....:                           (1,2,4,8), (1,3,9,7)])
            sage: superp.face_lattice()
            Finite lattice containing 16 elements with distinguished linear extension
            sage: superp.face_lattice().top()
            3-d lattice polytope in 4-d lattice M
            sage: p = superp.facets()[0]
            sage: p
            2-d face of 3-d lattice polytope in 4-d lattice M
            sage: p.face_lattice()
            Finite poset containing 8 elements with distinguished linear extension
            sage: p.face_lattice().bottom()
            -1-d face of 3-d lattice polytope in 4-d lattice M
            sage: p.face_lattice().top()
            2-d face of 3-d lattice polytope in 4-d lattice M
            sage: p.face_lattice().top() is p
            True
        """
    def faces(self, dim=None, codim=None):
        """
        Return faces of ``self`` of specified (co)dimension.

        INPUT:

        - ``dim`` -- integer; dimension of the requested faces

        - ``codim`` -- integer; codimension of the requested faces

        .. NOTE::

            You can specify at most one parameter. If you don't give any, then
            all faces will be returned.

        OUTPUT:

        - if either ``dim`` or ``codim`` is given, the output will be a
          :class:`tuple` of :class:`lattice polytopes <LatticePolytopeClass>`;

        - if neither ``dim`` nor ``codim`` is given, the output will be the
          :class:`tuple` of tuples as above, giving faces of all existing
          dimensions. If you care about inclusion relations between faces,
          consider using :meth:`face_lattice` or :meth:`adjacent`,
          :meth:`facet_of`, and :meth:`facets`.

        EXAMPLES:

        Let's take a look at the faces of a square::

            sage: square = LatticePolytope([(0,0), (1,0), (1,1), (0,1)])
            sage: square.faces()                                                        # needs sage.graphs
            ((-1-d face of 2-d lattice polytope in 2-d lattice M,),
             (0-d face of 2-d lattice polytope in 2-d lattice M,
              0-d face of 2-d lattice polytope in 2-d lattice M,
              0-d face of 2-d lattice polytope in 2-d lattice M,
              0-d face of 2-d lattice polytope in 2-d lattice M),
             (1-d face of 2-d lattice polytope in 2-d lattice M,
              1-d face of 2-d lattice polytope in 2-d lattice M,
              1-d face of 2-d lattice polytope in 2-d lattice M,
              1-d face of 2-d lattice polytope in 2-d lattice M),
             (2-d lattice polytope in 2-d lattice M,))

        Its faces of dimension one (i.e., edges)::

            sage: square.faces(dim=1)                                                   # needs sage.graphs
            (1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M,
             1-d face of 2-d lattice polytope in 2-d lattice M)

        Its faces of codimension one are the same (also edges)::

            sage: square.faces(codim=1) is square.faces(dim=1)                          # needs sage.graphs
            True

        Let's pick a particular face::

            sage: face = square.faces(dim=1)[0]                                         # needs sage.graphs

        Now you can look at the actual vertices of this face... ::

            sage: face.vertices()                                                       # needs sage.graphs
            M(0, 0),
            M(0, 1)
            in 2-d lattice M

        ... or you can see indices of the vertices of the original polytope that
        correspond to the above ones::

            sage: face.ambient_vertex_indices()                                         # needs sage.graphs
            (0, 3)
            sage: square.vertices(face.ambient_vertex_indices())                        # needs sage.graphs
            M(0, 0),
            M(0, 1)
            in 2-d lattice M
        """
    def facet_constant(self, i):
        """
        Return the constant in the `i`-th facet inequality of this polytope.

        This is equivalent to ``facet_constants()[i]``.

        INPUT:

        - ``i`` -- integer; the index of the facet

        OUTPUT: integer; the constant in the `i`-th facet inequality

        .. SEEALSO::

            :meth:`facet_constants`,
            :meth:`facet_normal`,
            :meth:`facet_normals`,
            :meth:`facets`.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.facet_constant(0)
            1
            sage: o.facet_constant(0) == o.facet_constants()[0]
            True
        """
    def facet_constants(self):
        """
        Return facet constants of ``self``.

        Facet inequalities have form `n \\cdot x + c \\geq 0` where `n` is the
        inner normal and `c` is a constant.

        OUTPUT: integer vector

        .. SEEALSO::

            :meth:`facet_constant`,
            :meth:`facet_normal`,
            :meth:`facet_normals`,
            :meth:`facets`.

        EXAMPLES:

        For reflexive polytopes all constants are 1::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: o.facet_constants()
            (1, 1, 1, 1, 1, 1, 1, 1)

        Here is an example of a 3-dimensional polytope in a 4-dimensional
        space with 3 facets containing the origin::

            sage: p = LatticePolytope([(0,0,0,0), (1,1,1,3),
            ....:                      (1,-1,1,3), (-1,-1,1,3)])
            sage: p.vertices()
            M( 0,  0, 0, 0),
            M( 1,  1, 1, 3),
            M( 1, -1, 1, 3),
            M(-1, -1, 1, 3)
            in 4-d lattice M
            sage: p.facet_constants()
            (0, 0, 3, 0)
        """
    def facet_normal(self, i):
        """
        Return the inner normal to the ``i``-th facet of this polytope.

        This is equivalent to ``facet_normals()[i]``.

        INPUT:

        - ``i`` -- integer; the index of the facet

        OUTPUT: a vector

        .. SEEALSO::

            :meth:`facet_constant`,
            :meth:`facet_constants`,
            :meth:`facet_normals`,
            :meth:`facets`.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.facet_normal(0)
            N(1, -1, -1)
            sage: o.facet_normal(0) is o.facet_normals()[0]
            True
        """
    def facet_normals(self):
        """
        Return inner normals to the facets of ``self``.

        If this polytope is not full-dimensional, facet normals will define
        this polytope in the affine subspace spanned by it.

        OUTPUT:

        - a :class:`point collection <PointCollection>` in the
          :meth:`dual_lattice` of ``self``.

        .. SEEALSO::

            :meth:`facet_constant`,
            :meth:`facet_constants`,
            :meth:`facet_normal`,
            :meth:`facets`.

        EXAMPLES:

        Normals to facets of an octahedron are vertices of a cube::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: o.facet_normals()
            N( 1, -1, -1),
            N( 1,  1, -1),
            N( 1,  1,  1),
            N( 1, -1,  1),
            N(-1, -1,  1),
            N(-1, -1, -1),
            N(-1,  1, -1),
            N(-1,  1,  1)
            in 3-d lattice N

        Here is an example of a 3-dimensional polytope in a 4-dimensional
        space::

            sage: p = LatticePolytope([(0,0,0,0), (1,1,1,3),
            ....:                      (1,-1,1,3), (-1,-1,1,3)])
            sage: p.vertices()
            M( 0,  0, 0, 0),
            M( 1,  1, 1, 3),
            M( 1, -1, 1, 3),
            M(-1, -1, 1, 3)
            in 4-d lattice M
            sage: p.facet_normals()
            N( 0,  3, 0,  1),
            N( 1, -1, 0,  0),
            N( 0,  0, 0, -1),
            N(-3,  0, 0,  1)
            in 4-d lattice N
            sage: p.facet_constants()
            (0, 0, 3, 0)

        Now we manually compute the distance matrix of this polytope. Since it
        is a simplex, each line (corresponding to a facet) should consist of
        zeros (indicating generating vertices of the corresponding facet) and
        a single positive number (since our normals are inner)::

            sage: matrix([[n * v + c for v in p.vertices()]
            ....:     for n, c in zip(p.facet_normals(), p.facet_constants())])
            [0 6 0 0]
            [0 0 2 0]
            [3 0 0 0]
            [0 0 0 6]
        """
    @cached_method
    def facet_of(self):
        """
        Return elements of the ambient face lattice having ``self`` as a facet.

        OUTPUT: :class:`tuple` of :class:`lattice polytopes <LatticePolytopeClass>`

        EXAMPLES::

            sage: # needs sage.graphs
            sage: square = LatticePolytope([(0,0), (1,0), (1,1), (0,1)])
            sage: square.facet_of()
            ()
            sage: face = square.faces(0)[0]
            sage: len(face.facet_of())
            2
            sage: face.facet_of()[1]
            1-d face of 2-d lattice polytope in 2-d lattice M
        """
    def facets(self):
        """
        Return facets (faces of codimension 1) of ``self``.

        OUTPUT: :class:`tuple` of :class:`lattice polytopes <LatticePolytopeClass>`

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.facets()                                                            # needs sage.graphs
            (2-d face of 3-d reflexive polytope in 3-d lattice M,
            ...
             2-d face of 3-d reflexive polytope in 3-d lattice M)
            sage: len(o.facets())                                                       # needs sage.graphs
            8
        """
    @cached_method
    def incidence_matrix(self):
        """
        Return the incidence matrix.

        .. NOTE::

            The columns correspond to facets/facet normals
            in the order of :meth:`facet_normals`, the rows
            correspond to the vertices in the order of
            :meth:`vertices`.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(2)
            sage: o.incidence_matrix()
            [0 0 1 1]
            [0 1 1 0]
            [1 1 0 0]
            [1 0 0 1]
            sage: o.faces(1)[0].incidence_matrix()                                      # needs sage.graphs
            [1 0]
            [0 1]

            sage: o = lattice_polytope.cross_polytope(4)
            sage: o.incidence_matrix().column(3).nonzero_positions()
            [3, 4, 5, 6]
            sage: o.facets()[3].ambient_vertex_indices()                                # needs sage.graphs
            (3, 4, 5, 6)

        TESTS::

            sage: o.incidence_matrix().is_immutable()
            True

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: o.incidence_matrix().base_ring()
            Integer Ring
        """
    @cached_method
    def index(self):
        '''
        Return the index of this polytope in the internal database of 2- or
        3-dimensional reflexive polytopes. Databases are stored in the
        directory of the package.

        .. NOTE::

            The first call to this function for each dimension can take
            a few seconds while the dictionary of all polytopes is
            constructed, but after that it is cached and fast.

        :rtype: integer

        EXAMPLES: We check what is the index of the "diamond" in the
        database::

            sage: d = lattice_polytope.cross_polytope(2)
            sage: d.index()                                                             # needs palp
            3

        Note that polytopes with the same index are not necessarily the
        same::

            sage: d.vertices()
            M( 1,  0),
            M( 0,  1),
            M(-1,  0),
            M( 0, -1)
            in 2-d lattice M
            sage: lattice_polytope.ReflexivePolytope(2,3).vertices()
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M

        But they are in the same `GL(\\ZZ^n)` orbit and have the same
        normal form::

            sage: d.normal_form()                                                       # needs sage.groups
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M
            sage: lattice_polytope.ReflexivePolytope(2,3).normal_form()                 # needs sage.groups
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M
        '''
    @cached_method
    def interior_point_indices(self):
        """
        Return indices of (relative) interior lattice points of this polytope.

        OUTPUT: increasing :class:`tuple` of integers

        EXAMPLES:

        The origin is the only interior point of this square::

            sage: square = lattice_polytope.cross_polytope(2).polar()
            sage: square.points()                                                       # needs palp
            N( 1,  1),
            N( 1, -1),
            N(-1, -1),
            N(-1,  1),
            N(-1,  0),
            N( 0, -1),
            N( 0,  0),
            N( 0,  1),
            N( 1,  0)
            in 2-d lattice N
            sage: square.interior_point_indices()                                       # needs palp
            (6,)

        Its edges also have a single interior point each::

            sage: face = square.edges()[0]                                              # needs sage.graphs
            sage: face.points()                                                         # needs sage.graphs
            N(-1, -1),
            N(-1,  1),
            N(-1,  0)
            in 2-d lattice N
            sage: face.interior_point_indices()                                         # needs sage.graphs
            (2,)
        """
    def interior_points(self):
        """
        Return (relative) boundary lattice points of this polytope.

        OUTPUT: a :class:`point collection <PointCollection>`

        EXAMPLES:

        The origin is the only interior point of this square::

            sage: square = lattice_polytope.cross_polytope(2).polar()
            sage: square.interior_points()                                              # needs palp
            N(0, 0)
            in 2-d lattice N

        Its edges also have a single interior point each::

            sage: face = square.edges()[0]                                              # needs sage.graphs
            sage: face.interior_points()                                                # needs sage.graphs
            N(-1, 0)
            in 2-d lattice N
        """
    @cached_method
    def is_reflexive(self):
        """
        Return ``True`` if this polytope is reflexive.

        EXAMPLES: The 3-dimensional octahedron is reflexive (and 4319 other
        3-polytopes)::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.is_reflexive()
            True

        But not all polytopes are reflexive::

            sage: p = LatticePolytope([(1,0,0), (0,1,17), (-1,0,0), (0,-1,0)])
            sage: p.is_reflexive()
            False

        Only full-dimensional polytopes can be reflexive (otherwise the polar
        set is not a polytope at all, since it is unbounded)::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.is_reflexive()
            False
        """
    def lattice(self):
        """
        Return the ambient lattice of ``self``.

        OUTPUT: a lattice

        EXAMPLES::

            sage: lattice_polytope.cross_polytope(3).lattice()
            3-d lattice M
        """
    def lattice_dim(self):
        """
        Return the dimension of the ambient lattice of ``self``.

        An alias is :meth:`ambient_dim`.

        OUTPUT: integer

        EXAMPLES::

            sage: p = LatticePolytope([(1,0)])
            sage: p.lattice_dim()
            2
            sage: p.dim()
            0
        """
    ambient_dim = lattice_dim
    def ambient_vector_space(self, base_field=None):
        """
        Return the ambient vector space.

        It is the ambient lattice (:meth:`lattice`) tensored with a field.

        INPUT:

        - ``base_field`` -- (default: the rationals) a field

        EXAMPLES::

            sage: p = LatticePolytope([(1,0)])
            sage: p.ambient_vector_space()
            Vector space of dimension 2 over Rational Field
            sage: p.ambient_vector_space(AA)                                            # needs sage.rings.number_field
            Vector space of dimension 2 over Algebraic Real Field
        """
    def linearly_independent_vertices(self):
        """
        Return a maximal set of linearly independent vertices.

        OUTPUT: a tuple of vertex indices

        EXAMPLES::

            sage: L = LatticePolytope([[0, 0], [-1, 1], [-1, -1]])
            sage: L.linearly_independent_vertices()
            (1, 2)
            sage: L = LatticePolytope([[0, 0, 0]])
            sage: L.linearly_independent_vertices()
            ()
            sage: L = LatticePolytope([[0, 1, 0]])
            sage: L.linearly_independent_vertices()
            (0,)
        """
    def nef_partitions(self, keep_symmetric: bool = False, keep_products: bool = True, keep_projections: bool = True, hodge_numbers: bool = False):
        '''
        Return 2-part nef-partitions of ``self``.

        INPUT:

        - ``keep_symmetric`` -- boolean (default: ``False``); if ``True``, "-s" option
          will be passed to ``nef.x`` in order to keep symmetric partitions,
          i.e. partitions related by lattice automorphisms preserving ``self``

        - ``keep_products`` -- boolean (default: ``True``); if ``True``, "-D" option
          will be passed to ``nef.x`` in order to keep product partitions,
          with corresponding complete intersections being direct products

        - ``keep_projections`` -- boolean (default: ``True``); if ``True``, "-P" option
          will be passed to ``nef.x`` in order to keep projection partitions,
          i.e. partitions with one of the parts consisting of a single vertex

        - ``hodge_numbers`` -- boolean (default: ``False``); if ``False``, "-p" option
          will be passed to ``nef.x`` in order to skip Hodge numbers
          computation, which takes a lot of time

        OUTPUT: a sequence of :class:`nef-partitions <NefPartition>`

        Type ``NefPartition?`` for definitions and notation.

        EXAMPLES:

        Nef-partitions of the 4-dimensional cross-polytope::

            sage: p = lattice_polytope.cross_polytope(4)
            sage: p.nef_partitions()                                                    # needs palp
            [Nef-partition {0, 1, 4, 5} ⊔ {2, 3, 6, 7} (direct product),
             Nef-partition {0, 1, 2, 4} ⊔ {3, 5, 6, 7},
             Nef-partition {0, 1, 2, 4, 5} ⊔ {3, 6, 7},
             Nef-partition {0, 1, 2, 4, 5, 6} ⊔ {3, 7} (direct product),
             Nef-partition {0, 1, 2, 3} ⊔ {4, 5, 6, 7},
             Nef-partition {0, 1, 2, 3, 4} ⊔ {5, 6, 7},
             Nef-partition {0, 1, 2, 3, 4, 5} ⊔ {6, 7},
             Nef-partition {0, 1, 2, 3, 4, 5, 6} ⊔ {7} (projection)]

        Now we omit projections::

            sage: p.nef_partitions(keep_projections=False)                              # needs palp
            [Nef-partition {0, 1, 4, 5} ⊔ {2, 3, 6, 7} (direct product),
             Nef-partition {0, 1, 2, 4} ⊔ {3, 5, 6, 7},
             Nef-partition {0, 1, 2, 4, 5} ⊔ {3, 6, 7},
             Nef-partition {0, 1, 2, 4, 5, 6} ⊔ {3, 7} (direct product),
             Nef-partition {0, 1, 2, 3} ⊔ {4, 5, 6, 7},
             Nef-partition {0, 1, 2, 3, 4} ⊔ {5, 6, 7},
             Nef-partition {0, 1, 2, 3, 4, 5} ⊔ {6, 7}]

        Currently Hodge numbers cannot be computed for a given nef-partition::

            sage: p.nef_partitions()[1].hodge_numbers()                                 # needs palp
            Traceback (most recent call last):
            ...
            NotImplementedError: use nef_partitions(hodge_numbers=True)!

        But they can be obtained from ``nef.x`` for all nef-partitions at once.
        Partitions will be exactly the same::

            sage: p.nef_partitions(hodge_numbers=True)  # long time (2s on sage.math, 2011), needs palp
            [Nef-partition {0, 1, 4, 5} ⊔ {2, 3, 6, 7} (direct product),
             Nef-partition {0, 1, 2, 4} ⊔ {3, 5, 6, 7},
             Nef-partition {0, 1, 2, 4, 5} ⊔ {3, 6, 7},
             Nef-partition {0, 1, 2, 4, 5, 6} ⊔ {3, 7} (direct product),
             Nef-partition {0, 1, 2, 3} ⊔ {4, 5, 6, 7},
             Nef-partition {0, 1, 2, 3, 4} ⊔ {5, 6, 7},
             Nef-partition {0, 1, 2, 3, 4, 5} ⊔ {6, 7},
             Nef-partition {0, 1, 2, 3, 4, 5, 6} ⊔ {7} (projection)]

        Now it is possible to get Hodge numbers::

            sage: p.nef_partitions(hodge_numbers=True)[1].hodge_numbers()               # needs palp
            (20,)

        Since nef-partitions are cached, their Hodge numbers are accessible
        after the first request, even if you do not specify
        ``hodge_numbers=True`` anymore::

            sage: p.nef_partitions()[1].hodge_numbers()                                 # needs palp
            (20,)

        We illustrate removal of symmetric partitions on a diamond::

            sage: p = lattice_polytope.cross_polytope(2)
            sage: p.nef_partitions()                                                    # needs palp
            [Nef-partition {0, 2} ⊔ {1, 3} (direct product),
             Nef-partition {0, 1} ⊔ {2, 3},
             Nef-partition {0, 1, 2} ⊔ {3} (projection)]
            sage: p.nef_partitions(keep_symmetric=True)                                 # needs palp
            [Nef-partition {0, 1, 3} ⊔ {2} (projection),
             Nef-partition {0, 2, 3} ⊔ {1} (projection),
             Nef-partition {0, 3} ⊔ {1, 2},
             Nef-partition {1, 2, 3} ⊔ {0} (projection),
             Nef-partition {1, 3} ⊔ {0, 2} (direct product),
             Nef-partition {2, 3} ⊔ {0, 1},
             Nef-partition {0, 1, 2} ⊔ {3} (projection)]

        Nef-partitions can be computed only for reflexive polytopes::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (0,0,2),
            ....:                      (-1,0,0), (0,-1,0), (0,0,-1)])
            sage: p.nef_partitions()                                                    # needs palp
            Traceback (most recent call last):
            ...
            ValueError: The given polytope is not reflexive!
            Polytope: 3-d lattice polytope in 3-d lattice M
        '''
    def nef_x(self, keys):
        '''
        Run ``nef.x`` with given ``keys`` on vertices of this
        polytope.

        INPUT:

        - ``keys`` -- string of options passed to ``nef.x``; the
          key "-f" is added automatically

        OUTPUT: the output of ``nef.x`` as a string

        EXAMPLES: This call is used internally for computing
        nef-partitions::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: s = o.nef_x("-N -V -p")                                               # needs palp
            sage: s                      # output contains random time                  # needs palp
            M:27 8 N:7 6  codim=2 #part=5
            3 6  Vertices of P:
                1    0    0   -1    0    0
                0    1    0    0   -1    0
                0    0    1    0    0   -1
             P:0 V:2 4 5       0sec  0cpu
             P:2 V:3 4 5       0sec  0cpu
             P:3 V:4 5       0sec  0cpu
            np=3 d:1 p:1    0sec     0cpu
        '''
    def nfacets(self):
        """
        Return the number of facets of this polytope.

        EXAMPLES: The number of facets of the 3-dimensional octahedron::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.nfacets()
            8

        The number of facets of an interval is 2::

            sage: LatticePolytope(([1],[2])).nfacets()
            2

        Now consider a 2-dimensional diamond in a 3-dimensional space::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.nfacets()
            4
        """
    @cached_method
    def normal_form(self, algorithm: str = 'palp_native', permutation: bool = False):
        '''
        Return the normal form of vertices of ``self``.

        Two full-dimensional lattice polytopes are in the same
        `GL(\\ZZ^n)`-orbit if and only if their normal forms are the
        same. Normal form is not defined and thus cannot be used for polytopes
        whose dimension is smaller than the dimension of the ambient space.

        The original algorithm was presented in [KS1998]_ and implemented
        in PALP. A modified version of the PALP algorithm is discussed in
        [GK2013]_ and available here as ``\'palp_modified\'``.

        INPUT:

        - ``algorithm`` -- (default: ``\'palp_native\'``) the algorithm which is used
          to compute the normal form. Options are:

          * ``\'palp\'`` -- run external PALP code, usually the fastest option
            when it works; but reproducible crashes have been observed in dimension
            5 and higher.

          * ``\'palp_native\'`` -- the original PALP algorithm implemented
            in sage. Currently competitive with PALP in many cases.

          * ``\'palp_modified\'`` -- a modified version of the PALP
            algorithm which determines the maximal vertex-facet
            pairing matrix first and then computes its
            automorphisms, while the PALP algorithm does both things
            concurrently.

        - ``permutation`` -- boolean (default: ``False``); if ``True``, the permutation
          applied to vertices to obtain the normal form is returned as well.
          Note that the different algorithms may return different results
          that nevertheless lead to the same normal form.

        OUTPUT:

        - a :class:`point collection <PointCollection>` in the :meth:`lattice`
          of ``self`` or a tuple of it and a permutation.

        EXAMPLES:

        We compute the normal form of the "diamond"::

            sage: d = LatticePolytope([(1,0), (0,1), (-1,0), (0,-1)])
            sage: d.vertices()
            M( 1,  0),
            M( 0,  1),
            M(-1,  0),
            M( 0, -1)
            in 2-d lattice M
            sage: d.normal_form()                                                       # needs sage.groups
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M

        The diamond is the 3rd polytope in the internal database::

            sage: d.index()                                                             # needs palp
            3
            sage: d                                                                     # needs palp
            2-d reflexive polytope #3 in 2-d lattice M

        You can get it in its normal form (in the default lattice) as ::

            sage: lattice_polytope.ReflexivePolytope(2, 3).vertices()
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M

        It is not possible to compute normal forms for polytopes which do not
        span the space::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.normal_form()
            Traceback (most recent call last):
            ...
            ValueError: normal form is not defined for
            2-d lattice polytope in 3-d lattice M

        We can perform the same examples using other algorithms::

            sage: o = lattice_polytope.cross_polytope(2)
            sage: o.normal_form(algorithm=\'palp_native\')                                # needs sage.groups
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M

            sage: o = lattice_polytope.cross_polytope(2)
            sage: o.normal_form(algorithm=\'palp_modified\')                              # needs sage.groups
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M

        The following examples demonstrate the speed of the available algorithms.
        In low dimensions, the default algorithm, ``\'palp_native\'``, is the fastest.
        As the dimension increases, ``\'palp\'`` is relatively faster than ``\'palp_native\'``.
        ``\'palp_native\'`` is usually much faster than ``\'palp_modified\'``.
        In some cases when the polytope has high symmetry, however, ``\'palp_native\'`` is slower::

            sage: # not tested
            sage: o = lattice_polytope.cross_polytope(2)
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp")
            625 loops, best of 3: 3.07 ms per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_native")
            625 loops, best of 3: 0.445 ms per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_modified")
            625 loops, best of 3: 5.01 ms per loop
            sage: o = lattice_polytope.cross_polytope(3)
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp")
            625 loops, best of 3: 3.22 ms per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_native")
            625 loops, best of 3: 2.73 ms per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_modified")
            625 loops, best of 3: 20.7 ms per loop
            sage: o = lattice_polytope.cross_polytope(4)
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp")
            625 loops, best of 3: 4.84 ms per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_native")
            625 loops, best of 3: 55.6 ms per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_modified")
            625 loops, best of 3: 129 ms per loop
            sage: o = lattice_polytope.cross_polytope(5)
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp")
            10 loops, best of 3: 0.0364 s per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_native")
            10 loops, best of 3: 1.68 s per loop
            sage: %timeit o.normal_form.clear_cache(); o.normal_form("palp_modified")
            10 loops, best of 3: 0.858 s per loop

        Note that the algorithm ``\'palp\'`` may crash for higher dimensions because of
        the overflow errors as mentioned in :issue:`13525#comment:9`.
        Then use ``\'palp_native\'`` instead, which is usually faster than ``\'palp_modified\'``.
        Below is an example where ``\'palp\'`` fails and
        ``\'palp_native\'`` is much faster than ``\'palp_modified\'``::

            sage: P = LatticePolytope([[-3, -3, -6, -6, -1], [3, 3, 6, 6, 1], [-3, -3, -6, -6, 1],
            ....:                      [-3, -3, -3, -6, 0], [-3, -3, -3, 0, 0], [-3, -3, 0, 0, 0],
            ....:                      [-3, 0, -6, -6, 0], [-3, 0, -3, -6, 0], [-3, 0, -3, 0, 0],
            ....:                      [-3, 0, 0, 0, -1], [3, 3, 6, 6, -1], [-3, 0, 0, 0, 1],
            ....:                      [0, -3, -6, -6, 0], [0, -3, -3, -6, 0], [0, -3, -3, 0, 0],
            ....:                      [0, -3, 0, 0, -1], [3, 3, 3, 6, 0], [0, -3, 0, 0, 1],
            ....:                      [0, 0, -6, -6, 0], [0, 0, -3, -6, -1], [3, 3, 3, 0, 0],
            ....:                      [0, 0, -3, -6, 1], [0, 0, -3, 0, -1], [3, 3, 0, 0, 0],
            ....:                      [0, 0, -3, 0, 1], [0, 0, 3, 0, -1], [3, 0, 6, 6, 0],
            ....:                      [0, 0, 3, 0, 1], [0, 0, 3, 6, -1], [3, 0, 3, 6, 0],
            ....:                      [0, 0, 3, 6, 1], [0, 0, 6, 6, 0], [0, 3, 0, 0, -1],
            ....:                      [3, 0, 3, 0, 0], [0, 3, 0, 0, 1], [0, 3, 3, 0, 0],
            ....:                      [0, 3, 3, 6, 0], [0, 3, 6, 6, 0], [3, 0,0, 0, -1], [3, 0, 0, 0, 1]])
            sage: P.normal_form(algorithm=\'palp\')  # not tested
            Traceback (most recent call last):
            ...
            RuntimeError: Error executing ... for a polytope sequence!
            Output:
            b\'*** stack smashing detected ***: terminated\\nAborted\\n\'
            sage: P.normal_form(algorithm=\'palp_native\')                                # needs sage.groups
            M(  6,  0,  0,  0,  0),
            M( -6,  0,  0,  0,  0),
            M(  0,  1,  0,  0,  0),
            M(  0,  0,  3,  0,  0),
            M(  0,  1,  0,  3,  0),
            M(  0,  0,  0,  0,  3),
            M( -6,  1,  6,  3, -6),
            M( -6,  0,  6,  0, -3),
            M(-12,  1,  6,  3, -3),
            M( -6,  1,  0,  3,  0),
            M( -6,  0,  3,  3,  0),
            M(  6,  0, -6, -3,  6),
            M(-12,  1,  6,  3, -6),
            M(-12,  0,  9,  3, -6),
            M(  0,  0,  0, -3,  0),
            M(-12,  1,  6,  6, -6),
            M(-12,  0,  6,  3, -3),
            M(  0,  1, -3,  0,  0),
            M(  0,  0, -3, -3,  3),
            M(  0,  1,  0,  3, -3),
            M(  0, -1,  0, -3,  3),
            M(  0,  0,  3,  3, -3),
            M(  0, -1,  3,  0,  0),
            M( 12,  0, -6, -3,  3),
            M( 12, -1, -6, -6,  6),
            M(  0,  0,  0,  3,  0),
            M( 12,  0, -9, -3,  6),
            M( 12, -1, -6, -3,  6),
            M( -6,  0,  6,  3, -6),
            M(  6,  0, -3, -3,  0),
            M(  6, -1,  0, -3,  0),
            M(-12,  1,  9,  6, -6),
            M(  6,  0, -6,  0,  3),
            M(  6, -1, -6, -3,  6),
            M(  0,  0,  0,  0, -3),
            M(  0, -1,  0, -3,  0),
            M(  0,  0, -3,  0,  0),
            M(  0, -1,  0,  0,  0),
            M( 12, -1, -9, -6,  6),
            M( 12, -1, -6, -3,  3)
            in 5-d lattice M
            sage: P.normal_form(algorithm=\'palp_modified\')      # not tested (22s; MemoryError on 32 bit), needs sage.groups
            M(  6,  0,  0,  0,  0),
            M( -6,  0,  0,  0,  0),
            M(  0,  1,  0,  0,  0),
            M(  0,  0,  3,  0,  0),
            M(  0,  1,  0,  3,  0),
            M(  0,  0,  0,  0,  3),
            M( -6,  1,  6,  3, -6),
            M( -6,  0,  6,  0, -3),
            M(-12,  1,  6,  3, -3),
            M( -6,  1,  0,  3,  0),
            M( -6,  0,  3,  3,  0),
            M(  6,  0, -6, -3,  6),
            M(-12,  1,  6,  3, -6),
            M(-12,  0,  9,  3, -6),
            M(  0,  0,  0, -3,  0),
            M(-12,  1,  6,  6, -6),
            M(-12,  0,  6,  3, -3),
            M(  0,  1, -3,  0,  0),
            M(  0,  0, -3, -3,  3),
            M(  0,  1,  0,  3, -3),
            M(  0, -1,  0, -3,  3),
            M(  0,  0,  3,  3, -3),
            M(  0, -1,  3,  0,  0),
            M( 12,  0, -6, -3,  3),
            M( 12, -1, -6, -6,  6),
            M(  0,  0,  0,  3,  0),
            M( 12,  0, -9, -3,  6),
            M( 12, -1, -6, -3,  6),
            M( -6,  0,  6,  3, -6),
            M(  6,  0, -3, -3,  0),
            M(  6, -1,  0, -3,  0),
            M(-12,  1,  9,  6, -6),
            M(  6,  0, -6,  0,  3),
            M(  6, -1, -6, -3,  6),
            M(  0,  0,  0,  0, -3),
            M(  0, -1,  0, -3,  0),
            M(  0,  0, -3,  0,  0),
            M(  0, -1,  0,  0,  0),
            M( 12, -1, -9, -6,  6),
            M( 12, -1, -6, -3,  3)
            in 5-d lattice M
            sage: %timeit P.normal_form.clear_cache(); P.normal_form("palp_native")    # not tested
            10 loops, best of 3: 0.137 s per loop
            sage: %timeit P.normal_form.clear_cache(); P.normal_form("palp_modified")  # not tested
            10 loops, best of 3:  22.2 s per loop

        TESTS::

            sage: d.normal_form("palp_fiction")
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be \'palp\', \'palp_native\', or \'palp_modified\'
        '''
    def npoints(self):
        """
        Return the number of lattice points of this polytope.

        EXAMPLES: The number of lattice points of the 3-dimensional
        octahedron and its polar cube::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.npoints()                                                           # needs palp
            7
            sage: cube = o.polar()
            sage: cube.npoints()                                                        # needs palp
            27
        """
    def nvertices(self):
        """
        Return the number of vertices of this polytope.

        EXAMPLES: The number of vertices of the 3-dimensional octahedron
        and its polar cube::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.nvertices()
            6
            sage: cube = o.polar()
            sage: cube.nvertices()
            8
        """
    @cached_method
    def origin(self):
        """
        Return the index of the origin in the list of points of ``self``.

        OUTPUT: integer if the origin belongs to this polytope, ``None`` otherwise

        EXAMPLES::

            sage: p = lattice_polytope.cross_polytope(2)
            sage: p.origin()                                                            # needs palp
            4
            sage: p.point(p.origin())                                                   # needs palp
            M(0, 0)

            sage: p = LatticePolytope(([1],[2]))
            sage: p.points()
            M(1),
            M(2)
            in 1-d lattice M
            sage: print(p.origin())
            None

        Now we make sure that the origin of non-full-dimensional polytopes can
        be identified correctly (:issue:`10661`)::

            sage: LatticePolytope([(1,0,0), (-1,0,0)]).origin()
            2
        """
    def parent(self):
        """
        Return the set of all lattice polytopes.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.parent()
            Set of all Lattice Polytopes
        """
    def plot3d(self, show_facets: bool = True, facet_opacity: float = 0.5, facet_color=(0, 1, 0), facet_colors=None, show_edges: bool = True, edge_thickness: int = 3, edge_color=(0.5, 0.5, 0.5), show_vertices: bool = True, vertex_size: int = 10, vertex_color=(1, 0, 0), show_points: bool = True, point_size: int = 10, point_color=(0, 0, 1), show_vindices=None, vindex_color=(0, 0, 0), vlabels=None, show_pindices=None, pindex_color=(0, 0, 0), index_shift: float = 1.1):
        '''
        Return a 3d-plot of this polytope.

        Polytopes with ambient dimension 1 and 2 will be plotted along x-axis
        or in xy-plane respectively. Polytopes of dimension 3 and less with
        ambient dimension 4 and greater will be plotted in some basis of the
        spanned space.

        By default, everything is shown with more or less pretty
        combination of size and color parameters.

        INPUT:

        Most of the parameters are self-explanatory:

        - ``show_facets`` -- (default: ``True``)

        - ``facet_opacity`` -- (default:0.5)

        - ``facet_color`` -- (default:(0,1,0))

        - ``facet_colors`` -- (default:None) if specified, must be a list of
          colors for each facet separately, used instead of ``facet_color``

        - ``show_edges`` -- boolean (default: ``True``); whether to draw
          edges as lines

        - ``edge_thickness`` -- (default:3)

        - ``edge_color`` -- (default:(0.5,0.5,0.5))

        - ``show_vertices`` -- boolean (default: ``True``); whether to draw
          vertices as balls

        - ``vertex_size`` -- (default:10)

        - ``vertex_color`` -- (default:(1,0,0))

        - ``show_points`` -- boolean (default: ``True``); whether to draw
          other points as balls

        - ``point_size`` -- (default:10)

        - ``point_color`` -- (default:(0,0,1))

        - ``show_vindices`` -- (default: same as
          ``show_vertices``) whether to show indices of vertices

        - ``vindex_color`` -- (default:(0,0,0)) color for
          vertex labels

        - ``vlabels`` -- (default:None) if specified, must be a list of labels
          for each vertex, default labels are vertex indices

        - ``show_pindices`` -- (default: same as ``show_points``)
          whether to show indices of other points

        - ``pindex_color`` -- (default:(0,0,0)) color for
          point labels

        - ``index_shift`` -- (default:1.1)) if 1, labels are
          placed exactly at the corresponding points. Otherwise the label
          position is computed as a multiple of the point position vector.

        EXAMPLES: The default plot of a cube::

            sage: c = lattice_polytope.cross_polytope(3).polar()
            sage: c.plot3d()                                                            # needs palp sage.plot
            Graphics3d Object

        Plot without facets and points, shown without the frame::

            sage: c.plot3d(show_facets=false,                                           # needs palp sage.plot
            ....:          show_points=false).show(frame=False)

        Plot with facets of different colors::

            sage: c.plot3d(facet_colors=rainbow(c.nfacets(), \'rgbtuple\'))               # needs palp sage.plot
            Graphics3d Object

        It is also possible to plot lower dimensional polytops in 3D (let\'s
        also change labels of vertices)::

            sage: c2 = lattice_polytope.cross_polytope(2)
            sage: c2.plot3d(vlabels=["A", "B", "C", "D"])                               # needs palp sage.plot
            Graphics3d Object

        TESTS::

            sage: p = LatticePolytope([[0,0,0],[0,1,1],[1,0,1],[1,1,0]])
            sage: p.plot3d()                                                            # needs palp sage.plot
            Graphics3d Object
        '''
    def polyhedron(self, **kwds):
        """
        Return the Polyhedron object determined by this polytope's vertices.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(2)
            sage: o.polyhedron()
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices
        """
    def show3d(self) -> None:
        """
        Show a 3d picture of the polytope with default settings and without axes or frame.

        See self.plot3d? for more details.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.show3d()                                                            # needs palp sage.plot
        """
    def point(self, i):
        """
        Return the `i`-th point of this polytope, i.e. the `i`-th column of the
        matrix returned by ``points()``.

        EXAMPLES: First few points are actually vertices::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: o.point(1)                                                            # needs palp
            M(0, 1, 0)

        The only other point in the octahedron is the origin::

            sage: o.point(6)                                                            # needs palp
            M(0, 0, 0)
            sage: o.points()                                                            # needs palp
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1),
            M( 0,  0,  0)
            in 3-d lattice M
        """
    def points(self, *args, **kwds):
        """
        Return all lattice points of ``self``.

        INPUT:

        - any arguments given will be passed on to the returned object.

        OUTPUT: a :class:`point collection <PointCollection>`

        EXAMPLES:

        Lattice points of the octahedron and its polar cube::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.points()                                                            # needs palp
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1),
            M( 0,  0,  0)
            in 3-d lattice M
            sage: cube = o.polar()
            sage: cube.points()                                                         # needs palp
            N( 1, -1, -1),
            N( 1,  1, -1),
            N( 1,  1,  1),
            N( 1, -1,  1),
            N(-1, -1,  1),
            N(-1, -1, -1),
            N(-1,  1, -1),
            N(-1,  1,  1),
            N(-1, -1,  0),
            N(-1,  0, -1),
            N(-1,  0,  0),
            N(-1,  0,  1),
            N(-1,  1,  0),
            N( 0, -1, -1),
            N( 0, -1,  0),
            N( 0, -1,  1),
            N( 0,  0, -1),
            N( 0,  0,  0),
            N( 0,  0,  1),
            N( 0,  1, -1),
            N( 0,  1,  0),
            N( 0,  1,  1),
            N( 1, -1,  0),
            N( 1,  0, -1),
            N( 1,  0,  0),
            N( 1,  0,  1),
            N( 1,  1,  0)
            in 3-d lattice N

        Lattice points of a 2-dimensional diamond in a 3-dimensional space::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.points()                                                            # needs palp
            M( 1,  0, 0),
            M( 0,  1, 0),
            M(-1,  0, 0),
            M( 0, -1, 0),
            M( 0,  0, 0)
            in 3-d lattice M

        Only two of the above points::

            sage: p.points(1, 3)                                                        # needs palp
            M(0,  1, 0),
            M(0, -1, 0)
            in 3-d lattice M

        We check that points of a zero-dimensional polytope can be computed::

            sage: p = LatticePolytope([[1]])
            sage: p.points()
            M(1)
            in 1-d lattice M
        """
    def polar(self):
        '''
        Return the polar polytope, if this polytope is reflexive.

        EXAMPLES: The polar polytope to the 3-dimensional octahedron::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: cube = o.polar()
            sage: cube
            3-d reflexive polytope in 3-d lattice N

        The polar polytope "remembers" the original one::

            sage: cube.polar()
            3-d reflexive polytope in 3-d lattice M
            sage: cube.polar().polar() is cube
            True

        Only reflexive polytopes have polars::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (0,0,2),
            ....:                      (-1,0,0), (0,-1,0), (0,0,-1)])
            sage: p.polar()
            Traceback (most recent call last):
            ...
            ValueError: The given polytope is not reflexive!
            Polytope: 3-d lattice polytope in 3-d lattice M
        '''
    def poly_x(self, keys, reduce_dimension: bool = False):
        '''
        Run ``poly.x`` with given ``keys`` on vertices of this
        polytope.

        INPUT:

        - ``keys`` -- string of options passed to ``poly.x``. The
          key "f" is added automatically

        - ``reduce_dimension`` -- boolean (default: ``False``); if ``True`` and this
          polytope is not full-dimensional, ``poly.x`` will be called for the
          vertices of this polytope in some basis of the spanned affine space

        OUTPUT: the output of ``poly.x`` as a string

        EXAMPLES: This call is used for determining if a polytope is
        reflexive or not::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: print(o.poly_x("e"))                                                  # needs palp
            8 3  Vertices of P-dual <-> Equations of P
              -1  -1   1
               1  -1   1
              -1   1   1
               1   1   1
              -1  -1  -1
               1  -1  -1
              -1   1  -1
               1   1  -1

        Since PALP has limits on different parameters determined during
        compilation, the following code is likely to fail, unless you
        change default settings of PALP::

            sage: BIG = lattice_polytope.cross_polytope(7)
            sage: BIG
            7-d reflexive polytope in 7-d lattice M
            sage: BIG.poly_x("e")                                                       # needs palp
            Traceback (most recent call last):
            ...
            ValueError: Error executing \'poly.x -fe\' for the given polytope!
            Output:
            Please increase POLY_Dmax to at least 7

        You cannot call ``poly.x`` for polytopes that don\'t span the space (if you
        could, it would crush anyway)::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.poly_x("e")                                                         # needs palp
            Traceback (most recent call last):
            ...
            ValueError: Cannot run PALP for a 2-dimensional polytope in a 3-dimensional space!

        But if you know what you are doing, you can call it for the polytope in
        some basis of the spanned space::

            sage: print(p.poly_x("e", reduce_dimension=True))                           # needs palp
            4 2  Equations of P
              -1   1     0
               1   1     2
              -1  -1     0
               1  -1     2
        '''
    @cached_method
    def skeleton(self):
        """
        Return the graph of the one-skeleton of this polytope.

        EXAMPLES::

            sage: d = lattice_polytope.cross_polytope(2)
            sage: g = d.skeleton(); g                                                   # needs palp sage.graphs
            Graph on 4 vertices
            sage: g.edges(sort=True)                                                    # needs palp sage.graphs
            [(0, 1, None), (0, 3, None), (1, 2, None), (2, 3, None)]
        """
    def skeleton_points(self, k: int = 1):
        """
        Return the increasing list of indices of lattice points in
        k-skeleton of the polytope (k is 1 by default).

        EXAMPLES: We compute all skeleton points for the cube::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: c = o.polar()
            sage: c.skeleton_points()                                                   # needs palp sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 19, 21, 22, 23, 25, 26]

        The default was 1-skeleton::

            sage: c.skeleton_points(k=1)                                                # needs palp sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 19, 21, 22, 23, 25, 26]

        0-skeleton just lists all vertices::

            sage: c.skeleton_points(k=0)                                                # needs palp sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7]

        2-skeleton lists all points except for the origin (point #17)::

            sage: c.skeleton_points(k=2)                                                # needs palp sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
             18, 19, 20, 21, 22, 23, 24, 25, 26]

        3-skeleton includes all points::

            sage: c.skeleton_points(k=3)                                                # needs palp
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
             18, 19, 20, 21, 22, 23, 24, 25, 26]

        It is OK to compute higher dimensional skeletons - you will get the
        list of all points::

            sage: c.skeleton_points(k=100)                                              # needs palp
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
             18, 19, 20, 21, 22, 23, 24, 25, 26]
        """
    def skeleton_show(self, normal=None) -> None:
        '''Show the graph of one-skeleton of this polytope.
        Works only for polytopes in a 3-dimensional space.

        INPUT:

        - ``normal`` -- a 3-dimensional vector (can be given as a list), which
          should be perpendicular to the screen. If not given, will be selected
          randomly (new each time and it may be far from "nice").

        EXAMPLES: Show a pretty picture of the octahedron::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.skeleton_show([1,2,4])                                              # needs palp sage.plot

        Does not work for a diamond at the moment::

            sage: d = lattice_polytope.cross_polytope(2)
            sage: d.skeleton_show()
            Traceback (most recent call last):
            ...
            NotImplementedError: skeleton view is implemented only in 3-d space
        '''
    def traverse_boundary(self):
        """
        Return a list of indices of vertices of a 2-dimensional polytope in their boundary order.

        Needed for plot3d function of polytopes.

        EXAMPLES::

            sage: p = lattice_polytope.cross_polytope(2).polar()
            sage: p.traverse_boundary()                                                 # needs sage.graphs
            [3, 0, 1, 2]
        """
    def vertex(self, i):
        """
        Return the `i`-th vertex of this polytope, i.e. the `i`-th column of
        the matrix returned by ``vertices()``.

        EXAMPLES: Note that numeration starts with zero::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: o.vertex(3)
            M(-1, 0, 0)
        """
    def vertex_facet_pairing_matrix(self):
        """
        Return the vertex facet pairing matrix `PM`.

        Return a matrix whose the `i, j^\\text{th}` entry is the height
        of the `j^\\text{th}` vertex over the `i^\\text{th}` facet.
        The ordering of the vertices and facets is as in
        :meth:`vertices` and :meth:`facets`.

        EXAMPLES::

            sage: L = lattice_polytope.cross_polytope(3)
            sage: L.vertex_facet_pairing_matrix()
            [2 0 0 0 2 2]
            [2 2 0 0 0 2]
            [2 2 2 0 0 0]
            [2 0 2 0 2 0]
            [0 0 2 2 2 0]
            [0 0 0 2 2 2]
            [0 2 0 2 0 2]
            [0 2 2 2 0 0]
        """
    def vertices(self, *args, **kwds):
        """
        Return vertices of ``self``.

        INPUT:

        - any arguments given will be passed on to the returned object.

        OUTPUT: a :class:`point collection <PointCollection>`

        EXAMPLES:

        Vertices of the octahedron and its polar cube are in dual lattices::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: o.vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: cube = o.polar()
            sage: cube.vertices()
            N( 1, -1, -1),
            N( 1,  1, -1),
            N( 1,  1,  1),
            N( 1, -1,  1),
            N(-1, -1,  1),
            N(-1, -1, -1),
            N(-1,  1, -1),
            N(-1,  1,  1)
            in 3-d lattice N
        """

def is_NefPartition(x):
    """
    Check if ``x`` is a nef-partition.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    - ``True`` if ``x`` is a :class:`nef-partition <NefPartition>` and
      ``False`` otherwise.

    EXAMPLES::

        sage: from sage.geometry.lattice_polytope import NefPartition
        sage: isinstance(1, NefPartition)
        False
        sage: o = lattice_polytope.cross_polytope(3)
        sage: np = o.nef_partitions()[0]; np                                            # needs palp
        Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
        sage: isinstance(np, NefPartition)                                              # needs palp
        True
    """

class NefPartition(SageObject, Hashable):
    '''
    Create a nef-partition.

    INPUT:

    - ``data`` -- list of integers, the `i`-th element of this list must be
      the part of the `i`-th vertex of ``Delta_polar`` in this nef-partition;

    - ``Delta_polar`` -- a :class:`lattice polytope
      <sage.geometry.lattice_polytope.LatticePolytopeClass>`;

    - ``check`` -- by default the input will be checked for correctness, i.e.
      that ``data`` indeed specify a nef-partition. If you are sure that the
      input is correct, you can speed up construction via ``check=False``
      option.

    OUTPUT: a nef-partition of ``Delta_polar``

    Let `M` and `N` be dual lattices. Let `\\Delta \\subset M_\\RR` be a reflexive
    polytope with polar `\\Delta^\\circ \\subset N_\\RR`. Let `X_\\Delta` be the
    toric variety associated to the normal fan of `\\Delta`. A **nef-partition**
    is a decomposition of the vertex set `V` of `\\Delta^\\circ` into a disjoint
    union `V = V_0 \\sqcup V_1 \\sqcup \\dots \\sqcup V_{k-1}` such that divisors
    `E_i = \\sum_{v\\in V_i} D_v` are Cartier (here `D_v` are prime
    torus-invariant Weil divisors corresponding to vertices of `\\Delta^\\circ`).
    Equivalently, let `\\nabla_i \\subset N_\\RR` be the convex hull of vertices
    from `V_i` and the origin. These polytopes form a nef-partition if their
    Minkowski sum `\\nabla \\subset N_\\RR` is a reflexive polytope.

    The **dual nef-partition** is formed by polytopes `\\Delta_i \\subset M_\\RR`
    of `E_i`, which give a decomposition of the vertex set of `\\nabla^\\circ
    \\subset M_\\RR` and their Minkowski sum is `\\Delta`, i.e. the polar duality
    of reflexive polytopes switches convex hull and Minkowski sum for dual
    nef-partitions:

    .. MATH::

        \\Delta^\\circ
        &=
        \\mathrm{Conv} \\left(\\nabla_0, \\nabla_1, \\dots, \\nabla_{k-1}\\right), \\\\\n        \\nabla^{\\phantom{\\circ}}
        &=
        \\nabla_0 + \\nabla_1 + \\dots + \\nabla_{k-1}, \\\\\n        &
        \\\\\n        \\Delta^{\\phantom{\\circ}}
        &=
        \\Delta_0 + \\Delta_1 + \\dots + \\Delta_{k-1}, \\\\\n        \\nabla^\\circ
        &=
        \\mathrm{Conv} \\left(\\Delta_0, \\Delta_1, \\dots, \\Delta_{k-1}\\right).

    One can also interpret the duality of nef-partitions as the duality of the
    associated cones. Below `\\overline{M} = M \\times \\ZZ^k` and
    `\\overline{N} = N \\times \\ZZ^k` are dual lattices.

    The **Cayley polytope** `P \\subset \\overline{M}_\\RR` of a nef-partition is
    given by `P = \\mathrm{Conv}(\\Delta_0 \\times e_0, \\Delta_1 \\times e_1,
    \\ldots, \\Delta_{k-1} \\times e_{k-1})`, where `\\{e_i\\}_{i=0}^{k-1}` is the
    standard basis of `\\ZZ^k`. The **dual Cayley polytope**
    `P^* \\subset \\overline{N}_\\RR` is the Cayley polytope of the dual
    nef-partition.

    The **Cayley cone** `C \\subset \\overline{M}_\\RR` of a nef-partition is the
    cone spanned by its Cayley polytope. The **dual Cayley cone**
    `C^\\vee \\subset \\overline{M}_\\RR` is the usual dual cone of `C`. It turns
    out, that `C^\\vee` is spanned by `P^*`.

    It is also possible to go back from the Cayley cone to the Cayley polytope,
    since `C` is a reflexive Gorenstein cone supported by `P`: primitive
    integral ray generators of `C` are contained in an affine hyperplane and
    coincide with vertices of `P`.

    See Section 4.3.1 in [CK1999]_ and references therein for further details, or
    [BN2008]_ for a purely combinatorial approach.

    EXAMPLES:

    It is very easy to create a nef-partition for the octahedron, since for
    this polytope any decomposition of vertices is a nef-partition. We create a
    3-part nef-partition with the 0th and 1st vertices belonging to the 0th
    part (recall that numeration in Sage starts with 0), the 2nd and 5th
    vertices belonging to the 1st part, and 3rd and 4th vertices belonging
    to the 2nd part::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: np = NefPartition([0,0,1,2,2,1], o)
        sage: np
        Nef-partition {0, 1} ⊔ {2, 5} ⊔ {3, 4}

    The octahedron plays the role of `\\Delta^\\circ` in the above description::

        sage: np.Delta_polar() is o
        True

    The dual nef-partition (corresponding to the "mirror complete
    intersection") gives decomposition of the vertex set of `\\nabla^\\circ`::

        sage: np.dual()
        Nef-partition {0, 1, 2} ⊔ {3, 4} ⊔ {5, 6, 7}
        sage: np.nabla_polar().vertices()
        N(-1, -1,  0),
        N(-1,  0,  0),
        N( 0, -1,  0),
        N( 0,  0, -1),
        N( 0,  0,  1),
        N( 1,  0,  0),
        N( 0,  1,  0),
        N( 1,  1,  0)
        in 3-d lattice N

    Of course, `\\nabla^\\circ` is `\\Delta^\\circ` from the point of view of the
    dual nef-partition::

        sage: np.dual().Delta_polar() is np.nabla_polar()
        True
        sage: np.Delta(1).vertices()
        N(0, 0, -1),
        N(0, 0,  1)
        in 3-d lattice N
        sage: np.dual().nabla(1).vertices()
        N(0, 0, -1),
        N(0, 0,  1)
        in 3-d lattice N

    Instead of constructing nef-partitions directly, you can request all 2-part
    nef-partitions of a given reflexive polytope (they will be computed using
    ``nef.x`` program from PALP)::

        sage: o.nef_partitions()                                                        # needs palp
        [Nef-partition {0, 1, 3} ⊔ {2, 4, 5},
         Nef-partition {0, 1, 3, 4} ⊔ {2, 5} (direct product),
         Nef-partition {0, 1, 2} ⊔ {3, 4, 5},
         Nef-partition {0, 1, 2, 3} ⊔ {4, 5},
         Nef-partition {0, 1, 2, 3, 4} ⊔ {5} (projection)]
    '''
    def __init__(self, data, Delta_polar, check: bool = True) -> None:
        """
        See :class:`NefPartition` for documentation.

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = o.nef_partitions()[0]                                            # needs palp
            sage: TestSuite(np).run()                                                   # needs palp
        """
    def __eq__(self, other):
        """
        Compare ``self`` with ``other``.

        INPUT:

        - ``other`` -- anything

        OUTPUT:

        - ``True`` if ``other`` is a :class:`nef-partition <NefPartition>`
          equal to ``self``, ``False`` otherwise.

        .. NOTE::

            Two nef-partitions are equal if they correspond to equal polytopes
            and their parts are the same, including their order.

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o)
            sage: np == np
            True
            sage: np == o.nef_partitions()[0]                                           # needs palp
            True
            sage: np == o.nef_partitions()[1]                                           # needs palp
            False
            sage: np2 = NefPartition(np._vertex_to_part, o)
            sage: np2 is np
            False
            sage: np2 == np
            True
            sage: np == 0
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        OUTPUT: integer

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o)
            sage: hash(np) == hash(np)
            True
        """
    def __ne__(self, other):
        """
        Compare ``self`` with ``other``.

        INPUT:

        - ``other`` -- anything

        OUTPUT:

        - ``False`` if ``other`` is a :class:`nef-partition <NefPartition>`
          equal to ``self``, ``True`` otherwise.

        .. NOTE::

            Two nef-partitions are equal if they correspond to equal polytopes
            and their parts are the same, including their order.

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o)
            sage: np != np
            False
            sage: np != o.nef_partitions()[0]                                           # needs palp
            False
            sage: np != o.nef_partitions()[1]                                           # needs palp
            True
            sage: np2 = NefPartition(np._vertex_to_part, o)
            sage: np2 is np
            False
            sage: np2 != np
            False
            sage: np != 0
            True
        """
    def Delta(self, i=None):
        """
        Return the polytope `\\Delta` or `\\Delta_i` corresponding to ``self``.

        INPUT:

        - ``i`` -- integer; if not given, `\\Delta` will be returned

        OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.Delta().polar() is o
            True
            sage: np.Delta().vertices()
            N( 1, -1, -1),
            N( 1,  1, -1),
            N( 1,  1,  1),
            N( 1, -1,  1),
            N(-1, -1,  1),
            N(-1, -1, -1),
            N(-1,  1, -1),
            N(-1,  1,  1)
            in 3-d lattice N
            sage: np.Delta(0).vertices()
            N(-1, -1, 0),
            N(-1,  0, 0),
            N( 1,  0, 0),
            N( 1, -1, 0)
            in 3-d lattice N
        """
    def Delta_polar(self):
        """
        Return the polytope `\\Delta^\\circ` corresponding to ``self``.

        OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.Delta_polar() is o
            True
        """
    def Deltas(self):
        """
        Return the polytopes `\\Delta_i` corresponding to ``self``.

        OUTPUT: a tuple of :class:`lattice polytopes <LatticePolytopeClass>`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.Delta().vertices()
            N( 1, -1, -1),
            N( 1,  1, -1),
            N( 1,  1,  1),
            N( 1, -1,  1),
            N(-1, -1,  1),
            N(-1, -1, -1),
            N(-1,  1, -1),
            N(-1,  1,  1)
            in 3-d lattice N
            sage: [Delta_i.vertices() for Delta_i in np.Deltas()]
            [N(-1, -1, 0),
             N(-1,  0, 0),
             N( 1,  0, 0),
             N( 1, -1, 0)
             in 3-d lattice N,
             N(0, 0, -1),
             N(0, 1,  1),
             N(0, 0,  1),
             N(0, 1, -1)
             in 3-d lattice N]
            sage: np.nabla_polar().vertices()
            N(-1, -1,  0),
            N( 1, -1,  0),
            N( 1,  0,  0),
            N(-1,  0,  0),
            N( 0,  1, -1),
            N( 0,  1,  1),
            N( 0,  0,  1),
            N( 0,  0, -1)
            in 3-d lattice N
        """
    @cached_method
    def dual(self):
        """
        Return the dual nef-partition.

        OUTPUT: a :class:`nef-partition <NefPartition>`

        See the class documentation for the definition.

        ALGORITHM:

        See Proposition 3.19 in [BN2008]_.

        .. NOTE::

            Automatically constructed dual nef-partitions will be ordered, i.e.
            vertex partition of `\\nabla` will look like
            `\\{0, 1, 2\\} \\sqcup \\{3, 4, 5, 6\\} \\sqcup \\{7, 8\\}`.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.dual()
            Nef-partition {0, 1, 2, 3} ⊔ {4, 5, 6, 7}
            sage: np.dual().Delta() is np.nabla()
            True
            sage: np.dual().nabla(0) is np.Delta(0)
            True
        """
    def hodge_numbers(self):
        """
        Return Hodge numbers corresponding to ``self``.

        OUTPUT: a tuple of integers (produced by ``nef.x`` program from PALP)

        EXAMPLES:

        Currently, you need to request Hodge numbers when you compute
        nef-partitions::

            sage: # long time, needs palp
            sage: p = lattice_polytope.cross_polytope(5)
            sage: np = p.nef_partitions()[0]                    # 4s on sage.math, 2011
            sage: np.hodge_numbers()
            Traceback (most recent call last):
            ...
            NotImplementedError: use nef_partitions(hodge_numbers=True)!
            sage: np = p.nef_partitions(hodge_numbers=True)[0]  # 13s on sage.math, 2011
            sage: np.hodge_numbers()
            (19, 19)
        """
    def nabla(self, i=None):
        """
        Return the polytope `\\nabla` or `\\nabla_i` corresponding to ``self``.

        INPUT:

        - ``i`` -- integer; if not given, `\\nabla` will be returned

        OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.Delta_polar().vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: np.nabla(0).vertices()
            M(-1, 0, 0),
            M( 1, 0, 0),
            M( 0, 1, 0)
            in 3-d lattice M
            sage: np.nabla().vertices()
            M(-1,  0,  1),
            M(-1,  0, -1),
            M( 1,  0,  1),
            M( 1,  0, -1),
            M( 0,  1,  1),
            M( 0,  1, -1),
            M( 1, -1,  0),
            M(-1, -1,  0)
            in 3-d lattice M
        """
    def nabla_polar(self):
        """
        Return the polytope `\\nabla^\\circ` corresponding to ``self``.

        OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.nabla_polar().vertices()
            N(-1, -1,  0),
            N( 1, -1,  0),
            N( 1,  0,  0),
            N(-1,  0,  0),
            N( 0,  1, -1),
            N( 0,  1,  1),
            N( 0,  0,  1),
            N( 0,  0, -1)
            in 3-d lattice N
            sage: np.nabla_polar() is np.dual().Delta_polar()
            True
        """
    def nablas(self):
        """
        Return the polytopes `\\nabla_i` corresponding to ``self``.

        OUTPUT: a tuple of :class:`lattice polytopes <LatticePolytopeClass>`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.Delta_polar().vertices()
            M( 1,  0,  0),
            M( 0,  1,  0),
            M( 0,  0,  1),
            M(-1,  0,  0),
            M( 0, -1,  0),
            M( 0,  0, -1)
            in 3-d lattice M
            sage: [nabla_i.vertices() for nabla_i in np.nablas()]
            [M(-1, 0, 0),
             M( 1, 0, 0),
             M( 0, 1, 0)
             in 3-d lattice M,
             M(0, -1,  0),
             M(0,  0, -1),
             M(0,  0,  1)
             in 3-d lattice M]
        """
    def nparts(self):
        """
        Return the number of parts in ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.nparts()
            2
        """
    def part(self, i, all_points: bool = False):
        """
        Return the ``i``-th part of ``self``.

        INPUT:

        - ``i`` -- integer

        - ``all_points`` -- boolean (default: ``False``); whether to list all lattice points
          or just vertices

        OUTPUT:

        - a tuple of integers, indices of vertices (or all lattice points) of
          `\\Delta^\\circ` belonging to `V_i`.

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.part(0)
            (0, 1, 3)
            sage: np.part(0, all_points=True)                                           # needs palp
            (0, 1, 3)
            sage: np.dual().part(0)
            (0, 1, 2, 3)
            sage: np.dual().part(0, all_points=True)                                    # needs palp
            (0, 1, 2, 3, 8)
        """
    @cached_method
    def parts(self, all_points: bool = False):
        """
        Return all parts of ``self``.

        INPUT:

        - ``all_points`` -- boolean (default: ``False``); whether to list all lattice points
          or just vertices

        OUTPUT:

        - a tuple of tuples of integers. The `i`-th tuple contains indices of
          vertices (or all lattice points) of `\\Delta^\\circ` belonging to `V_i`

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.parts()
            ((0, 1, 3), (2, 4, 5))
            sage: np.parts(all_points=True)                                             # needs palp
            ((0, 1, 3), (2, 4, 5))
            sage: np.dual().parts()
            ((0, 1, 2, 3), (4, 5, 6, 7))
            sage: np.dual().parts(all_points=True)                                      # needs palp
            ((0, 1, 2, 3, 8), (4, 5, 6, 7, 10))
        """
    def part_of(self, i):
        """
        Return the index of the part containing the ``i``-th vertex.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        - an integer `j` such that the ``i``-th vertex of `\\Delta^\\circ`
          belongs to `V_j`.

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = NefPartition([0, 0, 1, 0, 1, 1], o); np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: np.part_of(3)
            0
            sage: np.part_of(2)
            1
        """
    @cached_method
    def part_of_point(self, i):
        """
        Return the index of the part containing the ``i``-th point.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        - an integer `j` such that the ``i``-th point of `\\Delta^\\circ`
          belongs to `\\nabla_j`.

        .. NOTE::

            Since a nef-partition induces a partition on the set of boundary
            lattice points of `\\Delta^\\circ`, the value of `j` is well-defined
            for all `i` but the one that corresponds to the origin, in which
            case this method will raise a :exc:`ValueError` exception.
            (The origin always belongs to all `\\nabla_j`.)

        See :class:`nef-partition <NefPartition>` class documentation for
        definitions and notation.

        EXAMPLES:

        We consider a relatively complicated reflexive polytope #2252 (easily
        accessible in Sage as ``ReflexivePolytope(3, 2252)``, we create it here
        explicitly to avoid loading the whole database)::

            sage: p = LatticePolytope([(1,0,0), (0,1,0), (0,0,1), (0,1,-1),
            ....:         (0,-1,1), (-1,1,0), (0,-1,-1), (-1,-1,0), (-1,-1,2)])
            sage: np = p.nef_partitions()[0]; np                                        # needs palp
            Nef-partition {1, 2, 5, 7, 8} ⊔ {0, 3, 4, 6}
            sage: p.nvertices()
            9
            sage: p.npoints()                                                           # needs palp
            15

        We see that the polytope has 6 more points in addition to vertices. One
        of them is the origin::

            sage: p.origin()                                                            # needs palp
            14
            sage: np.part_of_point(14)                                                  # needs palp
            Traceback (most recent call last):
            ...
            ValueError: the origin belongs to all parts!

        But the remaining 5 are partitioned by ``np``::

            sage: [n for n in range(p.npoints())                                        # needs palp
            ....:    if p.origin() != n and np.part_of_point(n) == 0]
            [1, 2, 5, 7, 8, 9, 11, 13]
            sage: [n for n in range(p.npoints())                                        # needs palp
            ....:    if p.origin() != n and np.part_of_point(n) == 1]
            [0, 3, 4, 6, 10, 12]
        """

def all_cached_data(polytopes) -> None:
    """
    Compute all cached data for all given ``polytopes`` and
    their polars.

    This functions does it MUCH faster than member functions of
    ``LatticePolytope`` during the first run. So it is recommended to
    use this functions if you work with big sets of data. None of the
    polytopes in the given sequence should be constructed as the polar
    polytope to another one.

    INPUT:

    - ``polytopes`` -- a sequence of lattice polytopes

    EXAMPLES: This function has no output, it is just a fast way to
    work with long sequences of polytopes. Of course, you can use short
    sequences as well::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: lattice_polytope.all_cached_data([o])                                     # needs palp
    """
def all_nef_partitions(polytopes, keep_symmetric: bool = False) -> None:
    """
    Compute nef-partitions for all given ``polytopes``.

    This functions does it MUCH faster than member functions of
    ``LatticePolytope`` during the first run. So it is recommended to
    use this functions if you work with big sets of data.

    Note: member function ``is_reflexive`` will be called
    separately for each polytope. It is strictly recommended to call
    ``all_polars`` on the sequence of
    ``polytopes`` before using this function.

    INPUT:

    - ``polytopes`` -- a sequence of lattice polytopes

    EXAMPLES: This function has no output, it is just a fast way to
    work with long sequences of polytopes. Of course, you can use short
    sequences as well::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: lattice_polytope.all_nef_partitions([o])                                  # needs palp
        sage: o.nef_partitions()                                                        # needs palp
        [Nef-partition {0, 1, 3} ⊔ {2, 4, 5},
         Nef-partition {0, 1, 3, 4} ⊔ {2, 5} (direct product),
         Nef-partition {0, 1, 2} ⊔ {3, 4, 5},
         Nef-partition {0, 1, 2, 3} ⊔ {4, 5},
         Nef-partition {0, 1, 2, 3, 4} ⊔ {5} (projection)]

    You cannot use this function for non-reflexive polytopes::

        sage: p = LatticePolytope([(1,0,0), (0,1,0), (0,0,2),
        ....:                      (-1,0,0), (0,-1,0), (0,0,-1)])
        sage: lattice_polytope.all_nef_partitions([o, p])                               # needs palp
        Traceback (most recent call last):
        ...
        ValueError: nef-partitions can be computed for reflexive polytopes only
    """
def all_points(polytopes) -> None:
    """
    Compute lattice points for all given ``polytopes``.

    This functions does it MUCH faster than member functions of
    ``LatticePolytope`` during the first run. So it is recommended to
    use this functions if you work with big sets of data.

    INPUT:

    - ``polytopes`` -- a sequence of lattice polytopes

    EXAMPLES: This function has no output, it is just a fast way to
    work with long sequences of polytopes. Of course, you can use short
    sequences as well::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: lattice_polytope.all_points([o])                                          # needs palp
        sage: o.points()                                                                # needs palp
        M( 1,  0,  0),
        M( 0,  1,  0),
        M( 0,  0,  1),
        M(-1,  0,  0),
        M( 0, -1,  0),
        M( 0,  0, -1),
        M( 0,  0,  0)
        in 3-d lattice M
    """
def all_polars(polytopes) -> None:
    """
    Compute polar polytopes for all reflexive and equations of facets
    for all non-reflexive ``polytopes``.

    ``all_facet_equations`` and ``all_polars`` are synonyms.

    This functions does it MUCH faster than member functions of
    ``LatticePolytope`` during the first run. So it is recommended to
    use this functions if you work with big sets of data.

    INPUT:

    - ``polytopes`` -- a sequence of lattice polytopes

    EXAMPLES: This function has no output, it is just a fast way to
    work with long sequences of polytopes. Of course, you can use short
    sequences as well::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: lattice_polytope.all_polars([o])                                          # needs palp
        sage: o.polar()                                                                 # needs palp
        3-d reflexive polytope in 3-d lattice N
    """
all_facet_equations = all_polars

def convex_hull(points):
    """
    Compute the convex hull of the given points.

    .. NOTE::

        ``points`` might not span the space. Also, it fails for large
        numbers of vertices in dimensions 4 or greater

    INPUT:

    - ``points`` -- list that can be converted into
      vectors of the same dimension over `\\ZZ`

    OUTPUT: list of vertices of the convex hull of the given points (as vectors)

    EXAMPLES: Let's compute the convex hull of several points on a line
    in the plane::

        sage: lattice_polytope.convex_hull([[1,2],[3,4],[5,6],[7,8]])
        [(1, 2), (7, 8)]
    """
def cross_polytope(dim):
    """
    Return a cross-polytope of the given dimension.

    INPUT:

    - ``dim`` -- integer

    OUTPUT: a :class:`lattice polytope <LatticePolytopeClass>`

    EXAMPLES::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: o
        3-d reflexive polytope in 3-d lattice M
        sage: o.vertices()
        M( 1,  0,  0),
        M( 0,  1,  0),
        M( 0,  0,  1),
        M(-1,  0,  0),
        M( 0, -1,  0),
        M( 0,  0, -1)
        in 3-d lattice M
    """
def minkowski_sum(points1, points2):
    """
    Compute the Minkowski sum of two convex polytopes.

    .. NOTE::

        Polytopes might not be of maximal dimension.

    INPUT:

    - ``points1``, ``points2`` -- lists of objects that can be
      converted into vectors of the same dimension, treated as vertices
      of two polytopes.

    OUTPUT: list of vertices of the Minkowski sum, given as vectors

    EXAMPLES: Let's compute the Minkowski sum of two line segments::

        sage: lattice_polytope.minkowski_sum([[1,0],[-1,0]],[[0,1],[0,-1]])
        [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    """
def positive_integer_relations(points):
    """
    Return relations between given points.

    INPUT:

    - ``points`` -- lattice points given as columns of a matrix

    OUTPUT: matrix of relations between given points with nonnegative
    integer coefficients

    EXAMPLES: This is a 3-dimensional reflexive polytope::

        sage: p = LatticePolytope([(1,0,0), (0,1,0),
        ....:                      (-1,-1,0), (0,0,1), (-1,0,-1)])
        sage: p.points()                                                                # needs palp
        M( 1,  0,  0),
        M( 0,  1,  0),
        M(-1, -1,  0),
        M( 0,  0,  1),
        M(-1,  0, -1),
        M( 0,  0,  0)
        in 3-d lattice M

    We can compute linear relations between its points in the following
    way::

        sage: p.points().matrix().kernel().echelonized_basis_matrix()                   # needs palp
        [ 1  0  0  1  1  0]
        [ 0  1  1 -1 -1  0]
        [ 0  0  0  0  0  1]

    However, the above relations may contain negative and rational
    numbers. This function transforms them in such a way, that all
    coefficients are nonnegative integers::

        sage: points = p.points().column_matrix()
        sage: lattice_polytope.positive_integer_relations(points)                       # needs palp
        [1 0 0 1 1 0]
        [1 1 1 0 0 0]
        [0 0 0 0 0 1]

        sage: cm = ReflexivePolytope(2,1).vertices().column_matrix()
        sage: lattice_polytope.positive_integer_relations(cm)
        [2 1 1]
    """
def read_all_polytopes(file_name):
    '''
    Read all polytopes from the given file.

    INPUT:

    - ``file_name`` -- string with the name of a file with VERTICES of
      polytopes

    OUTPUT: a sequence of polytopes

    EXAMPLES:

    We use ``poly.x`` to compute two polar polytopes and read them::

        sage: # needs palp
        sage: d = lattice_polytope.cross_polytope(2)
        sage: o = lattice_polytope.cross_polytope(3)
        sage: result_name = lattice_polytope._palp("poly.x -fe", [d, o])
        sage: with open(result_name) as f:
        ....:     print(f.read())
        4 2  Vertices of P-dual <-> Equations of P
          -1   1
           1   1
          -1  -1
           1  -1
        8 3  Vertices of P-dual <-> Equations of P
          -1  -1   1
           1  -1   1
          -1   1   1
           1   1   1
          -1  -1  -1
           1  -1  -1
          -1   1  -1
           1   1  -1
        sage: lattice_polytope.read_all_polytopes(result_name)
        [2-d reflexive polytope #14 in 2-d lattice M,
         3-d reflexive polytope in 3-d lattice M]
        sage: os.remove(result_name)
    '''
def read_palp_matrix(data, permutation: bool = False):
    '''
    Read and return an integer matrix from a string or an opened file.

    First input line must start with two integers m and n, the number
    of rows and columns of the matrix. The rest of the first line is
    ignored. The next m lines must contain n numbers each.

    If m>n, returns the transposed matrix. If the string is empty or EOF
    is reached, returns the empty matrix, constructed by
    ``matrix()``.

    INPUT:

    - ``data`` -- either a string containing the filename or the file itself
      containing the output by PALP

    - ``permutation`` -- boolean (default: ``False``); if ``True``, try to retrieve
      the permutation output by PALP. This parameter makes sense only
      when PALP computed the normal form of a lattice polytope.

    OUTPUT: a matrix or a tuple of a matrix and a permutation

    EXAMPLES::

        sage: lattice_polytope.read_palp_matrix("2 3 comment \\n 1 2 3 \\n 4 5 6")
        [1 2 3]
        [4 5 6]
        sage: lattice_polytope.read_palp_matrix("3 2 Will be transposed \\n 1 2 \\n 3 4 \\n 5 6")
        [1 3 5]
        [2 4 6]
    '''
def set_palp_dimension(d) -> None:
    '''
    Set the dimension for PALP calls to ``d``.

    INPUT:

    - ``d`` -- integer from the list ``[4,5,6,11]`` or ``None``

    OUTPUT: none

    PALP has many hard-coded limits, which must be specified before
    compilation, one of them is dimension. Sage includes several versions with
    different dimension settings (which may also affect other limits and enable
    certain features of PALP). You can change the version which will be used by
    calling this function. Such a change is not done automatically for each
    polytope based on its dimension, since depending on what you are doing it
    may be necessary to use dimensions higher than that of the input polytope.

    EXAMPLES:

    Let\'s try to work with a 7-dimensional polytope::

        sage: p = lattice_polytope.cross_polytope(7)
        sage: p._palp("poly.x -fv")                                                     # needs palp
        Traceback (most recent call last):
        ...
        ValueError: Error executing \'poly.x -fv\' for the given polytope!
        Output:
        Please increase POLY_Dmax to at least 7

    However, we can work with this polytope by changing PALP dimension to 11::

        sage: lattice_polytope.set_palp_dimension(11)
        sage: p._palp("poly.x -fv")                                                     # needs palp
        \'7 14  Vertices of P...\'

    Let\'s go back to default settings::

        sage: lattice_polytope.set_palp_dimension(None)
    '''
def skip_palp_matrix(data, n: int = 1) -> None:
    '''
    Skip matrix data in a file.

    INPUT:

    - ``data`` -- opened file with blocks of matrix data in
      the following format: A block consisting of m+1 lines has the
      number m as the first element of its first line.

    - ``n`` -- (default: 1) integer, specifies how many
      blocks should be skipped

    If EOF is reached during the process, raises :exc:`ValueError` exception.

    EXAMPLES: We create a file with vertices of the square and the cube,
    but read only the second set::

        sage: # needs palp
        sage: d = lattice_polytope.cross_polytope(2)
        sage: o = lattice_polytope.cross_polytope(3)
        sage: result_name = lattice_polytope._palp("poly.x -fe", [d, o])
        sage: with open(result_name) as f:
        ....:     print(f.read())
        4 2  Vertices of P-dual <-> Equations of P
          -1   1
           1   1
          -1  -1
           1  -1
        8 3  Vertices of P-dual <-> Equations of P
          -1  -1   1
           1  -1   1
          -1   1   1
           1   1   1
          -1  -1  -1
           1  -1  -1
          -1   1  -1
           1   1  -1
        sage: f = open(result_name)
        sage: lattice_polytope.skip_palp_matrix(f)
        sage: lattice_polytope.read_palp_matrix(f)
        [-1  1 -1  1 -1  1 -1  1]
        [-1 -1  1  1 -1 -1  1  1]
        [ 1  1  1  1 -1 -1 -1 -1]
        sage: f.close()
        sage: os.remove(result_name)
    '''
def write_palp_matrix(m, ofile=None, comment: str = '', format=None) -> None:
    '''
    Write ``m`` into ``ofile`` in PALP format.

    INPUT:

    - ``m`` -- a matrix over integers or a
      :class:`point collection <PointCollection>`

    - ``ofile`` -- a file opened for writing (default: ``stdout``)

    - ``comment`` -- string (default: empty); see output description

    - ``format`` -- a format string used to print matrix entries

    OUTPUT: nothing is returned, output written to ``ofile`` has the format

      * First line: number_of_rows number_of_columns comment
      * Next number_of_rows lines: rows of the matrix.

    EXAMPLES::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: lattice_polytope.write_palp_matrix(o.vertices(), comment="3D Octahedron")
        3 6 3D Octahedron
         1  0  0 -1  0  0
         0  1  0  0 -1  0
         0  0  1  0  0 -1
        sage: lattice_polytope.write_palp_matrix(o.vertices(), format=\'%4d\')
        3 6
           1    0    0   -1    0    0
           0    1    0    0   -1    0
           0    0    1    0    0   -1
    '''
