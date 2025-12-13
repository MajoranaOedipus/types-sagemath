from sage.geometry.hyperplane_arrangement.hyperplane import AmbientVectorSpace as AmbientVectorSpace, Hyperplane as Hyperplane
from sage.matrix.constructor import matrix as matrix, vector as vector
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class HyperplaneArrangementElement(Element):
    """
    A hyperplane arrangement.

    .. WARNING::

        You should never create
        :class:`HyperplaneArrangementElement` instances directly,
        always use the parent.
    """
    def __init__(self, parent, hyperplanes, check: bool = True, backend=None) -> None:
        """
        Construct a hyperplane arrangement.

        INPUT:

        - ``parent`` -- the parent :class:`HyperplaneArrangements`

        - ``hyperplanes`` -- tuple of hyperplanes

        - ``check`` -- boolean (default: ``True``); whether to check input

        - ``backend`` -- string (optional); the backend to
          use for the related polyhedral objects

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: elt = H(x, y); elt
            Arrangement <y | x>
            sage: TestSuite(elt).run()

        It is possible to specify a backend for polyhedral computations::

            sage: # needs sage.rings.number_field
            sage: R.<sqrt5> = QuadraticField(5)
            sage: H = HyperplaneArrangements(R, names='xyz')
            sage: x, y, z = H.gens()
            sage: A = H(sqrt5*x + 2*y + 3*z, backend='normaliz')
            sage: A.backend()
            'normaliz'
            sage: A.regions()[0].backend()                              # optional - pynormaliz
            'normaliz'
        """
    def __getitem__(self, i):
        """
        Return the `i`-th hyperplane.

        INPUT:

        - ``i`` -- integer

        OUTPUT: the `i`-th hyperplane

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: h = x|y;  h
            Arrangement <y | x>
            sage: h[0]
            Hyperplane 0*x + y + 0
            sage: h[1]
            Hyperplane x + 0*y + 0
        """
    def __hash__(self):
        """
        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: h = x|y; h
            Arrangement <y | x>
            sage: len_dict = {h: len(h)}
        """
    def n_hyperplanes(self):
        """
        Return the number of hyperplanes in the arrangement.

        OUTPUT: integer

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([1,1,0], [2,3,-1], [4,5,3])
            sage: A.n_hyperplanes()
            3
            sage: len(A)    # equivalent
            3
        """
    __len__ = n_hyperplanes
    def hyperplanes(self):
        """
        Return the hyperplanes in the arrangement as a tuple.

        OUTPUT: a tuple

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([1,1,0], [2,3,-1], [4,5,3])
            sage: A.hyperplanes()
            (Hyperplane x + 0*y + 1, Hyperplane 3*x - y + 2, Hyperplane 5*x + 3*y + 4)

        Note that the hyperplanes can be indexed as if they were a list::

            sage: A[0]
            Hyperplane x + 0*y + 1
        """
    def dimension(self):
        """
        Return the ambient space dimension of the arrangement.

        OUTPUT: integer

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: (x | x-1 | x+1).dimension()
            2
            sage: H(x).dimension()
            2
        """
    def rank(self):
        """
        Return the rank.

        OUTPUT:

        The dimension of the span of the normals to the
        hyperplanes in the arrangement.

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = H([[0, 1, 2, 3],[-3, 4, 5, 6]])
            sage: A.dimension()
            3
            sage: A.rank()
            2

            sage: # needs sage.graphs
            sage: B = hyperplane_arrangements.braid(3)
            sage: B.hyperplanes()
            (Hyperplane 0*t0 + t1 - t2 + 0,
             Hyperplane t0 - t1 + 0*t2 + 0,
             Hyperplane t0 + 0*t1 - t2 + 0)
            sage: B.dimension()
            3
            sage: B.rank()
            2

            sage: p = polytopes.simplex(5, project=True)
            sage: H = p.hyperplane_arrangement()
            sage: H.rank()
            5
        """
    def backend(self):
        """
        Return the backend used for polyhedral objects.

        OUTPUT: string giving the backend or ``None`` if none is specified

        EXAMPLES:

        By default, no backend is specified::

           sage: H = HyperplaneArrangements(QQ)
           sage: A = H()
           sage: A.backend()

        Otherwise, one may specify a polyhedral backend::

           sage: A = H(backend='ppl')
           sage: A.backend()
           'ppl'
           sage: A = H(backend='normaliz')
           sage: A.backend()
           'normaliz'
        """
    def union(self, other):
        """
        The union of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a hyperplane arrangement or something that can
          be converted into a hyperplane arrangement

        OUTPUT: a new hyperplane arrangement

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([1,2,3], [0,1,1], [0,1,-1], [1,-1,0], [1,1,0])
            sage: B = H([1,1,1], [1,-1,1], [1,0,-1])
            sage: C = A.union(B); C
            Arrangement of 8 hyperplanes of dimension 2 and rank 2
            sage: C == A | B   # syntactic sugar
            True

        A single hyperplane is coerced into a hyperplane arrangement
        if necessary::

            sage: A.union(x+y-1)
            Arrangement of 6 hyperplanes of dimension 2 and rank 2
            sage: A.add_hyperplane(x+y-1)    # alias
            Arrangement of 6 hyperplanes of dimension 2 and rank 2

            sage: P.<x,y> = HyperplaneArrangements(RR)
            sage: C = P(2*x + 4*y + 5)
            sage: C.union(A)
            Arrangement of 6 hyperplanes of dimension 2 and rank 2
        """
    add_hyperplane = union
    __or__ = union
    def plot(self, **kwds):
        """
        Plot the hyperplane arrangement.

        OUTPUT: a graphics object

        EXAMPLES::

            sage: L.<x, y> = HyperplaneArrangements(QQ)
            sage: L(x, y, x+y-2).plot()                                                 # needs sage.plot
            Graphics object consisting of 3 graphics primitives
        """
    def cone(self, variable: str = 't'):
        """
        Return the cone over the hyperplane arrangement.

        INPUT:

        - ``variable`` -- string; the name of the additional variable

        OUTPUT:

        A new hyperplane arrangement `L`.
        Its equations consist of `[0, -d, a_1, \\ldots, a_n]` for each
        `[d, a_1, \\ldots, a_n]` in the original arrangement and the
        equation `[0, 1, 0, \\ldots, 0]` (maybe not in this order).

        .. WARNING::

            While there is an almost-one-to-one correspondence between the
            hyperplanes of ``self`` and those of ``self.cone()``, there is
            no guarantee that the order in which they appear in
            ``self.hyperplanes()`` will match the order in which their
            counterparts in ``self.cone()`` will appear in
            ``self.cone().hyperplanes()``! This warning does not apply
            to ordered hyperplane arrangements.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: a.<x,y,z> = hyperplane_arrangements.semiorder(3)
            sage: b = a.cone()
            sage: a.characteristic_polynomial().factor()
            x * (x^2 - 6*x + 12)
            sage: b.characteristic_polynomial().factor()
            (x - 1) * x * (x^2 - 6*x + 12)
            sage: a.hyperplanes()
            (Hyperplane 0*x + y - z - 1,
             Hyperplane 0*x + y - z + 1,
             Hyperplane x - y + 0*z - 1,
             Hyperplane x - y + 0*z + 1,
             Hyperplane x + 0*y - z - 1,
             Hyperplane x + 0*y - z + 1)
            sage: b.hyperplanes()
            (Hyperplane -t + 0*x + y - z + 0,
             Hyperplane -t + x - y + 0*z + 0,
             Hyperplane -t + x + 0*y - z + 0,
             Hyperplane t + 0*x + 0*y + 0*z + 0,
             Hyperplane t + 0*x + y - z + 0,
             Hyperplane t + x - y + 0*z + 0,
             Hyperplane t + x + 0*y - z + 0)
        """
    @cached_method
    def intersection_poset(self, element_label: str = 'int'):
        '''
        Return the intersection poset of the hyperplane arrangement.

        INPUT:

        - ``element_label`` -- (default: ``\'int\'``) specify how an
          intersection should be represented; must be one of the following:

          * ``\'subspace\'`` -- as a subspace
          * ``\'subset\'`` -- as a subset of the defining hyperplanes
          * ``\'int\'`` -- as an integer

        OUTPUT:

        The poset of non-empty intersections of hyperplanes, with intersections
        represented by integers, subsets of integers or subspaces (see the
        examples for more details).

        EXAMPLES:

        By default, the elements of the poset are the integers from `0` through
        the cardinality of the poset *minus one*. The element labelled `0`
        always corresponds to the ambient vector space, and the hyperplanes
        themselves are labelled `1, 2, \\ldots, n`, where `n` is the number
        of hyperplanes of the arrangement. ::

            sage: A = hyperplane_arrangements.coordinate(2)
            sage: L = A.intersection_poset(); L                                         # needs sage.combinat
            Finite poset containing 4 elements
            sage: sorted(L)                                                             # needs sage.combinat
            [0, 1, 2, 3]
            sage: L.level_sets()                                                        # needs sage.combinat
            [[0], [1, 2], [3]]

        ::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.semiorder(3)
            sage: L = A.intersection_poset(); L
            Finite poset containing 19 elements
            sage: sorted(L)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            sage: [sorted(level_set) for level_set in L.level_sets()]
            [[0], [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

        By passing the argument ``element_label="subset"``, each element of the
        intersection poset is labelled by the set of indices of the hyperplanes
        whose intersection is said element. The index of a hyperplane is its
        index in ``self.hyperplanes()``. ::

            sage: A = hyperplane_arrangements.semiorder(3)
            sage: L = A.intersection_poset(element_label=\'subset\')                      # needs sage.combinat
            sage: [sorted(level, key=sorted) for level in L.level_sets()]               # needs sage.combinat
            [[{}],
             [{0}, {1}, {2}, {3}, {4}, {5}],
             [{0, 2}, {0, 3}, {0, 4}, {0, 5}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}, {3, 4}, {3, 5}]]

        ::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H((y, y-1, y+1, x-y, x+y))
            sage: L = A.intersection_poset(element_label=\'subset\')                      # needs sage.combinat
            sage: sorted(L, key=sorted)                                                 # needs sage.combinat
            [{}, {0}, {0, 3}, {0, 4}, {1}, {1, 3, 4}, {2}, {2, 3}, {2, 4}, {3}, {4}]

        One can instead use affine subspaces as elements,
        which is what is used to compute the poset in the first place::

            sage: A = hyperplane_arrangements.coordinate(2)
            sage: L = A.intersection_poset(element_label=\'subspace\'); L                 # needs sage.combinat
            Finite poset containing 4 elements
            sage: sorted(L, key=lambda S: (S.dimension(),                               # needs sage.combinat
            ....:                          S.linear_part().basis_matrix()))
            [Affine space p + W where:
               p = (0, 0)
               W = Vector space of degree 2 and dimension 0 over Rational Field
                   Basis matrix: [],
             Affine space p + W where:
               p = (0, 0)
               W = Vector space of degree 2 and dimension 1 over Rational Field
                   Basis matrix: [0 1],
             Affine space p + W where:
               p = (0, 0)
               W = Vector space of degree 2 and dimension 1 over Rational Field
                   Basis matrix: [1 0],
             Affine space p + W where:
               p = (0, 0)
               W = Vector space of dimension 2 over Rational Field]
        '''
    @cached_method
    def characteristic_polynomial(self):
        """
        Return the characteristic polynomial of the hyperplane arrangement.

        OUTPUT: the characteristic polynomial in `\\QQ[x]`

        EXAMPLES::

            sage: a = hyperplane_arrangements.coordinate(2)
            sage: a.characteristic_polynomial()
            x^2 - 2*x + 1

        TESTS::

            sage: H.<s,t,u,v> = HyperplaneArrangements(QQ)
            sage: m = matrix([(0, -1, 0, 1, -1), (0, -1, 1, -1, 0), (0, -1, 1, 0, -1),
            ....:   (0, 1, 0, 0, 0), (0, 1, 0, 1, -1), (0, 1, 1, -1, 0), (0, 1, 1, 0, -1)])
            sage: R.<x> = QQ[]
            sage: expected_charpoly = (x - 1) * x * (x^2 - 6*x + 12)
            sage: for s in SymmetricGroup(4):   # long time (about a second on a Core i7)
            ....:     m_perm = [m.column(i) for i in [0, s(1), s(2), s(3), s(4)]]
            ....:     m_perm = matrix(m_perm).transpose()
            ....:     charpoly = H(m_perm.rows()).characteristic_polynomial()
            ....:     assert charpoly == expected_charpoly

        Check the corner case of the empty arrangement::

            sage: E = H()
            sage: E.characteristic_polynomial()
            1
        """
    @cached_method
    def poincare_polynomial(self):
        """
        Return the Poincaré polynomial of the hyperplane arrangement.

        OUTPUT: the Poincaré polynomial in `\\QQ[x]`

        EXAMPLES::

            sage: a = hyperplane_arrangements.coordinate(2)
            sage: a.poincare_polynomial()
            x^2 + 2*x + 1
        """
    @cached_method
    def cocharacteristic_polynomial(self):
        """
        Return the cocharacteristic polynomial of ``self``.

        The cocharacteristic polynomial of a hyperplane arrangement `A`
        is defined by

        .. MATH::

            \\Psi_A(z) := \\sum_{X \\in L} |\\mu(B,X)| z^{\\dim X},

        where `L` is the intersection poset of `A`, `B` is the minimal
        element of `L` (here, the `0` dimensional subspace), and
        `\\mu` is the Möbius function of `L`.

        OUTPUT: the cocharacteristic polynomial in `\\ZZ[z]`

        EXAMPLES::

            sage: A = hyperplane_arrangements.coordinate(2)
            sage: A.cocharacteristic_polynomial()                                       # needs sage.graphs
            z^2 + 2*z + 1
            sage: B = hyperplane_arrangements.braid(3)
            sage: B.cocharacteristic_polynomial()                                       # needs sage.graphs
            2*z^3 + 3*z^2 + z

        TESTS::

            sage: I = hyperplane_arrangements.Ish(2)
            sage: I.is_central()
            False
            sage: I.cocharacteristic_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: only defined for central hyperplane arrangements
        """
    @cached_method
    def primitive_eulerian_polynomial(self):
        """
        Return the primitive Eulerian polynomial of ``self``.

        The primitive Eulerian polynomial of a hyperplane arrangement `A`
        is defined [BHS2023]_ by

        .. MATH::

            P_A(z) := \\sum_{X \\in L} |\\mu(B,X)| (z - 1)^{\\mathrm{codim} X},

        where `L` is the intersection poset of `A`, `B` is the minimal
        element of `L` (here, the `0` dimensional subspace), and
        `\\mu` is the Möbius function of `L`.

        OUTPUT: the primitive Eulerian polynomial in `\\ZZ[z]`

        EXAMPLES::

            sage: A = hyperplane_arrangements.coordinate(2)
            sage: A.primitive_eulerian_polynomial()                                     # needs sage.graphs
            z^2
            sage: B = hyperplane_arrangements.braid(3)
            sage: B.primitive_eulerian_polynomial()                                     # needs sage.graphs
            z^2 + z

            sage: H = hyperplane_arrangements.Shi(['B',2]).cone()
            sage: H.is_simplicial()
            False
            sage: H.primitive_eulerian_polynomial()                                     # needs sage.graphs
            z^3 + 11*z^2 + 4*z

            sage: H = hyperplane_arrangements.graphical(graphs.CycleGraph(4))
            sage: H.primitive_eulerian_polynomial()                                     # needs sage.graphs
            z^3 + 3*z^2 - z

        We verify Example 2.4 in [BHS2023]_ for `k = 2,3,4,5`::

            sage: R.<x,y> = HyperplaneArrangements(QQ)
            sage: for k in range(2,6):                                                  # needs sage.graphs
            ....:     H = R([x+j*y for j in range(k)])
            ....:     H.primitive_eulerian_polynomial()
            z^2
            z^2 + z
            z^2 + 2*z
            z^2 + 3*z

        We verify Equation (4) in [BHS2023]_ on some examples::

            sage: # needs sage.graphs
            sage: R.<x> = ZZ[]
            sage: Arr = [hyperplane_arrangements.braid(n) for n in range(2,6)]
            sage: all(R(A.cocharacteristic_polynomial()(1/(x-1)) * (x-1)^A.dimension())
            ....:     == R(A.primitive_eulerian_polynomial()) for A in Arr)
            True

        We compute types `H_3` and `F_4` in Table 1 of [BHS2023]_::

            sage: # needs sage.libs.gap
            sage: W = CoxeterGroup(['H',3], implementation='matrix')
            sage: A = HyperplaneArrangements(W.base_ring(), tuple(f'x{s}' for s in range(W.rank())))
            sage: H = A([[0] + list(r) for r in W.positive_roots()])
            sage: H.is_simplicial()                                                     # needs sage.graphs
            True
            sage: H.primitive_eulerian_polynomial()
            z^3 + 28*z^2 + 16*z

            sage: W = CoxeterGroup(['F',4], implementation='permutation')
            sage: A = HyperplaneArrangements(QQ, tuple(f'x{s}' for s in range(W.rank())))
            sage: H = A([[0] + list(r) for r in W.positive_roots()])
            sage: H.primitive_eulerian_polynomial()     # long time                     # needs sage.graphs
            z^4 + 116*z^3 + 220*z^2 + 48*z

        We verify Proposition 2.5 in [BHS2023]_ on the braid arrangement
        `B_k` for `k = 2,3,4,5`::

            sage: B = [hyperplane_arrangements.braid(k) for k in range(2,6)]
            sage: all(H.is_simplicial() for H in B)
            True
            sage: all(c > 0 for H in B                                                  # needs sage.graphs
            ....:     for c in H.primitive_eulerian_polynomial().coefficients())
            True

        We verify Example 9.4 in [BHS2023]_ showing a hyperplane arrangement
        whose primitive Eulerian polynomial does not have real roots (in
        general, the graphical arrangement of a cycle graph corresponds
        to the arrangements in Example 9.4)::

            sage: # needs sage.graphs
            sage: H = hyperplane_arrangements.graphical(graphs.CycleGraph(5))
            sage: pep = H.primitive_eulerian_polynomial(); pep
            z^4 + 6*z^3 - 4*z^2 + z
            sage: pep.roots(QQbar)
            [(-6.626418492719221?, 1),
             (0, 1),
             (0.3132092463596102? - 0.2298065541510677?*I, 1),
             (0.3132092463596102? + 0.2298065541510677?*I, 1)]
            sage: pep.roots(AA)
            [(-6.626418492719221?, 1), (0, 1)]

        TESTS::

            sage: I = hyperplane_arrangements.Ish(2)
            sage: I.is_central()
            False
            sage: I.primitive_eulerian_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: only defined for central hyperplane arrangements
        """
    def deletion(self, hyperplanes):
        """
        Return the hyperplane arrangement obtained by removing ``h``.

        INPUT:

        - ``h`` -- a hyperplane or hyperplane arrangement

        OUTPUT:

        A new hyperplane arrangement with the given hyperplane(s)
        ``h`` removed.

        .. SEEALSO::

            :meth:`restriction`

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([0,1,0], [1,0,1], [-1,0,1], [0,1,-1], [0,1,1]);  A
            Arrangement of 5 hyperplanes of dimension 2 and rank 2
            sage: A.deletion(x)
            Arrangement <y - 1 | y + 1 | x - y | x + y>
            sage: h = H([0,1,0], [0,1,1])
            sage: A.deletion(h)
            Arrangement <y - 1 | y + 1 | x - y>

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([0,1,0], [1,0,1], [-1,0,1], [0,1,-1], [0,1,1])
            sage: h = H([0,4,0])
            sage: A.deletion(h)
            Arrangement <y - 1 | y + 1 | x - y | x + y>
            sage: l = H([1,2,3])
            sage: A.deletion(l)
            Traceback (most recent call last):
            ...
            ValueError: hyperplane is not in the arrangement

        Checks that deletion preserves the backend::

            sage: H = HyperplaneArrangements(QQ, names='xyz')
            sage: x,y,z = H.gens()
            sage: h1,h2 = [1*x+2*y+3*z, 3*x+2*y+1*z]
            sage: A = H(h1,h2,backend='normaliz')
            sage: A.deletion(h2).backend()
            'normaliz'
        """
    def restriction(self, hyperplane, repetitions: bool = False):
        """
        Return the restriction to a hyperplane.

        INPUT:

        - ``hyperplane`` -- a hyperplane of the hyperplane arrangement

        - ``repetitions`` -- boolean (default: ``False``); eliminate
          repetitions for ordered arrangements

        OUTPUT:

        The restriction `\\mathcal{A}_H` of the
        hyperplane arrangement `\\mathcal{A}` to the given ``hyperplane`` `H`.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: A.<u,x,y,z> = hyperplane_arrangements.braid(4);  A
            Arrangement of 6 hyperplanes of dimension 4 and rank 3
            sage: H = A[0];  H
            Hyperplane 0*u + 0*x + y - z + 0
            sage: R = A.restriction(H); R
            Arrangement <x - z | u - x | u - z>
            sage: A.add_hyperplane(z).restriction(z)
            Arrangement of 6 hyperplanes of dimension 3 and rank 3
            sage: A.add_hyperplane(u).restriction(u)
            Arrangement of 6 hyperplanes of dimension 3 and rank 3
            sage: D = A.deletion(H);  D
            Arrangement of 5 hyperplanes of dimension 4 and rank 3
            sage: ca = A.characteristic_polynomial()
            sage: cr = R.characteristic_polynomial()
            sage: cd = D.characteristic_polynomial()
            sage: ca
            x^4 - 6*x^3 + 11*x^2 - 6*x
            sage: cd - cr
            x^4 - 6*x^3 + 11*x^2 - 6*x

        .. SEEALSO::

            :meth:`deletion`

        TESTS:

        Checks that restriction preserves the backend::

            sage: H = HyperplaneArrangements(QQ, names='xyz')
            sage: x,y,z = H.gens()
            sage: h1,h2 = [1*x+2*y+3*z, 3*x+2*y+1*z]
            sage: A = H(h1, h2, backend='normaliz')
            sage: A.restriction(h2).backend()
            'normaliz'
        """
    def change_ring(self, base_ring):
        """
        Return hyperplane arrangement over the new base ring.

        INPUT:

        - ``base_ring`` -- the new base ring; must be a field for
          hyperplane arrangements

        OUTPUT:

        The hyperplane arrangement obtained by changing the base
        field, as a new hyperplane arrangement.

        .. WARNING::

            While there is often a one-to-one correspondence between the
            hyperplanes of ``self`` and those of
            ``self.change_ring(base_ring)``, there is
            no guarantee that the order in which they appear in
            ``self.hyperplanes()`` will match the order in which their
            counterparts in ``self.cone()`` will appear in
            ``self.change_ring(base_ring).hyperplanes()``!

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([(1,1), 0], [(2,3), -1])
            sage: A.change_ring(FiniteField(2))
            Arrangement <y + 1 | x + y>

        TESTS:

        Checks that changing the ring preserves the backend::

            sage: H = HyperplaneArrangements(QQ, names='xyz')
            sage: x,y,z = H.gens()
            sage: h1, h2 = [1*x+2*y+3*z, 3*x+2*y+1*z]
            sage: A = H(h1, h2, backend='normaliz')
            sage: A.change_ring(RDF).backend()
            'normaliz'
        """
    @cached_method
    def n_regions(self):
        """
        The number of regions of the hyperplane arrangement.

        OUTPUT: integer

        EXAMPLES::

            sage: A = hyperplane_arrangements.semiorder(3)
            sage: A.n_regions()
            19

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([(1,1), 0], [(2,3), -1], [(4,5), 3])
            sage: B = A.change_ring(FiniteField(7))
            sage: B.n_regions()
            Traceback (most recent call last):
            ...
            TypeError: base field must have characteristic zero

        Check that :issue:`30749` is fixed::

            sage: # needs sage.rings.number_field
            sage: R.<y> = QQ[]
            sage: v1 = AA.polynomial_root(AA.common_polynomial(y^2 - 3),
            ....:                         RIF(RR(1.7320508075688772), RR(1.7320508075688774)))
            sage: v2 = QQbar.polynomial_root(AA.common_polynomial(y^4 - y^2 + 1),
            ....:                            CIF(RIF(RR(0.8660254037844386), RR(0.86602540378443871)),
            ....:                                RIF(-RR(0.50000000000000011), -RR(0.49999999999999994))))
            sage: my_vectors = (vector(AA, [-v1, -1, 1]), vector(AA, [0, 2, 1]), vector(AA, [v1, -1, 1]),
            ....:               vector(AA, [1, 0, 0]), vector(AA, [1/2, AA(-1/2*v2^3 + v2),0]),
            ....:               vector(AA, [-1/2, AA(-1/2*v2^3 + v2), 0]))
            sage: H = HyperplaneArrangements(AA, names='xyz')
            sage: x,y,z = H.gens()
            sage: A = H(backend='normaliz')                                     # optional - pynormaliz
            sage: for v in my_vectors:                                          # optional - pynormaliz
            ....:     a, b, c = v
            ....:     A = A.add_hyperplane(a*x + b*y + c*z)
            sage: A.n_regions()                                                 # optional - pynormaliz
            24
        """
    @cached_method
    def n_bounded_regions(self):
        """
        Return the number of (relatively) bounded regions.

        OUTPUT:

        An integer. The number of relatively bounded regions of the
        hyperplane arrangement.

        EXAMPLES::

            sage: A = hyperplane_arrangements.semiorder(3)
            sage: A.n_bounded_regions()
            7

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([(1,1),0], [(2,3),-1], [(4,5),3])
            sage: B = A.change_ring(FiniteField(7))
            sage: B.n_bounded_regions()
            Traceback (most recent call last):
            ...
            TypeError: base field must have characteristic zero
        """
    def has_good_reduction(self, p) -> bool:
        """
        Return whether the hyperplane arrangement has good reduction mod `p`.

        Let `A` be a hyperplane arrangement with equations defined
        over the integers, and let `B` be the hyperplane arrangement
        defined by reducing these equations modulo a prime `p`.  Then
        `A` has good reduction modulo `p` if the intersection posets
        of `A` and `B` are isomorphic.

        INPUT:

        - ``p`` -- prime number

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.combinat
            sage: a = hyperplane_arrangements.semiorder(3)
            sage: a.has_good_reduction(5)
            True
            sage: a.has_good_reduction(3)
            False
            sage: b = a.change_ring(GF(3))
            sage: a.characteristic_polynomial()
            x^3 - 6*x^2 + 12*x
            sage: b.characteristic_polynomial()  # not equal to that for a
            x^3 - 6*x^2 + 10*x
        """
    def is_linear(self):
        """
        Test whether all hyperplanes pass through the origin.

        OUTPUT: boolean

        EXAMPLES::

            sage: a = hyperplane_arrangements.semiorder(3)
            sage: a.is_linear()
            False
            sage: b = hyperplane_arrangements.braid(3)                                  # needs sage.graphs
            sage: b.is_linear()                                                         # needs sage.graphs
            True

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: c = H(x+1, y+1)
            sage: c.is_linear()
            False
            sage: c.is_central()
            True
        """
    def is_essential(self):
        """
        Test whether the hyperplane arrangement is essential.

        A hyperplane arrangement is essential if the span of the normals
        of its hyperplanes spans the ambient space.

        .. SEEALSO::

            :meth:`essentialization`

        OUTPUT: boolean

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: H(x, x+1).is_essential()
            False
            sage: H(x, y).is_essential()
            True
        """
    @cached_method
    def is_central(self, certificate: bool = False):
        """
        Test whether the intersection of all the hyperplanes is nonempty.

        A hyperplane arrangement is central if the intersection of all the
        hyperplanes in the arrangement is nonempty.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return the center as a polyhedron (possibly empty) as part
          of the output

        OUTPUT: if ``certificate`` is ``True``, returns a tuple containing:

        1. A boolean
        2. The polyhedron defined to be the intersection of all the hyperplanes

        If ``certificate`` is ``False``, returns a boolean.

        EXAMPLES::

            sage: a = hyperplane_arrangements.braid(2)                                  # needs sage.graphs
            sage: a.is_central()                                                        # needs sage.graphs
            True

        The Catalan arrangement in dimension 3 is not central::

            sage: b = hyperplane_arrangements.Catalan(3)
            sage: b.is_central(certificate=True)
            (False, The empty polyhedron in QQ^3)

        The empty arrangement in dimension 5 is central::

            sage: H = HyperplaneArrangements(QQ, names=tuple(['x'+str(i) for i in range(7)]))
            sage: c = H()
            sage: c.is_central(certificate=True)
            (True, A 7-dimensional polyhedron in QQ^7 defined
                   as the convex hull of 1 vertex and 7 lines)
        """
    def center(self):
        """
        Return the center of the hyperplane arrangement.

        The polyhedron defined to be the set of all points in the
        ambient space of the arrangement that lie on all of the
        hyperplanes.

        OUTPUT: a polyhedron

        EXAMPLES:

        The empty hyperplane arrangement has the entire ambient space as its
        center::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H()
            sage: A.center()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 lines

        The Shi arrangement in dimension 3 has an empty center::

            sage: A = hyperplane_arrangements.Shi(3)
            sage: A.center()
            The empty polyhedron in QQ^3

        The Braid arrangement in dimension 3 has a center that is neither
        empty nor full-dimensional::

            sage: A = hyperplane_arrangements.braid(3)                                  # needs sage.combinat
            sage: A.center()                                                            # needs sage.combinat
            A 1-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex and 1 line
        """
    @cached_method
    def is_simplicial(self):
        """
        Test whether the arrangement is simplicial.

        A region is simplicial if the normal vectors of its bounding hyperplanes
        are linearly independent. A hyperplane arrangement is said to be
        simplicial if every region is simplicial.

        OUTPUT: boolean; whether the hyperplane arrangement is simplicial

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = H([[0,1,1,1], [0,1,2,3]])
            sage: A.is_simplicial()
            True
            sage: A = H([[0,1,1,1], [0,1,2,3], [0,1,3,2]])
            sage: A.is_simplicial()
            True
            sage: A = H([[0,1,1,1], [0,1,2,3], [0,1,3,2], [0,2,1,3]])
            sage: A.is_simplicial()
            False
            sage: hyperplane_arrangements.braid(3).is_simplicial()                      # needs sage.graphs
            True
        """
    @cached_method
    def essentialization(self):
        """
        Return the essentialization of the hyperplane arrangement.

        The essentialization of a hyperplane arrangement whose base field
        has characteristic 0 is obtained by intersecting the hyperplanes by
        the space spanned by their normal vectors.

        OUTPUT:

        The essentialization `\\mathcal{A}'` of `\\mathcal{A}` as a
        new hyperplane arrangement.

        EXAMPLES::

            sage: a = hyperplane_arrangements.braid(3)                                  # needs sage.graphs
            sage: a.is_essential()                                                      # needs sage.graphs
            False
            sage: a.essentialization()                                                  # needs sage.graphs
            Arrangement <t1 - t2 | t1 + 2*t2 | 2*t1 + t2>

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: B = H([(1,0),1], [(1,0),-1])
            sage: B.is_essential()
            False
            sage: B.essentialization()
            Arrangement <-x + 1 | x + 1>
            sage: B.essentialization().parent()
            Hyperplane arrangements in 1-dimensional linear space over
            Rational Field with coordinate x

            sage: H.<x,y> = HyperplaneArrangements(GF(2))
            sage: C = H([(1,1),1], [(1,1),0])
            sage: C.essentialization()
            Arrangement <y | y + 1>

            sage: h = hyperplane_arrangements.semiorder(4)
            sage: h.essentialization()
            Arrangement of 12 hyperplanes of dimension 3 and rank 3

        TESTS::

            sage: b = hyperplane_arrangements.coordinate(2)
            sage: b.is_essential()
            True
            sage: b.essentialization() is b
            True
        """
    def sign_vector(self, p):
        """
        Indicates on which side of each hyperplane the given
        point `p` lies.

        The base field must have characteristic zero.

        INPUT:

        - ``p`` -- point as a list/tuple/iterable

        OUTPUT:

        A vector whose entries are in `[-1, 0, +1]`.

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([(1,0), 0], [(0,1), 1]);  A
            Arrangement <y + 1 | x>
            sage: A.sign_vector([2, -2])
            (-1, 1)
            sage: A.sign_vector((-1, -1))
            (0, -1)

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(GF(3))
            sage: A = H(x, y)
            sage: A.sign_vector([1, 2])
            Traceback (most recent call last):
            ...
            ValueError: characteristic must be zero
        """
    def face_vector(self):
        """
        Return the face vector.

        OUTPUT: a vector of integers

        The `d`-th entry is the number of faces of dimension `d`.  A
        *face* is the intersection of a region with a hyperplane of
        the arrangement.

        EXAMPLES::

            sage: A = hyperplane_arrangements.Shi(3)
            sage: A.face_vector()                                                       # needs sage.combinat
            (0, 6, 21, 16)
        """
    def vertices(self, exclude_sandwiched: bool = False):
        """
        Return the vertices.

        The vertices are the zero-dimensional faces, see
        :meth:`face_vector`.

        INPUT:

        - ``exclude_sandwiched`` -- boolean (default:
          ``False``). Whether to exclude hyperplanes that are
          sandwiched between parallel hyperplanes. Useful if you only
          need the convex hull.

        OUTPUT:

        The vertices in a sorted tuple. Each vertex is returned as a
        vector in the ambient vector space.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.Shi(3).essentialization()
            sage: A.dimension()
            2
            sage: A.face_vector()
            (6, 21, 16)
            sage: A.vertices()
            ((-2/3, 1/3), (-1/3, -1/3), (0, -1), (0, 0), (1/3, -2/3), (2/3, -1/3))
            sage: point2d(A.vertices(), size=20) + A.plot()                             # needs sage.plot
            Graphics object consisting of 7 graphics primitives

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: chessboard = []
            sage: N = 8
            sage: for x0 in range(N + 1):
            ....:     for y0 in range(N + 1):
            ....:         chessboard.extend([x-x0, y-y0])
            sage: chessboard = H(chessboard)
            sage: len(chessboard.vertices())
            81
            sage: chessboard.vertices(exclude_sandwiched=True)
            ((0, 0), (0, 8), (8, 0), (8, 8))
        """
    @cached_method
    def regions(self):
        """
        Return the regions of the hyperplane arrangement.

        The base field must have characteristic zero.

        OUTPUT: a tuple containing the regions as polyhedra

        The regions are the connected components of the complement of
        the union of the hyperplanes as a subset of `\\RR^n`.

        EXAMPLES::

            sage: a = hyperplane_arrangements.braid(2)                                  # needs sage.graphs
            sage: a.regions()                                                           # needs sage.graphs
            (A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex, 1 ray, 1 line,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex, 1 ray, 1 line)

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H(x, y+1)
            sage: A.regions()
            (A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays)

            sage: chessboard = []
            sage: N = 8
            sage: for x0 in range(N + 1):
            ....:     for y0 in range(N + 1):
            ....:         chessboard.extend([x-x0, y-y0])
            sage: chessboard = H(chessboard)
            sage: len(chessboard.bounded_regions())   # long time, 359 ms on a Core i7
            64

        Example 6 of [KP2020]_::

            sage: from itertools import product
            sage: def zero_one(d):
            ....:     for x in product([0,1], repeat=d):
            ....:         if any(x):
            ....:             yield [0] + list(x)

            sage: K.<x,y> = HyperplaneArrangements(QQ)
            sage: A = K(*zero_one(2))
            sage: len(A.regions())
            6
            sage: K.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = K(*zero_one(3))
            sage: len(A.regions())
            32
            sage: K.<x,y,z,w> = HyperplaneArrangements(QQ)
            sage: A = K(*zero_one(4))
            sage: len(A.regions())
            370
            sage: K.<x,y,z,w,r> = HyperplaneArrangements(QQ)
            sage: A = K(*zero_one(5))
            sage: len(A.regions())            # not tested (~25s)
            11292

        It is possible to specify the backend::

            sage: # needs sage.rings.number_field
            sage: K.<q> = CyclotomicField(9)
            sage: L.<r9> = NumberField((q + q**(-1)).minpoly(),
            ....:                      embedding=AA(q + q**-1))
            sage: norms = [[1, 1/3*(-2*r9**2-r9+1), 0],
            ....:          [1, -r9**2 - r9, 0],
            ....:          [1, -r9**2 + 1, 0],
            ....:          [1, -r9**2, 0],
            ....:          [1, r9**2 - 4, -r9**2+3]]
            sage: H.<x,y,z> = HyperplaneArrangements(L)
            sage: A = H(backend='normaliz')
            sage: for v in norms:
            ....:     a,b,c = v
            ....:     A = A.add_hyperplane(a*x + b*y + c*z)
            sage: R = A.regions()                                       # optional - pynormaliz
            sage: R[0].backend()                                        # optional - pynormaliz
            'normaliz'

        TESTS::

            sage: K.<x,y,z,w,r> = HyperplaneArrangements(QQ)
            sage: A = K()
            sage: A.regions()
            (A 5-dimensional polyhedron in QQ^5
                 defined as the convex hull of 1 vertex and 5 lines,)
        """
    @cached_method
    def poset_of_regions(self, B=None, numbered_labels: bool = True):
        """
        Return the poset of regions for a central hyperplane arrangement.

        The poset of regions is a partial order on the set of regions
        where the regions are ordered by `R\\leq R'` if and only if
        `S(R) \\subseteq S(R')` where `S(R)` is the set of hyperplanes which
        separate the region `R` from the base region `B`.

        INPUT:

        - ``B`` -- a region (optional); if ``None``, then
          an arbitrary region is chosen as the base region

        - ``numbered_labels`` -- boolean (default: ``True``); if ``True``,
          then the elements of the poset are numbered. Else they are labelled
          with the regions themselves.

        OUTPUT: a Poset object containing the poset of regions

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = H([[0,1,1,1], [0,1,2,3]])
            sage: A.poset_of_regions()                                                  # needs sage.combinat
            Finite poset containing 4 elements

            sage: # needs sage.combinat sage.graphs
            sage: A = hyperplane_arrangements.braid(3)
            sage: A.poset_of_regions()
            Finite poset containing 6 elements
            sage: A.poset_of_regions(numbered_labels=False)
            Finite poset containing 6 elements
            sage: A = hyperplane_arrangements.braid(4)
            sage: A.poset_of_regions()
            Finite poset containing 24 elements

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = H([[0,1,1,1], [0,1,2,3], [0,1,3,2], [0,2,1,3]])
            sage: R = A.regions()
            sage: base_region = R[3]
            sage: A.poset_of_regions(B=base_region)                                     # needs sage.combinat
            Finite poset containing 14 elements
        """
    @cached_method
    def closed_faces(self, labelled: bool = True):
        """
        Return the closed faces of the hyperplane arrangement ``self``
        (provided that ``self`` is defined over a totally ordered field).

        Let `\\mathcal{A}` be a hyperplane arrangement in the vector
        space `K^n`, whose hyperplanes are the zero sets of the
        affine-linear functions `u_1, u_2, \\ldots, u_N`. (We consider
        these functions `u_1, u_2, \\ldots, u_N`, and not just the
        hyperplanes, as given. We also assume the field `K` to be
        totally ordered.) For any point `x \\in K^n`, we define the
        *sign vector* of `x` to be the vector
        `(v_1, v_2, \\ldots, v_N) \\in \\{-1, 0, 1\\}^N` such that (for each
        `i`) the number `v_i` is the sign of `u_i(x)`. For any
        `v \\in \\{-1, 0, 1\\}^N`, we let `F_v` be the set of all `x \\in K^n`
        which have sign vector `v`. The nonempty ones among all these
        subsets `F_v` are called the *open faces* of `\\mathcal{A}`. They
        form a partition of the set `K^n`.

        Furthermore, for any
        `v = (v_1, v_2, \\ldots, v_N) \\in \\{-1, 0, 1\\}^N`, we let `G_v` be
        the set of all `x \\in K^n` such that, for every `i`, the sign of
        `u_i(x)` is either `0` or `v_i`.
        Then, `G_v` is a polyhedron. The nonempty ones among all these
        polyhedra `G_v` are called the *closed faces* of `\\mathcal{A}`.
        While several sign vectors `v` can lead to one and the same
        closed face `G_v`, we can assign to every closed face a canonical
        choice of a sign vector: Namely, if `G` is a closed face of
        `\\mathcal{A}`, then the *sign vector* of `G` is defined to be the
        vector `(v_1, v_2, \\ldots, v_N) \\in \\{-1, 0, 1\\}^N` where `x` is
        any point in the relative interior of `G` and where, for each `i`,
        the number `v_i` is the sign of `u_i(x)`. (This does not depend on
        the choice of `x`.)

        There is a one-to-one correspondence between the closed faces and
        the open faces of `\\mathcal{A}`. It sends a closed face `G` to
        the open face `F_v`, where `v` is the sign vector of `G`; this
        `F_v` is also the relative interior of `G_v`. The inverse map
        sends any open face `O` to the closure of `O`.

        INPUT:

        - ``labelled`` -- boolean (default: ``True``); if ``True``, then
          this method returns not the faces itself but rather pairs
          `(v, F)` where `F` is a closed face and `v` is its sign vector
          (here, the order and the orientation of the
          `u_1, u_2, \\ldots, u_N` is as given by ``self.hyperplanes()``).

        OUTPUT:

        A tuple containing the closed faces as polyhedra, or (if
        ``labelled`` is set to ``True``) the pairs of sign vectors and
        corresponding closed faces.

        .. TODO::

            Should the output rather be a dictionary where the keys are
            the sign vectors and the values are the faces?

        EXAMPLES::

            sage: # needs sage.graphs
            sage: a = hyperplane_arrangements.braid(2)
            sage: a.hyperplanes()
            (Hyperplane t0 - t1 + 0,)
            sage: a.closed_faces()
            (((0,),  A 1-dimensional polyhedron in QQ^2 defined
                     as the convex hull of 1 vertex and 1 line),
             ((1,),  A 2-dimensional polyhedron in QQ^2 defined
                     as the convex hull of 1 vertex, 1 ray, 1 line),
             ((-1,), A 2-dimensional polyhedron in QQ^2 defined
                     as the convex hull of 1 vertex, 1 ray, 1 line))
            sage: a.closed_faces(labelled=False)
            (A 1-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 1 line,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex, 1 ray, 1 line,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex, 1 ray, 1 line)
            sage: [(v, F, F.representative_point()) for v, F in a.closed_faces()]
            [((0,),  A 1-dimensional polyhedron in QQ^2 defined
                     as the convex hull of 1 vertex and 1 line,      (0, 0)),
             ((1,),  A 2-dimensional polyhedron in QQ^2 defined
                     as the convex hull of 1 vertex, 1 ray, 1 line,  (0, -1)),
             ((-1,), A 2-dimensional polyhedron in QQ^2 defined
                     as the convex hull of 1 vertex, 1 ray, 1 line,  (-1, 0))]

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: a = H(x, y+1)
            sage: a.hyperplanes()
            (Hyperplane 0*x + y + 1, Hyperplane x + 0*y + 0)
            sage: [(v, F, F.representative_point()) for v, F in a.closed_faces()]
            [((0, 0),   A 0-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex,             (0, -1)),
             ((0, 1),   A 1-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 1 ray,   (1, -1)),
             ((0, -1),  A 1-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 1 ray,   (-1, -1)),
             ((1, 0),   A 1-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 1 ray,   (0, 0)),
             ((1, 1),   A 2-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 2 rays,  (1, 0)),
             ((1, -1),  A 2-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 2 rays,  (-1, 0)),
             ((-1, 0),  A 1-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 1 ray,   (0, -2)),
             ((-1, 1),  A 2-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 2 rays,  (1, -2)),
             ((-1, -1), A 2-dimensional polyhedron in QQ^2 defined
                        as the convex hull of 1 vertex and 2 rays,  (-1, -2))]

            sage: # needs sage.graphs
            sage: a = hyperplane_arrangements.braid(3)
            sage: a.hyperplanes()
            (Hyperplane 0*t0 + t1 - t2 + 0,
             Hyperplane t0 - t1 + 0*t2 + 0,
             Hyperplane t0 + 0*t1 - t2 + 0)
            sage: [(v, F, F.representative_point()) for v, F in a.closed_faces()]
            [((0, 0, 0),    A 1-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex and 1 line,      (0, 0, 0)),
             ((0, 1, 1),    A 2-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 1 ray, 1 line,  (0, -1, -1)),
             ((0, -1, -1),  A 2-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 1 ray, 1 line,  (-1, 0, 0)),
             ((1, 0, 1),    A 2-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 1 ray, 1 line,  (1, 1, 0)),
             ((1, 1, 1),    A 3-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 2 rays, 1 line, (0, -1, -2)),
             ((1, -1, 0),   A 2-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 1 ray, 1 line,  (-1, 0, -1)),
             ((1, -1, 1),   A 3-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 2 rays, 1 line, (1, 2, 0)),
             ((1, -1, -1),  A 3-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 2 rays, 1 line, (-2, 0, -1)),
             ((-1, 0, -1),  A 2-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 1 ray, 1 line,  (0, 0, 1)),
             ((-1, 1, 0),   A 2-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 1 ray, 1 line,  (1, 0, 1)),
             ((-1, 1, 1),   A 3-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 2 rays, 1 line, (0, -2, -1)),
             ((-1, 1, -1),  A 3-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 2 rays, 1 line, (1, 0, 2)),
             ((-1, -1, -1), A 3-dimensional polyhedron in QQ^3 defined
                            as the convex hull of 1 vertex, 2 rays, 1 line, (-1, 0, 1))]

        Let us check that the number of closed faces with a given
        dimension computed using ``self.closed_faces()`` equals the one
        computed using :meth:`face_vector`::

            sage: def test_number(a):
            ....:     Qx = PolynomialRing(QQ, 'x'); x = Qx.gen()
            ....:     RHS = Qx.sum(vi * x ** i for i, vi in enumerate(a.face_vector()))
            ....:     LHS = Qx.sum(x ** F[1].dim() for F in a.closed_faces())
            ....:     return LHS == RHS
            sage: a = hyperplane_arrangements.Catalan(2)
            sage: test_number(a)                                                        # needs sage.combinat
            True
            sage: a = hyperplane_arrangements.Shi(3)
            sage: test_number(a)                # long time                             # needs sage.combinat
            True

        TESTS:

        An empty border case::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: a = H()
            sage: a.closed_faces()
            (((),
              A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 lines),)
        """
    def face_product(self, F, G, normalize: bool = True):
        """
        Return the product `FG` in the face semigroup of ``self``, where
        `F` and `G` are two closed faces of ``self``.

        The face semigroup of a hyperplane arrangement `\\mathcal{A}` is
        defined as follows: As a set, it is the set of all open faces
        of ``self`` (see :meth:`closed_faces`). Its product is defined by
        the following rule: If `F` and `G` are two open faces of
        `\\mathcal{A}`, then `FG` is an open face of `\\mathcal{A}`, and
        for every hyperplane `H \\in \\mathcal{A}`, the open face `FG` lies
        on the same side of `H` as `F` unless `F \\subseteq H`, in which
        case `FG` lies on the same side of `H` as `G`. Alternatively,
        `FG` can be defined as follows: If `f` and `g` are two points in
        `F` and `G`, respectively, then `FG` is the face that contains
        the point `(f + \\varepsilon g) / (1 + \\varepsilon)` for any
        sufficiently small positive `\\varepsilon`.

        In our implementation, the face semigroup consists of closed faces
        rather than open faces (thanks to the 1-to-1 correspondence
        between open faces and closed faces, this is not really a
        different semigroup); these closed faces are given as polyhedra.

        The face semigroup of a hyperplane arrangement is always a
        left-regular band (i.e., a semigroup satisfying the identities
        `x^2 = x` and `xyx = xy`). When the arrangement is central, then
        this semigroup is a monoid. See [Br2000]_ (Appendix A in
        particular) for further properties.

        INPUT:

        - ``F``, ``G`` -- two faces of ``self`` (as polyhedra)

        - ``normalize`` -- boolean (default: ``True``); if ``True``, then
          this method returns the precise instance of `FG` in the list
          returned by ``self.closed_faces()``, rather than creating a new
          instance

        EXAMPLES::

            sage: # needs sage.graphs
            sage: a = hyperplane_arrangements.braid(3)
            sage: a.hyperplanes()
            (Hyperplane 0*t0 + t1 - t2 + 0,
             Hyperplane t0 - t1 + 0*t2 + 0,
             Hyperplane t0 + 0*t1 - t2 + 0)
            sage: faces = {F0: F1 for F0, F1 in a.closed_faces()}
            sage: xGyEz = faces[(0, 1, 1)]   # closed face x >= y = z
            sage: xGyEz.representative_point()
            (0, -1, -1)
            sage: xGyEz = faces[(0, 1, 1)]   # closed face x >= y = z
            sage: xGyEz.representative_point()
            (0, -1, -1)
            sage: yGxGz = faces[(1, -1, 1)]  # closed face y >= x >= z
            sage: xGyGz = faces[(1, 1, 1)]   # closed face x >= y >= z
            sage: a.face_product(xGyEz, yGxGz) == xGyGz
            True
            sage: a.face_product(yGxGz, xGyEz) == yGxGz
            True
            sage: xEzGy = faces[(-1, 1, 0)]  # closed face x = z >= y
            sage: xGzGy = faces[(-1, 1, 1)]  # closed face x >= z >= y
            sage: a.face_product(xEzGy, yGxGz) == xGzGy
            True
        """
    def face_semigroup_algebra(self, field=None, names: str = 'e'):
        """
        Return the face semigroup algebra of ``self``.

        This is the semigroup algebra of the face semigroup of ``self``
        (see :meth:`face_product` for the definition of the semigroup).

        Due to limitations of the current Sage codebase (e.g., semigroup
        algebras do not profit from the functionality of the
        :class:`FiniteDimensionalAlgebra` class), this is implemented not
        as a semigroup algebra, but as a
        :class:`FiniteDimensionalAlgebra`. The closed faces of ``self``
        (in the order in which the :meth:`closed_faces` method outputs
        them) are identified with the vectors `(0, 0, \\ldots, 0, 1, 0, 0,
        \\ldots, 0)` (with the `1` moving from left to right).

        INPUT:

        - ``field`` -- a field (default: `\\QQ`), to be used as the
          base ring for the algebra (can also be a commutative ring, but
          then certain representation-theoretical methods might misbehave)

        - ``names`` -- (default: ``'e'``) string; names for the basis
          elements of the algebra

        .. TODO::

            Also implement it as an actual semigroup algebra?

        EXAMPLES::

            sage: # needs sage.graphs
            sage: a = hyperplane_arrangements.braid(3)
            sage: [(i, F[0]) for i, F in enumerate(a.closed_faces())]
            [(0, (0, 0, 0)),
             (1, (0, 1, 1)),
             (2, (0, -1, -1)),
             (3, (1, 0, 1)),
             (4, (1, 1, 1)),
             (5, (1, -1, 0)),
             (6, (1, -1, 1)),
             (7, (1, -1, -1)),
             (8, (-1, 0, -1)),
             (9, (-1, 1, 0)),
             (10, (-1, 1, 1)),
             (11, (-1, 1, -1)),
             (12, (-1, -1, -1))]
            sage: U = a.face_semigroup_algebra(); U
            Finite-dimensional algebra of degree 13 over Rational Field
            sage: e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = U.basis()
            sage: e0 * e1
            e1
            sage: e0 * e5
            e5
            sage: e5 * e0
            e5
            sage: e3 * e2
            e6
            sage: e7 * e12
            e7
            sage: e3 * e12
            e6
            sage: e4 * e8
            e4
            sage: e8 * e4
            e11
            sage: e8 * e1
            e11
            sage: e5 * e12
            e7
            sage: (e3 + 2*e4) * (e1 - e7)
            e4 - e6

            sage: U3 = a.face_semigroup_algebra(field=GF(3)); U3                        # needs sage.graphs sage.rings.finite_rings
            Finite-dimensional algebra of degree 13 over Finite Field of size 3

        TESTS:

        The ``names`` keyword works::

            sage: # needs sage.graphs
            sage: a = hyperplane_arrangements.braid(3)
            sage: U = a.face_semigroup_algebra(names='x'); U
            Finite-dimensional algebra of degree 13 over Rational Field
            sage: e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = U.basis()
            sage: e0 * e1
            x1
        """
    def region_containing_point(self, p):
        """
        The region in the hyperplane arrangement containing a given point.

        The base field must have characteristic zero.

        INPUT:

        - ``p`` -- point

        OUTPUT:

        A polyhedron. A :exc:`ValueError` is raised if the point is not
        interior to a region, that is, sits on a hyperplane.

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: A = H([(1,0), 0], [(0,1), 1], [(0,1), -1], [(1,-1), 0], [(1,1), 0])
            sage: A.region_containing_point([1,2])
            A 2-dimensional polyhedron in QQ^2 defined
            as the convex hull of 2 vertices and 2 rays

        TESTS::

            sage: A = H([(1,1),0], [(2,3),-1], [(4,5),3])
            sage: B = A.change_ring(FiniteField(7))
            sage: B.region_containing_point((1,2))
            Traceback (most recent call last):
            ...
            ValueError: base field must have characteristic zero

            sage: A = H([(1,1),0], [(2,3),-1], [(4,5),3])
            sage: A.region_containing_point((1,-1))
            Traceback (most recent call last):
            ...
            ValueError: point sits on a hyperplane
        """
    def bounded_regions(self):
        """
        Return the relatively bounded regions of the arrangement.

        A region is relatively bounded if its intersection with the space
        spanned by the normals to the hyperplanes is bounded. This is the
        same as being bounded in the case that the hyperplane arrangement
        is essential. It is assumed that the arrangement is defined over
        the rationals.

        OUTPUT:

        Tuple of polyhedra. The relatively bounded regions of the
        arrangement.

        .. SEEALSO::

            :meth:`unbounded_regions`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.semiorder(3)
            sage: A.bounded_regions()
            (A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 3 vertices and 1 line,
             A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 3 vertices and 1 line,
             A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 3 vertices and 1 line,
             A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 6 vertices and 1 line,
             A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 3 vertices and 1 line,
             A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 3 vertices and 1 line,
             A 3-dimensional polyhedron in QQ^3 defined
                 as the convex hull of 3 vertices and 1 line)
            sage: A.bounded_regions()[0].is_compact()    # the regions are only *relatively* bounded
            False
            sage: A.is_essential()
            False
        """
    def unbounded_regions(self):
        """
        Return the relatively bounded regions of the arrangement.

        OUTPUT:

        Tuple of polyhedra. The regions of the arrangement that are not
        relatively bounded.  It is assumed that the arrangement is
        defined over the rationals.

        .. SEEALSO::

            :meth:`bounded_regions`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.semiorder(3)
            sage: B = A.essentialization()
            sage: B.n_regions() - B.n_bounded_regions()
            12
            sage: B.unbounded_regions()
            (A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 3 vertices and 1 ray,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 3 vertices and 1 ray,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 3 vertices and 1 ray,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 3 vertices and 1 ray,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                as the convex hull of 3 vertices and 1 ray,
             A 2-dimensional polyhedron in QQ^2 defined
                as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 3 vertices and 1 ray,
             A 2-dimensional polyhedron in QQ^2 defined
                as the convex hull of 1 vertex and 2 rays,
             A 2-dimensional polyhedron in QQ^2 defined
                 as the convex hull of 1 vertex and 2 rays)
        """
    @cached_method
    def whitney_data(self):
        """
        Return the Whitney numbers.

        .. SEEALSO::

            :meth:`whitney_number`,
            :meth:`doubly_indexed_whitney_number`

        OUTPUT:

        A pair of integer matrices. The two matrices are the
        doubly-indexed Whitney numbers of the first or second kind,
        respectively. The `i,j`-th entry is the `i,j`-th
        doubly-indexed Whitney number.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.Shi(3)
            sage: A.whitney_data()
            (
            [  1  -6   9]  [ 1  6  6]
            [  0   6 -15]  [ 0  6 15]
            [  0   0   6], [ 0  0  6]
            )
        """
    def doubly_indexed_whitney_number(self, i, j, kind: int = 1):
        """
        Return the `i,j`-th  doubly-indexed Whitney number.

        If ``kind=1``, this number is obtained by adding the Möbius function
        values `mu(x,y)` over all `x, y` in the intersection poset with
        `\\mathrm{rank}(x) = i` and `\\mathrm{rank}(y) = j`.

        If `kind=2`, this number is the number of elements `x,y` in the
        intersection poset such that `x \\leq y` with ranks `i` and `j`,
        respectively.

        INPUT:

        - ``i``, ``j`` -- integers

        - ``kind`` -- (default: 1) 1 or 2

        OUTPUT:

        Integer. The `(i,j)`-th entry of the ``kind`` Whitney number.

        .. SEEALSO::

            :meth:`whitney_number`,
            :meth:`whitney_data`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.Shi(3)
            sage: A.doubly_indexed_whitney_number(0, 2)
            9
            sage: A.whitney_number(2)
            9
            sage: A.doubly_indexed_whitney_number(1, 2)
            -15

        REFERENCES:

        - [GZ1983]_
        """
    def whitney_number(self, k, kind: int = 1):
        """
        Return the ``k``-th Whitney number.

        If ``kind=1``, this number is obtained by summing the Möbius function
        values `mu(0, x)` over all `x` in the intersection poset with
        `\\mathrm{rank}(x) = k`.

        If ``kind=2``, this number is the number of elements `x, y` in the
        intersection poset such that `x \\leq y` with ranks `i` and `j`,
        respectively.

        See [GZ1983]_ for more details.

        INPUT:

        - ``k`` -- integer

        - ``kind`` -- 1 or 2 (default: 1)

        OUTPUT:

        Integer. The ``k``-th Whitney number.

        .. SEEALSO::

            :meth:`doubly_indexed_whitney_number`
            :meth:`whitney_data`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = hyperplane_arrangements.Shi(3)
            sage: A.whitney_number(0)
            1
            sage: A.whitney_number(1)
            -6
            sage: A.whitney_number(2)
            9
            sage: A.characteristic_polynomial()
            x^3 - 6*x^2 + 9*x
            sage: A.whitney_number(1, kind=2)
            6
            sage: p = A.intersection_poset()
            sage: r = p.rank_function()
            sage: len([i for i in p if r(i) == 1])
            6
        """
    def is_separating_hyperplane(self, region1, region2, hyperplane):
        """
        Test whether the ``hyperplane`` separates the given regions.

        INPUT:

        - ``region1``, ``region2`` -- polyhedra or list/tuple/iterable
          of coordinates which are regions of the arrangement or an interior
          point of a region

        - ``hyperplane`` -- a hyperplane

        OUTPUT: boolean; whether the hyperplane ``hyperplane`` separate the
        given regions

        EXAMPLES::

            sage: A.<x,y> = hyperplane_arrangements.coordinate(2)
            sage: A.is_separating_hyperplane([1,1], [2,1], y)
            False
            sage: A.is_separating_hyperplane([1,1], [-1,1], x)
            True
            sage: r = A.region_containing_point([1,1])
            sage: s = A.region_containing_point([-1,1])
            sage: A.is_separating_hyperplane(r, s, x)
            True
        """
    def distance_between_regions(self, region1, region2):
        """
        Return the number of hyperplanes separating the two regions.

        INPUT:

        - ``region1``, ``region2`` -- regions of the arrangement or
          representative points of regions

        OUTPUT: integer; the number of hyperplanes separating the two regions

        EXAMPLES::

            sage: c = hyperplane_arrangements.coordinate(2)
            sage: r = c.region_containing_point([-1, -1])
            sage: s = c.region_containing_point([1, 1])
            sage: c.distance_between_regions(r, s)
            2
            sage: c.distance_between_regions(s, s)
            0
        """
    def distance_enumerator(self, base_region):
        """
        Return the generating function for the number of hyperplanes
        at given distance.

        INPUT:

        - ``base_region`` -- region of arrangement or point in region

        OUTPUT:

        A polynomial `f(x)` for which the coefficient of `x^i` is the
        number of hyperplanes of distance `i` from ``base_region``,
        i.e., the number of hyperplanes separated by `i` hyperplanes
        from ``base_region``.

        EXAMPLES::

            sage: c = hyperplane_arrangements.coordinate(3)
            sage: c.distance_enumerator(c.region_containing_point([1,1,1]))
            x^3 + 3*x^2 + 3*x + 1
        """
    @cached_method
    def varchenko_matrix(self, names: str = 'h'):
        """
        Return the Varchenko matrix of the arrangement.

        Let `H_1, \\ldots, H_s` and `R_1, \\ldots, R_t` denote the hyperplanes
        and regions, respectively, of the arrangement.  Let `S =
        \\QQ[h_1, \\ldots, h_s]`, a polynomial ring with indeterminate `h_i`
        corresponding to hyperplane `H_i`.  The Varchenko matrix is
        the `t \\times t` matrix with `i,j`-th entry the product of
        those `h_k` such that `H_k` separates `R_i` and `R_j`.

        INPUT:

        - ``names`` -- string or list/tuple/iterable of strings. The
          variable names for the polynomial ring `S`

        OUTPUT: the Varchenko matrix

        EXAMPLES::

            sage: a = hyperplane_arrangements.coordinate(3)
            sage: v = a.varchenko_matrix();  v
            [       1       h2       h1    h1*h2 h0*h1*h2    h0*h1    h0*h2       h0]
            [      h2        1    h1*h2       h1    h0*h1 h0*h1*h2       h0    h0*h2]
            [      h1    h1*h2        1       h2    h0*h2       h0 h0*h1*h2    h0*h1]
            [   h1*h2       h1       h2        1       h0    h0*h2    h0*h1 h0*h1*h2]
            [h0*h1*h2    h0*h1    h0*h2       h0        1       h2       h1    h1*h2]
            [   h0*h1 h0*h1*h2       h0    h0*h2       h2        1    h1*h2       h1]
            [   h0*h2       h0 h0*h1*h2    h0*h1       h1    h1*h2        1       h2]
            [      h0    h0*h2    h0*h1 h0*h1*h2    h1*h2       h1       h2        1]
            sage: factor(det(v))
            (h2 - 1)^4 * (h2 + 1)^4 * (h1 - 1)^4 * (h1 + 1)^4 * (h0 - 1)^4 * (h0 + 1)^4

        TESTS:

        Verify that :issue:`36490` is fixed::

            sage: hyperplane_arrangements.coordinate(1).varchenko_matrix()
            [1 h]
            [h 1]
        """
    @cached_method
    def matroid(self):
        """
        Return the matroid associated to ``self``.

        Let `A` denote a central hyperplane arrangement and `n_H` the
        normal vector of some hyperplane `H \\in A`. We define a matroid
        `M_A` as the linear matroid spanned by `\\{ n_H | H \\in A \\}`.
        The matroid `M_A` is such that the lattice of flats of `M` is
        isomorphic to the intersection lattice of `A`
        (Proposition 3.6 in [Sta2007]_).

        EXAMPLES::

            sage: P.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z)
            sage: M = A.matroid(); M
            Linear matroid of rank 3 on 7 elements represented over the Rational Field

        We check the lattice of flats is isomorphic to the
        intersection lattice::

            sage: f = sum([list(M.flats(i)) for i in range(M.rank() + 1)], [])
            sage: PF = Poset([f, lambda x, y: x < y])                                   # needs sage.combinat
            sage: PF.is_isomorphic(A.intersection_poset())                              # needs sage.combinat
            True
        """
    def orlik_solomon_algebra(self, base_ring=None, ordering=None, **kwds):
        """
        Return the Orlik-Solomon algebra of ``self``.

        INPUT:

        - ``base_ring`` -- (default: the base field of ``self``) the ring
          over which the Orlik-Solomon algebra will be defined
        - ``ordering`` -- (optional) an ordering of the ground set

        EXAMPLES::

            sage: P.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z)
            sage: A.orlik_solomon_algebra()
            Orlik-Solomon algebra of Linear matroid of rank 3 on 7 elements
             represented over the Rational Field
            sage: A.orlik_solomon_algebra(base_ring=ZZ)
            Orlik-Solomon algebra of Linear matroid of rank 3 on 7 elements
             represented over the Rational Field
        """
    def orlik_terao_algebra(self, base_ring=None, ordering=None, **kwds):
        """
        Return the Orlik-Terao algebra of ``self``.

        INPUT:

        - ``base_ring`` -- (default: the base field of ``self``) the ring
          over which the Orlik-Terao algebra will be defined
        - ``ordering`` -- (optional) an ordering of the ground set

        EXAMPLES::

            sage: P.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z)
            sage: A.orlik_terao_algebra()
            Orlik-Terao algebra of Linear matroid of rank 3 on 7 elements
             represented over the Rational Field over Rational Field
            sage: A.orlik_terao_algebra(base_ring=QQ['t'])
            Orlik-Terao algebra of Linear matroid of rank 3 on 7 elements
             represented over the Rational Field
             over Univariate Polynomial Ring in t over Rational Field
        """
    @cached_method
    def minimal_generated_number(self):
        """
        Return the minimum `k` such that ``self`` is `k`-generated.

        Let `A` be a central hyperplane arrangement. Let `W_k` denote
        the solution space of the linear system corresponding to the
        linear dependencies among the hyperplanes of `A` of length at
        most `k`. We say `A` is `k`-*generated* if
        `\\dim W_k = \\operatorname{rank} A`.

        Equivalently this says all dependencies forming the Orlik-Terao
        ideal are generated by at most `k` hyperplanes.

        EXAMPLES:

        We construct Example 2.2 from [Yuz1993]_::

            sage: P.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z, 3*x+5*z, 3*x+4*y+5*z)
            sage: B = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z, x+3*z, x+2*y+3*z)
            sage: A.minimal_generated_number()
            3
            sage: B.minimal_generated_number()
            4

        TESTS:

        Check that :issue:`26705` is fixed::

            sage: # needs sage.combinat sage.groups
            sage: w = WeylGroup(['A', 4]).from_reduced_word([3, 4, 2, 1])
            sage: I = w.inversion_arrangement()
            sage: I
            Arrangement <a4 | a1 | a1 + a2 | a1 + a2 + a3 + a4>
            sage: I.minimal_generated_number()
            0
            sage: I.is_formal()
            True
        """
    def is_formal(self):
        """
        Return if ``self`` is formal.

        A hyperplane arrangement is *formal* if it is 3-generated [Yuz1993]_,
        where `k`-generated is defined in :meth:`minimal_generated_number`.

        EXAMPLES::

            sage: P.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z, 3*x+5*z, 3*x+4*y+5*z)
            sage: B = P(x, y, z, x+y+z, 2*x+y+z, 2*x+3*y+z, 2*x+3*y+4*z, x+3*z, x+2*y+3*z)
            sage: A.is_formal()
            True
            sage: B.is_formal()
            False
        """
    def defining_polynomial(self):
        """
        Return the defining polynomial of ``A``.

        Let `A = (H_i)_i` be a hyperplane arrangement in a vector space `V`
        corresponding to the null spaces of `\\alpha_{H_i} \\in V^*`. Then
        the *defining polynomial* of `A` is given by

        .. MATH::

            Q(A) = \\prod_i \\alpha_{H_i} \\in S(V^*).

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = H([2*x + y - z, -x - 2*y + z])
            sage: p = A.defining_polynomial(); p
            -2*x^2 - 5*x*y - 2*y^2 + 3*x*z + 3*y*z - z^2
            sage: p.factor()
            (-1) * (x + 2*y - z) * (2*x + y - z)
        """
    @cached_method
    def derivation_module_free_chain(self):
        '''
        Return a free chain for the derivation module if one
        exists, otherwise return ``None``.

        .. SEEALSO::

            :meth:`is_free`

        EXAMPLES::

            sage: # needs sage.combinat sage.groups
            sage: W = WeylGroup([\'A\',3], prefix=\'s\')
            sage: A = W.long_element().inversion_arrangement()
            sage: for M in A.derivation_module_free_chain(): print("%s\\n"%M)
            [ 1  0  0]
            [ 0  1  0]
            [ 0  0 a3]
            <BLANKLINE>
            [ 1  0  0]
            [ 0  0  1]
            [ 0 a2  0]
            <BLANKLINE>
            [  1   0   0]
            [  0  -1  -1]
            [  0  a2 -a3]
            <BLANKLINE>
            [ 0  1  0]
            [ 0  0  1]
            [a1  0  0]
            <BLANKLINE>
            [ 1  0 -1]
            [a3 -1  0]
            [a1  0 a2]
            <BLANKLINE>
            [       1        0        0]
            [      a3       -1       -1]
            [       0       a1 -a2 - a3]
            <BLANKLINE>
        '''
    def is_free(self, algorithm: str = 'singular'):
        """
        Return if ``self`` is free.

        A hyperplane arrangement `A` is free if the module
        of derivations `\\operatorname{Der}(A)` is a free `S`-module,
        where `S` is the corresponding symmetric space.

        INPUT:

        - ``algorithm`` -- (default: ``'singular'``) can be one of
          the following:

          * ``'singular'`` -- use Singular's minimal free resolution
          * ``'BC'`` -- use the algorithm given by Barakat and Cuntz
            in [BC2012]_ (much slower than using Singular)

        ALGORITHM:

        .. RUBRIC:: singular

        Check that the minimal free resolution has length at most 2
        by using Singular.

        .. RUBRIC:: BC

        This implementation follows [BC2012]_ by constructing a chain
        of free modules

        .. MATH::

            D(A) = D(A_n) < D(A_{n-1}) < \\cdots < D(A_1) < D(A_0)

        corresponding to some ordering of the arrangements `A_0 \\subset
        A_1 \\subset \\cdots \\subset A_{n-1} \\subset A_n = A`. Such a
        chain is found by using a backtracking algorithm.

        EXAMPLES:

        For type `A` arrangements, chordality is equivalent to freeness.
        We verify that in type `A_3`::

            sage: W = WeylGroup(['A', 3], prefix='s')                                   # needs sage.combinat sage.groups
            sage: for x in W:                                                           # needs sage.combinat sage.groups
            ....:    A = x.inversion_arrangement()
            ....:    assert A.matroid().is_chordal() == A.is_free()

        TESTS:

        We check that the algorithms agree::

            sage: W = WeylGroup(['B', 3], prefix='s')                                   # needs sage.combinat sage.groups
            sage: for x in W:                   # long time                             # needs sage.combinat sage.groups
            ....:    A = x.inversion_arrangement()
            ....:    assert (A.is_free(algorithm='BC')
            ....:            == A.is_free(algorithm='singular'))
        """
    def derivation_module_basis(self, algorithm: str = 'singular'):
        """
        Return a basis for the derivation module of ``self`` if
        one exists, otherwise return ``None``.

        .. SEEALSO::

            :meth:`derivation_module_free_chain`, :meth:`is_free`

        INPUT:

        - ``algorithm`` -- (default: ``'singular'``) can be one of
          the following:

          * ``'singular'`` -- use Singular's minimal free resolution
          * ``'BC'`` -- use the algorithm given by Barakat and Cuntz
            in [BC2012]_ (much slower than using Singular)

        OUTPUT:

        A basis for the derivation module (over `S`, the
        :meth:`symmetric space
        <sage.geometry.hyperplane_arrangement.hyperplane.AmbientVectorSpace.symmetric_space>`)
        as vectors of a free module over `S`.

        ALGORITHM:

        .. RUBRIC:: Singular

        This gets the reduced syzygy module of the Jacobian ideal of
        the defining polynomial `f` of ``self``. It then checks Saito's
        criterion that the determinant of the basis matrix is a scalar
        multiple of `f`. If the basis matrix is not square or it fails
        Saito's criterion, then we check if the arrangement is free.
        If it is free, then we fall back to the Barakat-Cuntz algorithm.

        .. RUBRIC:: BC

        Return the product of the derivation module free chain matrices.
        See Section 6 of [BC2012]_.

        EXAMPLES::

            sage: # needs sage.combinat sage.groups
            sage: W = WeylGroup(['A', 2], prefix='s')
            sage: A = W.long_element().inversion_arrangement()
            sage: A.derivation_module_basis()
            [(a1, a2), (0, a1*a2 + a2^2)]

        TESTS:

        We check the algorithms produce a basis with the same exponents::

            sage: W = WeylGroup(['A', 2], prefix='s')                                   # needs sage.combinat sage.groups
            sage: def exponents(B):
            ....:     return sorted([max(x.degree() for x in b) for b in B])
            sage: for x in W:                   # long time                             # needs sage.combinat sage.groups
            ....:     A = x.inversion_arrangement()
            ....:     B = A.derivation_module_basis(algorithm='singular')
            ....:     Bp = A.derivation_module_basis(algorithm='BC')
            ....:     if B is None:
            ....:         assert Bp is None
            ....:     else:
            ....:         assert exponents(B) == exponents(Bp)
        """

