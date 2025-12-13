from sage.combinat.posets.lattices import LatticePoset as LatticePoset
from sage.graphs.digraph import DiGraph as DiGraph
from sage.topology.simplicial_complex import SimplicialComplex as SimplicialComplex

def hochschild_lattice(n) -> LatticePoset:
    """
    Return the Hochschild lattice `H_n`.

    INPUT:

    - `n \\geq 1` -- an integer

    The cardinality of `H_n` is `2^{n - 2} \\times (n + 3)`.

    .. SEEALSO:: :func:`hochschild_simplicial_complex`, :func:`hochschild_fan`

    EXAMPLES::

        sage: P = posets.HochschildLattice(5); P
        Finite lattice containing 64 elements
        sage: P.degree_polynomial()
        x^5 + 9*x^4*y + 22*x^3*y^2 + 22*x^2*y^3 + 9*x*y^4 + y^5

    TESTS::

        sage: posets.HochschildLattice(0)
        Traceback (most recent call last):
        ...
        ValueError: this requires n >= 1
    """
def hochschild_fan(n):
    """
    Return Saneblidze's fan for the Hochschild polytope.

    The dual polytope is obtained from a standard simplex
    by a sequence of truncations.

    .. SEEALSO::

        :func:`hochschild_simplicial_complex`, :func:`hochschild_lattice`

    EXAMPLES::

        sage: from sage.combinat.posets.hochschild_lattice import hochschild_fan
        sage: F = hochschild_fan(4); F
        Rational polyhedral fan in 4-d lattice N
        sage: F.f_vector()
        (1, 11, 39, 56, 28)
    """
def hochschild_simplicial_complex(n) -> SimplicialComplex:
    """
    Return a simplicial complex related to the Hochschild lattice `H_n`.

    This is a pure spherical simplicial complex, whose flip graph
    is isomorphic to the Hasse diagram of `H_n`.

    .. SEEALSO:: :func:`hochschild_fan`, :func:`hochschild_lattice`

    EXAMPLES::

        sage: C = simplicial_complexes.HochschildSphere(3); C
        Simplicial complex with 8 vertices and 12 facets
        sage: H = C.flip_graph()
        sage: P = posets.HochschildLattice(3)
        sage: H.is_isomorphic(P.hasse_diagram().to_undirected())
        True
    """
