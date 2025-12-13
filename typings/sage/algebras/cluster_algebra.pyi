from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import binomial as binomial
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.categories.rings import Rings as Rings
from sage.combinat.cluster_algebra_quiver.quiver import ClusterQuiver as ClusterQuiver
from sage.combinat.permutation import Permutation as Permutation
from sage.graphs.digraph import DiGraph as DiGraph
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.matrix.special import block_matrix as block_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing, LaurentPolynomialRing_generic as LaurentPolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ClusterAlgebraElement(ElementWrapper):
    """
    An element of a cluster algebra.
    """
    def d_vector(self) -> tuple:
        """
        Return the denominator vector of ``self`` as a tuple of integers.

        EXAMPLES::

            sage: A = ClusterAlgebra(['F', 4], principal_coefficients=True)
            sage: A.current_seed().mutate([0, 2, 1])
            sage: x = A.cluster_variable((-1, 2, -2, 2)) * A.cluster_variable((0, 0, 0, 1))**2
            sage: x.d_vector()
            (1, 1, 2, -2)
        """

class PrincipalClusterAlgebraElement(ClusterAlgebraElement):
    """
    An element in a cluster algebra with principle coefficients.
    """
    def g_vector(self):
        """
        Return the g-vector of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['B', 2], principal_coefficients=True)
            sage: A.cluster_variable((1, 0)).g_vector() == (1, 0)
            True
            sage: sum(A.initial_cluster_variables()).g_vector()
            Traceback (most recent call last):
            ...
            ValueError: this element does not have a well defined g-vector
        """
    def F_polynomial(self):
        """
        Return the F-polynomial of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['B', 2], principal_coefficients=True)
            sage: S = A.initial_seed()
            sage: S.mutate([0, 1, 0])
            sage: S.cluster_variable(0).F_polynomial() == S.F_polynomial(0)
            True
            sage: sum(A.initial_cluster_variables()).F_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: this element does not have a well defined g-vector
        """
    def is_homogeneous(self) -> bool:
        """
        Return ``True`` if ``self`` is a homogeneous element
        of ``self.parent()``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['B', 2], principal_coefficients=True)
            sage: A.cluster_variable((1, 0)).is_homogeneous()
            True
            sage: x = A.cluster_variable((1, 0)) + A.cluster_variable((0, 1))
            sage: x.is_homogeneous()
            False
        """
    def homogeneous_components(self) -> dict:
        """
        Return a dictionary of the homogeneous components of ``self``.

        OUTPUT:

        A dictionary whose keys are homogeneous degrees and whose values
        are the summands of ``self`` of the given degree.

        EXAMPLES::

            sage: A = ClusterAlgebra(['B', 2], principal_coefficients=True)
            sage: x = A.cluster_variable((1, 0)) + A.cluster_variable((0, 1))
            sage: x.homogeneous_components()
            {(0, 1): x1, (1, 0): x0}
        """
    def theta_basis_decomposition(self):
        """
        Return the decomposition of ``self`` in the theta basis.

        OUTPUT:

        A dictionary whose keys are the g-vectors and whose values are the coefficients
        in the decomposition of ``self`` in the theta basis.

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,-2],[3,0]]), principal_coefficients=True)
            sage: f = (A.theta_basis_element((1,0)) + A.theta_basis_element((0,1)))**2 + A.coefficient(1)* A.theta_basis_element((1,1))
            sage: decomposition = f.theta_basis_decomposition()
            sage: sum(decomposition[g] * A.theta_basis_element(g) for g in decomposition) == f
            True
            sage: f = A.theta_basis_element((4,-4))*A.theta_basis_element((1,-1))
            sage: decomposition =  f.theta_basis_decomposition()
            sage: sum(decomposition[g] * A.theta_basis_element(g) for g in decomposition) == f
            True
        """

