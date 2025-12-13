from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.functions import lcm as lcm
from sage.arith.misc import binomial as binomial, falling_factorial as falling_factorial
from sage.arith.srange import xsrange as xsrange
from sage.calculus.functional import derivative as derivative
from sage.combinat.integer_vector import integer_vectors_nk_fast_iter as integer_vectors_nk_fast_iter
from sage.combinat.parking_functions import ParkingFunctions as ParkingFunctions
from sage.combinat.set_partition import SetPartitions as SetPartitions
from sage.combinat.vector_partition import IntegerVectorsIterator as IntegerVectorsIterator
from sage.features.four_ti_2 import FourTi2Executable as FourTi2Executable
from sage.functions.log import exp as exp
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.graph import Graph as Graph
from sage.interfaces.singular import singular as singular
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.misc.functional import denominator as denominator, det as det
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc import exists as exists
from sage.misc.misc_c import prod as prod
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.modules.free_module_element import vector as vector
from sage.probability.probability_distribution import GeneralDiscreteDistribution as GeneralDiscreteDistribution
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.symbolic.constants import I as I, pi as pi
from sage.symbolic.ring import SR as SR
from sage.topology.simplicial_complex import SimplicialComplex as SimplicialComplex

class Sandpile(DiGraph):
    """
    Class for Dhar's abelian sandpile model.
    """
    @staticmethod
    def version() -> None:
        """
        The version number of Sage Sandpiles.

        OUTPUT: string

        EXAMPLES::

            sage: Sandpile.version()
            Sage Sandpiles Version 2.4
            sage: S = sandpiles.Complete(3)
            sage: S.version()
            Sage Sandpiles Version 2.4
        """
    @staticmethod
    def help(verbose: bool = True) -> None:
        '''
        List of Sandpile-specific methods (not inherited from :class:`Graph`).
        If ``verbose``, include short descriptions.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: printed string

        EXAMPLES::

            sage: Sandpile.help() # long time
            For detailed help with any method FOO listed below,
            enter "Sandpile.FOO?" or enter "S.FOO?" for any Sandpile S.
            <BLANKLINE>
            all_k_config             -- The constant configuration with all values set to k.
            all_k_div                -- The divisor with all values set to k.
            avalanche_polynomial     -- The avalanche polynomial.
            betti                    -- The Betti table for the homogeneous toppling ideal.
            betti_complexes          -- The support-complexes with non-trivial homology.
            burning_config           -- The minimal burning configuration.
            burning_script           -- A script for the minimal burning configuration.
            canonical_divisor        -- The canonical divisor.
            dict                     -- A dictionary of dictionaries representing a directed graph.
            genus                    -- The genus: (# non-loop edges) - (# vertices) + 1.
            groebner                 -- A Groebner basis for the homogeneous toppling ideal.
            group_gens               -- A minimal list of generators for the sandpile group.
            group_order              -- The size of the sandpile group.
            h_vector                 -- The number of superstable configurations in each degree.
            help                     -- List of Sandpile-specific methods (not inherited from ...Graph...).
            hilbert_function         -- The Hilbert function of the homogeneous toppling ideal.
            ideal                    -- The saturated homogeneous toppling ideal.
            identity                 -- The identity configuration.
            in_degree                -- The in-degree of a vertex or a list of all in-degrees.
            invariant_factors        -- The invariant factors of the sandpile group.
            is_undirected            -- Is the underlying graph undirected?
            jacobian_representatives -- Representatives for the elements of the Jacobian group.
            laplacian                -- The Laplacian matrix of the graph.
            markov_chain             -- The sandpile Markov chain for configurations or divisors.
            max_stable               -- The maximal stable configuration.
            max_stable_div           -- The maximal stable divisor.
            max_superstables         -- The maximal superstable configurations.
            min_recurrents           -- The minimal recurrent elements.
            nonsink_vertices         -- The nonsink vertices.
            nonspecial_divisors      -- The nonspecial divisors.
            out_degree               -- The out-degree of a vertex or a list of all out-degrees.
            picard_representatives   -- Representatives of the divisor classes of degree d in the Picard group.
            points                   -- Generators for the multiplicative group of zeros of the sandpile ideal.
            postulation              -- The postulation number of the toppling ideal.
            recurrents               -- The recurrent configurations.
            reduced_laplacian        -- The reduced Laplacian matrix of the graph.
            reorder_vertices         -- A copy of the sandpile with vertex names permuted.
            resolution               -- A minimal free resolution of the homogeneous toppling ideal.
            ring                     -- The ring containing the homogeneous toppling ideal.
            show                     -- Draw the underlying graph.
            show3d                   -- Draw the underlying graph.
            sink                     -- The sink vertex.
            smith_form               -- The Smith normal form for the Laplacian.
            solve                    -- Approximations of the complex affine zeros of the sandpile ideal.
            stable_configs           -- Generator for all stable configurations.
            stationary_density       -- The stationary density of the sandpile.
            superstables             -- The superstable configurations.
            symmetric_recurrents     -- The symmetric recurrent configurations.
            tutte_polynomial         -- The Tutte polynomial of the underlying graph.
            unsaturated_ideal        -- The unsaturated, homogeneous toppling ideal.
            version                  -- The version number of Sage Sandpiles.
            zero_config              -- The all-zero configuration.
            zero_div                 -- The all-zero divisor.
        '''
    def __init__(self, g, sink=None) -> None:
        """
        Create a sandpile.

        A sandpile is always a weighted graph.

        INPUT:

        - ``g`` -- dictionary for directed multigraph with edges weighted by
          nonnegative integers (see NOTE), a Graph or DiGraph

        - ``sink`` -- (optional) A sink vertex.  Any outgoing edges from the
          designated sink are ignored for the purposes of stabilization.  It is
          assumed that every vertex has a directed path into the sink.  If the
          ``sink`` argument is omitted, the first vertex in the list of the
          Sandpile's vertices is set as the sink.

        OUTPUT: Sandpile

        EXAMPLES:

        Below, ``g`` represents a square with directed, multiple edges
        with three vertices, ``a``, ``b``, ``c``, and ``d``.
        The vertex ``a`` has outgoing edges to itself (weight 2), to
        vertex ``b`` (weight 1), and vertex ``c`` (weight 3), for example.

        ::

            sage: g = {'a': {'a':2, 'b':1, 'c':3}, 'b': {'a':1, 'd':1},
            ....:      'c': {'a':1,'d': 1}, 'd': {'b':1, 'c':1}}
            sage: G = Sandpile(g,'d')

        Here is a square with unweighted edges.  In this example, the graph is
        also undirected. ::

            sage: g = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}
            sage: G = Sandpile(g,3)

        In the following example, multiple edges and loops in the dictionary
        become edge weights in the Sandpile. ::

            sage: s = Sandpile({0:[1,2,3], 1:[0,1,2,2,2], 2:[1,1,0,2,2,2,2]})
            sage: s.laplacian()
            [ 3 -1 -1 -1]
            [-1  4 -3  0]
            [-1 -2  3  0]
            [ 0  0  0  0]
            sage: s.dict()
            {0: {1: 1, 2: 1, 3: 1},
             1: {0: 1, 1: 1, 2: 3},
             2: {0: 1, 1: 2, 2: 4}}

        Sandpiles can be created from Graphs and DiGraphs. ::

            sage: g = DiGraph({0:{1:2,2:4}, 1:{1:3,2:1}, 2:{1:7}}, weighted=True)
            sage: s = Sandpile(g)
            sage: s.dict()
            {0: {1: 2, 2: 4}, 1: {0: 0, 1: 3, 2: 1}, 2: {0: 0, 1: 7}}
            sage: s.sink()
            0
            sage: s = sandpiles.Cycle(4)
            sage: s.laplacian()
            [ 2 -1  0 -1]
            [-1  2 -1  0]
            [ 0 -1  2 -1]
            [-1  0 -1  2]

        .. NOTE::

            Loops are allowed.  There are four admissible input
            formats.  Two of these are dictionaries whose keys are the
            vertex names.  In one, the values are dictionaries with
            keys the names of vertices which are the heads of outgoing
            edges and with values the weights of the edges.  In the
            other format, the values are lists of names of vertices
            which are the heads of the outgoing edges, with weights
            determined by the number of times a name of a vertex
            appears in the list.  Both Graphs and DiGraphs can also be
            used as inputs.

        TESTS::

            sage: S = sandpiles.Complete(4)
            sage: TestSuite(S).run()

        Make sure we cannot make an unweighted sandpile::

            sage: G = Sandpile({0:[]}, 0, weighted=False)
            Traceback (most recent call last):
            ...
            TypeError: ...__init__() got an unexpected keyword argument 'weighted'
        """
    def __copy__(self):
        """
        Make a copy of this sandpile.

        OUTPUT: a new :class:`Sandpile` instance

        EXAMPLES::

            sage: G = sandpiles.Complete(4)
            sage: G_copy = copy(G)
            sage: G_copy == G == G.__copy__()
            True
        """
    def __getattr__(self, name):
        """
        Set certain variables only when called.

        INPUT:

        - ``name`` -- name of an internal method

        EXAMPLES::

            sage: S = sandpiles.Complete(5)
            sage: S.__getattr__('_max_stable')
            {1: 3, 2: 3, 3: 3, 4: 3}
        """
    def show(self, **kwds) -> None:
        """
        Draw the underlying graph.

        INPUT:

        - ``kwds`` -- (optional) arguments passed to the show method for Graph or DiGraph

        EXAMPLES::

            sage: S = Sandpile({0:[], 1:[0,3,4], 2:[0,3,5], 3:[2,5], 4:[1,1], 5:[2,4]})
            sage: S.show()                                                              # needs sage.plot
            sage: S.show(graph_border=True, edge_labels=True)                           # needs sage.plot
        """
    def show3d(self, **kwds) -> None:
        """
        Draw the underlying graph.

        INPUT:

        - ``kwds`` -- (optional) arguments passed to the show method
          for Graph or DiGraph

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: S.show3d()                    # long time                             # needs sage.plot
        """
    def dict(self):
        """
        A dictionary of dictionaries representing a directed graph.

        OUTPUT: dictionary

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.dict()
            {0: {1: 1, 2: 1},
             1: {0: 1, 2: 1, 3: 1},
             2: {0: 1, 1: 1, 3: 1},
             3: {1: 1, 2: 1}}
            sage: S.sink()
            0
        """
    def sink(self):
        """
        The sink vertex.

        OUTPUT: sink vertex

        EXAMPLES::

            sage: G = sandpiles.House()
            sage: G.sink()
            0
            sage: H = sandpiles.Grid(2,2)
            sage: H.sink()
            (0, 0)
            sage: type(H.sink())
            <... 'tuple'>
        """
    def laplacian(self):
        """
        The Laplacian matrix of the graph.

        Its *rows* encode the vertex firing rules.

        OUTPUT: matrix

        EXAMPLES::

            sage: G = sandpiles.Diamond()
            sage: G.laplacian()
            [ 2 -1 -1  0]
            [-1  3 -1 -1]
            [-1 -1  3 -1]
            [ 0 -1 -1  2]

        .. WARNING::

            The function ``laplacian_matrix`` should be avoided.  It returns the
            indegree version of the Laplacian.
        """
    def reduced_laplacian(self):
        """
        The reduced Laplacian matrix of the graph.

        OUTPUT: matrix

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.laplacian()
            [ 2 -1 -1  0]
            [-1  3 -1 -1]
            [-1 -1  3 -1]
            [ 0 -1 -1  2]
            sage: S.reduced_laplacian()
            [ 3 -1 -1]
            [-1  3 -1]
            [-1 -1  2]

        .. NOTE::

            This is the Laplacian matrix with the row and column indexed by the
            sink vertex removed.
        """
    def group_order(self):
        """
        The size of the sandpile group.

        OUTPUT: integer

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: S.group_order()
            11
        """
    def max_stable(self):
        """
        The maximal stable configuration.

        OUTPUT: SandpileConfig (the maximal stable configuration)

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: S.max_stable()
            {1: 1, 2: 2, 3: 2, 4: 1}
        """
    def max_stable_div(self):
        """
        The maximal stable divisor.

        OUTPUT:

        SandpileDivisor (the maximal stable divisor)

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.max_stable_div()
            {0: 1, 1: 2, 2: 2, 3: 1}
            sage: s.out_degree()
            {0: 2, 1: 3, 2: 3, 3: 2}
        """
    def out_degree(self, v=None):
        """
        The out-degree of a vertex or a list of all out-degrees.

        INPUT:

        - ``v`` -- (optional) vertex name

        OUTPUT: integer or dict

        EXAMPLES::

            sage: s = sandpiles.House()
            sage: s.out_degree()
            {0: 2, 1: 2, 2: 3, 3: 3, 4: 2}
            sage: s.out_degree(2)
            3
        """
    def in_degree(self, v=None):
        """
        The in-degree of a vertex or a list of all in-degrees.

        INPUT:

        - ``v`` -- (optional) vertex name

        OUTPUT: integer or dict

        EXAMPLES::

            sage: s = sandpiles.House()
            sage: s.in_degree()
            {0: 2, 1: 2, 2: 3, 3: 3, 4: 2}
            sage: s.in_degree(2)
            3
        """
    def burning_config(self):
        """
        The minimal burning configuration.

        OUTPUT:

        dict (configuration)

        EXAMPLES::

            sage: g = {0:{},1:{0:1,3:1,4:1},2:{0:1,3:1,5:1},
            ....:      3:{2:1,5:1},4:{1:1,3:1},5:{2:1,3:1}}
            sage: S = Sandpile(g,0)
            sage: S.burning_config()
            {1: 2, 2: 0, 3: 1, 4: 1, 5: 0}
            sage: S.burning_config().values()
            [2, 0, 1, 1, 0]
            sage: S.burning_script()
            {1: 1, 2: 3, 3: 5, 4: 1, 5: 4}
            sage: script = S.burning_script().values()
            sage: script
            [1, 3, 5, 1, 4]
            sage: matrix(script)*S.reduced_laplacian()
            [2 0 1 1 0]

        .. NOTE::

            The burning configuration and script are computed using a modified
            version of Speer's script algorithm.  This is a generalization to
            directed multigraphs of Dhar's burning algorithm.

            A *burning configuration* is a nonnegative integer-linear
            combination of the rows of the reduced Laplacian matrix having
            nonnegative entries and such that every vertex has a path from some
            vertex in its support.  The corresponding *burning script* gives
            the integer-linear combination needed to obtain the burning
            configuration.  So if `b` is the burning configuration, `\\sigma`
            is its script, and `\\tilde{L}` is the reduced Laplacian,
            then `\\sigma\\cdot \\tilde{L} = b`.  The *minimal burning
            configuration* is the one with the minimal script (its
            components are no larger than the components of any other
            script for a burning configuration).

            The following are equivalent for a configuration `c` with burning
            configuration `b` having script `\\sigma`:

             - `c` is recurrent;
             - `c+b` stabilizes to `c`;
             - the firing vector for the stabilization of `c+b` is `\\sigma`.
        """
    def burning_script(self):
        """
        A script for the minimal burning configuration.

        OUTPUT: dictionary

        EXAMPLES::

            sage: g = {0:{},1:{0:1,3:1,4:1},2:{0:1,3:1,5:1},
            ....:      3:{2:1,5:1},4:{1:1,3:1},5:{2:1,3:1}}
            sage: S = Sandpile(g,0)
            sage: S.burning_config()
            {1: 2, 2: 0, 3: 1, 4: 1, 5: 0}
            sage: S.burning_config().values()
            [2, 0, 1, 1, 0]
            sage: S.burning_script()
            {1: 1, 2: 3, 3: 5, 4: 1, 5: 4}
            sage: script = S.burning_script().values()
            sage: script
            [1, 3, 5, 1, 4]
            sage: matrix(script)*S.reduced_laplacian()
            [2 0 1 1 0]

        .. NOTE::

            The burning configuration and script are computed using a modified
            version of Speer's script algorithm.  This is a generalization to
            directed multigraphs of Dhar's burning algorithm.

            A *burning configuration* is a nonnegative integer-linear
            combination of the rows of the reduced Laplacian matrix having
            nonnegative entries and such that every vertex has a path from some
            vertex in its support.  The corresponding *burning script* gives the
            integer-linear combination needed to obtain the burning configuration.
            So if `b` is the burning configuration, `s` is its script, and
            `L_{\\mathrm{red}}` is the reduced Laplacian, then `s\\cdot
            L_{\\mathrm{red}}= b`.  The *minimal burning configuration* is the one
            with the minimal script (its components are no larger than the
            components of any other script
            for a burning configuration).

            The following are equivalent for a configuration `c` with burning
            configuration `b` having script `s`:

             - `c` is recurrent;
             - `c+b` stabilizes to `c`;
             - the firing vector for the stabilization of `c+b` is `s`.
        """
    def nonsink_vertices(self):
        """
        The nonsink vertices.

        OUTPUT: list of vertices

        EXAMPLES::

            sage: s = sandpiles.Grid(2,3)
            sage: s.nonsink_vertices()
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
        """
    def all_k_config(self, k):
        """
        The constant configuration with all values set to `k`.

        INPUT:

        - ``k`` -- integer

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.all_k_config(7)
            {1: 7, 2: 7, 3: 7}
        """
    def zero_config(self):
        """
        The all-zero configuration.

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.zero_config()
            {1: 0, 2: 0, 3: 0}
        """
    def identity(self, verbose: bool = True):
        """
        The identity configuration.

        If ``verbose`` is ``False``, the
        configuration is converted to a list of integers.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: SandpileConfig or a list of integers

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.identity()
            {1: 2, 2: 2, 3: 0}
            sage: s.identity(False)
            [2, 2, 0]
            sage: s.identity() & s.max_stable() == s.max_stable()
            True
        """
    def recurrents(self, verbose: bool = True):
        """
        The recurrent configurations. If ``verbose`` is ``False``, the
        configurations are converted to lists of integers.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: list of recurrent configurations

        EXAMPLES::

            sage: r = Sandpile(graphs.HouseXGraph(),0).recurrents()
            sage: r[:3]
            [{1: 2, 2: 3, 3: 3, 4: 1},
             {1: 1, 2: 3, 3: 3, 4: 0},
             {1: 1, 2: 3, 3: 3, 4: 1}]
            sage: sandpiles.Complete(4).recurrents(False)                               # needs sage.combinat
            [[2, 2, 2],
             [2, 2, 1],
             [2, 1, 2],
             [1, 2, 2],
             [2, 2, 0],
             [2, 0, 2],
             [0, 2, 2],
             [2, 1, 1],
             [1, 2, 1],
             [1, 1, 2],
             [2, 1, 0],
             [2, 0, 1],
             [1, 2, 0],
             [1, 0, 2],
             [0, 2, 1],
             [0, 1, 2]]
            sage: sandpiles.Cycle(4).recurrents(False)
            [[1, 1, 1], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
        """
    def superstables(self, verbose: bool = True):
        """
        The superstable configurations.  If ``verbose`` is ``False``, the
        configurations are converted to lists of integers.  Superstables for
        undirected graphs are also known as ``G-parking functions``.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: list of SandpileConfig

        EXAMPLES::

            sage: sp = Sandpile(graphs.HouseXGraph(),0).superstables()
            sage: sp[:3]
            [{1: 0, 2: 0, 3: 0, 4: 0},
             {1: 1, 2: 0, 3: 0, 4: 1},
             {1: 1, 2: 0, 3: 0, 4: 0}]
            sage: sandpiles.Complete(4).superstables(False)                             # needs sage.combinat
            [[0, 0, 0],
             [0, 0, 1],
             [0, 1, 0],
             [1, 0, 0],
             [0, 0, 2],
             [0, 2, 0],
             [2, 0, 0],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 0],
             [0, 1, 2],
             [0, 2, 1],
             [1, 0, 2],
             [1, 2, 0],
             [2, 0, 1],
             [2, 1, 0]]
            sage: sandpiles.Cycle(4).superstables(False)
            [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """
    def group_gens(self, verbose: bool = True) -> list:
        """
        A minimal list of generators for the sandpile group.

        If ``verbose`` is ``False``
        then the generators are represented as lists of integers.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT:

        list of SandpileConfig
        (or of lists of integers if ``verbose`` is ``False``)

        EXAMPLES::

            sage: s = sandpiles.Cycle(5)
            sage: s.group_gens()
            [{1: 0, 2: 1, 3: 1, 4: 1}]
            sage: s.group_gens()[0].order()
            5
            sage: s = sandpiles.Complete(5)
            sage: s.group_gens(False)
            [[2, 3, 2, 2], [2, 2, 3, 2], [2, 2, 2, 3]]
            sage: [i.order() for i in s.group_gens()]
            [5, 5, 5]
            sage: s.invariant_factors()
            [1, 5, 5, 5]
        """
    def genus(self):
        """
        The genus: (# non-loop edges) - (# vertices) + 1.

        This is only defined for undirected graphs.

        OUTPUT: integer

        EXAMPLES::

            sage: sandpiles.Complete(4).genus()
            3
            sage: sandpiles.Cycle(5).genus()
            1
        """
    def is_undirected(self):
        """
        Is the underlying graph undirected?  ``True`` if `(u,v)` is and edge if
        and only if `(v,u)` is an edge, each edge with the same weight.

        OUTPUT: boolean

        EXAMPLES::

            sage: sandpiles.Complete(4).is_undirected()
            True
            sage: s = Sandpile({0:[1,2], 1:[0,2], 2:[0]}, 0)
            sage: s.is_undirected()
            False
        """
    def min_recurrents(self, verbose: bool = True):
        """
        The minimal recurrent elements.  If the underlying graph is
        undirected, these are the recurrent elements of least degree.
        If ``verbose`` is ``False``, the configurations are converted
        to lists of integers.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: list of SandpileConfig

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.recurrents(False)
            [[2, 2, 1],
             [2, 2, 0],
             [1, 2, 0],
             [2, 0, 1],
             [0, 2, 1],
             [2, 1, 0],
             [1, 2, 1],
             [2, 1, 1]]
            sage: s.min_recurrents(False)
            [[1, 2, 0], [2, 0, 1], [0, 2, 1], [2, 1, 0]]
            sage: [i.deg() for i in s.recurrents()]
            [5, 4, 3, 3, 3, 3, 4, 4]
        """
    def max_superstables(self, verbose: bool = True):
        """
        The maximal superstable configurations.  If the underlying graph is
        undirected, these are the superstables of highest degree.  If
        ``verbose`` is ``False``, the configurations are converted to lists of
        integers.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: tuple of SandpileConfig

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.superstables(False)
            [[0, 0, 0],
             [0, 0, 1],
             [1, 0, 1],
             [0, 2, 0],
             [2, 0, 0],
             [0, 1, 1],
             [1, 0, 0],
             [0, 1, 0]]
            sage: s.max_superstables(False)
            [[1, 0, 1], [0, 2, 0], [2, 0, 0], [0, 1, 1]]
            sage: s.h_vector()
            [1, 3, 4]
        """
    def tutte_polynomial(self):
        """
        The Tutte polynomial of the underlying graph.
        Only defined for undirected sandpile graphs.

        OUTPUT: polynomial

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: s.tutte_polynomial()
            x^3 + y^3 + 3*x^2 + 4*x*y + 3*y^2 + 2*x + 2*y
            sage: s.tutte_polynomial().subs(x=1)
            y^3 + 3*y^2 + 6*y + 6
            sage: s.tutte_polynomial().subs(x=1).coefficients() == s.h_vector()         # needs sage.combinat
            True
        """
    def avalanche_polynomial(self, multivariable: bool = True):
        """
        The avalanche polynomial.  See NOTE for details.

        INPUT:

        - ``multivariable`` -- boolean (default: ``True``)

        OUTPUT: polynomial

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: s.avalanche_polynomial()                                              # needs sage.combinat
            9*x0*x1*x2 + 2*x0*x1 + 2*x0*x2 + 2*x1*x2 + 3*x0 + 3*x1 + 3*x2 + 24
            sage: s.avalanche_polynomial(False)                                         # needs sage.combinat
            9*x0^3 + 6*x0^2 + 9*x0 + 24

        .. NOTE::

            For each nonsink vertex `v`, let `x_v` be an indeterminate.
            If `(r,v)` is a pair consisting of a recurrent `r` and nonsink
            vertex `v`, then for each nonsink vertex `w`, let `n_w` be the
            number of times vertex `w` fires in the stabilization of `r + v`.
            Let `M(r,v)` be the monomial `\\prod_w x_w^{n_w}`, i.e., the exponent
            records the vector of `n_w` as `w` ranges over the nonsink vertices.
            The avalanche polynomial is then the sum of `M(r,v)` as `r` ranges
            over the recurrents and `v` ranges over the nonsink vertices.  If
            ``multivariable`` is ``False``, then set all the indeterminates equal
            to each other (and, thus, only count the number of vertex firings in the
            stabilizations, forgetting which particular vertices fired).
        """
    def nonspecial_divisors(self, verbose: bool = True) -> list:
        '''
        The nonspecial divisors. Only for undirected graphs.  (See NOTE.)

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: list (of divisors)

        EXAMPLES::

            sage: # needs sage.combinat
            sage: S = sandpiles.Complete(4)
            sage: ns = S.nonspecial_divisors()
            sage: D = ns[0]
            sage: D.values()                                                            # needs sage.symbolic
            [-1, 0, 1, 2]
            sage: D.deg()                                                               # needs sage.symbolic
            2
            sage: [i.effective_div() for i in ns]
            [[], [], [], [], [], []]

        .. NOTE::

            The "nonspecial divisors" are those divisors of degree
            `g-1` with empty linear system.  The term is only defined
            for undirected graphs.  Here, `g = |E| - |V| + 1` is the
            genus of the graph (not counting loops as part of `|E|`).
            If ``verbose`` is ``False``, the divisors are converted to
            lists of integers.

        .. WARNING::

            The underlying graph must be undirected.
        '''
    def canonical_divisor(self):
        """
        The canonical divisor.  This is the divisor with `\\deg(v)-2` grains of
        sand on each vertex (not counting loops).  Only for undirected graphs.

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Complete(4)
            sage: S.canonical_divisor()
            {0: 1, 1: 1, 2: 1, 3: 1}
            sage: s = Sandpile({0:[1,1],1:[0,0,1,1,1]},0)
            sage: s.canonical_divisor()  # loops are disregarded
            {0: 0, 1: 0}

        .. WARNING::

            The underlying graph must be undirected.
        """
    def invariant_factors(self):
        """
        The invariant factors of the sandpile group.

        OUTPUT: list of integers

        EXAMPLES::

            sage: s = sandpiles.Grid(2,2)
            sage: s.invariant_factors()
            [1, 1, 8, 24]
        """
    def h_vector(self):
        """
        The number of superstable configurations in each degree.  Equivalently,
        this is the list of first differences of the Hilbert function of the
        (homogeneous) toppling ideal.

        OUTPUT: list of nonnegative integers

        EXAMPLES::

            sage: s = sandpiles.Grid(2,2)
            sage: s.hilbert_function()
            [1, 5, 15, 35, 66, 106, 146, 178, 192]
            sage: s.h_vector()
            [1, 4, 10, 20, 31, 40, 40, 32, 14]
        """
    def hilbert_function(self):
        """
        The Hilbert function of the homogeneous toppling ideal.

        OUTPUT: list of nonnegative integers

        EXAMPLES::

            sage: s = sandpiles.Wheel(5)
            sage: s.hilbert_function()
            [1, 5, 15, 31, 45]
            sage: s.h_vector()
            [1, 4, 10, 16, 14]
        """
    def postulation(self):
        """
        The postulation number of the toppling ideal.  This is the
        largest weight of a superstable configuration of the graph.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: s.postulation()                                                       # needs sage.combinat
            3
        """
    def smith_form(self) -> list:
        """
        The Smith normal form for the Laplacian.  In detail: a list of integer
        matrices `D, U, V` such that `ULV = D` where `L` is the transpose of the
        Laplacian, `D` is diagonal, and  `U` and `V` are invertible over the
        integers.

        OUTPUT: list of integer matrices

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D,U,V = s.smith_form()
            sage: D
            [1 0 0 0]
            [0 4 0 0]
            [0 0 4 0]
            [0 0 0 0]
            sage: U*s.laplacian()*V == D  # Laplacian symmetric => transpose not necessary
            True
        """
    def reorder_vertices(self):
        """
        A copy of the sandpile with vertex names permuted.

        After reordering, vertex `u` comes before vertex `v` in the
        list of vertices if `u` is closer to the sink.

        OUTPUT: Sandpile

        EXAMPLES::

            sage: S = Sandpile({0:[1], 2:[0,1], 1:[2]})
            sage: S.dict()
            {0: {1: 1}, 1: {2: 1}, 2: {0: 1, 1: 1}}
            sage: T = S.reorder_vertices()

        The vertices 1 and 2 have been swapped::

            sage: T.dict()
            {0: {1: 1}, 1: {0: 1, 2: 1}, 2: {0: 1}}
        """
    def jacobian_representatives(self, verbose: bool = True):
        """
        Representatives for the elements of the Jacobian group. If ``verbose``
        is ``False``, then lists representing the divisors are returned.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: list of SandpileDivisor (or of lists representing divisors)

        EXAMPLES:

        For an undirected graph, divisors of the form ``s - deg(s)*sink`` as
        ``s`` varies over the superstables forms a distinct set of
        representatives for the Jacobian group.::

            sage: s = sandpiles.Complete(3)
            sage: s.superstables(False)                                                 # needs sage.combinat
            [[0, 0], [0, 1], [1, 0]]
            sage: s.jacobian_representatives(False)                                     # needs sage.combinat
            [[0, 0, 0], [-1, 0, 1], [-1, 1, 0]]

        If the graph is directed, the representatives described above may by
        equivalent modulo the rowspan of the Laplacian matrix::

            sage: s = Sandpile({0: {1: 1, 2: 2}, 1: {0: 2, 2: 4}, 2: {0: 4, 1: 2}},0)
            sage: s.group_order()
            28
            sage: s.jacobian_representatives()                                          # needs sage.symbolic
            [{0: -5, 1: 3, 2: 2}, {0: -4, 1: 3, 2: 1}]

        Let `\\tau` be the nonnegative generator of the kernel of the transpose of
        the Laplacian, and let `\\tau_s` be its sink component, then the sandpile
        group is isomorphic to the direct sum of the cyclic group of order
        `\\tau_s` and the Jacobian group.  In the example above, we have::

            sage: s.laplacian().left_kernel()
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [14  5  8]

        .. NOTE::

            The Jacobian group is the set of all divisors of degree
            zero modulo the integer rowspan of the Laplacian matrix.
        """
    def picard_representatives(self, d, verbose: bool = True):
        """
        Representatives of the divisor classes of degree `d` in the Picard group.

        (Also see the documentation for ``jacobian_representatives``.)

        INPUT:

        - ``d`` -- integer

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: slist of SandpileDivisors (or lists representing divisors)

        EXAMPLES::

            sage: s = sandpiles.Complete(3)
            sage: s.superstables(False)                                                 # needs sage.combinat
            [[0, 0], [0, 1], [1, 0]]
            sage: s.jacobian_representatives(False)                                     # needs sage.combinat
            [[0, 0, 0], [-1, 0, 1], [-1, 1, 0]]
            sage: s.picard_representatives(3,False)                                     # needs sage.combinat
            [[3, 0, 0], [2, 0, 1], [2, 1, 0]]
        """
    def stable_configs(self, smax=None) -> Generator[Incomplete]:
        """
        Generator for all stable configurations.

        If ``smax`` is provided, then the generator gives all stable
        configurations less than or equal to ``smax``.  If ``smax``
        does not represent a stable configuration, then each component
        of ``smax`` is replaced by the corresponding component of the
        maximal stable configuration.

        INPUT:

        - ``smax`` -- (optional) SandpileConfig or list representing a SandpileConfig

        OUTPUT: generator for all stable configurations

        EXAMPLES::

            sage: s = sandpiles.Complete(3)
            sage: a = s.stable_configs()
            sage: next(a)                                                               # needs sage.combinat
            {1: 0, 2: 0}
            sage: [i.values() for i in a]                                               # needs sage.combinat
            [[0, 1], [1, 0], [1, 1]]
            sage: b = s.stable_configs([1,0])
            sage: list(b)                                                               # needs sage.combinat
            [{1: 0, 2: 0}, {1: 1, 2: 0}]
        """
    def markov_chain(self, state, distrib=None) -> Generator[Incomplete]:
        """
        The sandpile Markov chain for configurations or divisors.
        The chain starts at ``state``.  See NOTE for details.

        INPUT:

        - ``state`` -- SandpileConfig, SandpileDivisor, or list representing
          one of these

        - ``distrib`` -- (optional) list of nonnegative numbers summing to 1
          (representing a prob. dist.)

        OUTPUT: generator for Markov chain (see NOTE)

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: m = s.markov_chain([0,0,0])
            sage: next(m)          # random
            {1: 0, 2: 0, 3: 0}
            sage: next(m).values() # random
            [0, 0, 0]
            sage: next(m).values() # random
            [0, 0, 0]
            sage: next(m).values() # random
            [0, 0, 0]
            sage: next(m).values() # random
            [0, 1, 0]
            sage: next(m).values() # random
            [0, 2, 0]
            sage: next(m).values() # random
            [0, 2, 1]
            sage: next(m).values() # random
            [1, 2, 1]
            sage: next(m).values() # random
            [2, 2, 1]
            sage: m = s.markov_chain(s.zero_div(), [0.1,0.1,0.1,0.7])
            sage: next(m).values() # random
            [0, 0, 0, 1]
            sage: next(m).values() # random
            [0, 0, 1, 1]
            sage: next(m).values() # random
            [0, 0, 1, 2]
            sage: next(m).values() # random
            [1, 1, 2, 0]
            sage: next(m).values() # random
            [1, 1, 2, 1]
            sage: next(m).values() # random
            [1, 1, 2, 2]
            sage: next(m).values() # random
            [1, 1, 2, 3]
            sage: next(m).values() # random
            [1, 1, 2, 4]
            sage: next(m).values() # random
            [1, 1, 3, 4]

        .. NOTE::

            The ``closed sandpile Markov chain`` has state space
            consisting of the configurations on a sandpile.  It
            transitions from a state by choosing a vertex at random
            (according to the probability distribution ``distrib``),
            dropping a grain of sand at that vertex, and stabilizing.
            If the chosen vertex is the sink, the chain stays at the
            current state.

            The ``open sandpile Markov chain`` has state space
            consisting of the recurrent elements, i.e., the state
            space is the sandpile group.  It transitions from the
            configuration `c` by choosing a vertex `v` at random
            according to ``distrib``.  The next state is the
            stabilization of `c+v`.  If `v` is the sink vertex, then
            the stabilization of `c+v` is defined to be `c`.

            Note that in either case, if ``distrib`` is specified, its
            length is equal to the total number of vertices (including
            the sink).

        REFERENCES:

        - [Lev2014]_
        """
    def stationary_density(self):
        """
        The stationary density of the sandpile.

        OUTPUT: rational number

        EXAMPLES::

            sage: s = sandpiles.Complete(3)
            sage: s.stationary_density()
            10/9

            sage: # needs sage.combinat
            sage: s = Sandpile(digraphs.DeBruijn(2,2),'00')
            sage: s.stationary_density()
            9/8

        .. NOTE::

            The stationary density of a sandpile is the sum `\\sum_c
            (\\deg(c) + \\deg(s))` where `\\deg(s)` is the degree of the
            sink and the sum is over all recurrent configurations.

        REFERENCES:

        - [Lev2014]_
        """
    def all_k_div(self, k):
        """
        The divisor with all values set to `k`.

        INPUT:

        - ``k`` -- integer

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: S.all_k_div(7)
            {0: 7, 1: 7, 2: 7, 3: 7, 4: 7}
        """
    def zero_div(self):
        """
        The all-zero divisor.

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: S.zero_div()
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        """
    def betti_complexes(self):
        """
        The support-complexes with non-trivial homology.  (See NOTE.)

        OUTPUT: list (of pairs [divisors, corresponding simplicial complex])

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: S = Sandpile({0:{},1:{0: 1, 2: 1, 3: 4},2:{3: 5},3:{1: 1, 2: 1}},0)
            sage: p = S.betti_complexes()
            sage: p[0]
            [{0: -8, 1: 5, 2: 4, 3: 1},
             Simplicial complex with vertex set (1, 2, 3) and facets {(3,), (1, 2)}]
            sage: S.resolution()                                                        # needs sage.libs.singular
            'R^1 <-- R^5 <-- R^5 <-- R^1'
            sage: S.betti()                                                             # needs sage.libs.singular
                       0     1     2     3
            ------------------------------
                0:     1     -     -     -
                1:     -     5     5     -
                2:     -     -     -     1
            ------------------------------
            total:     1     5     5     1
            sage: len(p)
            11
            sage: p[0][1].homology()
            {0: Z, 1: 0}
            sage: p[-1][1].homology()
            {0: 0, 1: 0, 2: Z}

        .. NOTE::

            A ``support-complex`` is the simplicial complex formed from the
            supports of the divisors in a linear system.
        """
    def unsaturated_ideal(self):
        """
        The unsaturated, homogeneous toppling ideal.

        OUTPUT: ideal

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.unsaturated_ideal().gens()
            [x1^3 - x3*x2*x0, x2^3 - x3*x1*x0, x3^2 - x2*x1]
            sage: S.ideal().gens()                                                      # needs sage.libs.singular
            [x2*x1 - x0^2, x3^2 - x0^2, x1^3 - x3*x2*x0,
             x3*x1^2 - x2^2*x0, x2^3 - x3*x1*x0, x3*x2^2 - x1^2*x0]
        """
    def ideal(self, gens: bool = False):
        """
        The saturated homogeneous toppling ideal.  If ``gens`` is ``True``, the
        generators for the ideal are returned instead.

        INPUT:

        - ``gens`` -- boolean (default: ``False``)

        OUTPUT: ideal or, optionally, the generators of an ideal

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.ideal()                                                             # needs sage.libs.singular
            Ideal (x2*x1 - x0^2, x3^2 - x0^2, x1^3 - x3*x2*x0,
                   x3*x1^2 - x2^2*x0, x2^3 - x3*x1*x0, x3*x2^2 - x1^2*x0)
             of Multivariate Polynomial Ring in x3, x2, x1, x0 over Rational Field
            sage: S.ideal(True)                                                         # needs sage.libs.singular
            [x2*x1 - x0^2, x3^2 - x0^2, x1^3 - x3*x2*x0,
             x3*x1^2 - x2^2*x0, x2^3 - x3*x1*x0, x3*x2^2 - x1^2*x0]
            sage: S.ideal().gens()  # another way to get the generators                 # needs sage.libs.singular
            [x2*x1 - x0^2, x3^2 - x0^2, x1^3 - x3*x2*x0,
             x3*x1^2 - x2^2*x0, x2^3 - x3*x1*x0, x3*x2^2 - x1^2*x0]
        """
    def ring(self):
        """
        The ring containing the homogeneous toppling ideal.

        OUTPUT: ring

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.ring()
            Multivariate Polynomial Ring in x3, x2, x1, x0 over Rational Field
            sage: S.ring().gens()
            (x3, x2, x1, x0)

        .. NOTE::

            The indeterminate ``xi`` corresponds to the `i`-th vertex as listed my
            the method ``vertices``. The term-ordering is degrevlex with
            indeterminates ordered according to their distance from the sink (larger
            indeterminates are further from the sink).
        """
    def resolution(self, verbose: bool = False):
        """
        A minimal free resolution of the homogeneous toppling ideal.

        If ``verbose`` is ``True``, then all of the mappings are
        returned.  Otherwise, the resolution is summarized.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``)

        OUTPUT: free resolution of the toppling ideal

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: S = Sandpile({0: {}, 1: {0: 1, 2: 1, 3: 4}, 2: {3: 5}, 3: {1: 1, 2: 1}},0)
            sage: S.resolution()  # a Gorenstein sandpile graph
            'R^1 <-- R^5 <-- R^5 <-- R^1'
            sage: S.resolution(True)
            [
            [ x1^2 - x3*x0 x3*x1 - x2*x0  x3^2 - x2*x1  x2*x3 - x0^2  x2^2 - x1*x0],
            <BLANKLINE>
            [ x3  x2   0  x0   0]  [ x2^2 - x1*x0]
            [-x1 -x3  x2   0 -x0]  [-x2*x3 + x0^2]
            [ x0  x1   0  x2   0]  [-x3^2 + x2*x1]
            [  0   0 -x1 -x3  x2]  [x3*x1 - x2*x0]
            [  0   0  x0  x1 -x3], [ x1^2 - x3*x0]
            ]
            sage: r = S.resolution(True)
            sage: r[0]*r[1]
            [0 0 0 0 0]
            sage: r[1]*r[2]
            [0]
            [0]
            [0]
            [0]
            [0]
        """
    def groebner(self):
        """
        A Groebner basis for the homogeneous toppling ideal.  It is computed
        with respect to the standard sandpile ordering (see ``ring``).

        OUTPUT: Groebner basis

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.groebner()                                                          # needs sage.libs.singular
            [x3*x2^2 - x1^2*x0, x2^3 - x3*x1*x0, x3*x1^2 - x2^2*x0,
             x1^3 - x3*x2*x0, x3^2 - x0^2, x2*x1 - x0^2]
        """
    def betti(self, verbose: bool = True):
        """
        The Betti table for the homogeneous toppling ideal.  If
        ``verbose`` is ``True``, it prints the standard Betti table, otherwise,
        it returns a less formatted table.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: Betti numbers for the sandpile

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.betti()                                                             # needs sage.libs.singular
                       0     1     2     3
            ------------------------------
                0:     1     -     -     -
                1:     -     2     -     -
                2:     -     4     9     4
            ------------------------------
            total:     1     6     9     4
            sage: S.betti(False)                                                        # needs sage.libs.singular
            [1, 6, 9, 4]
        """
    def solve(self):
        """
        Approximations of the complex affine zeros of the sandpile
        ideal.

        OUTPUT: list of complex numbers

        EXAMPLES::

            sage: S = Sandpile({0: {}, 1: {2: 2}, 2: {0: 4, 1: 1}}, 0)
            sage: Z = S.solve(); Z                                                      # needs sage.libs.singular
            [[-0.707107000000000 + 0.707107000000000*I,
              0.707107000000000 - 0.707107000000000*I],
             [-0.707107000000000 - 0.707107000000000*I,
              0.707107000000000 + 0.707107000000000*I],
             [-I, -I],
             [I, I],
             [0.707107000000000 + 0.707107000000000*I,
              -0.707107000000000 - 0.707107000000000*I],
             [0.707107000000000 - 0.707107000000000*I,
              -0.707107000000000 + 0.707107000000000*I],
             [1, 1],
             [-1, -1]]
            sage: len(Z)                                                                # needs sage.libs.singular
            8
            sage: S.group_order()
            8

        .. NOTE::

            The solutions form a multiplicative group isomorphic to the sandpile
            group.  Generators for this group are given exactly by ``points()``.
        """
    def points(self):
        """
        Generators for the multiplicative group of zeros of the sandpile
        ideal.

        OUTPUT: list of complex numbers

        EXAMPLES:

        The sandpile group in this example is cyclic, and hence there is a
        single generator for the group of solutions.

        ::

            sage: S = sandpiles.Complete(4)
            sage: S.points()                                                            # needs sage.symbolic
            [[-I, I, 1], [-I, 1, I]]
        """
    def symmetric_recurrents(self, orbits):
        """
        The symmetric recurrent configurations.

        INPUT:

        - ``orbits`` -- list of lists partitioning the vertices

        OUTPUT: list of recurrent configurations

        EXAMPLES::

            sage: S = Sandpile({0: {},
            ....:              1: {0: 1, 2: 1, 3: 1},
            ....:              2: {1: 1, 3: 1, 4: 1},
            ....:              3: {1: 1, 2: 1, 4: 1},
            ....:              4: {2: 1, 3: 1}})
            sage: S.symmetric_recurrents([[1],[2,3],[4]])
            [{1: 2, 2: 2, 3: 2, 4: 1}, {1: 2, 2: 2, 3: 2, 4: 0}]
            sage: S.recurrents()
            [{1: 2, 2: 2, 3: 2, 4: 1},
             {1: 2, 2: 2, 3: 2, 4: 0},
             {1: 2, 2: 1, 3: 2, 4: 0},
             {1: 2, 2: 2, 3: 0, 4: 1},
             {1: 2, 2: 0, 3: 2, 4: 1},
             {1: 2, 2: 2, 3: 1, 4: 0},
             {1: 2, 2: 1, 3: 2, 4: 1},
             {1: 2, 2: 2, 3: 1, 4: 1}]

        .. NOTE::

            The user is responsible for ensuring that the list of
            orbits comes from a group of symmetries of the underlying
            graph.
        """

