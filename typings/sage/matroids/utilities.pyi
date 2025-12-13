from sage.matrix.constructor import Matrix as Matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.all import SageObject as SageObject

def setprint(X) -> None:
    """
    Print nested data structures nicely.

    Python's data structures ``set`` and ``frozenset`` do not print nicely.
    This function can be used as replacement for ``print`` to overcome this.
    For direct access to ``setprint``, run::

        sage: from sage.matroids.advanced import *

    .. NOTE::

        This function will be redundant when Sage moves to Python 3, since the
        default ``print`` will suffice then.

    INPUT:

    - ``X`` -- any Python object

    OUTPUT: none; however, the function prints a nice representation of ``X``

    EXAMPLES:

    Output looks much better::

        sage: from sage.matroids.advanced import setprint
        sage: L = [{1, 2, 3}, {1, 2, 4}, {2, 3, 4}, {4, 1, 3}]
        sage: print(L)
        [{1, 2, 3}, {1, 2, 4}, {2, 3, 4}, {1, 3, 4}]
        sage: setprint(L)
        [{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]

    Note that for iterables, the effect can be undesirable::

        sage: from sage.matroids.advanced import setprint
        sage: M = matroids.catalog.Fano().delete('efg')
        sage: M.bases()
        SetSystem of 3 sets over 4 elements
        sage: setprint(M.bases())
        [{'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}]

    An exception was made for subclasses of SageObject::

        sage: from sage.matroids.advanced import setprint
        sage: G = graphs.PetersenGraph()                                                # needs sage.graphs
        sage: list(G)                                                                   # needs sage.graphs
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: setprint(G)                                                               # needs sage.graphs
        Petersen graph: Graph on 10 vertices
    """
def setprint_s(X, toplevel: bool = False):
    '''
    Create the string for use by ``setprint()``.

    INPUT:

    - ``X`` -- any Python object
    - ``toplevel`` -- boolean (default: ``False``); indicates whether this is a
      recursion or not

    OUTPUT:

    A string representation of the object, with nice notation for sets and
    frozensets.

    EXAMPLES::

        sage: from sage.matroids.utilities import setprint_s
        sage: L = [{1, 2, 3}, {1, 2, 4}, {2, 3, 4}, {4, 1, 3}]
        sage: setprint_s(L)
        \'[{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]\'

    The ``toplevel`` argument only affects strings, to mimic ``print``\'s
    behavior::

        sage: X = \'abcd\'
        sage: setprint_s(X)
        "\'abcd\'"
        sage: setprint_s(X, toplevel=True)
        \'abcd\'
    '''
def newlabel(groundset):
    """
    Create a new element label different from the labels in ``groundset``.

    INPUT:

    - ``groundset`` -- set of objects

    OUTPUT: string not in the set ``groundset``

    For direct access to ``newlabel``, run::

        sage: from sage.matroids.advanced import *

    ALGORITHM:

    #. Create a set of all one-character alphanumeric strings.
    #. Remove the string representation of each existing element from this
       list.
    #. If the list is nonempty, return any element.
    #. Otherwise, return the concatenation of the strings of each existing
       element, preceded by 'e'.

    EXAMPLES::

        sage: from sage.matroids.advanced import newlabel
        sage: S = set(['a', 42, 'b'])
        sage: newlabel(S) in S
        False

        sage: S = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        sage: t = newlabel(S)
        sage: len(t)
        63
        sage: t[0]
        'e'
    """
