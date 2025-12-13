from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.combinat.subword_complex import SubwordComplex as SubwordComplex, SubwordComplexFacet as SubwordComplexFacet
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.semirings.non_negative_integer_semiring import NN as NN

class ClusterComplexFacet(SubwordComplexFacet):
    """
    A cluster (i.e., a facet) of a cluster complex.
    """
    def cluster(self):
        """
        Return this cluster as a set of almost positive roots.

        EXAMPLES::

            sage: C = ClusterComplex(['A', 2])
            sage: F = C((0, 1))
            sage: F.cluster()
            [(-1, 0), (0, -1)]
        """
    def upper_cluster(self):
        """
        Return the part of the cluster that contains positive roots.

        EXAMPLES::

            sage: C = ClusterComplex(['A', 2])
            sage: F = C((0, 1))
            sage: F.upper_cluster()
            []
        """
    def product_of_upper_cluster(self):
        """
        Return the product of the upper cluster in reversed order.

        EXAMPLES::

            sage: C = ClusterComplex(['A', 2])
            sage: for F in C: F.product_of_upper_cluster().reduced_word()
            []
            [2]
            [1]
            [1, 2]
            [1, 2]
        """

class ClusterComplex(SubwordComplex):
    """
    A cluster complex (or generalized dual associahedron).

    The cluster complex (or generalized dual associahedron) is a
    simplicial complex constructed from a cluster algebra.  Its
    vertices are the cluster variables and its facets are the
    clusters, i.e., maximal subsets of compatible cluster variables.

    The cluster complex of type `A_n` is the simplicial complex with
    vertices being (proper) diagonals in a convex `(n+3)`-gon and with
    facets being triangulations.

    The implementation of the cluster complex depends on its
    connection to subword complexes, see [CLS2014]_. Let `c` be a Coxeter
    element with reduced word `{\\bf c}` in a finite Coxeter group `W`,
    and let `{\\bf w}_\\circ` be the `c`-sorting word for the longest
    element `w_\\circ \\in W`.

    The ``multi-cluster complex`` `\\Delta(W,k)` has vertices in
    one-to-one correspondence with letters in the word
    `Q = {\\bf c^k w}_\\circ` and with facets being complements
    in `Q` of reduced expressions for `w_\\circ`.

    For `k = 1`, the multi-cluster complex is isomorphic to the
    cluster complex as defined above.

    EXAMPLES:

    A first example of a cluster complex::

        sage: C = ClusterComplex(['A', 2]); C
        Cluster complex of type ['A', 2] with 5 vertices and 5 facets

    Its vertices, facets, and minimal non-faces::

        sage: C.vertices()
        (0, 1, 2, 3, 4)

        sage: C.facets()
        [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]

        sage: C.minimal_nonfaces()
        [[0, 2], [0, 3], [1, 3], [1, 4], [2, 4]]

    We can do everything we can do on simplicial complexes,
    e.g. computing its homology::

        sage: C.homology()
        {0: 0, 1: Z}

    We can also create a multi-cluster complex::

        sage: ClusterComplex(['A', 2], k=2)
        Multi-cluster complex of type ['A', 2] with 7 vertices and 14 facets

    REFERENCES:

    - [CLS2014]_
    """
    @staticmethod
    def __classcall__(cls, W, k: int = 1, coxeter_element=None, algorithm: str = 'inductive'):
        """
        Standardize input to ensure a unique representation.

        TESTS::

            sage: S1 = ClusterComplex(['B',2])
            sage: W = CoxeterGroup(['B',2])
            sage: S2 = ClusterComplex(W)
            sage: S3 = ClusterComplex(CoxeterMatrix('B2'), coxeter_element=(1,2))
            sage: w = W.from_reduced_word([1,2])
            sage: S4 = ClusterComplex('B2', coxeter_element=w, algorithm='inductive')
            sage: S1 is S2 and S2 is S3 and S3 is S4
            True
        """
    def __init__(self, W, k, coxeter_element, algorithm) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: S = ClusterComplex(['A', 2])
            sage: TestSuite(S).run()
            sage: S = ClusterComplex(['A', 2], k=2)
            sage: TestSuite(S).run()
        """
    def __call__(self, F, facet_test: bool = True):
        """
        Create a facet of ``self``.

        INPUT:

        - ``F`` -- an iterable of positions
        - ``facet_test`` -- boolean (default: ``True``); tells whether
          or not the facet ``F`` should be tested before creation

        OUTPUT: the facet of ``self`` at positions given by ``F``

        EXAMPLES::

            sage: C = ClusterComplex(['A', 2])
            sage: F = C((0, 1)); F
            (0, 1)

        TESTS::

            sage: C = ClusterComplex(['A', 2])
            sage: F = C((0, 1))
            sage: C(F) is F
            True
        """
    Element = ClusterComplexFacet
    def k(self):
        """
        Return the index `k` of ``self``.

        EXAMPLES::

            sage: ClusterComplex(['A', 2]).k()
            1
        """
    def minimal_nonfaces(self):
        """
        Return the minimal non-faces of ``self``.

        EXAMPLES::

            sage: ClusterComplex(['A', 2]).minimal_nonfaces()
            [[0, 2], [0, 3], [1, 3], [1, 4], [2, 4]]
        """
    def cyclic_rotation(self):
        """
        Return the operation on the facets of ``self`` obtained by the
        cyclic rotation as defined in [CLS2014]_.

        EXAMPLES::

            sage: ClusterComplex(['A', 2]).cyclic_rotation()
            <function ...act at ...>
        """