class SandpileConfig(dict):
    """
    Class for configurations on a sandpile.
    """
    @staticmethod
    def help(verbose: bool = True) -> None:
        '''
        List of SandpileConfig methods.

        If ``verbose``, include short descriptions.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: printed string

        EXAMPLES::

            sage: SandpileConfig.help()
            Shortcuts for SandpileConfig operations:
            ~c    -- stabilize
            c & d -- add and stabilize
            c * c -- add and find equivalent recurrent
            c^k   -- add k times and find equivalent recurrent
                     (taking inverse if k is negative)
            <BLANKLINE>
            For detailed help with any method FOO listed below,
            enter "SandpileConfig.FOO?" or enter "c.FOO?" for any SandpileConfig c.
            <BLANKLINE>
            add_random             -- Add one grain of sand to a random vertex.
            burst_size             -- The burst size of the configuration with respect to the given vertex.
            deg                    -- The degree of the configuration.
            dualize                -- The difference with the maximal stable configuration.
            equivalent_recurrent   -- The recurrent configuration equivalent to the given configuration.
            equivalent_superstable -- The equivalent superstable configuration.
            fire_script            -- Fire the given script.
            fire_unstable          -- Fire all unstable vertices.
            fire_vertex            -- Fire the given vertex.
            help                   -- List of SandpileConfig methods.
            is_recurrent           -- Return whether the configuration is recurrent.
            is_stable              -- Return whether the configuration is stable.
            is_superstable         -- Return whether the configuration is superstable.
            is_symmetric           -- Return whether the configuration is symmetric.
            order                  -- The order of the equivalent recurrent element.
            sandpile               -- The configuration\'s underlying sandpile.
            show                   -- Show the configuration.
            stabilize              -- The stabilized configuration.
            support                -- The vertices containing sand.
            unstable               -- The unstable vertices.
            values                 -- The values of the configuration as a list.
        '''
    def __init__(self, S, c) -> None:
        """
        Create a configuration on a Sandpile.

        INPUT:

        - ``S`` -- Sandpile

        - ``c`` -- dictionary or list representing a configuration

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = SandpileConfig(S,[1,1,0])
            sage: 3*c
            {1: 3, 2: 3, 3: 0}
            sage: ~(3*c)  # stabilization
            {1: 2, 2: 2, 3: 0}
        """
    def __deepcopy__(self, memo):
        """
        Overrides the deepcopy method for dict.

        INPUT:

        - ``memo`` -- (optional) dict

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = SandpileConfig(S,[1,1,0])
            sage: d = deepcopy(c)
            sage: d[1] += 10
            sage: c
            {1: 1, 2: 1, 3: 0}
            sage: d
            {1: 11, 2: 1, 3: 0}
        """
    __dict__: Incomplete
    def __setitem__(self, key, item) -> None:
        """
        Overrides the setitem method for dict.

        INPUT:

        - ``key``, ``item`` -- objects

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [4,1])
            sage: c.equivalent_recurrent()
            {1: 1, 2: 1}
            sage: c.__dict__
            {'_equivalent_recurrent': [{1: 1, 2: 1}, {1: 2, 2: 1}],
             '_sandpile': Cycle sandpile graph: 3 vertices, sink = 0,
             '_vertices': [1, 2]}

        .. NOTE::

            In the example, above, changing the value of ``c`` at some
            vertex makes a call to setitem, which resets some of the
            stored variables for ``c``.
        """
    def __getattr__(self, name):
        """
        Set certain variables only when called.

        INPUT:

        - ``name`` -- name of an internal method

        EXAMPLES::

            sage: S = sandpiles.Complete(4)
            sage: C = SandpileConfig(S,[1,1,1])
            sage: C.__getattr__('_deg')
            3
        """
    def deg(self):
        """
        The degree of the configuration.

        OUTPUT: integer

        EXAMPLES::

            sage: S = sandpiles.Complete(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: c.deg()
            3
        """
    def __add__(self, other):
        """
        Addition of configurations.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: sum of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = SandpileConfig(S, [3,2])
            sage: c + d
            {1: 4, 2: 4}
        """
    def __sub__(self, other):
        """
        Subtraction of configurations.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: sum of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = SandpileConfig(S, [3,2])
            sage: c - d
            {1: -2, 2: 0}
        """
    def __rsub__(self, other):
        """
        Right-side subtraction of configurations.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: sum of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = {1: 3, 2: 2}
            sage: d - c
            {1: 2, 2: 0}

        TESTS::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = {1: 3, 2: 2}
            sage: c.__rsub__(d)
            {1: 2, 2: 0}
        """
    def __neg__(self):
        """
        The additive inverse of the configuration.

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: -c
            {1: -1, 2: -2}
        """
    def __mul__(self, other):
        """
        If ``other`` is a configuration, the recurrent element equivalent
        to the sum.  If ``other`` is an integer, the sum of configuration with
        itself ``other`` times.

        INPUT:

        - ``other`` -- SandpileConfig or Integer

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S, [1,0,0])
            sage: c + c  # ordinary addition
            {1: 2, 2: 0, 3: 0}
            sage: c & c  # add and stabilize
            {1: 0, 2: 1, 3: 0}
            sage: c*c  # add and find equivalent recurrent
            {1: 1, 2: 1, 3: 1}
            sage: (c*c).is_recurrent()
            True
            sage: c*(-c) == S.identity()
            True
            sage: c
            {1: 1, 2: 0, 3: 0}
            sage: c*3
            {1: 3, 2: 0, 3: 0}
        """
    def __rmul__(self, other):
        """
        The sum of configuration with itself ``other`` times.

        INPUT:

        - ``other`` -- integer

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S,[1,2,3])
            sage: c
            {1: 1, 2: 2, 3: 3}
            sage: 3*c
            {1: 3, 2: 6, 3: 9}
            sage: 3*c == c*3
            True
        """
    def __le__(self, other) -> bool:
        """
        Return ``True`` if every component of ``self`` is at most that of
        ``other``.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = SandpileConfig(S, [2,3])
            sage: e = SandpileConfig(S, [2,0])
            sage: c <= c
            True
            sage: c <= d
            True
            sage: d <= c
            False
            sage: c <= e
            False
            sage: e <= c
            False
        """
    def __lt__(self, other) -> bool:
        """
        Return ``True`` if every component of ``self`` is at most that
        of ``other`` and the two configurations are not equal.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = SandpileConfig(S, [2,3])
            sage: c < c
            False
            sage: c < d
            True
            sage: d < c
            False
        """
    def __ge__(self, other) -> bool:
        """
        Return ``True`` if every component of ``self`` is at least that of
        ``other``.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = SandpileConfig(S, [2,3])
            sage: e = SandpileConfig(S, [2,0])
            sage: c >= c
            True
            sage: d >= c
            True
            sage: c >= d
            False
            sage: e >= c
            False
            sage: c >= e
            False
        """
    def __gt__(self, other) -> bool:
        """
        Return ``True`` if every component of ``self`` is at least that
        of ``other`` and the two configurations are not equal.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: d = SandpileConfig(S, [1,3])
            sage: c > c
            False
            sage: d > c
            True
            sage: c > d
            False
        """
    def __pow__(self, k):
        """
        The recurrent element equivalent to the sum of the
        configuration with itself `k` times.  If `k` is negative, do the
        same for the negation of the configuration.  If `k` is zero, return
        the identity of the sandpile group.

        INPUT:

        - ``k`` -- SandpileConfig

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S, [1,0,0])
            sage: c^3
            {1: 1, 2: 1, 3: 0}
            sage: (c + c + c) == c^3
            False
            sage: (c + c + c).equivalent_recurrent() == c^3
            True
            sage: c^(-1)
            {1: 1, 2: 1, 3: 0}
            sage: c^0 == S.identity()
            True
        """
    def __and__(self, other):
        """
        The stabilization of the sum.

        INPUT:

        - ``other`` -- SandpileConfig

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S, [1,0,0])
            sage: c + c  # ordinary addition
            {1: 2, 2: 0, 3: 0}
            sage: c & c  # add and stabilize
            {1: 0, 2: 1, 3: 0}
            sage: c*c  # add and find equivalent recurrent
            {1: 1, 2: 1, 3: 1}
            sage: ~(c + c) == c & c
            True
        """
    def sandpile(self):
        """
        The configuration's underlying sandpile.

        OUTPUT: Sandpile

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = S.identity()
            sage: c.sandpile()
            Diamond sandpile graph: 4 vertices, sink = 0
            sage: c.sandpile() == S
            True
        """
    def values(self):
        """
        The values of the configuration as a list.

        The list is sorted in the order of the vertices.

        OUTPUT: list of integers

        EXAMPLES::

            sage: S = Sandpile({'a':['c','b'], 'b':['c','a'], 'c':['a']},'a')
            sage: c = SandpileConfig(S, {'b':1, 'c':2})
            sage: c
            {'b': 1, 'c': 2}
            sage: c.values()
            [1, 2]
            sage: S.nonsink_vertices()
            ['b', 'c']
        """
    def dualize(self):
        """
        The difference with the maximal stable configuration.

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: S.max_stable()
            {1: 1, 2: 1}
            sage: c.dualize()
            {1: 0, 2: -1}
            sage: S.max_stable() - c == c.dualize()
            True
        """
    def fire_vertex(self, v):
        """
        Fire the given vertex.

        INPUT:

        - ``v`` -- vertex

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: c = SandpileConfig(S, [1,2])
            sage: c.fire_vertex(2)
            {1: 2, 2: 0}
        """
    def fire_script(self, sigma):
        """
        Fire the given script.  In other words,  fire each vertex the number of
        times indicated by ``sigma``.

        INPUT:

        - ``sigma`` -- SandpileConfig or (list or dict representing a SandpileConfig)

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S, [1,2,3])
            sage: c.unstable()
            [2, 3]
            sage: c.fire_script(SandpileConfig(S,[0,1,1]))
            {1: 2, 2: 1, 3: 2}
            sage: c.fire_script(SandpileConfig(S,[2,0,0])) == c.fire_vertex(1).fire_vertex(1)
            True
        """
    def unstable(self) -> list:
        """
        The unstable vertices.

        OUTPUT: list of vertices

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S, [1,2,3])
            sage: c.unstable()
            [2, 3]
        """
    def fire_unstable(self):
        """
        Fire all unstable vertices.

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: c = SandpileConfig(S, [1,2,3])
            sage: c.fire_unstable()
            {1: 2, 2: 1, 3: 2}
        """
    def stabilize(self, with_firing_vector: bool = False):
        """
        The stabilized configuration. Optionally returns the
        corresponding firing vector.

        INPUT:

        - ``with_firing_vector`` -- boolean (default: ``False``)

        OUTPUT: ``SandpileConfig`` or ``[SandpileConfig, firing_vector]``

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: c = 2*S.max_stable()
            sage: c._set_stabilize()
            sage: '_stabilize' in c.__dict__
            True
            sage: S = sandpiles.House()
            sage: c = S.max_stable() + S.identity()
            sage: c.stabilize(True)
            [{1: 1, 2: 2, 3: 2, 4: 1}, {1: 2, 2: 2, 3: 3, 4: 3}]
            sage: S.max_stable() & S.identity() == c.stabilize()
            True
            sage: ~c == c.stabilize()
            True
        """
    def __invert__(self):
        """
        The stabilized configuration.

        OUTPUT: ``SandpileConfig``

        Returns the stabilized configuration.

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: c = S.max_stable() + S.identity()
            sage: ~c == c.stabilize()
            True
        """
    def support(self):
        """
        The vertices containing sand.

        OUTPUT: list - support of the configuration

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = S.identity()
            sage: c
            {1: 2, 2: 2, 3: 0}
            sage: c.support()
            [1, 2]
        """
    def add_random(self, distrib=None):
        '''
        Add one grain of sand to a random vertex.

        Optionally, a probability distribution, ``distrib``, may be
        placed on the vertices or the nonsink vertices.

        See NOTE for details.

        INPUT:

        - ``distrib`` -- (optional) list of nonnegative numbers
          summing to 1 (representing a prob. dist.)

        OUTPUT: SandpileConfig

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: c = s.zero_config()
            sage: c.add_random() # random
            {1: 0, 2: 1, 3: 0}
            sage: c
            {1: 0, 2: 0, 3: 0}
            sage: c.add_random([0.1,0.1,0.8]) # random
            {1: 0, 2: 0, 3: 1}
            sage: c.add_random([0.7,0.1,0.1,0.1]) # random
            {1: 0, 2: 0, 3: 0}

        We compute the "sizes" of the avalanches caused by adding random grains
        of sand to the maximal stable configuration on a grid graph.  The
        function ``stabilize()`` returns the firing vector of the
        stabilization, a dictionary whose values say how many times each vertex
        fires in the stabilization.::

            sage: S = sandpiles.Grid(10,10)
            sage: m = S.max_stable()
            sage: a = []
            sage: for i in range(1000):
            ....:     m = m.add_random()
            ....:     m, f = m.stabilize(True)
            ....:     a.append(sum(f.values()))

            sage: # needs sage.plot
            sage: p = list_plot([[log(i + 1), log(a.count(i))]
            ....:                for i in [0..max(a)] if a.count(i)])
            sage: p.axes_labels([\'log(N)\', \'log(D(N))\'])
            sage: t = text("Distribution of avalanche sizes", (2,2), rgbcolor=(1,0,0))
            sage: show(p + t, axes_labels=[\'log(N)\', \'log(D(N))\'])      # long time

        .. NOTE::

            If ``distrib`` is ``None``, then the probability is the uniform probability on the nonsink
            vertices.  Otherwise, there are two possibilities:

            (i) the length of ``distrib`` is equal to the number of vertices, and ``distrib`` represents
            a probability distribution on all of the vertices.  In that case, the sink may be chosen
            at random, in which case, the  configuration is unchanged.

            (ii) Otherwise, the length of ``distrib`` must be equal to the number of nonsink vertices,
            and ``distrib`` represents a probability distribution on the nonsink vertices.

        .. WARNING::

            If ``distrib != None``, the user is responsible for assuring the sum of its entries is
            1 and that its length is equal to the number of sink vertices or the number of nonsink vertices.
        '''
    def order(self):
        """
        The order of the equivalent recurrent element.

        OUTPUT: integer

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = SandpileConfig(S,[2,0,1])
            sage: c.order()
            4
            sage: ~(c + c + c + c) == S.identity()
            True
            sage: c = SandpileConfig(S,[1,1,0])
            sage: c.order()
            1
            sage: c.is_recurrent()
            False
            sage: c.equivalent_recurrent() == S.identity()
            True
        """
    def is_stable(self):
        """
        Return whether the configuration is stable.

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.max_stable().is_stable()
            True
            sage: (2*S.max_stable()).is_stable()
            False
            sage: (S.max_stable() & S.max_stable()).is_stable()
            True
        """
    def equivalent_recurrent(self, with_firing_vector: bool = False):
        """
        The recurrent configuration equivalent to the given configuration.
        Optionally, return the corresponding firing vector.

        INPUT:

        - ``with_firing_vector`` -- boolean (default: ``False``)

        OUTPUT: SandpileConfig or [SandpileConfig, firing_vector]

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = SandpileConfig(S, [0,0,0])
            sage: c.equivalent_recurrent() == S.identity()
            True
            sage: x = c.equivalent_recurrent(True)
            sage: r = vector([x[0][v] for v in S.nonsink_vertices()])
            sage: f = vector([x[1][v] for v in S.nonsink_vertices()])
            sage: cv = vector(c.values())
            sage: r == cv - f*S.reduced_laplacian()
            True

        .. NOTE::

            Let `L` be the reduced Laplacian, `c` the initial configuration, `r` the
            returned configuration, and `f` the firing vector.  Then `r = c - f\\cdot
            L`.
        """
    def is_recurrent(self):
        """
        Return whether the configuration is recurrent.

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.identity().is_recurrent()
            True
            sage: S.zero_config().is_recurrent()
            False
        """
    def equivalent_superstable(self, with_firing_vector: bool = False):
        """
        The equivalent superstable configuration. Optionally, return the
        corresponding firing vector.

        INPUT:

        - ``with_firing_vector`` -- boolean (default: ``False``)

        OUTPUT: SandpileConfig or [SandpileConfig, firing_vector]

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: m = S.max_stable()
            sage: m.equivalent_superstable().is_superstable()
            True
            sage: x = m.equivalent_superstable(True)
            sage: s = vector(x[0].values())
            sage: f = vector(x[1].values())
            sage: mv = vector(m.values())
            sage: s == mv - f*S.reduced_laplacian()
            True

        .. NOTE::

            Let `L` be the reduced Laplacian, `c` the initial configuration, `s` the
            returned configuration, and `f` the firing vector.  Then `s = c - f\\cdot
            L`.
        """
    def is_superstable(self):
        """
        Return whether the configuration is superstable.

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: S.zero_config().is_superstable()
            True
        """
    def is_symmetric(self, orbits) -> bool:
        """
        Return whether the configuration is symmetric.  Return ``True`` if the values of the
        configuration are constant over the vertices in each sublist of
        ``orbits``.

        INPUT:

        - ``orbits`` -- list of lists of vertices

        OUTPUT: boolean

        EXAMPLES::

            sage: S = Sandpile({0: {},
            ....:              1: {0: 1, 2: 1, 3: 1},
            ....:              2: {1: 1, 3: 1, 4: 1},
            ....:              3: {1: 1, 2: 1, 4: 1},
            ....:              4: {2: 1, 3: 1}})
            sage: c = SandpileConfig(S, [1, 2, 2, 3])
            sage: c.is_symmetric([[2,3]])
            True
        """
    def burst_size(self, v):
        """
        The burst size of the configuration with respect to the given vertex.

        INPUT:

        - ``v`` -- vertex

        OUTPUT: integer

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: [i.burst_size(0) for i in s.recurrents()]
            [1, 1, 1, 1, 1, 1, 1, 1]
            sage: [i.burst_size(1) for i in s.recurrents()]
            [0, 0, 1, 2, 1, 2, 0, 2]

        .. NOTE::

            To define ``c.burst(v)``, if `v` is not the sink, let `c'` be the unique
            recurrent for which the stabilization of `c' + v` is `c`.  The
            burst size is then the amount of sand that goes into the sink during this
            stabilization.  If `v` is the sink, the burst size is defined to be 1.

        REFERENCES:

        - [Lev2014]_
        """
    def show(self, sink: bool = True, colors: bool = True, heights: bool = False, directed=None, **kwds) -> None:
        """
        Show the configuration.

        INPUT:

        - ``sink`` -- boolean (default: ``True``); whether to show the sink

        - ``colors`` -- boolean (default: ``True``); whether to color-code the
          amount of sand on each vertex

        - ``heights`` -- boolean (default: ``False``); whether to label each
          vertex with the amount of sand

        - ``directed`` -- (optional) whether to draw directed edges

        - ``kwds`` -- (optional) arguments passed to the show method for Graph

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: c = S.identity()
            sage: c.show()                                                              # needs sage.plot
            sage: c.show(directed=False)                                                # needs sage.plot
            sage: c.show(sink=False, colors=False, heights=True)                        # needs sage.plot
        """

