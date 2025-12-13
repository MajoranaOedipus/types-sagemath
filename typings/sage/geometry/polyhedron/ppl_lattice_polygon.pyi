from sage.geometry.polyhedron.lattice_euclidean_group_element import LatticeEuclideanGroupElement as LatticeEuclideanGroupElement
from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL as LatticePolytope_PPL, LatticePolytope_PPL_class as LatticePolytope_PPL_class
from sage.matrix.constructor import block_matrix as block_matrix, matrix as matrix, zero_matrix as zero_matrix
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.modules.free_module_element import vector as vector, zero_vector as zero_vector
from sage.rings.integer_ring import ZZ as ZZ

class LatticePolygon_PPL_class(LatticePolytope_PPL_class):
    """
    A lattice polygon.

    This includes 2-dimensional polytopes as well as degenerate (0 and
    1-dimensional) lattice polygons. Any polytope in 2d is a polygon.
    """
    @cached_method
    def ordered_vertices(self):
        """
        Return the vertices of a lattice polygon in cyclic order.

        OUTPUT:

        A tuple of vertices ordered along the perimeter of the
        polygon. The first point is arbitrary.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: square = LatticePolytope_PPL((0,0), (1,1), (0,1), (1,0))
            sage: square.vertices()
            ((0, 0), (0, 1), (1, 0), (1, 1))
            sage: square.ordered_vertices()
            ((0, 0), (1, 0), (1, 1), (0, 1))
        """
    def find_isomorphism(self, polytope):
        """
        Return a lattice isomorphism with ``polytope``.

        INPUT:

        - ``polytope`` -- a polytope, potentially higher-dimensional

        OUTPUT:

        A
        :class:`~sage.geometry.polyhedron.lattice_euclidean_group_element.LatticeEuclideanGroupElement`. It
        is not necessarily invertible if the affine dimension of
        ``self`` or ``polytope`` is not two. A
        :class:`~sage.geometry.polyhedron.lattice_euclidean_group_element.LatticePolytopesNotIsomorphicError`
        is raised if no such isomorphism exists.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: L1 = LatticePolytope_PPL((1,0),(0,1),(0,0))
            sage: L2 = LatticePolytope_PPL((1,0,3),(0,1,0),(0,0,1))
            sage: iso = L1.find_isomorphism(L2)
            sage: iso(L1) == L2
            True

            sage: L1 = LatticePolytope_PPL((0, 1), (3, 0), (0, 3), (1, 0))
            sage: L2 = LatticePolytope_PPL((0,0,2,1),(0,1,2,0),(2,0,0,3),(2,3,0,0))
            sage: iso = L1.find_isomorphism(L2)
            sage: iso(L1) == L2
            True

        The following polygons are isomorphic over `\\QQ`, but not as
        lattice polytopes::

            sage: L1 = LatticePolytope_PPL((1,0),(0,1),(-1,-1))
            sage: L2 = LatticePolytope_PPL((0, 0), (0, 1), (1, 0))
            sage: L1.find_isomorphism(L2)
            Traceback (most recent call last):
            ...
            LatticePolytopesNotIsomorphicError: different number of integral points
            sage: L2.find_isomorphism(L1)
            Traceback (most recent call last):
            ...
            LatticePolytopesNotIsomorphicError: different number of integral points
        """
    def is_isomorphic(self, polytope):
        """
        Test if ``self`` and ``polytope`` are isomorphic.

        INPUT:

        - ``polytope`` -- a lattice polytope

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: L1 = LatticePolytope_PPL((1,0),(0,1),(0,0))
            sage: L2 = LatticePolytope_PPL((1,0,3),(0,1,0),(0,0,1))
            sage: L1.is_isomorphic(L2)
            True
        """
    def sub_polytopes(self):
        """
        Return a list of all lattice sub-polygons up to isomorphism.

        OUTPUT:

        All non-empty sub-lattice polytopes up to isomorphism. This
        includes ``self`` as improper sub-polytope, but excludes the
        empty polytope. Isomorphic sub-polytopes that can be embedded
        in different places are only returned once.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: P1xP1 = LatticePolytope_PPL((1,0), (0,1), (-1,0), (0,-1))
            sage: P1xP1.sub_polytopes()
            (A 2-dimensional lattice polytope in ZZ^2 with 4 vertices,
             A 2-dimensional lattice polytope in ZZ^2 with 3 vertices,
             A 2-dimensional lattice polytope in ZZ^2 with 3 vertices,
             A 1-dimensional lattice polytope in ZZ^2 with 2 vertices,
             A 1-dimensional lattice polytope in ZZ^2 with 2 vertices,
             A 0-dimensional lattice polytope in ZZ^2 with 1 vertex)
        """
    def plot(self):
        """
        Plot the lattice polygon.

        OUTPUT: a graphics object

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: P = LatticePolytope_PPL((1,0), (0,1), (0,0), (2,2))
            sage: P.plot()                                                              # needs sage.plot
            Graphics object consisting of 6 graphics primitives
            sage: LatticePolytope_PPL([0], [1]).plot()                                  # needs sage.plot
            Graphics object consisting of 3 graphics primitives
            sage: LatticePolytope_PPL([0]).plot()                                       # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        """

