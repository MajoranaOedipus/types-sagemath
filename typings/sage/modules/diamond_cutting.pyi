from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector

def plane_inequality(v) -> list:
    """
    Return the inequality for points on the same side as the origin
    with respect to the plane through ``v`` normal to ``v``.

    EXAMPLES::

        sage: from sage.modules.diamond_cutting import plane_inequality
        sage: ieq = plane_inequality([1, -1]); ieq
        [2, -1, 1]
        sage: ieq[0] + vector(ieq[1:]) * vector([1, -1])
        0
    """
def jacobi(M):
    """
    Compute the upper-triangular part of the Cholesky/Jacobi
    decomposition of the symmetric matrix ``M``.

    Let `M` be a symmetric `n \\times n`-matrix over a field `F`.
    Let `m_{i,j}` denote the `(i,j)`-th entry of `M` for any
    `1 \\leq i \\leq n` and `1 \\leq j \\leq n`. Then, the
    upper-triangular part computed by this method is the
    upper-triangular `n \\times n`-matrix `Q` whose
    `(i,j)`-th entry `q_{i,j}` satisfies

    .. MATH::

        q_{i,j} =
        \\begin{cases}
            \\frac{1}{q_{i,i}} \\left( m_{i,j} - \\sum_{r<i} q_{r,r} q_{r,i} q_{r,j} \\right) & i < j, \\\\\n            m_{i,j} - \\sum_{r<i} q_{r,r} q_{r,i}^2 & i = j, \\\\\n            0 & i > j,
        \\end{cases}

    for all `1 \\leq i \\leq n` and `1 \\leq j \\leq n`. (These
    equalities determine the entries of `Q` uniquely by
    recursion.) This matrix `Q` is defined for every invertible
    `n \\times n`-matrix `M`. Its definition is taken from (2.3)
    of [FP1985]_.

    .. NOTE::

        This should be a method of matrices.

    EXAMPLES::

        sage: from sage.modules.diamond_cutting import jacobi
        sage: jacobi(identity_matrix(3) * 4)
        [4 0 0]
        [0 4 0]
        [0 0 4]

        sage: def testall(M):
        ....:      Q = jacobi(M)
        ....:      for j in range(3):
        ....:          for i in range(j):
        ....:              if Q[i,j] * Q[i,i] != M[i,j] - sum(Q[r,i] * Q[r,j] * Q[r,r] for r in range(i)):
        ....:                  return False
        ....:      for i in range(3):
        ....:          if Q[i,i] != M[i,i] - sum(Q[r,i] ** 2 * Q[r,r] for r in range(i)):
        ....:              return False
        ....:          for j in range(i):
        ....:              if Q[i,j] != 0:
        ....:                  return False
        ....:      return True

        sage: M = Matrix(QQ, [[8,1,5], [1,6,0], [5,0,3]])
        sage: Q = jacobi(M); Q
        [    8   1/8   5/8]
        [    0  47/8 -5/47]
        [    0     0 -9/47]
        sage: testall(M)
        True

        sage: M = Matrix(QQ, [[3,6,-1,7],[6,9,8,5],[-1,8,2,4],[7,5,4,0]])
        sage: testall(M)
        True
    """
def diamond_cut(V, GM, C, verbose: bool = False) -> Polyhedron:
    """
    Perform diamond cutting on polyhedron ``V`` with basis matrix ``GM``
    and squared radius ``C``.

    INPUT:

    - ``V`` -- polyhedron to cut from

    - ``GM`` -- half of the basis matrix of the lattice

    - ``C`` -- square of the radius to use in cutting algorithm

    - ``verbose`` -- boolean (default: ``False``); whether to print
      debug information

    OUTPUT: a :class:`Polyhedron` instance

    ALGORITHM:

    Use the algorithm in (2.8) of [FP1985]_ to iterate through the nonzero
    vectors ``hv`` of length at most `\\sqrt{C}` in the lattice spanned by
    ``GM``. (Actually, the algorithm only constructs one vector from each pair
    ``{hv, -hv}``.) For each such vector ``hv``, intersect ``V`` with the
    half-spaces defined by ``plane_inequality(hv)`` and
    ``plane_inequality(-hv)``.

    EXAMPLES::

        sage: from sage.modules.diamond_cutting import diamond_cut
        sage: V = Polyhedron([[0], [2]])
        sage: GM = matrix([2])
        sage: V = diamond_cut(V, GM, 4)
        sage: V.vertices()
        (A vertex at (2), A vertex at (0))

    TESTS:

    Verify that code works when no cuts are performed::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: v = vector(ZZ, [1,1,-1])
        sage: L = IntegerLattice([v])
        sage: C = L.voronoi_cell(radius=0.1)
    """
def calculate_voronoi_cell(basis, radius=None, verbose: bool = False) -> Polyhedron:
    """
    Calculate the Voronoi cell of the lattice defined by basis.

    INPUT:

    - ``basis`` -- embedded basis matrix of the lattice

    - ``radius`` -- square of radius of basis vectors to consider

    - ``verbose`` -- whether to print debug information

    OUTPUT: a :class:`Polyhedron` instance

    EXAMPLES::

        sage: from sage.modules.diamond_cutting import calculate_voronoi_cell
        sage: V = calculate_voronoi_cell(matrix([[1, 0], [0, 1]]))
        sage: V.volume()
        1

    TESTS:

    Verify that :issue:`39507` is fixed::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: v = vector(ZZ, [1,1,1,-1])
        sage: L = IntegerLattice([v])
        sage: print(v in L)
        True
        sage: print(L.closest_vector(v))
        (1, 1, 1, -1)
        sage: C = L.voronoi_cell()
        sage: C.Hrepresentation()
        (An inequality (-1, -1, -1, 1) x + 2 >= 0,
         An inequality (1, 1, 1, -1) x + 2 >= 0)
        sage: v = vector(ZZ, [1,1,-1])
        sage: L = IntegerLattice([v])
        sage: C = L.voronoi_cell()
        sage: C.Hrepresentation()
        (An inequality (-2, -2, 2) x + 3 >= 0,
         An inequality (2, 2, -2) x + 3 >= 0)
        sage: C.Vrepresentation()
        (A line in the direction (0, 1, 1),
         A line in the direction (1, 0, 1),
         A vertex at (0, 0, -3/2),
         A vertex at (0, 0, 3/2))

    Verify that :issue:`37086` is fixed::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: l  = [7, 0, -1, -2, -1, -2, 7, -2, 0, 0, -2,
        ....:       0, 7, -2, 0, -1, -2, -1, 7, 0 , -1, -1, 0, -2, 7]
        sage: M = matrix(5, 5, l)
        sage: C = IntegerLattice(M).voronoi_cell()
        sage: C
        A 5-dimensional polyhedron in QQ^5 defined as the
        convex hull of 720 vertices
    """