class SandpileDivisor(dict):
    """
    Class for divisors on a sandpile.
    """
    @staticmethod
    def help(verbose: bool = True) -> None:
        '''
        List of SandpileDivisor methods.  If ``verbose``, include short descriptions.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: printed string

        EXAMPLES::

            sage: SandpileDivisor.help()
            For detailed help with any method FOO listed below,
            enter "SandpileDivisor.FOO?" or enter "D.FOO?" for any SandpileDivisor D.
            <BLANKLINE>
            Dcomplex               -- The support-complex.
            add_random             -- Add one grain of sand to a random vertex.
            betti                  -- The Betti numbers for the support-complex.
            deg                    -- The degree of the divisor.
            dualize                -- The difference with the maximal stable divisor.
            effective_div          -- All linearly equivalent effective divisors.
            fire_script            -- Fire the given script.
            fire_unstable          -- Fire all unstable vertices.
            fire_vertex            -- Fire the given vertex.
            help                   -- List of SandpileDivisor methods.
            is_alive               -- Return whether the divisor is stabilizable.
            is_linearly_equivalent -- Return whether the given divisor is linearly equivalent.
            is_q_reduced           -- Return whether the divisor is q-reduced.
            is_symmetric           -- Return whether the divisor is symmetric.
            is_weierstrass_pt      -- Return whether the given vertex is a Weierstrass point.
            polytope               -- The polytope determining the complete linear system.
            polytope_integer_pts   -- The integer points inside divisor\'s polytope.
            q_reduced              -- The linearly equivalent q-reduced divisor.
            rank                   -- The rank of the divisor.
            sandpile               -- The divisor\'s underlying sandpile.
            show                   -- Show the divisor.
            simulate_threshold     -- The first unstabilizable divisor in the closed Markov chain.
            stabilize              -- The stabilization of the divisor.
            support                -- List of vertices at which the divisor is nonzero.
            unstable               -- The unstable vertices.
            values                 -- The values of the divisor as a list.
            weierstrass_div        -- The Weierstrass divisor.
            weierstrass_gap_seq    -- The Weierstrass gap sequence at the given vertex.
            weierstrass_pts        -- The Weierstrass points (vertices).
            weierstrass_rank_seq   -- The Weierstrass rank sequence at the given vertex.
        '''
    def __init__(self, S, D) -> None:
        """
        Create a divisor on a Sandpile.

        INPUT:

        - ``S`` -- Sandpile

        - ``D`` -- dictionary or list representing a divisor

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(6)
            sage: D = SandpileDivisor(S,[0,1,0,1,1,3])
            sage: D.support()
            [1, 3, 4, 5]
        """
    def __deepcopy__(self, memo):
        """
        Overrides the deepcopy method for dict.

        INPUT:

        - ``memo`` -- (optional) dictionary

        EXAMPLES::

            sage: S = sandpiles.Cycle(6)
            sage: D = SandpileDivisor(S, [1,2,3,4,5,6])
            sage: E = deepcopy(D)
            sage: E[0] += 10
            sage: D
            {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
            sage: E
            {0: 11, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
        """
    __dict__: Incomplete
    def __setitem__(self, key, item) -> None:
        """
        Overrides the setitem method for dict.

        INPUT:

        - ``key``, ``item`` -- objects

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S,[0,1,1])
            sage: eff = D.effective_div()                                               # needs sage.geometry.polyhedron
            sage: D.__dict__                                                            # needs sage.geometry.polyhedron
            {'_effective_div': [{0: 0, 1: 1, 2: 1}, {0: 2, 1: 0, 2: 0}],
             '_polytope': A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 3 vertices,
             '_polytope_integer_pts': ((0, 0), (1, 1)),
             '_sandpile': Cycle sandpile graph: 3 vertices, sink = 0,
             '_vertices': [0, 1, 2],
             '_weierstrass_rank_seq': {}}
            sage: D[0] += 1
            sage: D.__dict__
            {'_sandpile': Cycle sandpile graph: 3 vertices, sink = 0,
             '_vertices': [0, 1, 2]}

        .. NOTE::

            In the example, above, changing the value of `D` at some vertex makes
            a call to setitem, which resets some of the stored variables for `D`.
        """
    def __getattr__(self, name):
        """
        Set certain variables only when called.

        INPUT:

        - ``name`` -- name of an internal method

        EXAMPLES::

            sage: S = sandpiles.Cycle(6)
            sage: D = SandpileDivisor(S,[0,1,0,1,1,3])
            sage: D.__getattr__('_deg')
            6
        """
    def deg(self):
        """
        The degree of the divisor.

        OUTPUT: integer

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: D.deg()
            6
        """
    def __add__(self, other):
        """
        Addition of divisors.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: sum of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [3,2,1])
            sage: D + E
            {0: 4, 1: 4, 2: 4}
        """
    def __mul__(self, other):
        """
        Sum of the divisor with itself ``other`` times.

        INPUT:

        - ``other`` -- integer

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: D = SandpileDivisor(S,[1,2,3,4])
            sage: D
            {0: 1, 1: 2, 2: 3, 3: 4}
            sage: 3*D
            {0: 3, 1: 6, 2: 9, 3: 12}
            sage: 3*D == D*3
            True
        """
    def __rmul__(self, other):
        """
        The sum of divisor with itself ``other`` times.

        INPUT:

        - ``other`` -- integer

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: D = SandpileDivisor(S,[1,2,3,4])
            sage: D
            {0: 1, 1: 2, 2: 3, 3: 4}
            sage: 3*D
            {0: 3, 1: 6, 2: 9, 3: 12}
            sage: 3*D == D*3
            True
        """
    def __radd__(self, other):
        """
        Right-side addition of divisors.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: sum of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [3,2,1])
            sage: D.__radd__(E)
            {0: 4, 1: 4, 2: 4}
        """
    def __sub__(self, other):
        """
        Subtraction of divisors.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: difference of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [3,2,1])
            sage: D - E
            {0: -2, 1: 0, 2: 2}
        """
    def __rsub__(self, other):
        """
        Right-side subtraction of divisors.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: difference of ``self`` and ``other``

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = {0: 3, 1: 2, 2: 1}
            sage: D.__rsub__(E)
            {0: 2, 1: 0, 2: -2}
            sage: E - D
            {0: 2, 1: 0, 2: -2}
        """
    def __neg__(self):
        """
        The additive inverse of the divisor.

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: -D
            {0: -1, 1: -2, 2: -3}
        """
    def __le__(self, other):
        """
        Return ``True`` if every component of ``self`` is at most that of
        ``other``.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [2,3,4])
            sage: F = SandpileDivisor(S, [2,0,4])
            sage: D <= D
            True
            sage: D <= E
            True
            sage: E <= D
            False
            sage: D <= F
            False
            sage: F <= D
            False
        """
    def __lt__(self, other):
        """
        Return ``True`` if every component of ``self`` is at most that
        of ``other`` and the two divisors are not equal.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [2,3,4])
            sage: D < D
            False
            sage: D < E
            True
            sage: E < D
            False
        """
    def __ge__(self, other):
        """
        Return ``True`` if every component of ``self`` is at least that of
        ``other``.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [2,3,4])
            sage: F = SandpileDivisor(S, [2,0,4])
            sage: D >= D
            True
            sage: E >= D
            True
            sage: D >= E
            False
            sage: F >= D
            False
            sage: D >= F
            False
        """
    def __gt__(self, other):
        """
        Return ``True`` if every component of ``self`` is at least that
        of ``other`` and the two divisors are not equal.

        INPUT:

        - ``other`` -- SandpileDivisor

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: E = SandpileDivisor(S, [1,3,4])
            sage: D > D
            False
            sage: E > D
            True
            sage: D > E
            False
        """
    def sandpile(self):
        """
        The divisor's underlying sandpile.

        OUTPUT: Sandpile

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: D = SandpileDivisor(S,[1,-2,0,3])
            sage: D.sandpile()
            Diamond sandpile graph: 4 vertices, sink = 0
            sage: D.sandpile() == S
            True
        """
    def values(self):
        """
        The values of the divisor as a list.

        The list is sorted in the order of the vertices.

        OUTPUT: list of integers

        boolean

        EXAMPLES::

            sage: S = Sandpile({'a':['c','b'], 'b':['c','a'], 'c':['a']},'a')
            sage: D = SandpileDivisor(S, {'a':0, 'b':1, 'c':2})
            sage: D
            {'a': 0, 'b': 1, 'c': 2}
            sage: D.values()
            [0, 1, 2]
            sage: S.vertices(sort=True)
            ['a', 'b', 'c']
        """
    def dualize(self):
        """
        The difference with the maximal stable divisor.

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: D.dualize()
            {0: 0, 1: -1, 2: -2}
            sage: S.max_stable_div() - D == D.dualize()
            True
        """
    def fire_vertex(self, v):
        """
        Fire the given vertex.

        INPUT:

        - ``v`` -- vertex

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: D.fire_vertex(1)
            {0: 2, 1: 0, 2: 4}
        """
    def fire_script(self, sigma):
        """
        Fire the given script.  In other words, fire each vertex the number of
        times indicated by ``sigma``.

        INPUT:

        - ``sigma`` -- SandpileDivisor or (list or dict representing a SandpileDivisor)

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: D.unstable()
            [1, 2]
            sage: D.fire_script([0,1,1])
            {0: 3, 1: 1, 2: 2}
            sage: D.fire_script(SandpileDivisor(S,[2,0,0])) == D.fire_vertex(0).fire_vertex(0)
            True
        """
    def unstable(self):
        """
        The unstable vertices.

        OUTPUT: list of vertices

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: D.unstable()
            [1, 2]
        """
    def fire_unstable(self):
        """
        Fire all unstable vertices.

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [1,2,3])
            sage: D.fire_unstable()
            {0: 3, 1: 1, 2: 2}
        """
    def q_reduced(self, verbose: bool = True):
        """
        The linearly equivalent `q`-reduced divisor.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: SandpileDivisor or list representing SandpileDivisor

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D = SandpileDivisor(s,[2,-3,2,0])
            sage: D.q_reduced()
            {0: -2, 1: 1, 2: 2, 3: 0}
            sage: D.q_reduced(False)
            [-2, 1, 2, 0]

        .. NOTE::

            The divisor `D` is `qreduced if `D = c + kq` where `c`
            is superstable, `k` is an integer, and `q` is the sink.
        """
    def is_q_reduced(self):
        """
        Return whether the divisor is `q`-reduced.  This would mean that `self = c + kq` where
        `c` is superstable, `k` is an integer, and `q` is the sink vertex.

        OUTPUT: boolean

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D = SandpileDivisor(s,[2,-3,2,0])
            sage: D.is_q_reduced()
            False
            sage: SandpileDivisor(s,[10,0,1,2]).is_q_reduced()
            True

        For undirected or, more generally, Eulerian graphs, `q`-reduced divisors are
        linearly equivalent if and only if they are equal.  The same does not hold for
        general directed graphs:

        ::

            sage: s = Sandpile({0:[1],1:[1,1]})
            sage: D = SandpileDivisor(s,[-1,1])
            sage: Z = s.zero_div()
            sage: D.is_q_reduced()
            True
            sage: Z.is_q_reduced()
            True
            sage: D == Z
            False
            sage: D.is_linearly_equivalent(Z)
            True
        """
    def is_linearly_equivalent(self, D, with_firing_vector: bool = False):
        """
        Return whether the given divisor is linearly equivalent.  Optionally, returns the
        firing vector.  (See NOTE.)

        INPUT:

        - ``D`` -- SandpileDivisor or list, tuple, etc. representing a divisor

        - ``with_firing_vector`` -- boolean (default: ``False``)

        OUTPUT: boolean or integer vector

        EXAMPLES::

            sage: s = sandpiles.Complete(3)
            sage: D = SandpileDivisor(s,[2,0,0])
            sage: D.is_linearly_equivalent([0,1,1])
            True
            sage: D.is_linearly_equivalent([0,1,1],True)
            (0, -1, -1)
            sage: v = vector(D.is_linearly_equivalent([0,1,1],True))
            sage: vector(D.values()) - s.laplacian()*v
            (0, 1, 1)
            sage: D.is_linearly_equivalent([0,0,0])
            False
            sage: D.is_linearly_equivalent([0,0,0],True)
            ()

        .. NOTE::

            - If ``with_firing_vector`` is ``False``, returns either ``True`` or ``False``.

            - If ``with_firing_vector`` is ``True`` then: (i) if ``self`` is linearly
              equivalent to `D`, returns a vector `v` such that ``self - v*self.laplacian().transpose() = D``.
              Otherwise, (ii) if ``self`` is not linearly equivalent to `D`, the output is the empty vector, ``()``.
        """
    def simulate_threshold(self, distrib=None):
        """
        The first unstabilizable divisor in the closed Markov chain.
        (See NOTE.)

        INPUT:

        - ``distrib`` -- (optional)  list of nonnegative numbers representing a probability distribution on the vertices

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D = s.zero_div()
            sage: D.simulate_threshold()  # random
            {0: 2, 1: 3, 2: 1, 3: 2}
            sage: n(mean([D.simulate_threshold().deg() for _ in range(10)]))  # random
            7.10000000000000
            sage: n(s.stationary_density()*s.num_verts())
            6.93750000000000

        .. NOTE::

            Starting at ``self``, repeatedly choose a vertex and add a grain of
            sand to it.  Return the first unstabilizable divisor that is
            reached.  Also see the ``markov_chain`` method for the underlying
            sandpile.
        """
    def polytope(self):
        """
        The polytope determining the complete linear system.

        OUTPUT: polytope

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: s = sandpiles.Complete(4)
            sage: D = SandpileDivisor(s,[4,2,0,0])
            sage: p = D.polytope()
            sage: p.inequalities()
            (An inequality (-3, 1, 1) x + 2 >= 0,
             An inequality (1, 1, 1) x + 4 >= 0,
             An inequality (1, -3, 1) x + 0 >= 0,
             An inequality (1, 1, -3) x + 0 >= 0)
            sage: D = SandpileDivisor(s,[-1,0,0,0])
            sage: D.polytope()
            The empty polyhedron in QQ^3

        .. NOTE::

            For a divisor `D`, this is the intersection of (i) the polyhedron
            determined by the system of inequalities `L^t x \\leq D` where `L^t`
            is the transpose of the Laplacian with (ii) the hyperplane
            `x_{\\mathrm{sink\\_vertex}} = 0`. The polytope is thought of as sitting in
            `(n-1)`-dimensional Euclidean space where `n` is the number of
            vertices.
        """
    def polytope_integer_pts(self):
        """
        The integer points inside divisor's polytope.  The polytope referred to
        here is the one determining the divisor's complete linear system (see the
        documentation for ``polytope``).

        OUTPUT: tuple of integer vectors

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D = SandpileDivisor(s,[4,2,0,0])
            sage: sorted(D.polytope_integer_pts())                                      # needs sage.geometry.polyhedron
            [(-2, -1, -1),
             (-1, -2, -1),
             (-1, -1, -2),
             (-1, -1, -1),
             (0, -1, -1),
             (0, 0, 0)]
            sage: D = SandpileDivisor(s,[-1,0,0,0])
            sage: D.polytope_integer_pts()                                              # needs sage.geometry.polyhedron
            ()
        """
    def effective_div(self, verbose: bool = True, with_firing_vectors: bool = False):
        """
        All linearly equivalent effective divisors.  If ``verbose``
        is ``False``, the divisors are converted to lists of integers.
        If ``with_firing_vectors`` is ``True`` then a list of firing vectors
        is also given, each of which prescribes the vertices to be fired
        in order to obtain an effective divisor.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        - ``with_firing_vectors`` -- boolean (default: ``False``)

        OUTPUT: list (of divisors)

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: s = sandpiles.Complete(4)
            sage: D = SandpileDivisor(s,[4,2,0,0])
            sage: sorted(D.effective_div(), key=str)
            [{0: 0, 1: 2, 2: 0, 3: 4},
             {0: 0, 1: 2, 2: 4, 3: 0},
             {0: 0, 1: 6, 2: 0, 3: 0},
             {0: 1, 1: 3, 2: 1, 3: 1},
             {0: 2, 1: 0, 2: 2, 3: 2},
             {0: 4, 1: 2, 2: 0, 3: 0}]
            sage: sorted(D.effective_div(False))
            [[0, 2, 0, 4],
             [0, 2, 4, 0],
             [0, 6, 0, 0],
             [1, 3, 1, 1],
             [2, 0, 2, 2],
             [4, 2, 0, 0]]
            sage: sorted(D.effective_div(with_firing_vectors=True), key=str)
            [({0: 0, 1: 2, 2: 0, 3: 4}, (0, -1, -1, -2)),
             ({0: 0, 1: 2, 2: 4, 3: 0}, (0, -1, -2, -1)),
             ({0: 0, 1: 6, 2: 0, 3: 0}, (0, -2, -1, -1)),
             ({0: 1, 1: 3, 2: 1, 3: 1}, (0, -1, -1, -1)),
             ({0: 2, 1: 0, 2: 2, 3: 2}, (0, 0, -1, -1)),
             ({0: 4, 1: 2, 2: 0, 3: 0}, (0, 0, 0, 0))]
            sage: a = _[2]
            sage: a[0].values()
            [0, 6, 0, 0]
            sage: vector(D.values()) - s.laplacian()*a[1]
            (0, 6, 0, 0)
            sage: sorted(D.effective_div(False, True))
            [([0, 2, 0, 4], (0, -1, -1, -2)),
             ([0, 2, 4, 0], (0, -1, -2, -1)),
             ([0, 6, 0, 0], (0, -2, -1, -1)),
             ([1, 3, 1, 1], (0, -1, -1, -1)),
             ([2, 0, 2, 2], (0, 0, -1, -1)),
             ([4, 2, 0, 0], (0, 0, 0, 0))]
            sage: D = SandpileDivisor(s,[-1,0,0,0])
            sage: D.effective_div(False,True)
            []
        """
    def rank(self, with_witness: bool = False):
        """
        The rank of the divisor.  Optionally returns an effective divisor `E` such
        that `D - E` is not winnable (has an empty complete linear system).

        INPUT:

        - ``with_witness`` -- boolean (default: ``False``)

        OUTPUT: integer or (integer, SandpileDivisor)

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: S = sandpiles.Complete(4)
            sage: D = SandpileDivisor(S,[4,2,0,0])
            sage: D.rank()
            3
            sage: D.rank(True)
            (3, {0: 3, 1: 0, 2: 1, 3: 0})
            sage: E = _[1]
            sage: (D - E).rank()                                                        # needs sage.rings.number_field
            -1

         Riemann-Roch theorem::

            sage: # needs sage.geometry.polyhedron
            sage: D.rank() - (S.canonical_divisor()-D).rank() == D.deg() + 1 - S.genus()
            True

         Riemann-Roch theorem::

            sage: # needs sage.geometry.polyhedron
            sage: D.rank() - (S.canonical_divisor()-D).rank() == D.deg() + 1 - S.genus()
            True
            sage: S = Sandpile({0:[1,1,1,2],1:[0,0,0,1,1,1,2,2],2:[2,2,1,1,0]},0)  # multigraph with loops
            sage: D = SandpileDivisor(S,[4,2,0])
            sage: D.rank(True)
            (2, {0: 1, 1: 1, 2: 1})
            sage: S = Sandpile({0:[1,2], 1:[0,2,2], 2: [0,1]},0) # directed graph
            sage: S.is_undirected()
            False
            sage: D = SandpileDivisor(S,[0,2,0])
            sage: D.effective_div()
            [{0: 0, 1: 2, 2: 0}, {0: 2, 1: 0, 2: 0}]
            sage: D.rank(True)
            (0, {0: 0, 1: 0, 2: 1})
            sage: E = D.rank(True)[1]
            sage: (D - E).effective_div()                                               # needs sage.rings.number_field
            []

        .. NOTE::

            The rank of a divisor `D` is -1 if `D` is not linearly equivalent to an effective divisor
            (i.e., the dollar game represented by `D` is unwinnable).  Otherwise, the rank of `D` is
            the largest integer `r` such that `D - E` is linearly equivalent to an effective divisor
            for all effective divisors `E` with `\\deg(E) = r`.
        """
    def weierstrass_rank_seq(self, v: str = 'sink'):
        """
        The Weierstrass rank sequence at the given vertex.  Computes the rank of
        the divisor `D - nv` starting with `n=0` and ending when the rank is
        `-1`.

        INPUT:

        - ``v`` -- (default: ``sink``) vertex

        OUTPUT: tuple of int

        EXAMPLES::

            sage: s = sandpiles.House()
            sage: K = s.canonical_divisor()
            sage: [K.weierstrass_rank_seq(v) for v in s.vertices(sort=True)]            # needs sage.geometry.polyhedron
            [(1, 0, -1), (1, 0, -1), (1, 0, -1), (1, 0, -1), (1, 0, 0, -1)]
        """
    def weierstrass_gap_seq(self, v: str = 'sink', weight: bool = True):
        """
        The Weierstrass gap sequence at the given vertex.  If ``weight`` is
        ``True``, then also compute the weight of each gap value.

        INPUT:

        - ``v`` -- (default: ``sink``) vertex

        - ``weight`` -- boolean (default: ``True``)

        OUTPUT: list or (list of list) of integers

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: s = sandpiles.Cycle(4)
            sage: D = SandpileDivisor(s,[2,0,0,0])
            sage: [D.weierstrass_gap_seq(v,False) for v in s.vertices(sort=True)]
            [(1, 3), (1, 2), (1, 3), (1, 2)]
            sage: [D.weierstrass_gap_seq(v) for v in s.vertices(sort=True)]
            [((1, 3), 1), ((1, 2), 0), ((1, 3), 1), ((1, 2), 0)]
            sage: D.weierstrass_gap_seq()   # gap sequence at sink vertex, 0
            ((1, 3), 1)
            sage: D.weierstrass_rank_seq()  # rank sequence at the sink vertex
            (1, 0, 0, -1)

        .. NOTE::

            The integer `k` is a Weierstrass gap for the divisor `D` at vertex `v` if the rank
            of `D - (k-1)v` does not equal the rank of `D - kv`.  Let `r` be the rank of `D` and
            let `k_i` be the `i`-th gap at `v`.  The Weierstrass weight of `v` for `D` is the
            sum of `(k_i - i)` as `i` ranges from `1` to `r + 1`.  It measure the difference
            between the sequence `r, r - 1, ..., 0, -1, -1, ...` and the rank sequence
            `\\mathrm{rank}(D), \\mathrm{rank}(D - v), \\mathrm{rank}(D - 2v), \\dots`
        """
    def is_weierstrass_pt(self, v: str = 'sink'):
        """
        Return whether the given vertex is a Weierstrass point.

        INPUT:

        - ``v`` -- (default: ``sink``) vertex

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: s = sandpiles.House()
            sage: K = s.canonical_divisor()
            sage: K.weierstrass_rank_seq()  # sequence at the sink vertex, 0
            (1, 0, -1)
            sage: K.is_weierstrass_pt()
            False
            sage: K.weierstrass_rank_seq(4)
            (1, 0, 0, -1)
            sage: K.is_weierstrass_pt(4)
            True

        .. NOTE::

            The vertex `v` is a (generalized) Weierstrass point for divisor
            `D` if the sequence of ranks `r(D - nv)`
            for `n = 0, 1, 2, \\dots` is not `r(D), r(D)-1, \\dots, 0, -1, -1, \\dots`
        """
    def weierstrass_pts(self, with_rank_seq: bool = False):
        """
        The Weierstrass points (vertices). Optionally, return the corresponding
        rank sequences.

        INPUT:

        - ``with_rank_seq`` -- boolean (default: ``False``)

        OUTPUT: tuple of vertices or list of (vertex, rank sequence)

        EXAMPLES::

            sage: s = sandpiles.House()
            sage: K = s.canonical_divisor()
            sage: K.weierstrass_pts()                                                   # needs sage.geometry.polyhedron
            (4,)
            sage: K.weierstrass_pts(True)                                               # needs sage.geometry.polyhedron
            [(4, (1, 0, 0, -1))]

        .. NOTE::

            The vertex `v` is a (generalized) Weierstrass point for divisor
            `D` if the sequence of ranks `r(D - nv)`
            for `n = 0, 1, 2, \\dots`` is not `r(D), r(D)-1, \\dots, 0, -1, -1, \\dots`
        """
    def weierstrass_div(self, verbose: bool = True):
        """
        The Weierstrass divisor.  Its value at a vertex is the weight of that
        vertex as a Weierstrass point.  (See
        ``SandpileDivisor.weierstrass_gap_seq``.)

        INPUT:

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: D = SandpileDivisor(s,[4,2,1,0])
            sage: [D.weierstrass_rank_seq(v) for v in s]                                # needs sage.geometry.polyhedron
            [(5, 4, 3, 2, 1, 0, 0, -1),
             (5, 4, 3, 2, 1, 0, -1),
             (5, 4, 3, 2, 1, 0, 0, 0, -1),
             (5, 4, 3, 2, 1, 0, 0, -1)]
            sage: D.weierstrass_div()                                                   # needs sage.geometry.polyhedron
            {0: 1, 1: 0, 2: 2, 3: 1}
            sage: k5 = sandpiles.Complete(5)
            sage: K = k5.canonical_divisor()
            sage: K.weierstrass_div()
            {0: 9, 1: 9, 2: 9, 3: 9, 4: 9}
        """
    def support(self):
        """
        List of vertices at which the divisor is nonzero.

        OUTPUT: list representing the support of the divisor

        EXAMPLES::

            sage: S = sandpiles.Cycle(4)
            sage: D = SandpileDivisor(S, [0,0,1,1])
            sage: D.support()
            [2, 3]
            sage: S.vertices(sort=True)
            [0, 1, 2, 3]
        """
    def Dcomplex(self):
        '''
        The support-complex. (See NOTE.)

        OUTPUT: simplicial complex

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: S = sandpiles.House()
            sage: p = SandpileDivisor(S, [1,2,1,0,0]).Dcomplex()
            sage: p.homology()
            {0: 0, 1: Z x Z, 2: 0}
            sage: p.f_vector()
            [1, 5, 10, 4]
            sage: p.betti()
            {0: 1, 1: 2, 2: 0}

        .. NOTE::

            The "support-complex" is the simplicial complex determined by the
            supports of the linearly equivalent effective divisors.
        '''
    def betti(self):
        '''
        The Betti numbers for the support-complex.  (See NOTE.)

        OUTPUT: dictionary of integers

        EXAMPLES::

            sage: S = sandpiles.Cycle(3)
            sage: D = SandpileDivisor(S, [2,0,1])
            sage: D.betti()                                                             # needs sage.geometry.polyhedron
            {0: 1, 1: 1}

        .. NOTE::

            The "support-complex" is the simplicial complex determined by the
            supports of the linearly equivalent effective divisors.
        '''
    def add_random(self, distrib=None):
        """
        Add one grain of sand to a random vertex.

        INPUT:

        - ``distrib`` -- (optional) list of nonnegative numbers representing a probability distribution on the vertices

        OUTPUT: SandpileDivisor

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D = s.zero_div()
            sage: D.add_random() # random
            {0: 0, 1: 0, 2: 1, 3: 0}
            sage: D.add_random([0.1,0.1,0.1,0.7]) # random
            {0: 0, 1: 0, 2: 0, 3: 1}

        .. WARNING::

            If ``distrib`` is not ``None``, the user is responsible for assuring the sum of its entries is 1.
        """
    def is_symmetric(self, orbits):
        """
        Return whether the divisor is symmetric.  Return ``True`` if the values of the
        configuration are constant over the vertices in each sublist of
        ``orbits``.

        INPUT:

        - ``orbits`` -- list of lists of vertices

        OUTPUT: boolean

        EXAMPLES::

            sage: S = sandpiles.House()
            sage: S.dict()
            {0: {1: 1, 2: 1},
             1: {0: 1, 3: 1},
             2: {0: 1, 3: 1, 4: 1},
             3: {1: 1, 2: 1, 4: 1},
             4: {2: 1, 3: 1}}
            sage: D = SandpileDivisor(S, [0,0,1,1,3])
            sage: D.is_symmetric([[2,3], [4]])
            True
        """
    def is_alive(self, cycle: bool = False):
        """
        Return whether the divisor is stabilizable.  In other words, will the divisor stabilize
        under repeated firings of all unstable vertices?  Optionally returns the
        resulting cycle.

        INPUT:

        - ``cycle`` -- boolean (default: ``False``)

        OUTPUT: boolean or optionally, a list of SandpileDivisors

        EXAMPLES::

            sage: S = sandpiles.Complete(4)
            sage: D = SandpileDivisor(S, {0: 4, 1: 3, 2: 3, 3: 2})
            sage: D.is_alive()
            True
            sage: D.is_alive(True)
            [{0: 4, 1: 3, 2: 3, 3: 2}, {0: 3, 1: 2, 2: 2, 3: 5}, {0: 1, 1: 4, 2: 4, 3: 3}]
        """
    def stabilize(self, with_firing_vector: bool = False):
        """
        The stabilization of the divisor.  If not stabilizable, return an error.

        INPUT:

        - ``with_firing_vector`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: D = SandpileDivisor(s,[0,3,0,0])
            sage: D.stabilize()
            {0: 1, 1: 0, 2: 1, 3: 1}
            sage: D.stabilize(with_firing_vector=True)
            [{0: 1, 1: 0, 2: 1, 3: 1}, {0: 0, 1: 1, 2: 0, 3: 0}]
        """
    def show(self, heights: bool = True, directed=None, **kwds) -> None:
        """
        Show the divisor.

        INPUT:

        - ``heights`` -- boolean (default: ``True``); whether to label each
          vertex with the amount of sand

        - ``directed`` -- (optional) whether to draw directed edges

        - ``kwds`` -- (optional) arguments passed to the show method for Graph

        EXAMPLES::

            sage: S = sandpiles.Diamond()
            sage: D = SandpileDivisor(S, [1,-2,0,2])
            sage: D.show(graph_border=True, vertex_size=700, directed=False)            # needs sage.plot
        """

