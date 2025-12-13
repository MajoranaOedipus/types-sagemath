import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.numerical.backends.generic_backend import get_solver as get_solver
from typing import Any, ClassVar

geodetic_closure: _cython_3_2_1.cython_function_or_method
is_geodetic: _cython_3_2_1.cython_function_or_method

class ConvexityProperties:
    """ConvexityProperties(G)

    File: /build/sagemath/src/sage/src/sage/graphs/convexity_properties.pyx (starting at line 52)

    This class gathers the algorithms related to convexity in a graph.

    **Definitions**

    A set `S \\subseteq V(G)` of vertices is said to be convex if for all `u,v\\in
    S` the set `S` contains all the vertices located on a shortest path between
    `u` and `v`. Alternatively, a set `S` is said to be convex if the distances
    satisfy `\\forall u,v\\in S, \\forall w\\in V\\backslash S : d_{G}(u,w) +
    d_{G}(w,v) > d_{G}(u,v)`.

    The convex hull `h(S)` of a set `S` of vertices is defined as the smallest
    convex set containing `S`.

    It is a closure operator, as trivially `S\\subseteq h(S)` and `h(h(S)) =
    h(S)`.

    **What this class contains**

    As operations on convex sets generally involve the computation of distances
    between vertices, this class' purpose is to cache that information so that
    computing the convex hulls of several different sets of vertices does not
    imply recomputing several times the distances between the vertices.

    In order to compute the convex hull of a set `S` it is possible to write the
    following algorithm:

        For any pair `u,v` of elements in the set `S`, and for any vertex `w`
        outside of it, add `w` to `S` if `d_{G}(u,w) + d_{G}(w,v) =
        d_{G}(u,v)`. When no vertex can be added anymore, the set `S` is convex

    The distances are not actually that relevant. The same algorithm can be
    implemented by remembering for each pair `u, v` of vertices the list of
    elements `w` satisfying the condition, and this is precisely what this class
    remembers, encoded as bitsets to make storage and union operations more
    efficient.

    .. NOTE::

        * This class is useful if you compute the convex hulls of many sets in
          the same graph, or if you want to compute the hull number itself as it
          involves many calls to :meth:`hull`

        * Using this class on non-connected graphs is a waste of space and
          efficiency ! If your graph is disconnected, the best for you is to
          deal independently with each connected component, whatever you are
          doing.

    **Possible improvements**

    When computing a convex set, all the pairs of elements belonging to the set
    `S` are enumerated several times.

    * There should be a smart way to avoid enumerating pairs of vertices which
      have already been tested. The cost of each of them is not very high, so
      keeping track of those which have been tested already may be too expensive
      to gain any efficiency.

    * The ordering in which they are visited is currently purely lexicographic,
      while there is a Poset structure to exploit. In particular, when two
      vertices `u, v` are far apart and generate a set `h(\\{u,v\\})` of vertices,
      all the pairs of vertices `u', v'\\in h(\\{u,v\\})` satisfy `h(\\{u',v'\\})
      \\subseteq h(\\{u,v\\})`, and so it is useless to test the pair `u', v'` when
      both `u` and `v` where present.

    * The information cached is for any pair `u,v` of vertices the list of
      elements `z` with `d_{G}(u,w) + d_{G}(w,v) = d_{G}(u,v)`. This is not in
      general equal to `h(\\{u,v\\})` !

    Nothing says these recommendations will actually lead to any actual
    improvements. There are just some ideas remembered while writing this
    code. Trying to optimize may well lead to lost in efficiency on many
    instances.

    EXAMPLES::

        sage: from sage.graphs.convexity_properties import ConvexityProperties
        sage: g = graphs.PetersenGraph()
        sage: CP = ConvexityProperties(g)
        sage: CP.hull([1, 3])
        [1, 2, 3]
        sage: CP.hull_number()                                                          # needs sage.numerical.mip
        3

    TESTS::

        sage: ConvexityProperties(digraphs.Circuit(5))
        Traceback (most recent call last):
        ...
        NotImplementedError: this is currently implemented for Graphs only, but only minor updates are needed if you want to make it support DiGraphs too"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/convexity_properties.pyx (starting at line 145)

                Constructor.

                EXAMPLES::

                    sage: from sage.graphs.convexity_properties import ConvexityProperties
                    sage: g = graphs.PetersenGraph()
                    sage: ConvexityProperties(g)
                    <sage.graphs.convexity_properties.ConvexityProperties object at ...>
        """
    def hull(self, listvertices) -> Any:
        """ConvexityProperties.hull(self, list vertices)

        File: /build/sagemath/src/sage/src/sage/graphs/convexity_properties.pyx (starting at line 294)

        Return the convex hull of a set of vertices.

        INPUT:

        - ``vertices`` -- list of vertices

        EXAMPLES::

            sage: from sage.graphs.convexity_properties import ConvexityProperties
            sage: g = graphs.PetersenGraph()
            sage: CP = ConvexityProperties(g)
            sage: CP.hull([1, 3])
            [1, 2, 3]"""
    def hull_number(self, value_only=..., verbose=...) -> Any:
        '''ConvexityProperties.hull_number(self, value_only=True, verbose=False)

        File: /build/sagemath/src/sage/src/sage/graphs/convexity_properties.pyx (starting at line 347)

        Compute the hull number and a corresponding generating set.

        The hull number `hn(G)` of a graph `G` is the cardinality of a smallest
        set of vertices `S` such that `h(S)=V(G)`.

        INPUT:

        - ``value_only`` -- boolean (default: ``True``); whether to return only
          the hull number (default) or a minimum set whose convex hull is the
          whole graph

        - ``verbose`` -- boolean (default: ``False``); whether to display
          information on the LP

        **COMPLEXITY:**

        This problem is NP-Hard [HLT1993]_, but seems to be of the "nice" kind.
        Update this comment if you fall on hard instances `:-)`

        **ALGORITHM:**

        This is solved by linear programming.

        As the function `h(S)` associating to each set `S` its convex hull is a
        closure operator, it is clear that any set `S_G` of vertices such that
        `h(S_G)=V(G)` must satisfy `S_G \\not \\subseteq C` for any *proper*
        convex set `C \\subsetneq V(G)`. The following formulation is hence
        correct

        .. MATH::

            \\text{Minimize :}& \\sum_{v\\in G}b_v\\\\\n            \\text{Such that :}&\\\\\n            &\\forall C\\subsetneq V(G)\\text{ a proper convex set }\\\\\n            &\\sum_{v\\in V(G)\\backslash C} b_v \\geq 1

        Of course, the number of convex sets -- and so the number of constraints
        -- can be huge, and hard to enumerate, so at first an incomplete
        formulation is solved (it is missing some constraints). If the answer
        returned by the LP solver is a set `S` generating the whole graph, then
        it is optimal and so is returned. Otherwise, the constraint
        corresponding to the set `h(S)` can be added to the LP, which makes the
        answer `S` infeasible, and another solution computed.

        This being said, simply adding the constraint corresponding to `h(S)` is
        a bit slow, as these sets can be large (and the corresponding constraint
        a bit weak). To improve it a bit, before being added, the set `h(S)` is
        "greedily enriched" to a set `S\'` with vertices for as long as
        `h(S\')\\neq V(G)`. This way, we obtain a set `S\'` with `h(S)\\subseteq
        h(S\')\\subsetneq V(G)`, and the constraint corresponding to `h(S\')` --
        which is stronger than the one corresponding to `h(S)` -- is added.

        This can actually be seen as a hitting set problem on the complement of
        convex sets.

        EXAMPLES:

        The Hull number of Petersen\'s graph::

            sage: from sage.graphs.convexity_properties import ConvexityProperties
            sage: g = graphs.PetersenGraph()
            sage: CP = ConvexityProperties(g)
            sage: CP.hull_number()                                                      # needs sage.numerical.mip
            3
            sage: generating_set = CP.hull_number(value_only=False)                     # needs sage.numerical.mip
            sage: CP.hull(generating_set)                                               # needs sage.numerical.mip
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'''
