from _typeshed import Incomplete
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.rational_field import QQ as QQ

VERIFY_RESULT: bool

def random_inequalities(d, n):
    """
    Random collections of inequalities for testing purposes.

    INPUT:

    - ``d`` -- integer; the dimension

    - ``n`` -- integer; the number of random inequalities to generate

    OUTPUT: a random set of inequalities as a :class:`StandardAlgorithm` instance

    EXAMPLES::

        sage: from sage.geometry.polyhedron.double_description import random_inequalities
        sage: P = random_inequalities(5, 10)
        sage: P.run().verify()
    """

class DoubleDescriptionPair:
    problem: Incomplete
    A: Incomplete
    R: Incomplete
    one: Incomplete
    zero: Incomplete
    zero_set_cache: Incomplete
    def __init__(self, problem, A_rows, R_cols) -> None:
        """
        Base class for a double description pair `(A, R)`.

        .. warning::

            You should use the :meth:`Problem.initial_pair` or
            :meth:`Problem.run` to generate double description pairs
            for a set of inequalities, and not generate
            ``DoubleDescriptionPair`` instances directly.

        INPUT:

        - ``problem`` -- instance of :class:`Problem`

        - ``A_rows`` -- list of row vectors of the matrix `A`; these
          encode the inequalities

        - ``R_cols`` -- list of column vectors of the matrix
          `R`; these encode the rays

        TESTS::

            sage: from sage.geometry.polyhedron.double_description import \\\n            ....:     DoubleDescriptionPair, Problem
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: alg = Problem(A)
            sage: DoubleDescriptionPair(alg,
            ....:     [(1, 0, 1), (0, 1, 1), (-1, -1, 1)],
            ....:     [(2/3, -1/3, 1/3), (-1/3, 2/3, 1/3), (-1/3, -1/3, 1/3)])
            Double description pair (A, R) defined by
                [ 1  0  1]        [ 2/3 -1/3 -1/3]
            A = [ 0  1  1],   R = [-1/3  2/3 -1/3]
                [-1 -1  1]        [ 1/3  1/3  1/3]
        """
    def inner_product_matrix(self):
        """
        Return the inner product matrix between the rows of `A`
        and the columns of `R`.

        OUTPUT:

        A matrix over the base ring. There is one row for each row of
        `A` and one column for each column of `R`.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: alg = StandardAlgorithm(A)
            sage: DD, _ = alg.initial_pair()
            sage: DD.inner_product_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def cone(self):
        """
        Return the cone defined by `A`.

        This method is for debugging only. Assumes that the base ring
        is `\\QQ`.

        OUTPUT:

        The cone defined by the inequalities as a
        :func:`~sage.geometry.polyhedron.constructor.Polyhedron`,
        using the PPL backend.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: DD, _ = StandardAlgorithm(A).initial_pair()
            sage: DD.cone().Hrepresentation()
            (An inequality (-1, -1, 1) x + 0 >= 0,
             An inequality (0, 1, 1) x + 0 >= 0,
             An inequality (1, 0, 1) x + 0 >= 0)
        """
    def verify(self) -> None:
        """
        Validate the double description pair.

        This method used the PPL backend to check that the double
        description pair is valid. An assertion is triggered if it is
        not. Does nothing if the base ring is not `\\QQ`.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import \\\n            ....:     DoubleDescriptionPair, Problem
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: alg = Problem(A)
            sage: DD = DoubleDescriptionPair(alg,
            ....:     [(1, 0, 3), (0, 1, 1), (-1, -1, 1)],
            ....:     [(2/3, -1/3, 1/3), (-1/3, 2/3, 1/3), (-1/3, -1/3, 1/3)])
            sage: DD.verify()
            Traceback (most recent call last):
            ...
                assert A_cone == R_cone
            AssertionError
        """
    def R_by_sign(self, a):
        """
        Classify the rays into those that are positive, zero, and negative on `a`.

        INPUT:

        - ``a`` -- vector; coefficient vector of a homogeneous inequality

        OUTPUT:

        A triple consisting of the rays (columns of `R`) that are
        positive, zero, and negative on `a`. In that order.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: DD, _ = StandardAlgorithm(A).initial_pair()
            sage: DD.R_by_sign(vector([1,-1,0]))
            ([(2/3, -1/3, 1/3)], [(-1/3, -1/3, 1/3)], [(-1/3, 2/3, 1/3)])
            sage: DD.R_by_sign(vector([1,1,1]))
            ([(2/3, -1/3, 1/3), (-1/3, 2/3, 1/3)], [], [(-1/3, -1/3, 1/3)])
        """
    def zero_set(self, ray):
        """
        Return the zero set (active set) `Z(r)`.

        INPUT:

        - ``ray`` -- a ray vector

        OUTPUT: a set containing the inequality vectors that are zero on ``ray``

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: DD, _ = Problem(A).initial_pair()
            sage: r = DD.R[0];  r
            (2/3, -1/3, 1/3)
            sage: DD.zero_set(r)
            {(-1, -1, 1), (0, 1, 1)}
        """
    def is_extremal(self, ray):
        """
        Test whether the ray is extremal.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: A = matrix(QQ, [(0,1,0), (1,0,0), (0,-1,1), (-1,0,1)])
            sage: DD = StandardAlgorithm(A).run()
            sage: DD.is_extremal(DD.R[0])
            True
        """
    @cached_method
    def matrix_space(self, nrows, ncols):
        """
        Return a matrix space of size ``nrows`` and ``ncols`` over the base ring
        of ``self``.

        These matrix spaces are cached to avoid their creation in the very
        demanding :meth:`add_inequality` and more precisely :meth:`are_adjacent`.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: A = matrix(QQ, [(1,0,1), (0,1,1), (-1,-1,1)])
            sage: DD, _ = Problem(A).initial_pair()
            sage: DD.matrix_space(2,2)
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: DD.matrix_space(3,2)
            Full MatrixSpace of 3 by 2 dense matrices over Rational Field

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: A = matrix([[1,sqrt2],[2,0]])
            sage: DD, _  = Problem(A).initial_pair()
            sage: DD.matrix_space(1,2)
            Full MatrixSpace of 1 by 2 dense matrices
             over Number Field in sqrt2 with defining polynomial x^2 - 2 with sqrt2 = 1.414213562373095?
        """
    def are_adjacent(self, r1, r2):
        """
        Return whether the two rays are adjacent.

        INPUT:

        - ``r1``, ``r2`` -- two rays

        OUTPUT: boolean; whether the two rays are adjacent

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: A = matrix(QQ, [(0,1,0), (1,0,0), (0,-1,1), (-1,0,1)])
            sage: DD = StandardAlgorithm(A).run()
            sage: DD.are_adjacent(DD.R[0], DD.R[1])
            True
            sage: DD.are_adjacent(DD.R[0], DD.R[2])
            True
            sage: DD.are_adjacent(DD.R[0], DD.R[3])
            False
        """
    def dual(self):
        """
        Return the dual.

        OUTPUT:

        For the double description pair `(A, R)` this method returns
        the dual double description pair `(R^T, A^T)`

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: A = matrix(QQ, [(0,1,0), (1,0,0), (0,-1,1), (-1,0,1)])
            sage: DD, _ = Problem(A).initial_pair()
            sage: DD
            Double description pair (A, R) defined by
                [ 0  1  0]        [0 1 0]
            A = [ 1  0  0],   R = [1 0 0]
                [ 0 -1  1]        [1 0 1]
            sage: DD.dual()
             Double description pair (A, R) defined by
                [0 1 1]        [ 0  1  0]
            A = [1 0 0],   R = [ 1  0 -1]
                [0 0 1]        [ 0  0  1]
        """
    def first_coordinate_plane(self):
        """
        Restrict to the first coordinate plane.

        OUTPUT:

        A new double description pair with the constraint `x_0 = 0`
        added.

        EXAMPLES::

            sage: A = matrix([(1, 1), (-1, 1)])
            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: DD, _ = StandardAlgorithm(A).initial_pair()
            sage: DD
            Double description pair (A, R) defined by
            A = [ 1  1],   R = [ 1/2 -1/2]
                [-1  1]        [ 1/2  1/2]
            sage: DD.first_coordinate_plane()
            Double description pair (A, R) defined by
                [ 1  1]
            A = [-1  1],   R = [  0]
                [-1  0]        [1/2]
                [ 1  0]
        """

class Problem:
    pair_class = DoubleDescriptionPair
    def __init__(self, A) -> None:
        """
        Base class for implementations of the double description algorithm.

        It does not make sense to instantiate the base class directly,
        it just provides helpers for implementations.

        INPUT:

        - ``A`` -- a matrix; the rows of the matrix are interpreted as
          homogeneous inequalities `A x \\geq 0`. Must have maximal rank.

        TESTS::

            sage: A = matrix([(1, 1), (-1, 1)])
            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: Problem(A)
            Pointed cone with inequalities
            (1, 1)
            (-1, 1)
        """
    @cached_method
    def A(self):
        """
        Return the rows of the defining matrix `A`.

        OUTPUT: the matrix `A` whose rows are the inequalities

        EXAMPLES::

            sage: A = matrix([(1, 1), (-1, 1)])
            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: Problem(A).A()
            ((1, 1), (-1, 1))
        """
    def A_matrix(self):
        """
        Return the defining matrix `A`.

        OUTPUT: matrix whose rows are the inequalities

        EXAMPLES::

            sage: A = matrix([(1, 1), (-1, 1)])
            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: Problem(A).A_matrix()
            [ 1  1]
            [-1  1]
        """
    def base_ring(self):
        """
        Return the base field.

        OUTPUT: a field

        EXAMPLES::

            sage: A = matrix(AA, [(1, 1), (-1, 1)])                                     # needs sage.rings.number_field
            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: Problem(A).base_ring()                                                # needs sage.rings.number_field
            Algebraic Real Field
        """
    @cached_method
    def dim(self):
        """
        Return the ambient space dimension.

        OUTPUT: integer; the ambient space dimension of the cone

        EXAMPLES::

            sage: A = matrix(QQ, [(1, 1), (-1, 1)])
            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: Problem(A).dim()
            2
        """
    def initial_pair(self):
        """
        Return an initial double description pair.

        Picks an initial set of rays by selecting a basis. This is
        probably the most efficient way to select the initial set.

        INPUT:

        - ``pair_class`` -- subclass of
          :class:`DoubleDescriptionPair`

        OUTPUT:

        A pair consisting of a :class:`DoubleDescriptionPair` instance
        and the tuple of remaining unused inequalities.

        EXAMPLES::

            sage: A = matrix([(-1, 1), (-1, 2), (1/2, -1/2), (1/2, 2)])
            sage: from sage.geometry.polyhedron.double_description import Problem
            sage: DD, remaining = Problem(A).initial_pair()
            sage: DD.verify()
            sage: remaining
            [(1/2, -1/2), (1/2, 2)]
        """

class StandardDoubleDescriptionPair(DoubleDescriptionPair):
    '''
    Double description pair for the "Standard Algorithm".

    See :class:`StandardAlgorithm`.

    TESTS::

        sage: A = matrix([(-1, 1, 0), (-1, 2, 1), (1/2, -1/2, -1)])
        sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
        sage: DD, _ = StandardAlgorithm(A).initial_pair()
    '''
    R: Incomplete
    def add_inequality(self, a) -> None:
        """
        Add the inequality ``a`` to the matrix `A` of the double description.

        INPUT:

        - ``a`` -- vector; an inequality

        EXAMPLES::

            sage: A = matrix([(-1, 1, 0), (-1, 2, 1), (1/2, -1/2, -1)])
            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: DD, _ = StandardAlgorithm(A).initial_pair()
            sage: DD.add_inequality(vector([1,0,0]))
            sage: DD
            Double description pair (A, R) defined by
                [  -1    1    0]        [   1    1    0    0]
            A = [  -1    2    1],   R = [   1    1    1    1]
                [ 1/2 -1/2   -1]        [   0   -1 -1/2   -2]
                [   1    0    0]
        """

class StandardAlgorithm(Problem):
    '''
    Standard implementation of the double description algorithm.

    See [FP1996]_ for the definition of the "Standard
    Algorithm".

    EXAMPLES::

        sage: A = matrix(QQ, [(1, 1), (-1, 1)])
        sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
        sage: DD = StandardAlgorithm(A).run()
        sage: DD.R    # the extremal rays
        [(1/2, 1/2), (-1/2, 1/2)]
    '''
    pair_class = StandardDoubleDescriptionPair
    def run(self):
        """
        Run the Standard Algorithm.

        OUTPUT:

        A double description pair `(A, R)` of all inequalities as a
        :class:`DoubleDescriptionPair`.  By virtue of the double
        description algorithm, the columns of `R` are the extremal
        rays.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.double_description import StandardAlgorithm
            sage: A = matrix(QQ, [(0,1,0), (1,0,0), (0,-1,1), (-1,0,1)])
            sage: StandardAlgorithm(A).run()
            Double description pair (A, R) defined by
                [ 0  1  0]        [0 0 1 1]
            A = [ 1  0  0],   R = [1 0 1 0]
                [ 0 -1  1]        [1 1 1 1]
                [-1  0  1]
        """