def sandlib(selector=None):
    """
    Return the sandpile identified by ``selector``.  If no argument is
    given, a description of the sandpiles in the sandlib is printed.

    INPUT:

    - ``selector`` -- (optional) identifier or None

    OUTPUT: Sandpile or description

    EXAMPLES::

            sage: from sage.sandpiles.sandpile import sandlib
            sage: sandlib()
              Sandpiles in the sandlib:
                 ci1 : complete intersection, non-DAG but equivalent to a DAG
                 generic : generic digraph with 6 vertices
                 genus2 : Undirected graph of genus 2
                 gor : Gorenstein but not a complete intersection
                 kite : generic undirected graphs with 5 vertices
                 riemann-roch1 : directed graph with postulation 9 and 3 maximal weight superstables
                 riemann-roch2 : directed graph with a superstable not majorized by a maximal superstable
            sage: S = sandlib('gor')
            sage: S.resolution()                                                        # needs sage.libs.singular
            'R^1 <-- R^5 <-- R^5 <-- R^1'
    """
def triangle_sandpile(n):
    """
    A triangular sandpile.  Each nonsink vertex has out-degree six.  The
    vertices on the boundary of the triangle are connected to the sink.

    INPUT:

    - ``n`` -- integer

    OUTPUT: Sandpile

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import triangle_sandpile
        sage: T = triangle_sandpile(5)
        sage: T.group_order()
        135418115000
    """
