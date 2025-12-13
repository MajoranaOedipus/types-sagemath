from sage.categories.fields import Fields as Fields
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import FreeModule_ambient_field as FreeModule_ambient_field, VectorSpace as VectorSpace
from sage.rings.infinity import InfinityRing as InfinityRing, infinity as infinity, minus_infinity as minus_infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.rings.real_mpfr import RR as RR

def is_FilteredVectorSpace(X):
    """
    Test whether ``X`` is a filtered vector space.

    This function is for library use only.

    INPUT:

    - ``X`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.modules.filtered_vector_space import is_FilteredVectorSpace
        sage: V = FilteredVectorSpace(2, 1)
        sage: is_FilteredVectorSpace(V)
        doctest:warning...:
        DeprecationWarning: the function is_FilteredVectorSpace is deprecated;
        use 'isinstance(..., FilteredVectorSpace_class)' instead
        See https://github.com/sagemath/sage/issues/37924 for details.
        True
        sage: is_FilteredVectorSpace('ceci n'est pas une pipe')
        False
    """
def FilteredVectorSpace(arg1, arg2=None, base_ring=..., check: bool = True):
    """
    Construct a filtered vector space.

    INPUT:

    This function accepts various input that determines the vector space and filtration.

    - Just the dimensionFilteredVectorSpace(dimension): Return the trivial filtration
      (where all vector spaces are isomorphic).

    - Dimension and maximal degree, see
      :func:`constructor_from_dim_degree` for arguments. Construct a
      filtration with only one non-trivial step `V\\supset 0` at the
      given cutoff degree.

    - A dictionary containing the degrees as keys and a list of vector
      space generators as values, see
      :func:`FilteredVectorSpace_from_generators`

    - Generators and a dictionary containing the degrees as keys and
      the indices of vector space generators as values, see
      :func:`FilteredVectorSpace_from_generators_indices`

    In addition, the following keyword arguments are supported:

    - ``base_ring`` -- a field (default: `\\QQ`). The base
      field of the vector space. Must be a field.

    EXAMPLES:

    Just the dimension for the trivial filtration::

        sage: FilteredVectorSpace(2)
        QQ^2

    Dimension and degree::

        sage: FilteredVectorSpace(2, 1)
        QQ^2 >= 0

    Dictionary of generators::

        sage: FilteredVectorSpace({1:[(1,0), (0,1)], 3:[(1,0)]})
        QQ^2 >= QQ^1 >= QQ^1 >= 0

    Generators and a dictionary referring to them by index::

        sage: FilteredVectorSpace([(1,0), (0,1)], {1:[0,1], 3:[0]})
        QQ^2 >= QQ^1 >= QQ^1 >= 0
    """
def normalize_degree(deg):
    """
    Normalize the degree.

    - ``deg`` -- something that defines the degree (either integer or infinity)

    OUTPUT: plus/minus infinity or a Sage integer

    EXAMPLES::

        sage: from sage.modules.filtered_vector_space import normalize_degree
        sage: type(normalize_degree(int(1)))
        <class 'sage.rings.integer.Integer'>
        sage: normalize_degree(oo)
        +Infinity
    """
def construct_from_dim_degree(dim, max_degree, base_ring, check):
    """
    Construct a filtered vector space.

    INPUT:

    - ``dim`` -- integer; the dimension

    - ``max_degree`` -- integer or infinity; the maximal degree where
      the vector subspace of the filtration is still the entire space

    EXAMPLES::

        sage: V = FilteredVectorSpace(2, 5);  V
        QQ^2 >= 0
        sage: V.get_degree(5)
        Vector space of degree 2 and dimension 2 over Rational Field
        Basis matrix:
        [1 0]
        [0 1]
        sage: V.get_degree(6)
        Vector space of degree 2 and dimension 0 over Rational Field
        Basis matrix:
        []

        sage: FilteredVectorSpace(2, oo)
        QQ^2
        sage: FilteredVectorSpace(2, -oo)
        0 in QQ^2

    TESTS::

        sage: from sage.modules.filtered_vector_space import construct_from_dim_degree
        sage: V = construct_from_dim_degree(2, 5, QQ, True);  V
        QQ^2 >= 0
    """
