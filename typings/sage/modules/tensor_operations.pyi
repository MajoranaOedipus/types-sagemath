from sage.matrix.constructor import matrix as matrix
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import FreeModule_ambient_field as FreeModule_ambient_field
from sage.rings.integer_ring import ZZ as ZZ

def symmetrized_coordinate_sums(dim, n):
    """
    Return formal symmetrized sum of multi-indices.

    INPUT:

    - ``dim`` -- integer; the dimension (range of each index)

    - ``n`` -- integer; the total number of indices

    OUTPUT:

    A symmetrized formal sum of multi-indices (tuples of integers)

    EXAMPLES::

        sage: from sage.modules.tensor_operations import symmetrized_coordinate_sums
        sage: symmetrized_coordinate_sums(2, 2)
        ((0, 0), (0, 1) + (1, 0), (1, 1))
    """
def antisymmetrized_coordinate_sums(dim, n):
    """
    Return formal anti-symmetrized sum of multi-indices.

    INPUT:

    - ``dim`` -- integer; the dimension (range of each index)

    - ``n`` -- integer; the total number of indices

    OUTPUT:

    An anti-symmetrized formal sum of multi-indices (tuples of integers)

    EXAMPLES::

        sage: from sage.modules.tensor_operations import antisymmetrized_coordinate_sums
        sage: antisymmetrized_coordinate_sums(3, 2)                                     # needs sage.groups
        ((0, 1) - (1, 0), (0, 2) - (2, 0), (1, 2) - (2, 1))
    """

class VectorCollection(FreeModule_ambient_field):
    """
    An ordered collection of generators of a vector space.

    This is like a list of vectors, but with extra argument checking.

    .. warning::

        This class is only used as a base class for filtered vector
        spaces. You should not use it yourself.

    INPUT:

    - ``dim`` -- integer; the dimension of the ambient vector space

    - ``base_ring`` -- a field; the base field of the ambient vector space

    - ``rays`` -- any list/iterable of things than can be converted
      into vectors of the ambient vector space. These will be used to
      span the subspaces of the filtration. Must span the ambient
      vector space.

    EXAMPLES::

        sage: from sage.modules.tensor_operations import VectorCollection
        sage: R = VectorCollection([(1,0), (0,1), (1,2)], QQ, 2);  R
        Vector space of dimension 2 over Rational Field

    TESTS::

        sage: R.vectors()
        ((1, 0), (0, 1), (1, 2))
        sage: r = R._vectors[0]
        sage: type(r)
        <class 'sage.modules.vector_rational_dense.Vector_rational_dense'>
        sage: r.parent() is R
        True
        sage: r.is_immutable()
        True
    """
    def __init__(self, vector_collection, base_ring, dim) -> None:
        """
        EXAMPLES::

            sage: from sage.modules.tensor_operations import VectorCollection
            sage: VectorCollection([(1,0), (4,1), (1,2)], QQ, 2)
            Vector space of dimension 2 over Rational Field
        """
    def vectors(self):
        """
        Return the collection of vectors.

        OUTPUT:

        A tuple of vectors. The vectors that were specified in the
        constructor, in the same order.

        EXAMPLES::

            sage: from sage.modules.tensor_operations import VectorCollection
            sage: V = VectorCollection([(1,0), (0,1), (1,2)], QQ, 2)
            sage: V.vectors()
            ((1, 0), (0, 1), (1, 2))
        """
    def n_vectors(self):
        """
        Return the number of vectors.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.modules.tensor_operations import VectorCollection
            sage: V = VectorCollection([(1,0), (0,1), (1,2)], QQ, 2)
            sage: V.n_vectors()
            3
        """

