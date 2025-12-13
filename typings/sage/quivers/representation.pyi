from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.modules.module import Module as Module
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.factory import UniqueFactory as UniqueFactory

class QuiverRepFactory(UniqueFactory):
    """
    A quiver representation is a diagram in the category of vector spaces whose
    underlying graph is the quiver.  Giving a finite dimensional representation
    is equivalent to giving a finite dimensional right module for the path
    algebra of the quiver.

    INPUT:

    The first two arguments specify the base ring and the quiver,
    and they are always required:

    - ``k`` -- ring, the base ring of the representation

    - ``P`` -- the partial semigroup formed by the paths of the quiver of the
      representation

    Then to specify the spaces and maps associated to the quiver
    there are three possible options.  The first is the ``'values'`` option,
    where the next two arguments give the data to be assigned.  The following
    can either be the next two entries in the argument list or they can be
    passed by keyword.  If the argument list is long enough the keywords
    are ignored; the keywords are only checked in the event that the argument
    list does not have enough entries after ``P``.

    - ``spaces`` -- dictionary (default: empty) associating to each vertex a
      free module over the base ring `k`.  Not all vertices must be specified;
      unspecified vertices are automatically set to `k^0`.  Keys of the
      dictionary  that don't correspond to vertices are ignored.

    - ``maps`` -- dictionary (default: empty) associating to each edge a map
      whose domain and codomain are the spaces associated to the initial and
      terminal vertex of the edge respectively.  Not all edges must be
      specified; unspecified edges are automatically set to the zero map. Keys
      of the dictionary that don't correspond to edges are ignored.

    The second option is the ``paths`` option which creates a module by
    generating a right ideal from a list of paths.  Thus the basis elements
    of this module correspond to paths of the quiver and the maps are given
    by right multiplication by the corresponding edge.  As above this can be
    passed either as the next entry in the argument list or as a keyword.
    The keyword is only checked if there is no entry in the argument list
    after ``Q``.

    - ``basis`` -- list; a nonempty list of paths in the quiver ``Q``.
      Entries that do not represent valid paths are ignored and duplicate
      paths are deleted.  There must be at least one valid path in the list
      or a :exc:`ValueError` is raised.  The closure of this list under right
      multiplication forms the basis of the resulting representation.

    The third option is the ``dual paths`` option which creates the dual of
    a left ideal in the quiver algebra.  Thus the basis elements of this
    module correspond to paths of the quiver and the maps are given by
    deleting the corresponding edge from the start of the path (the edge map
    is zero on a path if that edge is not the initial edge of the path).
    As above this can be passed either as the next entry in the argument
    list or as a keyword.

    - ``basis`` -- list; a nonempty list of paths in the quiver ``Q``.
      Entries that do not represent valid paths are ignored and duplicate
      paths are deleted.  There must be at least one valid path in the list
      or a :exc:`ValueError` is raised.  The closure of this list under left
      multiplication of edges forms the basis of  the resulting representation.

    Using the second and third options requires that the following keyword be
    passed to the constructor.  This must be passed as a keyword.

    - ``option`` -- string (default: ``None``); either ``'values'`` or
      ``'paths'`` or ``'dual paths'``. ``None`` is equivalent to ``'values'``

    OUTPUT: :class:`QuiverRep`

    EXAMPLES::

        sage: Q1 = DiGraph({1:{2:['a']}}).path_semigroup()

    When the ``option`` keyword is not supplied the constructor uses the
    ``'values'`` option and expects the spaces and maps to be specified.
    If no maps or spaces are given the zero module is created::

        sage: M = Q1.representation(GF(5))
        sage: M.is_zero()
        True

    The simple modules, indecomposable projectives, and indecomposable
    injectives are examples of quiver representations::

        sage: S = Q1.S(GF(3), 1)
        sage: I = Q1.I(QQ, 2)
        sage: P = Q1.P(GF(3), 1)

    Various standard submodules can be computed, such as radicals and socles.
    We can also form quotients and test for certain attributes such as
    semisimplicity::

        sage: R = P.radical()
        sage: R.is_zero()
        False
        sage: (P/R).is_simple()
        True
        sage: P == R
        False

    With the option ``'paths'`` the input data should be a list of
    :class:`QuiverPaths` or things that :class:`QuiverPaths` can be
    constructed from.  The resulting module is the submodule generated by
    these paths in the quiver algebra, when considered as a right module
    over itself::

        sage: P1 = Q1.representation(QQ, [[(1, 1)]], option='paths')
        sage: P1.dimension()
        2

    In the following example, the 3rd and 4th paths are actually the same,
    so the duplicate is removed::

        sage: N = Q1.representation(QQ, [[(1, 1)], [(2, 2)], [(1, 2, 'a')],
        ....:                           [(1, 2, 'a')]], option='paths')
        sage: N.dimension()
        3

    The dimension at each vertex equals the number of paths in the closed
    basis whose terminal point is that vertex::

        sage: Q2 = DiGraph({1:{2:['a'], 3:['b', 'c']}, 2:{3:['d']}}).path_semigroup()
        sage: M = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a')]], option='paths')
        sage: M.dimension_vector()
        (0, 2, 2)
        sage: N = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a'), (2, 3, 'd')]], option='paths')
        sage: N.dimension_vector()
        (0, 1, 2)
    """
    def create_key(self, k, P, *args, **kwds):
        """
        Return a key for the specified module.

        The key is a tuple.  The first and second entries are the base ring
        ``k`` and the partial semigroup ``P`` formed by the paths of a quiver.
        The third entry is the ``option`` and the remaining entries depend on
        that option.  If the option is ``'values'`` and the quiver
        has `n` vertices then the next `n` entries are the vector spaces
        to be assigned to those vertices.  After that are the matrices of
        the maps assigned to edges, listed in the same order that
        ``Q.edges(sort=True)`` uses.  If the option is ``'paths'`` or ``'dual paths'``
        then the next entry is a tuple containing a sorted list of the
        paths that form a basis of the quiver.

        INPUT:

        See the class documentation.

        OUTPUT: tuple

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: from sage.quivers.representation import QuiverRep
            sage: QuiverRep.create_key(GF(5), P)
            (Finite Field of size 5,
             Partial semigroup formed by the directed paths of Multi-digraph on 2 vertices,
             'values',
             Vector space of dimension 0 over Finite Field of size 5,
             Vector space of dimension 0 over Finite Field of size 5,
             [])
        """
    def create_object(self, version, key, **extra_args):
        """
        Create a :class:`QuiverRep_generic` or
        :class:`QuiverRep_with_path_basis` object from the key.

        The key is a tuple.  The first and second entries are the base ring
        ``k`` and the quiver ``Q``.  The third entry is the
        ``'option'`` and the remaining entries depend on that option.
        If the option is ``'values'`` and the quiver has `n`
        vertices then the next `n` entries are the vector spaces to be
        assigned to those vertices.  After that are the matrices
        of the maps assigned to edges, listed in the same order that
        ``Q.edges(sort=True)`` uses.  If the option is ``'paths'`` or ``'dual paths'``
        then the next entry is a tuple containing a sorted list of the
        paths that form a basis of the quiver.

        INPUT:

        - ``version`` -- the version of sage, this is currently ignored
        - ``key`` -- tuple

        OUTPUT: :class:`QuiverRep_generic` or :class:`QuiverRep_with_path_basis`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: from sage.quivers.representation import QuiverRep
            sage: key = QuiverRep.create_key(GF(5), Q)
            sage: QuiverRep.create_object(0, key)
            Representation with dimension vector (0, 0)
        """