def construct_from_generators(filtration, base_ring, check):
    """
    Construct a filtered vector space.

    INPUT:

    - ``filtration`` -- dictionary of filtration steps. Each
      filtration step is a pair consisting of an integer degree and a
      list/tuple/iterable of vector space generators. The integer
      ``degree`` stipulates that all filtration steps of degree higher
      or equal than ``degree`` (up to the next filtration step) are
      said subspace.

    EXAMPLES::

        sage: from sage.modules.filtered_vector_space import construct_from_generators
        sage: r = [1, 2]
        sage: construct_from_generators({1:[r]}, QQ, True)
        QQ^1 >= 0 in QQ^2
    """
def construct_from_generators_indices(generators, filtration, base_ring, check):
    """
    Construct a filtered vector space.

    INPUT:

    - ``generators`` -- list/tuple/iterable of vectors, or something
      convertible to them. The generators spanning various
      subspaces.

    - ``filtration`` -- list or iterable of filtration steps. Each
      filtration step is a pair ``(degree, ray_indices)``. The
      ``ray_indices`` are a list or iterable of ray indices, which
      span a subspace of the vector space. The integer ``degree``
      stipulates that all filtration steps of degree higher or equal
      than ``degree`` (up to the next filtration step) are said
      subspace.

    EXAMPLES::

        sage: from sage.modules.filtered_vector_space import construct_from_generators_indices
        sage: gens = [(1,0), (0,1), (-1,-1)]
        sage: V = construct_from_generators_indices(gens, {1:[0,1], 3:[1]}, QQ, True);  V
        QQ^2 >= QQ^1 >= QQ^1 >= 0

    TESTS::

        sage: gens = [(int(1),int(0)), (0,1), (-1,-1)]
        sage: construct_from_generators_indices(iter(gens), {int(0):[0, int(1)], 2:[2]}, QQ, True)
        QQ^2 >= QQ^1 >= QQ^1 >= 0
    """