def aztec_sandpile(n):
    """
    The aztec diamond graph.

    INPUT:

    - ``n`` -- integer

    OUTPUT: dictionary for the aztec diamond graph

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import aztec_sandpile
        sage: T = aztec_sandpile(2)
        sage: sorted(len(v) for u, v in T.items())
        [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 8]
        sage: Sandpile(T,(0, 0)).group_order()
        4542720

    .. NOTE::

        This is the aztec diamond graph with a sink vertex added.  Boundary
        vertices have edges to the sink so that each vertex has degree 4.
    """
def glue_graphs(g, h, glue_g, glue_h):
    """
    Glue two graphs together.

    INPUT:

    - ``g``, ``h`` -- dictionaries for directed multigraphs

    - ``glue_h``, ``glue_g`` -- dictionaries for a vertex

    OUTPUT: dictionary for a directed multigraph

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import glue_graphs
        sage: x = {0: {}, 1: {0: 1}, 2: {0: 1, 1: 1}, 3: {0: 1, 1: 1, 2: 1}}
        sage: y = {0: {}, 1: {0: 2}, 2: {1: 2}, 3: {0: 1, 2: 1}}
        sage: glue_x = {1: 1, 3: 2}
        sage: glue_y = {0: 1, 1: 2, 3: 1}
        sage: z = glue_graphs(x,y,glue_x,glue_y); z
        {'sink': {},
         'x0': {'sink': 1, 'x1': 1, 'x3': 2, 'y1': 2, 'y3': 1},
         'x1': {'x0': 1},
         'x2': {'x0': 1, 'x1': 1},
         'x3': {'x0': 1, 'x1': 1, 'x2': 1},
         'y1': {'sink': 2},
         'y2': {'y1': 2},
         'y3': {'sink': 1, 'y2': 1}}
        sage: S = Sandpile(z,'sink')
        sage: S.h_vector()
        [1, 6, 17, 31, 41, 41, 31, 17, 6, 1]
        sage: S.resolution()                                                            # needs sage.libs.singular
        'R^1 <-- R^7 <-- R^21 <-- R^35 <-- R^35 <-- R^21 <-- R^7 <-- R^1'

    .. NOTE::

        This method makes a dictionary for a graph by combining those for
        `g` and `h`.  The sink of `g` is replaced by a vertex that
        is connected to the vertices of `g` as specified by ``glue_g``
        the vertices of `h` as specified in ``glue_h``.  The sink of the glued
        graph is ``'sink'``.

        Both ``glue_g`` and ``glue_h`` are dictionaries with entries of the form
        ``v:w`` where ``v`` is the vertex to be connected to and ``w`` is the weight
        of the connecting edge.
    """