QuiverRep: Incomplete

class QuiverRepElement(ModuleElement):
    """
    An element of a quiver representation is a choice of element from each
    of the spaces assigned to the vertices of the quiver.  Addition,
    subtraction, and scalar multiplication of these elements is done
    pointwise within these spaces.

    INPUT:

    - ``module`` -- :class:`QuiverRep` (default: ``None``); the module to
      which the element belongs

    - ``elements`` -- dictionary (default: empty) associating to each vertex a
      vector or an object from which sage can create a vector. Not all vertices
      must be specified, unspecified vertices will be assigned the zero vector
      of the space associated to that vertex in the given module.  Keys that do
      not correspond to a vertex are ignored.

    - ``name`` -- string (default: ``None``); the name of the element

    OUTPUT: :class:`QuiverRepElement`

    .. NOTE::

        The constructor needs to know the quiver in order to create an
        element of a representation over that quiver.  The default is to
        read this information from ``module`` as well as to fill in
        unspecified vectors with the zeros of the spaces in ``module``.
        If ``module`` is ``None`` then ``quiver`` *MUST* be a quiver and each
        vertex *MUST* be specified or an error will result.  If both
        ``module`` and ``quiver`` are given then ``quiver`` is ignored.

    EXAMPLES::

        sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
        sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
        sage: M = Q.representation(GF(3), spaces)
        sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
        sage: M(elems)
        Element of quiver representation
        sage: v = M(elems, 'v')
        sage: v
        v
        sage: (v + v + v).is_zero()
        True
    """
    def __init__(self, parent, elements=None, name=None) -> None:
        """
        Initialize ``self``. Type ``QuiverRepElement?`` for more information.

        TESTS::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
            sage: v = M(elems, 'v')
            sage: TestSuite(v).run()
        """
    def __mul__(self, other):
        """
        Implement ``*`` for right multiplication by quiver algebra elements.

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: A = Q.algebra(QQ)
            sage: m = P.an_element()
            sage: a = A('a')
            sage: e1 = A([(1, 1)])
            sage: m.support()
            [1, 2]
            sage: (m*a).support()
            [2]
            sage: (m*e1).support()
            [1]
            sage: (m*(a + e1)).support()
            [1, 2]
        """
    @cached_method
    def __hash__(self):
        """
        The hash only depends on the elements assigned to each vertex of the
        underlying quiver.

        .. NOTE::

            The default hash inherited from
            :class:`~sage.structure.element.Element` would depend on
            the name of the element and would thus be mutable.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{4:['c']}, 3:{4:['d']}}).path_semigroup()
            sage: P = Q.P(QQ, 2)
            sage: v = P()   # let's not muddy P.zero(), which is cached
            sage: h1 = hash(v)
            sage: v.rename('foobar')
            sage: h1 == hash(v)
            True
        """
    def __eq__(self, other):
        """
        This overrides the ``==`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
            sage: v = M(elems)
            sage: w = M(elems)
            sage: v == w
            True
            sage: v += w
            sage: v == w
            False
        """
    def __ne__(self, other):
        """
        This overrides the ``!=`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
            sage: v = M(elems)
            sage: w = M(elems)
            sage: v != w
            False
            sage: v += w
            sage: v != w
            True
        """
    def quiver(self):
        """
        Return the quiver of the representation.

        OUTPUT: :class:`DiGraph`, the quiver of the representation

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: v = P.an_element()
            sage: v.quiver() is Q.quiver()
            True
        """
    def get_element(self, vertex):
        """
        Return the element at the given vertex.

        INPUT:

        - ``vertex`` -- integer; a vertex of the quiver

        OUTPUT: the vector assigned to the given vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
            sage: v = M(elems)
            sage: v.get_element(1)
            (1, 0)
            sage: v.get_element(3)
            (2, 1)
        """
    def is_zero(self) -> bool:
        """
        Test whether ``self`` is zero.

        OUTPUT: boolean, ``True`` if the element is the zero element, ``False``
        otherwise

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
            sage: v = M(elems)
            sage: v.is_zero()
            False
            sage: w = M()
            sage: w.is_zero()
            True

        TESTS::

            sage: M = Q.P(QQ, 1)
            sage: M.zero().is_zero()
            True
        """
    def support(self):
        """
        Return the support of ``self`` as a list.

        The support is the set of vertices to which a nonzero vector is
        associated.

        OUTPUT: list; the support

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 0), 3: (2, 1)}
            sage: v = M(elems)
            sage: v.support()
            [1, 3]
        """
    def copy(self):
        """
        Return a copy of ``self``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = dict((v, GF(3)^2) for v in Q.quiver())
            sage: M = Q.representation(GF(3), spaces)
            sage: elems = {1: (1, 0), 2: (0, 1), 3: (2, 1)}
            sage: v = M(elems)
            sage: w = v.copy()
            sage: w._set_element((0, 0), 1)
            sage: w.get_element(1)
            (0, 0)
            sage: v.get_element(1)
            (1, 0)
        """

