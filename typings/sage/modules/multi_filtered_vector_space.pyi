from sage.categories.fields import Fields as Fields
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.filtered_vector_space import FilteredVectorSpace as FilteredVectorSpace
from sage.modules.free_module import FreeModule_ambient_field as FreeModule_ambient_field, VectorSpace as VectorSpace
from sage.rings.infinity import infinity as infinity, minus_infinity as minus_infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def MultiFilteredVectorSpace(arg, base_ring=None, check: bool = True):
    """
    Construct a multi-filtered vector space.

    INPUT:

    - ``arg`` -- either a non-empty dictionary of filtrations or an
      integer. The latter is interpreted as the vector space
      dimension, and the indexing set of the filtrations is empty.

    - ``base_ring`` -- a field (default: ``'None'``). The
      base field of the vector space. Must be a field. If not
      specified, the base field is derived from the filtrations.

    - ``check`` -- boolean (default: ``True``); whether
      to perform consistency checks

    EXAMPLES::

        sage: MultiFilteredVectorSpace(3, QQ)
        Unfiltered QQ^3

        sage: F1 = FilteredVectorSpace(2, 1)
        sage: F2 = FilteredVectorSpace(2, 3)
        sage: V = MultiFilteredVectorSpace({1:F1, 2:F2});  V
        Filtrations
            1: QQ^2 >=  0   >=  0   >= 0
            2: QQ^2 >= QQ^2 >= QQ^2 >= 0
    """