def firing_graph(S, eff):
    """
    Create a digraph with divisors as vertices and edges between two divisors
    `D` and `E` if firing a single vertex in `D` gives `E`.

    INPUT:

    - ``S`` -- Sandpile

    - ``eff`` -- list of divisors

    OUTPUT: DiGraph

    EXAMPLES::

        sage: S = sandpiles.Cycle(6)
        sage: D = SandpileDivisor(S, [1,1,1,1,2,0])
        sage: eff = D.effective_div()                                                   # needs sage.geometry.polyhedron
        sage: firing_graph(S, eff).show3d(edge_size=.005,               # long time, needs sage.geometry.polyhedron sage.plot
        ....:                             vertex_size=0.01)
    """
def parallel_firing_graph(S, eff):
    """
    Create a digraph with divisors as vertices and edges between two divisors
    `D` and `E` if firing all unstable vertices in `D` gives `E`.

    INPUT:

    - ``S`` -- Sandpile

    - ``eff`` -- list of divisors

    OUTPUT: DiGraph

    EXAMPLES::

        sage: S = sandpiles.Cycle(6)
        sage: D = SandpileDivisor(S, [1,1,1,1,2,0])
        sage: eff = D.effective_div()                                                   # needs sage.geometry.polyhedron
        sage: parallel_firing_graph(S, eff).show3d(edge_size=.005,      # long time, needs sage.geometry.polyhedron sage.plot
        ....:                                      vertex_size=0.01)
    """
