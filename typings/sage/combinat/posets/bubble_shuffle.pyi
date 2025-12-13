from sage.combinat.posets.lattices import LatticePoset as LatticePoset
from sage.combinat.shuffle import ShuffleProduct as ShuffleProduct
from sage.combinat.subset import subsets as subsets
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.graph import Graph as Graph
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from typing import Iterator

def bubble_cardinality(m, n) -> Integer:
    """
    Return the cardinality of the Bubble lattice `B_{m,n}`.

    We have

    .. MATH::

        |B_{m,n}| = \\sum_{i=0}^m \\sum_{j=0}^n \\binom{i+j}{j} \\binom{m}{i} \\binom{n}{j}.

    This is also the cardinality of the Shuffle lattice `S_{m,n}`.

    INPUT:

    - ``m`` -- integer
    - ``n`` -- integer

    EXAMPLES::

        sage: from sage.combinat.posets.bubble_shuffle import bubble_cardinality
        sage: bubble_cardinality(2,1)
        12
    """
def bubble_set(m, n) -> Iterator[tuple[int, ...]]:
    """
    Return the underlying set of the Bubble lattice `B_{m,n}`.

    This is the set of all shuffles of subsets of `\\{-m,\\ldots,-1\\}`
    with subsets of `\\{1,\\ldots,n\\}`.

    This is also the underlying set of the Shuffle lattice `S_{m,n}`.

    INPUT:

    - ``m`` -- integer
    - ``n`` -- integer

    EXAMPLES::

        sage: from sage.combinat.posets.bubble_shuffle import bubble_set
        sage: list(bubble_set(2,1))
        [(),
         (1,),
         (-1,),
         (-1, 1),
         (1, -1),
         (-2,),
         (-2, 1),
         (1, -2),
         (-1, -2),
         (-1, -2, 1),
         (1, -1, -2),
         (-1, 1, -2)]
    """
def bubble_coverings(m, n, mot, transpose: bool = True) -> Iterator[tuple[int, ...]]:
    """
    Return generating relations of the Bubble lattice `B_{m,n}`.

    Note that these relations include the cover relations, but not only them.

    This can also produce covers in the Shuffle lattice `S_{m,n}`.

    INPUT:

    - ``m`` -- integer
    - ``n`` -- integer
    - ``mot`` -- element of `B_{m,n}` as a tuple
    - ``transpose`` -- boolean (default: ``True``) whether to return covers
      in the Bubble lattice or in the Shuffle lattice

    EXAMPLES::

        sage: from sage.combinat.posets.bubble_shuffle import bubble_coverings
        sage: list(bubble_coverings(2, 1, (-2, 1)))
        [(1,), (1, -2)]
        sage: list(bubble_coverings(2, 1, (-2, 1), False))
        [(1,)]
    """
def BubblePoset(m, n) -> LatticePoset:
    """
    Return the Bubble lattice `B_{m,n}`.

    Bubble lattices were introduced by McConville and Mühle in [MacCM2022]_.

    The Bubble lattice `B_{m,n}` and the Shuffle lattice `S_{m,n}` share
    the same underlying set, namely all shuffles of two subwords of the
    two words `X = (x_1,x_2,\\ldots,x_{m})` and `Y = (y_1,y_2,\\ldots,y_n)`.

    The Bubble poset is an extension of the Shuffle poset, by adding the
    exchange of adjacent letters from `X` and `Y`, from `xy` to `yx`.

    .. SEEALSO::

        :func:`ShufflePoset`, :func:`noncrossing_bipartite_complex`

    EXAMPLES::

        sage: P = posets.BubblePoset(2,1); P
        Finite lattice containing 12 elements
        sage: P.zeta_polynomial()
        1/40*q^5 + 7/24*q^4 + 23/24*q^3 - 7/24*q^2 + 1/60*q
    """
def ShufflePoset(m, n) -> LatticePoset:
    """
    Return the Shuffle lattice `S_{m,n}`.

    Shuffle lattices were defined by Greene in [Gre1988]_.

    The Bubble lattice `B_{m,n}` and the Shuffle lattice `S_{m,n}` share
    the same underlying set, namely all shuffles of two subwords of the
    two words `X = (x_1,x_2,\\ldots,x_{m})` and `Y = (y_1,y_2,\\ldots,y_n)`.

    The partial order in the Shuffle poset is defined by either inserting a
    letter from `Y` or deleting a letter from `X`.

    .. SEEALSO:: :func:`BubblePoset`

    EXAMPLES::

        sage: P = posets.ShufflePoset(2,1); P
        Finite lattice containing 12 elements
        sage: P.zeta_polynomial()
        2*q^3 - q^2
    """
def noncrossing_bipartite_complex(m, n):
    """
    Return a simplicial complex related to the Bubble lattice `B_{m,n}`.

    This is a pure spherical simplicial complex, whose flip graph
    is isomorphic to the Hasse diagram of `B_{m,n}`.

    .. SEEALSO:: :func:`BubblePoset`

    EXAMPLES::

        sage: C = simplicial_complexes.NoncrossingBipartiteComplex(2,1)
        sage: H = C.flip_graph()
        sage: P = posets.BubblePoset(2,1)
        sage: H.is_isomorphic(P.hasse_diagram().to_undirected())
        True
    """
