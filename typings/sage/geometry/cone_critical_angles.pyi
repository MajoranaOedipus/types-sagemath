from _typeshed import Incomplete
from collections.abc import Generator
from sage.functions.trig import arccos as arccos
from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.qqbar import AA as AA
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.symbolic.constants import pi as pi

def gevp_licis(G):
    """
    Return all nonempty subsets of indices for the columns of
    ``G`` that correspond to linearly independent sets (of columns of
    ``G``).

    Mnemonic: linearly independent column-index subsets (LICIS).

    The returned lists are all sorted in the same (the natural) order;
    and are returned as lists so that they may be used to index into
    the rows/columns of matrices.

    INPUT:

    - ``G`` -- the matrix whose linearly independent column index sets
      we want

    OUTPUT:

    A generator that returns sorted lists of natural numbers. Each
    generated list ``I`` is a set of indices corresponding to columns
    of ``G`` that, when considered as a set, is linearly independent.

    EXAMPLES:

    The linearly independent subsets of the matrix corresponding to a
    line (with two generators pointing in opposite directions) are the
    one-element subsets, since the only two-element subset isn't
    linearly independent::

        sage: from sage.geometry.cone_critical_angles import gevp_licis
        sage: K = Cone([(1,0),(-1,0)])
        sage: G = matrix.column(K.rays())
        sage: list(gevp_licis(G))
        [[0], [1]]

    The matrix for the trivial cone has no linearly independent
    subsets, since we require them to be nonempty::

        sage: from sage.geometry.cone_critical_angles import gevp_licis
        sage: trivial_cone = cones.trivial(0)
        sage: trivial_cone.is_trivial()
        True
        sage: list(gevp_licis(matrix.column(trivial_cone.rays())))
        []

    All rays in the nonnegative orthant of `R^{n}` are
    linearly independent, so we should get back `2^{n} - 1` subsets
    after accounting for the absence of the empty set::

        sage: from sage.geometry.cone_critical_angles import gevp_licis
        sage: K = cones.nonnegative_orthant(3)
        sage: G = matrix.column(K.rays())
        sage: len(list(gevp_licis(G))) == 2^(K.nrays()) - 1
        True

    TESTS:

    All sets corresponding to the returned indices should be linearly
    independent::

        sage: from sage.geometry.cone_critical_angles import gevp_licis
        sage: K = random_cone(max_rays=8)
        sage: G = matrix.column(K.rays())
        sage: all( len(s) == K.rays(s).dimension() for s in gevp_licis(G) )
        True
    """
def solve_gevp_zero(M, I, J) -> Generator[Incomplete]:
    """
    Solve the generalized eigenvalue problem in Theorem 3
    [Or2020]_ for a zero eigenvalue using Propositions 3 and 4
    [Or2020]_.

    INPUT:

    - ``M`` -- the matrix whose `(i,j)`-th entry is the inner product
      of `g_{i}` and `h_{j}` as in Proposition 6 [Or2020]_

    - ``I`` -- a linearly independent column-index set for the matrix
      `G` that appears in Theorem 3 [Or2020]_

    - ``J`` -- a linearly independent column-index set for the matrix
      `H` that appears in Theorem 3 [Or2020]_

    OUTPUT:

    A generator of ``(eigenvalue, xi, eta, multiplicity)`` quartets
    where

    - ``eigenvalue`` is zero (the eigenvalue of the system)

    - ``xi`` is the first (length ``len(I)``) component of an
      eigenvector associated with ``eigenvalue``

    - ``eta`` is the second (length ``len(J)``) component of an
      eigenvector associated with ``eigenvalue``

    - ``multiplicity`` is the dimension of the eigenspace associated
      with ``eigenvalue``

    ALGORITHM:

    Proposition 4 in [Or2020]_ is used.

    EXAMPLES:

    This particular configuration results in the zero matrix in the
    eigenvalue problem, so the only solutions correspond to the
    eigenvalue zero::

        sage: from sage.geometry.cone_critical_angles import solve_gevp_zero
        sage: K = cones.nonnegative_orthant(2)
        sage: G = matrix.column(K.rays())
        sage: GG = G.transpose() * G
        sage: I = [0]
        sage: J = [1]
        sage: list(solve_gevp_zero(GG, I, J))
        [(0, (1), (0), 2), (0, (0), (1), 2)]
    """