def admissible_partitions(S, k) -> Generator[Incomplete]:
    """
    The partitions of the vertices of `S` into `k` parts, each of which is
    connected.

    INPUT:

    - ``S`` -- Sandpile

    - ``k`` -- integer

    OUTPUT: partitions

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import admissible_partitions
        sage: from sage.sandpiles.sandpile import partition_sandpile
        sage: S = sandpiles.Cycle(4)
        sage: P = [list(admissible_partitions(S, i)) for i in [2,3,4]]                  # needs sage.combinat
        sage: P                                                                         # needs sage.combinat
        [[{{0, 2, 3}, {1}},
          {{0, 3}, {1, 2}},
          {{0, 1, 3}, {2}},
          {{0}, {1, 2, 3}},
          {{0, 1}, {2, 3}},
          {{0, 1, 2}, {3}}],
         [{{0, 3}, {1}, {2}},
          {{0}, {1}, {2, 3}},
          {{0}, {1, 2}, {3}},
          {{0, 1}, {2}, {3}}],
         [{{0}, {1}, {2}, {3}}]]
        sage: for p in P:                                                               # needs sage.combinat
        ....:  sum([partition_sandpile(S, i).betti(verbose=False)[-1] for i in p])
        6
        8
        3
        sage: S.betti()                                                                 # needs sage.libs.singular
                   0     1     2     3
        ------------------------------
            0:     1     -     -     -
            1:     -     6     8     3
        ------------------------------
        total:     1     6     8     3
    """