def sanitize_contractions_deletions(matroid, contractions, deletions):
    """
    Return a fixed version of sets ``contractions`` and ``deletions``.

    INPUT:

    - ``matroid`` -- a :class:`Matroid <sage.matroids.matroid.Matroid>`
      instance
    - ``contractions`` -- a subset of the groundset
    - ``deletions`` -- a subset of the groundset

    OUTPUT: an independent set ``C`` and a coindependent set ``D`` such that

        ``matroid / contractions \\ deletions == matroid / C \\ D``

    Raise an error if either is not a subset of the groundset of ``matroid``
    or if they are not disjoint.

    This function is used by the
    :meth:`Matroid.minor() <sage.matroids.matroid.Matroid.minor>` method.

    EXAMPLES::

        sage: from sage.matroids.utilities import setprint
        sage: from sage.matroids.utilities import sanitize_contractions_deletions
        sage: M = matroids.catalog.Fano()
        sage: setprint(sanitize_contractions_deletions(M, 'abc', 'defg'))
        [{'a', 'b', 'c'}, {'d', 'e', 'f', 'g'}]
        sage: setprint(sanitize_contractions_deletions(M, 'defg', 'abc'))
        [{'a', 'b', 'c', 'f'}, {'d', 'e', 'g'}]
        sage: setprint(sanitize_contractions_deletions(M, [1, 2, 3], 'efg'))
        Traceback (most recent call last):
        ...
        ValueError: [1, 2, 3] is not a subset of the groundset
        sage: setprint(sanitize_contractions_deletions(M, 'efg', [1, 2, 3]))
        Traceback (most recent call last):
        ...
        ValueError: [1, 2, 3] is not a subset of the groundset
        sage: setprint(sanitize_contractions_deletions(M, 'ade', 'efg'))
        Traceback (most recent call last):
        ...
        ValueError: contraction and deletion sets are not disjoint.
    """
def make_regular_matroid_from_matroid(matroid):
    """
    Attempt to construct a regular representation of a matroid.

    INPUT:

    - ``matroid`` -- matroid

    OUTPUT:

    Return a `(0, 1, -1)`-matrix over the integers such that, if the input is
    a regular matroid, then the output is a totally unimodular matrix
    representing that matroid.

    EXAMPLES::

        sage: from sage.matroids.utilities import make_regular_matroid_from_matroid
        sage: make_regular_matroid_from_matroid(                                        # needs sage.graphs
        ....:               matroids.CompleteGraphic(6)).is_isomorphic(
        ....:                                     matroids.CompleteGraphic(6))
        True
    """
def get_nonisomorphic_matroids(MSet):
    """
    Return non-isomorphic members of the matroids in set ``MSet``.

    For direct access to ``get_nonisomorphic_matroids``, run::

        sage: from sage.matroids.advanced import *

    INPUT:

    - ``MSet`` -- an iterable whose members are matroids

    OUTPUT:

    A list containing one representative of each isomorphism class of
    members of ``MSet``.

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: L = matroids.Uniform(3, 5).extensions()
        sage: len(list(L))
        32
        sage: len(get_nonisomorphic_matroids(L))
        5
    """
def spanning_forest(M):
    """
    Return a list of edges of a spanning forest of the bipartite
    graph defined by `M`

    INPUT:

    - ``M`` -- a matrix defining a bipartite graph G. The vertices are the
      rows and columns, if `M[i,j]` is nonzero, then there is an edge
      between row `i` and column `j`.

    OUTPUT:

    A list of tuples `(r_i,c_i)` representing edges between row `r_i` and
    column `c_i`.

    EXAMPLES::

        sage: from sage.matroids.utilities import spanning_forest
        sage: len(spanning_forest(matrix([[1,1,1],[1,1,1],[1,1,1]])))                   # needs sage.graphs
        5
        sage: len(spanning_forest(matrix([[0,0,1],[0,1,0],[0,1,0]])))                   # needs sage.graphs
        3
    """
def spanning_stars(M):
    """
    Return the edges of a connected subgraph that is a union of
    all edges incident some subset of vertices.

    INPUT:

    - ``M`` -- a matrix defining a bipartite graph G. The vertices are the
      rows and columns, if `M[i,j]` is nonzero, then there is an edge
      between row i and column 0.

    OUTPUT:

    A list of tuples `(row,column)` in a spanning forest of the bipartite graph
    defined by ``M``.

    EXAMPLES::

        sage: from sage.matroids.utilities import spanning_stars
        sage: edges = spanning_stars(matrix([[1,1,1],[1,1,1],[1,1,1]]))                 # needs sage.graphs
        sage: Graph([(x+3, y) for x,y in edges]).is_connected()                         # needs sage.graphs
        True
    """