class QuiverRep_generic(WithEqualityById, Module):
    """
    A generic quiver representation.

    This class should not be called by the user.

    Call :class:`QuiverRep` with ``option='values'`` (which is the default)
    instead.

    INPUT:

    - ``k`` -- ring, the base ring of the representation

    - ``P`` -- the path semigroup of the quiver `Q` of the representation

    - ``spaces`` -- dictionary (default: empty) associating to each vertex a
      free module over the base ring `k`.  Not all vertices need to be
      specified, unspecified vertices are automatically set to `k^0`.  Keys of
      the dictionary that don't correspond to vertices are ignored.

    - ``maps`` -- dictionary (default: empty) associating to each edge a map
      whose domain and codomain are the spaces associated to the initial and
      terminal vertex of the edge respectively.  Not all edges need to be
      specified, unspecified edges are automatically set to the zero map.  Keys
      of the dictionary that don't correspond to edges are ignored.

    OUTPUT: :class:`QuiverRep`

    EXAMPLES::

        sage: Q = DiGraph({1:{3:['a']}, 2:{3:['b']}}).path_semigroup()
        sage: spaces = {1: QQ^2, 2: QQ^3, 3: QQ^2}
        sage: maps = {(1, 3, 'a'): (QQ^2).Hom(QQ^2).identity(), (2, 3, 'b'): [[1, 0], [0, 0], [0, 0]]}
        sage: M = Q.representation(QQ, spaces, maps)

    ::

        sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
        sage: P = Q.P(GF(3), 1)
        sage: I = Q.I(QQ, 1)
        sage: P.an_element() in P
        True
        sage: I.an_element() in P
        False

    TESTS::

        sage: TestSuite(M).run()
        sage: TestSuite(P).run()
        sage: TestSuite(I).run()
        sage: TestSuite(Q.S(ZZ,2)).run()
    """
    Element = QuiverRepElement
    def __init__(self, k, P, spaces, maps) -> None:
        """
        Initialize ``self``. Type ``QuiverRep?`` for more information.

        .. NOTE::

            Use :meth:`~sage.quivers.quiver.Quiver.representation` to create a
            representation. The following is just a test, but it is not the
            recommended way of creating a representation.

        TESTS::

            sage: from sage.quivers.representation import QuiverRep_generic
            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: QuiverRep_generic(GF(5), Q, {1: GF(5)^2, 2: GF(5)^3}, {})
            Representation with dimension vector (2, 3)
        """
    def __truediv__(self, sub):
        """
        Overload the ``/`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: P = Q.P(GF(3), 1)
            sage: R = P.radical()
            sage: (P/R).is_simple()
            True
        """
    def get_space(self, vertex):
        """
        Return the module associated to the given vertex ``vertex``.

        INPUT:

        - ``vertex`` -- integer; a vertex of the quiver of the module

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}}).path_semigroup()
            sage: Q.P(QQ, 1).get_space(1)
            Vector space of dimension 1 over Rational Field
        """
    def get_map(self, edge):
        """
        Return the map associated to the given edge ``edge``.

        INPUT:

        - ``edge`` -- tuple of the form
          (initial vertex, terminal vertex, label) specifying the edge
          whose map is returned

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: Q.P(ZZ, 1).get_map((1, 2, 'a'))
            Free module morphism defined by the matrix
            [1 0]
            Domain: Ambient free module of rank 1 over the principal ideal domain Integer Ring
            Codomain: Ambient free module of rank 2 over the principal ideal domain Integer Ring
        """
    def quiver(self):
        """
        Return the quiver of the representation.

        OUTPUT: :class:`DiGraph`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: M = Q.representation(GF(5))
            sage: M.quiver() is Q.quiver()
            True
        """
    def actor(self):
        """
        Return the quiver path algebra acting on this representation.

        OUTPUT: a quiver path algebra

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: M = Q.representation(GF(5))
            sage: M.base_ring()
            Finite Field of size 5
            sage: M.actor()
            Path algebra of Multi-digraph on 2 vertices over Finite Field of size 5
        """
    def dimension(self, vertex=None):
        """
        Return the dimension of the space associated to the given vertex
        ``vertex``.

        INPUT:

        - ``vertex`` -- integer or ``None`` (default: ``None``), the given
          vertex

        OUTPUT:

        - integer, the dimension over the base ring of the space
          associated to the given vertex.  If ``vertex=None`` then the
          dimension over the base ring of the module is returned

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: P = Q.P(GF(2), 1)
            sage: P.dimension(1)
            1
            sage: P.dimension(2)
            2

        The total dimension of the module is the sum of the dimensions
        at each vertex::

            sage: P.dimension()
            3
        """
    def dimension_vector(self):
        """
        Return the dimension vector of the representation.

        OUTPUT: tuple

        .. NOTE::

            The order of the entries in the tuple matches the order given
            by calling the ``vertices()`` method on the quiver.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: P = Q.P(GF(2), 1)
            sage: P.dimension_vector()
            (1, 2)

        Each coordinate of the dimension vector is the dimension of the space
        associated to that coordinate::

            sage: P.get_space(2).dimension()
            2
        """
    def is_zero(self) -> bool:
        """
        Test whether the representation is zero.

        OUTPUT: boolean

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.representation(ZZ)
            sage: N = Q.representation(ZZ, {1: 1})
            sage: M
            Representation with dimension vector (0, 0)
            sage: N
            Representation with dimension vector (1, 0)
            sage: M.is_zero()
            True
            sage: N.is_zero()
            False
        """
    def is_simple(self) -> bool:
        """
        Test whether the representation is simple.

        OUTPUT: boolean

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: Q.P(RR, 1).is_simple()
            False
            sage: Q.S(RR, 1).is_simple()
            True
        """
    def is_semisimple(self) -> bool:
        """
        Test whether the representation is semisimple.

        OUTPUT: boolean

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: (M/M.radical()).is_semisimple()
            True
        """
    def an_element(self):
        """
        Return an element of ``self``.

        OUTPUT: :class:`QuiverRepElement`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.an_element()
            Element of quiver representation
        """
    def support(self):
        """
        Return the support of ``self`` as a list.

        OUTPUT:

        - list, the vertices of the representation that have nonzero
          spaces associated to them

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 3:{2:['b'], 4:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 3)
            sage: M
            Representation with dimension vector (0, 1, 1, 1)
            sage: M.support()
            [2, 3, 4]
        """
    def gens(self, names: str = 'v') -> tuple:
        '''
        Return a tuple of generators of ``self`` as a `k`-module.

        INPUT:

        - ``names`` -- an iterable variable of length equal to the number
          of generators, or a string (default: ``\'v\'``); gives the names of
          the generators either by giving a name to each generator or by
          giving a name to which an index will be appended

        OUTPUT:

        - tuple of :class:`QuiverRepElement` objects, the linear generators
          of the module (over the base ring)

        .. NOTE::

            The generators are ordered first by vertex and then by the order
            given by the ``gens()`` method of the space associated to
            that vertex.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:[\'a\', \'b\']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.gens()
            (v_0, v_1, v_2)

        If a string is given then it is used as the name of each generator,
        with the index of the generator appended in order to differentiate
        them::

            sage: M.gens(\'generator\')
            (generator_0, generator_1, generator_2)

        If a list or other iterable variable is given then each generator
        is named using the appropriate entry.  The length of the variable
        must equal the number of generators (the dimension of the module)::

            sage: M.gens([\'w\', \'x\', \'y\', \'z\'])
            Traceback (most recent call last):
            ...
            TypeError: can only concatenate list (not "str") to list
            sage: M.gens([\'x\', \'y\', \'z\'])
            (x, y, z)

        Strings are iterable, so if the length of the string is equal to the
        number of generators then the characters of the string will be used
        as the names::

            sage: M.gens(\'xyz\')
            (x, y, z)
        '''
    def coordinates(self, vector):
        """
        Return the coordinates when ``vector`` is expressed in terms of
        the gens.

        INPUT:

        - ``vector`` -- :class:`QuiverRepElement`

        OUTPUT:

        - list, the coefficients when the vector is expressed as a linear
          combination of the generators of the module

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: x, y, z = M.gens('xyz')
            sage: M.coordinates(x - y + z)
            [1, -1, 1]
            sage: M.coordinates(M.an_element())
            [1, 1, 0]
            sage: M.an_element() == x + y
            True
        """
    def linear_combination_of_basis(self, coordinates):
        """
        Return the linear combination of the basis for ``self`` given
        by ``coordinates``.

        INPUT:

        - ``coordinates`` -- list; a list whose length is the dimension of
          ``self``.  The `i`-th element of this list defines the
          coefficient of the `i`-th basis vector in the linear
          combination.

        OUTPUT: :class:`QuiverRepElement`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: x, y, z = M.gens('xyz')
            sage: e = x - y + z
            sage: M.coordinates(e)
            [1, -1, 1]
            sage: M.linear_combination_of_basis([1, -1, 1]) == e
            True
        """
    def submodule(self, elements=[], spaces=None):
        """
        Return the submodule generated by the data.

        INPUT:

        - ``elements`` -- a collection of QuiverRepElements (default:
          empty list), each should be an element of ``self``

        - ``spaces`` -- dictionary (default: empty); should contain entries of
          the form ``{v: S}`` where `v` is a vertex of the quiver and `S` is a
          subspace of the vector space associated to `v`

        OUTPUT:

        - :class:`QuiverRep`, the smallest subrepresentation of ``self``
          containing the given elements and the given subspaces

        .. NOTE::

            This function returns only a :class:`QuiverRep` object ``sub``.
            The inclusion map of ``sub`` into ``M = self`` can be obtained
            by calling ``M.coerce_map_from(sub)``.

        EXAMPLES::

            sage: Q = DiGraph({1:{3:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^3, 3: QQ^2}
            sage: maps = {(1, 3, 'a'): (QQ^2).Hom(QQ^2).identity(), (2, 3, 'b'): [[1, 0], [0, 0], [0, 0]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: v = M.an_element()
            sage: M.submodule([v])
            Representation with dimension vector (1, 1, 1)

        The smallest submodule containing the vector space at vertex 1
        also contains the entire vector space associated to vertex 3
        because there is an isomorphism associated to the edge
        ``(1, 3, 'a')``::

            sage: M.submodule(spaces={1: QQ^2})
            Representation with dimension vector (2, 0, 2)

        The smallest submodule containing the vector space at vertex 2
        also contains the image of the rank 1 homomorphism associated to
        the edge ``(2, 3, 'b')``::

            sage: M.submodule(spaces={2: QQ^3})
            Representation with dimension vector (0, 3, 1)

        As ``v`` is not already contained in this submodule, adding it as
        a generator yields a larger submodule::

            sage: v.support()
            [1, 2, 3]
            sage: M.submodule([v], {2: QQ^3})
            Representation with dimension vector (1, 3, 1)

        Giving no generating data yields the zero submodule::

            sage: M.submodule().is_zero()
            True

        If the given data generates all of M then the result is M::

            sage: M.submodule(M.gens()) is M
            True
        """
    def quotient(self, sub, check: bool = True):
        """
        Return the quotient of ``self`` by the submodule ``sub``.

        INPUT:

        - ``sub`` -- :class:`QuiverRep`; this must be a submodule of ``self``,
          meaning the space associated to each vertex `v` of ``sub`` is a
          subspace of the space associated to `v` in ``self`` and the map
          associated to each edge `e` of ``sub`` is the restriction of
          the map associated to `e` in ``self``

        - ``check`` -- boolean; if ``True`` then ``sub`` is checked to verify
          that it is indeed a submodule of ``self`` and an error is raised
          if it is not

        OUTPUT: :class:`QuiverRep`, the quotient module ``self / sub``

        .. NOTE::

            This function returns only a QuiverRep object ``quot``.  The
            projection map from ``self`` to ``quot`` can be obtained by
            calling ``quot.coerce_map_from(self)``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.I(GF(3), 3)
            sage: N = Q.S(GF(3), 3)
            sage: M.quotient(N)
            Representation with dimension vector (2, 1, 0)
            sage: M.quotient(M.radical())
            Representation with dimension vector (2, 0, 0)
            sage: M.quotient(M)
            Representation with dimension vector (0, 0, 0)
        """
    def socle(self):
        """
        The socle of ``self``.

        OUTPUT: :class:`QuiverRep`; the socle

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.socle()
            Representation with dimension vector (0, 0, 2)
        """
    def radical(self):
        """
        Return the Jacobson radical of ``self``.

        OUTPUT: :class:`QuiverRep`; the Jacobson radical

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.radical()
            Representation with dimension vector (0, 2, 2)
        """
    def top(self):
        """
        Return the top of ``self``.

        OUTPUT: :class:`QuiverRep`; the quotient of ``self`` by its radical

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.top()
            Representation with dimension vector (1, 0, 0)
            sage: M.top() == M/M.radical()
            True
        """
    def zero_submodule(self):
        """
        Return the zero submodule of ``self``.

        OUTPUT: :class:`QuiverRep`; the zero submodule of ``self``

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.zero_submodule()
            Representation with dimension vector (0, 0, 0)
            sage: M.zero_submodule().is_zero()
            True
        """
    def linear_dual(self):
        """
        Compute the linear dual `Hom_k(M, k)` of the module
        `M =` ``self`` over the base ring `k`.

        OUTPUT: :class:`QuiverRep`; the dual representation

        .. NOTE::

            If `e` is an edge of the quiver `Q` then we let
            `(fe)(m) = f(me)`.  This gives `Hom_k(M, k)` a module
            structure over the opposite quiver ``Q.reverse()``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: M.linear_dual()
            Representation with dimension vector (1, 2, 2)
            sage: M.linear_dual().quiver() is Q.reverse().quiver()
            True
        """
    def algebraic_dual(self, basis: bool = False):
        """
        Compute the algebraic dual `Hom_Q(M, kQ)` of the module
        `M` = ``self``.

        INPUT:

        - ``basis`` -- boolean; if ``False``, then only the module is
          returned.  If ``True``, then a tuple is returned.  The first
          element is the :class:`QuiverRep` and the second element is a
          dictionary which associates to each vertex a list.  The elements
          of this list are the homomorphisms which correspond to the basis
          elements of that vertex in the module.

        OUTPUT: :class:`QuiverRep` or tuple

        .. NOTE::

            Here `kQ` is the path algebra considered as a right module
            over itself.  If `e` is an edge of the quiver `Q` then we let
            `(fe)(m) = ef(m)`.  This gives `Hom_Q(M, kQ)` a module
            structure over the opposite quiver ``Q.reverse()``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b'], 3: ['c', 'd']}, 2:{3:['e']}}).path_semigroup()
            sage: Q.free_module(GF(7)).algebraic_dual().dimension_vector()
            (7, 2, 1)
        """
    def Hom(self, codomain):
        """
        Return the hom space from ``self`` to ``codomain``.

        For more information see the :class:`QuiverHomSpace` documentation.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: Q.S(QQ, 2).Hom(Q.P(QQ, 1))
            Dimension 2 QuiverHomSpace
        """
    def direct_sum(self, modules, return_maps: bool = False):
        """
        Return the direct sum of ``self`` with the given modules
        ``modules``.

        The modules must be modules over the same quiver and base ring.

        INPUT:

        - ``modules`` -- :class:`QuiverRep` or list of :class:`QuiverRep`'s

        - ``return_maps`` -- boolean (default: ``False``); if ``False``, then
          the output is a single QuiverRep object which is the direct sum
          of ``self`` with the given module or modules.  If ``True``, then
          the output is a list ``[sum, iota, pi]``.  The first entry
          ``sum`` is the direct sum of ``self`` with the given module or
          modules.  Both ``iota`` and ``pi`` are lists of QuiverRepHoms
          with one entry for each summand; ``iota[i]`` is the inclusion
          map and ``pi[i]`` is the projection map of the `i`-th summand.
          The summands are ordered as given with ``self`` being the zeroth
          summand.

        OUTPUT: :class:`QuiverRep` or tuple

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b']}, 2:{4:['c']}, 3:{4:['d']}}).path_semigroup()
            sage: P1 = Q.P(QQ, 1)
            sage: P2 = Q.P(QQ, 2)
            sage: S = P1.direct_sum(P2)
            sage: P1.dimension_vector()
            (1, 1, 1, 2)
            sage: P2.dimension_vector()
            (0, 1, 0, 1)
            sage: S.dimension_vector()
            (1, 2, 1, 3)
            sage: S, iota, pi = P1.direct_sum(P2, return_maps=True)
            sage: iota[0].domain() is P1
            True
            sage: iota[1].domain() is P2
            True
            sage: pi[0].codomain() is P1
            True
            sage: pi[1].codomain() is P2
            True
            sage: iota[0].codomain() is S
            True
            sage: iota[1].codomain() is S
            True
            sage: pi[0].domain() is S
            True
            sage: pi[1].domain() is S
            True
            sage: iota[0].get_matrix(4)
            [1 0 0]
            [0 1 0]
            sage: pi[0].get_matrix(4)
            [1 0]
            [0 1]
            [0 0]
            sage: P1prime = S/iota[1].image()
            sage: f = P1prime.coerce_map_from(S)
            sage: g = f*iota[0]
            sage: g.is_isomorphism()
            True
        """
    def projective_cover(self, return_maps: bool = False):
        """
        Return the projective cover of ``self``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c','d']}}).path_semigroup()
            sage: S1 = Q.S(GF(3), 1)
            sage: f1 = S1.projective_cover()
            sage: f1.is_surjective()
            True
            sage: f1._domain
            Representation with dimension vector (1, 2, 4)
            sage: Q.P(GF(3), 1)
            Representation with dimension vector (1, 2, 4)
        """
    def transpose(self):
        """
        Return the transpose of ``self``.

        The transpose, `\\mbox{Tr} M`, of a module `M` is defined as
        follows.  Let `p: P_1 \\to P_2` be the second map in a minimal
        projective presentation `P_1 \\to P_2 \\to M \\to 0` of `M`.
        If `p^t` is the algebraic dual of `p` then define
        `\\mbox{Tr} M = \\mbox{coker} p^t`.

        OUTPUT: :class:`QuiverRep`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.representation(GF(3), {1: 1, 2: 1}, {(1, 2, 'a'): 1})
            sage: M.transpose()
            Representation with dimension vector (1, 1)
        """
    def AR_translate(self):
        """
        Return the Auslander-Reiten translate of ``self``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: M = Q.representation(GF(3), {1: 1, 2: 1}, {(1, 2, 'a'): 1})
            sage: tauM = M.AR_translate()
            sage: tauM
            Representation with dimension vector (1, 1)
            sage: tauM.get_map((1, 2, 'a')).matrix()
            [1]
            sage: tauM.get_map((1, 2, 'b')).matrix()
            [0]

        The module ``M`` above is its own AR translate.  This is not
        always true::

            sage: Q2 = DiGraph({3:{1:['b']}, 5:{3:['a']}}).path_semigroup()
            sage: Q2.S(QQ, 5).AR_translate()
            Representation with dimension vector (0, 1, 0)
        """
    def right_edge_action(self, element, path):
        """
        Return the result of ``element*path``.

        INPUT:

        - ``element`` -- :class:`QuiverRepElement`, an element of ``self``

        - ``path`` -- :class:`QuiverPath` or list of tuples

        OUTPUT:

        - :class:`QuiverRepElement`, the result of ``element*path`` when
          ``path`` is considered an element of the path algebra of the quiver

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: v = M.an_element()
            sage: v.support()
            [1, 2, 3]
            sage: M.right_edge_action(v, [(1, 1)]).support()
            [1]
            sage: M.right_edge_action(v, [(1, 1)]).support()
            [1]
            sage: M.right_edge_action(v, [(1, 2, 'a')]).support()
            [2]
            sage: M.right_edge_action(v, 'a') == M.right_edge_action(v, [(1, 2, 'a')])
            True
        """