class ClusterAlgebraSeed(SageObject):
    """
    A seed in a Cluster Algebra.

    INPUT:

    - ``B`` -- a skew-symmetrizable integer matrix
    - ``C`` -- the matrix of c-vectors of ``self``
    - ``G`` -- the matrix of g-vectors of ``self``
    - ``parent`` -- :class:`ClusterAlgebra`; the algebra to which the
      seed belongs
    - ``path`` -- list (default: ``[]``); the mutation sequence from the
      initial seed of ``parent`` to ``self``

    .. WARNING::

        Seeds should **not** be created manually: no test is performed to
        assert that they are built from consistent data nor that they
        really are seeds of ``parent``. If you create seeds with
        inconsistent data all sort of things can go wrong, even
        :meth:`__eq__` is no longer guaranteed to give correct answers.
        Use at your own risk.
    """
    def __init__(self, B, C, G, parent, **kwargs) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['F', 4])
            sage: from sage.algebras.cluster_algebra import ClusterAlgebraSeed
            sage: ClusterAlgebraSeed(A.b_matrix(), identity_matrix(4), identity_matrix(4), A, path=[1, 2, 3])
            The seed of a Cluster Algebra with cluster variables x0, x1, x2, x3
             and no coefficients over Integer Ring obtained from the initial
             by mutating along the sequence [1, 2, 3]
        """
    def __copy__(self):
        """
        Return a copy of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = copy(A.current_seed())
            sage: S == A.current_seed()
            True
            sage: S is not A.current_seed()
            True
        """
    def __eq__(self, other):
        """
        Test equality of two seeds.

        INPUT:

        - ``other`` -- a :class:`ClusterAlgebraSeed`

        ALGORITHM:

        ``self`` and ``other`` are deemed to be equal if they have the same
        parent and their set of g-vectors coincide, i.e. this tests
        equality of unlabelled seeds.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: A.clear_computed_data()
            sage: S = copy(A.current_seed())
            sage: S.mutate([0, 2, 0])
            sage: S == A.current_seed()
            False
            sage: S.mutate(2)
            sage: S == A.current_seed()
            True

            sage: A = ClusterAlgebra(['B', 2], principal_coefficients=True)
            sage: S = A.current_seed()
            sage: S.mutate(0)
            sage: S == A.current_seed()
            True
        """
    def __contains__(self, element) -> bool:
        """
        Test whether ``element`` belong to ``self``.

        INPUT:

        - ``element`` -- either a g-vector or an element of :meth:`parent`

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: (1, 0, 0) in S
            True
            sage: (1, 1, 0) in S
            False
            sage: A.cluster_variable((1, 0, 0)) in S
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        ALGORITHM:

        For speed purposes the hash is computed on :meth:`self.g_vectors`.
        In particular it is guaranteed to be unique only within a given
        instance of :class:`ClusterAlgebra`. Moreover unlabelled seeds that
        have the same set of g-vectors have the same hash.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: T = S.mutate(1, inplace=False)
            sage: hash(S) == hash(S)
            True
            sage: hash(S) == hash(T)
            False
        """
    def parent(self):
        """
        Return the parent of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['B', 3])
            sage: A.current_seed().parent() == A
            True
        """
    def depth(self) -> int:
        """
        Return the length of a mutation sequence from the initial seed
         of :meth:`parent` to ``self``.

        .. WARNING::

            This is the length of the mutation sequence returned by
            :meth:`path_from_initial_seed`, which need not be the
            shortest possible.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: S1 = A.initial_seed()
            sage: S1.mutate([0, 1, 0, 1])
            sage: S1.depth()
            4
            sage: S2 = A.initial_seed()
            sage: S2.mutate(1)
            sage: S2.depth()
            1
            sage: S1 == S2
            True
        """
    def path_from_initial_seed(self) -> list:
        """
        Return a mutation sequence from the initial seed of :meth:`parent`
        to ``self``.

        .. WARNING::

            This is the path used to compute ``self`` and it does not
            have to be the shortest possible.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: S1 = A.initial_seed()
            sage: S1.mutate([0, 1, 0, 1])
            sage: S1.path_from_initial_seed()
            [0, 1, 0, 1]
            sage: S2 = A.initial_seed()
            sage: S2.mutate(1)
            sage: S2.path_from_initial_seed()
            [1]
            sage: S1 == S2
            True
        """
    def b_matrix(self):
        """
        Return the exchange matrix of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.b_matrix()
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]
        """
    def c_matrix(self):
        """
        Return the matrix whose columns are the c-vectors of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.c_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def c_vector(self, j) -> tuple:
        """
        Return the ``j``-th c-vector of ``self``.

        INPUT:

        - ``j`` -- integer in ``range(self.parent().rank())``;
          the index of the c-vector to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.c_vector(0)
            (1, 0, 0)
            sage: S.mutate(0)
            sage: S.c_vector(0)
            (-1, 0, 0)
            sage: S.c_vector(1)
            (1, 1, 0)
        """
    def c_vectors(self) -> list[tuple]:
        """
        Return all the c-vectors of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.c_vectors()
            [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        """
    def g_matrix(self):
        """
        Return the matrix whose columns are the g-vectors of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.g_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def g_vector(self, j) -> tuple:
        """
        Return the ``j``-th g-vector of ``self``.

        INPUT:

        - ``j`` -- integer in ``range(self.parent().rank())``;
          the index of the g-vector to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.g_vector(0)
            (1, 0, 0)
        """
    def g_vectors(self) -> list[tuple]:
        """
        Return all the g-vectors of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.g_vectors()
            [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        """
    def F_polynomial(self, j):
        """
        Return the ``j``-th F-polynomial of ``self``.

        INPUT:

        - ``j`` -- integer in ``range(self.parent().rank())``;
          the index of the F-polynomial to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.F_polynomial(0)
            1
        """
    def F_polynomials(self) -> list:
        """
        Return all the F-polynomials of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.F_polynomials()
            [1, 1, 1]
        """
    def cluster_variable(self, j):
        """
        Return the ``j``-th cluster variable of ``self``.

        INPUT:

        - ``j`` -- integer in ``range(self.parent().rank())``;
          the index of the cluster variable to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.cluster_variable(0)
            x0
            sage: S.mutate(0)
            sage: S.cluster_variable(0)
            (x1 + 1)/x0
        """
    def cluster_variables(self) -> list:
        """
        Return all the cluster variables of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: S = A.initial_seed()
            sage: S.cluster_variables()
            [x0, x1, x2]
        """
    def mutate(self, direction, **kwargs):
        '''
        Mutate ``self``.

        INPUT:

        - ``direction`` -- in which direction(s) to mutate, it can be:

          * an integer in ``range(self.rank())`` to mutate in one direction only
          * an iterable of such integers to mutate along a sequence
          * a string "sinks" or "sources" to mutate at all sinks or sources simultaneously

        - ``inplace`` -- boolean (default: ``True``); whether to mutate in place
          or to return a new object

        - ``mutating_F`` -- boolean (default: ``True``); whether to compute
          F-polynomials while mutating

        .. NOTE::

            While knowing F-polynomials is essential to computing
            cluster variables, the process of mutating them is quite slow.
            If you care only about combinatorial data like g-vectors and
            c-vectors, setting ``mutating_F=False`` yields significant
            benefits in terms of speed.

        EXAMPLES::

            sage: A = ClusterAlgebra([\'A\', 2])
            sage: S = A.initial_seed()
            sage: S.mutate(0); S
            The seed of a Cluster Algebra with cluster variables x0, x1
             and no coefficients over Integer Ring obtained from the initial
             by mutating in direction 0
            sage: S.mutate(5)
            Traceback (most recent call last):
            ...
            ValueError: cannot mutate in direction 5
        '''

class ClusterAlgebra(Parent, UniqueRepresentation):
    """
    A Cluster Algebra.

    INPUT:

    - ``data`` -- some data defining a cluster algebra; it can be anything
      that can be parsed by :class:`ClusterQuiver`

    - ``scalars`` -- a ring (default: `\\ZZ`); the scalars over
      which the cluster algebra is defined

    - ``cluster_variable_prefix`` -- string (default: ``'x'``); it needs to be
      a valid variable name

    - ``cluster_variable_names`` -- list of strings; each element needs
      to be a valid variable name;  supersedes ``cluster_variable_prefix``

    - ``coefficient_prefix`` -- string (default: ``'y'``); it needs to be
      a valid variable name

    - ``coefficient_names`` -- list of strings; each element needs
      to be a valid variable name; supersedes ``cluster_variable_prefix``

    - ``principal_coefficients`` -- boolean (default: ``False``); supersedes any
      coefficient defined by ``data``

    ALGORITHM:

    The implementation is mainly based on [FZ2007]_ and [NZ2012]_.

    EXAMPLES::

        sage: B = matrix([(0, 1, 0, 0), (-1, 0, -1, 0), (0, 1, 0, 1), (0, 0, -2, 0), (-1, 0, 0, 0), (0, -1, 0, 0)])
        sage: A = ClusterAlgebra(B); A
        A Cluster Algebra with cluster variables x0, x1, x2, x3
         and coefficients y0, y1 over Integer Ring
        sage: A.gens()
        (x0, x1, x2, x3, y0, y1)
        sage: A = ClusterAlgebra(['A', 2]); A
        A Cluster Algebra with cluster variables x0, x1 and no coefficients
         over Integer Ring
        sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True); A.gens()
        (x0, x1, y0, y1)
        sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True, coefficient_prefix='x'); A.gens()
        (x0, x1, x2, x3)
        sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True, cluster_variable_names=['a', 'b', 'c']); A.gens()
        (a, b, c, y0, y1, y2)
        sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True, cluster_variable_names=['a', 'b'])
        Traceback (most recent call last):
        ...
        ValueError: cluster_variable_names should be an iterable of 3 valid variable names
        sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True, coefficient_names=['a', 'b', 'c']); A.gens()
        (x0, x1, x2, a, b, c)
        sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True, coefficient_names=['a', 'b'])
        Traceback (most recent call last):
        ...
        ValueError: coefficient_names should be an iterable of 3 valid variable names
    """
    @staticmethod
    def __classcall__(self, data, **kwargs):
        """
        Preparse input.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2]); A   # indirect doctest
            A Cluster Algebra with cluster variables x0, x1 and no coefficients
            over Integer Ring

        Check that :issue:`28176` is fixed::

            sage: A1 = ClusterAlgebra(['A',2])
            sage: A2 = ClusterAlgebra(['A',2], cluster_variable_prefix='x')
            sage: A1 is A2
            True
            sage: A3 = ClusterAlgebra(Matrix([[0,1],[-1,0]]))
            sage: A1 is A3
            True
            sage: A4 = ClusterAlgebra([[0,1]]) # built from a digraph
            sage: A1 is A4
            True
        """
    Element: Incomplete
    def __init__(self, B, **kwargs) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: B = matrix([(0, 1, 0, 0), (-1, 0, -1, 0), (0, 1, 0, 1), (0, 0, -2, 0), (-1, 0, 0, 0), (0, -1, 0, 0)])
            sage: A = ClusterAlgebra(B)
            sage: A.clear_computed_data()
            sage: TestSuite(A).run()
            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: TestSuite(A).run()
            sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True)
            sage: A.clear_computed_data()
            sage: TestSuite(A).run()
            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True, coefficient_prefix='x')
            sage: A.clear_computed_data()
            sage: TestSuite(A).run()
            sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True, cluster_variable_names=['a','b','c'])
            sage: A.clear_computed_data()
            sage: TestSuite(A).run()
            sage: A = ClusterAlgebra(['A', 3], principal_coefficients=True, coefficient_names=['a','b','c'])
            sage: A.clear_computed_data()
            sage: TestSuite(A).run()
        """
    @cached_method
    def coxeter_element(self):
        """
        Return the Coxeter element associated to the initial exchange matrix, if acyclic.

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,1,1],[-1,0,1],[-1,-1,0]]))
            sage: A.coxeter_element()
            [0, 1, 2]

        Raise an error if the initial exchange matrix is not acyclic::

            sage: A = ClusterAlgebra(matrix([[0,1,-1],[-1,0,1],[1,-1,0]]))
            sage: A.coxeter_element()
            Traceback (most recent call last):
            ...
            ValueError: the initial exchange matrix is not acyclic
        """
    @cached_method
    def is_acyclic(self) -> bool:
        """
        Return ``True`` if the exchange matrix in the initial seed is acyclic, ``False`` otherwise.

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,1,1],[-1,0,1],[-1,-1,0]]))
            sage: A.is_acyclic()
            True
            sage: A = ClusterAlgebra(matrix([[0,1,-1],[-1,0,1],[1,-1,0]]))
            sage: A.is_acyclic()
            False
        """
    def rank(self):
        """
        Return the rank of ``self``, i.e. the number of cluster variables
        in any seed.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True); A
            A Cluster Algebra with cluster variables x0, x1
             and coefficients y0, y1 over Integer Ring
            sage: A.rank()
            2
        """
    def current_seed(self):
        """
        Return the current seed of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: A.current_seed()
            The initial seed of a Cluster Algebra with cluster variables x0, x1
             and no coefficients over Integer Ring
        """
    def set_current_seed(self, seed) -> None:
        """
        Set the value reported by :meth:`current_seed` to ``seed``,
        if it makes sense.

        INPUT:

        - ``seed`` -- a :class:`ClusterAlgebraSeed`

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: S = copy(A.current_seed())
            sage: S.mutate([0, 1, 0])
            sage: A.current_seed() == S
            False
            sage: A.set_current_seed(S)
            sage: A.current_seed() == S
            True
            sage: A1 = ClusterAlgebra(['B', 2])
            sage: A.set_current_seed(A1.initial_seed())
            Traceback (most recent call last):
            ...
            ValueError: this is not a seed in this cluster algebra
        """
    def reset_current_seed(self) -> None:
        """
        Reset the value reported by :meth:`current_seed`
        to :meth:`initial_seed`.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: A.current_seed().mutate([1, 0])
            sage: A.current_seed() == A.initial_seed()
            False
            sage: A.reset_current_seed()
            sage: A.current_seed() == A.initial_seed()
            True
        """
    def clear_computed_data(self) -> None:
        """
        Clear the cache of computed g-vectors and F-polynomials
        and reset both the current seed and the exploring iterator.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: sorted(A.g_vectors_so_far())
            [(0, 1), (1, 0)]
            sage: A.current_seed().mutate([1, 0])
            sage: sorted(A.g_vectors_so_far())
            [(-1, 0), (0, -1), (0, 1), (1, 0)]
            sage: A.clear_computed_data()
            sage: sorted(A.g_vectors_so_far())
            [(0, 1), (1, 0)]
        """
    def contains_seed(self, seed) -> bool:
        """
        Test if ``seed`` is a seed of ``self``.

        INPUT:

        - ``seed`` -- a :class:`ClusterAlgebraSeed`

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True); A
            A Cluster Algebra with cluster variables x0, x1 and coefficients y0, y1 over Integer Ring
            sage: S = copy(A.current_seed())
            sage: A.contains_seed(S)
            True
        """
    def initial_seed(self):
        """
        Return the initial seed of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.initial_seed()
            The initial seed of a Cluster Algebra with cluster variables x0, x1 and no coefficients over Integer Ring
        """
    def b_matrix(self):
        """
        Return the initial exchange matrix of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.b_matrix()
            [ 0  1]
            [-1  0]
        """
    def euler_matrix(self):
        """
        Return the Euler matrix associated to ``self``.

        ALGORITHM:

            This method returns the matrix of the bilinear form defined in Equation (2.1) of [ReSt2020]_ .

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,1,1],[-1,0,1],[-1,-1,0]]))
            sage: A.euler_matrix()
            [ 1  0  0]
            [-1  1  0]
            [-1 -1  1]

        Raise an error if the initial exchange matrix is not acyclic::

            sage: A = ClusterAlgebra(matrix([[0,1,-1],[-1,0,1],[1,-1,0]]))
            sage: A.euler_matrix()
            Traceback (most recent call last):
            ...
            ValueError: the initial exchange matrix is not acyclic
        """
    def d_vector_to_g_vector(self, d) -> tuple:
        """
        Return the g-vector of an element of ``self`` having d-vector ``d``

        INPUT:

        - ``d`` -- the d-vector

        ALGORITHM:

            This method implements the piecewise-linear map `\\\\nu_c` introduced in Section 9.1 of [ReSt2020]_.

        .. WARNING::

            This implementation works only when the initial exchange matrix is acyclic.

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,1,1],[-1,0,1],[-1,-1,0]]))
            sage: A.d_vector_to_g_vector((1,0,-1))
            (-1, 1, 2)
        """
    def g_vector_to_d_vector(self, g) -> tuple:
        """
        Return the d-vector of an element of ``self`` having g-vector ``g``

        INPUT:

        - ``g`` -- the g-vector

        ALGORITHM:

            This method implements the inverse of the piecewise-linear map `\\\\nu_c` introduced in Section 9.1 of [ReSt2020]_.

        .. WARNING::

            This implementation works only when the initial exchange matrix is acyclic.

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,1,1],[-1,0,1],[-1,-1,0]]))
            sage: A.g_vector_to_d_vector((-1,1,2))
            (1, 0, -1)
        """
    def g_vectors(self, mutating_F: bool = True) -> Generator[Incomplete]:
        """
        Return an iterator producing all the g-vectors of ``self``.

        INPUT:

        - ``mutating_F`` -- boolean (default: ``True``); whether to compute
          F-polynomials; disable this for speed considerations

        ALGORITHM:

        This method does not use the caching framework provided by ``self``,
        but recomputes all the g-vectors from scratch. On the other hand it
        stores the results so that other methods like :meth:`g_vectors_so_far`
        can access them afterwards.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: len(list(A.g_vectors()))
            9
        """
    def cluster_variables(self):
        """
        Return an iterator producing all the cluster variables of ``self``.

        ALGORITHM:

        This method does not use the caching framework provided by ``self``,
        but recomputes all the cluster variables from scratch. On the other
        hand it stores the results so that other methods like
        :meth:`cluster_variables_so_far` can access them afterwards.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: len(list(A.cluster_variables()))
            9
        """
    def F_polynomials(self):
        """
        Return an iterator producing all the F_polynomials of ``self``.

        ALGORITHM:

        This method does not use the caching framework provided by ``self``,
        but recomputes all the F-polynomials from scratch. On the other hand
        it stores the results so that other methods like
        :meth:`F_polynomials_so_far` can access them afterwards.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: len(list(A.F_polynomials()))
            9
        """
    def g_vectors_so_far(self) -> list:
        """
        Return a list of the g-vectors of cluster variables encountered so far.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: A.current_seed().mutate(0)
            sage: sorted(A.g_vectors_so_far())
            [(-1, 1), (0, 1), (1, 0)]
        """
    def cluster_variables_so_far(self) -> list:
        """
        Return a list of the cluster variables encountered so far.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: A.current_seed().mutate(0)
            sage: sorted(A.cluster_variables_so_far(), key=str)
            [(x1 + 1)/x0, x0, x1]
        """
    def F_polynomials_so_far(self) -> list:
        """
        Return a list of the F-polynomials encountered so far.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: A.current_seed().mutate(0)
            sage: sorted(A.F_polynomials_so_far(), key=str)
            [1, 1, u0 + 1]
        """
    def cluster_variable(self, g_vector):
        '''
        Return the cluster variable with g-vector ``g_vector`` if it has
        been found.

        INPUT:

        - ``g_vector`` -- tuple; the g-vector of the cluster variable to return

        ALGORITHM:

        This function computes cluster variables from their g-vectors and
        F-polynomials using the "separation of additions" formula of
        Theorem 3.7 in [FZ2007]_.

        EXAMPLES::

            sage: A = ClusterAlgebra([\'A\', 2])
            sage: A.initial_seed().mutate(0)
            sage: A.cluster_variable((-1, 1))
            (x1 + 1)/x0
        '''
    def F_polynomial(self, g_vector):
        """
        Return the F-polynomial with g-vector ``g_vector`` if it has
        been found.

        INPUT:

        - ``g_vector`` -- tuple; the g-vector of the F-polynomial to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.clear_computed_data()
            sage: A.F_polynomial((-1, 1))
            Traceback (most recent call last):
            ...
            KeyError: 'the g-vector (-1, 1) has not been found yet'
            sage: A.initial_seed().mutate(0, mutating_F=False)
            sage: A.F_polynomial((-1, 1))
            Traceback (most recent call last):
            ...
            KeyError: 'the F-polynomial with g-vector (-1, 1) has not been computed yet;
             you can compute it by mutating from the initial seed along the sequence [0]'
            sage: A.initial_seed().mutate(0)
            sage: A.F_polynomial((-1, 1))
            u0 + 1
        """
    def find_g_vector(self, g_vector, depth=...):
        """
        Return a mutation sequence to obtain a seed containing the g-vector
        ``g_vector`` from the initial seed.

        INPUT:

        - ``g_vector`` -- tuple; the g-vector to find
        - ``depth`` -- positive integer or infinity (default: ``infinity``);
          the maximum distance from ``self.current_seed`` to reach

        OUTPUT:

        This function returns a list of integers if it can find ``g_vector``,
        otherwise it returns ``None``.  If the exploring iterator stops, it
        means that the algebra is of finite type and ``g_vector`` is not the
        g-vector of any cluster variable. In this case the function resets the
        iterator and raises an error.

        EXAMPLES::

            sage: A = ClusterAlgebra(['G', 2], principal_coefficients=True)
            sage: A.clear_computed_data()
            sage: A.find_g_vector((-2, 3), depth=2)
            sage: A.find_g_vector((-2, 3), depth=3)
            [0, 1, 0]
            sage: A.find_g_vector((1, 1), depth=3)
            sage: A.find_g_vector((1, 1), depth=4)
            Traceback (most recent call last):
            ...
            ValueError: (1, 1) is not the g-vector of any cluster variable of a
             Cluster Algebra with cluster variables x0, x1 and coefficients y0, y1
             over Integer Ring
        """
    def ambient(self):
        """
        Return the Laurent polynomial ring containing ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.ambient()
            Multivariate Laurent Polynomial Ring in x0, x1, y0, y1 over Integer Ring
        """
    def scalars(self):
        """
        Return the ring of scalars over which ``self`` is defined.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.scalars()
            Integer Ring
        """
    def lift(self, x):
        """
        Return ``x`` as an element of :meth:`ambient`.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: x = A.cluster_variable((1, 0))
            sage: A.lift(x).parent()
            Multivariate Laurent Polynomial Ring in x0, x1, y0, y1 over Integer Ring
        """
    def retract(self, x):
        """
        Return ``x`` as an element of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: L = A.ambient()
            sage: x = L.gen(0)
            sage: A.retract(x).parent()
            A Cluster Algebra with cluster variables x0, x1 and coefficients y0, y1 over Integer Ring
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the list of initial cluster variables and coefficients of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.gens()
            (x0, x1, y0, y1)
            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True, coefficient_prefix='x')
            sage: A.gens()
            (x0, x1, x2, x3)
        """
    def coefficient(self, j):
        """
        Return the ``j``-th coefficient of ``self``.

        INPUT:

        - ``j`` -- integer in ``range(self.parent().rank())``;
          the index of the coefficient to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.coefficient(0)
            y0
        """
    @cached_method
    def coefficients(self) -> tuple:
        """
        Return the list of coefficients of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.coefficients()
            (y0, y1)
            sage: A1 = ClusterAlgebra(['B', 2])
            sage: A1.coefficients()
            ()
        """
    def coefficient_names(self) -> tuple:
        """
        Return the list of coefficient names.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 3])
            sage: A.coefficient_names()
            ()
            sage: A1 = ClusterAlgebra(['B', 2], principal_coefficients=True)
            sage: A1.coefficient_names()
            ('y0', 'y1')
            sage: A2 = ClusterAlgebra(['C', 3], principal_coefficients=True, coefficient_prefix='x')
            sage: A2.coefficient_names()
            ('x3', 'x4', 'x5')
        """
    def initial_cluster_variable(self, j):
        """
        Return the ``j``-th initial cluster variable of ``self``.

        INPUT:

        - ``j`` -- integer in ``range(self.parent().rank())``;
          the index of the cluster variable to return

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.initial_cluster_variable(0)
            x0
        """
    @cached_method
    def initial_cluster_variables(self) -> tuple:
        """
        Return the list of initial cluster variables of ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.initial_cluster_variables()
            (x0, x1)
        """
    def initial_cluster_variable_names(self) -> tuple:
        """
        Return the list of initial cluster variable names.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2], principal_coefficients=True)
            sage: A.initial_cluster_variable_names()
            ('x0', 'x1')
            sage: A1 = ClusterAlgebra(['B', 2], cluster_variable_prefix='a')
            sage: A1.initial_cluster_variable_names()
            ('a0', 'a1')
        """
    def seeds(self, **kwargs) -> Generator[Incomplete]:
        """
        Return an iterator running over seeds of ``self``.

        INPUT:

        - ``from_current_seed`` -- boolean (default: ``False``); whether to start
          the iterator from :meth:`current_seed` or :meth:`initial_seed`

        - ``mutating_F`` -- boolean (default: ``True``); whether to compute
          F-polynomials also; disable this for speed considerations

        - ``allowed_directions`` -- iterable of integers
          (default: ``range(self.rank())``); the directions in which to mutate

        - ``depth`` -- positive integer or infinity (default: ``infinity``);
          the maximum depth at which to stop searching

        - ``catch_KeyboardInterrupt`` -- boolean (default: ``False``); whether to
          catch ``KeyboardInterrupt`` and return it rather then raising an
          exception -- this allows the iterator returned by this method to be
          resumed after being interrupted

        ALGORITHM:

        This function traverses the exchange graph in a breadth-first search.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 4])
            sage: A.clear_computed_data()
            sage: seeds = A.seeds(allowed_directions=[3, 0, 1])
            sage: _ = list(seeds)
            sage: sorted(A.g_vectors_so_far())
            [(-1, 0, 0, 0),
             (-1, 1, 0, 0),
             (0, -1, 0, 0),
             (0, 0, 0, -1),
             (0, 0, 0, 1),
             (0, 0, 1, 0),
             (0, 1, 0, 0),
             (1, 0, 0, 0)]
        """
    def reset_exploring_iterator(self, mutating_F: bool = True) -> None:
        """
        Reset the iterator used to explore ``self``.

        INPUT:

        - ``mutating_F`` -- boolean (default: ``True``); whether to also compute
          F-polynomials; disable this for speed considerations

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 4])
            sage: A.clear_computed_data()
            sage: A.reset_exploring_iterator(mutating_F=False)
            sage: A.explore_to_depth(infinity)
            sage: len(A.g_vectors_so_far())
            14
            sage: len(A.F_polynomials_so_far())
            4
        """
    def explore_to_depth(self, depth) -> None:
        """
        Explore the exchange graph of ``self`` up to distance ``depth``
        from the initial seed.

        INPUT:

        - ``depth`` -- positive integer or infinity; the maximum depth
          at which to stop searching

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 4])
            sage: A.explore_to_depth(infinity)
            sage: len(A.g_vectors_so_far())
            14
        """
    def cluster_fan(self, depth=...):
        """
        Return the cluster fan (the fan of g-vectors) of ``self``.

        INPUT:

        - ``depth`` -- positive integer or infinity (default: ``infinity``);
          the maximum depth at which to compute

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', 2])
            sage: A.cluster_fan()                                                       # needs sage.geometry.polyhedron
            Rational polyhedral fan in 2-d lattice N
        """
    def mutate_initial(self, direction, **kwargs):
        '''
        Return the cluster algebra obtained by mutating ``self`` at
        the initial seed.

        .. WARNING::

            This method is significantly slower than :meth:`ClusterAlgebraSeed.mutate`.
            It is therefore advisable to use the latter for exploration purposes.

        INPUT:

        - ``direction`` -- in which direction(s) to mutate, it can be:

          * an integer in ``range(self.rank())`` to mutate in one direction only
          * an iterable of such integers to mutate along a sequence
          * a string "sinks" or "sources" to mutate at all sinks or sources simultaneously

        - ``mutating_F`` -- boolean (default: ``True``); whether to compute
          F-polynomials while mutating

        .. NOTE::

            While knowing F-polynomials is essential to computing
            cluster variables, the process of mutating them is quite slow.
            If you care only about combinatorial data like g-vectors and
            c-vectors, setting ``mutating_F=False`` yields significant
            benefits in terms of speed.

        ALGORITHM:

        This function computes data for the new algebra from known data for
        the old algebra using Equation (4.2) from [NZ2012]_ for g-vectors, and
        Equation (6.21) from [FZ2007]_ for F-polynomials. The exponent `h`
        in the formula for F-polynomials is ``-min(0, old_g_vect[k])``
        due to [NZ2012]_ Proposition 4.2.

        EXAMPLES::

            sage: A = ClusterAlgebra([\'F\', 4])
            sage: A.explore_to_depth(infinity)
            sage: B = A.b_matrix()
            sage: B.mutate(0)
            sage: A1 = ClusterAlgebra(B)
            sage: A1.explore_to_depth(infinity)
            sage: A2 = A1.mutate_initial(0)
            sage: A2._F_poly_dict == A._F_poly_dict
            True

        Check that we did not mess up the original algebra because of :class:`UniqueRepresentation`::

            sage: A = ClusterAlgebra([\'A\',2])
            sage: A.mutate_initial(0) is A
            False

        A faster example without recomputing F-polynomials::

            sage: A = ClusterAlgebra(matrix([[0,5],[-5,0]]))
            sage: A.mutate_initial([0,1]*10, mutating_F=False)
            A Cluster Algebra with cluster variables x20, x21 and no coefficients over Integer Ring

        Check that :issue:`28176` is fixed::

            sage: A = ClusterAlgebra( matrix(5,[0,1,-1,1,-1]), cluster_variable_names=[\'p13\'], coefficient_names=[\'p12\',\'p23\',\'p34\',\'p41\']); A
            A Cluster Algebra with cluster variable p13 and coefficients p12, p23, p34, p41 over Integer Ring
            sage: A.mutate_initial(0)
            A Cluster Algebra with cluster variable x0 and coefficients p12, p23, p34, p41 over Integer Ring

            sage: A1 = ClusterAlgebra([\'A\',[2,1],1])
            sage: A2 = A1.mutate_initial([0,1,0])
            sage: len(A2.g_vectors_so_far()) == len(A2.F_polynomials_so_far())
            True
            sage: all(parent(f) == A2._U for f in A2.F_polynomials_so_far())
            True
            sage: A2.find_g_vector((0,0,1)) == []
            True
        '''
    def greedy_element(self, d_vector):
        """
        Return the greedy element with denominator vector ``d_vector``.

        INPUT:

        - ``d_vector`` -- tuple of 2 integers; the denominator vector of
          the element to compute

        ALGORITHM:

        This implements greedy elements of a rank 2 cluster algebra using
        Equation (1.5) from [LLZ2014]_.

        EXAMPLES::

            sage: A = ClusterAlgebra(['A', [1, 1], 1])
            sage: A.greedy_element((1, 1))
            (x0^2 + x1^2 + 1)/(x0*x1)
        """
    def theta_basis_element(self, g_vector):
        """
        Return the element of the theta basis of ``self`` with g-vector ``g_vector``.

        INPUT:

        - ``g_vector`` -- tuple; the g-vector of the element to compute

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,-3],[2,0]]), principal_coefficients=True)
            sage: A.theta_basis_element((-1,-1))
            (x1^8*y0^4*y1 + 4*x1^6*y0^3*y1 + 6*x1^4*y0^2*y1 + x0^3*x1^2*y0 + 4*x1^2*y0*y1 + x0^3 + y1)/(x0^4*x1)

            sage: A = ClusterAlgebra(['F', 4])
            sage: A.theta_basis_element((1, 0, 0, 0))
            Traceback (most recent call last):
            ...
            NotImplementedError: currently only implemented for cluster algebras of rank 2

        .. NOTE::

            Elements of the theta basis correspond with the associated cluster
            monomial only for appropriate coefficient choices. For example::

                sage: A = ClusterAlgebra(matrix([[0,-1],[1,0],[-1,0]]))
                sage: A.theta_basis_element((-1,0))
                (x1 + y0)/(x0*y0)

            while::

                sage: _ = A.find_g_vector((-1,0));
                sage: A.cluster_variable((-1,0))
                (x1 + y0)/x0

            In particular theta basis elements do not satisfy a separation of additions formula.

        .. WARNING::

            Currently only cluster algebras of rank 2 are supported

        .. SEEALSO::

            :meth:`sage.algebras.cluster_algebra.theta_basis_F_polynomial`
        """
    def theta_basis_F_polynomial(self, g_vector):
        """
        Return the F-polynomial of the element of the theta basis of ``self`` with g-vector ``g_vector``.

        INPUT:

        - ``g_vector`` -- tuple; the g-vector of the F-polynomial to compute

        .. WARNING::

            Elements of the theta basis do not satisfy a separation of additions formula.
            See the implementation of :meth:`sage.algebras.cluster_algebra.theta_basis_F_polynomial`
            for further details.

        ALGORITHM:

        This method uses the fact that the greedy basis and the theta basis
        coincide in rank 2 and uses the former defining recursion (Equation
        (1.5) from [LLZ2014]_) to compute.

        EXAMPLES::

            sage: A = ClusterAlgebra(matrix([[0,-3],[2,0]]), principal_coefficients=True)
            sage: A.theta_basis_F_polynomial((-1,-1))
            u0^4*u1 + 4*u0^3*u1 + 6*u0^2*u1 + 4*u0*u1 + u0 + u1 + 1

            sage: A = ClusterAlgebra(['F', 4])
            sage: A.theta_basis_F_polynomial((1, 0, 0, 0))
            Traceback (most recent call last):
            ...
            NotImplementedError: currently only implemented for cluster algebras of rank 2
        """
    def upper_cluster_algebra(self) -> None:
        """
        Return the upper cluster algebra associated to ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['F', 4])
            sage: A.upper_cluster_algebra()
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented yet
        """
    def upper_bound(self) -> None:
        """
        Return the upper bound associated to ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['F', 4])
            sage: A.upper_bound()
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented yet
        """
    def lower_bound(self) -> None:
        """
        Return the lower bound associated to ``self``.

        EXAMPLES::

            sage: A = ClusterAlgebra(['F', 4])
            sage: A.lower_bound()
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented yet
        """
