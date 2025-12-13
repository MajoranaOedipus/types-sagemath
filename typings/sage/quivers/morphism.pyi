from sage.categories.morphism import CallMorphism as CallMorphism
from sage.matrix.constructor import Matrix as Matrix

class QuiverRepHom(CallMorphism):
    '''
    A homomorphism of quiver representations (of one and the same quiver)
    is given by specifying, for each vertex of the quiver, a homomorphism
    of the spaces assigned to this vertex such that these homomorphisms
    commute with the edge maps.  The domain and codomain of the
    homomorphism are required to be representations of the same quiver
    over the same base ring.

    INPUT:

    - ``domain`` -- :class:`QuiverRep`, the domain of the homomorphism

    - ``codomain`` -- :class:`QuiverRep`, the codomain of the homomorphism

    - ``data`` -- dict, list, or :class:`QuiverRepElement`
      (default: empty dict),
      with the following meaning:

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
        :class:`QuiverRepElement` belonging to the codomain.  The map is
        then defined by sending each path, ``p``, in the basis to ``data*p``.
        If ``data`` is not an element of the codomain or the domain is not a
        :class:`QuiverRep_with_path_basis` then an error will be generated.
      - :class:`QuiverRepHom`: the input can also be a map `f : D \\to C` such
        that there is a coercion from the domain of ``self`` to ``D``
        and from ``C`` to the codomain of ``self``.  The composition
        of these maps is the result.

    OUTPUT: :class:`QuiverRepHom`

    EXAMPLES::

        sage: Q = DiGraph({1:{2:[\'a\', \'b\']}, 2:{3:[\'c\']}}).path_semigroup()
        sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
        sage: maps = {(1, 2, \'a\'): [[1, 0], [0, 0]], (1, 2, \'b\'): [[0, 0], [0, 1]], (2, 3, \'c\'): [[1], [1]]}
        sage: M = Q.representation(QQ, spaces, maps)
        sage: spaces2 = {2: QQ^1, 3: QQ^1}
        sage: S = Q.representation(QQ, spaces2)

    With no additional data this creates the zero map::

        sage: f = S.hom(M)
        sage: f.is_zero()
        True

    We must specify maps at the vertices to get a nonzero homomorphism.
    Note that if the dimensions of the spaces assigned to the domain and
    codomain of a vertex are equal then Sage will construct the identity
    matrix from ``1``::

        sage: maps2 = {2:[1, -1], 3:1}
        sage: g = S.hom(maps2, M)

    Here we create the same map by specifying images for the generators::

        sage: x = M({2: (1, -1)})
        sage: y = M({3: (1,)})
        sage: h = S.hom([x, y], M)
        sage: g == h
        True

    If the domain is a module of type QuiverRep_with_path_basis (for example,
    the indecomposable projectives) we can create maps by specifying a single
    image::

        sage: Proj = Q.P(GF(7), 3)
        sage: Simp = Q.S(GF(7), 3)
        sage: im = Simp({3: (1,)})
        sage: Proj.hom(im, Simp).is_surjective()
        True
    '''
    def __init__(self, domain, codomain, data={}) -> None:
        """
        Initialize ``self``. Type ``QuiverRepHom?`` for more information.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: f = S.hom(M)
            sage: f.is_zero()
            True
            sage: maps2 = {2:[1, -1], 3:1}
            sage: g = S.hom(maps2, M)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: h = S.hom([x, y], M)
            sage: g == h
            True
            sage: Proj = Q.P(GF(7), 3)
            sage: Simp = Q.S(GF(7), 3)
            sage: im = Simp({3: (1,)})
            sage: Proj.hom(im, Simp).is_surjective()
            True

        ::

            sage: Q = DiGraph({1:{2:['a']}}).path_semigroup()
            sage: H1 = Q.P(GF(3), 2).Hom(Q.S(GF(3), 2))
            sage: H2 = Q.P(GF(3), 2).Hom(Q.S(GF(3), 1))
            sage: H1.an_element() in H1   # indirect doctest
            True
        """
    def __add__(left, right):
        """
        This function overloads the ``+`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: z = M.zero()
            sage: h = S.hom([x, z], M)
            sage: g = S.hom([z, z], M)
            sage: f = g + h
            sage: f(S.gens()[0]) == x
            True
            sage: f(S.gens()[1]) == z
            True
        """
    def __iadd__(self, other):
        """
        This function overloads the ``+=`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: z = M.zero()
            sage: h = S.hom([x, z], M)
            sage: g = S.hom([z, z], M)
            sage: g += h
            sage: g(S.gens()[0]) == x
            True
            sage: g(S.gens()[1]) == z
            True
        """
    def __sub__(left, right):
        """
        This function overloads the ``-`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: z = M.zero()
            sage: h = S.hom([x, z], M)
            sage: g = S.hom([z, y], M)
            sage: f = h - g
            sage: f(S.gens()[0]) == x
            True
            sage: f(S.gens()[1]) == -y
            True
        """
    def __isub__(self, other):
        """
        This function overloads the ``-=`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: z = M.zero()
            sage: h = S.hom([x, z], M)
            sage: g = S.hom([z, y], M)
            sage: h -= g
            sage: h(S.gens()[0]) == x
            True
            sage: h(S.gens()[1]) == -y
            True
        """
    def __neg__(self):
        """
        This function overrides the unary ``-`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: h = S.hom([x, y], M)
            sage: g = -h
            sage: g(S.gens()[0]) == -x
            True
            sage: g(S.gens()[1]) == -y
            True
        """
    def __pos__(self):
        """
        This function overrides the unary ``+`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: h = S.hom([x, y], M)
            sage: g = +h
            sage: g == h
            True
        """
    def __eq__(self, other):
        """
        This function overrides the ``==`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: g = S.hom([x, y], M)
            sage: h = S.hom([x, y], M)
            sage: g == h
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: g = S.hom([x, y], M)
            sage: H = hash(g)
        """
    def __ne__(self, other):
        """
        This function overrides the ``!=`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: z = M.zero()
            sage: g = S.hom([x, y], M)
            sage: h = S.hom([x, z], M)
            sage: g != h
            True
        """
    def __bool__(self) -> bool:
        """
        Return whether ``self`` is the zero morphism.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = M({2: (1, -1)})
            sage: y = M({3: (1,)})
            sage: z = M.zero()
            sage: g = S.hom([x, y], M)
            sage: h = S.hom([z, z], M)
            sage: bool(g)
            True
            sage: bool(h)
            False
        """
    def __mul__(self, other):
        """
        This function overrides the ``*`` operator.

        TESTS::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces2 = {2: QQ^1, 3: QQ^1}
            sage: S = Q.representation(QQ, spaces2)
            sage: x = S.gens()[0]
            sage: y = S.gens()[1]
            sage: g = S.hom([x, y], S)
            sage: h = S.hom(S)
            sage: (g*h).is_zero()
            True
        """
    def domain(self):
        """
        Return the domain of the homomorphism.

        OUTPUT: :class:`QuiverRep`; the domain

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: S = Q.representation(QQ)
            sage: g = M.hom(S)
            sage: g.domain() is M
            True
        """
    def codomain(self):
        """
        Return the codomain of the homomorphism.

        OUTPUT: :class:`QuiverRep`; the codomain

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: S = Q.representation(QQ)
            sage: g = S.hom(M)
            sage: g.codomain() is M
            True
        """
    def get_matrix(self, vertex):
        """
        Return the matrix of the homomorphism attached to vertex
        ``vertex``.

        INPUT:

        - ``vertex`` -- integer; a vertex of the quiver

        OUTPUT: the matrix representing the homomorphism associated to
        the given vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: I = Q.I(QQ, 3)
            sage: M = I/I.radical()
            sage: f = M.coerce_map_from(I)
            sage: f.get_matrix(1)
            [1 0]
            [0 1]
        """
    def get_map(self, vertex):
        """
        Return the homomorphism at the given vertex ``vertex``.

        INPUT:

        - ``vertex`` -- integer; a vertex of the quiver

        OUTPUT: the homomorphism associated to the given vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: S = P/P.radical()
            sage: f = S.coerce_map_from(P)
            sage: f.get_map(1).is_bijective()
            True
        """
    def quiver(self):
        """
        Return the quiver of the representations in the domain/codomain.

        OUTPUT:

        - :class:`DiGraph`, the quiver of the representations in the domain
          and codomain

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.quiver() is Q.quiver()
            True
        """
    def base_ring(self):
        """
        Return the base ring of the representation in the codomain.

        OUTPUT: the base ring of the codomain

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.base_ring() is QQ
            True
        """
    def is_injective(self) -> bool:
        """
        Test whether the homomorphism is injective.

        OUTPUT: boolean; ``True`` if the homomorphism is injective, ``False``
        otherwise

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.is_injective()
            True
            sage: g = P.hom(P)
            sage: g.is_injective()
            False
        """
    def is_surjective(self) -> bool:
        """
        Test whether the homomorphism is surjective.

        OUTPUT: boolean; ``True`` if the homomorphism is surjective, ``False``
        otherwise

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.is_surjective()
            True
            sage: g = P.hom(P)
            sage: g.is_surjective()
            False
        """
    def is_isomorphism(self) -> bool:
        """
        Test whether the homomorphism is an isomorphism.

        OUTPUT: boolean; ``True`` if the homomorphism is bijective, ``False``
        otherwise

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.is_isomorphism()
            True
            sage: g = P.hom(P)
            sage: g.is_isomorphism()
            False
        """
    def is_zero(self) -> bool:
        """
        Test whether the homomorphism is the zero homomorphism.

        OUTPUT: boolean; ``True`` if the homomorphism is zero, ``False``
        otherwise

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.is_zero()
            False
            sage: g = P.hom(P)
            sage: g.is_zero()
            True
        """
    def is_endomorphism(self) -> bool:
        """
        Test whether the homomorphism is an endomorphism.

        OUTPUT: boolean; ``True`` if the domain equals the codomain, ``False``
        otherwise

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: f = P.hom({1: 1, 2: 1, 3: 1}, P)
            sage: f.is_endomorphism()
            True
            sage: S = P/P.radical()
            sage: g = S.coerce_map_from(P)
            sage: g.is_endomorphism()
            False
        """
    def rank(self):
        """
        Return the rank of the homomorphism ``self`` (as a `k`-linear
        map).

        OUTPUT: integer; the rank

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: S = P/P.radical()
            sage: f = S.coerce_map_from(P)
            sage: assert(f.rank() == 1)
        """
    def kernel(self):
        """
        Return the kernel of ``self``.

        OUTPUT: :class:`QuiverRep`; the kernel

        .. NOTE::

            To get the inclusion map of the kernel, ``K``, into the
            domain, ``D``, use ``D.coerce_map_from(K)``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^2, 3: QQ^1}
            sage: N = Q.representation(QQ, spaces2, {(2, 3, 'c'): [[1], [0]]})
            sage: maps2 = {2:[[1, 0], [0, 0]], 3:1}
            sage: g = N.hom(maps2, M)
            sage: g.kernel().dimension_vector()
            (0, 1, 0)
        """
    def image(self):
        """
        Return the image of ``self``.

        OUTPUT: :class:`QuiverRep`; the image

        .. NOTE::

            To get the inclusion map of the image, ``I``, into the
            codomain, ``C``, use ``C.coerce_map_from(I)``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^2, 3: QQ^1}
            sage: N = Q.representation(QQ, spaces2, {(2, 3, 'c'): [[1], [0]]})
            sage: maps2 = {2:[[1, 0], [0, 0]], 3:1}
            sage: g = N.hom(maps2, M)
            sage: g.image().dimension_vector()
            (0, 1, 1)
        """
    def cokernel(self):
        """
        Return the cokernel of ``self``.

        OUTPUT: :class:`QuiverRep`; the cokernel

        .. NOTE::

            To get the factor map of the codomain, ``D``, onto the
            cokernel, ``C``, use ``C.coerce_map_from(D)``.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^2, 3:QQ^1}
            sage: maps = {(1, 2, 'a'): [[1, 0], [0, 0]], (1, 2, 'b'): [[0, 0], [0, 1]], (2, 3, 'c'): [[1], [1]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: spaces2 = {2: QQ^2, 3: QQ^1}
            sage: N = Q.representation(QQ, spaces2, {(2, 3, 'c'): [[1], [0]]})
            sage: maps2 = {2:[[1, 0], [0, 0]], 3:1}
            sage: g = N.hom(maps2, M)
            sage: g.cokernel().dimension_vector()
            (2, 1, 0)
        """
    def linear_dual(self):
        """
        Compute the linear dual `Df : DN \\to DM` of
        ``self`` = `f : M \\to N` where `D(-) = Hom_k(-, k)`.

        OUTPUT: :class:`QuiverRepHom`; the map `Df : DN \\to DM`

        .. NOTE::

            If `e` is an edge of the quiver `Q` and `g` is an element of
            `Hom_k(N, k)` then we let `(ga)(m) = g(ma)`.  This gives
            `Hom_k(N, k)` its structure as a module over the opposite
            quiver ``Q.reverse()``.  The map `Hom_k(N, k) \\to Hom_k(M, k)`
            returned sends `g` to `gf`.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}, 2:{3:['c']}}).path_semigroup()
            sage: P = Q.P(QQ, 1)
            sage: S = P/P.radical()
            sage: f = S.coerce_map_from(P)

        The dual of a surjective map is injective and vice versa::

            sage: f.is_surjective()
            True
            sage: g = f.linear_dual()
            sage: g.is_injective()
            True

        The dual of a right module is a left module for the same quiver, Sage
        represents this as a right module for the opposite quiver::

            sage: g.quiver().path_semigroup() is Q.reverse()
            True

        The double dual of a map is the original representation::

            sage: g.linear_dual() == f
            True
        """
    def algebraic_dual(self):
        """
        Compute the algebraic dual `f^t : N^t \\to M^t` of
        ``self`` = `f : M \\to N` where `(-)^t = Hom_Q(-, kQ)`.

        OUTPUT: :class:`QuiverRepHom`; the map `f^t : N^t \\to M^t`

        .. NOTE::

            If `e` is an edge of the quiver `Q` and `g` is an element of
            `Hom_Q(N, kQ)` then we let `(ge)(m) = eg(m)`.  This gives
            `Hom_Q(N, kQ)` its structure as a module over the opposite
            quiver ``Q.reverse()``.  The map
            `Hom_Q(N, kQ) \\to Hom_Q(M, kQ)` returned sends `g` to `gf`.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a'], 3:['b','c','d']}, 2:{4:['e','f']}, 3:{4:['g']}, 5:{2:['h','i']}}).path_semigroup()
            sage: P1 = Q.P(QQ, 4)
            sage: P1.algebraic_dual()
            Representation with dimension vector (5, 2, 1, 1, 4)

        The algebraic dual of an indecomposable projective is the indecomposable
        projective of the same vertex in the opposite quiver. ::

            sage: Q.reverse().P(QQ, 4)
            Representation with dimension vector (5, 2, 1, 1, 4)
        """
    def direct_sum(self, maps, return_maps: bool = False, pinch=None):
        """
        Return the direct sum of ``self`` with the maps in the list ``maps``.

        INPUT:

        - ``maps`` -- :class:`QuiverRepHom` or list of :class:`QuiverRepHom`'s

        - ``return_maps`` -- boolean (default: ``False``); if ``False``, then
          the return value is a :class:`QuiverRepHom` which is the direct sum
          of ``self`` with the :class:`QuiverRepHoms` in ``maps``.
          If ``True``, then the return value is a tuple of length either 3
          or 5.  The first entry of the tuple is the QuiverRepHom giving
          the direct sum.  If ``pinch`` is either ``None`` or
          ``'codomain'`` then the next two entries in the tuple are lists
          giving respectively the inclusion and the projection maps for
          the factors of the direct sum.  Summands are ordered as given
          in maps with ``self`` as the zeroth summand.  If ``pinch`` is
          either ``None`` or ``'domain'`` then the next two entries in the
          tuple are the inclusion and projection maps for the codomain.
          Thus if ``pinch`` is ``None`` then the tuple will have length 5.
          If ``pinch`` is either ``'domain'`` or ``'codomain'`` then the
          tuple will have length 3.

        - ``pinch`` -- string or ``None`` (default: ``None``); if this is
          equal to ``'domain'``, then the domains of ``self`` and the
          given maps must be equal.  The direct sum of `f: A \\to B` and
          `g: A \\to C` returned is then the map `A \\to B \\oplus C` defined
          by sending `x` to `(f(x), g(x))`.  If ``pinch`` equals
          ``'codomain'``, then the codomains of ``self`` and the given
          maps must be equal.  The direct sum of `f: A \\to C` and
          `g: B \\to C` returned is then the map `A \\oplus B \\to C` defined
          by sending `(x, y)` to `f(x) + g(y)`.  Finally, if ``pinch`` is
          anything other than ``'domain'`` or ``'codomain'``, then the
          direct sum of `f: A \\to B` and `g: C \\to D` returned is the map
          `A \\oplus C \\to B \\oplus D` defined by sending `(x, y)` to
          `(f(x), g(y))`.

        OUTPUT: :class:`QuiverRepHom` or tuple

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: P1 = Q.P(GF(3), 1)
            sage: P2 = Q.P(GF(3), 2)
            sage: S1 = P1/P1.radical()
            sage: S2 = P2/P2.radical()
            sage: pi1 = S1.coerce_map_from(P1)
            sage: pi2 = S2.coerce_map_from(P2)
            sage: f = pi1.direct_sum(pi2)
            sage: f.domain().dimension_vector() == Q.free_module(GF(3)).dimension_vector()
            True
            sage: f.is_surjective()
            True
            sage: id = P1.Hom(P1).identity()
            sage: g = pi1.direct_sum(id, pinch='domain')
            sage: g.is_surjective()
            False
        """
    def lift(self, x):
        """
        Given an element `x` of the image, return an element of the domain
        that maps onto it under ``self``.

        INPUT:

        - ``x`` -- :class:`QuiverRepElement`

        OUTPUT: :class:`QuiverRepElement`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c','d']}}).path_semigroup()
            sage: P = Q.P(QQ, 3)
            sage: S = P/P.radical()
            sage: proj = S.coerce_map_from(P)
            sage: x = S.an_element()
            sage: y = proj.lift(x)
            sage: proj(y) == x
            True
            sage: zero = S.hom(S, {})
            sage: zero.lift(x)
            Traceback (most recent call last):
            ...
            ValueError: element is not in the image
        """
    def scalar_mult(self, scalar):
        """
        Return the result of the scalar multiplication ``scalar * self``,
        where ``scalar`` is an element of the base ring `k`.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: f = M.Hom(M).an_element()
            sage: x = M.an_element()
            sage: g = f.scalar_mult(6)
            sage: g(x) == 6*f(x)
            True
        """
    def iscalar_mult(self, scalar) -> None:
        """
        Multiply ``self`` by ``scalar`` in place.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}}).path_semigroup()
            sage: M = Q.P(QQ, 1)
            sage: f = M.Hom(M).an_element()
            sage: x = M.an_element()
            sage: y = f(x)
            sage: f.iscalar_mult(6)
            sage: f(x) == 6*y
            True
        """
