from sage.matrix.constructor import block_matrix as block_matrix, vector as vector, zero_matrix as zero_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.multi_filtered_vector_space import MultiFilteredVectorSpace as MultiFilteredVectorSpace
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.all import SageObject as SageObject
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal

def is_KlyachkoBundle(X):
    """
    Test whether ``X`` is a Klyachko bundle.

    INPUT:

    - ``X`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.schemes.toric.sheaf.klyachko import is_KlyachkoBundle
        sage: is_KlyachkoBundle('test')
        doctest:warning...
        DeprecationWarning: The function is_KlyachkoBundle is deprecated; use 'isinstance(..., KlyachkoBundle_class)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
    """
def Bundle(toric_variety, multi_filtration, check: bool = True):
    """
    Construct a Klyacho bundle.

    INPUT:

    - ``toric_variety`` -- a toric variety; the base space of the bundle

    - ``multi_filtration`` -- a multi-filtered vectors space with
      multiple filtrations being indexed by the one-dimensional cones
      of the fan. Either an instance of
      :func:`~sage.modules.multi_filtered_vector_space.MultiFilteredVectorSpace`
      or something (like a dictionary of ordinary filtered vector
      spaces).

    EXAMPLES::

        sage: P1 = toric_varieties.P1()
        sage: v1, v2, v3 = [(1,0,0), (0,1,0), (0,0,1)]
        sage: F1 = FilteredVectorSpace({1: [v1, v2, v3], 3: [v1]})
        sage: F2 = FilteredVectorSpace({0: [v1, v2, v3], 2: [v2, v3]})
        sage: P1 = toric_varieties.P1()
        sage: r1, r2 = P1.fan().rays()
        sage: F = MultiFilteredVectorSpace({r1: F1, r2: F2});  F
        Filtrations
            N(-1): QQ^3 >= QQ^2 >= QQ^2 >=  0   >= 0
             N(1): QQ^3 >= QQ^3 >= QQ^1 >= QQ^1 >= 0

    You should use the
    :meth:`~sage.schemes.toric.sheaf.constructor.SheafLibrary.Klyachko`
    method to construct instances::

        sage: P1.sheaves.Klyachko(F)
        Rank 3 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.

        sage: P1.sheaves.Klyachko({r1: F1, r2: F2})   # alternative
        Rank 3 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.

    The above is just a shorthand for::

        sage: from sage.schemes.toric.sheaf.klyachko import Bundle
        sage: Bundle(P1, F)
        Rank 3 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.
    """

