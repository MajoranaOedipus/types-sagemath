from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

class LatticePolytopeError(Exception):
    """
    Base class for errors from lattice polytopes
    """
class LatticePolytopesNotIsomorphicError(LatticePolytopeError):
    """
    Raised when two lattice polytopes are not isomorphic.
    """
class LatticePolytopeNoEmbeddingError(LatticePolytopeError):
    """
    Raised when no embedding of the desired kind can be found.
    """

class LatticeEuclideanGroupElement(SageObject):
    def __init__(self, A, b) -> None:
        """
        An element of the lattice Euclidean group.

        Note that this is just intended as a container for results from
        LatticePolytope_PPL. There is no group-theoretic functionality to
        speak of.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL, C_Polyhedron
            sage: from sage.geometry.polyhedron.lattice_euclidean_group_element import LatticeEuclideanGroupElement
            sage: M = LatticeEuclideanGroupElement([[1,2],[2,3],[-1,2]], [1,2,3])
            sage: M
            The map A*x+b with A=
            [ 1  2]
            [ 2  3]
            [-1  2]
            b =
            (1, 2, 3)
            sage: M._A
            [ 1  2]
            [ 2  3]
            [-1  2]
            sage: M._b
            (1, 2, 3)
            sage: M(vector([0,0]))
            (1, 2, 3)
            sage: M(LatticePolytope_PPL((0,0),(1,0),(0,1)))
            A 2-dimensional lattice polytope in ZZ^3 with 3 vertices
            sage: _.vertices()
            ((1, 2, 3), (2, 4, 2), (3, 5, 5))
        """
    def __call__(self, x):
        """
        Return the image of ``x``.

        INPUT:

        - ``x`` -- a vector or lattice polytope

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL, C_Polyhedron
            sage: from sage.geometry.polyhedron.lattice_euclidean_group_element import LatticeEuclideanGroupElement
            sage: M = LatticeEuclideanGroupElement([[1,2],[2,3],[-1,2]], [1,2,3])
            sage: M(vector(ZZ, [11,13]))
            (38, 63, 18)
            sage: M(LatticePolytope_PPL((0,0),(1,0),(0,1)))
            A 2-dimensional lattice polytope in ZZ^3 with 3 vertices
        """
    def domain_dim(self):
        """
        Return the dimension of the domain lattice.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.lattice_euclidean_group_element import LatticeEuclideanGroupElement
            sage: M = LatticeEuclideanGroupElement([[1,2],[2,3],[-1,2]], [1,2,3])
            sage: M
            The map A*x+b with A=
            [ 1  2]
            [ 2  3]
            [-1  2]
            b =
            (1, 2, 3)
            sage: M.domain_dim()
            2
        """
    def codomain_dim(self):
        """
        Return the dimension of the codomain lattice.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.lattice_euclidean_group_element import LatticeEuclideanGroupElement
            sage: M = LatticeEuclideanGroupElement([[1,2],[2,3],[-1,2]], [1,2,3])
            sage: M
            The map A*x+b with A=
            [ 1  2]
            [ 2  3]
            [-1  2]
            b =
            (1, 2, 3)
            sage: M.codomain_dim()
            3

        Note that this is not the same as the rank. In fact, the
        codomain dimension depends only on the matrix shape, and not
        on the rank of the linear mapping::

            sage: zero_map = LatticeEuclideanGroupElement([[0,0],[0,0],[0,0]], [0,0,0])
            sage: zero_map.codomain_dim()
            3
        """