class HyperplaneArrangements(Parent, UniqueRepresentation):
    """
    Hyperplane arrangements.

    For more information on hyperplane arrangements, see
    :mod:`sage.geometry.hyperplane_arrangement.arrangement`.

    INPUT:

    - ``base_ring`` -- ring; the base ring

    - ``names`` -- tuple of strings; the variable names

    EXAMPLES::

        sage: H.<x,y> = HyperplaneArrangements(QQ)
        sage: x
        Hyperplane x + 0*y + 0
        sage: x + y
        Hyperplane x + y + 0
        sage: H(x, y, x-1, y-1)
        Arrangement <y - 1 | y | x - 1 | x>
    """
    Element = HyperplaneArrangementElement
    def __init__(self, base_ring, names=...) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: K = HyperplaneArrangements(QQ, names=('x', 'y'))
            sage: H is K
            True
            sage: type(K)
            <class 'sage.geometry.hyperplane_arrangement.arrangement.HyperplaneArrangements_with_category'>
            sage: K.change_ring(RR).gen(0)
            Hyperplane 1.00000000000000*x + 0.000000000000000*y + 0.000000000000000

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: TestSuite(H).run()
            sage: K = HyperplaneArrangements(QQ)
            sage: TestSuite(K).run()
        """
    def base_ring(self):
        """
        Return the base ring.

        OUTPUT: the base ring of the hyperplane arrangement

        EXAMPLES::

            sage: L.<x,y> = HyperplaneArrangements(QQ)
            sage: L.base_ring()
            Rational Field
        """
    def change_ring(self, base_ring):
        """
        Return hyperplane arrangements over a different base ring.

        INPUT:

        - ``base_ring`` -- a ring; the new base ring

        OUTPUT:

        A new :class:`HyperplaneArrangements` instance over the new
        base ring.

        EXAMPLES::

            sage: L.<x,y> = HyperplaneArrangements(QQ)
            sage: L.gen(0)
            Hyperplane x + 0*y + 0
            sage: L.change_ring(RR).gen(0)
            Hyperplane 1.00000000000000*x + 0.000000000000000*y + 0.000000000000000

        TESTS::

            sage: L.change_ring(QQ) is L
            True
        """
    @cached_method
    def ambient_space(self):
        """
        Return the ambient space.

        The ambient space is the parent of hyperplanes. That is, new
        hyperplanes are always constructed internally from the ambient
        space instance.

        EXAMPLES::

            sage: L.<x, y> = HyperplaneArrangements(QQ)
            sage: L.ambient_space()([(1,0), 0])
            Hyperplane x + 0*y + 0
            sage: L.ambient_space()([(1,0), 0]) == x
            True
        """
    @cached_method
    def ngens(self):
        """
        Return the number of linear variables.

        OUTPUT: integer

        EXAMPLES::

            sage: L.<x, y, z> = HyperplaneArrangements(QQ);  L
            Hyperplane arrangements in 3-dimensional linear space
             over Rational Field with coordinates x, y, z
            sage: L.ngens()
            3
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the coordinate hyperplanes.

        OUTPUT: a tuple of linear expressions, one for each linear variable

        EXAMPLES::

            sage: L = HyperplaneArrangements(QQ, ('x', 'y', 'z'))
            sage: L.gens()
            (Hyperplane x + 0*y + 0*z + 0,
             Hyperplane 0*x + y + 0*z + 0,
             Hyperplane 0*x + 0*y + z + 0)
        """
    def gen(self, i):
        """
        Return the `i`-th coordinate hyperplane.

        INPUT:

        - ``i`` -- integer

        OUTPUT: a linear expression

        EXAMPLES::

            sage: L.<x, y, z> = HyperplaneArrangements(QQ);  L
            Hyperplane arrangements in
             3-dimensional linear space over Rational Field with coordinates x, y, z
            sage: L.gen(0)
            Hyperplane x + 0*y + 0*z + 0
        """
