from _typeshed import Incomplete
from sage.categories.homset import Homset as Homset
from sage.misc.cachefunc import cached_method as cached_method
from sage.quivers.morphism import QuiverRepHom as QuiverRepHom

class QuiverHomSpace(Homset):
    """
    A homomorphism of quiver representations (of one and the same quiver)
    is given by specifying, for each vertex of the quiver, a homomorphism
    of the spaces assigned to this vertex such that these homomorphisms
    commute with the edge maps.  This class handles the set of all
    such maps, `Hom_Q(M, N)`.

    INPUT:

    - ``domain`` -- the domain of the homomorphism space

    - ``codomain`` -- the codomain of the homomorphism space

    OUTPUT:

    - :class:`QuiverHomSpace`, the homomorphism space
      ``Hom_Q(domain, codomain)``

    .. NOTE::

        The quivers of the domain and codomain must be equal or a
        :exc:`ValueError` is raised.

    EXAMPLES::

        sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
        sage: H = Q.S(QQ, 2).Hom(Q.P(QQ, 1))
        sage: H.dimension()
        2
        sage: H.gens()
        (Homomorphism of representations of Multi-digraph on 2 vertices,
         Homomorphism of representations of Multi-digraph on 2 vertices)
    """
    Element = QuiverRepHom
    identity: Incomplete
    def __init__(self, domain, codomain, category=None) -> None:
        """
        Initialize ``self``. Type ``QuiverHomSpace?`` for more information.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: H = Q.S(QQ, 2).Hom(Q.P(QQ, 1))
            sage: TestSuite(H).run()
        """
    @cached_method
    def zero(self):
        """
        Return the zero morphism.

        .. NOTE::

            It is needed to override the method inherited from
            the category of modules, because it would create
            a morphism that is of the wrong type and does not
            comply with :class:`~sage.quivers.morphism.QuiverRepHom`.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: H = Q.S(QQ, 2).Hom(Q.P(QQ, 1))
            sage: H.zero() + H.an_element() == H.an_element()
            True
            sage: isinstance(H.zero(), H.element_class)
            True
        """
    def __call__(self, *data, **kwds):
        '''
        A homomorphism of quiver representations (of one and the same
        quiver) is given by specifying, for each vertex of the quiver, a
        homomorphism of the spaces assigned to this vertex such that these
        homomorphisms commute with the edge maps. The domain and codomain
        of the homomorphism are required to be representations over the
        same quiver with the same base ring.

        INPUT:

        Usually, one would provide a single dict, list,
        :class:`QuiverRepElement` or :class:`QuiverRepHom` as arguments.
        The semantics is as follows:

          - list: ``data`` can be a list of images for the generators of
            the domain.  "Generators" means the output of the ``gens()``
            method.  An error will be generated if the map so defined
            is not equivariant with respect to the action of the quiver.
          - dictionary: ``data`` can be a dictionary associating to each
            vertex of the quiver either a homomorphism with domain and
            codomain the spaces associated to this vertex in the domain
            and codomain modules respectively, or a matrix defining such
            a homomorphism, or an object that sage can construct such a
            matrix from.  Not all vertices must be specified, unspecified
            vertices are assigned the zero map, and keys not corresponding
            to vertices of the quiver are ignored.  An error will be
            generated if these maps do not commute with the edge maps of
            the domain and codomain.
          - :class:`QuiverRepElement`: if the domain is a
            :class:`QuiverRep_with_path_basis` then ``data`` can be a single
            :class:`QuiverRepElement` belonging to the codomain.  The map
            is then defined by sending each path, ``p``, in the basis
            to ``data*p``.  If ``data`` is not an element of the codomain or
            the domain is not a :class:`QuiverRep_with_path_basis` then
            an error will be generated.
          - :class:`QuiverRepHom`: the input can also be a map `f : D \\to C`
            such that there is a coercion from the domain of ``self`` to ``D``
            and from ``C`` to the codomain of ``self``.  The composition
            of these maps is the result.

        If there additionally are keyword arguments or if a
        :class:`QuiverRepHom` can not be created from the data, then the
        default call method of :class:`~sage.categories.homset.Homset`
        is called instead.

        OUTPUT: :class:`QuiverRepHom`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:[\'a\', \'b\']}, 2:{3:[\'c\']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, \'a\'): [[1, 0], [0, 0]], (1, 2, \'b\'): [[0, 0], [0, 1]], (2, 3, \'c\'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: H = S.Hom(M)

        With no additional data this creates the zero map::

            sage: f = H() # indirect doctest
            sage: f.is_zero()
            True

        We must specify maps at the vertices to get a nonzero
        homomorphism.  Note that if the dimensions of the spaces assigned
        to the domain and codomain of a vertex are equal then Sage will
        construct the identity matrix from ``1``::

            sage: maps2 = {2:[1, -1], 3:1}
            sage: g = H(maps2) # indirect doctest

        Here we create the same map by specifying images for the generators::

            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: h = H([x, y]) # indirect doctest
            sage: g == h
            True

        Here is an example of the same with a bigger identity matrix::

            sage: spaces3 = {2: QQ^2, 3: QQ^2}
            sage: maps3 = {(2, 3, \'c\'): [[1, 0], [1, 0]]}
            sage: S3 = Q.representation(QQ, spaces3, maps3)
            sage: h3 = S3.Hom(M)({2: 1, 3: [[1], [0]]})
            sage: h3.get_map(2)
            Vector space morphism represented by the matrix:
            [1 0]
            [0 1]
            Domain: Vector space of dimension 2 over Rational Field
            Codomain: Vector space of dimension 2 over Rational Field

        If the domain is a module of type :class:`QuiverRep_with_path_basis`
        (for example, the indecomposable projectives) we can create maps by
        specifying a single image::

            sage: Proj = Q.P(GF(7), 3)
            sage: Simp = Q.S(GF(7), 3)
            sage: im = Simp({3: (1,)})
            sage: H2 = Proj.Hom(Simp)
            sage: H2(im).is_surjective() # indirect doctest
            True
        '''
    def natural_map(self):
        """
        The natural map from domain to codomain.

        This is the zero map.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: S.hom(M)      # indirect doctest
            Homomorphism of representations of Multi-digraph on 3 vertices
            sage: S.hom(M) == S.Hom(M).natural_map()
            True
        """
    def base_ring(self):
        """
        Return the base ring of the representations.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: H = Q.S(QQ, 2).Hom(Q.P(QQ, 1))
            sage: H.base_ring()
            Rational Field
        """
    def quiver(self):
        """
        Return the quiver of the representations.

        OUTPUT: :class:`DiGraph`; the quiver of the representations

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: H = P.S(QQ, 2).Hom(P.P(QQ, 1))
            sage: H.quiver() is P.quiver()
            True
        """
    def domain(self):
        """
        Return the domain of the hom space.

        OUTPUT: :class:`QuiverRep`; the domain of the Hom space

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: S = Q.S(QQ, 2)
            sage: H = S.Hom(Q.P(QQ, 1))
            sage: H.domain() is S
            True
        """
    def codomain(self):
        """
        Return the codomain of the hom space.

        OUTPUT: :class:`QuiverRep`; the codomain of the Hom space

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: H = Q.S(QQ, 2).Hom(P)
            sage: H.codomain() is P
            True
        """
    def dimension(self):
        """
        Return the dimension of the hom space.

        OUTPUT: integer; the dimension

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: H = Q.S(QQ, 2).Hom(Q.P(QQ, 1))
            sage: H.dimension()
            2
        """
    def gens(self) -> tuple:
        """
        Return a tuple of generators of the hom space (as a `k`-vector
        space).

        OUTPUT: tuple of :class:`QuiverRepHom` objects; the generators

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: H = Q.S(QQ, 2).Hom(Q.P(QQ, 1))
            sage: H.gens()
            (Homomorphism of representations of Multi-digraph on 2 vertices,
             Homomorphism of representations of Multi-digraph on 2 vertices)
        """
    def coordinates(self, hom):
        """
        Return the coordinates of the map when expressed in terms of the
        generators (i. e., the output of the ``gens`` method) of the
        hom space.

        INPUT:

        - ``hom`` -- :class:`QuiverRepHom`

        OUTPUT:

        - list, the coordinates of the given map when written in terms of the
          generators of the :class:`QuiverHomSpace`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: S = Q.S(QQ, 2)
            sage: P = Q.P(QQ, 1)
            sage: H = S.Hom(P)
            sage: f = S.hom({2: [[1,-1]]}, P)
            sage: H.coordinates(f)
            [1, -1]
        """
    def left_module(self, basis: bool = False):
        """
        Create the QuiverRep of ``self`` as a module over the opposite
        quiver.

        INPUT:

        - ``basis`` -- boolean; if ``False``, then only the module is
          returned.  If ``True``, then a tuple is returned.  The first
          element is the QuiverRep and the second element is a
          dictionary which associates to each vertex a list.  The
          elements of this list are the homomorphisms which correspond to
          the basis elements of that vertex in the module.

        OUTPUT: :class:`QuiverRep` or tuple

        .. WARNING::

            The codomain of the Hom space must be a left module.

        .. NOTE::

            The left action of a path `e` on a map `f` is given by
            `(ef)(m) = ef(m)`.  This gives the Hom space its structure as
            a left module over the path algebra. This is then converted to
            a right module over the path algebra of the opposite quiver
            ``Q.reverse()`` and returned.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b'], 3: ['c', 'd']}, 2:{3:['e']}}).path_semigroup()
            sage: P = Q.P(GF(3), 3)
            sage: A = Q.free_module(GF(3))
            sage: H = P.Hom(A)
            sage: H.dimension()
            6
            sage: M, basis_dict = H.left_module(true)
            sage: M.dimension_vector()
            (4, 1, 1)
            sage: Q.reverse().P(GF(3), 3).dimension_vector()
            (4, 1, 1)

        As lists start indexing at 0 the `i`-th vertex corresponds to the
        `(i-1)`-th entry of the dimension vector::

            sage: len(basis_dict[2]) == M.dimension_vector()[1]
            True
        """
