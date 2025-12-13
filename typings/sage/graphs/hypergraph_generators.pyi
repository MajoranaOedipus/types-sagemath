from _typeshed import Incomplete
from collections.abc import Generator

class HypergraphGenerators:
    """
    A class consisting of constructors for common hypergraphs.
    """
    def nauty(self, number_of_sets, number_of_vertices, multiple_sets: bool = False, vertex_min_degree=None, vertex_max_degree=None, set_max_size=None, set_min_size=None, regular: bool = False, uniform: bool = False, max_intersection=None, connected: bool = False, debug: bool = False, options: str = '') -> Generator[Incomplete]:
        '''
        Enumerate hypergraphs up to isomorphism using Nauty.

        INPUT:

        - ``number_of_sets`` -- integer; at most 64 minus ``number_of_vertices``

        - ``number_of_vertices`` -- integer; at most 30

        - ``multiple_sets`` -- boolean (default: ``False``); whether to allow
          several sets of the hypergraph to be equal

        - ``vertex_min_degree``, ``vertex_max_degree`` -- integers (default:
          ``None``); define the maximum and minimum degree of an element from
          the ground set (i.e. the number of sets which contain it)

        - ``set_min_size``, ``set_max_size`` -- integers (default: ``None``);
          define the maximum and minimum size of a set

        - ``regular`` -- integer (default: ``False``); if set to an integer
          value `k`, requires the hypergraphs to be `k`-regular. It is actually
          a shortcut for the corresponding min/max values.

        - ``uniform`` -- integer (default: ``False``); if set to an integer
          value `k`, requires the hypergraphs to be `k`-uniform. It is actually
          a shortcut for the corresponding min/max values.

        - ``max_intersection`` -- integer (default: ``None``); constraints the
          maximum cardinality of the intersection of two sets from the
          hypergraphs

        - ``connected`` -- boolean (default: ``False``); whether to require the
          hypergraphs to be connected

        - ``debug`` -- boolean (default: ``False``); if ``True`` the first line
          of genbgL\'s output to standard error is captured and the first call to
          the generator\'s ``next()`` function will return this line as a string.
          A line leading with ">A" indicates a successful initiation of the
          program with some information on the arguments, while a line beginning
          with ">E" indicates an error with the input.

        - ``options`` -- string (default: ``\'\'``); anything else that should
          be forwarded as input to Nauty\'s genbgL. See its documentation for more
          information : `<http://cs.anu.edu.au/~bdm/nauty/>`_.

          .. NOTE::

              For genbgL the *first class* elements are vertices, and *second
              class* elements are the hypergraph\'s sets.

        OUTPUT: a tuple of tuples

        EXAMPLES:

        Small hypergraphs::

            sage: list(hypergraphs.nauty(4, 2))
            [((), (0,), (1,), (0, 1))]

        Only connected ones::

            sage: list(hypergraphs.nauty(2, 2, connected=True))
            [((0,), (0, 1))]

        Non-empty sets only::

            sage: list(hypergraphs.nauty(3, 2, set_min_size=1))
            [((0,), (1,), (0, 1))]

        The Fano Plane, as the only 3-uniform hypergraph with 7 sets and 7
        vertices::

            sage: fano = next(hypergraphs.nauty(7, 7, uniform=3, max_intersection=1))
            sage: print(fano)
            ((0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (2, 4, 5), (2, 3, 6), (1, 4, 6))

        The Fano Plane, as the only 3-regular hypergraph with 7 sets and 7
        vertices::

            sage: fano = next(hypergraphs.nauty(7, 7, regular=3, max_intersection=1))
            sage: print(fano)
            ((0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (2, 4, 5), (2, 3, 6), (1, 4, 6))

        TESTS::

            sage: len(list(hypergraphs.nauty(20, 20, uniform=2, regular=2,max_intersection=1)))
            49
            sage: list(hypergraphs.nauty(40, 40, uniform=2, regular=2,max_intersection=1))
            Traceback (most recent call last):
            ...
            ValueError: cannot have more than 30 vertices
            sage: list(hypergraphs.nauty(40, 30, uniform=2, regular=2,max_intersection=1))
            Traceback (most recent call last):
            ...
            ValueError: cannot have more than 64 sets+vertices
        '''
    def CompleteUniform(self, n, k):
        """
        Return the complete `k`-uniform hypergraph on `n` points.

        INPUT:

        - ``k``, ``n`` -- nonnegative integers with `k\\leq n`

        EXAMPLES::

            sage: h = hypergraphs.CompleteUniform(5, 2); h
            Incidence structure with 5 points and 10 blocks
            sage: len(h.packing())                                                      # needs sage.numerical.mip
            2
        """
    def UniformRandomUniform(self, n, k, m):
        """
        Return a uniformly sampled `k`-uniform hypergraph on `n` points with
        `m` hyperedges.

        - ``n`` -- number of nodes of the graph

        - ``k`` -- uniformity

        - ``m`` -- number of edges

        EXAMPLES::

            sage: H = hypergraphs.UniformRandomUniform(52, 3, 17)
            sage: H
            Incidence structure with 52 points and 17 blocks
            sage: H.is_connected()
            False

        TESTS::

            sage: hypergraphs.UniformRandomUniform(-52, 3, 17)
            Traceback (most recent call last):
            ...
            ValueError: number of vertices should be nonnegative
            sage: hypergraphs.UniformRandomUniform(52.9, 3, 17)
            Traceback (most recent call last):
            ...
            ValueError: number of vertices should be an integer
            sage: hypergraphs.UniformRandomUniform(52, -3, 17)
            Traceback (most recent call last):
            ...
            ValueError: the uniformity should be nonnegative
            sage: hypergraphs.UniformRandomUniform(52, I, 17)                           # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: the uniformity should be an integer
        """
    def BinomialRandomUniform(self, n, k, p):
        """
        Return a random `k`-uniform hypergraph on `n` points, in which each
        edge is inserted independently with probability `p`.

        - ``n`` -- number of nodes of the graph

        - ``k`` -- uniformity

        - ``p`` -- probability of an edge

        EXAMPLES::

            sage: hypergraphs.BinomialRandomUniform(50, 3, 1).num_blocks()              # needs numpy, long time
            19600
            sage: hypergraphs.BinomialRandomUniform(50, 3, 0).num_blocks()              # needs numpy
            0

        TESTS::

            sage: # needs numpy
            sage: hypergraphs.BinomialRandomUniform(50, 3, -0.1)
            Traceback (most recent call last):
            ...
            ValueError: edge probability should be in [0,1]
            sage: hypergraphs.BinomialRandomUniform(50, 3, 1.1)
            Traceback (most recent call last):
            ...
            ValueError: edge probability should be in [0,1]
            sage: hypergraphs.BinomialRandomUniform(-50, 3, 0.17)
            Traceback (most recent call last):
            ...
            ValueError: number of vertices should be nonnegative
            sage: hypergraphs.BinomialRandomUniform(50.9, 3, 0.17)
            Traceback (most recent call last):
            ...
            ValueError: number of vertices should be an integer
            sage: hypergraphs.BinomialRandomUniform(50, -3, 0.17)
            Traceback (most recent call last):
            ...
            ValueError: the uniformity should be nonnegative
            sage: hypergraphs.BinomialRandomUniform(50, I, 0.17)
            Traceback (most recent call last):
            ...
            ValueError: the uniformity should be an integer
        """

hypergraphs: Incomplete
