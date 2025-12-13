from _typeshed import Incomplete
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.structure.sage_object import SageObject as SageObject

VERIFY_RESULT: bool

class PivotedInequalities(SageObject):
    base_ring: Incomplete
    dim: Incomplete
    def __init__(self, base_ring, dim) -> None:
        """
        Base class for inequalities that may contain linear subspaces.

        INPUT:

        - ``base_ring`` -- a field

        - ``dim`` -- integer; the ambient space dimension

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description_inhomogeneous             ....:     import PivotedInequalities
            sage: piv = PivotedInequalities(QQ, 2)
            sage: piv._pivot_inequalities(matrix([(1,1,3), (5,5,7)]))
            [1 3]
            [5 7]
            sage: piv._pivots
            (0, 2)
            sage: piv._linear_subspace
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [ 1 -1  0]
        """

class Hrep2Vrep(PivotedInequalities):
    def __init__(self, base_ring, dim, inequalities, equations) -> None:
        """
        Convert H-representation to a minimal V-representation.

        INPUT:

        - ``base_ring`` -- a field

        - ``dim`` -- integer; the ambient space dimension

        - ``inequalities`` -- list of inequalities; each inequality
          is given as constant term, ``dim`` coefficients

        - ``equations`` -- list of equations; same notation as for
          inequalities

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description_inhomogeneous import Hrep2Vrep
            sage: Hrep2Vrep(QQ, 2, [(1,2,3), (2,4,3)], [])
            [-1/2|-1/2  1/2|]
            [   0| 2/3 -1/3|]
            sage: Hrep2Vrep(QQ, 2, [(1,2,3), (2,-2,-3)], [])
            [   1 -1/2||   1]
            [   0    0||-2/3]
            sage: Hrep2Vrep(QQ, 2, [(1,2,3), (2,2,3)], [])
            [-1/2| 1/2|   1]
            [   0|   0|-2/3]
            sage: Hrep2Vrep(QQ, 2, [(8,7,-2), (1,-4,3), (4,-3,-1)], [])
            [ 1  0 -2||]
            [ 1  4 -3||]
            sage: Hrep2Vrep(QQ, 2, [(1,2,3), (2,4,3), (5,-1,-2)], [])
            [-19/5  -1/2| 2/33  1/11|]
            [ 22/5     0|-1/33 -2/33|]
            sage: Hrep2Vrep(QQ, 2, [(0,2,3), (0,4,3), (0,-1,-2)], [])
            [   0| 1/2  1/3|]
            [   0|-1/3 -1/6|]
            sage: Hrep2Vrep(QQ, 2, [], [(1,2,3), (7,8,9)])
            [-2||]
            [ 1||]
            sage: Hrep2Vrep(QQ, 2, [(1,0,0)], [])    # universe
            [0||1 0]
            [0||0 1]
            sage: Hrep2Vrep(QQ, 2, [(-1,0,0)], [])   # empty
            []
            sage: Hrep2Vrep(QQ, 2, [], [])   # universe
            [0||1 0]
            [0||0 1]
        """
    def verify(self, inequalities, equations) -> None:
        """
        Compare result to PPL if the base ring is QQ.

        This method is for debugging purposes and compares the
        computation with another backend if available.

        INPUT:

        - ``inequalities``, ``equations`` -- see :class:`Hrep2Vrep`

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description_inhomogeneous import Hrep2Vrep
            sage: H = Hrep2Vrep(QQ, 1, [(1,2)], [])
            sage: H.verify([(1,2)], [])
        """

class Vrep2Hrep(PivotedInequalities):
    equations: Incomplete
    inequalities: Incomplete
    def __init__(self, base_ring, dim, vertices, rays, lines) -> None:
        """
        Convert V-representation to a minimal H-representation.

        INPUT:

        - ``base_ring`` -- a field

        - ``dim`` -- integer; the ambient space dimension

        - ``vertices`` -- list of vertices; each vertex is given as
          list of ``dim`` coordinates

        - ``rays`` -- list of rays; each ray is given as
          list of ``dim`` coordinates, not all zero

        - ``lines`` -- list of line generators; each line is given as
          list of ``dim`` coordinates, not all zero

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description_inhomogeneous import Vrep2Hrep
            sage: Vrep2Hrep(QQ, 2, [(-1/2,0)], [(-1/2,2/3), (1/2,-1/3)], [])
            [1 2 3]
            [2 4 3]
            [-----]

            sage: Vrep2Hrep(QQ, 2, [(1,0), (-1/2,0)], [], [(1,-2/3)])
            [ 1/3  2/3    1]
            [ 2/3 -2/3   -1]
            [--------------]

            sage: Vrep2Hrep(QQ, 2, [(-1/2,0)], [(1/2,0)], [(1,-2/3)])
            [1 2 3]
            [-----]

            sage: Vrep2Hrep(QQ, 2, [(1,1), (0,4), (-2,-3)], [], [])
            [ 8/13  7/13 -2/13]
            [ 1/13 -4/13  3/13]
            [ 4/13 -3/13 -1/13]
            [-----------------]

            sage: Vrep2Hrep(QQ, 2, [(-19/5,22/5), (-1/2,0)], [(2/33,-1/33), (1/11,-2/33)], [])
            [10/11 -2/11 -4/11]
            [ 66/5 132/5  99/5]
            [ 2/11  4/11  6/11]
            [-----------------]

            sage: Vrep2Hrep(QQ, 2, [(0,0)], [(1/2,-1/3), (1/3,-1/6)], [])
            [  0  -6 -12]
            [  0  12  18]
            [-----------]

            sage: Vrep2Hrep(QQ, 2, [(-1/2,0)], [], [(1,-2/3)])
            [-----]
            [1 2 3]

            sage: Vrep2Hrep(QQ, 2, [(-1/2,0)], [], [(1,-2/3), (1,0)])
            []
        """
    def verify(self, vertices, rays, lines) -> None:
        """
        Compare result to PPL if the base ring is QQ.

        This method is for debugging purposes and compares the
        computation with another backend if available.

        INPUT:

        - ``vertices``, ``rays``, ``lines`` -- see :class:`Vrep2Hrep`

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description_inhomogeneous import Vrep2Hrep
            sage: vertices = [(-1/2,0)]
            sage: rays = [(-1/2,2/3), (1/2,-1/3)]
            sage: lines = []
            sage: V2H = Vrep2Hrep(QQ, 2, vertices, rays, lines)
            sage: V2H.verify(vertices, rays, lines)
        """
