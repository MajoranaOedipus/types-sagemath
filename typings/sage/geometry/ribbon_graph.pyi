from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class RibbonGraph(SageObject, UniqueRepresentation):
    '''
    A ribbon graph codified as two elements of a certain permutation group.

    A comprehensive introduction on the topic can be found in the beginning
    of [GGD2011]_ Chapter 4. More concretely, we will use a variation of what
    is called in the reference "The permutation representation pair of a
    dessin". Note that in that book, ribbon graphs are called "dessins
    d\'enfant". For the sake on completeness we reproduce an adapted version
    of that introduction here.

    **Brief introduction**

    Let `\\Sigma` be an orientable surface with non-empty boundary and let
    `\\Gamma` be the topological realization of a graph that is embedded in
    `\\Sigma` in such a way that the graph is a strong deformation retract of
    the surface.

    Let `v(\\Gamma)` be the set of vertices of `\\Gamma`, suppose that these
    are white vertices. Now we mark black vertices in an interior point
    of each edge. In this way we get a bipartite graph where all the black
    vertices have valency 2 and there is no restriction on the valency
    of the white vertices. We call the edges of this new graph *darts*
    (sometimes they are also called *half edges* of the original graph).
    Observe that each edge of the original graph is formed by two darts.

    Given a white vertex `v \\in v(\\Gamma)`, let `d(v)` be the set of darts
    adjacent to `v`. Let `D(\\Gamma)` be the set of all the darts of
    `\\Gamma` and suppose that we enumerate the set `D(\\Gamma)` and that it
    has `n` elements.

    With the orientation of the surface and the embedding of the graph in
    the surface we can produce two permutations:

    - A permutation that we denote by `\\sigma`. This permutation is a
      product of as many cycles as white vertices (that is vertices in
      `\\Gamma`). For each vertex consider a small topological circle
      around it in `\\Sigma`. This circle intersects each adjacent dart
      once. The circle has an orientation induced by the orientation on
      `\\Sigma` and so defines a cycle that sends the number associated
      to one dart to the number associated to the next dart in the
      positive orientation of the circle.

    - A permutation that we denote by `\\rho`. This permutation is a
      product of as many `2`-cycles as edges has `\\Gamma`. It just tells
      which two darts belong to the same edge.

    .. RUBRIC:: Abstract definition

    Consider a graph `\\Gamma` (not a priori embedded in any surface).
    Now we can again consider one vertex in the interior of each edge
    splitting each edge in two darts. We label the darts with numbers.

    We say that a ribbon structure on `\\Gamma` is a set of two
    permutations `(\\sigma, \\rho)`. Where `\\sigma` is formed by as many
    disjoint cycles as vertices had `\\Gamma`. And each cycle is a
    cyclic ordering of the darts adjacent to a vertex. The permutation
    `\\rho` just tell us which two darts belong to the same edge.

    For any two such permutations there is a way of "thickening" the
    graph to a surface with boundary in such a way that the surface
    retracts (by a strong deformation retract) to the graph and hence
    the graph is embedded in the surface in a such a way that we could
    recover `\\sigma` and `\\rho`.

    INPUT:

    - ``sigma`` -- a permutation a product of disjoint cycles of any
      length; singletons (vertices of valency 1) need not be specified
    - ``rho`` -- a permutation which is a product of disjoint 2-cycles

    Alternatively, one can pass in 2 integers and this will construct
    a ribbon graph with genus ``sigma`` and ``rho`` boundary components.
    See :func:`~sage.geometry.ribbon_graphs.make_ribbon`.

    One can also construct the bipartite graph modeling the
    corresponding Brieskorn-Pham singularity by passing 2 integers
    and the keyword ``bipartite=True``.
    See :func:`~sage.geometry.ribbon_graphs.bipartite_ribbon_graph`.

    EXAMPLES:

    Consider the ribbon graph consisting of just `1` edge and `2`
    vertices of valency `1`::

        sage: s0 = PermutationGroupElement(\'(1)(2)\')
        sage: r0 = PermutationGroupElement(\'(1,2)\')
        sage: R0 = RibbonGraph(s0,r0); R0
        Ribbon graph of genus 0 and 1 boundary components

    Consider a graph that has `2` vertices of valency `3` (and hence `3`
    edges). That is represented by the following two permutations::

        sage: s1 = PermutationGroupElement(\'(1,3,5)(2,4,6)\')
        sage: r1 = PermutationGroupElement(\'(1,2)(3,4)(5,6)\')
        sage: R1 = RibbonGraph(s1, r1); R1
        Ribbon graph of genus 1 and 1 boundary components

    By drawing the picture in a piece of paper, one can see that its
    thickening has only `1` boundary component. Since the thickening
    is homotopically equivalent to the graph and the graph has Euler
    characteristic `-1`, we find that the thickening has genus `1`::

        sage: R1.number_boundaries()
        1
        sage: R1.genus()
        1

    The following example corresponds to the  complete bipartite graph
    of type `(2,3)`, where we have added one more edge `(8,15)` that
    ends at a vertex of valency `1`. Observe that it is not necessary
    to specify the  vertex `(15)` of valency `1` when we define sigma::

        sage: s2 = PermutationGroupElement(\'(1,3,5,8)(2,4,6)\')
        sage: r2 = PermutationGroupElement(\'(1,2)(3,4)(5,6)(8,15)\')
        sage: R2 = RibbonGraph(s2, r2); R1
        Ribbon graph of genus 1 and 1 boundary components
        sage: R2.sigma()
        (1,3,5,8)(2,4,6)

    This example is constructed by taking the bipartite graph of
    type `(3,3)`::

        sage: s3 = PermutationGroupElement(\'(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18)\')
        sage: r3 = PermutationGroupElement(\'(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)\')
        sage: R3 = RibbonGraph(s3, r3); R3
        Ribbon graph of genus 1 and 3 boundary components

    The labeling of the darts can omit some numbers::

        sage: s4 = PermutationGroupElement(\'(3,5,10,12)\')
        sage: r4 = PermutationGroupElement(\'(3,10)(5,12)\')
        sage: R4 = RibbonGraph(s4,r4); R4
        Ribbon graph of genus 1 and 1 boundary components

    The next example is the complete bipartite graph of type `(3,3)`, where we
    have added an edge that ends at a vertex of valency 1::

        sage: s5 = PermutationGroupElement(\'(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18,19)\')
        sage: r5 = PermutationGroupElement(\'(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)(19,20)\')
        sage: R5 = RibbonGraph(s5,r5); R5
        Ribbon graph of genus 1 and 3 boundary components
        sage: C = R5.contract_edge(9); C
        Ribbon graph of genus 1 and 3 boundary components
        sage: C.sigma()
        (1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18)
        sage: C.rho()
        (1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)
        sage: S = R5.reduced(); S
        Ribbon graph of genus 1 and 3 boundary components
        sage: S.sigma()
        (5,6,8,9,14,15,11,12)
        sage: S.rho()
        (5,14)(6,11)(8,15)(9,12)
        sage: R5.boundary()
        [[1, 16, 17, 4, 5, 14, 15, 8, 9, 12, 10, 3],
         [2, 13, 14, 5, 6, 11, 12, 9, 7, 18, 19, 20, 20, 19, 16, 1],
         [3, 10, 11, 6, 4, 17, 18, 7, 8, 15, 13, 2]]
        sage: S.boundary()
        [[5, 14, 15, 8, 9, 12], [6, 11, 12, 9, 14, 5], [8, 15, 11, 6]]
        sage: R5.homology_basis()
        [[[5, 14], [13, 2], [1, 16], [17, 4]],
         [[6, 11], [10, 3], [1, 16], [17, 4]],
         [[8, 15], [13, 2], [1, 16], [18, 7]],
         [[9, 12], [10, 3], [1, 16], [18, 7]]]
        sage: S.homology_basis()
        [[[5, 14]], [[6, 11]], [[8, 15]], [[9, 12]]]

    We construct a ribbon graph corresponding to a genus 0 surface
    with 5 boundary components::

        sage: R = RibbonGraph(0, 5); R
        Ribbon graph of genus 0 and 5 boundary components
        sage: R.sigma()
        (1,9,7,5,3)(2,4,6,8,10)
        sage: R.rho()
        (1,2)(3,4)(5,6)(7,8)(9,10)

    We construct the Brieskorn-Pham singularity of type `(2,3)`::

        sage: B23 = RibbonGraph(2, 3, bipartite=True); B23
        Ribbon graph of genus 1 and 1 boundary components
        sage: B23.sigma()
        (1,2,3)(4,5,6)(7,8)(9,10)(11,12)
        sage: B23.rho()
        (1,8)(2,10)(3,12)(4,7)(5,9)(6,11)
    '''
    @staticmethod
    def __classcall_private__(cls, sigma, rho, bipartite: bool = False):
        """
        Normalize input.

        EXAMPLES::

            sage: s1 = PermutationGroupElement('(1,3,5,8)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)(8,15)')
            sage: R1 = RibbonGraph(s1, r1)
            sage: s2 = PermutationGroupElement('(1,3,5,8)(2,4,6)(15)')
            sage: R2 = RibbonGraph(s2, r1)
            sage: R1 is R2
            True
        """
    def __init__(self, sigma, rho) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: s0 = PermutationGroupElement('(1)(2)')
            sage: r0 = PermutationGroupElement('(1,2)')
            sage: R0 = RibbonGraph(s0,r0)
            sage: TestSuite(R0).run()

            sage: s1 = PermutationGroupElement('(1,3,5,8)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)(8,15)')
            sage: R1 = RibbonGraph(s1, r1)
            sage: TestSuite(R1).run()

            sage: s2 = PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18)')
            sage: r2 = PermutationGroupElement('(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)')
            sage: R2 = RibbonGraph(s2, r2)
            sage: TestSuite(R2).run()
        """
    def sigma(self):
        """
        Return the permutation `\\sigma` of ``self``.

        EXAMPLES::

            sage: s1 = PermutationGroupElement('(1,3,5,8)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)(8,15)')
            sage: R = RibbonGraph(s1, r1)
            sage: R.sigma()
            (1,3,5,8)(2,4,6)
        """
    def rho(self):
        """
        Return the permutation `\\rho` of ``self``.

        EXAMPLES::

            sage: s1 = PermutationGroupElement('(1,3,5,8)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)(8,15)')
            sage: R = RibbonGraph(s1, r1)
            sage: R.rho()
            (1,2)(3,4)(5,6)(8,15)
        """
    @cached_method
    def number_boundaries(self):
        """
        Return number of boundary components of the thickening of the
        ribbon graph.

        EXAMPLES:

        The first example is the ribbon graph corresponding to the torus
        with one hole::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1)
            sage: R1.number_boundaries()
            1

        This example is constructed by taking the bipartite graph of
        type `(3,3)`::

            sage: s2 = PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18)')
            sage: r2 = PermutationGroupElement('(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)')
            sage: R2 = RibbonGraph(s2,r2)
            sage: R2.number_boundaries()
            3
        """
    def contract_edge(self, k):
        """
        Return the ribbon graph resulting from the contraction of
        the ``k``-th edge in ``self``.

        For a ribbon graph `(\\sigma, \\rho)`, we contract the edge
        corresponding to the `k`-th transposition of `\\rho`.

        INPUT:

        - ``k`` -- nonnegative integer; the position in `\\rho` of the
          transposition that is going to be contracted

        OUTPUT: a ribbon graph resulting from the contraction of that edge

        EXAMPLES:

        We start again with the one-holed torus ribbon graph::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1); R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: S1 = R1.contract_edge(1); S1
            Ribbon graph of genus 1 and 1 boundary components
            sage: S1.sigma()
            (1,6,2,5)
            sage: S1.rho()
            (1,2)(5,6)

        However, this ribbon graphs is formed only by loops and hence
        it cannot be longer reduced, we get an error if we try to
        contract a loop::

            sage: S1.contract_edge(1)
            Traceback (most recent call last):
            ...
            ValueError: the edge is a loop and cannot be contracted

        In this example, we consider a graph that has one edge ``(19,20)``
        such that one of its ends is a vertex of valency 1. This is
        the vertex ``(20)`` that is not specified when defining `\\sigma`.
        We contract precisely this edge and get a ribbon graph with no
        vertices of valency 1::

            sage: s2 = PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18,19)')
            sage: r2 = PermutationGroupElement('(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)(19,20)')
            sage: R2 = RibbonGraph(s2,r2); R2
            Ribbon graph of genus 1 and 3 boundary components
            sage: R2.sigma()
            (1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18,19)
            sage: R2c = R2.contract_edge(9); R2; R2c.sigma(); R2c.rho()
            Ribbon graph of genus 1 and 3 boundary components
            (1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18)
            (1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)
        """
    def extrude_edge(self, vertex, dart1, dart2):
        """
        Return a ribbon graph resulting from extruding an edge from a
        vertex, pulling from it, all darts from ``dart1`` to ``dart2``
        including both.

        INPUT:

        - ``vertex`` -- the position of the vertex in the permutation
          `\\sigma`, which must have valency at least 2

        - ``dart1`` -- the position of the first in the
          cycle corresponding to ``vertex``

        - ``dart2`` -- the position of the second dart in the cycle
          corresponding to ``vertex``

        OUTPUT:

        A ribbon graph resulting from extruding a new edge that
        pulls from ``vertex`` a new vertex that is, now, adjacent
        to all the darts from ``dart1``to ``dart2`` (not including
        ``dart2``) in the cyclic ordering given by the cycle corresponding
        to ``vertex``. Note that ``dart1`` may be equal to ``dart2``
        allowing thus to extrude a contractible edge from a vertex.

        EXAMPLES:

        We try several possibilities in the same graph::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1); R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: E1 = R1.extrude_edge(1,1,2); E1
            Ribbon graph of genus 1 and 1 boundary components
            sage: E1.sigma()
            (1,3,5)(2,8,6)(4,7)
            sage: E1.rho()
            (1,2)(3,4)(5,6)(7,8)
            sage: E2 = R1.extrude_edge(1,1,3); E2
            Ribbon graph of genus 1 and 1 boundary components
            sage: E2.sigma()
            (1,3,5)(2,8)(4,6,7)
            sage: E2.rho()
            (1,2)(3,4)(5,6)(7,8)

        We can also extrude a contractible edge from a vertex. This
        new edge will end at a vertex of valency 1::

            sage: E1p = R1.extrude_edge(0,0,0); E1p
            Ribbon graph of genus 1 and 1 boundary components
            sage: E1p.sigma()
            (1,3,5,8)(2,4,6)
            sage: E1p.rho()
            (1,2)(3,4)(5,6)(7,8)

        In the following example we first extrude one edge from a vertex
        of valency 3 generating a new vertex of valency 2. Then we
        extrude a new edge from this vertex of valency 2::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1); R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: E1 = R1.extrude_edge(0,0,1); E1
            Ribbon graph of genus 1 and 1 boundary components
            sage: E1.sigma()
            (1,7)(2,4,6)(3,5,8)
            sage: E1.rho()
            (1,2)(3,4)(5,6)(7,8)
            sage: F1 = E1.extrude_edge(0,0,1); F1
            Ribbon graph of genus 1 and 1 boundary components
            sage: F1.sigma()
            (1,9)(2,4,6)(3,5,8)(7,10)
            sage: F1.rho()
            (1,2)(3,4)(5,6)(7,8)(9,10)
        """
    @cached_method
    def genus(self):
        """
        Return the genus of the thickening of ``self``.

        OUTPUT:

        - ``g`` -- nonnegative integer representing the genus of the
          thickening of the ribbon graph

        EXAMPLES::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1)
            sage: R1.genus()
            1

            sage: s3=PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15,16)(17,18,19,20)(21,22,23,24)')
            sage: r3=PermutationGroupElement('(1,21)(2,17)(3,13)(4,22)(7,23)(5,18)(6,14)(8,19)(9,15)(10,24)(11,20)(12,16)')
            sage: R3 = RibbonGraph(s3,r3); R3.genus()
            3
        """
    def mu(self):
        """
        Return the rank of the first homology group of the thickening
        of the ribbon graph.

        EXAMPLES::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1);R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: R1.mu()
            2
        """
    def boundary(self):
        """
        Return the labeled boundaries of ``self``.

        If you cut the thickening of the graph along the graph. you
        get a collection of cylinders (recall that the graph was a
        strong deformation retract of the thickening). In each cylinder
        one of the boundary components has a labelling of its edges
        induced by the labelling of the darts.

        OUTPUT:

        A list of lists. The number of inner lists is the number of
        boundary components of the surface. Each list in the list
        consists of an ordered tuple of numbers, each number comes
        from the number assigned to the corresponding dart before
        cutting.

        EXAMPLES:

        We start with a ribbon graph whose thickening has one boundary
        component. We compute its labeled boundary, then reduce it and
        compute the labeled boundary of the reduced  ribbon graph::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1); R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: R1.boundary()
            [[1, 2, 4, 3, 5, 6, 2, 1, 3, 4, 6, 5]]
            sage: H1 = R1.reduced(); H1
            Ribbon graph of genus 1 and 1 boundary components
            sage: H1.sigma()
            (3,5,4,6)
            sage: H1.rho()
            (3,4)(5,6)
            sage: H1.boundary()
            [[3, 4, 6, 5, 4, 3, 5, 6]]

        We now consider a ribbon graph whose thickening has 3 boundary
        components. Also observe that in one of the labeled boundary
        components, a numbers appears twice in a row. That is because
        the ribbon graph has a vertex of valency 1::

            sage: s2=PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18,19)')
            sage: r2=PermutationGroupElement('(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)(19,20)')
            sage: R2 = RibbonGraph(s2,r2)
            sage: R2.number_boundaries()
            3
            sage: R2.boundary()
            [[1, 16, 17, 4, 5, 14, 15, 8, 9, 12, 10, 3],
             [2, 13, 14, 5, 6, 11, 12, 9, 7, 18, 19, 20, 20, 19, 16, 1],
             [3, 10, 11, 6, 4, 17, 18, 7, 8, 15, 13, 2]]
        """
    def reduced(self):
        """
        Return a ribbon graph with 1 vertex and `\\mu` edges (where `\\mu`
        is the first betti number of the graph).

        OUTPUT:

        - a ribbon graph whose `\\sigma` permutation has only 1 non-singleton
          cycle and whose `\\rho` permutation is a product of `\\mu` disjoint
          2-cycles

        EXAMPLES::

            sage: s1 = PermutationGroupElement('(1,3,5)(2,4,6)')
            sage: r1 = PermutationGroupElement('(1,2)(3,4)(5,6)')
            sage: R1 = RibbonGraph(s1,r1); R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: G1 = R1.reduced(); G1
            Ribbon graph of genus 1 and 1 boundary components
            sage: G1.sigma()
            (3,5,4,6)
            sage: G1.rho()
            (3,4)(5,6)

            sage: s2 = PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18,19)')
            sage: r2 = PermutationGroupElement('(1,16)(2,13)(3,10)(4,17)(5,14)(6,11)(7,18)(8,15)(9,12)(19,20)')
            sage: R2 = RibbonGraph(s2,r2); R2
            Ribbon graph of genus 1 and 3 boundary components
            sage: G2 = R2.reduced(); G2
            Ribbon graph of genus 1 and 3 boundary components
            sage: G2.sigma()
            (5,6,8,9,14,15,11,12)
            sage: G2.rho()
            (5,14)(6,11)(8,15)(9,12)

            sage: s3 = PermutationGroupElement('(1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15,16)(17,18,19,20)(21,22,23,24)')
            sage: r3 = PermutationGroupElement('(1,21)(2,17)(3,13)(4,22)(7,23)(5,18)(6,14)(8,19)(9,15)(10,24)(11,20)(12,16)')
            sage: R3 = RibbonGraph(s3,r3); R3
            Ribbon graph of genus 3 and 1 boundary components
            sage: G3 = R3.reduced(); G3
            Ribbon graph of genus 3 and 1 boundary components
            sage: G3.sigma()
            (5,6,8,9,11,12,18,19,20,14,15,16)
            sage: G3.rho()
            (5,18)(6,14)(8,19)(9,15)(11,20)(12,16)
        """
    def make_generic(self):
        """
        Return a ribbon graph equivalent to ``self`` but where every
        vertex has valency 3.

        OUTPUT:

        - a ribbon graph that is equivalent to ``self`` but is generic
          in the sense that all vertices have valency 3

        EXAMPLES::

            sage: R = RibbonGraph(1,3); R
            Ribbon graph of genus 1 and 3 boundary components
            sage: R.sigma()
            (1,2,3,9,7)(4,8,10,5,6)
            sage: R.rho()
            (1,4)(2,5)(3,6)(7,8)(9,10)
            sage: G = R.make_generic(); G
            Ribbon graph of genus 1 and 3 boundary components
            sage: G.sigma()
            (2,3,11)(5,6,13)(7,8,15)(9,16,17)(10,14,19)(12,18,21)(20,22)
            sage: G.rho()
            (2,5)(3,6)(7,8)(9,10)(11,12)(13,14)(15,16)(17,18)(19,20)(21,22)
            sage: R.genus() == G.genus() and R.number_boundaries() == G.number_boundaries()
            True

            sage: R = RibbonGraph(5,4); R
            Ribbon graph of genus 5 and 4 boundary components
            sage: R.sigma()
            (1,2,3,4,5,6,7,8,9,10,11,27,25,23)(12,24,26,28,13,14,15,16,17,18,19,20,21,22)
            sage: R.rho()
            (1,12)(2,13)(3,14)(4,15)(5,16)(6,17)(7,18)(8,19)(9,20)(10,21)(11,22)(23,24)(25,26)(27,28)
            sage: G = R.reduced(); G
            Ribbon graph of genus 5 and 4 boundary components
            sage: G.sigma()
            (2,3,4,5,6,7,8,9,10,11,27,25,23,24,26,28,13,14,15,16,17,18,19,20,21,22)
            sage: G.rho()
            (2,13)(3,14)(4,15)(5,16)(6,17)(7,18)(8,19)(9,20)(10,21)(11,22)(23,24)(25,26)(27,28)
            sage: G.genus() == R.genus() and G.number_boundaries() == R.number_boundaries()
            True

            sage: R = RibbonGraph(0,6); R
            Ribbon graph of genus 0 and 6 boundary components
            sage: R.sigma()
            (1,11,9,7,5,3)(2,4,6,8,10,12)
            sage: R.rho()
            (1,2)(3,4)(5,6)(7,8)(9,10)(11,12)
            sage: G = R.reduced(); G
            Ribbon graph of genus 0 and 6 boundary components
            sage: G.sigma()
            (3,4,6,8,10,12,11,9,7,5)
            sage: G.rho()
            (3,4)(5,6)(7,8)(9,10)(11,12)
            sage: G.genus() == R.genus() and G.number_boundaries() == R.number_boundaries()
            True
        """
    def homology_basis(self):
        """
        Return an oriented basis of the first homology group of the
        graph.

        OUTPUT:

        - A 2-dimensional array of ordered edges in the graph (given by pairs).
          The length of the first dimension is `\\mu`. Each row corresponds
          to an element of the basis and is a circle contained in the graph.

        EXAMPLES::

            sage: R = RibbonGraph(0,6); R
            Ribbon graph of genus 0 and 6 boundary components
            sage: R.mu()
            5
            sage: R.homology_basis()
            [[[3, 4], [2, 1]],
             [[5, 6], [2, 1]],
             [[7, 8], [2, 1]],
             [[9, 10], [2, 1]],
             [[11, 12], [2, 1]]]

            sage: R = RibbonGraph(1,1); R
            Ribbon graph of genus 1 and 1 boundary components
            sage: R.mu()
            2
            sage: R.homology_basis()
            [[[2, 5], [4, 1]], [[3, 6], [4, 1]]]
            sage: H = R.reduced(); H
            Ribbon graph of genus 1 and 1 boundary components
            sage: H.sigma()
            (2,3,5,6)
            sage: H.rho()
            (2,5)(3,6)
            sage: H.homology_basis()
            [[[2, 5]], [[3, 6]]]

            sage: s3 = PermutationGroupElement('(1,2,3,4,5,6,7,8,9,10,11,27,25,23)(12,24,26,28,13,14,15,16,17,18,19,20,21,22)')
            sage: r3 = PermutationGroupElement('(1,12)(2,13)(3,14)(4,15)(5,16)(6,17)(7,18)(8,19)(9,20)(10,21)(11,22)(23,24)(25,26)(27,28)')
            sage: R3 = RibbonGraph(s3,r3); R3
            Ribbon graph of genus 5 and 4 boundary components
            sage: R3.mu()
            13
            sage: R3.homology_basis()
            [[[2, 13], [12, 1]],
             [[3, 14], [12, 1]],
             [[4, 15], [12, 1]],
             [[5, 16], [12, 1]],
             [[6, 17], [12, 1]],
             [[7, 18], [12, 1]],
             [[8, 19], [12, 1]],
             [[9, 20], [12, 1]],
             [[10, 21], [12, 1]],
             [[11, 22], [12, 1]],
             [[23, 24], [12, 1]],
             [[25, 26], [12, 1]],
             [[27, 28], [12, 1]]]
            sage: H3 = R3.reduced(); H3
            Ribbon graph of genus 5 and 4 boundary components
            sage: H3.sigma()
            (2,3,4,5,6,7,8,9,10,11,27,25,23,24,26,28,13,14,15,16,17,18,19,20,21,22)
            sage: H3.rho()
            (2,13)(3,14)(4,15)(5,16)(6,17)(7,18)(8,19)(9,20)(10,21)(11,22)(23,24)(25,26)(27,28)
            sage: H3.homology_basis()
            [[[2, 13]],
             [[3, 14]],
             [[4, 15]],
             [[5, 16]],
             [[6, 17]],
             [[7, 18]],
             [[8, 19]],
             [[9, 20]],
             [[10, 21]],
             [[11, 22]],
             [[23, 24]],
             [[25, 26]],
             [[27, 28]]]
        """
    def normalize(self):
        """
        Return an equivalent graph such that the enumeration of its darts
        exhausts all numbers from 1 to the number of darts.

        OUTPUT:

        - a ribbon graph equivalent to ``self`` such that the enumeration
          of its darts exhausts all numbers from 1 to the number of darts.

        EXAMPLES::

            sage: s0 = PermutationGroupElement('(1,22,3,4,5,6,7,15)(8,16,9,10,11,12,13,14)')
            sage: r0 = PermutationGroupElement('(1,8)(22,9)(3,10)(4,11)(5,12)(6,13)(7,14)(15,16)')
            sage: R0 = RibbonGraph(s0,r0); R0
            Ribbon graph of genus 3 and 2 boundary components
            sage: RN0 = R0.normalize(); RN0; RN0.sigma(); RN0.rho()
            Ribbon graph of genus 3 and 2 boundary components
            (1,16,2,3,4,5,6,14)(7,15,8,9,10,11,12,13)
            (1,7)(2,9)(3,10)(4,11)(5,12)(6,13)(8,16)(14,15)

            sage: s1 = PermutationGroupElement('(5,10,12)(30,34,78)')
            sage: r1 = PermutationGroupElement('(5,30)(10,34)(12,78)')
            sage: R1 = RibbonGraph(s1,r1); R1
            Ribbon graph of genus 1 and 1 boundary components
            sage: RN1 = R1.normalize(); RN1; RN1.sigma(); RN1.rho()
            Ribbon graph of genus 1 and 1 boundary components
            (1,2,3)(4,5,6)
            (1,4)(2,5)(3,6)
        """

def make_ribbon(g, r):
    """
    Return a ribbon graph whose thickening has genus ``g`` and ``r``
    boundary components.

    INPUT:

    - ``g`` -- nonnegative integer representing the genus of the
      thickening

    - ``r`` -- positive integer representing the number of boundary
      components of the thickening

    OUTPUT:

    - a ribbon graph that has 2 vertices (two non-trivial cycles
      in its sigma permutation) of valency `2g + r` and it has
      `2g + r` edges (and hence `4g + 2r` darts)

    EXAMPLES::

        sage: from sage.geometry.ribbon_graph import make_ribbon
        sage: R = make_ribbon(0,1); R
        Ribbon graph of genus 0 and 1 boundary components
        sage: R.sigma()
        ()
        sage: R.rho()
        (1,2)

        sage: R = make_ribbon(0,5); R
        Ribbon graph of genus 0 and 5 boundary components
        sage: R.sigma()
        (1,9,7,5,3)(2,4,6,8,10)
        sage: R.rho()
        (1,2)(3,4)(5,6)(7,8)(9,10)

        sage: R = make_ribbon(1,1); R
        Ribbon graph of genus 1 and 1 boundary components
        sage: R.sigma()
        (1,2,3)(4,5,6)
        sage: R.rho()
        (1,4)(2,5)(3,6)

        sage: R = make_ribbon(7,3); R
        Ribbon graph of genus 7 and 3 boundary components
        sage: R.sigma()
        (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,33,31)(16,32,34,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
        sage: R.rho()
        (1,16)(2,17)(3,18)(4,19)(5,20)(6,21)(7,22)(8,23)(9,24)(10,25)(11,26)(12,27)(13,28)(14,29)(15,30)(31,32)(33,34)
    """
def bipartite_ribbon_graph(p, q):
    """
    Return the bipartite graph modeling the corresponding
    Brieskorn-Pham singularity.

    Take two parallel lines in the plane, and consider `p` points in
    one of them and `q` points in the other. Join with a line each
    point from the first set with every point with the second set.
    The resulting is a planar projection of the complete bipartite
    graph of type `(p,q)`. If you consider the cyclic ordering at
    each vertex induced by the positive orientation of the plane,
    the result is a ribbon graph whose associated orientable surface
    with boundary is homeomorphic to the Milnor fiber of the
    Brieskorn-Pham singularity `x^p + y^q`. It satisfies that it has
    `\\gcd(p,q)` number of  boundary components and genus
    `(pq - p - q - \\gcd(p,q) - 2) / 2`.

    INPUT:

    - ``p`` -- positive integer
    - ``q`` -- positive integer

    EXAMPLES::

        sage: B23 = RibbonGraph(2,3,bipartite=True); B23; B23.sigma(); B23.rho()
        Ribbon graph of genus 1 and 1 boundary components
        (1,2,3)(4,5,6)(7,8)(9,10)(11,12)
        (1,8)(2,10)(3,12)(4,7)(5,9)(6,11)

        sage: B32 = RibbonGraph(3,2,bipartite=True); B32; B32.sigma(); B32.rho()
        Ribbon graph of genus 1 and 1 boundary components
        (1,2)(3,4)(5,6)(7,8,9)(10,11,12)
        (1,9)(2,12)(3,8)(4,11)(5,7)(6,10)

        sage: B33 = RibbonGraph(3,3,bipartite=True); B33; B33.sigma(); B33.rho()
        Ribbon graph of genus 1 and 3 boundary components
        (1,2,3)(4,5,6)(7,8,9)(10,11,12)(13,14,15)(16,17,18)
        (1,12)(2,15)(3,18)(4,11)(5,14)(6,17)(7,10)(8,13)(9,16)

        sage: B24 = RibbonGraph(2,4,bipartite=True); B24; B24.sigma(); B24.rho()
        Ribbon graph of genus 1 and 2 boundary components
        (1,2,3,4)(5,6,7,8)(9,10)(11,12)(13,14)(15,16)
        (1,10)(2,12)(3,14)(4,16)(5,9)(6,11)(7,13)(8,15)

        sage: B47 = RibbonGraph(4,7, bipartite=True); B47; B47.sigma(); B47.rho()
        Ribbon graph of genus 9 and 1 boundary components
        (1,2,3,4,5,6,7)(8,9,10,11,12,13,14)(15,16,17,18,19,20,21)(22,23,24,25,26,27,28)(29,30,31,32)(33,34,35,36)(37,38,39,40)(41,42,43,44)(45,46,47,48)(49,50,51,52)(53,54,55,56)
        (1,32)(2,36)(3,40)(4,44)(5,48)(6,52)(7,56)(8,31)(9,35)(10,39)(11,43)(12,47)(13,51)(14,55)(15,30)(16,34)(17,38)(18,42)(19,46)(20,50)(21,54)(22,29)(23,33)(24,37)(25,41)(26,45)(27,49)(28,53)
    """
