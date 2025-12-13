from .cell_complex import GenericCellComplex as GenericCellComplex
from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.fields import Fields as Fields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygens as polygens
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.parent import Parent as Parent
from sage.structure.sage_object import SageObject as SageObject

def lattice_paths(t1, t2, length=None):
    """
    Given lists (or tuples or ...) ``t1`` and ``t2``, think of them as
    labelings for vertices: ``t1`` labeling points on the x-axis,
    ``t2`` labeling points on the y-axis, both increasing.  Return the
    list of rectilinear paths along the grid defined by these points
    in the plane, starting from ``(t1[0], t2[0])``, ending at
    ``(t1[last], t2[last])``, and at each grid point, going either
    right or up.  See the examples.

    INPUT:

    - ``t1`` -- list or other iterable; labeling for vertices
    - ``t2`` -- list or other iterable; labeling for vertices
    - ``length`` -- integer or ``None`` (default: ``None``); if not ``None``, then
      an integer, the length of the desired path

    OUTPUT: list of lists of vertices making up the paths

    This is used when triangulating the product of simplices.  The
    optional argument ``length`` is used for `\\Delta`-complexes, to
    specify all simplices in a product: in the triangulation of a
    product of two simplices, there is a `d`-simplex for every path of
    length `d+1` in the lattice.  The path must start at the bottom
    left and end at the upper right, and it must use at least one
    point in each row and in each column, so if ``length`` is too
    small, there will be no paths.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex import lattice_paths
        sage: lattice_paths([0,1,2], [0,1,2])
        [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
         [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)],
         [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)],
         [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],
         [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],
         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]]
        sage: lattice_paths(('a', 'b', 'c'), (0, 3, 5))
        [[('a', 0), ('a', 3), ('a', 5), ('b', 5), ('c', 5)],
         [('a', 0), ('a', 3), ('b', 3), ('b', 5), ('c', 5)],
         [('a', 0), ('b', 0), ('b', 3), ('b', 5), ('c', 5)],
         [('a', 0), ('a', 3), ('b', 3), ('c', 3), ('c', 5)],
         [('a', 0), ('b', 0), ('b', 3), ('c', 3), ('c', 5)],
         [('a', 0), ('b', 0), ('c', 0), ('c', 3), ('c', 5)]]
        sage: lattice_paths(range(3), range(3), length=2)
        []
        sage: lattice_paths(range(3), range(3), length=3)
        [[(0, 0), (1, 1), (2, 2)]]
        sage: lattice_paths(range(3), range(3), length=4)
        [[(0, 0), (1, 1), (1, 2), (2, 2)],
         [(0, 0), (0, 1), (1, 2), (2, 2)],
         [(0, 0), (1, 1), (2, 1), (2, 2)],
         [(0, 0), (1, 0), (2, 1), (2, 2)],
         [(0, 0), (0, 1), (1, 1), (2, 2)],
         [(0, 0), (1, 0), (1, 1), (2, 2)]]
    """
def rename_vertex(n, keep, left: bool = True):
    """
    Rename a vertex: the vertices from the list ``keep`` get
    relabeled 0, 1, 2, ..., in order.  Any other vertex (e.g. 4) gets
    renamed to by prepending an 'L' or an 'R' (thus to either 'L4' or
    'R4'), depending on whether the argument left is ``True`` or ``False``.

    INPUT:

    - ``n`` -- a 'vertex'; either an integer or a string
    - ``keep`` -- list of three vertices
    - ``left`` -- boolean (default: ``True``); if ``True``, rename for use in
      left factor

    This is used by the :meth:`~SimplicialComplex.connected_sum` method for
    simplicial complexes.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex import rename_vertex
        sage: rename_vertex(6, [5, 6, 7])
        1
        sage: rename_vertex(3, [5, 6, 7, 8, 9])
        'L3'
        sage: rename_vertex(3, [5, 6, 7], left=False)
        'R3'
    """

class Simplex(SageObject):
    """
    Define a simplex.

    Topologically, a simplex is the convex hull of a collection of
    vertices in general position.  Combinatorially, it is defined just
    by specifying a set of vertices.  It is represented in Sage by the
    tuple of the vertices.

    INPUT:

    - ``X`` -- set of vertices (integer, list, or other iterable)

    OUTPUT: simplex with those vertices

    ``X`` may be a nonnegative integer `n`, in which case the
    simplicial complex will have `n+1` vertices `(0, 1, ..., n)`, or
    it may be anything which may be converted to a tuple, in which
    case the vertices will be that tuple.  In the second case, each
    vertex must be hashable, so it should be a number, a string, or a
    tuple, for instance, but not a list.

    .. WARNING::

       The vertices should be distinct, and no error checking is done
       to make sure this is the case.

    EXAMPLES::

        sage: Simplex(4)
        (0, 1, 2, 3, 4)
        sage: Simplex([3, 4, 1])
        (3, 4, 1)
        sage: X = Simplex((3, 'a', 'vertex')); X
        (3, 'a', 'vertex')
        sage: X == loads(dumps(X))
        True

    Vertices may be tuples but not lists::

        sage: Simplex([(1,2), (3,4)])
        ((1, 2), (3, 4))
        sage: Simplex([[1,2], [3,4]])
        Traceback (most recent call last):
        ...
        TypeError: unhashable type: 'list'
    """
    def __init__(self, X) -> None:
        """
        Define a simplex.  See :class:`Simplex` for full documentation.

        EXAMPLES::

            sage: Simplex(2)
            (0, 1, 2)
            sage: Simplex(('a', 'b', 'c'))
            ('a', 'b', 'c')
            sage: Simplex(-1)
            ()
            sage: Simplex(-3)
            Traceback (most recent call last):
            ...
            ValueError: the n-simplex is only defined if n > -2
        """
    def tuple(self):
        """
        The tuple attached to this simplex.

        EXAMPLES::

            sage: Simplex(3).tuple()
            (0, 1, 2, 3)

        Although simplices are printed as if they were tuples, they
        are not the same type::

            sage: type(Simplex(3).tuple())
            <... 'tuple'>
            sage: type(Simplex(3))
            <class 'sage.topology.simplicial_complex.Simplex'>
        """
    def set(self):
        """
        The frozenset attached to this simplex.

        EXAMPLES::

            sage: Simplex(3).set()
            frozenset({0, 1, 2, 3})
        """
    def is_face(self, other):
        """
        Return ``True`` iff this simplex is a face of other.

        EXAMPLES::

            sage: Simplex(3).is_face(Simplex(5))
            True
            sage: Simplex(5).is_face(Simplex(2))
            False
            sage: Simplex(['a', 'b', 'c']).is_face(Simplex(8))
            False
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` iff ``x`` is a vertex of this simplex.

        EXAMPLES::

            sage: 3 in Simplex(5)
            True
            sage: 3 in Simplex(2)
            False
        """
    def __getitem__(self, n):
        """
        Return the `n`-th vertex in this simplex.

        EXAMPLES::

            sage: Simplex(5)[2]
            2
            sage: Simplex(['a', 'b', 'c'])[1]
            'b'
        """
    def __iter__(self):
        """
        Iterator for the vertices of this simplex.

        EXAMPLES::

            sage: [v**2 for v in Simplex(3)]
            [0, 1, 4, 9]
        """
    def __add__(self, other):
        """
        Simplex obtained by concatenating the underlying tuples of the
        two arguments.

        INPUT:

        - ``other`` -- another simplex

        EXAMPLES::

            sage: Simplex((1,2,3)) + Simplex((5,6))
            (1, 2, 3, 5, 6)
        """
    def face(self, n):
        """
        The `n`-th face of this simplex.

        INPUT:

        - ``n`` -- integer between 0 and the dimension of this simplex

        OUTPUT: the simplex obtained by removing the `n`-th vertex from this
        simplex

        EXAMPLES::

            sage: S = Simplex(4)
            sage: S.face(0)
            (1, 2, 3, 4)
            sage: S.face(3)
            (0, 1, 2, 4)
        """
    def faces(self):
        """
        The list of faces (of codimension 1) of this simplex.

        EXAMPLES::

            sage: S = Simplex(4)
            sage: S.faces()
            [(1, 2, 3, 4), (0, 2, 3, 4), (0, 1, 3, 4), (0, 1, 2, 4), (0, 1, 2, 3)]
            sage: len(Simplex(10).faces())
            11
        """
    def dimension(self):
        """
        The dimension of this simplex.

        The dimension of a simplex is the number of vertices minus 1.

        EXAMPLES::

            sage: Simplex(5).dimension() == 5
            True
            sage: Simplex(5).face(1).dimension()
            4
        """
    def is_empty(self):
        """
        Return ``True`` iff this simplex is the empty simplex.

        EXAMPLES::

            sage: [Simplex(n).is_empty() for n in range(-1,4)]
            [True, False, False, False, False]
        """
    def join(self, right, rename_vertices: bool = True):
        '''
        The join of this simplex with another one.

        The join of two simplices `[v_0, ..., v_k]` and `[w_0, ...,
        w_n]` is the simplex `[v_0, ..., v_k, w_0, ..., w_n]`.

        INPUT:

        - ``right`` -- the other simplex (the right-hand factor)

        - ``rename_vertices`` -- boolean (default: ``True``); if this is ``True``,
          the vertices in the join will be renamed by this formula: vertex "v"
          in the left-hand factor --> vertex "Lv" in the join, vertex "w" in
          the right-hand factor --> vertex "Rw" in the join.  If this is
          ``False``, this tries to construct the join without renaming the
          vertices; this may cause problems if the two factors have any
          vertices with names in common.

        EXAMPLES::

            sage: Simplex(2).join(Simplex(3))
            (\'L0\', \'L1\', \'L2\', \'R0\', \'R1\', \'R2\', \'R3\')
            sage: Simplex([\'a\', \'b\']).join(Simplex([\'x\', \'y\', \'z\']))
            (\'La\', \'Lb\', \'Rx\', \'Ry\', \'Rz\')
            sage: Simplex([\'a\', \'b\']).join(Simplex([\'x\', \'y\', \'z\']), rename_vertices=False)
            (\'a\', \'b\', \'x\', \'y\', \'z\')
        '''
    def product(self, other, rename_vertices: bool = True):
        '''
        The product of this simplex with another one, as a list of simplices.

        INPUT:

        - ``other`` -- the other simplex

        - ``rename_vertices`` -- boolean (default: ``True``); if this is
          ``False``, then the vertices in the product are the set of ordered
          pairs `(v,w)` where `v` is a vertex in the left-hand factor
          (``self``) and `w` is a vertex in the right-hand factor (``other``).
          If this is ``True``, then the vertices are renamed as "LvRw" (e.g.,
          the vertex (1,2) would become "L1R2").  This is useful if you want to
          define the Stanley-Reisner ring of the complex: vertex names like
          (0,1) are not suitable for that, while vertex names like "L0R1" are.

        ALGORITHM: see Hatcher, p. 277-278 [Hat2002]_ (who in turn refers to
        Eilenberg-Steenrod, p. 68): given ``S = Simplex(m)`` and
        ``T = Simplex(n)``, then `S \\times T` can be
        triangulated as follows: for each path `f` from `(0,0)` to
        `(m,n)` along the integer grid in the plane, going up or right
        at each lattice point, associate an `(m+n)`-simplex with
        vertices `v_0`, `v_1`, ..., where `v_k` is the `k`-th vertex
        in the path `f`.

        Note that there are `m+n` choose `n` such paths.  Note also
        that each vertex in the product is a pair of vertices `(v,w)`
        where `v` is a vertex in the left-hand factor and `w`
        is a vertex in the right-hand factor.

        .. NOTE::

           This produces a list of simplices -- not a :class:`Simplex`, not
           a :class:`SimplicialComplex`.

        EXAMPLES::

            sage: len(Simplex(2).product(Simplex(2)))
            6
            sage: Simplex(1).product(Simplex(1))
            [(\'L0R0\', \'L0R1\', \'L1R1\'), (\'L0R0\', \'L1R0\', \'L1R1\')]
            sage: Simplex(1).product(Simplex(1), rename_vertices=False)
            [((0, 0), (0, 1), (1, 1)), ((0, 0), (1, 0), (1, 1))]
        '''
    def alexander_whitney(self, dim):
        """
        Subdivide this simplex into a pair of simplices.

        If this simplex has vertices `v_0`, `v_1`, ..., `v_n`, then
        subdivide it into simplices `(v_0, v_1, ..., v_{dim})` and
        `(v_{dim}, v_{dim + 1}, ..., v_n)`.

        INPUT:

        - ``dim`` -- integer between 0 and one more than the
          dimension of this simplex

        OUTPUT:

        - a list containing just the triple ``(1, left, right)``,
          where ``left`` and ``right`` are the two simplices described
          above.

        This method allows one to construct a coproduct from the
        `p+q`-chains to the tensor product of the `p`-chains and the
        `q`-chains. The number 1 (a Sage integer) is the coefficient
        of ``left tensor right`` in this coproduct. (The corresponding
        formula is more complicated for the cubes that make up a
        cubical complex, and the output format is intended to be
        consistent for both cubes and simplices.)

        Calling this method ``alexander_whitney`` is an abuse of
        notation, since the actual Alexander-Whitney map goes from
        `C(X \\times Y) \\to C(X) \\otimes C(Y)`, where `C(-)` denotes
        the chain complex of singular chains, but this subdivision of
        simplices is at the heart of it.

        EXAMPLES::

            sage: s = Simplex((0,1,3,4))
            sage: s.alexander_whitney(0)
            [(1, (0,), (0, 1, 3, 4))]
            sage: s.alexander_whitney(2)
            [(1, (0, 1, 3), (3, 4))]
        """
    def __eq__(self, other):
        """
        Return ``True`` iff this simplex is the same as ``other``: that
        is, if the vertices of the two are the same, even with a
        different ordering

        INPUT:

        - ``other`` -- the other simplex

        EXAMPLES::

            sage: Simplex([0,1,2]) == Simplex([0,2,1])
            True
            sage: Simplex([0,1,2]) == Simplex(['a','b','c'])
            False
            sage: Simplex([1]) < Simplex([2])
            True
            sage: Simplex([1]) > Simplex([2])
            False
        """
    def __ne__(self, other):
        """
        Return ``True`` iff this simplex is not equal to ``other``.

        INPUT:

        - ``other`` -- the other simplex

        EXAMPLES::

            sage: Simplex([0,1,2]) != Simplex([0,2,1])
            False
            sage: Simplex([0,1,2]) != Simplex(['a','b','c'])
            True
        """
    def __lt__(self, other):
        """
        Return ``True`` iff the sorted tuple for this simplex is less than
        that for ``other``.

        INPUT:

        - ``other`` -- the other simplex

        EXAMPLES::

            sage: Simplex([1]) < Simplex([2])
            True
            sage: Simplex([2,3]) < Simplex([1])
            False
            sage: Simplex([0,1,2]) < Simplex([0,2,1])
            False

        Test ``@total_ordering`` by testing other comparisons::

            sage: Simplex([0,1,2]) <= Simplex([0,2,1])
            True
            sage: Simplex([1]) <= Simplex([2])
            True
            sage: Simplex([2]) <= Simplex([1])
            False
            sage: Simplex([0,1,2]) > Simplex([0,2,1])
            False
            sage: Simplex([1]) > Simplex([2])
            False
            sage: Simplex([2]) > Simplex([1])
            True
            sage: Simplex([0,1,2]) > Simplex([0,2,1])
            False
            sage: Simplex([0,1,2]) >= Simplex([0,2,1])
            True
            sage: Simplex([1]) >= Simplex([2])
            False
            sage: Simplex([2]) >= Simplex([1])
            True
        """
    def __hash__(self):
        """
        Hash value for this simplex.  This computes the hash value of
        the Python frozenset of the underlying tuple, since this is
        what's important when testing equality.

        EXAMPLES::

            sage: Simplex([1,2,0]).__hash__() == Simplex(2).__hash__()
            True
            sage: Simplex([1,2,0,1,1,2]).__hash__() == Simplex(2).__hash__()
            True
        """