def solve_gevp_nonzero(GG, HH, M, I, J) -> Generator[Incomplete, Incomplete]:
    """
    Solve the generalized eigenvalue problem in Theorem 3
    [Or2020]_ for a nonzero eigenvalue using Propositions 3 and 5
    [Or2020]_.

    INPUT:

    - ``GG`` -- the matrix whose `(i,j)`-th entry is the inner product
      of `g_{i}` and `g_{j}`, which are in turn the `i`-th and `j`-th
      columns of the matrix `G` in Theorem 3 [Or2020]_

    - ``HH`` -- the matrix whose `(i,j)`-th entry is the inner product
      of `h_{i}` and `h_{j}`, which are in turn the `i`-th and `j`-th
      columns of the matrix `H` in Theorem 3 [Or2020]_

    - ``M`` -- the matrix whose `(i,j)`-th entry is the inner product
      of `g_{i}` and `h_{j}` as in Proposition 6 in [Or2020]_

    - ``I`` -- a linearly independent column-index set for the matrix
      `G` that appears in Theorem 3 [Or2020]_

    - ``J`` -- a linearly independent column-index set for the matrix
      `H` that appears in Theorem 3 [Or2020]_

    OUTPUT:

    A generator of ``(eigenvalue, xi, eta, multiplicity)`` quartets
    where

    - ``eigenvalue`` is a real eigenvalue of the system

    - ``xi`` is the first (length ``len(I)``) component of an
      eigenvector associated with ``eigenvalue``

    - ``eta`` is the second (length ``len(J)``) component of an
      eigenvector associated with ``eigenvalue``

    - ``multiplicity`` is the dimension of the eigenspace associated
      with ``eigenvalue``

    Note that we do not return a basis for each eigenspace along with
    its eigenvalue. For the application we have in mind, an eigenspace
    of dimension greater than one (so, ``multiplicity > 1``) is an
    error. As such, our return value is optimized for convenience in
    the non-error case, where there is only one eigenvector (spanning
    a one-dimensional eigenspace) associated with each eigenvalue.

    ALGORITHM:

    According to Proposition 5 [Or2020]_, the solutions corresponding
    to nonzero eigenvalues can be found by solving a smaller
    eigenvalue problem in only the variable `\\xi`. So, we do that, and
    then solve for `\\eta` in terms of `\\xi` as described in the
    proposition.

    EXAMPLES:

    When the zero solutions are included, this function returns the
    same solutions as the naive method on the Schur cone in three
    dimensions::

        sage: from itertools import chain
        sage: from sage.geometry.cone_critical_angles import (
        ....:   _normalize_gevp_solution,
        ....:   _solve_gevp_naive,
        ....:   gevp_licis,
        ....:   solve_gevp_nonzero,
        ....:   solve_gevp_zero)
        sage: K = cones.schur(3)
        sage: gs = [g.change_ring(AA).normalized() for g in K]
        sage: G = matrix.column(gs)
        sage: GG = G.transpose() * G
        sage: G_index_sets = list(gevp_licis(G))
        sage: all(
        ....:   set(
        ....:     _normalize_gevp_solution(s)
        ....:     for s in
        ....:     chain(
        ....:       solve_gevp_zero(GG, I, J),
        ....:       solve_gevp_nonzero(GG, GG, GG, I, J)
        ....:     )
        ....:   )
        ....:   ==
        ....:   set(
        ....:     _normalize_gevp_solution(s)
        ....:     for s in
        ....:     _solve_gevp_naive(GG,GG,GG,I,J)
        ....:   )
        ....:   for I in G_index_sets
        ....:   for J in G_index_sets
        ....: )
        True

    TESTS:

    This function should return the same solutions (with zero included,
    of course) as the naive implementation even for random cones::

        sage: # long time
        sage: from itertools import chain
        sage: from sage.geometry.cone_critical_angles import (
        ....:   _normalize_gevp_solution,
        ....:   _random_admissible_cone,
        ....:   _solve_gevp_naive,
        ....:   gevp_licis,
        ....:   solve_gevp_nonzero,
        ....:   solve_gevp_zero)
        sage: n = ZZ.random_element(1,3)
        sage: P = _random_admissible_cone(ambient_dim=n)
        sage: Q = _random_admissible_cone(ambient_dim=n)
        sage: gs = [g.change_ring(AA).normalized() for g in P]
        sage: G = matrix.column(gs)
        sage: GG = G.transpose() * G
        sage: hs = [h.change_ring(AA).normalized() for h in Q]
        sage: H = matrix.column(hs)
        sage: HH = H.transpose() * H
        sage: M = G.transpose() * H
        sage: G_index_sets = list(gevp_licis(G))
        sage: H_index_sets = list(gevp_licis(H))
        sage: all(
        ....:   set(
        ....:     _normalize_gevp_solution(s)
        ....:     for s in
        ....:     chain(
        ....:       solve_gevp_zero(M, I, J),
        ....:       solve_gevp_nonzero(GG, HH, M, I, J)
        ....:     )
        ....:   )
        ....:   ==
        ....:   set(
        ....:     _normalize_gevp_solution(s)
        ....:     for s in
        ....:     _solve_gevp_naive(GG, HH, M, I, J)
        ....:   )
        ....:   for I in G_index_sets
        ....:   for J in H_index_sets
        ....: )
        True

    According to Proposition 7 [Or2020]_, the only eigenvalues that
    arise when either ``G`` or ``H`` is invertible are `-1`, `0`, and
    `1`::

        sage: # long time
        sage: from sage.geometry.cone_critical_angles import (
        ....:   _random_admissible_cone,
        ....:   gevp_licis,
        ....:   solve_gevp_nonzero)
        sage: n = ZZ.random_element(1,3)
        sage: P = _random_admissible_cone(ambient_dim=n)
        sage: Q = _random_admissible_cone(ambient_dim=n)
        sage: gs = [g.change_ring(AA).normalized() for g in P]
        sage: hs = [h.change_ring(AA).normalized() for h in Q]
        sage: G = matrix.column(gs)
        sage: GG = G.transpose() * G
        sage: H = matrix.column(hs)
        sage: HH = H.transpose() * H
        sage: M = G.transpose() * H
        sage: from itertools import product
        sage: all(
        ....:  (v in [-1,0,1]
        ....:   for (v,_,_,_) in solve_gevp_nonzero(GG, HH, M, I, J))
        ....:   for (I,J) in product(gevp_licis(G),gevp_licis(H))
        ....:   if len(I) == n or len(J) == n )
        True
    """