@cached_function
def polar_P2_polytope():
    """
    The polar of the `P^2` polytope.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import polar_P2_polytope
        sage: polar_P2_polytope()
        A 2-dimensional lattice polytope in ZZ^2 with 3 vertices
        sage: _.vertices()
        ((0, 0), (0, 3), (3, 0))
    """
@cached_function
def polar_P1xP1_polytope():
    """
    The polar of the `P^1 \\times P^1` polytope.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import polar_P1xP1_polytope
        sage: polar_P1xP1_polytope()
        A 2-dimensional lattice polytope in ZZ^2 with 4 vertices
        sage: _.vertices()
        ((0, 0), (0, 2), (2, 0), (2, 2))
    """
@cached_function
def polar_P2_112_polytope():
    """
    The polar of the `P^2[1,1,2]` polytope.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import polar_P2_112_polytope
        sage: polar_P2_112_polytope()
        A 2-dimensional lattice polytope in ZZ^2 with 3 vertices
        sage: _.vertices()
        ((0, 0), (0, 2), (4, 0))
    """
@cached_function
def subpolygons_of_polar_P2():
    """
    The lattice sub-polygons of the polar `P^2` polytope.

    OUTPUT: a tuple of lattice polytopes

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import subpolygons_of_polar_P2
        sage: len(subpolygons_of_polar_P2())
        27
    """
@cached_function
def subpolygons_of_polar_P2_112():
    """
    The lattice sub-polygons of the polar `P^2[1,1,2]` polytope.

    OUTPUT: a tuple of lattice polytopes

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import subpolygons_of_polar_P2_112
        sage: len(subpolygons_of_polar_P2_112())
        28
    """
@cached_function
def subpolygons_of_polar_P1xP1():
    """
    The lattice sub-polygons of the polar `P^1 \\times P^1` polytope.

    OUTPUT: a tuple of lattice polytopes

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import subpolygons_of_polar_P1xP1
        sage: len(subpolygons_of_polar_P1xP1())
        20
    """
@cached_function
def sub_reflexive_polygons():
    """
    Return all lattice sub-polygons of reflexive polygons.

    OUTPUT:

    A tuple of all lattice sub-polygons. Each sub-polygon is returned
    as a pair sub-polygon, containing reflexive polygon.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polygon import sub_reflexive_polygons
        sage: l = sub_reflexive_polygons(); l[5]
        (A 2-dimensional lattice polytope in ZZ^2 with 6 vertices,
         A 2-dimensional lattice polytope in ZZ^2 with 3 vertices)
        sage: len(l)
        33
    """
