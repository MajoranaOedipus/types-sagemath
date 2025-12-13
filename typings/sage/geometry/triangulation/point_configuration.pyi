from _typeshed import Incomplete
from collections.abc import Generator
from sage.features import FeatureNotPresentError as FeatureNotPresentError
from sage.features.topcom import TOPCOMExecutable as TOPCOMExecutable
from sage.geometry.triangulation.base import ConnectedTriangulationsIterator as ConnectedTriangulationsIterator, Point as Point, PointConfiguration_base as PointConfiguration_base
from sage.geometry.triangulation.element import Triangulation as Triangulation
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PointConfiguration(UniqueRepresentation, PointConfiguration_base):
    """
    A collection of points in Euclidean (or projective) space.

    This is the parent class for the triangulations of the point
    configuration. There are a few options to specifically select what
    kind of triangulations are admissible.

    INPUT:

    The constructor accepts the following arguments:

    - ``points`` -- the points; technically, any iterable of iterables
      will do. In particular, a :class:`PointConfiguration` can be passed.

    - ``projective`` -- boolean (default: ``False``); whether the
      point coordinates should be interpreted as projective (``True``)
      or affine (``False``) coordinates. If necessary, points are
      projectivized by setting the last homogeneous coordinate to one
      and/or affine patches are chosen internally.

    - ``connected`` -- boolean (default: ``True``); whether the
      triangulations should be connected to the regular triangulations
      via bistellar flips. These are much easier to compute than all
      triangulations.

    - ``fine`` -- boolean (default: ``False``); whether the
      triangulations must be fine, that is, make use of all points of
      the configuration

    - ``regular`` -- boolean or ``None`` (default: ``None``); whether
      the triangulations must be regular. A regular triangulation is
      one that is induced by a piecewise-linear convex support
      function. In other words, the shadows of the faces of a
      polyhedron in one higher dimension.

      * ``True``: Only regular triangulations.

      * ``False``: Only non-regular triangulations.

      * ``None`` (default): Both kinds of triangulation.

    - ``star`` -- either ``None`` or a point; whether the
      triangulations must be star. A triangulation is star if all
      maximal simplices contain a common point. The central point can
      be specified by its index (an integer) in the given points or by
      its coordinates (anything iterable.)

    EXAMPLES::

        sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]]); p
        A point configuration in affine 2-space over Integer Ring
        consisting of 5 points. The triangulations of this point
        configuration are assumed to be connected, not necessarily fine,
        not necessarily regular.
        sage: p.triangulate()  # a single triangulation
        (<1,3,4>, <2,3,4>)
    """
    @staticmethod
    def __classcall__(cls, points, projective: bool = False, connected: bool = True, fine: bool = False, regular=None, star=None):
        """
        Normalize the constructor arguments to be unique keys.

        EXAMPLES::

            sage: pc1 = PointConfiguration([[1,2], [2,3], [3,4]], connected=True)
            sage: pc2 = PointConfiguration(((1,2), (2,3), (3,4)), regular=None)
            sage: pc1 is pc2   # indirect doctest
            True
        """
    def __init__(self, points, connected, fine, regular, star, defined_affine) -> None:
        """
        Initialize a :class:`PointConfiguration` object.

        EXAMPLES::

            sage: p = PointConfiguration([[0,4], [2,3], [3,2], [4,0], [3,-2], [2,-3],
            ....:                         [0,-4], [-2,-3], [-3,-2], [-4,0], [-3,2], [-2,3]])
            sage: len(p.triangulations_list())  # long time (26s on sage.math, 2012)
            16796

        TESTS::

            sage: TestSuite(p).run()
        """
    @classmethod
    def set_engine(cls, engine: str = 'auto') -> None:
        """
        Set the engine used to compute triangulations.

        INPUT:

        - ``engine`` -- either ``'auto'`` (default), ``'internal'``, or
          ``'topcom'``. The latter two instruct this package to always use
          its own triangulation algorithms or TOPCOM's algorithms,
          respectively. By default (``'auto'``), internal routines are used.

        EXAMPLES::

            sage: # optional - topcom
            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: p.set_engine('internal')   # to make doctests independent of TOPCOM
            sage: p.triangulate()
            (<1,3,4>, <2,3,4>)
            sage: p.set_engine('topcom')
            sage: p.triangulate()
            (<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)
            sage: p.set_engine('internal')
        """
    def star_center(self):
        """
        Return the center used for star triangulations.

        .. SEEALSO:: :meth:`restrict_to_star_triangulations`.

        OUTPUT:

        A :class:`~sage.geometry.triangulation.base.Point` if a
        distinguished star central point has been fixed.
        :exc:`ValueError` exception is raised otherwise.

        EXAMPLES::

            sage: pc = PointConfiguration([(1,0), (-1,0), (0,1), (0,2)], star=(0,1)); pc
            A point configuration in affine 2-space over Integer Ring
            consisting of 4 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular, and star with center P(0, 1).
            sage: pc.star_center()
            P(0, 1)

            sage: pc_nostar = pc.restrict_to_star_triangulations(None); pc_nostar
            A point configuration in affine 2-space over Integer Ring
            consisting of 4 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: pc_nostar.star_center()
            Traceback (most recent call last):
            ...
            ValueError: The point configuration has no star center defined.
        """
    def __reduce__(self):
        """
        Override __reduce__ to correctly pickle/unpickle.

        TESTS::

            sage: p = PointConfiguration([[0, 1], [0, 0], [1, 0], [1,1]])
            sage: loads(p.dumps()) is p
            True

            sage: p = PointConfiguration([[0, 1, 1], [0, 0, 1], [1, 0, 1], [1,1, 1]],
            ....:                        projective=True)
            sage: loads(p.dumps()) is p
            True
        """
    def an_element(self):
        """
        Synonymous for :meth:`triangulate`.

        TESTS::

            sage: p = PointConfiguration([[0, 1], [0, 0], [1, 0], [1,1]])
            sage: p.an_element()
            (<0,1,3>, <1,2,3>)
        """
    Element = Triangulation
    def __iter__(self):
        """
        Iterate through the points of the point configuration.

        OUTPUT:

        Returns projective coordinates of the points. See also the
        ``PointConfiguration.points()`` method, which returns affine
        coordinates.

        EXAMPLES::

            sage: p = PointConfiguration([[1,1], [2,2], [3,3]])
            sage: list(p)     # indirect doctest
            [P(1, 1), P(2, 2), P(3, 3)]
            sage: [p[i] for i in range(p.n_points())]
            [P(1, 1), P(2, 2), P(3, 3)]
            sage: list(p.points())
            [P(1, 1), P(2, 2), P(3, 3)]
            sage: [p.point(i) for i in range(p.n_points())]
            [P(1, 1), P(2, 2), P(3, 3)]
        """
    def restrict_to_regular_triangulations(self, regular: bool = True):
        """
        Restrict to regular triangulations.

        NOTE:

        Regularity testing requires the optional TOPCOM package.

        INPUT:

        - ``regular`` -- ``True``, ``False``, or ``None``; whether to
          restrict to regular triangulations, irregular
          triangulations, or lift any restrictions on regularity

        OUTPUT:

        A new :class:`PointConfiguration` with the same points, but
        whose triangulations will all be regular as specified. See
        :class:`PointConfiguration` for details.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]]); p
            A point configuration in affine 2-space over Integer Ring
            consisting of 5 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: len(p.triangulations_list())
            4
            sage: PointConfiguration.set_engine('topcom')
            sage: p_regular = p.restrict_to_regular_triangulations() # optional - topcom
            sage: len(p_regular.triangulations_list())               # optional - topcom
            4
            sage: p == p_regular.restrict_to_regular_triangulations(regular=None) # optional - topcom
            True
            sage: PointConfiguration.set_engine('internal')
        """
    def restrict_to_connected_triangulations(self, connected: bool = True):
        """
        Restrict to connected triangulations.

        NOTE:

        Finding non-connected triangulations requires the optional
        TOPCOM package.

        INPUT:

        - ``connected`` -- boolean; whether to restrict to
          triangulations that are connected by bistellar flips to the
          regular triangulations

        OUTPUT:

        A new :class:`PointConfiguration` with the same points, but
        whose triangulations will all be in the connected
        component. See :class:`PointConfiguration` for details.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]]); p
            A point configuration in affine 2-space over Integer Ring
            consisting of 5 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: len(p.triangulations_list())
            4
            sage: PointConfiguration.set_engine('topcom')
            sage: p_all = p.restrict_to_connected_triangulations(connected=False)  # optional - topcom
            sage: len(p_all.triangulations_list())                                 # optional - topcom
            4
            sage: p == p_all.restrict_to_connected_triangulations(connected=True)  # optional - topcom
            True
            sage: PointConfiguration.set_engine('internal')
        """
    def restrict_to_fine_triangulations(self, fine: bool = True):
        """
        Restrict to fine triangulations.

        INPUT:

        - ``fine`` -- boolean; whether to restrict to fine triangulations

        OUTPUT:

        A new :class:`PointConfiguration` with the same points, but
        whose triangulations will all be fine. See
        :class:`PointConfiguration` for details.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: p
            A point configuration in affine 2-space over Integer Ring
            consisting of 5 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.

            sage: len(p.triangulations_list())
            4
            sage: p_fine = p.restrict_to_fine_triangulations()
            sage: len(p.triangulations_list())
            4
            sage: p == p_fine.restrict_to_fine_triangulations(fine=False)
            True
        """
    def restrict_to_star_triangulations(self, star):
        """
        Restrict to star triangulations with the given point as the
        center.

        INPUT:

        - ``origin`` -- ``None`` or an integer or the coordinates of a
          point. An integer denotes the index of the central point. If
          ``None`` is passed, any restriction on the starshape will be
          removed.

        OUTPUT:

        A new :class:`PointConfiguration` with the same points, but
        whose triangulations will all be star. See
        :class:`PointConfiguration` for details.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: len(list(p.triangulations()))
            4
            sage: p_star =  p.restrict_to_star_triangulations(0)
            sage: p_star is p.restrict_to_star_triangulations((0,0))
            True
            sage: p_star.triangulations_list()
            [(<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>)]
            sage: p_newstar = p_star.restrict_to_star_triangulations(1)  # pick different origin
            sage: p_newstar.triangulations_list()
            [(<1,2,3>, <1,2,4>)]
            sage: p == p_star.restrict_to_star_triangulations(star=None)
            True
        """
    def triangulations(self, verbose: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        Return all triangulations.

        - ``verbose`` -- boolean (default: ``False``); whether to
          print out the TOPCOM interaction, if any

        OUTPUT:

        A generator for the triangulations satisfying all the
        restrictions imposed. Each triangulation is returned as a
        :class:`~sage.geometry.triangulation.element.Triangulation` object.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: iter = p.triangulations()
            sage: next(iter)
            (<1,3,4>, <2,3,4>)
            sage: next(iter)
            (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>)
            sage: next(iter)
            (<1,2,3>, <1,2,4>)
            sage: next(iter)
            (<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)
            sage: p.triangulations_list()
            [(<1,3,4>, <2,3,4>),
             (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>),
             (<1,2,3>, <1,2,4>),
             (<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)]
            sage: p_fine = p.restrict_to_fine_triangulations()
            sage: p_fine.triangulations_list()
            [(<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>),
             (<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)]

         Note that we explicitly asked the internal algorithm to
         compute the triangulations. Using TOPCOM, we obtain the same
         triangulations but in a different order::

            sage: # optional - topcom
            sage: p.set_engine('topcom')
            sage: iter = p.triangulations()
            sage: next(iter)
            (<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)
            sage: next(iter)
            (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>)
            sage: next(iter)
            (<1,2,3>, <1,2,4>)
            sage: next(iter)
            (<1,3,4>, <2,3,4>)
            sage: p.triangulations_list()
            [(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>),
             (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>),
             (<1,2,3>, <1,2,4>),
             (<1,3,4>, <2,3,4>)]
            sage: p_fine = p.restrict_to_fine_triangulations()
            sage: p_fine.set_engine('topcom')
            sage: p_fine.triangulations_list()
            [(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>),
             (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>)]
            sage: p.set_engine('internal')
        """
    def triangulations_list(self, verbose: bool = False):
        """
        Return all triangulations.

        INPUT:

        - ``verbose`` -- boolean; whether to print out the TOPCOM
          interaction, if any

        OUTPUT:

        A list of triangulations (see
        :class:`~sage.geometry.triangulation.element.Triangulation`)
        satisfying all restrictions imposed previously.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1]])
            sage: p.triangulations_list()
            [(<0,1,2>, <1,2,3>), (<0,1,3>, <0,2,3>)]
            sage: list(map(list, p.triangulations_list()))
            [[(0, 1, 2), (1, 2, 3)], [(0, 1, 3), (0, 2, 3)]]
            sage: p.set_engine('topcom')
            sage: p.triangulations_list()      # optional - topcom
            [(<0,1,2>, <1,2,3>), (<0,1,3>, <0,2,3>)]
            sage: p.set_engine('internal')
        """
    def triangulate(self, verbose: bool = False):
        """
        Return one (in no particular order) triangulation.

        INPUT:

        - ``verbose`` -- boolean; whether to print out the TOPCOM
          interaction, if any

        OUTPUT:

        A :class:`~sage.geometry.triangulation.element.Triangulation`
        satisfying all restrictions imposed. This raises a :exc:`ValueError`
        if no such triangulation exists.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: p.triangulate()
            (<1,3,4>, <2,3,4>)
            sage: list( p.triangulate() )
            [(1, 3, 4), (2, 3, 4)]

        Using TOPCOM yields a different, but equally good, triangulation::

            sage: # optional - topcom
            sage: p.set_engine('topcom')
            sage: p.triangulate()
            (<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)
            sage: list(p.triangulate())
            [(0, 1, 2), (0, 1, 4), (0, 2, 4), (1, 2, 3)]
            sage: p.set_engine('internal')
        """
    def convex_hull(self):
        """
        Return the convex hull of the point configuration.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: p.convex_hull()
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices
        """
    @cached_method
    def restricted_automorphism_group(self):
        """
        Return the restricted automorphism group.

        First, let the linear automorphism group be the subgroup of
        the affine group `AGL(d,\\RR) = GL(d,\\RR) \\ltimes \\RR^d`
        preserving the `d`-dimensional point configuration. The
        affine group acts in the usual way `\\vec{x}\\mapsto
        A\\vec{x}+b` on the ambient space.

        The restricted automorphism group is the subgroup of the
        linear automorphism group generated by permutations of
        points. See [BSS2009]_ for more details and a description of the
        algorithm.

        OUTPUT:

        A
        :class:`PermutationGroup<sage.groups.perm_gps.permgroup.PermutationGroup_generic>`
        that is isomorphic to the restricted automorphism group is
        returned.

        Note that in Sage, permutation groups always act on positive
        integers while lists etc. are indexed by nonnegative
        integers. The indexing of the permutation group is chosen to
        be shifted by ``+1``. That is, the transposition ``(i,j)`` in
        the permutation group corresponds to exchange of ``self[i-1]``
        and ``self[j-1]``.

        EXAMPLES::

            sage: pyramid = PointConfiguration([[1,0,0], [0,1,1], [0,1,-1],
            ....:                               [0,-1,-1], [0,-1,1]])
            sage: G = pyramid.restricted_automorphism_group()                      # needs sage.graphs sage.groups
            sage: G == PermutationGroup([[(3,5)], [(2,3),(4,5)], [(2,4)]])         # needs sage.graphs sage.groups
            True
            sage: DihedralGroup(4).is_isomorphic(G)                                # needs sage.graphs sage.groups
            True

        The square with an off-center point in the middle. Note that
        the middle point breaks the restricted automorphism group
        `D_4` of the convex hull::

            sage: square = PointConfiguration([(3/4,3/4), (1,1), (1,-1), (-1,-1), (-1,1)])
            sage: square.restricted_automorphism_group()                           # needs sage.graphs sage.groups
            Permutation Group with generators [(3,5)]
            sage: DihedralGroup(1).is_isomorphic(_)                                # needs sage.graphs sage.groups
            True
        """
    def face_codimension(self, point):
        """
        Return the smallest `d\\in\\ZZ` such that ``point`` is
        contained in the interior of a codimension-`d` face.

        EXAMPLES::

            sage: triangle = PointConfiguration([[0,0], [1,-1], [1,0], [1,1]])
            sage: triangle.point(2)
            P(1, 0)
            sage: triangle.face_codimension(2)
            1
            sage: triangle.face_codimension([1,0])
            1

        This also works for degenerate cases like the tip of the
        pyramid over a square (which saturates four inequalities)::

            sage: pyramid = PointConfiguration([[1,0,0], [0,1,1], [0,1,-1],
            ....:                               [0,-1,-1], [0,-1,1]])
            sage: pyramid.face_codimension(0)
            3
        """
    def face_interior(self, dim=None, codim=None):
        """
        Return points by the codimension of the containing face in the convex hull.

        EXAMPLES::

            sage: triangle = PointConfiguration([[-1,0], [0,0], [1,-1], [1,0], [1,1]])
            sage: triangle.face_interior()
            ((1,), (3,), (0, 2, 4))
            sage: triangle.face_interior(dim=0)    # the vertices of the convex hull
            (0, 2, 4)
            sage: triangle.face_interior(codim=1)  # interior of facets
            (3,)
        """
    def exclude_points(self, point_idx_list):
        """
        Return a new point configuration with the given points
        removed.

        INPUT:

        - ``point_idx_list`` -- list of integers; the indices of
          points to exclude

        OUTPUT:

        A new :class:`PointConfiguration` with the given points
        removed.

        EXAMPLES::

            sage: p = PointConfiguration([[-1,0], [0,0], [1,-1], [1,0], [1,1]])
            sage: list(p)
            [P(-1, 0), P(0, 0), P(1, -1), P(1, 0), P(1, 1)]
            sage: q = p.exclude_points([3])
            sage: list(q)
            [P(-1, 0), P(0, 0), P(1, -1), P(1, 1)]
            sage: p.exclude_points(p.face_interior(codim=1)).points()
            (P(-1, 0), P(0, 0), P(1, -1), P(1, 1))
        """
    def volume(self, simplex=None):
        '''
        Find `n!` times the `n`-volume of a simplex of dimension `n`.

        INPUT:

        - ``simplex`` -- (optional argument) a simplex from a
          triangulation T specified as a list of point indices

        OUTPUT:

        * If a simplex was passed as an argument: `n!` * (volume of ``simplex``).

        * Without argument: `n!` * (the total volume of the convex hull).

        EXAMPLES:

        The volume of the standard simplex should always be 1::

            sage: p = PointConfiguration([[0,0], [1,0], [0,1], [1,1]])
            sage: p.volume([0,1,2])
            1
            sage: simplex = p.triangulate()[0]  # first simplex of triangulation
            sage: p.volume(simplex)
            1

        The square can be triangulated into two minimal simplices, so
        in the "integral" normalization its volume equals two::

            sage: p.volume()
            2

        .. NOTE::

            We return `n!` * (metric volume of the simplex) to ensure that
            the volume is an integer.  Essentially, this normalizes
            things so that the volume of the standard `n`-simplex is 1.
            See [GKZ1994]_ page 182.
        '''
    def secondary_polytope(self):
        """
        Calculate the secondary polytope of the point configuration.

        For a definition of the secondary polytope, see [GKZ1994]_ page 220
        Definition 1.6.

        Note that if you restricted the admissible triangulations of
        the point configuration then the output will be the
        corresponding face of the whole secondary polytope.

        OUTPUT:

        The secondary polytope of the point configuration as an
        instance of
        :class:`~sage.geometry.polyhedron.base.Polyhedron_base`.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [1,0], [2,1], [1,2], [0,1]])
            sage: poly = p.secondary_polytope()
            sage: poly.vertices_matrix()
            [1 1 3 3 5]
            [3 5 1 4 1]
            [4 2 5 2 4]
            [2 4 2 5 4]
            [5 3 4 1 1]
            sage: poly.Vrepresentation()
            (A vertex at (1, 3, 4, 2, 5),
             A vertex at (1, 5, 2, 4, 3),
             A vertex at (3, 1, 5, 2, 4),
             A vertex at (3, 4, 2, 5, 1),
             A vertex at (5, 1, 4, 4, 1))
            sage: poly.Hrepresentation()
            (An equation (0, 0, 1, 2, 1) x - 13 == 0,
             An equation (1, 0, 0, 2, 2) x - 15 == 0,
             An equation (0, 1, 0, -3, -2) x + 13 == 0,
             An inequality (0, 0, 0, -1, -1) x + 7 >= 0,
             An inequality (0, 0, 0, 1, 0) x - 2 >= 0,
             An inequality (0, 0, 0, -2, -1) x + 11 >= 0,
             An inequality (0, 0, 0, 0, 1) x - 1 >= 0,
             An inequality (0, 0, 0, 3, 2) x - 14 >= 0)
        """
    def circuits_support(self) -> Generator[Incomplete]:
        """
        A generator for the supports of the circuits of the point configuration.

        See :meth:`circuits` for details.

        OUTPUT:

        A generator for the supports `C_-\\cup C_+` (returned as a
        Python tuple) for all circuits of the point configuration.

        EXAMPLES::

            sage: p = PointConfiguration([(0,0), (+1,0), (-1,0), (0,+1), (0,-1)])
            sage: sorted(p.circuits_support())
            [(0, 1, 2), (0, 3, 4), (1, 2, 3, 4)]
        """
    def circuits(self):
        """
        Return the circuits of the point configuration.

        Roughly, a circuit is a minimal linearly dependent subset of
        the points. That is, a circuit is a partition

        .. MATH::

            \\{ 0, 1, \\dots, n-1 \\} = C_+ \\cup C_0 \\cup C_-

        such that there is an (unique up to an overall normalization) affine
        relation

        .. MATH::

            \\sum_{i\\in C_+}  \\alpha_i \\vec{p}_i =
            \\sum_{j\\in C_-}  \\alpha_j \\vec{p}_j

        with all positive (or all negative) coefficients, where
        `\\vec{p}_i=(p_1,\\dots,p_k,1)` are the projective coordinates
        of the `i`-th point.

        OUTPUT:

        The list of (unsigned) circuits as triples `(C_+, C_0,
        C_-)`. The swapped circuit `(C_-, C_0, C_+)` is not returned
        separately.

        EXAMPLES::

            sage: p = PointConfiguration([(0,0), (+1,0), (-1,0), (0,+1), (0,-1)])
            sage: sorted(p.circuits())
            [((0,), (1, 2), (3, 4)), ((0,), (3, 4), (1, 2)), ((1, 2), (0,), (3, 4))]


        TESTS::

            sage: U=matrix([
            ....:    [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
            ....:    [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
            ....:    [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
            ....:    [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
            ....:    [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
            ....: ])
            sage: p = PointConfiguration(U.columns())
            sage: len(p.circuits())    # long time
            218
        """
    def positive_circuits(self, *negative):
        """
        Return the positive part of circuits with fixed negative part.

        A circuit is a pair `(C_+, C_-)`, each consisting of a subset
        (actually, an ordered tuple) of point indices.

        INPUT:

        - ``*negative`` -- integer; the indices of points

        OUTPUT: a tuple of all circuits with `C_-` = ``negative``

        EXAMPLES::

            sage: p = PointConfiguration([(1,0,0), (0,1,0), (0,0,1), (-2,0,-1), (-2,-1,0),
            ....:                         (-3,-1,-1), (1,1,1), (-1,0,0), (0,0,0)])
            sage: sorted(p.positive_circuits(8))
            [(0, 1, 2, 5), (0, 1, 4), (0, 2, 3), (0, 3, 4, 6), (0, 5, 6), (0, 7)]
            sage: p.positive_circuits(0,5,6)
            ((8,),)
        """
    def bistellar_flips(self):
        """
        Return the bistellar flips.

        OUTPUT:

        The bistellar flips as a tuple. Each flip is a pair
        `(T_+,T_-)` where `T_+` and `T_-` are partial triangulations
        of the point configuration.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0),(1,0),(0,1),(1,1)])
            sage: pc.bistellar_flips()
            (((<0,1,3>, <0,2,3>), (<0,1,2>, <1,2,3>)),)
            sage: Tpos, Tneg = pc.bistellar_flips()[0]
            sage: Tpos.plot(axes=False)                                            # needs sage.plot
            Graphics object consisting of 11 graphics primitives
            sage: Tneg.plot(axes=False)                                            # needs sage.plot
            Graphics object consisting of 11 graphics primitives

        The 3d analog::

            sage: pc = PointConfiguration([(0,0,0),(0,2,0),(0,0,2),(-1,0,0),(1,1,1)])
            sage: pc.bistellar_flips()
            (((<0,1,2,3>, <0,1,2,4>), (<0,1,3,4>, <0,2,3,4>, <1,2,3,4>)),)

        A 2d flip on the base of the pyramid over a square::

            sage: pc = PointConfiguration([(0,0,0),(0,2,0),(0,0,2),(0,2,2),(1,1,1)])
            sage: pc.bistellar_flips()
            (((<0,1,3>, <0,2,3>), (<0,1,2>, <1,2,3>)),)
            sage: Tpos, Tneg = pc.bistellar_flips()[0]
            sage: Tpos.plot(axes=False)                                            # needs sage.plot
            Graphics3d Object
        """
    def lexicographic_triangulation(self):
        """
        Return the lexicographic triangulation.

        The algorithm was taken from [PUNTOS]_.

        EXAMPLES::

            sage: p = PointConfiguration([(0,0), (+1,0), (-1,0), (0,+1), (0,-1)])
            sage: p.lexicographic_triangulation()
            (<1,3,4>, <2,3,4>)

        TESTS::

            sage: U = matrix([
            ....:    [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
            ....:    [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
            ....:    [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
            ....:    [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
            ....:    [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
            ....: ])
            sage: pc = PointConfiguration(U.columns())
            sage: pc.lexicographic_triangulation()
            (<1,3,4,7,10,13>, <1,3,4,8,10,13>, <1,3,6,7,10,13>, <1,3,6,8,10,13>,
             <1,4,6,7,10,13>, <1,4,6,8,10,13>, <2,3,4,6,7,12>, <2,3,4,7,12,13>,
             <2,3,6,7,12,13>, <2,4,6,7,12,13>, <3,4,5,6,9,12>, <3,4,5,8,9,12>,
             <3,4,6,7,11,12>, <3,4,6,9,11,12>, <3,4,7,10,11,13>, <3,4,7,11,12,13>,
             <3,4,8,9,10,12>, <3,4,8,10,12,13>, <3,4,9,10,11,12>, <3,4,10,11,12,13>,
             <3,5,6,8,9,12>, <3,6,7,10,11,13>, <3,6,7,11,12,13>, <3,6,8,9,10,12>,
             <3,6,8,10,12,13>, <3,6,9,10,11,12>, <3,6,10,11,12,13>, <4,5,6,8,9,12>,
             <4,6,7,10,11,13>, <4,6,7,11,12,13>, <4,6,8,9,10,12>, <4,6,8,10,12,13>,
             <4,6,9,10,11,12>, <4,6,10,11,12,13>)
            sage: len(_)
            34
        """
    @cached_method
    def distance_affine(self, x, y):
        """
        Return the distance between two points.

        The distance function used in this method is `d_{aff}(x,y)^2`,
        the square of the usual affine distance function

        .. MATH::

            d_{aff}(x,y) = |x-y|

        INPUT:

        - ``x``, ``y`` -- two points of the point configuration

        OUTPUT:

        The metric distance-square `d_{aff}(x,y)^2`. Note that this
        distance lies in the same field as the entries of ``x``,
        ``y``. That is, the distance of rational points will be
        rational and so on.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0),(1,0),(2,1),(1,2),(0,1)])
            sage: [pc.distance_affine(pc.point(0), p) for p in pc.points()]
            [0, 1, 5, 5, 1]
        """
    @cached_method
    def distance_FS(self, x, y):
        """
        Return the distance between two points.

        The distance function used in this method is `1-\\cos
        d_{FS}(x,y)^2`, where `d_{FS}` is the Fubini-Study distance of
        projective points. Recall the Fubini-Studi distance function

        .. MATH::

            d_{FS}(x,y) = \\arccos \\sqrt{ \\frac{(x\\cdot y)^2}{|x|^2 |y|^2} }

        INPUT:

        - ``x``, ``y`` -- two points of the point configuration

        OUTPUT:

        The distance `1-\\cos d_{FS}(x,y)^2`. Note that this distance
        lies in the same field as the entries of ``x``, ``y``. That
        is, the distance of rational points will be rational and so
        on.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (2,1), (1,2), (0,1)])
            sage: [pc.distance_FS(pc.point(0), p) for p in pc.points()]
            [0, 1/2, 5/6, 5/6, 1/2]
        """
    @cached_method
    def distance(self, x, y):
        """
        Return the distance between two points.

        INPUT:

        - ``x``, ``y`` -- two points of the point configuration

        OUTPUT:

        The distance between ``x`` and ``y``, measured either with
        :meth:`distance_affine` or :meth:`distance_FS` depending on
        whether the point configuration is defined by affine or
        projective points. These are related, but not equal to the
        usual flat and Fubini-Study distance.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (2,1), (1,2), (0,1)])
            sage: [pc.distance(pc.point(0), p) for p in pc.points()]
            [0, 1, 5, 5, 1]

            sage: pc = PointConfiguration([(0,0,1), (1,0,1), (2,1,1), (1,2,1), (0,1,1)],
            ....:                         projective=True)
            sage: [pc.distance(pc.point(0), p) for p in pc.points()]
            [0, 1/2, 5/6, 5/6, 1/2]
        """
    def farthest_point(self, points, among=None):
        """
        Return the point with the most distance from ``points``.

        INPUT:

        - ``points`` -- list of points

        - ``among`` -- list of points or ``None`` (default); the set
          of points from which to pick the farthest one. By default,
          all points of the configuration are considered.

        OUTPUT:

        A :class:`~sage.geometry.triangulation.base.Point` with
        largest minimal distance from all given ``points``.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (1,1), (0,1)])
            sage: pc.farthest_point([pc.point(0)])
            P(1, 1)
        """
    def contained_simplex(self, large: bool = True, initial_point=None, point_order=None):
        """
        Return a simplex contained in the point configuration.

        INPUT:

        - ``large`` -- boolean; whether to attempt to return a large
          simplex

        - ``initial_point`` -- a
          :class:`~sage.geometry.triangulation.base.Point` or ``None``
          (default). A specific point to start with when picking the
          simplex vertices.

        - ``point_order`` -- list or tuple of (some or all)
          :class:`~sage.geometry.triangulation.base.Point` s or ``None``
          (default)

        OUTPUT:

        A tuple of points that span a simplex of dimension
        :meth:`dim`. If ``large==True``, the simplex is constructed by
        successively picking the farthest point. This will ensure that
        the simplex is not unnecessarily small, but will in general
        not return a maximal simplex.
        If a ``point_order`` is specified, the simplex is greedily
        constructed by considering the points in this order.
        The ``large`` option and ``initial_point`` is ignored in this case.
        The ``point_order`` may contain only a subset of the points;
        in this case, the dimension of the simplex will be the dimension of
        this subset.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (2,1), (1,1), (0,1)])
            sage: pc.contained_simplex()
            (P(0, 1), P(2, 1), P(1, 0))
            sage: pc.contained_simplex(large=False)
            (P(0, 1), P(1, 1), P(1, 0))
            sage: pc.contained_simplex(initial_point=pc.point(2))
            (P(2, 1), P(0, 0), P(1, 0))

            sage: pc = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: pc.contained_simplex()
            (P(-1, -1), P(1, 1), P(0, 1))
            sage: pc.contained_simplex(point_order=[pc[1], pc[3], pc[4], pc[2], pc[0]])
            (P(0, 1), P(1, 1), P(-1, -1))

        Lower-dimensional example::

            sage: pc.contained_simplex(point_order=[pc[0], pc[3], pc[4]])
            (P(0, 0), P(1, 1))

        TESTS::

            sage: pc = PointConfiguration([[0,0], [0,1], [1,0]])
            sage: pc.contained_simplex()
            (P(1, 0), P(0, 1), P(0, 0))
            sage: pc = PointConfiguration([[0,0], [0,1]])
            sage: pc.contained_simplex()
            (P(0, 1), P(0, 0))
            sage: pc = PointConfiguration([[0,0]])
            sage: pc.contained_simplex()
            (P(0, 0),)
            sage: pc = PointConfiguration([])
            sage: pc.contained_simplex()
            ()
        """
    def placing_triangulation(self, point_order=None):
        """
        Construct the placing (pushing) triangulation.

        INPUT:

        - ``point_order`` -- list of points or integers. The order in
          which the points are to be placed. If not given, the points
          will be placed in some arbitrary order that attempts to
          produce a small number of simplices.

        OUTPUT: a :class:`~sage.geometry.triangulation.triangulation.Triangulation`

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (2,1), (1,2), (0,1)])
            sage: pc.placing_triangulation()
            (<0,1,2>, <0,2,4>, <2,3,4>)
            sage: pc.placing_triangulation(point_order=(3,2,1,4,0))
            (<0,1,4>, <1,2,3>, <1,3,4>)
            sage: pc.placing_triangulation(point_order=[pc[1], pc[3], pc[4], pc[0]])
            (<0,1,4>, <1,3,4>)
            sage: U = matrix([
            ....:    [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
            ....:    [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
            ....:    [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
            ....:    [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
            ....:    [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
            ....: ])
            sage: p = PointConfiguration(U.columns())
            sage: triangulation = p.placing_triangulation();  triangulation
            (<0,2,3,4,6,7>, <0,2,3,4,6,12>, <0,2,3,4,7,13>, <0,2,3,4,12,13>,
             <0,2,3,6,7,13>, <0,2,3,6,12,13>, <0,2,4,6,7,13>, <0,2,4,6,12,13>,
             <0,3,4,6,7,12>, <0,3,4,7,12,13>, <0,3,6,7,12,13>, <0,4,6,7,12,13>,
             <1,3,4,5,6,12>, <1,3,4,6,11,12>, <1,3,4,7,11,13>, <1,3,4,11,12,13>,
             <1,3,6,7,11,13>, <1,3,6,11,12,13>, <1,4,6,7,11,13>, <1,4,6,11,12,13>,
             <3,4,6,7,11,12>, <3,4,7,11,12,13>, <3,6,7,11,12,13>, <4,6,7,11,12,13>)
            sage: sum(p.volume(t) for t in triangulation)
            42
            sage: p0 = PointConfiguration([(0,0), (+1,0), (-1,0), (0,+1), (0,-1)])
            sage: p0.pushing_triangulation(point_order=[1,2,0,3,4])
            (<1,2,3>, <1,2,4>)
            sage: p0.pushing_triangulation(point_order=[0,1,2,3,4])
            (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>)

        The same triangulation with renumbered points 0->4, 1->0, etc::

            sage: p1 = PointConfiguration([(+1,0), (-1,0), (0,+1), (0,-1), (0,0)])
            sage: p1.pushing_triangulation(point_order=[4,0,1,2,3])
            (<0,2,4>, <0,3,4>, <1,2,4>, <1,3,4>)
        """
    pushing_triangulation = placing_triangulation
    @cached_method
    def Gale_transform(self, points=None, homogenize: bool = True):
        """
        Return the Gale transform of ``self``.

        INPUT:

        - ``points`` -- tuple of points or point indices or ``None``
          (default). A subset of points for which to compute the Gale
          transform. By default, all points are used.

        - ``homogenize`` -- boolean (default: ``True``); whether to add a row
          of 1's before taking the transform.

        OUTPUT: a matrix over :meth:`base_ring`

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (2,1), (1,1), (0,1)])
            sage: pc.Gale_transform()
            [ 1 -1  0  1 -1]
            [ 0  0  1 -2  1]

            sage: pc.Gale_transform((0,1,3,4))
            [ 1 -1  1 -1]

            sage: points = (pc.point(0), pc.point(1), pc.point(3), pc.point(4))
            sage: pc.Gale_transform(points)
            [ 1 -1  1 -1]

        It is possible to take the inverse of the Gale transform, by specifying
        whether to homogenize or not::

            sage: pc2 = PointConfiguration([[0,0],[3,0],[0,3],[3,3],[1,1]])
            sage: pc2.Gale_transform(homogenize=False)
            [ 1  0  0  0  0]
            [ 0  1  1  0 -3]
            [ 0  0  0  1 -3]
            sage: pc2.Gale_transform(homogenize=True)
            [ 1  1  1  0 -3]
            [ 0  2  2 -1 -3]

        It might not affect the result (when acyclic)::

            sage: PC = PointConfiguration([[4,0,0],[0,4,0],[0,0,4],[2,1,1],[1,2,1],[1,1,2]])
            sage: GT = PC.Gale_transform(homogenize=False);GT
            [ 1  0  0 -3  1  1]
            [ 0  1  0  1 -3  1]
            [ 0  0  1  1  1 -3]
            sage: GT = PC.Gale_transform(homogenize=True);GT
            [ 1  0  0 -3  1  1]
            [ 0  1  0  1 -3  1]
            [ 0  0  1  1  1 -3]

        The following point configuration is totally cyclic (the cone spanned
        by the vectors is equal to the vector space spanned by the points),
        hence its Gale dual is acyclic (there is a linear functional that is
        positive in all the points of the configuration) when not homogenized::

            sage: pc3 = PointConfiguration([[-1, -1, -1], [-1, 0, 0], [0, -1, 0], [0, 0, -1], [1, 0, 0], [0, 0, 1], [0, 1, 0]])
            sage: g_hom = pc3.Gale_transform(homogenize=True);g_hom
            [ 1  0  0 -2  1 -1  1]
            [ 0  1  0 -1  1 -1  0]
            [ 0  0  1 -1  0 -1  1]
            sage: g_inhom = pc3.Gale_transform(homogenize=False);g_inhom
            [1 0 0 0 1 1 1]
            [0 1 0 0 1 0 0]
            [0 0 1 0 0 0 1]
            [0 0 0 1 0 1 0]
            sage: Polyhedron(rays=g_hom.columns())
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 1 vertex and 3 lines
            sage: Polyhedron(rays=g_inhom.columns())
            A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 4 rays
        """
    def deformation_cone(self, collection):
        """
        Return the deformation cone for the ``collection`` of subconfigurations
        of ``self``.

        INPUT:

        - ``collection`` -- a collection of subconfigurations of ``self``.
          Subconfigurations are given as indices

        OUTPUT: a polyhedron. It contains the liftings of the point configuration
        making the collection a regular (or coherent, or projective, or
        polytopal) subdivision.

        EXAMPLES::

            sage: PC = PointConfiguration([(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1)])
            sage: coll = [(1, 4), (0, 2), (0, 1), (2, 3), (3, 4)]
            sage: dc = PC.deformation_cone(coll);dc
            A 5-dimensional polyhedron in QQ^5 defined as the convex hull of 1 vertex, 3 rays, 2 lines
            sage: dc.rays()
            (A ray in the direction (1, 0, 1, 0, 0),
             A ray in the direction (1, 1, 0, 0, 0),
             A ray in the direction (1, 1, 1, 0, 0))
            sage: dc.lines()
            (A line in the direction (1, 0, 1, 0, -1),
             A line in the direction (1, 1, 0, -1, 0))
            sage: dc.an_element()
            (3, 2, 2, 0, 0)

        We add to the interior element the first line and we verify that the
        given rays are defining rays of the lower hull::

            sage: P = Polyhedron(rays=[(-1, -1, 4), (-1, 0, 3), (0, -1, 2), (1, 0, -1), (0, 1, 0)])
            sage: P.rays()
            (A ray in the direction (-1, -1, 4),
             A ray in the direction (-1, 0, 3),
             A ray in the direction (0, -1, 2),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, -1))

        Let's verify the mother of all examples explained in Section 7.1.1 of
        [DLRS2010]_::

            sage: def mother(epsilon=0):
            ....:     return PointConfiguration([(4-epsilon,epsilon,0),(0,4-epsilon,epsilon),(epsilon,0,4-epsilon),(2,1,1),(1,2,1),(1,1,2)])

            sage: epsilon = 0
            sage: m = mother(0)
            sage: m.points()
            (P(4, 0, 0), P(0, 4, 0), P(0, 0, 4), P(2, 1, 1), P(1, 2, 1), P(1, 1, 2))
            sage: S1 = [(0,1,4),(0,3,4),(1,2,5),(1,4,5),(0,2,3),(2,3,5)]
            sage: S2 = [(0,1,3),(1,3,4),(1,2,4),(2,4,5),(0,2,5),(0,3,5)]

        Both subdivisions `S1` and `S2` are not regular::

            sage: mother_dc1 = m.deformation_cone(S1)
            sage: mother_dc1
            A 4-dimensional polyhedron in QQ^6 defined as the convex hull of 1 vertex, 1 ray, 3 lines
            sage: mother_dc2 = m.deformation_cone(S2)
            sage: mother_dc2
            A 4-dimensional polyhedron in QQ^6 defined as the convex hull of 1 vertex, 1 ray, 3 lines

        Notice that they have a ray which provides a degenerate lifting which
        only provides a coarsening of the subdivision from the lower hull (it
        has 5 facets, and should have 8)::

            sage: result = Polyhedron([vector(list(m.points()[_])+[mother_dc1.rays()[0][_]]) for _ in range(len(m.points()))])
            sage: result.f_vector()
            (1, 6, 9, 5, 1)

        But if we use epsilon to perturb the configuration, suddenly
        `S1` becomes regular::

            sage: epsilon = 1/2
            sage: mp = mother(epsilon)
            sage: mp.points()
            (P(7/2, 1/2, 0),
             P(0, 7/2, 1/2),
             P(1/2, 0, 7/2),
             P(2, 1, 1),
             P(1, 2, 1),
             P(1, 1, 2))
            sage: mother_dc1 = mp.deformation_cone(S1);mother_dc1
            A 6-dimensional polyhedron in QQ^6 defined as the convex hull of 1 vertex, 3 rays, 3 lines
            sage: mother_dc2 = mp.deformation_cone(S2);mother_dc2
            A 3-dimensional polyhedron in QQ^6 defined as the convex hull of 1 vertex and 3 lines

        .. SEEALSO::

            :meth:`~sage.schemes.toric.variety.Kaehler_cone`

        REFERENCES:

            For more information, see Section 5.4 of [DLRS2010]_ and Section
            2.2 of [ACEP2020].
        """
    def plot(self, **kwds):
        """
        Produce a graphical representation of the point configuration.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sage: p.plot(axes=False)                                                    # needs sage.plot
            Graphics object consisting of 5 graphics primitives

        .. PLOT::
            :width: 300 px

            p = PointConfiguration([[0,0], [0,1], [1,0], [1,1], [-1,-1]])
            sphinx_plot(p.plot(axes=False))
        """