def compute_gevp_M(gs, hs):
    '''
    Compute the matrix `M` whose `(i,j)`-th entry is the inner
    product of ``gs[i]`` and ``hs[j]``.

    This is the "generalized Gram matrix" appearing in Proposition 6
    in [Or2020]_. For efficiency, we also return the minimal pair,
    whose inner product is minimal among the entries of `M`. This
    allows our consumer to bail out immediately (knowing the optimal
    pair!) if it turns out that the maximal angle is acute; i.e. if
    the smallest entry of `M` is nonnegative.

    INPUT:

    - ``gs`` -- a linearly independent list of unit-norm generators
      for the cone `P`

    - ``hs`` -- a linearly independent list of unit-norm generators
      for the cone `Q`

    OUTPUT: a tuple containing four elements, in order:

    - The matrix `M` described in Proposition 6

    - The minimal entry in the matrix `M`

    - A vector in ``gs`` that achieves that minimal inner product
      along with the next element of the tuple

    - A vector in ``hs`` that achieves the minimal inner product
      along with the previous element in the tuple

    EXAMPLES::

        sage: from sage.geometry.cone_critical_angles import compute_gevp_M
        sage: P = Cone([ (1,2,0), (3,4,0) ])
        sage: Q = Cone([ (-1,4,1), (5,-2,-1),  (-1,-1,5) ])
        sage: gs = [g.change_ring(QQ) for g in P]
        sage: hs = [h.change_ring(QQ) for h in Q]
        sage: M = compute_gevp_M(gs, hs)[0]
        sage: all( M[i][j] == gs[i].inner_product(hs[j])
        ....:       for i in range(P.nrays())
        ....:       for j in range(Q.nrays()) )
        True

    TESTS:

    The products `(G_{I})^{T}H_{J}` correspond to
    submatrices of the "generalized Gram matrix" `M` in Proposition
    6. Note that SageMath does (row,column) indexing but [Or2020]_
    does (column,row) indexing::

        sage: from sage.geometry.cone_critical_angles import (
        ....:   _random_admissible_cone,
        ....:   compute_gevp_M,
        ....:   gevp_licis)
        sage: n = ZZ.random_element(1,4)
        sage: n = ZZ.random_element(1,8) # long time
        sage: P = _random_admissible_cone(ambient_dim=n)
        sage: Q = _random_admissible_cone(ambient_dim=n)
        sage: gs = [g.change_ring(QQ) for g in P]
        sage: hs = [h.change_ring(QQ) for h in Q]
        sage: M = compute_gevp_M(gs,hs)[0]
        sage: f = lambda i,j: gs[i].inner_product(hs[j])
        sage: expected_M = matrix(QQ, P.nrays(), Q.nrays(), f)
        sage: M == expected_M
        True
        sage: G = matrix.column(gs)
        sage: H = matrix.column(hs)
        sage: def _test_indexing(I, J):
        ....:      G_I = G.matrix_from_columns(I)
        ....:      H_J = H.matrix_from_columns(J)
        ....:      return (G_I.transpose()*H_J == M[I,J]
        ....:              and
        ....:              H_J.transpose()*G_I == M.transpose()[J,I])
        sage: G_index_sets = list(gevp_licis(G))
        sage: H_index_sets = list(gevp_licis(H))
        sage: all( _test_indexing(I,J) for I in G_index_sets
        ....:                          for J in H_index_sets )
        True
    '''