class KlyachkoBundle_class(SageObject):
    def __init__(self, toric_variety, multi_filtration, check: bool = True) -> None:
        """
        A toric bundle using Klyachko's representation.

        .. warning::

            You should always use the :func:`Bundle` factory function
            to construct instances.

        INPUT:

        - ``toric_variety`` -- a toric variety; the base space of the bundle

        - ``multi_filtration`` -- a
          :func:`~sage.modules.multi_filtered_vector_space.MultiFilteredVectorSpace`
          with index set the rays of the fan.

        - ``check`` -- boolean (default: ``True``); whether to perform
          consistency checks

        EXAMPLES::

            sage: P1 = toric_varieties.P1()
            sage: r1, r2 = P1.fan().rays()
            sage: F = MultiFilteredVectorSpace({
            ....:      r1: FilteredVectorSpace(3,1),
            ....:      r2: FilteredVectorSpace(3,0)});  F
            Filtrations
                N(-1): QQ^3 >=  0   >= 0
                 N(1): QQ^3 >= QQ^3 >= 0
            sage: from sage.schemes.toric.sheaf.klyachko import Bundle
            sage: Bundle(P1, F)
            Rank 3 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.
        """
    def variety(self):
        """
        Return the base toric variety.

        OUTPUT: a toric variety

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: V = X.sheaves.tangent_bundle(); V
            Rank 2 bundle on 2-d CPR-Fano toric variety covered by 3 affine patches.
            sage: V.variety() is X
            True
        """
    def base_ring(self):
        """
        Return the base field.

        OUTPUT: a field

        EXAMPLES::

            sage: T_P2 = toric_varieties.P2().sheaves.tangent_bundle()
            sage: T_P2.base_ring()
            Rational Field
        """
    def fiber(self):
        """
        Return the generic fiber of the vector bundle.

        OUTPUT: a vector space over :meth:`base_ring`

        EXAMPLES::

            sage: T_P2 = toric_varieties.P2().sheaves.tangent_bundle()
            sage: T_P2.fiber()
            Vector space of dimension 2 over Rational Field
        """
    def rank(self):
        """
        Return the rank of the vector bundle.

        OUTPUT: integer

        EXAMPLES::

            sage: T_P2 = toric_varieties.P2().sheaves.tangent_bundle()
            sage: T_P2.rank()
            2
        """
    def get_filtration(self, ray=None):
        """
        Return the filtration associated to the ``ray``.

        INPUT:

        - ``ray`` -- integer; a `N`-lattice point, a one-dimensional
          cone, or ``None`` (default). Specifies a ray of the fan of
          the toric variety, either via its index or its generator.

        OUTPUT:

        The filtered vector space associated to the given ``ray``. If
        no ray is specified, all filtrations are returned.

        EXAMPLES::

            sage: TX = toric_varieties.dP6().sheaves.tangent_bundle()
            sage: TX.get_filtration(0)
            QQ^2 >= QQ^1 >= 0
            sage: TX.get_filtration([-1, -1])
            QQ^2 >= QQ^1 >= 0
            sage: TX.get_filtration(TX.variety().fan(1)[0])
            QQ^2 >= QQ^1 >= 0
            sage: TX.get_filtration()
            Filtrations
                N(-1, -1): QQ^2 >= QQ^1 >= 0
                 N(-1, 0): QQ^2 >= QQ^1 >= 0
                 N(0, -1): QQ^2 >= QQ^1 >= 0
                  N(0, 1): QQ^2 >= QQ^1 >= 0
                  N(1, 0): QQ^2 >= QQ^1 >= 0
                  N(1, 1): QQ^2 >= QQ^1 >= 0
        """
    def get_degree(self, ray, i):
        """
        Return the vector subspace ``E^\\alpha(i)``.

        - ``ray`` -- integer; a `N`-lattice point, a one-dimensional
          cone, or ``None`` (default). Specifies a ray of the fan of
          the toric variety, either via its index or its generator.

        - ``i`` -- integer; the filtration degree

        OUTPUT:

        A subspace of the :meth:`fiber` vector space. The defining
        data of a Klyachko bundle.

        EXAMPLES::

            sage: TX = toric_varieties.dP6().sheaves.tangent_bundle()
            sage: TX.get_degree(0, 1)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [0 1]
        """
    def filtration_intersection(self, sigma, i):
        """
        Return the intersection of the filtered subspaces.

        INPUT:

        - ``sigma`` -- a cone of the fan of the base toric variety

        - ``i`` -- integer; the filtration degree

        OUTPUT:

        Let the cone be spanned by the rays `\\sigma=\\langle r_1,\\dots,
        r_k\\rangle`. This method returns the intersection

        .. MATH::

            \\bigcap_{r\\in \\{r_1,\\dots,r_k\\}}
            E^{r}(i)

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: fan = X.fan()
            sage: V = X.sheaves.tangent_bundle()
            sage: V.filtration_intersection(fan(1)[0], 1)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [1 0]
            sage: V.filtration_intersection(fan(2)[0], 1)
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix: []
        """
    def E_degree(self, alpha, m):
        """
        Return the vector subspace `E^\\alpha(m)`.

        INPUT:

        - ``alpha`` -- a ray of the fan. Can be specified by its index
          (an integer), a one-dimensional cone, or a `N`-lattice
          point.

        - ``m`` -- tuple of integers or `M`-lattice point. A point in
          the dual lattice of the fan.

        OUTPUT:

        The subspace `E^\\alpha(\\alpha m)` of the filtration indexed by
        the ray `\\alpha` and at the filtration degree `\\alpha * m`

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: M = X.fan().dual_lattice()
            sage: V = X.sheaves.tangent_bundle()
            sage: V.E_degree(X.fan().ray(0), (1,0))
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [1 0]
            sage: V.E_degree(X.fan(1)[0], (1,0))
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [1 0]
            sage: V.E_degree(0, (1,0))
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [1 0]
        """
    @cached_method
    def E_intersection(self, sigma, m):
        """
        Return the vector subspace `E^\\sigma(m)`.

        See [Kly1990]_, equation 4.1.

        INPUT:

        - ``sigma`` -- a cone of the fan of the base toric variety

        - ``m`` -- tuple of integers or `M`-lattice point. A point in
          the dual lattice of the fan. Must be immutable.

        OUTPUT: the subspace `E^\\sigma(m)`.

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: fan = X.fan()
            sage: V = X.sheaves.tangent_bundle()
            sage: V.E_intersection(fan(1)[0], (1,0))
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [1 0]
            sage: V.E_intersection(fan(2)[0], (-1,1))
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix: [0 1]

        For the empty cone, this is always the whole vector space::

            sage: V.E_intersection(fan(0)[0], (1,0))
            Vector space of dimension 2 over Rational Field
        """
    @cached_method
    def E_quotient(self, sigma, m):
        """
        Return the vector space quotient `E_\\sigma(m)`.

        See [Kly1990]_, equation 4.1.

        INPUT:

        - ``sigma`` -- a cone of the fan of the base toric variety

        - ``m`` -- tuple of integers or `M`-lattice point. A point in
          the dual lattice of the fan. Must be immutable.

        OUTPUT: the subspace `E_\\sigma(m)`.

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: fan = X.fan()
            sage: M = fan.dual_lattice()
            sage: cone = fan(1)[0]
            sage: V = X.sheaves.tangent_bundle()
            sage: m = M(1, 0)
            sage: m.set_immutable()
            sage: V.E_quotient(cone, m)
            Vector space quotient V/W of dimension 1 over Rational Field where
             V: Vector space of dimension 2 over Rational Field
             W: Vector space of degree 2 and dimension 1 over Rational Field
                Basis matrix: [1 0]
            sage: V.E_quotient(fan(2)[0], (-1,1))
            Vector space quotient V/W of dimension 0 over Rational Field where
             V: Vector space of dimension 2 over Rational Field
             W: Vector space of degree 2 and dimension 2 over Rational Field
                Basis matrix:
                [1 0]
                [0 1]
        """
    @cached_method
    def E_quotient_projection(self, sigma, tau, m):
        """
        Return the projection map `E_\\sigma(m) \\to E_\\tau(m)` where
        `\\sigma` is a face of `\\tau`.

        INPUT:

        - ``sigma`` -- a cone of the fan of the base toric variety

        - ``tau`` -- a cone of the fan containing ``sigma``

        - ``m`` -- tuple of integers or `M`-lattice point. A point in
          the dual lattice of the fan. Must be immutable.

        OUTPUT: the restriction map

        .. MATH::

            E_\\sigma(m) \\to E_\\tau(m)

        EXAMPLES::

            sage: P3 = toric_varieties.P(3)
            sage: rays = [(1,0,0), (0,1,0), (0,0,1)]
            sage: F1 = FilteredVectorSpace(rays, {0: [0], 1: [2], 2: [1]})
            sage: F2 = FilteredVectorSpace(3, 0)
            sage: r = P3.fan().rays()
            sage: V = P3.sheaves.Klyachko({r[0]: F1, r[1]: F2, r[2]: F2, r[3]: F2})
            sage: tau = Cone([(1,0,0), (0,1,0)])
            sage: sigma = Cone([(1,0,0)])
            sage: M = P3.fan().dual_lattice()
            sage: m = M(2,1,0)
            sage: m.set_immutable()
            sage: V.E_quotient(sigma, m)
            Vector space quotient V/W of dimension 2 over Rational Field where
             V: Vector space of dimension 3 over Rational Field
             W: Vector space of degree 3 and dimension 1 over Rational Field
                Basis matrix: [0 1 0]
            sage: V.E_quotient(tau, m)
            Vector space quotient V/W of dimension 2 over Rational Field where
             V: Vector space of dimension 3 over Rational Field
             W: Vector space of degree 3 and dimension 1 over Rational Field
                Basis matrix: [0 1 0]
            sage: V.E_quotient_projection(sigma, tau, m)
            Vector space morphism represented by the matrix:
             [1 0]
             [0 1]
             Domain:   Vector space quotient V/W of dimension 2 over Rational Field where
                       V: Vector space of dimension 3 over Rational Field
                       W: Vector space of degree 3 and dimension 1 over Rational Field
                          Basis matrix: [0 1 0]
             Codomain: Vector space quotient V/W of dimension 2 over Rational Field where
                       V: Vector space of dimension 3 over Rational Field
                       W: Vector space of degree 3 and dimension 1 over Rational Field
                          Basis matrix: [0 1 0]
        """
    def cohomology_complex(self, m):
        '''
        Return the "cohomology complex" `C^*(m)`.

        See [Kly1990]_, equation 4.2.

        INPUT:

        - ``m`` -- tuple of integers or `M`-lattice point. A point in
          the dual lattice of the fan. Must be immutable.

        OUTPUT:

        The "cohomology complex" as a chain complex over the
        :meth:`base_ring`.

        EXAMPLES::

            sage: P3 = toric_varieties.P(3)
            sage: rays = [(1,0,0), (0,1,0), (0,0,1)]
            sage: F1 = FilteredVectorSpace(rays, {0: [0], 1: [2], 2: [1]})
            sage: F2 = FilteredVectorSpace(rays, {0: [1,2], 1: [0]})
            sage: r = P3.fan().rays()
            sage: V = P3.sheaves.Klyachko({r[0]: F1, r[1]: F2, r[2]: F2, r[3]: F2})
            sage: tau = Cone([(1,0,0), (0,1,0)])
            sage: sigma = Cone([(1, 0, 0)])
            sage: M = P3.fan().dual_lattice()
            sage: m = M(1, 1, 0); m.set_immutable()
            sage: V.cohomology_complex(m)
            Chain complex with at most 2 nonzero terms over Rational Field

            sage: F = CyclotomicField(3)
            sage: P3 = toric_varieties.P(3).change_ring(F)
            sage: V = P3.sheaves.Klyachko({r[0]: F1, r[1]: F2, r[2]: F2, r[3]: F2})
            sage: V.cohomology_complex(m)
            Chain complex with at most 2 nonzero terms over Cyclotomic
            Field of order 3 and degree 2
        '''
    def cohomology(self, degree=None, weight=None, dim: bool = False):
        """
        Return the bundle cohomology groups.

        INPUT:

        - ``degree`` -- ``None`` (default) or an integer; the degree of
          the cohomology group

        - ``weight`` -- ``None`` (default) or a tuple of integers or a
          `M`-lattice point. A point in the dual lattice of the fan
          defining a torus character. The weight of the cohomology
          group.

        - ``dim`` -- boolean (default: ``False``); whether to return
          vector spaces or only their dimension

        OUTPUT:

        The cohomology group of given cohomological ``degree`` and
        torus ``weight``.

        * If no ``weight`` is specified, the unweighted group (sum
          over all weights) is returned.

        * If no ``degree`` is specified, a dictionary whose keys are
          integers and whose values are the cohomology groups is
          returned. If, in addition, ``dim=True``, then an integral
          vector of the dimensions is returned.

        EXAMPLES::

            sage: V = toric_varieties.P2().sheaves.tangent_bundle()
            sage: V.cohomology(degree=0, weight=(0,0))
            Vector space of dimension 2 over Rational Field
            sage: V.cohomology(weight=(0,0), dim=True)
            (2, 0, 0)
            sage: for i,j in cartesian_product((list(range(-2,3)), list(range(-2,3)))):
            ....:       HH = V.cohomology(weight=(i,j), dim=True)
            ....:       if HH.is_zero(): continue
            ....:       print('H^*i(P^2, TP^2)_M({}, {}) = {}'.format(i,j,HH))
            H^*i(P^2, TP^2)_M(-1, 0) = (1, 0, 0)
            H^*i(P^2, TP^2)_M(-1, 1) = (1, 0, 0)
            H^*i(P^2, TP^2)_M(0, -1) = (1, 0, 0)
            H^*i(P^2, TP^2)_M(0, 0) = (2, 0, 0)
            H^*i(P^2, TP^2)_M(0, 1) = (1, 0, 0)
            H^*i(P^2, TP^2)_M(1, -1) = (1, 0, 0)
            H^*i(P^2, TP^2)_M(1, 0) = (1, 0, 0)
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        .. warning::

            This method tests whether the underlying representation is
            the same. Use :meth:`is_isomorphic` to test for
            mathematical equivalence.

        INPUT:

        - ``other`` -- anything

        OUTPUT: boolean

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: V1 = X.sheaves.trivial_bundle(1)
            sage: V2 = X.sheaves.trivial_bundle(2)
            sage: V2 == V1
            False
            sage: V2 == V1 + V1
            True

            sage: T_X = X.sheaves.tangent_bundle()
            sage: O_X = X.sheaves.trivial_bundle(1)
            sage: T_X + O_X == O_X + T_X
            False
        """
    def is_isomorphic(self, other) -> None:
        """
        Test whether two bundles are isomorphic.

        INPUT:

        - ``other`` -- anything

        OUTPUT: boolean

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: T_X = X.sheaves.tangent_bundle()
            sage: O_X = X.sheaves.trivial_bundle(1)
            sage: T_X + O_X == O_X + T_X
            False
            sage: (T_X + O_X).is_isomorphic(O_X + T_X)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def direct_sum(self, other):
        """
        Return the sum of two vector bundles.

        INPUT:

        - ``other`` -- a Klyachko bundle over the same base

        OUTPUT: the direct sum as a new Klyachko bundle

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: V1 = X.sheaves.trivial_bundle(1)
            sage: V2 = X.sheaves.trivial_bundle(2)
            sage: V2.direct_sum(V1)
            Rank 3 bundle on 2-d CPR-Fano toric variety covered by 3 affine patches.

            sage: V1 = X.sheaves.trivial_bundle(1)
            sage: V2 = X.sheaves.trivial_bundle(2)
            sage: V2 == V1 + V1
            True
        """
    __add__ = direct_sum
    def tensor_product(self, other):
        """
        Return the sum of two vector bundles.

        INPUT:

        - ``other`` -- a Klyachko bundle over the same base

        OUTPUT: the tensor product as a new Klyachko bundle

        EXAMPLES::

            sage: X = toric_varieties.P2()
            sage: OX = X.sheaves.trivial_bundle(1)
            sage: X.sheaves.tangent_bundle().tensor_product(OX)
            Rank 2 bundle on 2-d CPR-Fano toric variety covered by 3 affine patches.
            sage: OX == OX * OX
            True
        """
    __mul__ = tensor_product
    def exterior_power(self, n):
        """
        Return the `n`-th exterior power.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        The `n`-th exterior power `\\wedge_{i=1}^n V` of the bundle `V`
        as a new Klyachko bundle.

        EXAMPLES::

            sage: X = toric_varieties.P2_123()
            sage: TX = X.sheaves.tangent_bundle()
            sage: antiK = X.sheaves.line_bundle(-X.K())
            sage: TX.exterior_power(2) == antiK
            True
            sage: TX.wedge(2) == antiK   # alias
            True
        """
    wedge = exterior_power
    def symmetric_power(self, n):
        """
        Return the `n`-th symmetric power.

        INPUT:

        - ``n`` -- integer

        OUTPUT: the `n`-th symmetric power as a new Klyachko bundle

        EXAMPLES::

            sage: P1 = toric_varieties.P1()
            sage: H = P1.divisor(0)
            sage: L = P1.sheaves.line_bundle(H)
            sage: (L + L).symmetric_power(2)
            Rank 3 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.
            sage: (L + L).symmetric_power(2) == L*L + L*L + L*L
            True
        """
    def dual(self):
        """
        Return the dual bundle.

        OUTPUT: the dual bundle as a new Klyachko bundle

        EXAMPLES::

            sage: P1 = toric_varieties.P1()
            sage: H = P1.divisor(0)
            sage: L = P1.sheaves.line_bundle(H)
            sage: L.dual()
            Rank 1 bundle on 1-d CPR-Fano toric variety covered by 2 affine patches.
            sage: L.dual() == P1.sheaves.line_bundle(-H)
            True
        """
    def random_deformation(self, epsilon=None):
        """
        Return a generic torus-equivariant deformation of the bundle.

        INPUT:

        - ``epsilon`` -- an element of the base ring; scales the
          random deformation

        OUTPUT:

        A new Klyachko bundle with randomly perturbed moduli. In
        particular, the same Chern classes.

        EXAMPLES::

           sage: P1 = toric_varieties.P1()
           sage: H = P1.divisor(0)
           sage: V = P1.sheaves.line_bundle(H) + P1.sheaves.line_bundle(-H)
           sage: V.cohomology(dim=True, weight=(0,))
           (1, 0)
           sage: Vtilde = V.random_deformation()
           sage: Vtilde.cohomology(dim=True, weight=(0,))  # random failure (see #32773)
           (1, 0)
        """
