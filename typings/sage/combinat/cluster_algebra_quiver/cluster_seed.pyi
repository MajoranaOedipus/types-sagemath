from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.cluster_algebra_quiver.interact import cluster_interact as cluster_interact
from sage.combinat.cluster_algebra_quiver.mutation_type import is_mutation_finite as is_mutation_finite
from sage.combinat.cluster_algebra_quiver.quiver import ClusterQuiver as ClusterQuiver
from sage.combinat.cluster_algebra_quiver.quiver_mutation_type import QuiverMutationType_Irreducible as QuiverMutationType_Irreducible, QuiverMutationType_Reducible as QuiverMutationType_Reducible
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import identity_matrix as identity_matrix
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.sage_object import SageObject as SageObject

class ClusterSeed(SageObject):
    """
    The *cluster seed* associated to an *exchange matrix*.

    INPUT:

    - ``data`` -- can be any of the following::

      * :class:`QuiverMutationType`

      * :class:`str` -- string representing a :class:`QuiverMutationType`
        or a common quiver type (see Examples)

      * :class:`ClusterQuiver`

      * :class:`Matrix` -- a skew-symmetrizable matrix

      * :class:`DiGraph` -- must be the input data for a quiver

      * List of edges -- must be the edge list of a digraph for a quiver

    EXAMPLES::

        sage: S = ClusterSeed(['A',5]); S
        A seed for a cluster algebra of rank 5 of type ['A', 5]

        sage: S = ClusterSeed(['A',[2,5],1]); S
        A seed for a cluster algebra of rank 7 of type ['A', [2, 5], 1]

        sage: T = ClusterSeed(S); T
        A seed for a cluster algebra of rank 7 of type ['A', [2, 5], 1]

        sage: T = ClusterSeed(S._M); T
        A seed for a cluster algebra of rank 7

        sage: T = ClusterSeed(S.quiver()._digraph); T
        A seed for a cluster algebra of rank 7

        sage: T = ClusterSeed(S.quiver()._digraph.edges(sort=True)); T
        A seed for a cluster algebra of rank 7

        sage: S = ClusterSeed(['B',2]); S
        A seed for a cluster algebra of rank 2 of type ['B', 2]

        sage: S = ClusterSeed(['C',2]); S
        A seed for a cluster algebra of rank 2 of type ['B', 2]

        sage: S = ClusterSeed(['A', [5,0],1]); S
        A seed for a cluster algebra of rank 5 of type ['D', 5]

        sage: S = ClusterSeed(['GR',[3,7]]); S
        A seed for a cluster algebra of rank 6 of type ['E', 6]

        sage: S = ClusterSeed(['F', 4, [2,1]]); S
        A seed for a cluster algebra of rank 6 of type ['F', 4, [1, 2]]

        sage: S = ClusterSeed(['A',4]); S._use_fpolys
        True
        sage: S._use_d_vec
        True
        sage: S._use_g_vec
        True
        sage: S._use_c_vec
        True

        sage: S = ClusterSeed(['A', 4]); S.use_fpolys(False); S._use_fpolys
        False

        sage: S = ClusterSeed(DiGraph([['a', 'b'], ['c', 'b'], ['c', 'd'], ['e', 'd']]),
        ....:                 frozen=['c']); S
        A seed for a cluster algebra of rank 4 with 1 frozen variable

        sage: S = ClusterSeed(['D', 4], user_labels=[-1, 0, 1, 2]); S
        A seed for a cluster algebra of rank 4 of type ['D', 4]
    """
    def __init__(self, data, frozen=None, is_principal: bool = False, user_labels=None, user_labels_prefix: str = 'x') -> None:
        """
        Initialize the ClusterSeed ``self`` with the following range of possible attributes:

        * self._n - the number of mutable elements of the cluster seed.
        * self._m - the number of immutable elements of the cluster seed.
        * self._nlist - a list of mutable elements of the cluster seed.
        * self._mlist - a list of immutable elements of the cluster seed.
        * self._M - the 'n + m' x 'n' exchange matrix associated to the cluster seed.
        * self._B - the mutable part of self._M.
        * self._b_initial - the initial exchange matrix
        * self._description - the description of the ClusterSeed
        * self._use_fpolys - a boolean tracking whether F-polynomials and cluster
          variables will be tracked as part of every mutation.
        * self._cluster - a list tracking the current names of cluster elements.
        * self._user_labels_prefix - the prefix for every named cluster element.
          Defaults to 'x'.
        * self._user_labels - an optional dictionary or list of user
          defined names for all cluster elements. Defaults to ``'x_i'``
          for mutable elements and ``'y_i'`` for immutable elements.
          All labels should be integers or alphanumeric strings.
        * self._init_vars - an internal list for defining ambient
          the algebraic setting and naming quiver vertices.
        * self._init_exch - the dictionary storing the initial
          mutable cluster variable names.
        * self._U - the coefficient tuple of the initial cluster seed.
        * self._F - the dictionary of F-polynomials.
        * self._R - the ambient polynomial ring.
        * self._y - the coefficient tuple for the current cluster seed.
        * self._yhat - the mixed coefficient tuple appearing in
          Proposition 3.9 of [FZ2007]
        * self._use_g_vec - a boolean stating if g-vectors for the cluster seed
          are being tracked. User input overridden as needed.
        * self._G - the matrix containing all g-vectors.
        * self._use_d_vec - a boolean stating if d-vectors for the cluster seed
          are being tracked.
        * self._D - the matrix containing all d-vectors.
        * self._bot_is_c - a boolean stating if the c-vectors are stored
          on the bottom of the exchange matrix M.
        * self._use_c_vec - a boolean stating if c-vectors for the cluster seed
          are being tracked. User input overridden as needed.
        * self._C - the matrix containing all c-vectors.
        * self._BC - an extended matrix involving the B and C matrices used
          for simplifying mutation calculations.
        * self._is_principal - a boolean tracking whether the ClusterSeed
          contains immutable elements coming from a principal extension
          of the mutable vertices. To be deprecated in future versions.

        * self._quiver - the ClusterQuiver corresponding to the
          exchange matrix ``self._M``.
        * self._mutation_type - the mutation type of self._quiver .

        * self._track_mut - a boolean tracking whether the ClusterSeed's
          mutation path is being recorded.
        * self._mut_path - the list of integers recording the mutation path of
          a seed - with consecutive repeats deleted since mutations
          is an involution.

        TESTS::

            sage: S = ClusterSeed(['A',4])
            sage: TestSuite(S).run()
        """
    def use_c_vectors(self, use: bool = True, bot_is_c: bool = False, force: bool = False) -> None:
        """
        Reconstruct `c`-vectors from other data or initialize if no usable data
        exists.

        Warning: Initialization may lead to inconsistent data.

        INPUT:

        - ``use`` -- boolean (default: ``True``); if ``True``, will use
          `c`-vectors
        - ``bot_is_c`` -- boolean (default: ``False``); if ``True`` and
          :class:`ClusterSeed` ``self`` has ``self._m == self._n``, then will
          assume bottom half of the extended exchange matrix is the c-matrix.
          If ``True``, lets the :class:`ClusterSeed` know c-vectors can be
          calculated.

        EXAMPLES::

            sage: S = ClusterSeed(['A',4])
            sage: S.use_c_vectors(False); S.use_g_vectors(False)
            sage: S.use_fpolys(False); S.track_mutations(False)
            sage: S.use_c_vectors(True)
            Warning: Initializing c-vectors at this point
            could lead to inconsistent seed data.

            sage: S.use_c_vectors(True, force=True)
            sage: S.c_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

            sage: S = ClusterSeed(['A',4])
            sage: S.use_c_vectors(False); S.use_g_vectors(False)
            sage: S.use_fpolys(False); S.track_mutations(False)
            sage: S.mutate(1)
            sage: S.use_c_vectors(True, force=True)
            sage: S.c_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
        """
    def use_g_vectors(self, use: bool = True, force: bool = False) -> None:
        """
        Reconstruct g-vectors from other data or initialize if no usable data
        exists.

        .. warning::

            Initialization may lead to inconsistent data.

        INPUT:

        - ``use`` -- boolean (default: ``True``); if ``True``, will use
          g-vectors

        EXAMPLES::

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_fpolys(False)
            sage: S.use_g_vectors(True)
            sage: S.g_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_fpolys(False)
            sage: S.mutate(1)
            sage: S.use_g_vectors(True)
            sage: S.g_matrix()
            [ 1  0  0  0]
            [ 0 -1  0  0]
            [ 0  0  1  0]
            [ 0  0  0  1]

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_fpolys(False); S.track_mutations(False)
            sage: S.mutate(1)
            sage: S.use_c_vectors(False)
            sage: S.g_matrix()
            Traceback (most recent call last):
            ...
            ValueError: Unable to calculate g-vectors. Need to use g vectors.

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_fpolys(False); S.track_mutations(False)
            sage: S.mutate(1)
            sage: S.use_c_vectors(False)
            sage: S.use_g_vectors(True)
            Warning: Initializing g-vectors at this point
            could lead to inconsistent seed data.

            sage: S.use_g_vectors(True, force=True)
            sage: S.g_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
        """
    def use_d_vectors(self, use: bool = True, force: bool = False) -> None:
        """
        Reconstruct `d`-vectors from other data or initialize if no usable data
        exists.

        .. warning::

            Initialization may lead to inconsistent data.

        INPUT:

        - ``use`` -- boolean (default: ``True``); if ``True``, will use
          `d`-vectors

        EXAMPLES::

            sage: S = ClusterSeed(['A',4])
            sage: S.use_d_vectors(True)
            sage: S.d_matrix()
            [-1  0  0  0]
            [ 0 -1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]

            sage: S = ClusterSeed(['A',4]); S.use_d_vectors(False)
            sage: S.track_mutations(False); S.mutate(1); S.d_matrix()
            [-1  0  0  0]
            [ 0  1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]
            sage: S.use_fpolys(False)
            sage: S.d_matrix()
            Traceback (most recent call last):
            ...
            ValueError: Unable to calculate d-vectors. Need to use d vectors.

            sage: S = ClusterSeed(['A',4]); S.use_d_vectors(False)
            sage: S.track_mutations(False); S.mutate(1); S.d_matrix()
            [-1  0  0  0]
            [ 0  1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]
            sage: S.use_fpolys(False)
            sage: S.use_d_vectors(True)
            Warning: Initializing d-vectors at this point
            could lead to inconsistent seed data.

            sage: S.use_d_vectors(True, force=True)
            sage: S.d_matrix()
            [-1  0  0  0]
            [ 0 -1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]

            sage: S = ClusterSeed(['A',4]); S.mutate(1); S.d_matrix()
            [-1  0  0  0]
            [ 0  1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]
            sage: S = ClusterSeed(['A',4])
            sage: S.use_d_vectors(True); S.mutate(1); S.d_matrix()
            [-1  0  0  0]
            [ 0  1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]
        """
    def use_fpolys(self, use: bool = True, user_labels=None, user_labels_prefix=None) -> None:
        """
        Use `F`-polynomials in our Cluster Seed.

        Note: This will automatically try to recompute the cluster variables
        if possible

        INPUT:

        - ``use`` -- boolean (default: ``True``); if ``True``, will use
          `F`-polynomials
        - ``user_labels`` -- (default: ``None``) if set, will overwrite the
          default cluster variable ``labels``
        - ``user_labels_prefix`` -- (default: ``None``) if set, will overwrite
          the default

        EXAMPLES::

            sage: S = ClusterSeed(['A',4]); S.use_fpolys(False); S._cluster
            sage: S.use_fpolys(True)
            sage: S.cluster()
            [x0, x1, x2, x3]

            sage: S = ClusterSeed(['A',4]); S.use_fpolys(False); S.track_mutations(False)
            sage: S.mutate(1)
            sage: S.use_fpolys(True)
            Traceback (most recent call last):
            ...
            ValueError: F-polynomials and Cluster Variables cannot be reconstructed
            from given data.
            sage: S.cluster()
            Traceback (most recent call last):
            ...
            ValueError: Clusters not being tracked
        """
    def track_mutations(self, use: bool = True) -> None:
        """
        Begin tracking the mutation path.

        .. warning::

            May initialize all other data to ensure that all
            c-, d-, and g-vectors agree on the start of mutations.

        INPUT:

        - ``use`` -- boolean (default: ``True``); if ``True``, will begin
          filling the mutation path

        EXAMPLES::

            sage: S = ClusterSeed(['A',4]); S.track_mutations(False)
            sage: S.mutate(0)
            sage: S.mutations()
            Traceback (most recent call last):
            ...
            ValueError: Not recording mutation sequence.  Need to track mutations.
            sage: S.track_mutations(True)
            sage: S.g_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

            sage: S.mutate([0,1])
            sage: S.mutations()
            [0, 1]
        """
    def set_c_matrix(self, data) -> None:
        """
        Will force set the c-matrix according to a matrix, a quiver, or a seed.

        INPUT:

        - ``data`` -- the matrix to set the c-matrix to; also allowed
          to be a quiver or cluster seed, in which case the b-matrix
          is used

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: X = matrix([[0,0,1],[0,1,0],[1,0,0]])
            sage: S.set_c_matrix(X)
            sage: S.c_matrix()
            [0 0 1]
            [0 1 0]
            [1 0 0]

            sage: Y = matrix([[-1,0,1],[0,1,0],[1,0,0]])
            sage: S.set_c_matrix(Y)
            C matrix does not look to be valid - there exists a column
            containing positive and negative entries.
            Continuing...

            sage: Z = matrix([[1,0,1],[0,1,0],[2,0,2]])
            sage: S.set_c_matrix(Z)
            C matrix does not look to be valid - not a linearly independent set.
            Continuing...
        """
    def __eq__(self, other):
        """
        Return ``True`` iff ``self`` represent the same cluster seed as ``other`` and all tracked data agrees.

        EXAMPLES::

            sage: S = ClusterSeed(['A',5])
            sage: T = S.mutate(2, inplace=False)
            sage: S.__eq__(T)
            False

            sage: T.mutate(2)
            sage: S.__eq__(T)
            True

            sage: S = ClusterSeed(['A',2])
            sage: T = ClusterSeed(S)
            sage: S.__eq__(T)
            True

            sage: S.mutate([0,1,0,1,0])
            sage: S.__eq__(T)
            False
            sage: S.cluster()
            [x1, x0]
            sage: T.cluster()
            [x0, x1]

            sage: S.mutate([0,1,0,1,0])
            sage: S.__eq__(T)
            True
            sage: S.cluster()
            [x0, x1]
        """
    def __hash__(self):
        """
        Return a hash of ``self``.

        EXAMPLES::

            sage: Q1 = ClusterSeed(['A',5])
            sage: Q2 = ClusterSeed(ClusterQuiver(['A',5]))
            sage: hash(Q1) == hash(Q2)
            True
            sage: hash(Q1) == hash('something')
            False
        """
    def plot(self, circular: bool = False, mark=None, save_pos: bool = False, force_c: bool = False, with_greens: bool = False, add_labels: bool = False):
        """
        Return the plot of the quiver of ``self``.

        INPUT:

        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used
        - ``mark`` -- (default: ``None``) if set to i, the vertex i is
          highlighted
        - ``save_pos`` -- boolean (default: ``False``); if ``True``, the
          positions of the vertices are saved
        - ``force_c`` -- boolean (default: ``False``); if ``True``, will show
          the frozen vertices even if they were never initialized
        - ``with_greens`` -- boolean (default: ``False``); if ``True``, will
          display the green vertices in green
        - ``add_labels`` -- boolean (default: ``False``); if ``True``, will use
          the initial variables as labels

        EXAMPLES::

            sage: S = ClusterSeed(['A',5])
            sage: S.plot()                                                              # needs sage.plot sage.symbolic
            Graphics object consisting of 15 graphics primitives
            sage: S.plot(circular=True)                                                 # needs sage.plot sage.symbolic
            Graphics object consisting of 15 graphics primitives
            sage: S.plot(circular=True, mark=1)                                         # needs sage.plot sage.symbolic
            Graphics object consisting of 15 graphics primitives
        """
    def show(self, fig_size: int = 1, circular: bool = False, mark=None, save_pos: bool = False, force_c: bool = False, with_greens: bool = False, add_labels: bool = False) -> None:
        """
        Shows the plot of the quiver of ``self``.

        INPUT:

        - ``fig_size`` -- (default: 1) factor by which the size of the plot
          is multiplied
        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used
        - ``mark`` -- (default: ``None``) if set to i, the vertex i is
          highlighted
        - ``save_pos`` -- boolean (default: ``False``); if ``True``, the
          positions of the vertices are saved
        - ``force_c`` -- boolean (default: ``False``); if ``True``, will show
          the frozen vertices even if they were never initialized
        - ``with_greens`` -- boolean (default: ``False``); if ``True``, will
          display the green vertices in green
        - ``add_labels`` -- boolean (default: ``False``); if ``True``, will use
          the initial variables as labels

        TESTS::

            sage: S = ClusterSeed(['A',5])
            sage: S.show()                      # long time                             # needs sage.plot sage.symbolic
        """
    def interact(self, fig_size: int = 1, circular: bool = True):
        """
        Start an interactive window for cluster seed mutations.

        Only in *Jupyter notebook mode*.

        INPUT:

        - ``fig_size`` -- (default: 1) factor by which the size of the
          plot is multiplied

        - ``circular`` -- boolean (default: ``True``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used

        TESTS::

            sage: S = ClusterSeed(['A',4])
            sage: S.interact()                                                          # needs sage.plot sage.symbolic
            ...VBox(children=...
        """
    def save_image(self, filename, circular: bool = False, mark=None, save_pos: bool = False) -> None:
        """
        Save the plot of the underlying digraph of the quiver of ``self``.

        INPUT:

        - ``filename`` -- the filename the image is saved to
        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used
        - ``mark`` -- (default: ``None``) if set to i, the vertex i is
          highlighted
        - ``save_pos`` -- boolean (default: ``False``); if ``True``, the
          positions of the vertices are saved

        EXAMPLES::

            sage: S = ClusterSeed(['F',4,[1,2]])
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.png') as f:                 # needs sage.plot sage.symbolic
            ....:     S.save_image(f.name)
        """
    def b_matrix(self):
        """
        Return the `B` *-matrix* of ``self``.

        EXAMPLES::

            sage: ClusterSeed(['A',4]).b_matrix()
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -1  0]

            sage: ClusterSeed(['B',4]).b_matrix()
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -2  0]

            sage: ClusterSeed(['D',4]).b_matrix()
            [ 0  1  0  0]
            [-1  0 -1 -1]
            [ 0  1  0  0]
            [ 0  1  0  0]

            sage: ClusterSeed(QuiverMutationType([['A',2],['B',2]])).b_matrix()
            [ 0  1  0  0]
            [-1  0  0  0]
            [ 0  0  0  1]
            [ 0  0 -2  0]
        """
    def ground_field(self):
        """
        Return the *ground field* of the cluster of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.ground_field()
            Multivariate Polynomial Ring in x0, x1, x2, y0, y1, y2 over Rational Field
        """
    def x(self, k):
        """
        Return the `k` *-th initial cluster variable* for the associated cluster seed,
        or the cluster variable of the corresponding vertex in ``self.quiver``.

        EXAMPLES::

            sage: S = ClusterSeed(['A', 3])
            sage: S.mutate([2, 1])
            sage: S.x(0)
            x0

            sage: S.x(1)
            x1

            sage: S.x(2)
            x2

            sage: dg = DiGraph([['a', 'b'], ['b', 'c']], format='list_of_edges')
            sage: S = ClusterSeed(dg, frozen=['c'])
            sage: S.x(0)
            a
            sage: S.x('a')
            a
        """
    def y(self, k):
        """
        Return the `k` *-th initial coefficient (frozen variable)* for the
        associated cluster seed, or the cluster variable of the corresponding
        vertex in ``self.quiver``.

        EXAMPLES::

            sage: S = ClusterSeed(['A', 3]).principal_extension()
            sage: S.mutate([2, 1])
            sage: S.y(0)
            y0

            sage: S.y(1)
            y1

            sage: S.y(2)
            y2

            sage: dg = DiGraph([['a', 'b'], ['b', 'c']], format='list_of_edges')
            sage: S = ClusterSeed(dg, frozen=['c'])
            sage: S.y(0)
            c
            sage: S.y('c')
            c
        """
    def n(self):
        """
        Return the number of *exchangeable variables* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A', 3])
            sage: S.n()
            3
        """
    def m(self):
        """
        Return the number of *frozen variables* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.n()
            3

            sage: S.m()
            0

            sage: S = S.principal_extension()
            sage: S.m()
            3
        """
    def free_vertices(self):
        """
        Return the list of *exchangeable vertices* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(DiGraph([['a', 'b'], ['c', 'b'], ['c', 'd'], ['e', 'd']]),
            ....:                         frozen=['b', 'd'])
            sage: S.free_vertices()
            ['a', 'c', 'e']

            sage: S = ClusterSeed(DiGraph([[5, 'b']]))
            sage: S.free_vertices()
            [5, 'b']
        """
    def frozen_vertices(self):
        """
        Return the list of *frozen vertices* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(DiGraph([['a', 'b'], ['c', 'b'], ['c', 'd'], ['e', 'd']]),
            ....:                         frozen=['b', 'd'])
            sage: sorted(S.frozen_vertices())
            ['b', 'd']
        """
    def mutations(self):
        """
        Return the list of mutations ``self`` has undergone if they are being tracked.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.mutations()
            []

            sage: S.mutate([0,1,0,2])
            sage: S.mutations()
            [0, 1, 0, 2]

            sage: S.track_mutations(False)
            sage: S.mutations()
            Traceback (most recent call last):
            ...
            ValueError: Not recording mutation sequence.  Need to track mutations.
        """
    def cluster_variable(self, k):
        """
        Generates a cluster variable using F-polynomials.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.mutate([0,1])
            sage: S.cluster_variable(0)
            (x1 + 1)/x0
            sage: S.cluster_variable(1)
            (x0*x2 + x1 + 1)/(x0*x1)
        """
    def cluster(self):
        """
        Return a copy of the *cluster* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.cluster()
            [x0, x1, x2]

            sage: S.mutate(1)
            sage: S.cluster()
            [x0, (x0*x2 + 1)/x1, x2]

            sage: S.mutate(2)
            sage: S.cluster()
            [x0, (x0*x2 + 1)/x1, (x0*x2 + x1 + 1)/(x1*x2)]

            sage: S.mutate([2,1])
            sage: S.cluster()
            [x0, x1, x2]
        """
    def f_polynomial(self, k):
        """
        Return the ``k``-th *F-polynomial* of ``self``. It is obtained from the
        ``k``-th cluster variable by setting all `x_i` to `1`.

        .. warning::

            This method assumes the sign-coherence conjecture and that the
            input seed is sign-coherent (has an exchange matrix with columns of like signs).
            Otherwise, computational errors might arise.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: [S.f_polynomial(k) for k in range(3)]
            [1, y1*y2 + y2 + 1, y1 + 1]

            sage: S = ClusterSeed(Matrix([[0,1],[-1,0],[1,0],[-1,1]]))
            sage: S.use_c_vectors(bot_is_c=True); S
            A seed for a cluster algebra of rank 2 with 2 frozen variables
            sage: T = ClusterSeed(Matrix([[0,1],[-1,0]])).principal_extension(); T
            A seed for a cluster algebra of rank 2 with principal coefficients
            sage: S.mutate(0)
            sage: T.mutate(0)
            sage: S.f_polynomials()
            [y0 + y1, 1]
            sage: T.f_polynomials()
            [y0 + 1, 1]
        """
    def f_polynomials(self):
        """
        Return all *F-polynomials* of ``self``. These are obtained from the
        cluster variables by setting all `x_i`'s to `1`.

        .. warning::

            This method assumes the sign-coherence conjecture and that the
            input seed is sign-coherent (has an exchange matrix with columns of like signs).
            Otherwise, computational errors might arise.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: S.f_polynomials()
            [1, y1*y2 + y2 + 1, y1 + 1]
        """
    def g_vector(self, k):
        """
        Return the ``k``-th *g-vector* of ``self``. This is the degree vector
        of the ``k``-th cluster variable after setting all `y_i`'s to `0`.

        .. warning::

            This method assumes the sign-coherence conjecture and that the
            input seed is sign-coherent (has an exchange matrix with columns of like signs).
            Otherwise, computational errors might arise.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: [S.g_vector(k) for k in range(3)]
            [(1, 0, 0), (0, 0, -1), (0, -1, 0)]
        """
    def g_matrix(self, show_warnings: bool = True):
        """
        Return the matrix of all *g-vectors* of ``self``. These are the degree
        vectors of the cluster variables after setting all `y_i`'s to `0`.

        .. warning::

            This method assumes the sign-coherence conjecture and that the
            input seed is sign-coherent (has an exchange matrix with columns of like signs).
            Otherwise, computational errors might arise.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: S.g_matrix()
            [ 1  0  0]
            [ 0  0 -1]
            [ 0 -1  0]

            sage: S = ClusterSeed(['A',3])
            sage: S.mutate([0,1])
            sage: S.g_matrix()
            [-1 -1  0]
            [ 1  0  0]
            [ 0  0  1]

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_fpolys(False); S.g_matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_c_vectors(False); S.use_fpolys(False)
            sage: S.track_mutations(False); S.g_matrix()
            Traceback (most recent call last):
            ...
            ValueError: Unable to calculate g-vectors. Need to use g vectors.
        """
    def c_vector(self, k):
        """
        Return the ``k``-th *c-vector* of ``self``. It is obtained as the
        ``k``-th column vector of the bottom part of the ``B``-matrix
        of ``self``.

        .. warning::

            This method assumes the sign-coherence conjecture and that the
            input seed is sign-coherent (has an exchange matrix with columns of like signs).
            Otherwise, computational errors might arise.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: [S.c_vector(k) for k in range(3)]
            [(1, 0, 0), (0, 0, -1), (0, -1, 0)]

            sage: S = ClusterSeed(Matrix([[0,1],[-1,0],[1,0],[-1,1]])); S
            A seed for a cluster algebra of rank 2 with 2 frozen variables
            sage: S.c_vector(0)
            (1, 0)

            sage: S = ClusterSeed(Matrix([[0,1],[-1,0],[1,0],[-1,1]]))
            sage: S.use_c_vectors(bot_is_c=True); S
            A seed for a cluster algebra of rank 2 with 2 frozen variables
            sage: S.c_vector(0)
            (1, -1)
        """
    def c_matrix(self, show_warnings: bool = True):
        """
        Return all *c-vectors* of ``self``.

        .. warning::

            This method assumes the sign-coherence conjecture and that the
            input seed is sign-coherent (has an exchange matrix with columns of like signs).
            Otherwise, computational errors might arise.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: S.c_matrix()
            [ 1  0  0]
            [ 0  0 -1]
            [ 0 -1  0]

            sage: S = ClusterSeed(['A',4])
            sage: S.use_g_vectors(False); S.use_fpolys(False)
            sage: S.use_c_vectors(False); S.use_d_vectors(False); S.track_mutations(False)
            sage: S.c_matrix()
            Traceback (most recent call last):
            ...
            ValueError: Unable to calculate c-vectors. Need to use c vectors.
        """
    def d_vector(self, k):
        """
        Return the ``k``-th *d-vector* of ``self``. This is the exponent vector
        of the denominator of the ``k``-th cluster variable.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.mutate([2,1,2])
            sage: [S.d_vector(k) for k in range(3)]
            [(-1, 0, 0), (0, 1, 1), (0, 1, 0)]
        """
    def d_matrix(self, show_warnings: bool = True):
        """
        Return the matrix of *d-vectors* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',4]); S.d_matrix()
            [-1  0  0  0]
            [ 0 -1  0  0]
            [ 0  0 -1  0]
            [ 0  0  0 -1]
            sage: S.mutate([1,2,1,0,1,3]); S.d_matrix()
            [1 1 0 1]
            [1 1 1 1]
            [1 0 1 1]
            [0 0 0 1]
        """
    def coefficient(self, k):
        """
        Return the *coefficient* of ``self`` at index ``k``,
        or vertex ``k`` if ``k`` is not an index.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: [S.coefficient(k) for k in range(3)]
            [y0, 1/y2, 1/y1]
        """
    def coefficients(self):
        """
        Return all *coefficients* of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutate([2,1,2])
            sage: S.coefficients()
            [y0, 1/y2, 1/y1]
        """
    def quiver(self):
        """
        Return the *quiver* associated to ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.quiver()
            Quiver on 3 vertices of type ['A', 3]
        """
    def is_acyclic(self) -> bool:
        """
        Return ``True`` iff ``self`` is acyclic (i.e., if the underlying quiver is acyclic).

        EXAMPLES::

            sage: ClusterSeed(['A',4]).is_acyclic()
            True

            sage: ClusterSeed(['A',[2,1],1]).is_acyclic()
            True

            sage: ClusterSeed([[0,1],[1,2],[2,0]]).is_acyclic()
            False
        """
    def is_bipartite(self, return_bipartition: bool = False):
        """
        Return ``True`` iff ``self`` is bipartite (i.e., if the underlying
        quiver is bipartite).

        INPUT:

        - ``return_bipartition`` -- boolean (default: ``False``); if ``True``,
          the bipartition is returned in the case of ``self`` being bipartite

        EXAMPLES::

            sage: ClusterSeed(['A',[3,3],1]).is_bipartite()
            True

            sage: ClusterSeed(['A',[4,3],1]).is_bipartite()
            False
        """
    def green_vertices(self):
        """
        Return the list of green vertices of ``self``.

        A vertex is defined to be green if its c-vector has all nonpositive
        entries. More information on green vertices can be found at [BDP2013]_

        OUTPUT: the green vertices as a list of integers

        EXAMPLES::

            sage: ClusterSeed(['A',3]).principal_extension().green_vertices()
            [0, 1, 2]

            sage: ClusterSeed(['A',[3,3],1]).principal_extension().green_vertices()
            [0, 1, 2, 3, 4, 5]
        """
    def first_green_vertex(self):
        """
        Return the first green vertex of ``self``.

        A vertex is defined to be green if its c-vector has all nonpositive entries.
        More information on green vertices can be found at [BDP2013]_

        EXAMPLES::

            sage: ClusterSeed(['A',3]).principal_extension().first_green_vertex()
            0

            sage: ClusterSeed(['A',[3,3],1]).principal_extension().first_green_vertex()
            0
        """
    def red_vertices(self):
        """
        Return the list of red vertices of ``self``.

        A vertex is defined to be red if its c-vector has all nonnegative entries.
        More information on red vertices can be found at [BDP2013]_.

        OUTPUT: the red vertices as a list of integers

        EXAMPLES::

            sage: ClusterSeed(['A',3]).principal_extension().red_vertices()
            []

            sage: ClusterSeed(['A',[3,3],1]).principal_extension().red_vertices()
            []

            sage: Q = ClusterSeed(['A',[3,3],1]).principal_extension()
            sage: Q.mutate(1)
            sage: Q.red_vertices()
            [1]
        """
    def first_red_vertex(self):
        """
        Return the first red vertex of ``self``.

        A vertex is defined to be red if its c-vector has all nonnegative entries.
        More information on red vertices can be found at [BDP2013]_.

        EXAMPLES::

            sage: ClusterSeed(['A',3]).principal_extension().first_red_vertex()

            sage: ClusterSeed(['A',[3,3],1]).principal_extension().first_red_vertex()

            sage: Q = ClusterSeed(['A',[3,3],1]).principal_extension()
            sage: Q.mutate(1)
            sage: Q.first_red_vertex()
            1
        """
    def urban_renewals(self, return_first: bool = False):
        """
        Return the list of the urban renewal vertices of ``self``.

        An urban renewal vertex is one in which there are two arrows pointing
        toward the vertex and two arrows pointing away.

        INPUT:

        - ``return_first`` -- boolean (default: ``False``); if ``True``, will
          return the first urban renewal

        OUTPUT:

        A list of vertices (as integers)

        EXAMPLES::

            sage: G = ClusterSeed(['GR',[4,9]]); G.urban_renewals()
            [5, 6]
        """
    def first_urban_renewal(self):
        """
        Return the first urban renewal vertex.

        An urban renewal vertex is one in which there are two arrows pointing
        toward the vertex and two arrows pointing away.

        EXAMPLES::

            sage: G = ClusterSeed(['GR',[4,9]]); G.first_urban_renewal()
            5
        """
    def highest_degree_denominator(self, filter=None):
        """
        Return the vertex of the cluster polynomial with highest degree in the denominator.

        INPUT:

        - ``filter`` -- list or iterable

        OUTPUT: integer

        EXAMPLES::

            sage: B = matrix([[0,-1,0,-1,1,1], [1,0,1,0,-1,-1], [0,-1,0,-1,1,1],
            ....:             [1,0,1,0,-1,-1], [-1,1,-1,1,0,0], [-1,1,-1,1,0,0]])
            sage: C = ClusterSeed(B).principal_extension(); C.mutate([0,1,2,4,3,2,5,4,3])
            sage: C.highest_degree_denominator()
            5
        """
    def smallest_c_vector(self):
        """
        Return the vertex with the smallest c-vector.

        OUTPUT: integer

        EXAMPLES::

            sage: B = matrix([[0,2], [-2,0]])
            sage: C = ClusterSeed(B).principal_extension()
            sage: C.mutate(0)
            sage: C.smallest_c_vector()
            0
        """
    def most_decreased_edge_after_mutation(self):
        """
        Return the vertex that will produce the least degrees after mutation.

        EXAMPLES::

            sage: S = ClusterSeed(['A',5])
            sage: S.mutate([0,2,3,1,2,3,1,2,0,2,3])
            sage: S.most_decreased_edge_after_mutation()
            2
        """
    def most_decreased_denominator_after_mutation(self):
        """
        Return the vertex that will produce the most decrease in denominator degrees after mutation.

        EXAMPLES::

            sage: S = ClusterSeed(['A',5])
            sage: S.mutate([0,2,3,1,2,3,1,2,0,2,3])
            sage: S.most_decreased_denominator_after_mutation()
            2
        """
    def mutate(self, sequence, inplace: bool = True, input_type=None):
        """
        Mutate ``self`` at a vertex or a sequence of vertices.

        INPUT:

        - ``sequence`` -- a vertex of ``self``, an iterator of vertices of
          ``self``, a function which takes in the :class:`ClusterSeed`
          and returns a vertex or an iterator of vertices,
          or a string representing a type of vertices to mutate
        - ``inplace`` -- boolean (default: ``True``); if ``False``, the result
          is returned, otherwise ``self`` is modified
        - ``input_type`` -- (default: ``None``) indicates the type of data
          contained in the sequence

        Possible values for vertex types in ``sequence`` are:

        - ``'first_source'`` -- mutates at first found source vertex
        - ``'sources'`` -- mutates at all sources
        - ``'first_sink'`` -- mutates at first sink
        - ``'sinks'`` -- mutates at all sink vertices
        - ``'green'`` -- mutates at the first green vertex
        - ``'red'`` -- mutates at the first red vertex
        - ``'urban_renewal'`` or ``'urban'`` -- mutates at first urban renewal vertex
        - ``'all_urban_renewals'`` or ``'all_urban'`` -- mutates at all
          urban renewal vertices

        For ``input_type``, if no value is given, preference will
        be given to vertex names, then indices, then cluster variables.
        If all input is not of the same type, an error is given.
        Possible values for ``input_type`` are:

        - ``'vertices'`` -- interprets the input sequence as vertices
        - ``'indices'`` -- interprets the input sequence as indices
        - ``'cluster_vars'`` -- interprets the input sequence as cluster variables.
          This must be selected if inputting a sequence of cluster variables.

        EXAMPLES::

            sage: S = ClusterSeed(['A',4]); S.b_matrix()
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -1  0]

            sage: S.mutate(0); S.b_matrix()
            [ 0 -1  0  0]
            [ 1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -1  0]

            sage: T = S.mutate(0, inplace=False); T
            A seed for a cluster algebra of rank 4 of type ['A', 4]

            sage: S.mutate(0)
            sage: S == T
            True

            sage: S.mutate([0,1,0])
            sage: S.b_matrix()
            [ 0 -1  1  0]
            [ 1  0  0  0]
            [-1  0  0  1]
            [ 0  0 -1  0]

            sage: S = ClusterSeed(QuiverMutationType([['A',1],['A',3]]))
            sage: S.b_matrix()
            [ 0  0  0  0]
            [ 0  0  1  0]
            [ 0 -1  0 -1]
            [ 0  0  1  0]

            sage: T = S.mutate(0,inplace=False)
            sage: S == T
            False

            sage: Q = ClusterSeed(['A',3]);Q.b_matrix()
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]

            sage: Q.mutate('first_sink');Q.b_matrix()
            [ 0 -1  0]
            [ 1  0  1]
            [ 0 -1  0]

            sage: def last_vertex(self): return self._n - 1
            sage: Q.mutate(last_vertex); Q.b_matrix()
            [ 0 -1  0]
            [ 1  0 -1]
            [ 0  1  0]

            sage: S = ClusterSeed(['A', 4], user_labels=['a', 'b', 'c', 'd'])
            sage: S.mutate('a'); S.mutate('(b+1)/a')
            sage: S.cluster()
            [a, b, c, d]

            sage: S = ClusterSeed(['A', 4], user_labels=['a', 'b', 'c'])
            Traceback (most recent call last):
            ...
            ValueError: the number of user-defined labels is not
             the number of exchangeable and frozen variables

            sage: S = ClusterSeed(['A', 4], user_labels=['x', 'y', 'w', 'z'])
            sage: S.mutate('x')
            sage: S.cluster()
            [(y + 1)/x, y, w, z]
            sage: S.mutate('(y+1)/x')
            sage: S.cluster()
            [x, y, w, z]
            sage: S.mutate('y')
            sage: S.cluster()
            [x, (x*w + 1)/y, w, z]
            sage: S.mutate('(x*w+1)/y')
            sage: S.cluster()
            [x, y, w, z]

            sage: S = ClusterSeed(['A', 4], user_labels=[[1, 2], [2, 3], [4, 5], [5, 6]])
            sage: S.cluster()
            [x_1_2, x_2_3, x_4_5, x_5_6]
            sage: S.mutate('[1,2]')
            sage: S.cluster()
            [(x_2_3 + 1)/x_1_2, x_2_3, x_4_5, x_5_6]

            sage: S = ClusterSeed(['A', 4], user_labels=[[1, 2], [2, 3], [4, 5], [5, 6]],
            ....:                 user_labels_prefix='P');
            sage: S.cluster()
            [P_1_2, P_2_3, P_4_5, P_5_6]
            sage: S.mutate('[1,2]')
            sage: S.cluster()
            [(P_2_3 + 1)/P_1_2, P_2_3, P_4_5, P_5_6]
            sage: S.mutate('P_4_5')
            sage: S.cluster()
            [(P_2_3 + 1)/P_1_2, P_2_3, (P_2_3*P_5_6 + 1)/P_4_5, P_5_6]

            sage: S = ClusterSeed(['A', 4])
            sage: S.mutate([0, 1, 0, 1, 0, 2, 1])
            sage: T = ClusterSeed(S)
            sage: S.use_fpolys(False)
            sage: S.use_g_vectors(False)
            sage: S.use_c_vectors(False)
            sage: S._C
            sage: S._G
            sage: S._F
            sage: S.g_matrix()
            [ 0 -1  0  0]
            [ 1  1  1  0]
            [ 0  0 -1  0]
            [ 0  0  1  1]
            sage: S.c_matrix()
            [ 1 -1  0  0]
            [ 1  0  0  0]
            [ 1  0 -1  1]
            [ 0  0  0  1]
            sage: S.f_polynomials() == T.f_polynomials()
            True

            sage: S.cluster() == T.cluster()
            True
            sage: S._mut_path
            [0, 1, 0, 1, 0, 2, 1]

            sage: S = ClusterSeed(DiGraph([[1, 2], [2, 'c']]))
            sage: S.mutate(1)
            Input can be ambiguously interpreted as both vertices and indices.
             Mutating at vertices by default.
            sage: S.cluster()
            [(x2 + 1)/x1, x2, c]
            sage: S.mutate(1, input_type='indices')
            sage: S.cluster()
            [(x2 + 1)/x1, (x2*c + x1 + c)/(x1*x2), c]

            sage: S = ClusterSeed(DiGraph([['a', 'b'], ['c', 'b'], ['d', 'b']]))
            sage: S.mutate(['a', 'b', 'a', 'b', 'a'])
            sage: S.cluster()
            [b, a, c, d]
            sage: S.mutate('a')
            Input can be ambiguously interpreted as both vertices and cluster variables.
             Mutating at vertices by default.
            sage: S.cluster()
            [(a*c*d + 1)/b, a, c, d]
            sage: S.mutate('a', input_type='cluster_vars')
            sage: S.cluster()
            [(a*c*d + 1)/b, (a*c*d + b + 1)/(a*b), c, d]
            sage: S.mutate(['(a*c*d + 1)/b', 'd'])
            sage: S.cluster()
            [(b + 1)/a, (a*c*d + b + 1)/(a*b), c, (a*c*d + b^2 + 2*b + 1)/(a*b*d)]

            sage: S = ClusterSeed(DiGraph([[5, 'b']]))
            sage: S.mutate(5)
            sage: S.cluster()
            [(b + 1)/x5, b]
            sage: S.mutate([5])
            sage: S.cluster()
            [x5, b]
            sage: S.mutate(0)
            sage: S.cluster()
            [(b + 1)/x5, b]

            sage: S = ClusterSeed(DiGraph([[1, 2]]))
            sage: S.cluster()
            [x1, x2]
            sage: S.mutate(1)
            Input can be ambiguously interpreted as both vertices and indices.
             Mutating at vertices by default.
            sage: S.cluster()
            [(x2 + 1)/x1, x2]

            sage: S = ClusterSeed(DiGraph([[-1, 0], [0, 1]]))
            sage: S.cluster()
            [xneg1, x0, x1]
            sage: S.mutate(-1);S.cluster()
            [(x0 + 1)/xneg1, x0, x1]
            sage: S.mutate(0, input_type='vertices');S.cluster()
            [(x0 + 1)/xneg1, (x0*x1 + xneg1 + x1)/(xneg1*x0), x1]
        """
    def cluster_index(self, cluster_str):
        """
        Return the index of a cluster if ``use_fpolys`` is on.

        INPUT:

        - ``cluster_str`` -- the string to look for in the cluster

        OUTPUT: integer or ``None`` if the string is not a cluster variable

        EXAMPLES::

            sage: S = ClusterSeed(['A', 4], user_labels=['x', 'y', 'z', 'w']); S.mutate('x')
            sage: S.cluster_index('x')
            sage: S.cluster_index('(y+1)/x')
            0
        """
    def mutation_sequence(self, sequence, show_sequence: bool = False, fig_size: float = 1.2, return_output: str = 'seed'):
        """
        Return the seeds obtained by mutating ``self`` at all vertices
        in ``sequence``.

        INPUT:

        - ``sequence`` -- an iterable of vertices of self

        - ``show_sequence`` -- boolean (default: ``False``); if ``True``, a png
          containing the associated quivers is shown

        - ``fig_size`` -- (default: 1.2) factor by which the size of
          the plot is multiplied

        - ``return_output`` -- (default: ``'seed'``) determines what output
          is to be returned:

          * if ``'seed'``, outputs all the cluster seeds obtained
            by the ``sequence`` of mutations

          * if ``'matrix'``, outputs a list of exchange matrices

          * if ``'var'``, outputs a list of new cluster variables obtained
            at each step

        EXAMPLES::

            sage: S = ClusterSeed(['A',2])
            sage: for T in S.mutation_sequence([0,1,0]):
            ....:     print(T.b_matrix())
            [ 0 -1]
            [ 1  0]
            [ 0  1]
            [-1  0]
            [ 0 -1]
            [ 1  0]

            sage: S = ClusterSeed(['A',2])
            sage: S.mutation_sequence([0,1,0,1], return_output='var')
            [(x1 + 1)/x0, (x0 + x1 + 1)/(x0*x1), (x0 + 1)/x1, x0]
        """
    def mutation_analysis(self, options=['all'], filter=None):
        """
        Run an analysis of all potential mutation options. Note that this might
        take a long time on large seeds.

        .. NOTE::

            Edges are only returned if we have a non-valued quiver.
            Green and red vertices are only returned if the cluster is principal.

        INPUT:

        - ``options`` -- (default: ``['all']``) a list of mutation options
        - ``filter`` -- (default: ``None``) a vertex or interval of vertices to limit our search to

        Possible options are:

        - ``'all'`` -- all options below
        - ``'edges'`` -- number of edges (works with skew-symmetric quivers)
        - ``'edge_diff'`` -- edges added/deleted (works with skew-symmetric quivers)
        - ``'green_vertices'`` -- list of green vertices (works with principals)
        - ``'green_vertices_diff'`` -- green vertices added/removed (works with principals)
        - ``'red_vertices'`` -- list of red vertices (works with principals)
        - ``'red_vertices_diff'`` -- red vertices added/removed (works with principals)
        - ``'urban_renewals'`` -- list of urban renewal vertices
        - ``'urban_renewals_diff'`` -- urban renewal vertices added/removed
        - ``'sources'`` -- list of source vertices
        - ``'sources_diff'`` -- source vertices added/removed
        - ``'sinks'`` -- list of sink vertices
        - ``'sinks_diff'`` -- sink vertices added/removed
        - ``'denominators'`` -- list of all denominators of the cluster variables

        OUTPUT:

        Outputs a dictionary indexed by the vertex numbers. Each vertex will itself also be a
        dictionary with each desired option included as a key in the dictionary. As an example
        you would get something similar to: ``{0: {'edges': 1}, 1: {'edges': 2}}``. This represents
        that if you were to do a mutation at the current seed then mutating at vertex 0 would result
        in a quiver with 1 edge and mutating at vertex 0 would result in a quiver with 2 edges.

        EXAMPLES::

            sage: B = [[0, 4, 0, -1],[-4,0, 3, 0],[0, -3, 0, 1],[1, 0, -1, 0]]
            sage: S = ClusterSeed(matrix(B)); S.mutate([2,3,1,2,1,3,0,2])
            sage: S.mutation_analysis()
            {0: {'d_matrix': [ 0  0  1  0]
                             [ 0 -1  0  0]
                             [ 0  0  0 -1]
                             [-1  0  0  0],
                 'denominators': [1, 1, x0, 1],
                 'edge_diff': 6,
                 'edges': 13,
                 'green_vertices': [0, 1, 3],
                 'green_vertices_diff': {'added': [0], 'removed': []},
                 'red_vertices': [2],
                 'red_vertices_diff': {'added': [], 'removed': [0]},
                 'sinks': [],
                 'sinks_diff': {'added': [], 'removed': [2]},
                 'sources': [],
                 'sources_diff': {'added': [], 'removed': []},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}},
             1: {'d_matrix': [ 1  4  1  0]
                             [ 0  1  0  0]
                             [ 0  0  0 -1]
                             [ 1  4  0  0],
                 'denominators': [x0*x3, x0^4*x1*x3^4, x0, 1],
                 'edge_diff': 2,
                 'edges': 9,
                 'green_vertices': [0, 3],
                 'green_vertices_diff': {'added': [0], 'removed': [1]},
                 'red_vertices': [1, 2],
                 'red_vertices_diff': {'added': [1], 'removed': [0]},
                 'sinks': [2],
                 'sinks_diff': {'added': [], 'removed': []},
                 'sources': [],
                 'sources_diff': {'added': [], 'removed': []},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}},
             2: {'d_matrix': [ 1  0  0  0]
                             [ 0 -1  0  0]
                             [ 0  0  0 -1]
                             [ 1  0  1  0],
                 'denominators': [x0*x3, 1, x3, 1],
                 'edge_diff': 0,
                 'edges': 7,
                 'green_vertices': [1, 2, 3],
                 'green_vertices_diff': {'added': [2], 'removed': []},
                 'red_vertices': [0],
                 'red_vertices_diff': {'added': [], 'removed': [2]},
                 'sinks': [],
                 'sinks_diff': {'added': [], 'removed': [2]},
                 'sources': [2],
                 'sources_diff': {'added': [2], 'removed': []},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}},
             3: {'d_matrix': [ 1  0  1  1]
                             [ 0 -1  0  0]
                             [ 0  0  0  1]
                             [ 1  0  0  1],
                 'denominators': [x0*x3, 1, x0, x0*x2*x3],
                 'edge_diff': -1,
                 'edges': 6,
                 'green_vertices': [1],
                 'green_vertices_diff': {'added': [], 'removed': [3]},
                 'red_vertices': [0, 2, 3],
                 'red_vertices_diff': {'added': [3], 'removed': []},
                 'sinks': [2],
                 'sinks_diff': {'added': [], 'removed': []},
                 'sources': [1],
                 'sources_diff': {'added': [1], 'removed': []},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}}}

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.mutation_analysis()
            {0: {'d_matrix': [ 1  0  0]
                             [ 0 -1  0]
                             [ 0  0 -1],
                 'denominators': [x0, 1, 1],
                 'green_vertices': [1, 2],
                 'green_vertices_diff': {'added': [], 'removed': [0]},
                 'red_vertices': [0],
                 'red_vertices_diff': {'added': [0], 'removed': []},
                 'sinks': [],
                 'sinks_diff': {'added': [], 'removed': [1]},
                 'sources': [4, 5],
                 'sources_diff': {'added': [], 'removed': [3]},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}},
             1: {'d_matrix': [-1  0  0]
                             [ 0  1  0]
                             [ 0  0 -1],
                 'denominators': [1, x1, 1],
                 'green_vertices': [0, 2],
                 'green_vertices_diff': {'added': [], 'removed': [1]},
                 'red_vertices': [1],
                 'red_vertices_diff': {'added': [1], 'removed': []},
                 'sinks': [0, 2, 4],
                 'sinks_diff': {'added': [0, 2, 4], 'removed': [1]},
                 'sources': [1, 3, 5],
                 'sources_diff': {'added': [1], 'removed': [4]},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}},
             2: {'d_matrix': [-1  0  0]
                             [ 0 -1  0]
                             [ 0  0  1],
                 'denominators': [1, 1, x2],
                 'green_vertices': [0, 1],
                 'green_vertices_diff': {'added': [], 'removed': [2]},
                 'red_vertices': [2],
                 'red_vertices_diff': {'added': [2], 'removed': []},
                 'sinks': [],
                 'sinks_diff': {'added': [], 'removed': [1]},
                 'sources': [3, 4],
                 'sources_diff': {'added': [], 'removed': [5]},
                 'urban_renewals': [],
                 'urban_renewals_diff': {'added': [], 'removed': []}}}
        """
    def exchangeable_part(self):
        """
        Return the restriction to the principal part (i.e. the exchangeable
        variables) of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',4])
            sage: T = ClusterSeed(S.quiver().digraph().edges(sort=True), frozen=[3])
            sage: T.quiver().digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1)), (2, 3, (1, -1))]

            sage: T.exchangeable_part().quiver().digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1))]
        """
    def universal_extension(self):
        """
        Return the universal extension of ``self``.

        This is the initial seed of the associated cluster algebra
        with universal coefficients, as defined in section 12 of
        [FZ2007]_.

        This method works only if ``self`` is a bipartite, finite-type seed.

        Due to some limitations in the current implementation of
        ``CartanType``, we need to construct the set of almost positive
        coroots by hand. As a consequence their ordering is not the
        standard one (the rows of the bottom part of the exchange
        matrix might be a shuffling of those you would expect).

        EXAMPLES::

            sage: S = ClusterSeed(['A',2])
            sage: T = S.universal_extension()
            sage: T.b_matrix()
            [ 0  1]
            [-1  0]
            [-1  0]
            [ 1  0]
            [ 1 -1]
            [ 0  1]
            [ 0 -1]

            sage: S = ClusterSeed(['A',3])
            sage: T = S.universal_extension()
            sage: T.b_matrix()
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]
            [-1  0  0]
            [ 1  0  0]
            [ 1 -1  0]
            [ 1 -1  1]
            [ 0  1  0]
            [ 0 -1  0]
            [ 0 -1  1]
            [ 0  0 -1]
            [ 0  0  1]

            sage: S = ClusterSeed(['B',2])
            sage: T = S.universal_extension()
            sage: T.b_matrix()
            [ 0  1]
            [-2  0]
            [-1  0]
            [ 1  0]
            [ 1 -1]
            [ 2 -1]
            [ 0  1]
            [ 0 -1]

            sage: S = ClusterSeed(['A', 5], user_labels=[-2, -1, 0, 1 ,2])
            sage: U = S.universal_extension()
            sage: U.b_matrix() == ClusterSeed(['A', 5]).universal_extension().b_matrix()
            True
        """
    def principal_extension(self):
        """
        Return the principal extension of ``self``, yielding a
        `2n \\times n` matrix.

        Raises an error if the input seed has a non-square exchange matrix.
        In this case, the method instead adds `n` frozen variables to any
        previously frozen variables. I.e., the seed obtained by adding a
        frozen variable to every exchangeable variable of ``self``.

        EXAMPLES::

            sage: S = ClusterSeed([[0,1],[1,2],[2,3],[2,4]]); S
            A seed for a cluster algebra of rank 5

            sage: T = S.principal_extension(); T
            A seed for a cluster algebra of rank 5 with principal coefficients

            sage: T.b_matrix()
            [ 0  1  0  0  0]
            [-1  0  1  0  0]
            [ 0 -1  0  1  1]
            [ 0  0 -1  0  0]
            [ 0  0 -1  0  0]
            [ 1  0  0  0  0]
            [ 0  1  0  0  0]
            [ 0  0  1  0  0]
            [ 0  0  0  1  0]
            [ 0  0  0  0  1]

            sage: S = ClusterSeed(['A', 4], user_labels=['a', 'b', 'c', 'd'])
            sage: T = S.principal_extension()
            sage: T.cluster()
            [a, b, c, d]
            sage: T.coefficients()
            [y0, y1, y2, y3]
            sage: S2 = ClusterSeed(['A', 4], user_labels={0:'a', 1:'b', 2:'c', 3:'d'})
            sage: S2 == S
            True
            sage: T2 = S2.principal_extension()
            sage: T2 == T
            True
        """
    def reorient(self, data) -> None:
        """
        Reorients ``self`` with respect to the given total order,
        or with respect to an iterator of ordered pairs.

        .. warning::

            - This operation might change the mutation type of ``self``.
            - Ignores ordered pairs `(i,j)` for which neither `(i,j)` nor `(j,i)`
              is an edge of ``self``.

        INPUT:

        - ``data`` -- an iterator defining a total order on ``self.vertices()``,
          or an iterator of ordered pairs in ``self`` defining the new
          orientation of these edges.

        EXAMPLES::

            sage: S = ClusterSeed(['A',[2,3],1])
            sage: S.mutation_type()
            ['A', [2, 3], 1]

            sage: S.reorient([(0,1),(2,3)])
            sage: S.mutation_type()
            ['D', 5]

            sage: S.reorient([(1,0),(2,3)])
            sage: S.mutation_type()
            ['A', [1, 4], 1]

            sage: S.reorient([0,1,2,3,4])
            sage: S.mutation_type()
            ['A', [1, 4], 1]
        """
    def set_cluster(self, cluster, force: bool = False) -> None:
        """
        Set the cluster for ``self`` to ``cluster``.

        .. warning::

            Initialization may lead to inconsistent data.

        INPUT:

        - ``cluster`` -- an iterable defining a cluster for ``self``

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: cluster = S.cluster()
            sage: S.mutate([1,2,1])
            sage: S.cluster()
            [x0, (x1 + 1)/x2, (x0*x2 + x1 + 1)/(x1*x2)]
            sage: cluster2 = S.cluster()

            sage: S.set_cluster(cluster)
            Warning: using set_cluster at this point could lead to inconsistent seed data.

            sage: S.set_cluster(cluster, force=True)
            sage: S.cluster()
            [x0, x1, x2]
            sage: S.set_cluster(cluster2, force=True)
            sage: S.cluster()
            [x0, (x1 + 1)/x2, (x0*x2 + x1 + 1)/(x1*x2)]

            sage: S = ClusterSeed(['A',3]); S.use_fpolys(False)
            sage: S.set_cluster([1,1,1])
            Warning: clusters not being tracked so this command is ignored.
        """
    def reset_cluster(self) -> None:
        """
        Reset the cluster of ``self`` to the initial cluster.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.mutate([1,2,1])
            sage: S.cluster()
            [x0, (x1 + 1)/x2, (x0*x2 + x1 + 1)/(x1*x2)]

            sage: S.reset_cluster()
            sage: S.cluster()
            [x0, x1, x2]

            sage: T = S.principal_extension()
            sage: T.cluster()
            [x0, x1, x2]
            sage: T.mutate([1,2,1])
            sage: T.cluster()
            [x0, (x1*y2 + x0)/x2, (x1*y1*y2 + x0*y1 + x2)/(x1*x2)]

            sage: T.reset_cluster()
            sage: T.cluster()
            [x0, x1, x2]

            sage: S = ClusterSeed(['B',3], user_labels=[[1,2],[2,3],[3,4]],
            ....:                 user_labels_prefix='p')
            sage: S.mutate([0,1])
            sage: S.cluster()
            [(p_2_3 + 1)/p_1_2, (p_1_2*p_3_4^2 + p_2_3 + 1)/(p_1_2*p_2_3), p_3_4]

            sage: S.reset_cluster()
            sage: S.cluster()
            [p_1_2, p_2_3, p_3_4]
            sage: S.g_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: S.f_polynomials()
            [1, 1, 1]
        """
    def reset_coefficients(self) -> None:
        """
        Reset the coefficients of ``self`` to the frozen variables but keep the current cluster.

        This raises an error if the number of frozen variables is different
        from the number of exchangeable variables.

        .. warning::

            This command to be phased out since :meth:`use_c_vectors`
            does this more effectively.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3]).principal_extension()
            sage: S.b_matrix()
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]
            [ 1  0  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: S.mutate([1,2,1])
            sage: S.b_matrix()
            [ 0  1 -1]
            [-1  0  1]
            [ 1 -1  0]
            [ 1  0  0]
            [ 0  1 -1]
            [ 0  0 -1]
            sage: S.reset_coefficients()
            sage: S.b_matrix()
            [ 0  1 -1]
            [-1  0  1]
            [ 1 -1  0]
            [ 1  0  0]
            [ 0  1  0]
            [ 0  0  1]
        """
    def mutation_class_iter(self, depth=..., show_depth: bool = False, return_paths: bool = False, up_to_equivalence: bool = True, only_sink_source: bool = False) -> Generator[Incomplete]:
        """
        Return an iterator for the mutation class of ``self`` with
        respect to certain constraints.

        INPUT:

        - ``depth`` -- (default: infinity) integer or infinity, only seeds with
          distance at most ``depth`` from ``self`` are returned
        - ``show_depth`` -- boolean (default: ``False``); if ``True``, the
          current depth of the mutation is shown while computing
        - ``return_paths`` -- boolean (default: ``False``); if ``True``, a
          shortest path of mutations from ``self`` to the given quiver is
          returned as well
        - ``up_to_equivalence`` -- boolean (default: ``True``); if ``True``,
          only one seed up to simultaneous permutation of rows and columns of
          the exchange matrix is recorded
        - ``sink_source`` -- boolean (default: ``False``); if ``True``, only
          mutations at sinks and sources are applied

        EXAMPLES:

        A standard finite type example::

            sage: S = ClusterSeed(['A',3])
            sage: it = S.mutation_class_iter()
            sage: for T in it: print(T)
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]

        A finite type example with given depth::

            sage: it = S.mutation_class_iter(depth=1)
            sage: for T in it: print(T)
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]
            A seed for a cluster algebra of rank 3 of type ['A', 3]

        A finite type example where the depth is shown while computing::

            sage: it = S.mutation_class_iter(show_depth=True)
            sage: for T in it: pass
            Depth: 0     found: 1          Time: ... s
            Depth: 1     found: 4          Time: ... s
            Depth: 2     found: 9          Time: ... s
            Depth: 3     found: 13         Time: ... s
            Depth: 4     found: 14         Time: ... s

        A finite type example with shortest paths returned::

            sage: it = S.mutation_class_iter(return_paths=True)
            sage: mutation_class = list(it)
            sage: len(mutation_class)
            14
            sage: mutation_class[0]
            (A seed for a cluster algebra of rank 3 of type ['A', 3], [])

        Finite type examples not considered up to equivalence::

            sage: it = S.mutation_class_iter(up_to_equivalence=False)
            sage: len([T for T in it])
            84

            sage: it = ClusterSeed(['A',2]).mutation_class_iter(return_paths=True,
            ....:                                               up_to_equivalence=False)
            sage: mutation_class = list(it)
            sage: len(mutation_class)
            10
            sage: mutation_class[0]
            (A seed for a cluster algebra of rank 2 of type ['A', 2], [])

        Check that :issue:`14638` is fixed::

            sage: S = ClusterSeed(['E',6])
            sage: MC = S.mutation_class(depth=6); len(MC)  # long time
            388

        Infinite type examples::

            sage: S = ClusterSeed(['A',[1,1],1])
            sage: it = S.mutation_class_iter()
            sage: next(it)
            A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1]
            sage: next(it)
            A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1]
            sage: next(it)
            A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1]
            sage: next(it)
            A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1]

            sage: it = S.mutation_class_iter(depth=3, return_paths=True)
            sage: for T in it: print(T)
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [])
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [1])
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [0])
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [1, 0])
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [0, 1])
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [1, 0, 1])
            (A seed for a cluster algebra of rank 2 of type ['A', [1, 1], 1], [0, 1, 0])
        """
    def mutation_class(self, depth=..., show_depth: bool = False, return_paths: bool = False, up_to_equivalence: bool = True, only_sink_source: bool = False):
        """
        Return the mutation class of ``self`` with respect to
        certain constraints.

        .. NOTE::

            Vertex labels are not tracked in this method.

        .. SEEALSO::

            :meth:`mutation_class_iter`

        INPUT:

        - ``depth`` -- (default: ``infinity``) integer, only seeds with
          distance at most depth from ``self`` are returned
        - ``show_depth`` -- boolean (default: ``False``); if ``True``, the
          actual depth of the mutation is shown
        - ``return_paths`` -- boolean (default: ``False``); if ``True``, a
          shortest path of mutation sequences from self to the given quiver is
          returned as well
        - ``up_to_equivalence`` -- boolean (default: ``True``); if ``True``,
          only seeds up to equivalence are considered
        - ``sink_source`` -- boolean (default: ``False``); if ``True``, only
          mutations at sinks and sources are applied

        EXAMPLES:

        - for examples see :meth:`mutation_class_iter`

        TESTS::

            sage: A = ClusterSeed(['A',3]).mutation_class()
        """
    def cluster_class_iter(self, depth=..., show_depth: bool = False, up_to_equivalence: bool = True) -> Generator[Incomplete]:
        """
        Return an iterator through all clusters in the mutation class of ``self``.

        INPUT:

        - ``depth`` -- (default: infinity) integer or infinity, only seeds with
          distance at most ``depth`` from ``self`` are returned
        - ``show_depth`` -- boolean (default: ``False``); if ``True``, ignored
          if ``depth`` is set; returns the depth of the mutation class, i.e.,
          the maximal distance from ``self`` of an element in the mutation
          class
        - ``up_to_equivalence`` -- boolean (default: ``True``); if ``True``,
          only clusters up to equivalence are considered

        EXAMPLES:

        A standard finite type example::

            sage: S = ClusterSeed(['A',3])
            sage: it = S.cluster_class_iter()
            sage: cluster_class = list(it)
            sage: len(cluster_class)
            14
            sage: cluster_class[0]
            [x0, x1, x2]

        A finite type example with given depth::

            sage: it = S.cluster_class_iter(depth=1)
            sage: for T in it: print(T)
            [x0, x1, x2]
            [x0, x1, (x1 + 1)/x2]
            [x0, (x0*x2 + 1)/x1, x2]
            [(x1 + 1)/x0, x1, x2]

        A finite type example where the depth is returned while computing::

            sage: it = S.cluster_class_iter(show_depth=True)
            sage: _ = list(it)
            Depth: 0     found: 1          Time: ... s
            Depth: 1     found: 4          Time: ... s
            Depth: 2     found: 9          Time: ... s
            Depth: 3     found: 13         Time: ... s
            Depth: 4     found: 14         Time: ... s

        Finite type examples not considered up to equivalence::

            sage: it = S.cluster_class_iter(up_to_equivalence=False)
            sage: len([T for T in it])
            84

            sage: it = ClusterSeed(['A',2]).cluster_class_iter(up_to_equivalence=False)
            sage: cluster_class = list(it)
            sage: len(cluster_class)
            10
            sage: cluster_class[0]
            [x0, x1]
            sage: cluster_class[-1]
            [x1, x0]

        Infinite type examples::

            sage: S = ClusterSeed(['A',[1,1],1])
            sage: it = S.cluster_class_iter()
            sage: next(it)
            [x0, x1]
            sage: next(it)
            [x0, (x0^2 + 1)/x1]
            sage: next(it)
            [(x1^2 + 1)/x0, x1]
            sage: next(it)
            [(x0^4 + 2*x0^2 + x1^2 + 1)/(x0*x1^2), (x0^2 + 1)/x1]
            sage: next(it)
            [(x1^2 + 1)/x0, (x1^4 + x0^2 + 2*x1^2 + 1)/(x0^2*x1)]

            sage: it = S.cluster_class_iter(depth=3)
            sage: for T in it: print(T)
            [x0, x1]
            [x0, (x0^2 + 1)/x1]
            [(x1^2 + 1)/x0, x1]
            [(x0^4 + 2*x0^2 + x1^2 + 1)/(x0*x1^2), (x0^2 + 1)/x1]
            [(x1^2 + 1)/x0, (x1^4 + x0^2 + 2*x1^2 + 1)/(x0^2*x1)]
            [(x0^4 + 2*x0^2 + x1^2 + 1)/(x0*x1^2), (x0^6 + 3*x0^4 + 2*x0^2*x1^2 + x1^4 + 3*x0^2 + 2*x1^2 + 1)/(x0^2*x1^3)]
            [(x1^6 + x0^4 + 2*x0^2*x1^2 + 3*x1^4 + 2*x0^2 + 3*x1^2 + 1)/(x0^3*x1^2), (x1^4 + x0^2 + 2*x1^2 + 1)/(x0^2*x1)]

        For a cluster seed from an arbitrarily labelled digraph::

            sage: dg = DiGraph([['a', 'b'], ['b', 'c']], format='list_of_edges')
            sage: S = ClusterSeed(dg, frozen=['b'])
            sage: S.cluster_class()
            [[a, c], [a, (b + 1)/c], [(b + 1)/a, c], [(b + 1)/a, (b + 1)/c]]

            sage: S2 = ClusterSeed(dg, frozen=[])
            sage: S2.cluster_class()[0]
            [a, b, c]
        """
    def cluster_class(self, depth=..., show_depth: bool = False, up_to_equivalence: bool = True):
        """
        Return the cluster class of ``self`` with respect to certain constraints.

        INPUT:

        - ``depth`` -- (default: infinity) integer, only seeds with distance
          at most ``depth`` from ``self`` are returned
        - ``return_depth`` -- (default: ``False``) if ``True``, ignored if
          ``depth`` is set; returns the depth of the mutation class, i.e.,
          the maximal distance from ``self`` of an element in the mutation class
        - ``up_to_equivalence`` -- (default: ``True``) if ``True``, only
          clusters up to equivalence are considered

        EXAMPLES:

        - for examples see :meth:`cluster_class_iter`

        TESTS::

            sage: A = ClusterSeed(['A',3]).cluster_class()
        """
    def b_matrix_class_iter(self, depth=..., up_to_equivalence: bool = True) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator through all `B`-matrices in the mutation class of
        ``self``.

        INPUT:

        - ``depth`` -- (default: infinity) integer or infinity, only seeds
          with distance at most ``depth`` from ``self`` are returned
        - ``up_to_equivalence`` -- boolean (default: ``True``); if ``True``,
          only `B`-matrices up to equivalence are considered

        EXAMPLES:

        A standard finite type example::

            sage: S = ClusterSeed(['A',4])
            sage: it = S.b_matrix_class_iter()
            sage: for T in it: print(T)
            [ 0  0  0  1]
            [ 0  0  1  1]
            [ 0 -1  0  0]
            [-1 -1  0  0]
            [ 0  0  0  1]
            [ 0  0  1  0]
            [ 0 -1  0  1]
            [-1  0 -1  0]
            [ 0  0  1  1]
            [ 0  0  0 -1]
            [-1  0  0  0]
            [-1  1  0  0]
            [ 0  0  0  1]
            [ 0  0 -1  1]
            [ 0  1  0 -1]
            [-1 -1  1  0]
            [ 0  0  0  1]
            [ 0  0 -1  0]
            [ 0  1  0 -1]
            [-1  0  1  0]
            [ 0  0  0 -1]
            [ 0  0 -1  1]
            [ 0  1  0 -1]
            [ 1 -1  1  0]

        A finite type example with given depth::

            sage: it = S.b_matrix_class_iter(depth=1)
            sage: for T in it: print(T)
            [ 0  0  0  1]
            [ 0  0  1  1]
            [ 0 -1  0  0]
            [-1 -1  0  0]
            [ 0  0  0  1]
            [ 0  0  1  0]
            [ 0 -1  0  1]
            [-1  0 -1  0]
            [ 0  0  1  1]
            [ 0  0  0 -1]
            [-1  0  0  0]
            [-1  1  0  0]

        Finite type example not considered up to equivalence::

            sage: S = ClusterSeed(['A',3])
            sage: it = S.b_matrix_class_iter(up_to_equivalence=False)
            sage: b_matrix_class = list(it)
            sage: len(b_matrix_class)
            14
            sage: b_matrix_class[0]
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]

        Infinite (but finite mutation) type example::

            sage: S = ClusterSeed(['A',[1,2],1])
            sage: it = S.b_matrix_class_iter()
            sage: for T in it: print(T)
            [ 0  1  1]
            [-1  0  1]
            [-1 -1  0]
            [ 0 -2  1]
            [ 2  0 -1]
            [-1  1  0]

        Infinite mutation type example::

            sage: S = ClusterSeed(['E',10])
            sage: it = S.b_matrix_class_iter(depth=3)
            sage: len ([T for T in it])
            266

        For a cluster seed from an arbitrarily labelled digraph::

            sage: dg = DiGraph([['a', 'b'], ['b', 'c']], format='list_of_edges')
            sage: S = ClusterSeed(dg, frozen=['b'])
            sage: S.b_matrix_class()
            [
            [ 0  0]  [ 0  0]  [0 0]
            [ 0  0]  [ 0  0]  [0 0]
            [-1  1], [-1 -1], [1 1]
            ]
        """
    def b_matrix_class(self, depth=..., up_to_equivalence: bool = True):
        """
        Return all `B`-matrices in the mutation class of ``self``.

        INPUT:

        - ``depth`` -- (default: infinity) integer or infinity, only seeds
          with distance at most ``depth`` from ``self`` are returned
        - ``up_to_equivalence`` -- boolean (default: ``True``); if ``True``,
          only `B`-matrices up to equivalence are considered

        EXAMPLES:

        - for examples see :meth:`b_matrix_class_iter`

        TESTS::

            sage: A = ClusterSeed(['A',3]).b_matrix_class()
            sage: A = ClusterSeed(['A',[2,1],1]).b_matrix_class()
        """
    def variable_class_iter(self, depth=..., ignore_bipartite_belt: bool = False) -> Generator[Incomplete]:
        """
        Return an iterator for all cluster variables in the mutation class of
        ``self``.

        INPUT:

            - ``depth`` -- (default: infinity) integer, only seeds with distance
              at most ``depth`` from ``self`` are returned
            - ``ignore_bipartite_belt`` -- boolean (default: ``False``); if
              ``True``, the algorithm does not use the bipartite belt

        EXAMPLES:

        A standard finite type example::

            sage: S = ClusterSeed(['A',3])
            sage: it = S.variable_class_iter()
            sage: for T in it: print(T)
            x0
            x1
            x2
            (x1 + 1)/x0
            (x1^2 + x0*x2 + 2*x1 + 1)/(x0*x1*x2)
            (x1 + 1)/x2
            (x0*x2 + x1 + 1)/(x0*x1)
            (x0*x2 + 1)/x1
            (x0*x2 + x1 + 1)/(x1*x2)

        Finite type examples with given depth::

            sage: it = S.variable_class_iter(depth=1)
            sage: for T in it: print(T)
            Found a bipartite seed - restarting the depth counter at zero
            and constructing the variable class using its bipartite belt.
            x0
            x1
            x2
            (x1 + 1)/x0
            (x1^2 + x0*x2 + 2*x1 + 1)/(x0*x1*x2)
            (x1 + 1)/x2
            (x0*x2 + x1 + 1)/(x0*x1)
            (x0*x2 + 1)/x1
            (x0*x2 + x1 + 1)/(x1*x2)

        Note that the notion of *depth* depends on whether a bipartite seed
        is found or not, or if it is manually ignored::

            sage: it = S.variable_class_iter(depth=1, ignore_bipartite_belt=True)
            sage: for T in it: print(T)
            x0
            x1
            x2
            (x1 + 1)/x2
            (x0*x2 + 1)/x1
            (x1 + 1)/x0

            sage: S.mutate([0,1])
            sage: it2 = S.variable_class_iter(depth=1)
            sage: for T in it2: print(T)
            (x1 + 1)/x0
            (x0*x2 + x1 + 1)/(x0*x1)
            x2
            (x1^2 + x0*x2 + 2*x1 + 1)/(x0*x1*x2)
            x1
            (x0*x2 + 1)/x1

        Infinite type examples::

            sage: S = ClusterSeed(['A',[1,1],1])
            sage: it = S.variable_class_iter(depth=2)
            sage: for T in it: print(T)
            Found a bipartite seed - restarting the depth counter at zero
            and constructing the variable class using its bipartite belt.
            x0
            x1
            (x1^2 + 1)/x0
            (x1^4 + x0^2 + 2*x1^2 + 1)/(x0^2*x1)
            (x0^4 + 2*x0^2 + x1^2 + 1)/(x0*x1^2)
            (x0^2 + 1)/x1
            (x1^6 + x0^4 + 2*x0^2*x1^2 + 3*x1^4 + 2*x0^2 + 3*x1^2 + 1)/(x0^3*x1^2)
            (x1^8 + x0^6 + 2*x0^4*x1^2 + 3*x0^2*x1^4 + 4*x1^6 + 3*x0^4 + 6*x0^2*x1^2 + 6*x1^4 + 3*x0^2 + 4*x1^2 + 1)/(x0^4*x1^3)
            (x0^8 + 4*x0^6 + 3*x0^4*x1^2 + 2*x0^2*x1^4 + x1^6 + 6*x0^4 + 6*x0^2*x1^2 + 3*x1^4 + 4*x0^2 + 3*x1^2 + 1)/(x0^3*x1^4)
            (x0^6 + 3*x0^4 + 2*x0^2*x1^2 + x1^4 + 3*x0^2 + 2*x1^2 + 1)/(x0^2*x1^3)
        """
    def variable_class(self, depth=..., ignore_bipartite_belt: bool = False):
        """
        Return all cluster variables in the mutation class of ``self``.

        INPUT:

        - ``depth`` -- (default: infinity) integer, only seeds with distance
          at most ``depth`` from ``self`` are returned
        - ``ignore_bipartite_belt`` -- boolean (default: ``False``); if
          ``True``, the algorithm does not use the bipartite belt

        EXAMPLES:

        - for examples see :meth:`variable_class_iter`

        TESTS::

            sage: A = ClusterSeed(['A',3]).variable_class()
        """
    def is_finite(self) -> bool:
        """
        Return ``True`` if ``self`` is of finite type.

        EXAMPLES::

            sage: S = ClusterSeed(['A',3])
            sage: S.is_finite()
            True

            sage: S = ClusterSeed(['A',[2,2],1])
            sage: S.is_finite()
            False

        TESTS::

            sage: Q = ClusterQuiver([[1,2],[2,3],[3,4],[4,1]])
            sage: Q.is_finite()
            True
        """
    def is_mutation_finite(self, nr_of_checks=None, return_path: bool = False):
        """
        Return ``True`` if ``self`` is of finite mutation type.

        INPUT:

        - ``nr_of_checks`` -- (default: ``None``) number of mutations applied;
          standard is 500 times the number of vertices of ``self``
        - ``return_path`` -- boolean (default: ``False``); if ``True``, in case
          of ``self`` not being mutation finite, a path from ``self`` to a
          quiver with an edge label `(a,-b)` and `a*b > 4` is returned

        ALGORITHM:

        - A cluster seed is mutation infinite if and only if every
          `b_{ij}*b_{ji} > -4`. Thus, we apply random mutations in random directions

        .. warning::

            - Uses a non-deterministic method by random mutations in various directions.
            - In theory, it can return a wrong ``True``.

        EXAMPLES::

            sage: S = ClusterSeed(['A',10])
            sage: S._mutation_type = None
            sage: S.is_mutation_finite()
            True

            sage: S = ClusterSeed([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,9)])
            sage: S.is_mutation_finite()
            False
        """
    def mutation_type(self):
        """
        Return the mutation type of each connected component of ``self``, if it can be determined.

        Otherwise, the mutation type of this component is set to be unknown.

        The mutation types of the components are ordered by vertex labels.

        .. warning::

            - All finite types can be detected,
            - All affine types can be detected, **except** affine type D
              (the algorithm is not yet implemented)
            - All exceptional types can be detected.

            - Might fail to work if it is used within different Sage processes
              simultaneously (that happened in the doctesting).

        EXAMPLES:

        - finite types::

            sage: S = ClusterSeed(['A',5])
            sage: S._mutation_type = S._quiver._mutation_type = None
            sage: S.mutation_type()
            ['A', 5]

            sage: S = ClusterSeed([(0,1),(1,2),(2,3),(3,4)])
            sage: S.mutation_type()
            ['A', 5]

            sage: S = ClusterSeed(DiGraph([['a','b'],['c','b'],['c','d'],['e','d']]),
            ....:                 frozen=['c'])
            sage: S.mutation_type()
            [ ['A', 2], ['A', 2] ]

        - affine types::

            sage: S = ClusterSeed(['E',8,[1,1]]); S
            A seed for a cluster algebra of rank 10 of type ['E', 8, [1, 1]]
            sage: S._mutation_type = S._quiver._mutation_type = None; S
            A seed for a cluster algebra of rank 10
            sage: S.mutation_type() # long time
            ['E', 8, [1, 1]]

        - the not yet working affine type D::

            sage: S = ClusterSeed(['D',4,1])
            sage: S._mutation_type = S._quiver._mutation_type = None
            sage: S.mutation_type() # todo: not implemented
            ['D', 4, 1]

        - the exceptional types::

            sage: S = ClusterSeed(['X',6])
            sage: S._mutation_type = S._quiver._mutation_type = None
            sage: S.mutation_type() # long time
            ['X', 6]

        -  infinite types::

            sage: S = ClusterSeed(['GR',[4,9]])
            sage: S._mutation_type = S._quiver._mutation_type = None
            sage: S.mutation_type()
            'undetermined infinite mutation type'
        """
    def greedy(self, a1, a2, algorithm: str = 'by_recursion'):
        """
        Return the greedy element `x[a_1,a_2]` assuming that ``self`` is rank two.

        The third input can be ``'by_recursion'``, ``'by_combinatorics'``, or
        ``'just_numbers'`` to specify if the user wants the element
        computed by the recurrence, combinatorial formula, or wants to
        set `x_1` and `x_2` to be one.

        See [LLZ2014]_ for more details.

        EXAMPLES::

            sage: S = ClusterSeed(['R2', [3, 3]])
            sage: S.greedy(4, 4)
            (x0^12 + x1^12 + 4*x0^9 + 4*x1^9 + 6*x0^6
              + 4*x0^3*x1^3 + 6*x1^6 + 4*x0^3 + 4*x1^3 + 1)/(x0^4*x1^4)
            sage: S.greedy(4, 4, 'by_combinatorics')
            (x0^12 + x1^12 + 4*x0^9 + 4*x1^9 + 6*x0^6
              + 4*x0^3*x1^3 + 6*x1^6 + 4*x0^3 + 4*x1^3 + 1)/(x0^4*x1^4)
            sage: S.greedy(4, 4, 'just_numbers')
            35
            sage: S = ClusterSeed(['R2', [2, 2]])
            sage: S.greedy(1, 2)
            (x0^4 + 2*x0^2 + x1^2 + 1)/(x0*x1^2)
            sage: S.greedy(1, 2, 'by_combinatorics')
            (x0^4 + 2*x0^2 + x1^2 + 1)/(x0*x1^2)

        TESTS:

        We check that :issue:`23688` has been resolved::

            sage: S = ClusterSeed(Matrix([[0,1],[-4,0]])); S
            A seed for a cluster algebra of rank 2
            sage: S.greedy(1,2)
            (x1^4 + x0^2 + 2*x0 + 1)/(x0*x1^2)
            sage: S.greedy(1,2,'by_combinatorics')
            (x1^4 + x0^2 + 2*x0 + 1)/(x0*x1^2)
        """
    def oriented_exchange_graph(self):
        """
        Return the oriented exchange graph of ``self`` as a directed graph.

        The seed must be a cluster seed for a cluster algebra of
        finite type with principal coefficients (the corresponding
        quiver must have mutable vertices `0,1,...,n-1`).

        EXAMPLES::

            sage: S = ClusterSeed(['A', 2]).principal_extension()
            sage: G = S.oriented_exchange_graph(); G
            Digraph on 5 vertices
            sage: G.out_degree_sequence()
            [2, 1, 1, 1, 0]

            sage: S = ClusterSeed(['B', 2]).principal_extension()
            sage: G = S.oriented_exchange_graph(); G
            Digraph on 6 vertices
            sage: G.out_degree_sequence()
            [2, 1, 1, 1, 1, 0]

        TESTS::

            sage: S = ClusterSeed(['A',[2,2],1])
            sage: S.oriented_exchange_graph()
            Traceback (most recent call last):
            ...
            TypeError: only works for finite mutation type

            sage: S = ClusterSeed(['A', 2])
            sage: S.oriented_exchange_graph()
            Traceback (most recent call last):
            ...
            TypeError: only works for principal coefficients
        """
    def find_upper_bound(self, verbose: bool = False):
        """
        Return the upper bound of the given cluster algebra as a quotient ring.

        The upper bound is the intersection of the Laurent polynomial
        rings of the initial cluster and its neighboring clusters.  As
        such, it always contains both the cluster algebra and the
        upper cluster algebra.  This function uses the algorithm from
        [MM2015]_.

        When the initial seed is totally coprime (for example, when
        the unfrozen part of the exchange matrix has full rank), the
        upper bound is equal to the upper cluster algebra by
        [BFZ2005]_.

        .. WARNING::

            The computation time grows rapidly with the size
            of the seed and the number of steps.  For most seeds
            larger than four vertices, the algorithm may take an
            infeasible amount of time.  Additionally, it will run
            forever without terminating whenever the upper bound is
            infinitely-generated (such as the example in [Spe2013]_).

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); if ``True``, prints
          output during the computation

        EXAMPLES:

        - finite type::

            sage: S = ClusterSeed(['A',3])
            sage: S.find_upper_bound()
            Quotient of Multivariate Polynomial Ring in x0, x1, x2, x0p, x1p, x2p, z0
             over Rational Field
             by the ideal (x0*x0p - x1 - 1, x1*x1p - x0*x2 - 1, x2*x2p - x1 - 1,
                           x0*z0 - x2p, x1*z0 + z0 - x0p*x2p, x2*z0 - x0p,
                           x1p*z0 + z0 - x0p*x1p*x2p + x1 + 1)

        - Markov::

            sage: B = matrix([[0,2,-2],[-2,0,2],[2,-2,0]])
            sage: S = ClusterSeed(B)
            sage: S.find_upper_bound()
            Quotient of Multivariate Polynomial Ring in x0, x1, x2, x0p, x1p, x2p, z0
             over Rational Field
             by the ideal (x0*x0p - x2^2 - x1^2, x1*x1p - x2^2 - x0^2, x2*x2p - x1^2 - x0^2,
                           x0p*x1p*x2p - x0*x1*x2p - x0*x2*x1p - x1*x2*x0p - 2*x0*x1*x2,
                           x0^3*z0 - x1p*x2p + x1*x2, x0*x1*z0 - x2p - x2,
                           x1^3*z0 - x0p*x2p + x0*x2, x0*x2*z0 - x1p - x1,
                           x1*x2*z0 - x0p - x0, x2^3*z0 - x0p*x1p + x0*x1)
        """
    def get_upper_cluster_algebra_element(self, a):
        """
        Compute an element in the upper cluster algebra of `B` corresponding to
        the vector `a \\in \\ZZ^n`.

        See [LLM2014]_ for more details.

        INPUT:

        - ``B`` -- a skew-symmetric matrix. Must have the same number of columns
          as the length of the vectors in `vd`
        - ``a`` -- a vector in `\\ZZ^n` where `n` is the number of columns in `B`

        OUTPUT: an element in the upper cluster algebra. Depending on the input
        it may or may not be irreducible

        EXAMPLES::

            sage: B = matrix([[0,3,-3],[-3,0,3],[3,-3,0],[1,0,0],[0,1,0],[0,0,1]])
            sage: C = ClusterSeed(B)
            sage: C.get_upper_cluster_algebra_element([1,1,0])
            (x0^3*x2^3*x3*x4 + x2^6*x3 + x1^3*x2^3)/(x0*x1)
            sage: C.get_upper_cluster_algebra_element([1,1,1])
            x0^2*x1^2*x2^2*x3*x4*x5 + x0^2*x1^2*x2^2

            sage: B = matrix([[0,3,0],[-3,0,3],[0,-3,0]])
            sage: C = ClusterSeed(B)
            sage: C.get_upper_cluster_algebra_element([1,1,0])
            (x1^3*x2^3 + x0^3 + x2^3)/(x0*x1)
            sage: C.get_upper_cluster_algebra_element([1,1,1])
            (x0^3*x1^3 + x1^3*x2^3 + x0^3 + x2^3)/(x0*x1*x2)

            sage: B = matrix([[0,2],[-3,0],[4,-5]])
            sage: C = ClusterSeed(B)
            sage: C.get_upper_cluster_algebra_element([1,1])
            (x2^9 + x1^3*x2^5 + x0^2*x2^4)/(x0*x1)

            sage: B = matrix([[0,3,-5],[-3,0,4],[5,-4,0]])
            sage: C = ClusterSeed(B)
            sage: C.get_upper_cluster_algebra_element([1,1,1])
            x0^4*x1^2*x2^3 + x0^2*x1^3*x2^4
        """
    def LLM_gen_set(self, size_limit: int = -1):
        """
        Produce a list of upper cluster algebra elements corresponding to all
        vectors in `\\{0,1\\}^n`.

        INPUT:

        - ``B`` -- a skew-symmetric matrix
        - ``size_limit`` -- a limit on how many vectors you want
          the function to return

        OUTPUT: an array of elements in the upper cluster algebra

        EXAMPLES::

            sage: B = matrix([[0,1,0],[-1,0,1],[0,-1,0],[1,0,0],[0,1,0],[0,0,1]])
            sage: C = ClusterSeed(B)
            sage: C.LLM_gen_set()
            [1,
             (x1 + x3)/x0,
             (x0*x4 + x2)/x1,
             (x0*x3*x4 + x1*x2 + x2*x3)/(x0*x1),
             (x1*x5 + 1)/x2,
             (x1^2*x5 + x1*x3*x5 + x1 + x3)/(x0*x2),
             (x0*x1*x4*x5 + x0*x4 + x2)/(x1*x2),
             (x0*x1*x3*x4*x5 + x0*x3*x4 + x1*x2 + x2*x3)/(x0*x1*x2)]
        """

def coeff_recurs(p, q, a1, a2, b, c):
    """
    Coefficients in Laurent expansion of greedy element, as defined by recursion.

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import coeff_recurs
        sage: coeff_recurs(1, 1, 5, 5, 3, 3)
        10
    """
def PathSubset(n, m):
    """
    Encode a *maximal* Dyck path from `(0,0)` to `(n,m)` (for `n \\geq m \\geq 0`) as a subset of `\\{0,1,2,..., 2n-1\\}`.

    The encoding is given by indexing horizontal edges by odd numbers and vertical edges by evens.

    The horizontal between `(i,j)` and `(i+1,j)` is indexed by the odd number `2*i+1`.
    The vertical between `(i,j)` and `(i,j+1)` is indexed by the even number `2*j`.

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import PathSubset
        sage: PathSubset(4,0)
        {1, 3, 5, 7}
        sage: PathSubset(4,1)
        {1, 3, 5, 6, 7}
        sage: PathSubset(4,2)
        {1, 2, 3, 5, 6, 7}
        sage: PathSubset(4,3)
        {1, 2, 3, 4, 5, 6, 7}
        sage: PathSubset(4,4)
        {0, 1, 2, 3, 4, 5, 6, 7}
    """
def SetToPath(T):
    """
    Rearrange the encoding for a *maximal* Dyck path (as a set) so that it is a list in the proper order of the edges.

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import PathSubset
        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import SetToPath
        sage: SetToPath(PathSubset(4,0))
        [1, 3, 5, 7]
        sage: SetToPath(PathSubset(4,1))
        [1, 3, 5, 7, 6]
        sage: SetToPath(PathSubset(4,2))
        [1, 3, 2, 5, 7, 6]
        sage: SetToPath(PathSubset(4,3))
        [1, 3, 2, 5, 4, 7, 6]
        sage: SetToPath(PathSubset(4,4))
        [1, 0, 3, 2, 5, 4, 7, 6]
    """
def is_LeeLiZel_allowable(T, n, m, b, c):
    """
    Check if the subset `T` contributes to the computation of the greedy element `x[m,n]` in the rank two `(b,c)`-cluster algebra.

    This uses the conditions of Lee-Li-Zelevinsky's paper [LLZ2014]_.

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import is_LeeLiZel_allowable
        sage: is_LeeLiZel_allowable({1,3,2,5,7,6},4,2,6,6)
        False
        sage: is_LeeLiZel_allowable({1,2,5},3,3,1,1)
        True
    """
def get_green_vertices(C):
    """
    Get the green vertices from a matrix.

    Will go through each column and return
    the ones where no entry is greater than 0.

    INPUT:

    - ``C`` -- the C-matrix to check

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import get_green_vertices
        sage: S = ClusterSeed(['A',4]); S.mutate([1,2,3,2,0,1,2,0,3])
        sage: get_green_vertices(S.c_matrix())
        [0, 3]
    """
def get_red_vertices(C):
    """
    Get the red vertices from a matrix.

    Will go through each column and return
    the ones where no entry is less than 0.

    INPUT:

    - ``C`` -- the C-matrix to check

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.cluster_seed import get_red_vertices
        sage: S = ClusterSeed(['A',4]); S.mutate([1,2,3,2,0,1,2,0,3])
        sage: get_red_vertices(S.c_matrix())
        [1, 2]
    """

class ClusterVariable(FractionFieldElement):
    '''
    This class is a thin wrapper for cluster variables in cluster seeds.

    It provides the extra feature to store if a variable is frozen or not.

    - the associated positive root::

        sage: S = ClusterSeed([\'A\',3])
        sage: for T in S.variable_class_iter():
        ....:     print("{} {}".format(T, T.almost_positive_root()))
        x0 -alpha[1]
        x1 -alpha[2]
        x2 -alpha[3]
        (x1 + 1)/x0 alpha[1]
        (x1^2 + x0*x2 + 2*x1 + 1)/(x0*x1*x2) alpha[1] + alpha[2] + alpha[3]
        (x1 + 1)/x2 alpha[3]
        (x0*x2 + x1 + 1)/(x0*x1) alpha[1] + alpha[2]
        (x0*x2 + 1)/x1 alpha[2]
        (x0*x2 + x1 + 1)/(x1*x2) alpha[2] + alpha[3]
    '''
    def __init__(self, parent, numerator, denominator, coerce: bool = True, reduce: bool = True, mutation_type=None, variable_type=None, xdim: int = 0) -> None:
        """
        Initialize a cluster variable in the same way that elements in the field of rational functions are initialized.

        .. SEEALSO:: :class:`Fraction Field of Multivariate Polynomial Ring`

        TESTS::

            sage: S = ClusterSeed(['A',2])
            sage: for f in S.cluster():
            ....:     print(type(f))
            <class 'sage.combinat.cluster_algebra_quiver.cluster_seed.ClusterVariable'>
            <class 'sage.combinat.cluster_algebra_quiver.cluster_seed.ClusterVariable'>

            sage: S.variable_class()
            [(x0 + x1 + 1)/(x0*x1), (x1 + 1)/x0, (x0 + 1)/x1, x1, x0]
        """
    def almost_positive_root(self):
        '''
        Return the *almost positive root* associated to ``self`` if ``self`` is of finite type.

        EXAMPLES::

            sage: S = ClusterSeed([\'A\',3])
            sage: for T in S.variable_class_iter():
            ....:     print("{} {}".format(T, T.almost_positive_root()))
            x0 -alpha[1]
            x1 -alpha[2]
            x2 -alpha[3]
            (x1 + 1)/x0 alpha[1]
            (x1^2 + x0*x2 + 2*x1 + 1)/(x0*x1*x2) alpha[1] + alpha[2] + alpha[3]
            (x1 + 1)/x2 alpha[3]
            (x0*x2 + x1 + 1)/(x0*x1) alpha[1] + alpha[2]
            (x0*x2 + 1)/x1 alpha[2]
            (x0*x2 + x1 + 1)/(x1*x2) alpha[2] + alpha[3]
        '''