def check_gevp_feasibility(cos_theta, xi, eta, G_I, G_I_c_T, H_J, H_J_c_T, epsilon):
    '''
    Determine if a solution to the generalized eigenvalue problem
    in Theorem 3 [Or2020]_ is feasible.

    Implementation detail: we take four matrices that we are capable
    of computing as parameters instead, because we will be called in a
    nested loop "for all `I`... and for all `J`..." The data
    corresponding to `I` should be computed only once, which means
    that we can\'t do it here -- it needs to be done outside of the `J`
    loop. For symmetry (and to avoid relying on too many
    cross-function implementation details), we also insist that the
    `J` data be passed in.

    INPUT:

    - ``cos_theta`` -- an eigenvalue corresponding to
      `( \\xi, \\eta )`

    - ``xi`` -- first component of the `( \\xi, \\eta )` eigenvector

    - ``eta`` -- second component of the `( \\xi, \\eta )` eigenvector

    - ``G_I`` -- the submatrix of `G` with columns indexed by `I`

    - ``G_I_c_T`` -- a matrix whose rows are the non-`I` columns of `G`

    - ``H_J`` -- the submatrix of `H` with columns indexed by `J`

    - ``H_J_c_T`` -- a matrix whose rows are the non-`J` columns of `H`

    - ``epsilon`` -- the tolerance to use when making comparisons

    OUTPUT:

    A triple containing (in order),

    - a boolean,
    - a vector in the cone `P` (of the same length as ``xi``), and
    - a vector in the cone `Q` (of the same length as ``eta``).

    If `( \\xi, \\eta )` is feasible, we return ``(True, u, v)`` where `u`
    and `v` are the vectors in `P` and `Q` respectively that form the
    the angle `\\theta`.

    If `( \\xi, \\eta )` is **not** feasible, then we return ``(False, 0, 0)``
    where ``0`` should be interpreted to mean the zero vector in the
    appropriate space.

    EXAMPLES:

    If `\\xi` has any components less than "zero," it isn\'t feasible::

        sage: from sage.geometry.cone_critical_angles import(
        ....:   check_gevp_feasibility)
        sage: xi = vector(QQ, [-1,1])
        sage: eta = vector(QQ, [1,1,1])
        sage: check_gevp_feasibility(0,xi,eta,None,None,None,None,0)
        (False, (0, 0), (0, 0, 0))

    If `\\eta` has any components less than "zero," it isn\'t feasible::

        sage: from sage.geometry.cone_critical_angles import(
        ....:   check_gevp_feasibility)
        sage: xi = vector(QQ, [2])
        sage: eta = vector(QQ, [1,-4,4,5])
        sage: check_gevp_feasibility(0,xi,eta,None,None,None,None,0)
        (False, (0), (0, 0, 0, 0))

    If `\\xi` and `\\eta` are equal and if `G_{I}` and `H_{J}` are not,
    then the copy of `\\eta` that\'s been scaled by the norm of `G_{I}\\xi`
    generally won\'t satisfy its norm-equality constraint::

        sage: from sage.geometry.cone_critical_angles import(
        ....:   check_gevp_feasibility)
        sage: xi = vector(QQ, [1,1])
        sage: eta = xi
        sage: G_I = matrix.identity(QQ,2)
        sage: H_J = 2*G_I
        sage: check_gevp_feasibility(0,xi,eta,G_I,None,H_J,None,0)
        (False, (0, 0), (0, 0))

    When `\\cos\\theta` is zero, the inequality (42) in Theorem 7.3
    [SS2016]_ is just an inner product with `v` which we can make
    positive by ensuring that all of the entries of `H_{J}` are
    positive. So, if any of the rows of ``G_I_c_T`` contain a negative
    entry, (42) will fail::

        sage: from sage.geometry.cone_critical_angles import(
        ....:   check_gevp_feasibility)
        sage: xi = vector(QQ, [1/2,1/2,1/2,1/2])
        sage: eta = xi
        sage: G_I = matrix.identity(QQ,4)
        sage: G_I_c_T = matrix(QQ, [[0,-1,0,0]])
        sage: H_J = G_I
        sage: check_gevp_feasibility(0,xi,eta,G_I,G_I_c_T,H_J,None,0)
        (False, (0, 0, 0, 0), (0, 0, 0, 0))

    Likewise we can make (43) fail in exactly the same way::

        sage: from sage.geometry.cone_critical_angles import(
        ....:   check_gevp_feasibility)
        sage: xi = vector(QQ, [1/2,1/2,1/2,1/2])
        sage: eta = xi
        sage: G_I = matrix.identity(QQ,4)
        sage: G_I_c_T = matrix(QQ, [[0,1,0,0]])
        sage: H_J = G_I
        sage: H_J_c_T = matrix(QQ, [[0,-1,0,0]])
        sage: check_gevp_feasibility(0,xi,eta,G_I,G_I_c_T,H_J,H_J_c_T,0)
        (False, (0, 0, 0, 0), (0, 0, 0, 0))

    Finally, if we ensure that everything works, we get back a feasible
    result along with the vectors (scaled `\\xi` and `\\eta`) that worked::

        sage: from sage.geometry.cone_critical_angles import(
        ....:   check_gevp_feasibility)
        sage: xi = vector(QQ, [1/2,1/2,1/2,1/2])
        sage: eta = xi
        sage: G_I = matrix.identity(QQ,4)
        sage: G_I_c_T = matrix(QQ, [[0,1,0,0]])
        sage: H_J = G_I
        sage: H_J_c_T = matrix(QQ, [[0,1,0,0]])
        sage: check_gevp_feasibility(0,xi,eta,G_I,G_I_c_T,H_J,H_J_c_T,0)
        (True, (1/2, 1/2, 1/2, 1/2), (1/2, 1/2, 1/2, 1/2))
    '''
def max_angle(P, Q, exact, epsilon):
    """
    Find the maximal angle between the cones `P` and `Q`.

    This implements
    :meth:`sage.geometry.cone.ConvexRationalPolyhedralCone.max_angle`,
    which should be fully documented.

    EXAMPLES:

    For the sake of the user interface, the argument validation for
    this function is performed in the associated cone method; we can
    therefore crash it by feeding it invalid input like an
    inadmissible cone::

        sage: from sage.geometry.cone_critical_angles import max_angle
        sage: K = cones.trivial(3)
        sage: max_angle(K,K,True,0)
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
    """