def lift_cross_ratios(A, lift_map=None):
    """
    Return a matrix which arises from the given matrix by lifting cross ratios.

    INPUT:

    - ``A`` -- a matrix over a ring ``source_ring``
    - ``lift_map`` -- a Python dictionary, mapping each cross ratio of ``A`` to
      some element of a target ring, and such that
      ``lift_map[source_ring(1)] = target_ring(1)``

    OUTPUT: ``Z`` -- a matrix over the ring ``target_ring``

    The intended use of this method is to create a (reduced) matrix representation of a
    matroid ``M`` over a ring ``target_ring``, given a (reduced) matrix representation of
    ``A`` of ``M`` over a ring ``source_ring`` and a map ``lift_map`` from ``source_ring``
    to ``target_ring``.

    This method will create a unique candidate representation ``Z``, but will not verify
    if ``Z`` is indeed a representation of ``M``. However, this is guaranteed if the
    conditions of the lift theorem (see [PvZ2010]_) hold for the lift map in combination with
    the matrix ``A``.

    For a lift map `f` and a matrix `A` these conditions are as follows. First of all
    `f: S \\rightarrow T`, where `S` is a set of invertible elements of the source ring and
    `T` is a set of invertible elements of the target ring. The matrix `A` has entries
    from the source ring, and each cross ratio of `A` is contained in `S`. Moreover:

    - `1 \\in S`, `1 \\in T`;
    - for all `x \\in S`: `f(x) = 1` if and only if `x = 1`;
    - for all `x, y \\in S`: if `x + y = 0` then `f(x) + f(y) = 0`;
    - for all `x, y \\in S`: if `x + y = 1` then `f(x) + f(y) = 1`;
    - for all `x, y, z \\in S`: if  `xy = z` then `f(x)f(y) = f(z)`.

    Any ring homomorphism `h: P \\rightarrow R` induces a lift map from the set of units `S` of
    `P` to the set of units `T` of `R`. There exist lift maps which do not arise in
    this manner. Several such maps can be created by the function
    :meth:`lift_map() <sage.matroids.utilities.lift_map>`.

    .. SEEALSO::

        :meth:`lift_map() <sage.matroids.utilities.lift_map>`

    EXAMPLES::

        sage: # needs sage.graphs
        sage: from sage.matroids.advanced import lift_cross_ratios, lift_map, LinearMatroid
        sage: R = GF(7)
        sage: to_sixth_root_of_unity = lift_map('sru')                                  # needs sage.rings.number_field
        sage: A = Matrix(R, [[1, 0, 6, 1, 2],[6, 1, 0, 0, 1],[0, 6, 3, 6, 0]])
        sage: A
        [1 0 6 1 2]
        [6 1 0 0 1]
        [0 6 3 6 0]
        sage: Z = lift_cross_ratios(A, to_sixth_root_of_unity)                          # needs sage.rings.finite_rings sage.rings.number_field
        sage: Z                                                                         # needs sage.rings.finite_rings sage.rings.number_field
        [     1      0      1      1      1]
        [-z + 1      1      0      0      1]
        [     0     -1      1 -z + 1      0]
        sage: M = LinearMatroid(reduced_matrix=A)
        sage: sorted(M.cross_ratios())
        [3, 5]
        sage: N = LinearMatroid(reduced_matrix=Z)                                       # needs sage.rings.finite_rings sage.rings.number_field
        sage: sorted(N.cross_ratios())                                                  # needs sage.rings.finite_rings sage.rings.number_field
        [-z + 1, z]
        sage: M.is_isomorphism(N, {e:e for e in M.groundset()})                         # needs sage.rings.finite_rings sage.rings.number_field
        True
    """