class QuiverRep_with_path_basis(QuiverRep_generic):
    """
    The basis of the module must be closed under right multiplication by
    an edge; that is, appending any edge to the end of any path in the
    basis must result in either an invalid path or a valid path also
    contained in the basis of the module.

    INPUT:

    - ``k`` -- ring, the base ring of the representation

    - ``P`` -- the path semigroup of the quiver `Q` of the representation

    - ``basis`` -- list (default: empty); should be a list of paths (also
      lists) in the quiver `Q`.  Entries that do not represent valid paths
      are ignored and duplicate paths are deleted.  The closure of this
      list under right multiplication forms the basis of the resulting
      representation.
    """
    left_edge_action: Incomplete
    def __init__(self, k, P, basis) -> None:
        """
        Initialize ``self``. Type ``QuiverRep_with_path_basis?`` for more
        information.

        TESTS::

            sage: Q1 = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: P1 = Q1.representation(QQ, [[(1, 1)]], option='paths')
            sage: P1.dimension()
            2
            sage: kQ = Q1.representation(QQ, [[(1, 1)], [(2, 2)], [(1, 2, 'a')], [(1, 2, 'a')]], option='paths')
            sage: kQ.dimension()
            3
            sage: Q2 = DiGraph({1:{2:['a'], 3:['b', 'c']}, 2:{3:['d']}}).path_semigroup()
            sage: M = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a')]], option='paths')
            sage: M.dimension_vector()
            (0, 2, 2)
            sage: N = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a'), (2, 3, 'd')]], option='paths')
            sage: N.dimension_vector()
            (0, 1, 2)
            sage: TestSuite(M).run()
        """
    def is_left_module(self) -> bool:
        """
        Test whether the basis is closed under left multiplication.

        EXAMPLES::

            sage: Q1 = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: P2 = Q1.representation(QQ, [[(2, 2)]], option='paths')
            sage: P2.is_left_module()
            False

        The supplied basis is not closed under left multiplication, but it's
        not closed under right multiplication either.  When the closure under
        right multiplication is taken the result is also closed under left
        multiplication and therefore produces a left module structure::

            sage: kQ = Q1.representation(QQ, [[(1, 1)], [(2, 2)]], option='paths')
            sage: kQ.is_left_module()
            True

        Taking the right closure of a left closed set produces another
        left closed set::

            sage: Q2 = DiGraph({1:{2:['a'], 3:['b', 'c']}, 2:{3:['d']}}).path_semigroup()
            sage: M = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a')]], option='paths')
            sage: M.is_left_module()
            True

        Note that the second path is length 2, so even though the edge (1, 2, 'a')
        appears in the input the path [(1, 2, 'a')] is not in the right closure::

            sage: N = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a'), (2, 3, 'd')]], option='paths')
            sage: N.is_left_module()
            False
        """