class TensorOperation(VectorCollection):
    """
    Auxiliary class to compute the tensor product of two
    :class:`VectorCollection` objects.

    .. warning::

        This class is only used as a base class for filtered vector
        spaces. You should not use it yourself.

    INPUT:

    - ``vector_collections`` -- a nonempty list/tuple/iterable of
      :class:`VectorCollection` objects

    - ``operation`` -- string; the tensor operation. Currently allowed
      values are ``'product'``, ``'symmetric'``, and ``'antisymmetric'``.

    .. TODO::

        More general tensor operations (specified by Young tableaux)
        should be implemented.

    EXAMPLES::

        sage: from sage.modules.tensor_operations import VectorCollection, TensorOperation
        sage: R = VectorCollection([(1,0), (1,2), (-1,-2)], QQ, 2)
        sage: S = VectorCollection([(1,), (-1,)], QQ, 1)
        sage: R_tensor_S = TensorOperation([R, S])
        sage: R_tensor_S.index_map(0, 0)
        0
        sage: matrix(ZZ, 3, 2, lambda i,j: R_tensor_S.index_map(i, j))
        [0 1]
        [2 3]
        [3 2]
        sage: R_tensor_S.vectors()
        ((1, 0), (-1, 0), (1, 2), (-1, -2))
    """
    def __init__(self, vector_collections, operation: str = 'product') -> None:
        """
        EXAMPLES::

            sage: from sage.modules.tensor_operations import VectorCollection, TensorOperation
            sage: R = VectorCollection([(1,0), (5,2), (-1,-2)], QQ, 2)
            sage: S = VectorCollection([(1,), (-1,)], QQ, 1)
            sage: TensorOperation([S, R])
            Vector space of dimension 2 over Rational Field
        """
    def index_map(self, *i):
        """
        Return the result of the tensor operation.

        INPUT:

        - ``*i`` -- list of integers. The indices (in the
          corresponding factor of the tensor operation) of the domain
          vector.

        OUTPUT:

        The index (in :meth:`vectors`) of the image of the tensor
        product/operation acting on the domain vectors indexed by `i`.

        ``None`` is returned if the tensor operation maps the
        generators to zero (usually because of antisymmetry).

        EXAMPLES::

            sage: from sage.modules.tensor_operations import             ....:      VectorCollection, TensorOperation
            sage: R = VectorCollection([(1,0), (1,2), (-1,-2)], QQ, 2)
            sage: Sym3_R = TensorOperation([R]*3, 'symmetric')

        The symmetric product of the first vector ``(1,0)``, the
        second vector ``(1,2)``, and the third vector ``(-1,-2)``
        equals the vector with index number 4 (that is, the fifth) in
        the symmetric product vector collection::

            sage: Sym3_R.index_map(0, 1, 2)
            4

        In suitable coordinates, this is the vector::

            sage: Sym3_R.vectors()[4]
            (-1, -4, -4, 0)

        The product is symmetric::

            sage: Sym3_R.index_map(2, 0, 1)
            4
            sage: Sym3_R.index_map(2, 1, 0)
            4

        As another example, here is the rank-2 determinant::

            sage: from sage.modules.tensor_operations import             ....:      VectorCollection, TensorOperation
            sage: R = VectorCollection([(1,0), (0,1), (-2,-3)], QQ, 2)
            sage: detR = TensorOperation([R]*2, 'antisymmetric')                        # needs sage.groups
            sage: detR.index_map(1, 0)                                                  # needs sage.groups
            0
            sage: detR.index_map(0, 1)                                                  # needs sage.groups
            0

        TESTS::

            sage: sorted(detR._index_map.items())                                       # needs sage.groups
            [((0, 1), 0), ((0, 2), 1), ((1, 2), 2)]
            sage: detR.vectors()                                                        # needs sage.groups
            ((1), (-3), (2))
        """
    def preimage(self):
        """
        A choice of pre-image multi-indices.

        OUTPUT:

        A list of multi-indices (tuples of integers) whose image is
        the entire image under the :meth:`index_map`.

        EXAMPLES::

            sage: from sage.modules.tensor_operations import             ....:      VectorCollection, TensorOperation
            sage: R = VectorCollection([(1,0), (0,1), (-2,-3)], QQ, 2)
            sage: detR = TensorOperation([R]*2, 'antisymmetric')                        # needs sage.groups
            sage: sorted(detR.preimage())                                               # needs sage.groups
            [(0, 1), (0, 2), (1, 2)]
            sage: sorted(detR.codomain())                                               # needs sage.groups
            [0, 1, 2]
        """
    def codomain(self):
        """
        The codomain of the index map.

        OUTPUT: list of integers; the image of :meth:`index_map`

        EXAMPLES::

            sage: from sage.modules.tensor_operations import             ....:      VectorCollection, TensorOperation
            sage: R = VectorCollection([(1,0), (0,1), (-2,-3)], QQ, 2)
            sage: detR = TensorOperation([R]*2, 'antisymmetric')                        # needs sage.groups
            sage: sorted(detR.preimage())                                               # needs sage.groups
            [(0, 1), (0, 2), (1, 2)]
            sage: sorted(detR.codomain())                                               # needs sage.groups
            [0, 1, 2]
        """