def lift_map(target):
    '''
    Create a lift map, to be used for lifting the cross ratios of a matroid
    representation.

    .. SEEALSO::

        :meth:`lift_cross_ratios() <sage.matroids.utilities.lift_cross_ratios>`

    INPUT:

    - ``target`` -- string describing the target (partial) field

    OUTPUT: dictionary

    Depending on the value of ``target``, the following lift maps will be created:

    - "reg": a lift map from `\\GF3` to the regular partial field `(\\ZZ, <-1>)`.

    - "sru": a lift map from `\\GF7` to the
      sixth-root-of-unity partial field `(\\QQ(z), <z>)`, where `z` is a sixth root
      of unity. The map sends 3 to `z`.

    - "dyadic": a lift map from `\\GF{11}` to the dyadic partial field `(\\QQ, <-1, 2>)`.

    - "gm": a lift map from `\\GF{19}` to the golden mean partial field
      `(\\QQ(t), <-1,t>)`, where `t` is a root of `t^2-t-1`. The map sends `5` to `t`.

    The example below shows that the latter map satisfies three necessary conditions stated in
    :meth:`lift_cross_ratios() <sage.matroids.utilities.lift_cross_ratios>`

    EXAMPLES::

        sage: from sage.matroids.utilities import lift_map
        sage: lm = lift_map(\'gm\')                                                       # needs sage.rings.finite_rings sage.rings.number_field
        sage: for x in lm:                                                              # needs sage.rings.finite_rings sage.rings.number_field
        ....:     if (x == 1) is not (lm[x] == 1):
        ....:         print(\'not a proper lift map\')
        ....:     for y in lm:
        ....:         if (x+y == 0) and not (lm[x]+lm[y] == 0):
        ....:             print(\'not a proper lift map\')
        ....:         if (x+y == 1) and not (lm[x]+lm[y] == 1):
        ....:             print(\'not a proper lift map\')
        ....:         for z in lm:
        ....:             if (x*y==z) and not (lm[x]*lm[y]==lm[z]):
        ....:                 print(\'not a proper lift map\')
    '''
def split_vertex(G, u, v=None, edges=None) -> None:
    """
    Split a vertex in a graph.

    If an edge is inserted between the vertices after splitting, this
    corresponds to a graphic coextension of a matroid.

    INPUT:

    - ``G`` -- a SageMath :class:`Graph`
    - ``u`` -- a vertex in ``G``
    - ``v`` -- (optional) the name of the new vertex after the splitting. If
      ``v`` is specified and already in the graph, it must be an isolated vertex.
    - ``edges`` -- (optional) iterable container of edges on ``u`` that
      move to ``v`` after the splitting. If ``None``, ``v`` will be an isolated
      vertex. The edge labels must be specified.

    EXAMPLES::

        sage: # needs sage.graphs
        sage: from sage.matroids.utilities import split_vertex
        sage: G = graphs.BullGraph()
        sage: split_vertex(G, u=1, v=55, edges=[(1, 3)])
        Traceback (most recent call last):
        ...
        ValueError: the edges are not all incident with u
        sage: split_vertex(G, u=1, v=55, edges=[(1, 3, None)])
        sage: list(G.edges(sort=True))
        [(0, 1, None), (0, 2, None), (1, 2, None), (2, 4, None), (3, 55, None)]
    """
def cmp_elements_key(x):
    """
    A helper function to compare elements which may be integers or strings.

    EXAMPLES::

        sage: from sage.matroids.utilities import cmp_elements_key
        sage: l = ['a', 'b', 1, 3, 2, 10, 111, 100, 'c', 'aa']
        sage: sorted(l, key=cmp_elements_key)
        [1, 2, 3, 10, 100, 111, 'a', 'aa', 'b', 'c']
    """