def partition_sandpile(S, p) -> Sandpile:
    """
    Each set of vertices in `p` is regarded as a single vertex, with and edge
    between `A` and `B` if some element of `A` is connected by an edge to  some
    element of `B` in `S`.

    INPUT:

    - ``S`` -- Sandpile

    - ``p`` -- partition of the vertices of ``S``

    OUTPUT: Sandpile

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import admissible_partitions, partition_sandpile
        sage: S = sandpiles.Cycle(4)
        sage: P = [list(admissible_partitions(S, i)) for i in [2,3,4]]                  # needs sage.combinat
        sage: for p in P:                                                               # needs sage.combinat
        ....:  sum([partition_sandpile(S, i).betti(verbose=False)[-1] for i in p])
        6
        8
        3
        sage: S.betti()                                                                 # needs sage.libs.singular
                   0     1     2     3
        ------------------------------
            0:     1     -     -     -
            1:     -     6     8     3
        ------------------------------
        total:     1     6     8     3
    """
def min_cycles(G, v) -> list:
    """
    Minimal length cycles in the digraph `G` starting at vertex `v`.

    INPUT:

    - ``G`` -- DiGraph

    - ``v`` -- vertex of ``G``

    OUTPUT: list of lists of vertices

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import min_cycles, sandlib
        sage: T = sandlib('gor')
        sage: [min_cycles(T, i) for i in T.vertices(sort=True)]
        [[], [[1, 3]], [[2, 3, 1], [2, 3]], [[3, 1], [3, 2]]]
    """
def wilmes_algorithm(M):
    """
    Compute an integer matrix `L` with the same integer row span as `M` and
    such that `L` is the reduced Laplacian of a directed multigraph.

    INPUT:

    - ``M`` -- square integer matrix of full rank

    OUTPUT: integer matrix (``L``)

    EXAMPLES::

        sage: from sage.sandpiles.sandpile import wilmes_algorithm
        sage: P = matrix([[2,3,-7,-3],[5,2,-5,5],[8,2,5,4],[-5,-9,6,6]])
        sage: wilmes_algorithm(P)
        [ 3279   -79 -1599 -1600]
        [   -1  1539  -136 -1402]
        [    0    -1  1650 -1649]
        [    0     0 -1658  1658]

    REFERENCES:

    - [PPW2013]_
    """