class QuiverRep_with_dual_path_basis(QuiverRep_generic):
    """
    The basis of the module must be closed under left deletion of an edge; that
    is, deleting any edge from the beginning of any path in the basis must
    result in a path also contained in the basis of the module.

    INPUT:

    - ``k`` -- ring; the base ring of the representation

    - ``P`` -- the path semigroup of the quiver `Q` of the representation

    - ``basis`` -- list (default: empty); should be a list of paths (also
      lists) in the quiver `Q`.  Entries that do not represent valid paths
      are ignored and duplicate paths are deleted.  The closure of this
      list under left deletion forms the basis of the resulting
      representation.
    """
    def __init__(self, k, P, basis) -> None:
        """
        Initialize ``self``. Type ``QuiverRep_with_dual_path_basis?`` for
        more information.

        TESTS::

            sage: Q1 = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: I2 = Q1.representation(QQ, [[(2, 2)]], option='dual paths')
            sage: I2.dimension()
            2
            sage: kQdual = Q1.representation(QQ, [[(1, 1)], [(2, 2)], [(1, 2, 'a')], [(1, 2, 'a')]], option='dual paths')
            sage: kQdual.dimension()
            3
            sage: Q2 = DiGraph({1:{2:['a'], 3:['b', 'c']}, 2:{3:['d']}}).path_semigroup()
            sage: M = Q2.representation(QQ, [[(1, 2, 'a'), (2, 3, 'd')], [(1, 3, 'b')]], option='dual paths')
            sage: M.dimension_vector()
            (2, 0, 0)
            sage: N = Q2.representation(QQ, [[(2, 2)], [(1, 2, 'a'), (2, 3, 'd')]], option='dual paths')
            sage: N.dimension_vector()
            (2, 1, 0)
            sage: TestSuite(N).run()
        """