class MultiFilteredVectorSpace_class(FreeModule_ambient_field):
    def __init__(self, base_ring, dim, filtrations, check: bool = True) -> None:
        """
        Python constructor.

        .. warning::

            Use :func:`MultiFilteredVectorSpace` to construct
            multi-filtered vector spaces.

        INPUT:

        - ``base_ring`` -- the base ring

        - ``dim`` -- integer; the dimension of the ambient vector space

        - ``filtrations`` -- dictionary whose values are filtrations

        - ``check`` -- boolean (default: ``True``); whether to perform
          additional consistency checks

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2});  V
            Filtrations
                1: QQ^2 >=  0   >=  0   >= 0
                2: QQ^2 >= QQ^2 >= QQ^2 >= 0
        """
    @cached_method
    def index_set(self):
        """
        Return the allowed indices for the different filtrations.

        OUTPUT: set

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.index_set()
            {1, 2}
        """
    def change_ring(self, base_ring):
        """
        Return the same multi-filtration over a different base ring.

        INPUT:

        - ``base_ring`` -- the new base ring

        OUTPUT:

        This method returns a new multi-filtered vector space whose
        subspaces are defined by the same generators but over a
        different base ring.

        EXAMPLES::

            sage: V = FilteredVectorSpace(2, 0)
            sage: W = FilteredVectorSpace(2, 2)
            sage: F = MultiFilteredVectorSpace({'a':V, 'b':W});  F
            Filtrations
                a: QQ^2 >=  0   >=  0   >= 0
                b: QQ^2 >= QQ^2 >= QQ^2 >= 0
            sage: F.change_ring(RDF)
            Filtrations
                a: RDF^2 >=   0   >=   0   >= 0
                b: RDF^2 >= RDF^2 >= RDF^2 >= 0

            sage: MultiFilteredVectorSpace(3, base_ring=QQ).change_ring(RR)
            Unfiltered RR^3
        """
    def ambient_vector_space(self):
        """
        Return the ambient (unfiltered) vector space.

        OUTPUT: a vector space

        EXAMPLES::

            sage: V = FilteredVectorSpace(2, 0)
            sage: W = FilteredVectorSpace(2, 2)
            sage: F = MultiFilteredVectorSpace({'a':V, 'b':W})
            sage: F.ambient_vector_space()
            Vector space of dimension 2 over Rational Field
        """
    @cached_method
    def is_constant(self) -> bool:
        """
        Return whether the multi-filtration is constant.

        OUTPUT: boolean; whether the each filtration is constant, see
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.is_constant`

        EXAMPLES::

            sage: V = FilteredVectorSpace(2, 0)
            sage: W = FilteredVectorSpace(2, 2)
            sage: F = MultiFilteredVectorSpace({'a':V, 'b':W});  F
            Filtrations
                a: QQ^2 >=  0   >=  0   >= 0
                b: QQ^2 >= QQ^2 >= QQ^2 >= 0
            sage: F.is_constant()
            False
        """
    def is_exhaustive(self) -> bool:
        """
        Return whether the multi-filtration is exhaustive.

        A filtration `\\{F_d\\}` in an ambient vector space `V` is
        exhaustive if `\\cup F_d = V`. See also :meth:`is_separating`.

        OUTPUT: boolean; whether each filtration is constant, see
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.is_exhaustive`

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.is_exhaustive()
            True
        """
    def is_separating(self) -> bool:
        """
        Return whether the multi-filtration is separating.

        A filtration `\\{F_d\\}` in an ambient vector space `V` is
        exhaustive if `\\cap F_d = 0`. See also :meth:`is_exhaustive`.

        OUTPUT: boolean; whether each filtration is separating, see
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.is_separating`

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.is_separating()
            True
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

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.support()
            (1, 3)
        """
    @cached_method
    def min_degree(self):
        """
        Return the lowest degree of the filtration.

        OUTPUT:

        Integer or plus infinity. The largest degree `d` of the
        (descending) filtrations such that, for each individual
        filtration, the filtered vector space `F_d` still equal to
        `F_{-\\infty}`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.min_degree()
            1
        """
    @cached_method
    def max_degree(self):
        """
        Return the highest degree of the filtration.

        OUTPUT:

        Integer or minus infinity. The smallest degree of the
        filtrations such that the filtrations are constant to the
        right.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.max_degree()
            4
        """
    def get_filtration(self, key):
        """
        Return the filtration indexed by ``key``.

        OUTPUT: a filtered vector space

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.get_filtration(2)
            QQ^2 >= 0
        """
    def get_degree(self, key, deg):
        """
        Return one filtered vector space.

        INPUT:

        - ``key`` -- an element of the :meth:`index_set`; specifies
          which filtration

        - ``d`` -- integer; the desired degree of the filtration

        OUTPUT:

        The vector space of degree ``deg`` in the filtration indexed
        by ``key`` as subspace of the ambient space.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(2, 3)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.get_degree(2, 0)
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
        """
    def graded(self, key, deg):
        """
        Return the associated graded vector space.

        INPUT:

        - ``key`` -- an element of the :meth:`index_set`; specifies
          which filtration

        - ``d`` -- integer; the desired degree of the filtration

        OUTPUT:

        The quotient `G_d = F_d / F_{d+1}` of the filtration `F`
        corresponding to ``key``.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V.graded(2, 3)
            Vector space quotient V/W of dimension 1 over Rational Field where
            V: Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            W: Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
        """
    def __eq__(self, other):
        """
        Return whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V == MultiFilteredVectorSpace({2:F2, 1:F1})
            True
            sage: V == MultiFilteredVectorSpace({'a':F1, 'b':F2})
            False
        """
    def __ne__(self, other):
        """
        Return whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({1:F1, 2:F2})
            sage: V != MultiFilteredVectorSpace({2:F2, 1:F1})
            False
            sage: V != MultiFilteredVectorSpace({'a':F1, 'b':F2})
            True
        """
    def direct_sum(self, other):
        """
        Return the direct sum.

        INPUT:

        - ``other`` -- a multi-filtered vector space with the same
          :meth:`index_set`

        OUTPUT:

        The direct sum as a multi-filtered vector space. See
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.direct_sum`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: G1 = FilteredVectorSpace(1, 1)
            sage: G2 = FilteredVectorSpace(1, 3)
            sage: W = MultiFilteredVectorSpace({'a':G1, 'b':G2})
            sage: V.direct_sum(W)
            Filtrations
                a: QQ^3 >= QQ^3 >=  0   >=  0   >= 0
                b: QQ^3 >= QQ^2 >= QQ^2 >= QQ^2 >= 0
            sage: V + W   # syntactic sugar
            Filtrations
                a: QQ^3 >= QQ^3 >=  0   >=  0   >= 0
                b: QQ^3 >= QQ^2 >= QQ^2 >= QQ^2 >= 0
        """
    __add__ = direct_sum
    def tensor_product(self, other):
        """
        Return the graded tensor product.

        INPUT:

        - ``other`` -- a multi-filtered vector space with the same
          :meth:`index_set`

        OUTPUT:

        The tensor product of ``self`` and ``other`` as a
        multi-filtered vector space. See
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.tensor_product`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: G1 = FilteredVectorSpace(1, 1)
            sage: G2 = FilteredVectorSpace(1, 3)
            sage: W = MultiFilteredVectorSpace({'a':G1, 'b':G2})
            sage: V.tensor_product(W)
            Filtrations
                a: QQ^2 >=  0   >=  0   >=  0   >=  0   >= 0
                b: QQ^2 >= QQ^2 >= QQ^1 >= QQ^1 >= QQ^1 >= 0
            sage: V * W   # syntactic sugar
            Filtrations
                a: QQ^2 >=  0   >=  0   >=  0   >=  0   >= 0
                b: QQ^2 >= QQ^2 >= QQ^1 >= QQ^1 >= QQ^1 >= 0
        """
    __mul__ = tensor_product
    def exterior_power(self, n):
        """
        Return the `n`-th graded exterior power.

        INPUT:

        - ``n`` -- integer; exterior product of how many copies of ``self``

        OUTPUT:

        The exterior power as a multi-filtered vector space. See
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.exterior_power`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: V.exterior_power(2)  # long time
            Filtrations
                a: QQ^1 >=  0   >= 0
                b: QQ^1 >= QQ^1 >= 0
        """
    wedge = exterior_power
    def symmetric_power(self, n):
        """
        Return the `n`-th graded symmetric power.

        INPUT:

        - ``n`` -- integer; symmetric product of how many copies of ``self``

        OUTPUT:

        The symmetric power as a multi-filtered vector space. See
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.symmetric_power`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: V.symmetric_power(2)
            Filtrations
                a: QQ^3 >= QQ^3 >= QQ^3 >=  0   >=  0   >=  0   >=  0   >= 0
                b: QQ^3 >= QQ^2 >= QQ^2 >= QQ^2 >= QQ^1 >= QQ^1 >= QQ^1 >= 0
        """
    def dual(self):
        """
        Return the dual.

        OUTPUT:

        The dual as a multi-filtered vector space. See
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.dual`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: V.dual()
            Filtrations
                a: QQ^2 >= QQ^2 >= QQ^2 >=  0   >= 0
                b: QQ^2 >= QQ^1 >= QQ^1 >= QQ^1 >= 0
        """
    def shift(self, deg):
        """
        Return a filtered vector space with degrees shifted by a constant.

        OUTPUT:

        The shift of ``self``. See
        :meth:`~sage.modules.filtered_vector_space.FilteredVectorSpace_class.shift`.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: V.support()
            (0, 1, 3)
            sage: V.shift(-5).support()
            (-5, -4, -2)
        """
    def random_deformation(self, epsilon=None):
        """
        Return a random deformation.

        INPUT:

        - ``epsilon`` -- a number in the base ring

        OUTPUT:

        A new multi-filtered vector space where the generating vectors
        of subspaces are moved by ``epsilon`` times a random vector.

        EXAMPLES::

            sage: F1 = FilteredVectorSpace(2, 1)
            sage: F2 = FilteredVectorSpace(1, 3) + FilteredVectorSpace(1,0)
            sage: V = MultiFilteredVectorSpace({'a':F1, 'b':F2})
            sage: V.get_degree('b',1)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            sage: D = V.random_deformation(1/100).get_degree('b',1)
            sage: D.degree()
            2
            sage: D.dimension()
            1
            sage: D.matrix()[0, 0]
            1

            sage: while V.random_deformation(1/100).get_degree('b',1).matrix() == matrix([1, 0]):
            ....:     pass
        """