class SimplicialComplex(Parent, GenericCellComplex):
    """
    Define a simplicial complex.

    INPUT:

    - ``maximal_faces`` -- set of maximal faces
    - ``from_characteristic_function`` -- see below
    - ``maximality_check`` -- boolean (default: ``True``); see below
    - ``sort_facets`` -- dictionary; see below
    - ``name_check`` -- boolean (default: ``False``); see below
    - ``is_mutable`` -- boolean (default: ``True``); set to ``False`` to make
      this immutable
    - ``category`` -- the category of the simplicial complex (default: finite
      simplicial complexes)

    OUTPUT: a simplicial complex

    ``maximal_faces`` should be a list or tuple or set (indeed,
    anything which may be converted to a set) whose elements are lists
    (or tuples, etc.) of vertices.  Maximal faces are also known as
    'facets'. ``maximal_faces`` can also be a list containing a single
    nonnegative integer `n`, in which case this constructs the
    simplicial complex with a single `n`-simplex as the only facet.

    Alternatively, the maximal faces can be defined from a monotone boolean
    function on the subsets of a set `X`. While defining ``maximal_faces=None``,
    you can thus set ``from_characteristic_function=(f,X)`` where ``X`` is the
    set of points and ``f`` a boolean monotone hereditary function that accepts
    a list of elements from ``X`` as input (see
    :func:`~sage.combinat.subsets_hereditary.subsets_with_hereditary_property`
    for more information).

    If ``maximality_check`` is ``True``, check that each maximal face is,
    in fact, maximal. In this case, when producing the internal
    representation of the simplicial complex, omit those that are not.
    It is highly recommended that this be ``True``; various methods for
    this class may fail if faces which are claimed to be maximal are
    in fact not.

    ``sort_facets``: if not set to ``None``, the default, this should
    be a dictionary, used for sorting the vertices in each facet. The
    keys must be the vertices for the simplicial complex, and the
    values should be distinct sortable objects, for example
    integers. This should not need to be specified except in very
    special circumstances; currently the only use in the Sage library
    is when defining the product of a simplicial complex with itself:
    in this case, the vertices in the product must be sorted
    compatibly with the vertices in each factor so that the diagonal
    map is properly defined.

    If ``name_check`` is ``True``, check the names of the vertices to see
    if they can be easily converted to generators of a polynomial ring
    -- use this if you plan to use the Stanley-Reisner ring for the
    simplicial complex.

    EXAMPLES::

        sage: SimplicialComplex([[1,2], [1,4]])
        Simplicial complex with vertex set (1, 2, 4) and facets {(1, 2), (1, 4)}
        sage: SimplicialComplex([[0,2], [0,3], [0]])
        Simplicial complex with vertex set (0, 2, 3) and facets {(0, 2), (0, 3)}
        sage: SimplicialComplex([[0,2], [0,3], [0]], maximality_check=False)
        Simplicial complex with vertex set (0, 2, 3) and facets {(0,), (0, 2), (0, 3)}

    Finally, if the first argument is a simplicial complex, return
    that complex.  If it is an object with a built-in conversion to
    simplicial complexes (via a ``_simplicial_`` method), then the
    resulting simplicial complex is returned::

        sage: S = SimplicialComplex([[0,2], [0,3], [0,6]])
        sage: SimplicialComplex(S) == S
        True
        sage: Tc = cubical_complexes.Torus(); Tc
        Cubical complex with 16 vertices and 64 cubes
        sage: Ts = SimplicialComplex(Tc); Ts
        Simplicial complex with 16 vertices and 32 facets
        sage: Ts.homology()                                                             # needs sage.modules
        {0: 0, 1: Z x Z, 2: Z}

    In the situation where the first argument is a simplicial complex
    or another object with a built-in conversion, most of the other
    arguments are ignored. The only exception is ``is_mutable``::

        sage: S.is_mutable()
        True
        sage: SimplicialComplex(S, is_mutable=False).is_mutable()
        False

    From a characteristic monotone boolean function, e.g. the simplicial complex
    of all subsets `S\\subseteq \\{0,1,2,3,4\\}` such that `sum(S)\\leq 4`::

        sage: SimplicialComplex(from_characteristic_function=(lambda x:sum(x)<=4, range(5)))
        Simplicial complex with vertex set (0, 1, 2, 3, 4) and facets {(0, 4), (0, 1, 2), (0, 1, 3)}

    or e.g. the simplicial complex of all 168 hyperovals of the projective plane of order 4::

        sage: l = designs.ProjectiveGeometryDesign(2, 1, GF(4,name='a'))                # needs sage.rings.finite_rings
        sage: f = lambda S: not any(len(set(S).intersection(x))>2 for x in l)
        sage: SimplicialComplex(from_characteristic_function=(f, l.ground_set()))       # needs sage.rings.finite_rings, long time
        Simplicial complex with 21 vertices and 168 facets

    TESTS:

    Check that we can make mutable copies (see :issue:`14142`)::

        sage: S = SimplicialComplex([[0,2], [0,3]], is_mutable=False)
        sage: S.is_mutable()
        False
        sage: C = copy(S)
        sage: C.is_mutable()
        True
        sage: SimplicialComplex(S, is_mutable=True).is_mutable()
        True
        sage: SimplicialComplex(S, is_immutable=False).is_mutable()
        True

    .. WARNING::

        Simplicial complexes are not proper parents as they do
        not possess element classes. In particular, parents are assumed
        to be hashable (and hence immutable) by the coercion framework.
        However this is close enough to being a parent with elements
        being the faces of ``self`` that we currently allow this abuse.
    """
    def __init__(self, maximal_faces=None, from_characteristic_function=None, maximality_check: bool = True, sort_facets=None, name_check: bool = False, is_mutable: bool = True, is_immutable: bool = False, category=None) -> None:
        """
        Define a simplicial complex.  See ``SimplicialComplex`` for more
        documentation.

        EXAMPLES::

            sage: SimplicialComplex([[0,2], [0,3], [0]])
            Simplicial complex with vertex set (0, 2, 3) and facets {(0, 2), (0, 3)}
            sage: SimplicialComplex((('a', 'b'), ['a', 'c'], ('b', 'c'))) == SimplicialComplex((('a', 'b'), ('b', 'c'), ('a', 'c')))
            True

        TESTS::

            sage: S = SimplicialComplex([[1,4], [2,4]])
            sage: S2 = SimplicialComplex([[1,4], [2,4]], is_mutable=False)
            sage: S == S2
            True
            sage: S3 = SimplicialComplex(maximal_faces=[[1,4], [2,4]])
            sage: S == S3
            True

        Test that we have fixed a problem revealed in :issue:`20718`;
        see also :issue:`20720`::

            sage: SimplicialComplex([2])
            Simplicial complex with vertex set (0, 1, 2) and facets {(0, 1, 2)}

            sage: S = SimplicialComplex((('a', 'b'), ('a', 'c'), ('b', 'c')))
            sage: S == loads(dumps(S))
            True

            sage: TestSuite(S).run()
            sage: TestSuite(S3).run()

        Test ``sort_facets``::

            sage: S = SimplicialComplex((('a', 'b'), ('a', 'c'), ('b', 'c')), sort_facets=True)
            Traceback (most recent call last):
            ...
            TypeError: sort_facets must be a dict
            sage: S = SimplicialComplex((('a', 'b'), ('a', 'c'), ('b', 'c')), sort_facets={'a': 1, 6: 3, 'c': 2})
            Traceback (most recent call last):
            ...
            ValueError: the set of keys of sort_facets must equal the set of vertices
            sage: S = SimplicialComplex((('a', 'b'), ('a', 'c'), ('b', 'c')), sort_facets={'a': 1, 'b': 3, 'c': 2})
            sage: S._vertex_to_index['b']
            3
        """
    def __hash__(self):
        """
        Compute the hash value of ``self``.

        If this simplicial complex is immutable, it computes the hash value
        based upon the facets. Otherwise it raises a :class`ValueError`.

        EXAMPLES::

            sage: S = SimplicialComplex([[1,4], [2,4]])
            sage: hash(S)
            Traceback (most recent call last):
            ...
            ValueError: this simplicial complex must be immutable; call set_immutable()
            sage: S.set_immutable()
            sage: hash(S) == hash(S)
            True
            sage: S2 = SimplicialComplex([[1,4], [2,4]], is_mutable=False)
            sage: S == S2
            True
            sage: hash(S) == hash(S2)
            True
        """
    def __eq__(self, right):
        """
        Two simplicial complexes are equal iff their vertex sets are
        equal and their sets of facets are equal.

        EXAMPLES::

            sage: SimplicialComplex([[1,2], [2,3], [4]]) == SimplicialComplex([[4], [2,3], [3], [2,1]])
            True
            sage: X = SimplicialComplex()
            sage: X.add_face([1,3])
            sage: X == SimplicialComplex([[1,3]])
            True
        """
    def __ne__(self, right):
        """
        Return ``True`` if ``self`` and ``right`` are not equal.

        EXAMPLES::

            sage: SimplicialComplex([[1,2], [2,3], [4]]) != SimplicialComplex([[4], [2,3], [3], [2,1]])
            False
            sage: X = SimplicialComplex()
            sage: X.add_face([1,3])
            sage: X != SimplicialComplex([[1,3]])
            False
        """
    def __copy__(self):
        """
        Return a mutable copy of ``self``.

        EXAMPLES::

            sage: S = SimplicialComplex([[0,2], [0,3]], is_mutable=False)
            sage: S.is_mutable()
            False
            sage: C = copy(S)
            sage: C.is_mutable()
            True
            sage: C == S
            True
            sage: S.is_mutable()
            False
            sage: T = copy(C)
            sage: T == C
            True
        """
    def vertices(self):
        """
        The vertex set, as a tuple, of this simplicial complex.

        EXAMPLES::

            sage: S = SimplicialComplex([[i] for i in range(16)] + [[0,1], [1,2]])
            sage: S
            Simplicial complex with 16 vertices and 15 facets
            sage: sorted(S.vertices())
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is a simplex which is contained in this complex.

        EXAMPLES::

            sage: K = SimplicialComplex([(0,1,2), (0,2,3)])
            sage: Simplex((0,2)) in K
            True
            sage: Simplex((1,3)) in K
            False
            sage: 0 in K  # not a simplex
            False
        """
    def __call__(self, simplex):
        """
        If ``simplex`` is a simplex in this complex, return it.

        Otherwise, this raises a :exc:`ValueError`.

        EXAMPLES::

            sage: K = SimplicialComplex([(0,1,2), (0,2,3)])
            sage: K(Simplex((1,2)))
            (1, 2)
            sage: K(Simplex((0,1,3)))
            Traceback (most recent call last):
            ...
            ValueError: the simplex is not in this complex
        """
    def maximal_faces(self):
        """
        The maximal faces (a.k.a. facets) of this simplicial complex.

        This just returns the set of facets used in defining the
        simplicial complex, so if the simplicial complex was defined
        with no maximality checking, none is done here, either.

        EXAMPLES::

            sage: Y = SimplicialComplex([[0,2], [1,4]])
            sage: sorted(Y.maximal_faces())
            [(0, 2), (1, 4)]

        ``facets`` is a synonym for ``maximal_faces``::

            sage: S = SimplicialComplex([[0,1], [0,1,2]])
            sage: S.facets()
            {(0, 1, 2)}
        """
    facets = maximal_faces
    def faces(self, subcomplex=None):
        """
        The faces of this simplicial complex, in the form of a
        dictionary of sets keyed by dimension.  If the optional
        argument ``subcomplex`` is present, then return only the
        faces which are *not* in the subcomplex.

        INPUT:

        - ``subcomplex`` -- a subcomplex of this simplicial complex (default:
          ``None``); return faces which are not in this subcomplex

        EXAMPLES::

            sage: Y = SimplicialComplex([[1,2], [1,4]])
            sage: Y.faces()
            {-1: {()}, 0: {(1,), (2,), (4,)}, 1: {(1, 2), (1, 4)}}
            sage: L = SimplicialComplex([[1,2]])
            sage: Y.faces(subcomplex=L)
            {-1: set(), 0: {(4,)}, 1: {(1, 4)}}
        """
    def face_iterator(self, increasing: bool = True) -> Generator[Incomplete, Incomplete]:
        """
        An iterator for the faces in this simplicial complex.

        INPUT:

        - ``increasing`` -- boolean (default: ``True``); if ``True``, return
          faces in increasing order of dimension, thus starting with
          the empty face. Otherwise it returns faces in decreasing order of
          dimension.

        .. NOTE::

            Among the faces of a fixed dimension, there is no sorting.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: sorted(S1.face_iterator())
            [(), (0,), (0, 1), (0, 2), (1,), (1, 2), (2,)]
        """
    cells = faces
    n_faces: Incomplete
    def is_pure(self):
        """
        Return ``True`` iff this simplicial complex is pure.

        A simplicial complex is pure if and only if all of its maximal faces
        have the same dimension.

        .. WARNING::

           This may give the wrong answer if the simplicial complex
           was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: U = SimplicialComplex([[1,2], [1, 3, 4]])
            sage: U.is_pure()
            False
            sage: X = SimplicialComplex([[0,1], [0,2], [1,2]])
            sage: X.is_pure()
            True

        Demonstration of the warning::

            sage: S = SimplicialComplex([[0,1], [0]], maximality_check=False)
            sage: S.is_pure()
            False
        """
    def h_vector(self):
        """
        The `h`-vector of this simplicial complex.

        If the complex has dimension `d` and `(f_{-1}, f_0, f_1, ...,
        f_d)` is its `f`-vector (with `f_{-1} = 1`, representing the
        empty simplex), then the `h`-vector `(h_0, h_1, ..., h_d,
        h_{d+1})` is defined by

        .. MATH::

           \\sum_{i=0}^{d+1} h_i x^{d+1-i} = \\sum_{i=0}^{d+1} f_{i-1} (x-1)^{d+1-i}.

        Alternatively,

        .. MATH::

           h_j = \\sum_{i=-1}^{j-1} (-1)^{j-i-1} \\binom{d-i}{j-i-1} f_i.

        EXAMPLES:

        The `f`- and `h`-vectors of the boundary of an octahedron are
        computed in :wikipedia:`Simplicial_complex`::

            sage: square = SimplicialComplex([[0,1], [1,2], [2,3], [0,3]])
            sage: S0 = SimplicialComplex([[0], [1]])
            sage: octa = square.join(S0) # boundary of an octahedron
            sage: octa.f_vector()
            [1, 6, 12, 8]
            sage: octa.h_vector()
            [1, 3, 3, 1]
        """
    def g_vector(self):
        """
        The `g`-vector of this simplicial complex.

        If the `h`-vector of the complex is `(h_0, h_1, ..., h_d,
        h_{d+1})` -- see :meth:`h_vector` -- then its `g`-vector
        `(g_0, g_1, ..., g_{[(d+1)/2]})` is defined by `g_0 = 1` and
        `g_i = h_i - h_{i-1}` for `i > 0`.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: S3 = simplicial_complexes.Sphere(3).barycentric_subdivision()
            sage: S3.f_vector()
            [1, 30, 150, 240, 120]
            sage: S3.h_vector()
            [1, 26, 66, 26, 1]
            sage: S3.g_vector()
            [1, 25, 40]
        """
    def face(self, simplex, i):
        """
        The `i`-th face of ``simplex`` in this simplicial complex.

        INPUT:

        - ``simplex`` -- a simplex in this simplicial complex
        - ``i`` -- integer

        EXAMPLES::

            sage: S = SimplicialComplex([[0,1,4], [0,1,2]])
            sage: S.face(Simplex((0,2)), 0)
            (2,)

            sage: S.face(Simplex((0,3)), 0)
            Traceback (most recent call last):
            ...
            ValueError: this simplex is not in this simplicial complex
        """
    def f_triangle(self):
        """
        Compute the `f`-triangle of ``self``.

        The `f`-triangle is given by `f_{i,j}` being the number of
        faces `F` of size `j` such that `i = \\max_{G \\subseteq F} |G|`.

        .. SEEALSO::

            Not to be confused with :meth:`F_triangle` .

        EXAMPLES::

            sage: X = SimplicialComplex([[1,2,3], [3,4,5], [1,4], [1,5], [2,4], [2,5]])
            sage: X.f_triangle()   # this complex is not pure
            [[0],
             [0, 0],
             [0, 0, 4],
             [1, 5, 6, 2]]

        A complex is pure if and only if the last row is nonzero::

            sage: X = SimplicialComplex([[1,2,3], [3,4,5], [1,4,5]])
            sage: X.f_triangle()
            [[0], [0, 0], [0, 0, 0], [1, 5, 8, 3]]
        """
    def h_triangle(self):
        """
        Compute the `h`-triangle of ``self``.

        The `h`-triangle of a simplicial complex `\\Delta` is given by

        .. MATH::

            h_{i,j} = \\sum_{k=0}^j (-1)^{j-k} \\binom{i-k}{j-k} f_{i,k},

        where `f_{i,k}` is the `f`-triangle of `\\Delta`.

        EXAMPLES::

            sage: X = SimplicialComplex([[1,2,3], [3,4,5], [1,4], [1,5], [2,4], [2,5]])
            sage: X.h_triangle()
            [[0],
             [0, 0],
             [0, 0, 4],
             [1, 2, -1, 0]]
        """
    def F_triangle(self, S):
        """
        Return the F-triangle of ``self`` with respect
        to one maximal simplex ``S``.

        This is the bivariate generating polynomial of all faces,
        according to the number of elements in ``S`` and outside ``S``.

        OUTPUT: an :class:`~sage.combinat.triangles_FHM.F_triangle`

        .. SEEALSO::

            Not to be confused with :meth:`f_triangle` .

        EXAMPLES::

            sage: cs = simplicial_complexes.Torus()
            sage: cs.F_triangle(cs.facets()[0])                                         # needs sage.combinat
            F: x^3 + 9*x^2*y + 3*x*y^2 + y^3 + 6*x^2 + 12*x*y
            + 3*y^2 + 4*x + 3*y + 1

        TESTS::

            sage: S = SimplicialComplex([])
            sage: S.F_triangle(S.facets()[0])                                           # needs sage.combinat
            F: 1
        """
    def flip_graph(self):
        """
        If ``self`` is pure, return the flip graph of ``self``,
        otherwise, return ``None``.

        The flip graph of a pure simplicial complex is the (undirected) graph
        with vertices being the facets, such that two facets are joined by
        an edge if they meet in a codimension `1` face.

        The flip graph is used to detect if ``self`` is a pseudomanifold.

        EXAMPLES::

            sage: S0 = simplicial_complexes.Sphere(0)
            sage: G = S0.flip_graph()
            sage: G.vertices(sort=True); G.edges(sort=True, labels=False)
            [(0,), (1,)]
            [((0,), (1,))]

            sage: G = (S0.wedge(S0)).flip_graph()
            sage: G.vertices(sort=True); G.edges(sort=True, labels=False)
            [(0,), ('L1',), ('R1',)]
            [((0,), ('L1',)), ((0,), ('R1',)), (('L1',), ('R1',))]

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S2 = simplicial_complexes.Sphere(2)
            sage: G = (S1.wedge(S1)).flip_graph()
            sage: len(G.vertices(sort=False))
            6
            sage: len(G.edges(sort=False))
            10

            sage: (S1.wedge(S2)).flip_graph() is None
            True

            sage: G = S2.flip_graph()
            sage: G.vertices(sort=True); G.edges(sort=True, labels=False)
            [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
            [((0, 1, 2), (0, 1, 3)),
             ((0, 1, 2), (0, 2, 3)),
             ((0, 1, 2), (1, 2, 3)),
             ((0, 1, 3), (0, 2, 3)),
             ((0, 1, 3), (1, 2, 3)),
             ((0, 2, 3), (1, 2, 3))]

            sage: T = simplicial_complexes.Torus()
            sage: G = T.suspension(4).flip_graph()
            sage: len(G.vertices(sort=False)); len(G.edges(sort=False, labels=False))
            46
            161
        """
    def is_pseudomanifold(self):
        """
        Return ``True`` if ``self`` is a pseudomanifold.

        A pseudomanifold is a simplicial complex with the following properties:

        - it is pure of some dimension `d` (all of its facets are `d`-dimensional)
        - every `(d-1)`-dimensional simplex is the face of exactly two facets
        - for every two facets `S` and `T`, there is a sequence of
          facets

          .. MATH::

            S = f_0, f_1, ..., f_n = T

          such that for each `i`, `f_i` and `f_{i-1}` intersect in a
          `(d-1)`-simplex.

        By convention, `S^0` is the only 0-dimensional pseudomanifold.

        EXAMPLES::

            sage: S0 = simplicial_complexes.Sphere(0)
            sage: S0.is_pseudomanifold()
            True
            sage: (S0.wedge(S0)).is_pseudomanifold()
            False
            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S2 = simplicial_complexes.Sphere(2)
            sage: (S1.wedge(S1)).is_pseudomanifold()
            False
            sage: (S1.wedge(S2)).is_pseudomanifold()
            False
            sage: S2.is_pseudomanifold()
            True
            sage: T = simplicial_complexes.Torus()
            sage: T.suspension(4).is_pseudomanifold()
            True
        """
    def product(self, right, rename_vertices: bool = True, is_mutable: bool = True):
        '''
        The product of this simplicial complex with another one.

        INPUT:

        - ``right`` -- the other simplicial complex (the right-hand factor)

        - ``rename_vertices`` -- boolean (default: ``True``); if this is
          ``False``, then the vertices in the product are the set of ordered
          pairs `(v,w)` where `v` is a vertex in ``self`` and `w` is a vertex
          in ``right``. If this is ``True``, then the vertices are renamed as
          "LvRw" (e.g., the vertex (1,2) would become "L1R2"). This is useful
          if you want to define the Stanley-Reisner ring of the complex: vertex
          names like (0,1) are not suitable for that, while vertex names like
          "L0R1" are.

        - ``is_mutable`` -- boolean (default: ``True``); determines whether the
          output is mutable

        The vertices in the product will be the set of ordered pairs
        `(v,w)` where `v` is a vertex in ``self`` and `w` is a vertex in
        right.

        .. WARNING::

           If ``X`` and ``Y`` are simplicial complexes, then ``X*Y``
           returns their join, not their product.

        EXAMPLES::

            sage: S = SimplicialComplex([[0,1], [1,2], [0,2]]) # circle
            sage: K = SimplicialComplex([[0,1]])   # edge
            sage: Cyl = S.product(K)  # cylinder
            sage: sorted(Cyl.vertices())
            [\'L0R0\', \'L0R1\', \'L1R0\', \'L1R1\', \'L2R0\', \'L2R1\']
            sage: Cyl2 = S.product(K, rename_vertices=False)
            sage: sorted(Cyl2.vertices())
            [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
            sage: T = S.product(S)  # torus
            sage: T
            Simplicial complex with 9 vertices and 18 facets
            sage: T.homology()                                                          # needs sage.modules
            {0: 0, 1: Z x Z, 2: Z}

        These can get large pretty quickly::

            sage: T = simplicial_complexes.Torus(); T
            Minimal triangulation of the torus
            sage: K = simplicial_complexes.KleinBottle(); K
            Minimal triangulation of the Klein bottle
            sage: T.product(K)      # long time: 5 or 6 seconds
            Simplicial complex with 56 vertices and 1344 facets
        '''
    def join(self, right, rename_vertices: bool = True, is_mutable: bool = True):
        '''
        The join of this simplicial complex with another one.

        The join of two simplicial complexes `S` and `T` is the
        simplicial complex `S*T` with simplices of the form `[v_0,
        ..., v_k, w_0, ..., w_n]` for all simplices `[v_0, ..., v_k]` in
        `S` and `[w_0, ..., w_n]` in `T`.

        INPUT:

        - ``right`` -- the other simplicial complex (the right-hand factor)

        - ``rename_vertices`` -- boolean (default: ``True``); if this is
          ``True``, the vertices in the join will be renamed by the formula:
          vertex "v" in the left-hand factor --> vertex "Lv" in the join,
          vertex "w" in the right-hand factor --> vertex "Rw" in the join.
          If this is ``False``, this tries to construct the join without
          renaming the vertices; this will cause problems if the two factors
          have any vertices with names in common.

        - ``is_mutable`` -- boolean (default: ``True``); determine whether the
          output is mutable

        EXAMPLES::

            sage: S = SimplicialComplex([[0], [1]])
            sage: T = SimplicialComplex([[2], [3]])
            sage: S.join(T)
            Simplicial complex with vertex set (\'L0\', \'L1\', \'R2\', \'R3\') and 4 facets
            sage: S.join(T, rename_vertices=False)
            Simplicial complex with vertex set (0, 1, 2, 3)
            and facets {(0, 2), (0, 3), (1, 2), (1, 3)}

        The notation \'*\' may be used, as well::

            sage: S * S
            Simplicial complex with vertex set (\'L0\', \'L1\', \'R0\', \'R1\') and 4 facets
            sage: S * S * S * S * S * S * S * S
            Simplicial complex with 16 vertices and 256 facets
        '''
    __mul__ = join
    def cone(self, is_mutable: bool = True):
        """
        The cone on this simplicial complex.

        INPUT:

        - ``is_mutable`` -- boolean (default: ``True``); determines whether
          the output is mutable

        The cone is the simplicial complex formed by adding a new
        vertex `C` and simplices of the form `[C, v_0, ..., v_k]` for
        every simplex `[v_0, ..., v_k]` in the original simplicial
        complex.  That is, the cone is the join of the original
        complex with a one-point simplicial complex.

        EXAMPLES::

            sage: S = SimplicialComplex([[0], [1]])
            sage: CS = S.cone()
            sage: sorted(CS.vertices())
            ['L0', 'L1', 'R0']
            sage: len(CS.facets())
            2
            sage: CS.facets() == set([Simplex(['L0', 'R0']), Simplex(['L1', 'R0'])])
            True
        """
    def suspension(self, n: int = 1, is_mutable: bool = True):
        '''
        The suspension of this simplicial complex.

        INPUT:

        - ``n`` -- positive integer (default: 1); suspend this many times

        - ``is_mutable`` -- boolean (default: ``True``); determine whether
          the output is mutable

        The suspension is the simplicial complex formed by adding two
        new vertices `S_0` and `S_1` and simplices of the form `[S_0,
        v_0, ..., v_k]` and `[S_1, v_0, ..., v_k]` for every simplex
        `[v_0, ..., v_k]` in the original simplicial complex.  That
        is, the suspension is the join of the original complex with a
        two-point simplicial complex.

        If the simplicial complex `M` happens to be a pseudomanifold
        (see :meth:`is_pseudomanifold`), then this instead constructs
        Datta\'s one-point suspension (see [Dat2007]_, p. 434):
        choose a vertex `u` in `M` and choose a new vertex
        `w` to add.  Denote the join of simplices by "`*`".  The
        facets in the one-point suspension are of the two forms

        - `u * \\alpha` where `\\alpha` is a facet of `M` not containing
          `u`

        - `w * \\beta` where `\\beta` is any facet of `M`.

        EXAMPLES::

            sage: S0 = SimplicialComplex([[0], [1]])
            sage: S0.suspension() == simplicial_complexes.Sphere(1)
            True
            sage: S3 = S0.suspension(3)  # the 3-sphere
            sage: S3.homology()                                                         # needs sage.modules
            {0: 0, 1: 0, 2: 0, 3: Z}

        For pseudomanifolds, the complex constructed here will be
        smaller than that obtained by taking the join with the
        0-sphere: the join adds two vertices, while this construction
        only adds one. ::

            sage: T = simplicial_complexes.Torus()
            sage: sorted(T.join(S0).vertices())      # 9 vertices
            [\'L0\', \'L1\', \'L2\', \'L3\', \'L4\', \'L5\', \'L6\', \'R0\', \'R1\']
            sage: T.suspension().vertices()  # 8 vertices
            (0, 1, 2, 3, 4, 5, 6, 7)
        '''
    def disjoint_union(self, right, is_mutable: bool = True):
        """
        The disjoint union of this simplicial complex with another one.

        INPUT:

        - ``right`` -- the other simplicial complex (the right-hand factor)

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S2 = simplicial_complexes.Sphere(2)
            sage: S1.disjoint_union(S2).homology()                                      # needs sage.modules
            {0: Z, 1: Z, 2: Z}
        """
    def wedge(self, right, rename_vertices: bool = True, is_mutable: bool = True):
        '''
        The wedge (one-point union) of this simplicial complex with
        another one.

        INPUT:

        - ``right`` -- the other simplicial complex (the right-hand factor)

        - ``rename_vertices`` -- boolean (default: ``True``); if this is
          ``True``, the vertices in the wedge will be renamed by the formula:
          first vertex in each are glued together and called "0".  Otherwise,
          each vertex "v" in the left-hand factor --> vertex "Lv" in the wedge,
          vertex "w" in the right-hand factor --> vertex "Rw" in the wedge.  If
          this is ``False``, this tries to construct the wedge without renaming
          the vertices; this will cause problems if the two factors have any
          vertices with names in common.

        - ``is_mutable`` -- boolean (default: ``True``); determine whether
          the output is mutable

        .. NOTE::

            This operation is not well-defined if ``self`` or
            ``other`` is not path-connected.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S2 = simplicial_complexes.Sphere(2)
            sage: S1.wedge(S2).homology()                                               # needs sage.modules
            {0: 0, 1: Z, 2: Z}
        '''
    def chain_complex(self, subcomplex=None, augmented: bool = False, verbose: bool = False, check: bool = False, dimensions=None, base_ring=..., cochain: bool = False):
        """
        The chain complex associated to this simplicial complex.

        INPUT:

        - ``dimensions`` -- if ``None``, compute the chain complex in all
          dimensions.  If a list or tuple of integers, compute the
          chain complex in those dimensions, setting the chain groups
          in all other dimensions to zero.
        - ``base_ring`` -- commutative ring (default: ``ZZ``)
        - ``subcomplex`` -- a subcomplex of this simplicial complex (default:
          empty); compute the chain complex relative to this subcomplex
        - ``augmented`` -- boolean (default: ``False``); if ``True``, return
          the augmented chain complex (that is, include a class in dimension
          `-1` corresponding to the empty cell). This is ignored if
          ``dimensions`` is specified
        - ``cochain`` -- boolean (default: ``False``); if ``True``, return the
          cochain complex (that is, the dual of the chain complex)
        - ``verbose`` -- boolean (default: ``False``); if ``True``, print some
          messages as the chain complex is computed
        - ``check`` -- boolean (default: ``False``); if ``True``, make sure
          that the chain complex is actually a chain complex: the differentials
          are composable and their product is zero

        .. NOTE::

           If subcomplex is nonempty, then the argument ``augmented``
           has no effect: the chain complex relative to a nonempty
           subcomplex is zero in dimension `-1`.

        The rows and columns of the boundary matrices are indexed by
        the lists given by the :meth:`_n_cells_sorted` method, which by
        default are sorted.

        EXAMPLES::

            sage: circle = SimplicialComplex([[0,1], [1,2], [0, 2]])
            sage: circle.chain_complex()                                                # needs sage.modules
            Chain complex with at most 2 nonzero terms over Integer Ring
            sage: circle.chain_complex()._latex_()                                      # needs sage.modules
            '\\\\Bold{Z}^{3} \\\\xrightarrow{d_{1}} \\\\Bold{Z}^{3}'
            sage: circle.chain_complex(base_ring=QQ, augmented=True)                    # needs sage.modules
            Chain complex with at most 3 nonzero terms over Rational Field
        """
    @cached_method
    def algebraic_topological_model(self, base_ring=None):
        '''
        Algebraic topological model for this simplicial complex with
        coefficients in ``base_ring``.

        The term "algebraic topological model" is defined by Pilarczyk
        and Réal [PR2015]_.

        INPUT:

        - ``base_ring`` -- coefficient ring (default: ``QQ``); must be a field

        Denote by `C` the chain complex associated to this simplicial
        complex. The algebraic topological model is a chain complex
        `M` with zero differential, with the same homology as `C`,
        along with chain maps `\\pi: C \\to M` and `\\iota: M \\to C`
        satisfying `\\iota \\pi = 1_M` and `\\pi \\iota` chain homotopic
        to `1_C`. The chain homotopy `\\phi` must satisfy

        - `\\phi \\phi = 0`,
        - `\\pi \\phi = 0`,
        - `\\phi \\iota = 0`.

        Such a chain homotopy is called a *chain contraction*.

        OUTPUT: a pair consisting of

        - chain contraction ``phi`` associated to `C`, `M`, `\\pi`, and
          `\\iota`
        - the chain complex `M`

        Note that from the chain contraction ``phi``, one can recover the
        chain maps `\\pi` and `\\iota` via ``phi.pi()`` and
        ``phi.iota()``. Then one can recover `C` and `M` from, for
        example, ``phi.pi().domain()`` and ``phi.pi().codomain()``,
        respectively.

        EXAMPLES::

            sage: # needs sage.modules
            sage: RP2 = simplicial_complexes.RealProjectivePlane()
            sage: phi, M = RP2.algebraic_topological_model(GF(2))
            sage: M.homology()
            {0: Vector space of dimension 1 over Finite Field of size 2,
             1: Vector space of dimension 1 over Finite Field of size 2,
             2: Vector space of dimension 1 over Finite Field of size 2}
            sage: T = simplicial_complexes.Torus()
            sage: phi, M = T.algebraic_topological_model(QQ)
            sage: M.homology()
            {0: Vector space of dimension 1 over Rational Field,
             1: Vector space of dimension 2 over Rational Field,
             2: Vector space of dimension 1 over Rational Field}
        '''
    def alexander_whitney(self, simplex, dim_left):
        """
        Subdivide this simplex into a pair of simplices.

        If this simplex has vertices `v_0`, `v_1`, ..., `v_n`, then
        subdivide it into simplices `(v_0, v_1, ..., v_{dim})` and
        `(v_{dim}, v_{dim + 1}, ..., v_n)`.

        See :meth:`Simplex.alexander_whitney` for more details. This
        method just calls that one.

        INPUT:

        - ``simplex`` -- a simplex in this complex
        - ``dim`` -- integer between 0 and one more than the
          dimension of this simplex

        OUTPUT: list containing just the triple ``(1, left,
        right)``, where ``left`` and ``right`` are the two simplices
        described above.

        EXAMPLES::

            sage: s = Simplex((0,1,3,4))
            sage: X = SimplicialComplex([s])
            sage: X.alexander_whitney(s, 0)
            [(1, (0,), (0, 1, 3, 4))]
            sage: X.alexander_whitney(s, 2)
            [(1, (0, 1, 3), (3, 4))]
        """
    def add_face(self, face) -> None:
        """
        Add a face to this simplicial complex.

        INPUT:

        - ``face`` -- a subset of the vertex set

        This *changes* the simplicial complex, adding a new face and all
        of its subfaces.

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1], [0,2]])
            sage: X.add_face([0,1,2,]); X
            Simplicial complex with vertex set (0, 1, 2) and facets {(0, 1, 2)}
            sage: Y = SimplicialComplex(); Y
            Simplicial complex with vertex set () and facets {()}
            sage: Y.add_face([0,1])
            sage: Y.add_face([1,2,3])
            sage: Y
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(0, 1), (1, 2, 3)}

        If you add a face which is already present, there is no effect::

            sage: Y.add_face([1,3]); Y
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(0, 1), (1, 2, 3)}

        TESTS:

        Check that the bug reported at :issue:`14354` has been fixed::

            sage: T = SimplicialComplex([range(1,5)]).n_skeleton(1)
            sage: T.homology()                                                          # needs sage.modules
            {0: 0, 1: Z x Z x Z}
            sage: T.add_face([1,2,3])
            sage: T.homology()                                                          # needs sage.modules
            {0: 0, 1: Z x Z, 2: 0}

        Check that the ``_faces`` cache is treated correctly
        (:issue:`20758`)::

            sage: T = SimplicialComplex([range(1,5)]).n_skeleton(1)
            sage: _ = T.faces()       # populate the _faces attribute
            sage: _ = T.homology()    # add more to _faces                              # needs sage.modules
            sage: T.add_face((1,2,3))
            sage: all(Simplex((1,2,3)) in T._faces[L][2] for L in T._faces)
            True

        Check that the ``__enlarged`` cache is treated correctly
        (:issue:`20758`)::

            sage: T = SimplicialComplex([range(1,5)]).n_skeleton(1)
            sage: T.homology()  # to populate the __enlarged attribute                  # needs sage.modules
            {0: 0, 1: Z x Z x Z}
            sage: T.add_face([1,2,3])
            sage: len(T._SimplicialComplex__enlarged) > 0                               # needs sage.modules
            True

        Check we've fixed the bug reported at :issue:`14578`::

            sage: t0 = SimplicialComplex()
            sage: t0.add_face(('a', 'b'))
            sage: t0.add_face(('c', 'd', 'e'))
            sage: t0.add_face(('e', 'f', 'c'))
            sage: t0.homology()                                                         # needs sage.modules
            {0: Z, 1: 0, 2: 0}

        Check that we've fixed the bug reported at :issue:`22880`::

            sage: X = SimplicialComplex([[0], [1]])
            sage: temp = X.faces(SimplicialComplex(()))
            sage: X.add_face([0,1])
        """
    def remove_face(self, face, check: bool = False) -> None:
        """
        Remove a face from this simplicial complex.

        INPUT:

        - ``face`` -- a face of the simplicial complex

        - ``check`` -- boolean (default: ``False``); if
          ``True``, raise an error if ``face`` is not a
          face of this simplicial complex

        This does not return anything; instead, it *changes* the
        simplicial complex.

        ALGORITHM:

        The facets of the new simplicial complex are
        the facets of the original complex not containing ``face``,
        together with those of ``link(face)*boundary(face)``.

        EXAMPLES::

            sage: S = range(1,5)
            sage: Z = SimplicialComplex([S]); Z
            Simplicial complex with vertex set (1, 2, 3, 4) and facets {(1, 2, 3, 4)}
            sage: Z.remove_face([1,2])
            sage: Z
            Simplicial complex with vertex set (1, 2, 3, 4) and
             facets {(1, 3, 4), (2, 3, 4)}

            sage: S = SimplicialComplex([[0,1,2],[2,3]])
            sage: S
            Simplicial complex with vertex set (0, 1, 2, 3) and
             facets {(2, 3), (0, 1, 2)}
            sage: S.remove_face([0,1,2])
            sage: S
            Simplicial complex with vertex set (0, 1, 2, 3) and
             facets {(0, 1), (0, 2), (1, 2), (2, 3)}

        TESTS:

        Check that the ``_faces`` cache is treated properly: see
        :issue:`20758`::

            sage: T = SimplicialComplex([range(1,5)]).n_skeleton(1)
            sage: _ = T.faces()     # populate the _faces attribute
            sage: _ = T.homology()  # add more to _faces                                # needs sage.modules
            sage: T.add_face((1,2,3))
            sage: T.remove_face((1,2,3))
            sage: len(T._faces)                                                         # needs sage.modules
            2
            sage: T.remove_face((1,2))
            sage: len(T._faces)
            1

        Check that the face to be removed can be given with a
        different vertex ordering::

            sage: S = SimplicialComplex([[1,2], [1,3]])
            sage: S.remove_face([3,1])
            sage: S
            Simplicial complex with vertex set (1, 2, 3) and facets {(3,), (1, 2)}
        """
    def remove_faces(self, faces, check: bool = False) -> None:
        """
        Remove a collection of faces from this simplicial complex.

        INPUT:

        - ``faces`` -- list (or any iterable) of faces of the simplicial
          complex

        - ``check`` -- boolean (default: ``False``); if ``True``, raise an
          error if any element of ``faces`` is not a face of this simplicial
          complex

        This does not return anything; instead, it *changes* the
        simplicial complex.

        ALGORITHM:

        Run ``self.remove_face(f)`` repeatedly, for ``f`` in ``faces``.

        EXAMPLES::

            sage: S = range(1,5)
            sage: Z = SimplicialComplex([S]); Z
            Simplicial complex with vertex set (1, 2, 3, 4) and facets {(1, 2, 3, 4)}
            sage: Z.remove_faces([[1,2]])
            sage: Z
            Simplicial complex with vertex set (1, 2, 3, 4) and facets {(1, 3, 4), (2, 3, 4)}

            sage: Z = SimplicialComplex([S]); Z
            Simplicial complex with vertex set (1, 2, 3, 4) and facets {(1, 2, 3, 4)}
            sage: Z.remove_faces([[1,2], [2,3]])
            sage: Z
            Simplicial complex with vertex set (1, 2, 3, 4) and facets {(2, 4), (1, 3, 4)}

        TESTS:

        Check the ``check`` argument::

            sage: Z = SimplicialComplex([[1,2,3,4]])
            sage: Z.remove_faces([[1,2], [3,4]])
            sage: Z.remove_faces([[1,2]])
            sage: Z.remove_faces([[1,2]], check=True)
            Traceback (most recent call last):
            ...
            ValueError: trying to remove a face which is not in the simplicial complex
        """
    def is_subcomplex(self, other):
        """
        Return ``True`` if this is a subcomplex of ``other``.

        INPUT:

        - ``other`` -- another simplicial complex

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S1.is_subcomplex(S1)
            True
            sage: Empty = SimplicialComplex()
            sage: Empty.is_subcomplex(S1)
            True
            sage: S1.is_subcomplex(Empty)
            False

            sage: sorted(S1.facets())
            [(0, 1), (0, 2), (1, 2)]
            sage: T = S1.product(S1)
            sage: sorted(T.facets())[0] # typical facet in T
            ('L0R0', 'L0R1', 'L1R1')
            sage: S1.is_subcomplex(T)
            False
            sage: T._contractible_subcomplex().is_subcomplex(T)
            True
        """
    def connected_sum(self, other, is_mutable: bool = True):
        '''
        The connected sum of this simplicial complex with another one.

        INPUT:

        - ``other`` -- another simplicial complex
        - ``is_mutable`` -- boolean (default: ``True``); determine whether
          the output is mutable

        OUTPUT: the connected sum ``self # other``

        .. WARNING::

           This does not check that ``self`` and ``other`` are manifolds,
           only that their facets all have the same dimension.  Since a
           (more or less) random facet is chosen from each complex and
           then glued together, this method may return random
           results if applied to non-manifolds, depending on which
           facet is chosen.

        Algorithm: a facet is chosen from each surface, and removed.
        The vertices of these two facets are relabeled to
        ``(0,1,...,dim)``.  Of the remaining vertices, the ones from
        the left-hand factor are renamed by prepending an "L", and
        similarly the remaining vertices in the right-hand factor are
        renamed by prepending an "R".

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S1.connected_sum(S1.connected_sum(S1)).homology()                     # needs sage.modules
            {0: 0, 1: Z}
            sage: P = simplicial_complexes.RealProjectivePlane(); P
            Minimal triangulation of the real projective plane
            sage: P.connected_sum(P)    # the Klein bottle
            Simplicial complex with 9 vertices and 18 facets

        The notation \'+\' may be used for connected sum, also::

            sage: P + P    # the Klein bottle
            Simplicial complex with 9 vertices and 18 facets
            sage: (P + P).homology()[1]                                                 # needs sage.modules
            Z x C2
        '''
    __add__ = connected_sum
    def link(self, simplex, is_mutable: bool = True):
        """
        The link of a simplex in this simplicial complex.

        The link of a simplex `F` is the simplicial complex formed by
        all simplices `G` which are disjoint from `F` but for which `F
        \\cup G` is a simplex.

        INPUT:

        - ``simplex`` -- a simplex in this simplicial complex
        - ``is_mutable`` -- boolean (default: ``True``); determine whether
          the output is mutable

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1,2], [1,2,3]])
            sage: X.link(Simplex([0]))
            Simplicial complex with vertex set (1, 2) and facets {(1, 2)}
            sage: X.link([1,2])
            Simplicial complex with vertex set (0, 3) and facets {(0,), (3,)}
            sage: Y = SimplicialComplex([[0,1,2,3]])
            sage: Y.link([1])
            Simplicial complex with vertex set (0, 2, 3) and facets {(0, 2, 3)}
        """
    def star(self, simplex, is_mutable: bool = True):
        """
        Return the star of a simplex in this simplicial complex.

        The star of ``simplex`` is the simplicial complex formed by
        all simplices which contain ``simplex``.

        INPUT:

        - ``simplex`` -- a simplex in this simplicial complex
        - ``is_mutable`` -- boolean (default: ``True``); determines if the output
          is mutable

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1,2], [1,2,3]])
            sage: X.star(Simplex([0]))
            Simplicial complex with vertex set (0, 1, 2) and facets {(0, 1, 2)}
            sage: X.star(Simplex([1]))
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(0, 1, 2), (1, 2, 3)}
            sage: X.star(Simplex([1,2]))
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(0, 1, 2), (1, 2, 3)}
            sage: X.star(Simplex([]))
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(0, 1, 2), (1, 2, 3)}
        """
    def is_cohen_macaulay(self, base_ring=..., ncpus: int = 0):
        """
        Return ``True`` if ``self`` is Cohen-Macaulay.

        A simplicial complex `\\Delta` is Cohen-Macaulay over `R` iff
        `\\tilde{H}_i(\\mathrm{lk}_\\Delta(F);R) = 0` for all
        `F \\in \\Delta` and `i < \\dim\\mathrm{lk}_\\Delta(F)`.
        Here, `\\Delta` is ``self`` and `R` is ``base_ring``, and
        `\\mathrm{lk}` denotes the link operator on ``self``.

        INPUT:

        - ``base_ring`` -- (default: ``QQ``) the base ring

        - ``ncpus`` -- (default: 0) number of cpus used for the
          computation. If this is 0, determine the number of cpus
          automatically based on the hardware being used.

        For finite simplicial complexes, this is equivalent to the
        statement that the Stanley-Reisner ring of ``self`` is
        Cohen-Macaulay.

        EXAMPLES:

        Spheres are Cohen-Macaulay::

            sage: S = SimplicialComplex([[1,2],[2,3],[3,1]])
            sage: S.is_cohen_macaulay(ncpus=3)                                          # needs sage.modules
            True

        The following example is taken from Bruns, Herzog - Cohen-Macaulay
        rings, Figure 5.3::

            sage: S = SimplicialComplex([[1,2,3],[1,4,5]])
            sage: S.is_cohen_macaulay(ncpus=3)                                          # needs sage.modules
            False

        The choice of base ring can matter.  The real projective plane `\\RR P^2`
        has `H_1(\\RR P^2) = \\ZZ/2`, hence is CM over `\\QQ` but not over `\\ZZ`. ::

            sage: X = simplicial_complexes.RealProjectivePlane()
            sage: X.is_cohen_macaulay()                                                 # needs sage.modules
            True
            sage: X.is_cohen_macaulay(ZZ)                                               # needs sage.modules
            False
        """
    def generated_subcomplex(self, sub_vertex_set, is_mutable: bool = True):
        """
        Return the largest sub-simplicial complex of ``self`` containing
        exactly ``sub_vertex_set`` as vertices.

        INPUT:

        - ``sub_vertex_set`` -- the sub-vertex set
        - ``is_mutable`` -- boolean (default: ``True``); determine whether
          the output is mutable

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(2)
            sage: S
            Minimal triangulation of the 2-sphere
            sage: S.generated_subcomplex([0,1,2])
            Simplicial complex with vertex set (0, 1, 2) and facets {(0, 1, 2)}
        """
    def is_shelling_order(self, shelling_order, certificate: bool = False):
        """
        Return if the order of the facets given by ``shelling_order``
        is a shelling order for ``self``.

        A sequence of facets `(F_i)_{i=1}^N` of a simplicial
        complex of dimension `d` is a *shelling order* if for all
        `i = 2, 3, 4, \\ldots`, the complex

        .. MATH::

            X_i = \\left( \\bigcup_{j=1}^{i-1} F_j \\right) \\cap F_i

        is pure and of dimension `\\dim F_i - 1`.

        INPUT:

        - ``shelling_order`` -- an ordering of the facets of ``self``
        - ``certificate`` -- boolean (default: ``False``); if ``True`` then returns
          the index of the first facet that violate the condition

        .. SEEALSO::

            :meth:`is_shellable`

        EXAMPLES::

            sage: facets = [[1,2,5],[2,3,5],[3,4,5],[1,4,5]]
            sage: X = SimplicialComplex(facets)
            sage: X.is_shelling_order(facets)
            True

            sage: b = [[1,2,5], [3,4,5], [2,3,5], [1,4,5]]
            sage: X.is_shelling_order(b)
            False
            sage: X.is_shelling_order(b, True)
            (False, 1)

        A non-pure example::

            sage: facets = [[1,2,3], [3,4], [4,5], [5,6], [4,6]]
            sage: X = SimplicialComplex(facets)
            sage: X.is_shelling_order(facets)
            True

        REFERENCES:

        - [BW1996]_
        """
    @cached_method
    def is_shellable(self, certificate: bool = False):
        """
        Return if ``self`` is shellable.

        A simplicial complex is shellable if there exists a shelling
        order.

        .. NOTE::

            1. This method can check all orderings of the facets by brute
               force, hence can be very slow.

            2. This is shellability in the general (nonpure) sense of
               Bjorner and Wachs [BW1996]_. This method does not check purity.

        .. SEEALSO::

            :meth:`is_shelling_order`

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True`` then
          returns the shelling order (if it exists)

        EXAMPLES::

            sage: X = SimplicialComplex([[1,2,5], [2,3,5], [3,4,5], [1,4,5]])
            sage: X.is_shellable()
            True
            sage: order = X.is_shellable(True); order
            ((1, 2, 5), (2, 3, 5), (1, 4, 5), (3, 4, 5))
            sage: X.is_shelling_order(order)
            True

            sage: X = SimplicialComplex([[1,2,3], [3,4,5]])
            sage: X.is_shellable()
            False

        Examples from Figure 1 in [BW1996]_::

            sage: X = SimplicialComplex([[1,2,3], [3,4], [4,5], [5,6], [4,6]])
            sage: X.is_shellable()
            True

            sage: X = SimplicialComplex([[1,2,3], [3,4], [4,5,6]])
            sage: X.is_shellable()
            False

        REFERENCES:

        - :wikipedia:`Shelling_(topology)`
        """
    def restriction_sets(self, order):
        """
        Return the restriction sets of the facets according to ``order``.

        A restriction set of a shelling order is the sequence of
        smallest new faces that are created during the shelling order.

        .. SEEALSO::

            :meth:`is_shelling_order`

        EXAMPLES::

            sage: facets = [[1,2,5], [2,3,5], [3,4,5], [1,4,5]]
            sage: X = SimplicialComplex(facets)
            sage: X.restriction_sets(facets)
            [(), (3,), (4,), (1, 4)]

            sage: b = [[1,2,5], [3,4,5], [2,3,5], [1,4,5]]
            sage: X.restriction_sets(b)
            Traceback (most recent call last):
            ...
            ValueError: not a shelling order
        """
    def minimal_nonfaces(self):
        """
        Set consisting of the minimal subsets of the vertex set of
        this simplicial complex which do not form faces.

        Algorithm: Proceeds through the faces of the complex increasing the
        dimension, starting from dimension 0, and add the faces that are not
        contained in the complex and that are not already contained in a
        previously seen minimal non-face.

        This is used in computing the
        :meth:`Stanley-Reisner ring<stanley_reisner_ring>` and the
        :meth:`Alexander dual<alexander_dual>`.

        EXAMPLES::

            sage: X = SimplicialComplex([[1,3],[1,2]])
            sage: X.minimal_nonfaces()
            {(2, 3)}
            sage: Y = SimplicialComplex([[0,1], [1,2], [2,3], [3,0]])
            sage: sorted(Y.minimal_nonfaces())
            [(0, 2), (1, 3)]

        TESTS::

            sage: SC = SimplicialComplex([(0,1,2),(0,2,3),(2,3,4),(1,2,4),             ....:                         (1,4,5),(0,3,6),(3,6,7),(4,5,7)])

        This was taking a long time before :issue:`20078`::

            sage: sorted(SC.minimal_nonfaces())
            [(0, 4),
             (0, 5),
             (0, 7),
             (1, 3),
             (1, 6),
             (1, 7),
             (2, 5),
             (2, 6),
             (2, 7),
             (3, 4, 7),
             (3, 5),
             (4, 6),
             (5, 6)]
        """
    def stanley_reisner_ring(self, base_ring=...):
        """
        The Stanley-Reisner ring of this simplicial complex.

        INPUT:

        - ``base_ring`` -- a commutative ring (default: ``ZZ``)

        OUTPUT: a quotient of a polynomial algebra with coefficients
        in ``base_ring``, with one generator for each vertex in the
        simplicial complex, by the ideal generated by the products
        of those vertices which do not form faces in it

        Thus the ideal is generated by the products corresponding to
        the minimal nonfaces of the simplicial complex.

        .. WARNING::

           This may be quite slow!

           Also, this may behave badly if the vertices have the
           'wrong' names. To avoid this, define the simplicial complex
           at the start with the flag ``name_check`` set to ``True``.

           More precisely, this is a quotient of a polynomial ring
           with one generator for each vertex.  If the name of a
           vertex is a nonnegative integer, then the corresponding
           polynomial generator is named ``'x'`` followed by that integer
           (e.g., ``'x2'``, ``'x3'``, ``'x5'``, ...).  Otherwise, the
           polynomial generators are given the same names as the vertices.
           Thus if the vertex set is ``(2, 'x2')``, there will be problems.

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1,2], [0,2,3]])
            sage: X.stanley_reisner_ring()
            Quotient of Multivariate Polynomial Ring in x0, x1, x2, x3 over Integer Ring
             by the ideal (x1*x3)
            sage: Y = SimplicialComplex([[0,1,2,3,4]]); Y
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and facets {(0, 1, 2, 3, 4)}
            sage: Y.add_face([0,1,2,3,4])
            sage: Y.stanley_reisner_ring(base_ring=QQ)
            Multivariate Polynomial Ring in x0, x1, x2, x3, x4 over Rational Field
        """
    def alexander_dual(self, is_mutable: bool = True):
        """
        The Alexander dual of this simplicial complex: according to
        the Macaulay2 documentation, this is the simplicial complex
        whose faces are the complements of its nonfaces.

        Thus find the minimal nonfaces and take their complements to
        find the facets in the Alexander dual.

        INPUT:

        - ``is_mutable`` -- boolean (default: ``True``); determine whether
          the output is mutable

        EXAMPLES::

            sage: Y = SimplicialComplex([[i] for i in range(5)]); Y
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and
             facets {(0,), (1,), (2,), (3,), (4,)}
            sage: Y.alexander_dual()
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and 10 facets
            sage: X = SimplicialComplex([[0,1], [1,2], [2,3], [3,0]])
            sage: X.alexander_dual()
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(0, 2), (1, 3)}
        """
    def barycentric_subdivision(self):
        """
        The barycentric subdivision of this simplicial complex.

        See :wikipedia:`Barycentric_subdivision` for a
        definition.

        EXAMPLES::

            sage: triangle = SimplicialComplex([[0,1], [1,2], [0, 2]])
            sage: hexagon = triangle.barycentric_subdivision(); hexagon
            Simplicial complex with 6 vertices and 6 facets
            sage: hexagon.homology(1) == triangle.homology(1)                           # needs sage.modules
            True

        Barycentric subdivisions can get quite large, since each
        `n`-dimensional facet in the original complex produces
        `(n+1)!` facets in the subdivision::

            sage: S4 = simplicial_complexes.Sphere(4); S4
            Minimal triangulation of the 4-sphere
            sage: S4.barycentric_subdivision()
            Simplicial complex with 62 vertices and 720 facets
        """
    def stellar_subdivision(self, simplex, inplace: bool = False, is_mutable: bool = True):
        """
        Return the stellar subdivision of a simplex in this simplicial complex.

        The stellar subdivision of a face is obtained by adding a new vertex to the
        simplicial complex ``self`` joined to the star of the face and then
        deleting the face ``simplex`` to the result.

        INPUT:

        - ``simplex`` -- a simplex face of ``self``
        - ``inplace`` -- boolean (default: ``False``); determines if the
          operation is done on ``self`` or on a copy
        - ``is_mutable`` -- boolean (default: ``True``); determines if the
          output is mutable

        OUTPUT:

        - A simplicial complex obtained by the stellar subdivision of the face
          ``simplex``

        EXAMPLES::

            sage: SC = SimplicialComplex([[0,1,2],[1,2,3]])
            sage: F1 = Simplex([1,2])
            sage: F2 = Simplex([1,3])
            sage: F3 = Simplex([1,2,3])
            sage: SC.stellar_subdivision(F1)
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and
             facets {(0, 1, 4), (0, 2, 4), (1, 3, 4), (2, 3, 4)}
            sage: SC.stellar_subdivision(F2)
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and
             facets {(0, 1, 2), (1, 2, 4), (2, 3, 4)}
            sage: SC.stellar_subdivision(F3)
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and
             facets {(0, 1, 2), (1, 2, 4), (1, 3, 4), (2, 3, 4)}
            sage: SC.stellar_subdivision(F3, inplace=True);SC
            Simplicial complex with vertex set (0, 1, 2, 3, 4) and
             facets {(0, 1, 2), (1, 2, 4), (1, 3, 4), (2, 3, 4)}

        The simplex to subdivide should be a face of self::

            sage: SC = SimplicialComplex([[0,1,2],[1,2,3]])
            sage: F4 = Simplex([3,4])
            sage: SC.stellar_subdivision(F4)
            Traceback (most recent call last):
            ...
            ValueError: the face to subdivide is not a face of self

        One can not modify an immutable simplicial complex::

            sage: SC = SimplicialComplex([[0,1,2],[1,2,3]], is_mutable=False)
            sage: SC.stellar_subdivision(F1, inplace=True)
            Traceback (most recent call last):
            ...
            ValueError: this simplicial complex is not mutable
        """
    def graph(self):
        """
        The 1-skeleton of this simplicial complex, as a graph.

        .. WARNING::

           This may give the wrong answer if the simplicial complex
           was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: S = SimplicialComplex([[0,1,2,3]])
            sage: G = S.graph(); G
            Graph on 4 vertices
            sage: G.edges(sort=True)
            [(0, 1, None), (0, 2, None), (0, 3, None), (1, 2, None), (1, 3, None), (2, 3, None)]
        """
    def delta_complex(self, sort_simplices: bool = False):
        """
        Return ``self`` as a `\\Delta`-complex.

        The `\\Delta`-complex is essentially identical to the
        simplicial complex: it has same simplices with the same
        boundaries.

        INPUT:

        - ``sort_simplices`` -- boolean (default: ``False``); if ``True``, sort
          the list of simplices in each dimension

        EXAMPLES::

            sage: T = simplicial_complexes.Torus()
            sage: Td = T.delta_complex()
            sage: Td
            Delta complex with 7 vertices and 43 simplices
            sage: T.homology() == Td.homology()                                         # needs sage.modules
            True
        """
    def is_flag_complex(self):
        """
        Return ``True`` if and only if ``self`` is a flag complex.

        A flag complex is a simplicial complex that is the largest simplicial
        complex on its 1-skeleton. Thus a flag complex is the clique complex
        of its graph.

        EXAMPLES::

            sage: h = Graph({0: [1,2,3,4], 1: [2,3,4], 2: [3]})
            sage: x = h.clique_complex(); x
            Simplicial complex with vertex set (0, 1, 2, 3, 4)
            and facets {(0, 1, 4), (0, 1, 2, 3)}
            sage: x.is_flag_complex()
            True

            sage: X = simplicial_complexes.ChessboardComplex(3,3)
            sage: X.is_flag_complex()
            True
        """
    def n_skeleton(self, n):
        """
        The `n`-skeleton of this simplicial complex.

        The `n`-skeleton of a simplicial complex is obtained by discarding
        all of the simplices in dimensions larger than `n`.

        INPUT:

        - ``n`` -- nonnegative integer

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1], [1,2,3], [0,2,3]])
            sage: X.n_skeleton(1)
            Simplicial complex with vertex set (0, 1, 2, 3) and
             facets {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
            sage: X.set_immutable()
            sage: X.n_skeleton(2)
            Simplicial complex with vertex set (0, 1, 2, 3) and
             facets {(0, 1), (0, 2, 3), (1, 2, 3)}
            sage: X.n_skeleton(4)
            Simplicial complex with vertex set (0, 1, 2, 3) and
             facets {(0, 1), (0, 2, 3), (1, 2, 3)}
        """
    def connected_component(self, simplex=None):
        """
        Return the connected component of this simplicial complex
        containing ``simplex``. If ``simplex`` is omitted, then return
        the connected component containing the zeroth vertex in the
        vertex list. (If the simplicial complex is empty, raise an
        error.)

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S1 == S1.connected_component()
            True
            sage: X = S1.disjoint_union(S1)
            sage: X == X.connected_component()
            False
            sage: CL0 = X.connected_component(Simplex(['L0']))
            sage: CR0 = X.connected_component(Simplex(['R0']))
            sage: CL0 == CR0
            False

            sage: S0 = simplicial_complexes.Sphere(0)
            sage: S0.vertices()
            (0, 1)
            sage: S0.connected_component()
            Simplicial complex with vertex set (0,) and facets {(0,)}
            sage: S0.connected_component(Simplex((1,)))
            Simplicial complex with vertex set (1,) and facets {(1,)}

            sage: SimplicialComplex([[]]).connected_component()
            Traceback (most recent call last):
            ...
            ValueError: the empty simplicial complex has no connected components
        """
    def fundamental_group(self, base_point=None, simplify: bool = True):
        """
        Return the fundamental group of this simplicial complex.

        INPUT:

        - ``base_point`` -- (default: ``None``) if this complex is
          not path-connected, then specify a vertex; the fundamental
          group is computed with that vertex as a base point. If the
          complex is path-connected, then you may specify a vertex or
          leave this as its default setting of ``None``. (If this
          complex is path-connected, then this argument is ignored.)

        - ``simplify`` -- boolean (default: ``True``); then return a
          presentation of the group in terms of generators and
          relations. If ``True``, the default, simplify as much as GAP is
          able to.

        Algorithm: we compute the edge-path group -- see
        :wikipedia:`Fundamental_group`. Choose a spanning tree for the
        1-skeleton, and then the group's generators are given by the
        edges in the 1-skeleton; there are two types of relations:
        `e=1` if `e` is in the spanning tree, and for every 2-simplex,
        if its edges are `e_0`, `e_1`, and `e_2`, then we impose the
        relation `e_0 e_1^{-1} e_2 = 1`.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S1.fundamental_group()                                                # needs sage.groups
            Finitely presented group < e |  >

        If we pass the argument ``simplify=False``, we get generators and
        relations in a form which is not usually very helpful. Here is the
        cyclic group of order 2, for instance::

            sage: RP2 = simplicial_complexes.RealProjectiveSpace(2)
            sage: C2 = RP2.fundamental_group(simplify=False); C2                        # needs sage.groups
            Finitely presented group < e0, e1, e2, e3, e4, e5, e6, e7, e8, e9 | e0, e3,
            e4, e7, e9, e5*e2^-1*e0, e7*e2^-1*e1, e8*e3^-1*e1, e8*e6^-1*e4, e9*e6^-1*e5 >
            sage: C2.simplified()                                                       # needs sage.groups
            Finitely presented group < e1 | e1^2 >

        This is the same answer given if the argument ``simplify`` is True
        (the default)::

            sage: RP2.fundamental_group()                                               # needs sage.groups
            Finitely presented group < e1 | e1^2 >

        You must specify a base point to compute the fundamental group
        of a non-connected complex::

            sage: # needs sage.groups
            sage: K = S1.disjoint_union(RP2)
            sage: K.fundamental_group()
            Traceback (most recent call last):
            ...
            ValueError: this complex is not connected, so you must specify a base point
            sage: K.fundamental_group(base_point='L0')
            Finitely presented group < e |  >
            sage: K.fundamental_group(base_point='R0').order()
            2

        Some other examples::

            sage: S1.wedge(S1).fundamental_group()                                      # needs sage.groups
            Finitely presented group < e0, e1 | >
            sage: simplicial_complexes.Torus().fundamental_group()                      # needs sage.groups
            Finitely presented group < e1, e4 | e4^-1*e1^-1*e4*e1 >

            sage: # needs sage.groups
            sage: G = simplicial_complexes.MooreSpace(5).fundamental_group()
            sage: G.ngens()
            1
            sage: x = G.gen(0)
            sage: [(x**n).is_one() for n in range(1,6)]
            [False, False, False, False, True]
        """
    def is_isomorphic(self, other, certificate: bool = False):
        """
        Check whether two simplicial complexes are isomorphic.

        INPUT:

        - ``certificate`` -- if ``True``, then output is ``(a, b)``, where ``a``
          is a boolean and ``b`` is either a map or ``None``

        This is done by creating two graphs and checking whether they
        are isomorphic.

        EXAMPLES::

            sage: Z1 = SimplicialComplex([[0,1],[1,2],[2,3,4],[4,5]])
            sage: Z2 = SimplicialComplex([['a','b'],['b','c'],['c','d','e'],['e','f']])
            sage: Z3 = SimplicialComplex([[1,2,3]])
            sage: Z1.is_isomorphic(Z2)
            True
            sage: Z1.is_isomorphic(Z2, certificate=True)
            (True, {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'})
            sage: Z3.is_isomorphic(Z2)
            False

        We check that :issue:`20751` is fixed::

            sage: C1 = SimplicialComplex([[1,2,3], [2,4], [3,5], [5,6]])
            sage: C2 = SimplicialComplex([['a','b','c'], ['b','d'], ['c','e'], ['e','f']])
            sage: C1.is_isomorphic(C2, certificate=True)
            (True, {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'})
        """
    def automorphism_group(self):
        """
        Return the automorphism group of the simplicial complex.

        This is done by creating a bipartite graph, whose vertices are
        vertices and facets of the simplicial complex, and computing
        its automorphism group.

        .. WARNING::

            Since :issue:`14319` the domain of the automorphism group is equal to
            the graph's vertex set, and the ``translation`` argument has become
            useless.

        EXAMPLES::

            sage: S = simplicial_complexes.Simplex(3)
            sage: S.automorphism_group().is_isomorphic(SymmetricGroup(4))               # needs sage.groups
            True

            sage: P = simplicial_complexes.RealProjectivePlane()
            sage: P.automorphism_group().is_isomorphic(AlternatingGroup(5))             # needs sage.groups
            True

            sage: Z = SimplicialComplex([['1','2'],['2','3','a']])
            sage: Z.automorphism_group().is_isomorphic(CyclicPermutationGroup(2))       # needs sage.groups
            True
            sage: group = Z.automorphism_group()                                        # needs sage.groups
            sage: sorted(group.domain())                                                # needs sage.groups
            ['1', '2', '3', 'a']

        Check that :issue:`17032` is fixed::

            sage: s = SimplicialComplex([[(0,1),(2,3)]])
            sage: s.automorphism_group().cardinality()                                  # needs sage.groups
            2
        """
    def fixed_complex(self, G):
        """
        Return the fixed simplicial complex `Fix(G)` for a subgroup `G`.

        INPUT:

        - ``G`` -- a subgroup of the automorphism group of the simplicial
          complex or a list of elements of the automorphism group

        OUTPUT:

        - a simplicial complex `Fix(G)`

        Vertices in `Fix(G)` are the orbits of `G` (acting on vertices
        of ``self``) that form a simplex in ``self``. More generally,
        simplices in `Fix(G)` correspond to simplices in ``self`` that
        are union of such orbits.

        A basic example::

            sage: S4 = simplicial_complexes.Sphere(4)
            sage: S3 = simplicial_complexes.Sphere(3)
            sage: fix = S4.fixed_complex([S4.automorphism_group()([(0,1)])]); fix       # needs sage.groups
            Simplicial complex with vertex set (0, 2, 3, 4, 5) and 5 facets
            sage: fix.is_isomorphic(S3)                                                 # needs sage.groups
            True

        Another simple example::

            sage: T = SimplicialComplex([[1,2,3],[2,3,4]])
            sage: G = T.automorphism_group()                                            # needs sage.groups
            sage: T.fixed_complex([G([(1,4)])])                                         # needs sage.groups
            Simplicial complex with vertex set (2, 3) and facets {(2, 3)}

        A more sophisticated example::

            sage: RP2 = simplicial_complexes.ProjectivePlane()
            sage: CP2 = simplicial_complexes.ComplexProjectivePlane()
            sage: G = CP2.automorphism_group()                                          # needs sage.groups
            sage: H = G.subgroup([G([(2,3),(5,6),(8,9)])])                              # needs sage.groups
            sage: CP2.fixed_complex(H).is_isomorphic(RP2)                               # needs sage.groups
            True
        """
    def set_immutable(self) -> None:
        """
        Make this simplicial complex immutable.

        EXAMPLES::

            sage: S = SimplicialComplex([[1,4], [2,4]])
            sage: S.is_mutable()
            True
            sage: S.set_immutable()
            sage: S.is_mutable()
            False
        """
    def is_mutable(self):
        """
        Return ``True`` if mutable.

        EXAMPLES::

            sage: S = SimplicialComplex([[1,4], [2,4]])
            sage: S.is_mutable()
            True
            sage: S.set_immutable()
            sage: S.is_mutable()
            False
            sage: S2 = SimplicialComplex([[1,4], [2,4]], is_mutable=False)
            sage: S2.is_mutable()
            False
            sage: S3 = SimplicialComplex([[1,4], [2,4]], is_mutable=False)
            sage: S3.is_mutable()
            False
        """
    def is_immutable(self):
        """
        Return ``True`` if immutable.

        EXAMPLES::

            sage: S = SimplicialComplex([[1,4], [2,4]])
            sage: S.is_immutable()
            False
            sage: S.set_immutable()
            sage: S.is_immutable()
            True
        """
    def cone_vertices(self):
        """
        Return the list of cone vertices of ``self``.

        A vertex is a cone vertex if and only if it appears in every facet.

        EXAMPLES::

            sage: SimplicialComplex([[1,2,3]]).cone_vertices()
            [1, 2, 3]
            sage: SimplicialComplex([[1,2,3], [1,3,4], [1,5,6]]).cone_vertices()
            [1]
            sage: SimplicialComplex([[1,2,3], [1,3,4], [2,5,6]]).cone_vertices()
            []
        """
    def decone(self):
        """
        Return the subcomplex of ``self`` induced by the non-cone vertices.

        EXAMPLES::

            sage: SimplicialComplex([[1,2,3]]).decone()
            Simplicial complex with vertex set () and facets {()}
            sage: SimplicialComplex([[1,2,3], [1,3,4], [1,5,6]]).decone()
            Simplicial complex with vertex set (2, 3, 4, 5, 6)
             and facets {(2, 3), (3, 4), (5, 6)}
            sage: X = SimplicialComplex([[1,2,3], [1,3,4], [2,5,6]])
            sage: X.decone() == X
            True
        """
    def is_balanced(self, check_purity: bool = False, certificate: bool = False):
        """
        Determine whether ``self`` is balanced.

        A simplicial complex `X` of dimension `d-1` is balanced if and
        only if its vertices can be colored with `d` colors such that
        every face contains at most one vertex of each color.  An
        equivalent condition is that the 1-skeleton of `X` is
        `d`-colorable.  In some contexts, it is also required that `X`
        be pure (i.e., that all maximal faces of `X` have the same
        dimension).

        INPUT:

        - ``check_purity`` -- boolean (default: ``False``); if this is ``True``,
          require that ``self`` be pure as well as balanced

        - ``certificate`` -- boolean (default: ``False``); if this is ``True`` and
          ``self`` is balanced, then return a `d`-coloring of the 1-skeleton

        EXAMPLES:

        A 1-dim simplicial complex is balanced iff it is bipartite::

            sage: X = SimplicialComplex([[1,2], [1,4], [3,4], [2,5]])
            sage: X.is_balanced()
            True
            sage: sorted(X.is_balanced(certificate=True))
            [[1, 3, 5], [2, 4]]
            sage: X = SimplicialComplex([[1,2], [1,4], [3,4], [2,4]])
            sage: X.is_balanced()
            False

        Any barycentric division is balanced::

            sage: X = SimplicialComplex([[1,2,3], [1,2,4], [2,3,4]])
            sage: X.is_balanced()
            False
            sage: X.barycentric_subdivision().is_balanced()
            True

        A non-pure balanced complex::

            sage: X = SimplicialComplex([[1,2,3], [3,4]])
            sage: X.is_balanced(check_purity=True)
            False
            sage: sorted(X.is_balanced(certificate=True))
            [[1, 4], [2], [3]]
        """
    def is_partitionable(self, certificate: bool = False, *, solver=None, integrality_tolerance: float = 0.001):
        """
        Determine whether ``self`` is partitionable.

        A partitioning of a simplicial complex `X` is a decomposition
        of its face poset into disjoint Boolean intervals `[R,F]`,
        where `F` ranges over all facets of `X`.

        The method sets up an integer program with:

        - a variable `y_i` for each pair `(R,F)`, where `F` is a facet of `X`
          and `R` is a subface of `F`

        - a constraint `y_i+y_j \\leq 1` for each pair `(R_i,F_i)`, `(R_j,F_j)`
          whose Boolean intervals intersect nontrivially (equivalent to
          `(R_i\\subseteq F_j and R_j\\subseteq F_i))`

        - objective function equal to the sum of all `y_i`

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          and ``self`` is partitionable, then return a list of pairs `(R,F)`
          that form a partitioning.

        - ``solver`` -- (default: ``None``) specifies a Mixed Integer Linear Programming
          (MILP) solver to be used. If set to ``None``, the default one is used. For
          more information on MILP solvers and which default solver is used, see
          the method
          :meth:`solve <sage.numerical.mip.MixedIntegerLinearProgram.solve>`
          of the class
          :class:`MixedIntegerLinearProgram <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``integrality_tolerance`` -- parameter for use with MILP solvers over an
          inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

        EXAMPLES:

        Simplices are trivially partitionable::

            sage: X = SimplicialComplex([[1,2,3,4]])
            sage: X.is_partitionable()                                                  # needs sage.numerical.mip
            True
            sage: X.is_partitionable(certificate=True)                                  # needs sage.numerical.mip
            [((), (1, 2, 3, 4), 4)]

        Shellable complexes are partitionable::

            sage: # needs sage.numerical.mip, long time
            sage: X = SimplicialComplex([[1,3,5], [1,3,6], [1,4,5], [1,4,6],
            ....:                        [2,3,5], [2,3,6], [2,4,5]])
            sage: X.is_partitionable()
            True
            sage: P = X.is_partitionable(certificate=True)
            sage: def n_intervals_containing(f):
            ....:     return len([RF for RF in P
            ....:                    if RF[0].is_face(f) and f.is_face(RF[1])])
            sage: all(n_intervals_containing(f) == 1
            ....:     for k in X.faces().keys() for f in X.faces()[k])
            True

        A non-shellable, non-Cohen-Macaulay, partitionable example, constructed by Björner::

            sage: X = SimplicialComplex([[1,2,3], [1,2,4], [1,3,4], [2,3,4], [1,5,6]])
            sage: X.is_partitionable()                                                  # needs sage.numerical.mip
            True

        The bowtie complex is not partitionable::

            sage: X = SimplicialComplex([[1,2,3], [1,4,5]])
            sage: X.is_partitionable()                                                  # needs sage.numerical.mip
            False
        """
    def intersection(self, other):
        """
        Calculate the intersection of two simplicial complexes.

        EXAMPLES::

            sage: X = SimplicialComplex([[1,2,3], [1,2,4]])
            sage: Y = SimplicialComplex([[1,2,3], [1,4,5]])
            sage: Z = SimplicialComplex([[1,2,3], [1,4], [2,4]])
            sage: sorted(X.intersection(Y).facets())
            [(1, 2, 3), (1, 4)]
            sage: X.intersection(X) == X
            True
            sage: X.intersection(Z) == X
            False
            sage: X.intersection(Z) == Z
            True
        """
    def bigraded_betti_numbers(self, base_ring=..., verbose: bool = False):
        """
        Return a dictionary of the bigraded Betti numbers of ``self``,
        with keys `(-a, 2b)`.

        INPUT:

        - ``base_ring`` -- (default: ``ZZ``) the base ring used
          when computing homology
        - ``verbose`` -- boolean (default: ``False``); if ``True``, print
          messages during the computation, which indicate in which
          subcomplexes non-trivial homologies appear

        .. NOTE::

            If ``verbose`` is ``True``, then caching is avoided.

        .. SEEALSO::

            See :meth:`bigraded_betti_number` for more information.

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1],[1,2],[1,3],[2,3]])
            sage: Y = SimplicialComplex([[1,2,3],[1,2,4],[3,5],[4,5]])
            sage: sorted(X.bigraded_betti_numbers(base_ring=QQ).items(), reverse=True)
            [((0, 0), 1), ((-1, 6), 1), ((-1, 4), 2), ((-2, 8), 1), ((-2, 6), 1)]
            sage: sorted(Y.bigraded_betti_numbers(verbose=True).items(), reverse=True)
            (-1, 4): Non-trivial homology Z in dimension 0 of the full
            subcomplex generated by a set of vertices (1, 5)
            (-1, 4): Non-trivial homology Z in dimension 0 of the full
            subcomplex generated by a set of vertices (2, 5)
            (-1, 4): Non-trivial homology Z in dimension 0 of the full
            subcomplex generated by a set of vertices (3, 4)
            (-2, 6): Non-trivial homology Z in dimension 0 of the full
            subcomplex generated by a set of vertices (1, 2, 5)
            (-2, 8): Non-trivial homology Z in dimension 1 of the full
            subcomplex generated by a set of vertices (1, 3, 4, 5)
            (-2, 8): Non-trivial homology Z in dimension 1 of the full
            subcomplex generated by a set of vertices (2, 3, 4, 5)
            (-3, 10): Non-trivial homology Z in dimension 1 of the full
            subcomplex generated by a set of vertices (1, 2, 3, 4, 5)
            [((0, 0), 1), ((-1, 4), 3), ((-2, 8), 2), ((-2, 6), 1), ((-3, 10), 1)]

        If we wish to view them in a form of a table, it is
        simple enough to create a function as such::

            sage: def print_table(bbns):
            ....:     max_a = max(-p[0] for p in bbns)
            ....:     max_b = max(p[1] for p in bbns)
            ....:     bbn_table = [[bbns.get((-a,b), 0) for a in range(max_a+1)]
            ....:                                       for b in range(max_b+1)]
            ....:     width = len(str(max(bbns.values()))) + 1
            ....:     print(' '*width, end=' ')
            ....:     for i in range(max_a+1):
            ....:         print(f'{-i:{width}}', end=' ')
            ....:     print()
            ....:     for j in range(len(bbn_table)):
            ....:         print(f'{j:{width}}', end=' ')
            ....:         for r in bbn_table[j]:
            ....:             print(f'{r:{width}}', end=' ')
            ....:         print()
            sage: print_table(X.bigraded_betti_numbers())
                0 -1 -2
             0  1  0  0
             1  0  0  0
             2  0  0  0
             3  0  0  0
             4  0  2  0
             5  0  0  0
             6  0  1  1
             7  0  0  0
             8  0  0  1
        """
    def bigraded_betti_number(self, a, b, base_ring=..., verbose: bool = False):
        """
        Return the bigraded Betti number indexed in the form `(-a, 2b)`.

        Bigraded Betti number with indices `(-a, 2b)` is defined as a
        sum of ranks of `(b-a-1)`-th (co)homologies of full subcomplexes
        with exactly `b` vertices.

        INPUT:

        - ``base_ring`` -- (default: ``ZZ``) the base ring used
          when computing homology
        - ``verbose`` -- boolean (default: ``False``); if ``True``, print
          messages during the computation, which indicate in which
          subcomplexes non-trivial homologies appear

        .. NOTE::

            If ``verbose`` is ``True``, then caching is avoided.

        EXAMPLES::

            sage: # needs sage.modules
            sage: X = SimplicialComplex([[0,1],[1,2],[2,0],[1,3]])
            sage: X.bigraded_betti_number(-1, 4, base_ring=QQ)
            2
            sage: X.bigraded_betti_number(-1, 8)
            0
            sage: X.bigraded_betti_number(-2, 5)
            0
            sage: X.bigraded_betti_number(0, 0)
            1
            sage: sorted(X.bigraded_betti_numbers().items(), reverse=True)
            [((0, 0), 1), ((-1, 6), 1), ((-1, 4), 2), ((-2, 8), 1), ((-2, 6), 1)]
            sage: X.bigraded_betti_number(-1, 4, base_ring=QQ)
            2
            sage: X.bigraded_betti_number(-1, 8)
            0
            sage: Y = SimplicialComplex([[1,2,3],[1,2,4],[3,5],[4,5]])
            sage: Y.bigraded_betti_number(-1, 4, verbose=True)
            Non-trivial homology Z in dimension 0 of the full subcomplex
            generated by a set of vertices (1, 5)
            Non-trivial homology Z in dimension 0 of the full subcomplex
            generated by a set of vertices (2, 5)
            Non-trivial homology Z in dimension 0 of the full subcomplex
            generated by a set of vertices (3, 4)
            3
        """
    def is_golod(self) -> bool:
        """
        Return whether ``self`` is Golod.

        A simplicial complex is Golod if multiplication and all higher
        Massey operations in the associated Tor-algebra are trivial. This
        is done by checking the bigraded Betti numbers.

        EXAMPLES::

            sage: # needs sage.modules
            sage: X = SimplicialComplex([[0,1],[1,2],[2,3],[3,0]])
            sage: Y = SimplicialComplex([[0,1,2],[0,2],[0,4]])
            sage: X.is_golod()
            False
            sage: Y.is_golod()
            True
        """
    def is_minimally_non_golod(self) -> bool:
        """
        Return whether ``self`` is minimally non-Golod.

        If a simplicial complex itself is not Golod, but deleting any vertex
        gives us a full subcomplex that is Golod, then we say that a simplicial
        complex is minimally non-Golod.

        .. SEEALSO::

            See :meth:`is_golod` for more information.

        EXAMPLES::

            sage: # needs sage.modules
            sage: X = SimplicialComplex([[0,1],[1,2],[2,3],[3,0]])
            sage: Y = SimplicialComplex([[1,2,3],[1,2,4],[3,5],[4,5]])
            sage: X.is_golod()
            False
            sage: X.is_minimally_non_golod()
            True
            sage: Y.is_golod()
            False
            sage: Y.is_minimally_non_golod()
            False
        """
    def moment_angle_complex(self):
        """
        Return the moment-angle complex of ``self``.

        A moment-angle complex is a topological space created
        from this simplicial complex, which holds a lot of
        information about the simplicial complex itself.

        .. SEEALSO::

            See :mod:`sage.topology.moment_angle_complex` for
            more information on moment-angle complexes.

        EXAMPLES::

            sage: X = SimplicialComplex([[0,1,2,3], [1,4], [3,2,4]])
            sage: X.moment_angle_complex()
            Moment-angle complex of Simplicial complex with vertex set
            (0, 1, 2, 3, 4) and facets {(1, 4), (2, 3, 4), (0, 1, 2, 3)}
            sage: K = simplicial_complexes.KleinBottle()
            sage: K.moment_angle_complex()
            Moment-angle complex of Simplicial complex with vertex set
            (0, 1, 2, 3, 4, 5, 6, 7) and 16 facets

        We can also create it explicitly::

            sage: Z = MomentAngleComplex(K); Z
            Moment-angle complex of Simplicial complex with vertex set
            (0, 1, 2, 3, 4, 5, 6, 7) and 16 facets
        """

def facets_for_RP4():
    """
    Return the list of facets for a minimal triangulation of 4-dimensional
    real projective space.

    We use vertices numbered 1 through 16, define two facets, and define
    a certain subgroup `G` of the symmetric group `S_{16}`. Then the set
    of all facets is the `G`-orbit of the two given facets.

    See the description in Example 3.12 in Datta [Dat2007]_.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex import facets_for_RP4
        sage: A = facets_for_RP4()   # long time (1 or 2 seconds)
        sage: SimplicialComplex(A) == simplicial_complexes.RealProjectiveSpace(4) # long time
        True
    """
def facets_for_K3():
    """
    Return the facets for a minimal triangulation of the K3 surface.

    This is a pure simplicial complex of dimension 4 with 16
    vertices and 288 facets. The facets are obtained by constructing a
    few facets and a permutation group `G`, and then computing the
    `G`-orbit of those facets.

    See Casella and Kühnel in [CK2001]_ and Spreer and Kühnel [SK2011]_;
    the construction here uses the labeling from Spreer and Kühnel.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex import facets_for_K3
        sage: A = facets_for_K3()   # long time (a few seconds)
        sage: SimplicialComplex(A) == simplicial_complexes.K3Surface()  # long time
        True
    """
