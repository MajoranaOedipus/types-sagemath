from sage.misc.abstract_method import abstract_method as abstract_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class GenericCellComplex(SageObject):
    """
    Class of abstract cell complexes.

    This is meant to be used by developers to produce new classes, not
    by casual users.  Classes which derive from this are
    :class:`~sage.homology.simplicial_complex.SimplicialComplex`,
    :class:`~sage.homology.delta_complex.DeltaComplex`, and
    :class:`~sage.homology.cubical_complex.CubicalComplex`.

    Most of the methods here are not implemented, but probably should
    be implemented in a derived class.  Most of the other methods call
    a non-implemented one; their docstrings contain examples from
    derived classes in which the various methods have been defined.
    For example, :meth:`homology` calls :meth:`chain_complex`; the
    class :class:`~sage.homology.delta_complex.DeltaComplex`
    implements
    :meth:`~sage.homology.delta_complex.DeltaComplex.chain_complex`,
    and so the :meth:`homology` method here is illustrated with
    examples involving `\\Delta`-complexes.

    EXAMPLES:

    It's hard to give informative examples of the base class, since
    essentially nothing is implemented. ::

        sage: from sage.topology.cell_complex import GenericCellComplex
        sage: A = GenericCellComplex()
    """
    def __eq__(self, right):
        """
        Comparisons of cell complexes are not implemented.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex(); B = GenericCellComplex()
            sage: A == B # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __ne__(self, right):
        """
        Comparisons of cell complexes are not implemented.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex(); B = GenericCellComplex()
            sage: A != B # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    @abstract_method
    def cells(self, subcomplex=None) -> None:
        """
        The cells of this cell complex, in the form of a dictionary:
        the keys are integers, representing dimension, and the value
        associated to an integer `d` is the set of `d`-cells.  If the
        optional argument ``subcomplex`` is present, then return only
        the cells which are *not* in the subcomplex.

        INPUT:

        - ``subcomplex`` -- subcomplex (default: ``None``); a subcomplex of
          this cell complex; return the cells which are not in this subcomplex

        This is not implemented in general; it should be implemented
        in any derived class.  When implementing, see the warning in
        the :meth:`dimension` method.

        This method is used by various other methods, such as
        :meth:`n_cells` and :meth:`f_vector`.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex()
            sage: A.cells()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method cells at ...>
        """
    def dimension(self):
        """
        The dimension of this cell complex: the maximum
        dimension of its cells.

        .. WARNING::

          If the :meth:`cells` method calls :meth:`dimension`,
          then you'll get an infinite loop.  So either don't use
          :meth:`dimension` or override :meth:`dimension`.

        EXAMPLES::

            sage: simplicial_complexes.RandomComplex(d=5, n=8).dimension()
            5
            sage: delta_complexes.Sphere(3).dimension()
            3
            sage: T = cubical_complexes.Torus()
            sage: T.product(T).dimension()
            4
        """
    def n_cells(self, n, subcomplex=None):
        """
        List of cells of dimension `n` of this cell complex.
        If the optional argument ``subcomplex`` is present, then
        return the `n`-dimensional cells which are *not* in the
        subcomplex.

        INPUT:

        - ``n`` -- nonnegative integer; the dimension
        - ``subcomplex`` -- (optional) a subcomplex of this cell complex;
          return the cells which are not in this subcomplex

        .. NOTE::

            The resulting list need not be sorted. If you want a sorted
            list of `n`-cells, use :meth:`_n_cells_sorted`.

        EXAMPLES::

            sage: delta_complexes.Torus().n_cells(1)
            [(0, 0), (0, 0), (0, 0)]
            sage: cubical_complexes.Cube(1).n_cells(0)
            [[1,1], [0,0]]
        """
    def f_vector(self):
        """
        The `f`-vector of this cell complex: a list whose `n`-th
        item is the number of `(n-1)`-cells.  Note that, like all
        lists in Sage, this is indexed starting at 0: the 0th element
        in this list is the number of `(-1)`-cells (which is 1: the
        empty cell is the only `(-1)`-cell).

        EXAMPLES::

            sage: simplicial_complexes.KleinBottle().f_vector()
            [1, 8, 24, 16]
            sage: delta_complexes.KleinBottle().f_vector()
            [1, 1, 3, 2]
            sage: cubical_complexes.KleinBottle().f_vector()
            [1, 42, 84, 42]
        """
    def euler_characteristic(self):
        """
        The Euler characteristic of this cell complex: the
        alternating sum over `n \\geq 0` of the number of
        `n`-cells.

        EXAMPLES::

            sage: simplicial_complexes.Simplex(5).euler_characteristic()
            1
            sage: delta_complexes.Sphere(6).euler_characteristic()
            2
            sage: cubical_complexes.KleinBottle().euler_characteristic()
            0
        """
    @abstract_method
    def product(self, right, rename_vertices: bool = True) -> None:
        """
        The (Cartesian) product of this cell complex with another one.

        Products are not implemented for general cell complexes.  They
        may be implemented in some derived classes (like simplicial
        complexes).

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex(); B = GenericCellComplex()
            sage: A.product(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method product at ...>
        """
    @abstract_method
    def disjoint_union(self, right) -> None:
        """
        The disjoint union of this cell complex with another one.

        INPUT:

        - ``right`` -- the other cell complex (the right-hand factor)

        Disjoint unions are not implemented for general cell complexes.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex(); B = GenericCellComplex()
            sage: A.disjoint_union(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method disjoint_union at ...>
        """
    @abstract_method
    def wedge(self, right) -> None:
        """
        The wedge (one-point union) of this cell complex with
        another one.

        INPUT:

        - ``right`` -- the other cell complex (the right-hand factor)

        Wedges are not implemented for general cell complexes.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex(); B = GenericCellComplex()
            sage: A.wedge(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method wedge at ...>
        """
    @abstract_method
    def join(self, right) -> None:
        """
        The join of this cell complex with another one.

        INPUT:

        - ``right`` -- the other cell complex (the right-hand factor)

        Joins are not implemented for general cell complexes.  They
        may be implemented in some derived classes (like simplicial
        complexes).

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex(); B = GenericCellComplex()
            sage: A.join(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method join at ...>
        """
    @abstract_method
    def chain_complex(self, subcomplex=None, augmented: bool = False, verbose: bool = False, check: bool = True, dimensions=None, base_ring=..., cochain: bool = False) -> None:
        """
        This is not implemented for general cell complexes.

        Some keywords to possibly implement in a derived class:

        - ``subcomplex`` -- a subcomplex: compute the relative chain complex
        - ``augmented`` -- a bool: whether to return the augmented complex
        - ``verbose`` -- a bool: whether to print informational messages as
          the chain complex is being computed
        - ``check`` -- a bool: whether to check that the each
          composite of two consecutive differentials is zero
        - ``dimensions`` -- if ``None``, compute the chain complex in all
          dimensions.  If a list or tuple of integers, compute the
          chain complex in those dimensions, setting the chain groups
          in all other dimensions to zero.

        Definitely implement the following:

        - ``base_ring`` -- commutative ring (default: ZZ)
        - ``cochain`` -- a bool: whether to return the cochain complex

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex()
            sage: A.chain_complex()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method chain_complex at ...>
        """
    def homology(self, dim=None, base_ring=..., subcomplex=None, generators: bool = False, cohomology: bool = False, algorithm: str = 'pari', verbose: bool = False, reduced: bool = True, **kwds):
        """
        The (reduced) homology of this cell complex.

        INPUT:

        - ``dim`` -- integer or list of integers or ``None`` (default:
          ``None``); if ``None``, then return the homology in every
          dimension.  If ``dim`` is an integer or list, return the
          homology in the given dimensions.  (Actually, if ``dim`` is
          a list, return the homology in the range from ``min(dim)``
          to ``max(dim)``.)
        - ``base_ring`` -- commutative ring (default: ``ZZ``); must be `\\ZZ` or
          a field
        - ``subcomplex`` -- (default: empty) a subcomplex of this simplicial
          complex. Compute the homology relative to this subcomplex.
        - ``generators`` -- boolean (default: ``False``); if ``True``, return
          generators for the homology groups along with the groups.
        - ``cohomology`` -- boolean (default: ``False``); if ``True``, compute
          cohomology rather than homology
        - ``algorithm`` -- string (default: ``'pari'``); the algorithm options
          are 'auto', 'dhsw', or 'pari'. See below for a description of what
          they mean.
        - ``verbose`` -- boolean (default: ``False``); if True, print some
          messages as the homology is computed
        - ``reduced`` -- boolean (default: ``True``); if ``True``, return the
          reduced homology

        ALGORITHM:

        Compute the chain complex of ``self`` and compute its homology
        groups.  To do this: over a field, just compute ranks and
        nullities, thus obtaining dimensions of the homology groups as
        vector spaces.  Over the integers, compute Smith normal form
        of the boundary matrices defining the chain complex according
        to the value of ``algorithm``.  If ``algorithm`` is
        ``'auto'``, then for each relatively small matrix, use the
        standard Sage method, which calls the Pari package.  For any
        large matrix, reduce it using the Dumas, Heckenbach, Saunders,
        and Welker elimination algorithm [DHSW2003]_: see
        :func:`~sage.homology.matrix_utils.dhsw_snf` for details.

        ``'no_chomp'`` is a synonym for ``'auto'``, maintained for
        backward-compatibility.

        ``algorithm`` may also be ``'pari'`` or ``'dhsw'``, which
        forces the named algorithm to be used regardless of the size
        of the matrices.

        As of this writing, ``'pari'`` is the fastest standard option.

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = delta_complexes.RealProjectivePlane()
            sage: P.homology()
            {0: 0, 1: C2, 2: 0}
            sage: P.homology(reduced=False)
            {0: Z, 1: C2, 2: 0}
            sage: P.homology(base_ring=GF(2))
            {0: Vector space of dimension 0 over Finite Field of size 2,
             1: Vector space of dimension 1 over Finite Field of size 2,
             2: Vector space of dimension 1 over Finite Field of size 2}
            sage: S7 = delta_complexes.Sphere(7)
            sage: S7.homology(7)
            Z
            sage: cubical_complexes.KleinBottle().homology(1, base_ring=GF(2))
            Vector space of dimension 2 over Finite Field of size 2

        Sage can compute generators of homology groups::

            sage: S2 = simplicial_complexes.Sphere(2)
            sage: S2.homology(dim=2, generators=True, base_ring=GF(2))                  # needs sage.modules
            [(Vector space of dimension 1 over Finite Field of size 2,
              (0, 1, 2) + (0, 1, 3) + (0, 2, 3) + (1, 2, 3))]

        When generators are computed, Sage returns a pair for each
        dimension: the group and the list of generators.  For
        simplicial complexes, each generator is represented as a
        linear combination of simplices, as above, and for cubical
        complexes, each generator is a linear combination of cubes::

            sage: S2_cub = cubical_complexes.Sphere(2)
            sage: S2_cub.homology(dim=2, generators=True)                               # needs sage.modules
            [(Z,
             [0,0] x [0,1] x [0,1] - [0,1] x [0,0] x [0,1] + [0,1] x [0,1] x [0,0]
             - [0,1] x [0,1] x [1,1] + [0,1] x [1,1] x [0,1] - [1,1] x [0,1] x [0,1])]

        Similarly for simplicial sets::

            sage: S = simplicial_sets.Sphere(2)
            sage: S.homology(generators=True)                                           # needs sage.modules
            {0: [], 1: 0, 2: [(Z, sigma_2)]}
        """
    def cohomology(self, dim=None, base_ring=..., subcomplex=None, generators: bool = False, algorithm: str = 'pari', verbose: bool = False, reduced: bool = True):
        """
        The reduced cohomology of this cell complex.

        The arguments are the same as for the :meth:`homology` method,
        except that :meth:`homology` accepts a ``cohomology`` key
        word, while this function does not: ``cohomology`` is
        automatically true here.  Indeed, this function just calls
        :meth:`homology` with ``cohomology`` set to ``True``.

        INPUT:

        - ``dim``
        - ``base_ring``
        - ``subcomplex``
        - ``algorithm``
        - ``verbose``
        - ``reduced``

        EXAMPLES::

            sage: circle = SimplicialComplex([[0,1], [1,2], [0, 2]])
            sage: circle.cohomology(0)                                                  # needs sage.modules
            0
            sage: circle.cohomology(1)                                                  # needs sage.modules
            Z

        Projective plane::

            sage: # needs sage.modules
            sage: P2 = SimplicialComplex([[0,1,2], [0,2,3], [0,1,5], [0,4,5], [0,3,4],
            ....:                         [1,2,4], [1,3,4], [1,3,5], [2,3,5], [2,4,5]])
            sage: P2.cohomology(2)
            C2
            sage: P2.cohomology(2, base_ring=GF(2))
            Vector space of dimension 1 over Finite Field of size 2
            sage: P2.cohomology(2, base_ring=GF(3))
            Vector space of dimension 0 over Finite Field of size 3

            sage: cubical_complexes.KleinBottle().cohomology(2)                         # needs sage.modules
            C2

        Relative cohomology::

            sage: T = SimplicialComplex([[0,1]])
            sage: U = SimplicialComplex([[0], [1]])
            sage: T.cohomology(1, subcomplex=U)                                         # needs sage.modules
            Z

        A `\\Delta`-complex example::

            sage: s5 = delta_complexes.Sphere(5)
            sage: s5.cohomology(base_ring=GF(7))[5]                                     # needs sage.modules
            Vector space of dimension 1 over Finite Field of size 7
        """
    def betti(self, dim=None, subcomplex=None):
        """
        The Betti numbers of this simplicial complex as a dictionary
        (or a single Betti number, if only one dimension is given):
        the `i`-th Betti number is the rank of the `i`-th homology group.

        INPUT:

        - ``dim`` -- integer or list of integers or ``None`` (default:
          ``None``); if ``None``, then return every Betti number, as
          a dictionary with keys the non-negative integers.  If
          ``dim`` is an integer or list, return the Betti number for
          each given dimension.  (Actually, if ``dim`` is a list,
          return the Betti numbers, as a dictionary, in the range
          from ``min(dim)`` to ``max(dim)``.  If ``dim`` is a number,
          return the Betti number in that dimension.)
        - ``subcomplex`` -- a subcomplex (default: ``None``) of this cell
          complex;  compute the Betti numbers of the homology relative to this
          subcomplex

        EXAMPLES:

        Build the two-sphere as a three-fold join of a
        two-point space with itself::

            sage: S = SimplicialComplex([[0], [1]])
            sage: (S*S*S).betti()                                                       # needs sage.modules
            {0: 1, 1: 0, 2: 1}
            sage: (S*S*S).betti([1,2])                                                  # needs sage.modules
            {1: 0, 2: 1}
            sage: (S*S*S).betti(2)                                                      # needs sage.modules
            1

        Or build the two-sphere as a `\\Delta`-complex::

            sage: S2 = delta_complexes.Sphere(2)
            sage: S2.betti([1,2])                                                       # needs sage.modules
            {1: 0, 2: 1}

        Or as a cubical complex::

            sage: S2c = cubical_complexes.Sphere(2)
            sage: S2c.betti(2)                                                          # needs sage.modules
            1
        """
    def is_acyclic(self, base_ring=...):
        """
        Return ``True`` if the reduced homology with coefficients in
        ``base_ring`` of this cell complex is zero.

        INPUT:

        - ``base_ring`` -- (default: ``ZZ``) compute homology
          with coefficients in this ring

        EXAMPLES::

            sage: RP2 = simplicial_complexes.RealProjectivePlane()
            sage: RP2.is_acyclic()                                                      # needs sage.modules
            False
            sage: RP2.is_acyclic(QQ)                                                    # needs sage.modules
            True

        This first computes the Euler characteristic: if it is not 1,
        the complex cannot be acyclic. So this should return ``False``
        reasonably quickly on complexes with Euler characteristic not
        equal to 1::

            sage: K = cubical_complexes.KleinBottle()
            sage: C = cubical_complexes.Cube(2)
            sage: P = K.product(C); P
            Cubical complex with 168 vertices and 1512 cubes
            sage: P.euler_characteristic()
            0
            sage: P.is_acyclic()
            False
        """
    def n_chains(self, n, base_ring=..., cochains: bool = False):
        '''
        Return the free module of chains in degree ``n`` over ``base_ring``.

        INPUT:

        - ``n`` -- integer
        - ``base_ring`` -- ring (default: `\\ZZ`)
        - ``cochains`` -- boolean (default: ``False``); if
          ``True``, return cochains instead

        The only difference between chains and cochains is
        notation. In a simplicial complex, for example, a simplex
        ``(0,1,2)`` is written as "(0,1,2)" in the group of chains but
        as "\\chi_(0,1,2)" in the group of cochains.

        EXAMPLES::

            sage: S2 = simplicial_complexes.Sphere(2)
            sage: S2.n_chains(1, QQ)                                                    # needs sage.modules
            Free module generated by {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
             over Rational Field
            sage: list(S2.n_chains(1, QQ, cochains=False).basis())                      # needs sage.modules
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            sage: list(S2.n_chains(1, QQ, cochains=True).basis())                       # needs sage.modules
            [\\chi_(0, 1), \\chi_(0, 2), \\chi_(0, 3), \\chi_(1, 2), \\chi_(1, 3), \\chi_(2, 3)]
        '''
    def algebraic_topological_model(self, base_ring=...) -> None:
        '''
        Algebraic topological model for this cell complex with
        coefficients in ``base_ring``.

        The term "algebraic topological model" is defined by Pilarczyk
        and Réal [PR2015]_.

        This is not implemented for generic cell complexes. For any
        classes deriving from this one, when this method is
        implemented, it should essentially just call either
        :func:`~sage.homology.algebraic_topological_model.algebraic_topological_model`
        or
        :func:`~sage.homology.algebraic_topological_model.algebraic_topological_model_delta_complex`.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex()
            sage: A.algebraic_topological_model(QQ)
            Traceback (most recent call last):
            ...
            NotImplementedError
        '''
    def homology_with_basis(self, base_ring=..., cohomology: bool = False):
        """
        Return the unreduced homology of this complex with
        coefficients in ``base_ring`` with a chosen basis.

        This is implemented for simplicial, cubical, and
        `\\Delta`-complexes, not for arbitrary generic cell complexes.

        INPUT:

        - ``base_ring`` -- coefficient ring (default:
          ``QQ``); must be a field
        - ``cohomology`` -- boolean (default: ``False``); if
          ``True``, return cohomology instead of homology

        Homology basis elements are named 'h_{dim,i}' where i ranges
        between 0 and `r-1`, if `r` is the rank of the homology
        group. Cohomology basis elements are denoted `h^{dim,i}`
        instead.

        .. SEEALSO::

            If ``cohomology`` is ``True``, this returns the cohomology
            as a ring: it calls :meth:`cohomology_ring`.

        EXAMPLES::

            sage: # needs sage.modules
            sage: K = simplicial_complexes.KleinBottle()
            sage: H = K.homology_with_basis(QQ); H
            Homology module of Minimal triangulation of the Klein bottle
             over Rational Field
            sage: sorted(H.basis(), key=str)
            [h_{0,0}, h_{1,0}]
            sage: H = K.homology_with_basis(GF(2)); H
            Homology module of Minimal triangulation of the Klein bottle
             over Finite Field of size 2
            sage: sorted(H.basis(), key=str)
            [h_{0,0}, h_{1,0}, h_{1,1}, h_{2,0}]

        The homology is constructed as a graded object, so for
        example, you can ask for the basis in a single degree::

            sage: H.basis(1)                                                            # needs sage.modules
            Finite family {(1, 0): h_{1,0}, (1, 1): h_{1,1}}

            sage: S3 = delta_complexes.Sphere(3)
            sage: H = S3.homology_with_basis(QQ, cohomology=True)                       # needs sage.modules
            sage: list(H.basis(3))                                                      # needs sage.modules
            [h^{3,0}]
        """
    def cohomology_ring(self, base_ring=...):
        '''
        Return the unreduced cohomology with coefficients in
        ``base_ring`` with a chosen basis.

        This is implemented for simplicial, cubical, and
        `\\Delta`-complexes, not for arbitrary generic cell complexes.
        The resulting elements are suitable for computing cup
        products. For simplicial complexes, they should be suitable
        for computing cohomology operations; so far, only mod 2
        cohomology operations have been implemented.

        INPUT:

        - ``base_ring`` -- coefficient ring (default:
          ``QQ``); must be a field

        The basis elements in dimension ``dim`` are named \'h^{dim,i}\'
        where `i` ranges between 0 and `r-1`, if `r` is the rank of
        the cohomology group.

        .. NOTE::

            For all but the smallest complexes, this is likely to be
            slower than :meth:`cohomology` (with field coefficients),
            possibly by several orders of magnitude. This and its
            companion :meth:`homology_with_basis` carry extra
            information which allows computation of cup products, for
            example, but because of speed issues, you may only wish to
            use these if you need that extra information.

        EXAMPLES::

            sage: # needs sage.modules
            sage: K = simplicial_complexes.KleinBottle()
            sage: H = K.cohomology_ring(QQ); H
            Cohomology ring of Minimal triangulation of the Klein bottle
             over Rational Field
            sage: sorted(H.basis(), key=str)
            [h^{0,0}, h^{1,0}]
            sage: H = K.cohomology_ring(GF(2)); H
            Cohomology ring of Minimal triangulation of the Klein bottle
             over Finite Field of size 2
            sage: sorted(H.basis(), key=str)
            [h^{0,0}, h^{1,0}, h^{1,1}, h^{2,0}]

            sage: X = delta_complexes.SurfaceOfGenus(2)
            sage: H = X.cohomology_ring(QQ); H                                          # needs sage.modules
            Cohomology ring of Delta complex with 3 vertices and 29 simplices
             over Rational Field
            sage: sorted(H.basis(1), key=str)                                           # needs sage.modules
            [h^{1,0}, h^{1,1}, h^{1,2}, h^{1,3}]

            sage: H = simplicial_complexes.Torus().cohomology_ring(QQ); H               # needs sage.modules
            Cohomology ring of Minimal triangulation of the torus
             over Rational Field
            sage: x = H.basis()[1,0]; x                                                 # needs sage.modules
            h^{1,0}
            sage: y = H.basis()[1,1]; y                                                 # needs sage.modules
            h^{1,1}

        You can compute cup products of cohomology classes::

            sage: # needs sage.modules
            sage: x.cup_product(y)
            -h^{2,0}
            sage: x * y # alternate notation
            -h^{2,0}
            sage: y.cup_product(x)
            h^{2,0}
            sage: x.cup_product(x)
            0

        Cohomology operations::

            sage: # needs sage.groups
            sage: RP2 = simplicial_complexes.RealProjectivePlane()
            sage: K = RP2.suspension()
            sage: K.set_immutable()
            sage: y = K.cohomology_ring(GF(2)).basis()[2,0]; y                          # needs sage.modules
            h^{2,0}
            sage: y.Sq(1)                                                               # needs sage.modules
            h^{3,0}

        To compute the cohomology ring, the complex must be
        "immutable". This is only relevant for simplicial complexes,
        and most simplicial complexes are immutable, but certain
        constructions make them mutable. The suspension is one
        example, and this is the reason for calling
        ``K.set_immutable()`` above. Another example::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: T = S1.product(S1)
            sage: T.is_immutable()
            False
            sage: T.cohomology_ring()                                                   # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: this simplicial complex must be immutable; call set_immutable()
            sage: T.set_immutable()
            sage: T.cohomology_ring()                                                   # needs sage.modules
            Cohomology ring of Simplicial complex with 9 vertices and
             18 facets over Rational Field
        '''
    @abstract_method
    def alexander_whitney(self, cell, dim_left) -> None:
        """
        The decomposition of ``cell`` in this complex into left and right
        factors, suitable for computing cup products. This should
        provide a cellular approximation for the diagonal map `K \\to K
        \\times K`.

        This method is not implemented for generic cell complexes, but
        must be implemented for any derived class to make cup products
        work in ``self.cohomology_ring()``.

        INPUT:

        - ``cell`` -- a cell in this complex
        - ``dim_left`` -- the dimension of the left-hand factors in
          the decomposition

        OUTPUT: list containing triples ``(c, left, right)``.
        ``left`` and ``right`` should be cells in this complex, and
        ``c`` an integer. In the cellular approximation of the
        diagonal map, the chain represented by ``cell`` should get
        sent to the sum of terms `c (left \\otimes right)` in the
        tensor product `C(K) \\otimes C(K)` of the chain complex for
        this complex with itself.

        This gets used in the method
        :meth:`~sage.homology.homology_vector_space_with_basis.CohomologyRing.product_on_basis`
        for the class of cohomology rings.

        For simplicial and cubical complexes, the decomposition can be
        done at the level of individual cells: see
        :meth:`~sage.homology.simplicial_complex.Simplex.alexander_whitney`
        and
        :meth:`~sage.homology.cubical_complex.Cube.alexander_whitney`. Then
        the method for simplicial complexes just calls the method for
        individual simplices, and similarly for cubical complexes. For
        `\\Delta`-complexes and simplicial sets, the method is instead
        defined at the level of the cell complex.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex()
            sage: A.alexander_whitney(None, 2)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method alexander_whitney at ...>
        """
    def face_poset(self):
        """
        The face poset of this cell complex, the poset of
        nonempty cells, ordered by inclusion.

        This uses the :meth:`cells` method, and also assumes that for
        each cell ``f``, all of ``f.faces()``, ``tuple(f)``, and
        ``f.dimension()`` make sense.  (If this is not the case in
        some derived class, as happens with `\\Delta`-complexes, then
        override this method.)

        EXAMPLES::

            sage: P = SimplicialComplex([[0, 1], [1,2], [2,3]]).face_poset(); P
            Finite poset containing 7 elements
            sage: sorted(P.list())
            [(0,), (0, 1), (1,), (1, 2), (2,), (2, 3), (3,)]

            sage: S2 = cubical_complexes.Sphere(2)
            sage: S2.face_poset()
            Finite poset containing 26 elements
        """
    def graph(self) -> None:
        """
        The 1-skeleton of this cell complex, as a graph.

        This is not implemented for general cell complexes.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex()
            sage: A.graph()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def is_connected(self):
        """
        Return ``True`` if this cell complex is connected.

        EXAMPLES::

            sage: V = SimplicialComplex([[0,1,2],[3]]); V
            Simplicial complex with vertex set (0, 1, 2, 3) and facets {(3,), (0, 1, 2)}
            sage: V.is_connected()
            False
            sage: X = SimplicialComplex([[0,1,2]])
            sage: X.is_connected()
            True
            sage: U = simplicial_complexes.ChessboardComplex(3,3)
            sage: U.is_connected()
            True
            sage: W = simplicial_complexes.Sphere(3)
            sage: W.is_connected()
            True
            sage: S = SimplicialComplex([[0,1],[2,3]])
            sage: S.is_connected()
            False

            sage: cubical_complexes.Sphere(0).is_connected()
            False
            sage: cubical_complexes.Sphere(2).is_connected()
            True
        """
    @abstract_method
    def n_skeleton(self, n) -> None:
        """
        The `n`-skeleton of this cell complex: the cell
        complex obtained by discarding all of the simplices in
        dimensions larger than `n`.

        INPUT:

        - ``n`` -- nonnegative integer

        This is not implemented for general cell complexes.

        EXAMPLES::

            sage: from sage.topology.cell_complex import GenericCellComplex
            sage: A = GenericCellComplex()
            sage: A.n_skeleton(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method n_skeleton at ...>
        """