class FilteredVectorSpace_class(FreeModule_ambient_field):
    def __init__(self, base_ring, dim, generators, filtration, check: bool = True) -> None:
        """
        A descending filtration of a vector space.

        INPUT:

        - ``base_ring`` -- a field; the base field of the ambient vector space

        - ``dim`` -- integer; the dimension of the ambient vector space

        - ``generators`` -- tuple of generators for the ambient vector
          space. These will be used to span the subspaces of the
          filtration.

        - ``filtration`` -- dictionary of filtration steps in ray
          index notation. See
          :func:`construct_from_generators_indices` for details.

        - ``check`` -- boolean (default: ``True``); whether
          to perform consistency checks

        TESTS::

            sage: from sage.modules.filtered_vector_space import FilteredVectorSpace_class
            sage: gens = [(1,0,0), (1,1,0), (1,2,0), (-1,-1, 0), (0,0,1)]
            sage: FilteredVectorSpace_class(QQ, 3, gens, {2:(0,1), oo:(4,)})
            QQ^3 >= QQ^1
            sage: FilteredVectorSpace_class(QQ, 3, gens, {2:(0,1), 3:(4,)})
            QQ^3 >= QQ^1 >= 0

        The trivial filtration::

            sage: FilteredVectorSpace_class(QQ, 3, gens, {}, QQ)
            0 in QQ^3

        The empty vector space::

            sage: FilteredVectorSpace_class(QQ, 0, [], {})
            0

        Higher-degree generators are automatically generators in lower degrees::

            sage: FilteredVectorSpace_class(QQ, 3, gens, {2:(4,), 3:(1,)})
            QQ^2 >= QQ^1 >= 0 in QQ^3
        """
    def change_ring(self, base_ring):
        """
        Return the same filtration over a different base ring.

        INPUT:

        - ``base_ring`` -- the new base ring

        OUTPUT:

        This method returns a new filtered vector space whose
        subspaces are defined by the same generators but over a
        different base ring.

        EXAMPLES::

            sage: V = FilteredVectorSpace(1, 0);  V
            QQ^1 >= 0
            sage: V.change_ring(RDF)
            RDF^1 >= 0
        """
    def ambient_vector_space(self):
        """
        Return the ambient (unfiltered) vector space.

        OUTPUT: a vector space

        EXAMPLES::

            sage: V = FilteredVectorSpace(1, 0)
            sage: V.ambient_vector_space()
            Vector space of dimension 1 over Rational Field
        """
    @cached_method
    def is_constant(self) -> bool:
        """
        Return whether the filtration is constant.

        OUTPUT: boolean; whether the filtered vector spaces are identical in
        all degrees

        EXAMPLES::

            sage: V = FilteredVectorSpace(2); V
            QQ^2
            sage: V.is_constant()
            True

            sage: V = FilteredVectorSpace(1, 0);  V
            QQ^1 >= 0
            sage: V.is_constant()
            False

            sage: V = FilteredVectorSpace({0:[(1,)]});  V
            QQ^1 >= 0
            sage: V.is_constant()
            False
        """
    def is_exhaustive(self) -> bool:
        """
        Return whether the filtration is exhaustive.

        A filtration `\\{F_d\\}` in an ambient vector space `V` is
        exhaustive if `\\cup F_d = V`. See also :meth:`is_separating`.

        OUTPUT: boolean

        EXAMPLES::

            sage: F = FilteredVectorSpace({0:[(1,1)]});  F
            QQ^1 >= 0 in QQ^2
            sage: F.is_exhaustive()
            False
            sage: G = FilteredVectorSpace(2, 0);  G
            QQ^2 >= 0
            sage: G.is_exhaustive()
            True
        """
    def is_separating(self) -> bool:
        """
        Return whether the filtration is separating.

        A filtration `\\{F_d\\}` in an ambient vector space `V` is
        exhaustive if `\\cap F_d = 0`. See also :meth:`is_exhaustive`.

        OUTPUT: boolean

        EXAMPLES::

            sage: F = FilteredVectorSpace({0:[(1,1)]});  F
            QQ^1 >= 0 in QQ^2
            sage: F.is_separating()
            True
            sage: G = FilteredVectorSpace({0:[(1,1,0)], oo:[(0,0,1)]});  G
            QQ^2 >= QQ^1 in QQ^3
            sage: G.is_separating()
            False
        """
    @cached_method
    def support(self):
        """
        Return the degrees in which there are non-trivial generators.

        OUTPUT:

        A tuple of integers (and plus infinity) in ascending
        order. The last entry is plus infinity if and only if the
        filtration is not separating (see :meth:`is_separating`).

        EXAMPLES::

            sage: G = FilteredVectorSpace({0:[(1,1,0)], 3:[(0,1,0)]});  G
            QQ^2 >= QQ^1 >= QQ^1 >= QQ^1 >= 0 in QQ^3
            sage: G.support()
            (0, 3)

            sage: G = FilteredVectorSpace({0:[(1,1,0)], 3:[(0,1,0)], oo:[(0,0,1)]});  G
            QQ^3 >= QQ^2 >= QQ^2 >= QQ^2 >= QQ^1
            sage: G.support()
            (0, 3, +Infinity)
        """
    @cached_method
    def min_degree(self):
        """
        Return the lowest degree of the filtration.

        OUTPUT:

        Integer or plus infinity. The largest degree `d` of the
        (descending) filtration such that the filtered vector space
        `F_d` is still equal to `F_{-\\infty}`.

        EXAMPLES::

            sage: FilteredVectorSpace(1, 3).min_degree()
            3
            sage: FilteredVectorSpace(2).min_degree()
            +Infinity
        """
    @cached_method
    def max_degree(self):
        """
        Return the highest degree of the filtration.

        OUTPUT:

        Integer or minus infinity. The smallest degree of the
        filtration such that the filtration is constant to the right.

        EXAMPLES::

            sage: FilteredVectorSpace(1, 3).max_degree()
            4
            sage: FilteredVectorSpace({0:[[1]]}).max_degree()
            1
            sage: FilteredVectorSpace(3).max_degree()
            -Infinity
        """
    def get_degree(self, d):
        """
        Return the degree-``d`` entry of the filtration.

        INPUT:

        - ``d`` -- integer; the desired degree of the filtration

        OUTPUT:

        The degree-``d`` vector space in the filtration as subspace of
        the ambient space.

        EXAMPLES::

            sage: rays = [(1,0), (1,1), (1,2), (-1,-1)]
            sage: F = FilteredVectorSpace(rays, {3:[1], 1:[1,2]})
            sage: F.get_degree(2)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 1]
            sage: F.get_degree(oo)
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            sage: F.get_degree(-oo)
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
        """
    def graded(self, d):
        """
        Return the associated graded vectorspace.

        INPUT:

        - ``d`` -- integer; the degree

        OUTPUT: the quotient `G_d = F_d / F_{d+1}`

        EXAMPLES::

            sage: rays = [(1,0), (1,1), (1,2)]
            sage: F = FilteredVectorSpace(rays, {3:[1], 1:[1,2]})
            sage: F.graded(1)
            Vector space quotient V/W of dimension 1 over Rational Field where
            V: Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
            W: Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 1]
        """
    def presentation(self):
        """
        Return a presentation in term of generators of various degrees.

        OUTPUT:

        A pair consisting of generators and a filtration suitable as
        input to :func:`~construct_from_generators_indices`.

        EXAMPLES::

            sage: rays = [(1,0), (1,1), (1,2), (-1,-1)]
            sage: F = FilteredVectorSpace(rays, {0:[1, 2], 2:[3]});  F
            QQ^2 >= QQ^1 >= QQ^1 >= 0
            sage: F.presentation()
            (((0, 1), (1, 0), (1, 1)), {0: (1, 0), 2: (2,), +Infinity: ()})
        """
    def __eq__(self, other):
        """
        Return whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: V = FilteredVectorSpace(2, 0)
            sage: W = FilteredVectorSpace([(1,0),(0,1)], {0:[0, 1]})
            sage: V == W
            True
            sage: V is W
            False

            sage: W = FilteredVectorSpace([(1,0),(1,1)], {0:[1]})
            sage: V == W
            False

        TESTS::

            sage: # needs sage.geometry.polyhedron sage.schemes
            sage: P = toric_varieties.P2()
            sage: T_P = P.sheaves.tangent_bundle()
            sage: O_P = P.sheaves.trivial_bundle(1)
            sage: S1 = T_P + O_P
            sage: S2 = O_P + T_P
            sage: S1._filt[0].is_isomorphic(S2._filt[0])        # known bug
            True

            sage: FilteredVectorSpace(2, base_ring=QQ) == FilteredVectorSpace(2, base_ring=GF(5))
            False
        """
    def __ne__(self, other):
        """
        Return whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: V = FilteredVectorSpace(2, 0)
            sage: W = FilteredVectorSpace([(1,0),(0,1)], {0:[0, 1]})
            sage: V != W
            False

            sage: W = FilteredVectorSpace([(1,0),(1,1)], {0:[1]})
            sage: V != W
            True
        """
    def direct_sum(self, other):
        """
        Return the direct sum.

        INPUT:

        - ``other`` -- a filtered vector space

        OUTPUT: the direct sum as a filtered vector space

        EXAMPLES::

            sage: V = FilteredVectorSpace(2, 0)
            sage: W = FilteredVectorSpace({0:[(1,-1),(2,1)], 1:[(1,1)]})
            sage: V.direct_sum(W)
            QQ^4 >= QQ^1 >= 0
            sage: V + W    # syntactic sugar
            QQ^4 >= QQ^1 >= 0
            sage: V + V == FilteredVectorSpace(4, 0)
            True

            sage: W = FilteredVectorSpace([(1,-1),(2,1)], {1:[0,1], 2:[1]})
            sage: V + W
            QQ^4 >= QQ^2 >= QQ^1 >= 0

        A suitable base ring is chosen if they do not match::

            sage: v = [(1,0), (0,1)]
            sage: F1 = FilteredVectorSpace(v, {0:[0], 1:[1]}, base_ring=QQ)
            sage: F2 = FilteredVectorSpace(v, {0:[0], 1:[1]}, base_ring=RDF)
            sage: F1 + F2                                                               # needs scipy
            RDF^4 >= RDF^2 >= 0
        """
    __add__ = direct_sum
    def tensor_product(self, other):
        """
        Return the graded tensor product.

        INPUT:

        - ``other`` -- a filtered vector space

        OUTPUT:

        The graded tensor product, that is, the tensor product of a
        generator of degree `d_1` with a generator in degree `d_2` has
        degree `d_1 + d_2`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(1, 1)
            sage: F2 = FilteredVectorSpace(1, 2)
            sage: F1.tensor_product(F2)
            QQ^1 >= 0
            sage: F1 * F2
            QQ^1 >= 0

            sage: F1.min_degree()
            1
            sage: F2.min_degree()
            2
            sage: (F1*F2).min_degree()
            3

        A suitable base ring is chosen if they do not match::

            sage: v = [(1,0), (0,1)]
            sage: F1 = FilteredVectorSpace(v, {0:[0], 1:[1]}, base_ring=QQ)
            sage: F2 = FilteredVectorSpace(v, {0:[0], 1:[1]}, base_ring=RDF)
            sage: F1 * F2                                                               # needs scipy
            RDF^4 >= RDF^3 >= RDF^1 >= 0
        """
    __mul__ = tensor_product
    def exterior_power(self, n):
        """
        Return the `n`-th graded exterior power.

        INPUT:

        - ``n`` -- integer; exterior product of how many copies of ``self``

        OUTPUT:

        The graded exterior product, that is, the wedge product of a
        generator of degree `d_1` with a generator in degree `d_2` has
        degree `d_1 + d_2`.

        EXAMPLES::

            sage: # needs sage.groups
            sage: F = FilteredVectorSpace(1, 1) + FilteredVectorSpace(1, 2);  F
            QQ^2 >= QQ^1 >= 0
            sage: F.exterior_power(1)
            QQ^2 >= QQ^1 >= 0
            sage: F.exterior_power(2)
            QQ^1 >= 0
            sage: F.exterior_power(3)
            0
            sage: F.wedge(2)
            QQ^1 >= 0
        """
    wedge = exterior_power
    def symmetric_power(self, n):
        """
        Return the `n`-th graded symmetric power.

        INPUT:

        - ``n`` -- integer; symmetric product of how many copies of
          ``self``

        OUTPUT:

        The graded symmetric product, that is, the symmetrization of a
        generator of degree `d_1` with a generator in degree `d_2` has
        degree `d_1 + d_2`.

        EXAMPLES::

            sage: F = FilteredVectorSpace(1, 1) + FilteredVectorSpace(1, 2);  F
            QQ^2 >= QQ^1 >= 0
            sage: F.symmetric_power(2)
            QQ^3 >= QQ^2 >= QQ^1 >= 0
        """
    def dual(self):
        """
        Return the dual filtered vector space.

        OUTPUT:

        The graded dual, that is, the dual of a degree-`d` subspace is
        a set of linear constraints in degree `-d+1`. That is, the
        dual generators live in degree `-d`.

        EXAMPLES::

            sage: gens = identity_matrix(3).rows()
            sage: F = FilteredVectorSpace(gens, {0:[0,1,2], 2:[0]});  F
            QQ^3 >= QQ^1 >= QQ^1 >= 0
            sage: F.support()
            (0, 2)

            sage: F.dual()
            QQ^3 >= QQ^2 >= QQ^2 >= 0
            sage: F.dual().support()
            (-2, 0)
        """
    def shift(self, deg):
        """
        Return a filtered vector space with degrees shifted by a constant.

        EXAMPLES::

            sage: gens = identity_matrix(3).rows()
            sage: F = FilteredVectorSpace(gens, {0:[0,1,2], 2:[0]});  F
            QQ^3 >= QQ^1 >= QQ^1 >= 0
            sage: F.support()
            (0, 2)
            sage: F.shift(-5).support()
            (-5, -3)
        """
    def random_deformation(self, epsilon=None):
        """
        Return a random deformation.

        INPUT:

        - ``epsilon`` -- a number in the base ring

        OUTPUT:

        A new filtered vector space where the generators of the
        subspaces are moved by ``epsilon`` times a random vector.

        EXAMPLES::

            sage: gens = identity_matrix(3).rows()
            sage: F = FilteredVectorSpace(gens, {0:[0,1,2], 2:[0]});  F
            QQ^3 >= QQ^1 >= QQ^1 >= 0
            sage: F.get_degree(2)
            Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [1 0 0]
            sage: G = F.random_deformation(1/50);  G
            QQ^3 >= QQ^1 >= QQ^1 >= 0
            sage: D = G.get_degree(2)
            sage: D.degree()
            3
            sage: v = D.basis_matrix()[0]
            sage: v[0]
            1

            sage: while F.random_deformation(1/50).get_degree(2).matrix() == matrix([1, 0, 0]):
            ....:     pass
        """
