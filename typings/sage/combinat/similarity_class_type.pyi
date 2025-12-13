from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import divisors as divisors, factorial as factorial, moebius as moebius
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.misc import IterableFunctionCall as IterableFunctionCall
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.misc.cachefunc import cached_function as cached_function, cached_in_parent_method as cached_in_parent_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.misc_c import prod as prod
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element, Matrix as Matrix
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

@cached_function
def fq(n, q=None):
    """
    Return `(1-q^{-1}) (1-q^{-2}) \\cdots (1-q^{-n})`.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``q`` -- integer or an indeterminate

    OUTPUT: a rational function in ``q``

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import fq
        sage: fq(0)
        1
        sage: fq(3)
        (q^6 - q^5 - q^4 + q^2 + q - 1)/q^6
    """
@cached_function
def primitives(n, invertible: bool = False, q=None):
    """
    Return the number of similarity classes of simple matrices
    of order ``n`` with entries in a finite field of order ``q``.
    This is the same as the number of irreducible polynomials
    of degree `d`.

    If ``invertible`` is ``True``, then only the number of
    similarity classes of invertible matrices is returned.

    .. NOTE::

        All primitive classes are invertible unless ``n`` is `1`.

    INPUT:

    - ``n`` -- positive integer

    - ``invertible`` -- boolean; if set, only number of nonzero classes is returned

    - ``q`` -- integer or an indeterminate

    OUTPUT: a rational function of the variable ``q``

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import primitives
        sage: primitives(1)
        q
        sage: primitives(1, invertible = True)
        q - 1
        sage: primitives(4)
        1/4*q^4 - 1/4*q^2
        sage: primitives(4, invertible = True)
        1/4*q^4 - 1/4*q^2
    """
@cached_function
def order_of_general_linear_group(n, q=None):
    """
    Return the cardinality of the group of `n \\times n` invertible matrices
    with entries in a field of order ``q``.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``q`` -- integer or an indeterminate

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import order_of_general_linear_group
        sage: order_of_general_linear_group(0)
        1
        sage: order_of_general_linear_group(2)
        q^4 - q^3 - q^2 + q
    """
@cached_function
def centralizer_algebra_dim(la):
    """
    Return the dimension of the centralizer algebra in `M_n(\\GF{q})`
    of a nilpotent matrix whose Jordan blocks are given by ``la``.

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import centralizer_algebra_dim
        sage: centralizer_algebra_dim(Partition([2, 1]))
        5

    .. NOTE::

        If it is a list, ``la`` is expected to be sorted in decreasing order.
    """
@cached_function
def centralizer_group_cardinality(la, q=None):
    """
    Return the cardinality of the centralizer group in `GL_n(\\GF{q})`
    of a nilpotent matrix whose Jordan blocks are given by ``la``.

    INPUT:

    - ``lambda`` -- a partition

    - ``q`` -- an integer or an indeterminate

    OUTPUT: a polynomial function of ``q``

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import centralizer_group_cardinality
        sage: q = ZZ['q'].gen()
        sage: centralizer_group_cardinality(Partition([2, 1]))
        q^5 - 2*q^4 + q^3
    """
def invariant_subspace_generating_function(la, q=None, t=None):
    """
    Return the invariant subspace generating function of a nilpotent matrix with
    Jordan block sizes given by ``la``.

    INPUT:

    - ``la`` -- a partition
    - ``q`` -- (optional) an integer or an inderminate
    - ``t`` -- (optional) an indeterminate

    OUTPUT: a polynomial in ``t`` whose coefficients are polynomials in ``q``

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import invariant_subspace_generating_function
        sage: invariant_subspace_generating_function([2,2])
        t^4 + (q + 1)*t^3 + (q^2 + q + 1)*t^2 + (q + 1)*t + 1
    """

class PrimarySimilarityClassType(Element, metaclass=InheritComparisonClasscallMetaclass):
    """
    A primary similarity class type is a pair consisting of a partition and a positive
    integer.

    For a partition `\\lambda` and a positive integer `d`, the primary similarity
    class type `(d, \\lambda)` represents similarity classes of square matrices
    of order `|\\lambda| \\cdot d` with entries in a finite field of order `q`
    which correspond to the `\\GF{q[t]}`-module

    .. MATH::

        \\frac{\\GF{q[t]}}{p(t)^{\\lambda_1} } \\oplus
        \\frac{\\GF{q[t]}}{p(t)^{\\lambda_2}} \\oplus \\dotsb

    for some irreducible polynomial `p(t)` of degree `d`.
    """
    @staticmethod
    def __classcall_private__(cls, deg, par):
        """
        Create a primary similarity class type.

        EXAMPLES::

            sage: PrimarySimilarityClassType(2, [3, 2, 1])
            [2, [3, 2, 1]]

        The parent class is the class of primary similarity class types of order
        `d |\\lambda|`::

            sage: PT = PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT.parent().size()
            12
        """
    def __init__(self, parent, deg, par) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: elt =  PrimarySimilarityClassType(2, [3, 2, 1])
            sage: TestSuite(elt).run()
        """
    def __hash__(self):
        """
        TESTS::

            sage: PT1 = PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT2 = PrimarySimilarityClassType(3, [3, 2, 1])
            sage: PT3 = PrimarySimilarityClassType(2, [4, 2, 1])
            sage: hash(PT1) == hash(PrimarySimilarityClassType(2, [3, 2, 1]))
            True
            sage: abs(hash(PT1) - hash(PT2)) == 1
            True
            sage: hash(PT1) == hash(PT3)
            False
            sage: hash(PT2) == hash(PT3)
            False
        """
    def __eq__(self, other):
        """
        Check equality.

        EXAMPLES::

            sage: PT1 =  PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT2 =  PrimarySimilarityClassType(2, Partition([3, 2, 1]))
            sage: PT1 == PT2
            True
            sage: PT3 =  PrimarySimilarityClassType(3, [3, 2, 1])
            sage: PT1 == PT3
            False
            sage: PT4 =  PrimarySimilarityClassType(2, [3, 2, 1, 0])
            sage: PT1 == PT4
            True
            sage: PT5 = PrimarySimilarityClassType(2, [4, 2, 1])
            sage: PT1 == PT5
            False
        """
    def __ne__(self, other):
        """
        TESTS::

            sage: PT1 =  PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT2 =  PrimarySimilarityClassType(2, Partition([3, 2, 1]))
            sage: PT1 != PT2
            False
            sage: PT3 =  PrimarySimilarityClassType(3, [3, 2, 1])
            sage: PT1 != PT3
            True
        """
    def size(self):
        """
        Return the size of ``self``.

        EXAMPLES::

            sage: PT = PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT.size()
            12
        """
    def degree(self):
        """
        Return degree of ``self``.

        EXAMPLES::

            sage: PT = PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT.degree()
            2
        """
    def partition(self):
        """
        Return partition corresponding to ``self``.

        EXAMPLES::

            sage: PT = PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT.partition()
            [3, 2, 1]
        """
    def centralizer_algebra_dim(self):
        """
        Return the dimension of the algebra of matrices which commute with a
        matrix of type ``self``.

        For a partition `(d, \\lambda)` this dimension is given by
        `d(\\lambda_1 + 3\\lambda_2 + 5\\lambda_3 + \\cdots)`.

        EXAMPLES::

            sage: PT = PrimarySimilarityClassType(2, [3, 2, 1])
            sage: PT.centralizer_algebra_dim()
            28
        """
    @cached_in_parent_method
    def statistic(self, func, q=None):
        """
        Return `n_{\\lambda}(q^d)` where `n_{\\lambda}` is the value returned by
        ``func`` upon input `\\lambda`, if ``self`` is `(d, \\lambda)`.

        EXAMPLES::

            sage: PT = PrimarySimilarityClassType(2, [3, 1])
            sage: q = ZZ['q'].gen()
            sage: PT.statistic(lambda la:q**la.size(), q = q)
            q^8
        """
    @cached_in_parent_method
    def centralizer_group_card(self, q=None):
        """
        Return the cardinality of the centralizer group of a matrix of type
        ``self`` in a field of order ``q``.

        INPUT:

        - ``q`` -- integer or an indeterminate

        EXAMPLES::

            sage: PT = PrimarySimilarityClassType(1, [])
            sage: PT.centralizer_group_card()
            1
            sage: PT = PrimarySimilarityClassType(2, [1, 1])
            sage: PT.centralizer_group_card()
            q^8 - q^6 - q^4 + q^2
        """
    def invariant_subspace_generating_function(self, q=None, t=None):
        """
        Return the invariant subspace generating function of ``self``.

        INPUT:

        - ``q`` -- (optional) an integer or an inderminate
        - ``t`` -- (optional) an indeterminate

        EXAMPLES::

            sage: PrimarySimilarityClassType(1, [2, 2]).invariant_subspace_generating_function()
            t^4 + (q + 1)*t^3 + (q^2 + q + 1)*t^2 + (q + 1)*t + 1
        """

class PrimarySimilarityClassTypes(UniqueRepresentation, Parent):
    """
    All primary similarity class types of size ``n`` whose degree is greater
    than that of ``min`` or whose degree is that of ``min`` and  whose partition
    is less than of ``min`` in lexicographic order.

    A primary similarity class type of size `n` is a pair `(\\lambda, d)`
    consisting of a partition `\\lambda` and a positive integer `d` such that
    `|\\lambda| d = n`.

    INPUT:

    - ``n`` -- positive integer
    - ``min`` -- a primary matrix type of size ``n``

    EXAMPLES:

    If ``min`` is not specified, then the class of all primary similarity class
    types of size ``n`` is created::

        sage: PTC = PrimarySimilarityClassTypes(2)
        sage: for PT in PTC:
        ....:     print(PT)
        [1, [2]]
        [1, [1, 1]]
        [2, [1]]

    If ``min`` is specified, then the class consists of only those primary
    similarity class types whose degree is greater than that of ``min`` or whose
    degree is that of ``min`` and  whose partition is less than of ``min`` in
    lexicographic order::

        sage: PTC = PrimarySimilarityClassTypes(2, min = PrimarySimilarityClassType(1, [1, 1]))
        sage: for PT in PTC:
        ....:     print(PT)
        [1, [1, 1]]
        [2, [1]]
    """
    @staticmethod
    def __classcall_private__(cls, n, min=None):
        """
        Create the class of vector partitions of ``vec`` where all parts
        are greater than or equal to the vector ``min``.

        EXAMPLES::

            sage: PTC1 = PrimarySimilarityClassTypes(2)
            sage: PTC2 = PrimarySimilarityClassTypes(2, min = PrimarySimilarityClassType(1, [2]))
            sage: PTC1 is PTC2
            True
        """
    def __init__(self, n, min) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PTC = PrimarySimilarityClassTypes(2)
            sage: TestSuite(PTC).run()
        """
    Element = PrimarySimilarityClassType
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: PTC = PrimarySimilarityClassTypes(2)
            sage: PTC.cardinality()
            3
        """
    def size(self):
        """
        Return size of elements of ``self``.

        The size of a primary similarity class type `(d, \\lambda)` is
        `d |\\lambda|`.

        EXAMPLES::

            sage: PTC = PrimarySimilarityClassTypes(2)
            sage: PTC.size()
            2
        """

class SimilarityClassType(CombinatorialElement):
    """
    A similarity class type.

    A matrix type is a multiset of primary similarity class types.

    INPUT:

    - ``tau`` -- list of primary similarity class types or a square matrix
      over a finite field

    EXAMPLES::

        sage: tau1 = SimilarityClassType([[3, [3, 2, 1]], [2, [2, 1]]]); tau1
        [[2, [2, 1]], [3, [3, 2, 1]]]

        sage: SimilarityClassType(Matrix(GF(2), [[1,1],[0,1]]))
        [[1, [2]]]
    """
    @staticmethod
    def __classcall_private__(cls, tau):
        """
        Create a similarity class type.

        EXAMPLES:

        The input can be a list of lists or a list of primary similarity class
        types, and the order in which this list is given does not matter::

            sage: tau1 = SimilarityClassType([[3, [3, 2, 1]], [2, [2, 1]]]); tau1
            [[2, [2, 1]], [3, [3, 2, 1]]]
            sage: types = [PrimarySimilarityClassType(2, [2, 1]), PrimarySimilarityClassType(3, [3, 2, 1])]
            sage: tau2 = SimilarityClassType(types)
            sage: tau1 == tau2
            True

        The input can also be a matrix with entries in a finite field::

            sage: SimilarityClassType(Matrix(GF(2), [[1,1],[0,1]]))
            [[1, [2]]]

        The parent class is the class of similarity class types of the sum of
        the sizes of the primary matrix types in ``tau``::

            sage: tau = SimilarityClassType([[3, [3, 2, 1]], [2, [2, 1]]])
            sage: tau.parent().size()
            24
        """
    def __init__(self, parent, tau) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: elt =  SimilarityClassType([[3, [3, 2, 1]], [2, [2, 1]]])
            sage: TestSuite(elt).run()
        """
    def size(self):
        """
        Return the sum of the sizes of the primary parts of ``self``.

        EXAMPLES::

            sage: tau = SimilarityClassType([[3, [3, 2, 1]], [2, [2, 1]]])
            sage: tau.size()
            24
        """
    def centralizer_algebra_dim(self):
        """
        Return the dimension of the algebra of matrices which commute with a
        matrix of type ``self``.

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1]], [1, [1]]])
            sage: tau.centralizer_algebra_dim()
            2
        """
    def centralizer_group_card(self, q=None):
        """
        Return the cardinality of the group of matrices in `GL_n(\\GF{q})`
        which commute with a matrix of type ``self``.

        INPUT:

        - ``q`` -- integer or an indeterminate

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1]], [1, [1]]])
            sage: tau.centralizer_group_card()
            q^2 - 2*q + 1
        """
    def as_partition_dictionary(self):
        """
        Return a dictionary whose keys are the partitions of types occurring in
        ``self`` and the value at the key `\\lambda` is the partition formed by
        sorting the degrees of primary types with partition `\\lambda`.

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1]], [1, [1]]])
            sage: tau.as_partition_dictionary()
            {[1]: [1, 1]}
        """
    def number_of_classes(self, invertible: bool = False, q=None):
        """
        Return the number of similarity classes of matrices of type ``self``.

        INPUT:

        - ``invertible`` -- boolean; return number of invertible classes if set
          to ``True``

        - ``q`` -- integer or an indeterminate

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1]], [1, [1]]])
            sage: tau.number_of_classes()
            1/2*q^2 - 1/2*q
        """
    def is_semisimple(self) -> bool:
        """
        Return ``True`` if every primary similarity class type in ``self`` has
        all parts equal to ``1``.

        EXAMPLES::

            sage: tau = SimilarityClassType([[2, [1, 1]], [1, [1]]])
            sage: tau.is_semisimple()
            True
            sage: tau = SimilarityClassType([[2, [1, 1]], [1, [2]]])
            sage: tau.is_semisimple()
            False
        """
    def is_regular(self) -> bool:
        """
        Return ``True`` if every primary type in ``self`` has partition with one
        part.

        EXAMPLES::

            sage: tau = SimilarityClassType([[2, [1]], [1, [3]]])
            sage: tau.is_regular()
            True
            sage: tau = SimilarityClassType([[2, [1, 1]], [1, [3]]])
            sage: tau.is_regular()
            False
        """
    def rcf(self):
        """
        Return the partition corresponding to the rational canonical form of a
        matrix of type ``self``.

        EXAMPLES::

            sage: tau = SimilarityClassType([[2, [1, 1, 1]], [1, [3, 2]]])
            sage: tau.rcf()
            [5, 4, 2]
        """
    def class_card(self, q=None):
        """
        Return the number of matrices in each similarity class of type ``self``.

        INPUT:

        - ``q`` -- integer or an indeterminate

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1, 1, 1, 1]]])
            sage: tau.class_card()
            1
            sage: tau = SimilarityClassType([[1, [1]], [1, [1]]])
            sage: tau.class_card()
            q^2 + q
        """
    def number_of_matrices(self, invertible: bool = False, q=None):
        """
        Return the number of matrices of type ``self``.

        INPUT:

        - ``invertible`` -- a boolean; return the number of invertible
          matrices if set

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1]]])
            sage: tau.number_of_matrices()
            q
            sage: tau.number_of_matrices(invertible = True)
            q - 1
            sage: tau = SimilarityClassType([[1, [1]], [1, [1]]])
            sage: tau.number_of_matrices()
            1/2*q^4 - 1/2*q^2
        """
    def statistic(self, func, q=None):
        """
        Return.

        .. MATH::

            \\prod_{(d, \\lambda)\\in \\tau} n_{\\lambda}(q^d)

        where `n_{\\lambda}(q)` is the value returned by ``func`` on the input
        `\\lambda`.

        INPUT:

        - ``func`` -- a function that takes a partition to a polynomial in ``q``

        - ``q`` -- integer or an indeterminate

        EXAMPLES::

            sage: tau = SimilarityClassType([[1, [1]], [1, [2, 1]], [2, [1, 1]]])
            sage: from sage.combinat.similarity_class_type import fq
            sage: tau.statistic(lambda la: prod([fq(m) for m in la.to_exp()]))
            (q^9 - 3*q^8 + 2*q^7 + 2*q^6 - 4*q^5 + 4*q^4 - 2*q^3 - 2*q^2 + 3*q - 1)/q^9
            sage: q = ZZ['q'].gen()
            sage: tau.statistic(lambda la: q**la.size(), q = q)
            q^8
        """
    def invariant_subspace_generating_function(self, q=None, t=None):
        """
        Return the invariant subspace generating function of ``self``.

        The invariant subspace generating function is the function is the
        polynomial

        .. MATH::

            \\sum_{j\\geq 0} a_j(q) t^j,

        where `a_j(q)` denotes the number of `j`-dimensional invariant subspaces
        of dimensiona `j` for any matrix with the similarity class type ``self``
        with entries in a field of order `q`.

        EXAMPLES::

            sage: SimilarityClassType([[1, [2, 2]]]).invariant_subspace_generating_function()
            t^4 + (q + 1)*t^3 + (q^2 + q + 1)*t^2 + (q + 1)*t + 1
            sage: A = Matrix(GF(2),[(0, 1, 0, 0), (0, 1, 1, 1), (1, 0, 1, 0), (1, 1, 0, 0)])
            sage: SimilarityClassType(A).invariant_subspace_generating_function()
            t^4 + 1
        """

class SimilarityClassTypes(UniqueRepresentation, Parent):
    """
    Class of all similarity class types of size ``n`` with all primary matrix
    types greater than or equal to the primary matrix type ``min``.

    A similarity class type is a multiset of primary matrix types.

    INPUT:

    - ``n`` -- nonnegative integer
    - ``min`` -- a primary similarity class type

    EXAMPLES:

    If ``min`` is not specified, then the class of all matrix types of size
    ``n`` is constructed::

        sage: M = SimilarityClassTypes(2)
        sage: for tau in M:
        ....:     print(tau)
        [[1, [1]], [1, [1]]]
        [[1, [2]]]
        [[1, [1, 1]]]
        [[2, [1]]]

    If ``min`` is specified, then the class consists of only those similarity
    class types which are multisets of primary matrix types which either have
    size greater than that of ``min``, or if they have size equal to that of
    ``min``, then they occur after ``min`` in the iterator for
    ``PrimarySimilarityClassTypes(n)``, where ``n`` is the size of ``min``::

        sage: M = SimilarityClassTypes(2, min = [1, [1, 1]])
        sage: for tau in M:
        ....:     print(tau)
        [[1, [1, 1]]]
        [[2, [1]]]
    """
    @staticmethod
    def __classcall_private__(cls, n, min=None):
        """
        Create the class of similarity class types of size ``n`` consisting of
        primary similarity class types greater than or equal to ``min``.

        EXAMPLES::

            sage: M1 = SimilarityClassTypes(2, min = [1, [1]])
            sage: M2 = SimilarityClassTypes(2)
            sage: M1 is M2
            True
        """
    def __init__(self, n, min) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: M = SimilarityClassTypes(2)
            sage: TestSuite(M).run()
        """
    Element = SimilarityClassType
    def __iter__(self):
        """
        Iterator for vector partitions.

        EXAMPLES::

            sage: SimilarityClassTypes(3).cardinality()
            8

        A good test of the iterator is to see that all elements of
        `M_n(\\GF{q})` or `GL_n(\\GF{q})` are enumerated through
        types::

            sage: from sage.combinat.similarity_class_type import order_of_general_linear_group
            sage: q = QQ['q'].gen()
            sage: def test(n):
            ....:     M = SimilarityClassTypes(n)
            ....:     return M.sum(lambda la:1) == q**(n**2) and M.sum(lambda la:1, invertible = True)== order_of_general_linear_group(n)
            sage: all(test(n) for n in range(5))
            True
            sage: all(test(n) for n in range(5, 10)) # long time
            True
        """
    def size(self):
        """
        Return size of ``self``.

        EXAMPLES::

            sage: tau = SimilarityClassType([[3, [3, 2, 1]], [2, [2, 1]]])
            sage: tau.parent().size()
            24
        """
    def sum(self, stat, sumover: str = 'matrices', invertible: bool = False, q=None):
        '''
        Return the sum of a local statistic over all types.

        Given a set of functions `n_{\\lambda}(q)` (these could be polynomials or
        rational functions in `q`, for each similarity class type `\\tau` define

        .. MATH::

            n_\\tau(q) = \\prod_{(d,\\lambda)\\in \\tau} n_{\\lambda}(q^d).

        This function returns

        .. MATH::

            \\sum n_{\\tau(g)}(q)

        where `\\tau(g)` denotes the type of a matrix `g`, and the sum is over
        all `n \\times n` matrices if ``sumover`` is set to ``\'matrices\'``, is
        over all `n \\times n` similarity classes if ``sumover`` is set to
        ``\'classes\'``, and over all `n \\times n` types if ``sumover`` is set
        to ``\'types\'``. If ``invertible`` is set to ``True``, then the sum is
        only over invertible matrices or classes.

        INPUT:

        - ``stat`` -- a function which takes partitions and returns a function
          of ``q``
        - ``sumover`` -- can be one of the following:

          * ``\'matrices\'``
          * ``\'classes\'``
          * ``\'types\'``

        - ``q`` -- integer or an indeterminate

        OUTPUT: a function of ``q``

        EXAMPLES::

            sage: M = SimilarityClassTypes(2)
            sage: M.sum(lambda la:1)
            q^4
            sage: M.sum(lambda la:1, invertible = True)
            q^4 - q^3 - q^2 + q
            sage: M.sum(lambda la:1, sumover = "classes")
            q^2 + q
            sage: M.sum(lambda la:1, sumover = "classes", invertible = True)
            q^2 - 1

        Burside\'s lemma can be used to calculate the number of similarity
        classes of matrices::

            sage: from sage.combinat.similarity_class_type import centralizer_algebra_dim, order_of_general_linear_group
            sage: q = ZZ[\'q\'].gen()
            sage: M.sum(lambda la:q**centralizer_algebra_dim(la), invertible = True)/order_of_general_linear_group(2)
            q^2 + q
        '''

def dictionary_from_generator(gen):
    """
    Given a generator for a list of pairs `(c,f)`, construct a dictionary whose
    keys are the distinct values for `c` and whose value at `c` is the sum of
    `f` over all pairs of the form `(c',f)` such that `c=c'`.

    EXAMPLES::

        sage: from sage.combinat.similarity_class_type import dictionary_from_generator
        sage: dictionary_from_generator(((x // 2, x) for x in range(10)))
        {0: 1, 1: 5, 2: 9, 3: 13, 4: 17}

    It also works with lists::

        sage: dictionary_from_generator([(x // 2, x) for x in range(10)])
        {0: 1, 1: 5, 2: 9, 3: 13, 4: 17}

    .. NOTE::

        Since the generator is first converted to a list, memory usage could be
        high.
    """
def matrix_similarity_classes(n, q=None, invertible: bool = False):
    """
    Return the number of matrix similarity classes over a finite field of order
    ``q``.

    TESTS::

        sage: from sage.combinat.similarity_class_type import matrix_similarity_classes
        sage: matrix_similarity_classes(2)
        q^2 + q
        sage: matrix_similarity_classes(2, invertible = True)
        q^2 - 1
        sage: matrix_similarity_classes(2, invertible = True, q = 4)
        15
    """
def matrix_centralizer_cardinalities(n, q=None, invertible: bool = False) -> Generator[Incomplete]:
    """
    Generate pairs consisting of centralizer cardinalities of matrices over a
    finite field and their frequencies.

    TESTS::

        sage: from sage.combinat.similarity_class_type import matrix_centralizer_cardinalities
        sage: list(matrix_centralizer_cardinalities(1))
        [(q - 1, q)]
        sage: list(matrix_centralizer_cardinalities(2))
        [(q^2 - 2*q + 1, 1/2*q^2 - 1/2*q),
        (q^2 - q, q),
        (q^4 - q^3 - q^2 + q, q),
        (q^2 - 1, 1/2*q^2 - 1/2*q)]
        sage: list(matrix_centralizer_cardinalities(2, invertible = True))
        [(q^2 - 2*q + 1, 1/2*q^2 - 3/2*q + 1),
        (q^2 - q, q - 1),
        (q^4 - q^3 - q^2 + q, q - 1),
        (q^2 - 1, 1/2*q^2 - 1/2*q)]
    """
def input_parsing(data):
    """
    Recognize and return the intended type of ``input``.

    TESTS::

        sage: from sage.combinat.similarity_class_type import input_parsing
        sage: input_parsing(Partition([2, 1]))
        ('par', [2, 1])
        sage: input_parsing(PrimarySimilarityClassType(2, [2, 1]))
        ('pri', [2, [2, 1]])
        sage: input_parsing(SimilarityClassType([[2, [2, 1]]]))
        ('sim', [[2, [2, 1]]])
        sage: input_parsing([2, 1])
        ('par', [2, 1])
        sage: input_parsing([2, [2, 1]])
        ('pri', [2, [2, 1]])
        sage: input_parsing([[2, [2, 1]]])
        ('sim', [[2, [2, 1]]])
    """
def ext_orbits(input_data, q=None, selftranspose: bool = False):
    """
    Return the number of orbits in `\\mathrm{Ext}^1(M, M)` for the action of
    `\\mathrm{Aut}(M, M)`, where `M` is the `\\GF{q[t]}`-module constructed
    from ``input_data``.

    INPUT:

    - ``input_data`` -- input for :func:`input_parsing()`
    - ``q`` -- (default: `q`) an integer or an indeterminate
    - ``selftranspose`` -- boolean (default: ``False``); stating if we only
      want selftranspose type

    TESTS::

        sage: from sage.combinat.similarity_class_type import ext_orbits
        sage: ext_orbits([6, 1])
        q^7 + q^6 + q^5
        sage: ext_orbits([6, 1], selftranspose = True)
        q^7 + q^6 - q^5
        sage: ext_orbits([6, 1, 1])
        q^8 + 2*q^7 + 2*q^6 + 2*q^5
        sage: ext_orbits ([6, 1, 1], selftranspose = True)
        q^8 + 2*q^7
        sage: ext_orbits([2, 2])
        q^4 + q^3 + q^2
        sage: ext_orbits([2, 2], selftranspose = True)
        q^4 + q^3 + q^2
        sage: ext_orbits([2, 2, 2])
        q^6 + q^5 + 2*q^4 + q^3 + 2*q^2
        sage: ext_orbits([2, 2, 2], selftranspose = True)
        q^6 + q^5 + 2*q^4 + q^3
        sage: ext_orbits([2, 2, 2, 2])
        q^8 + q^7 + 3*q^6 + 3*q^5 + 5*q^4 + 3*q^3 + 3*q^2
        sage: ext_orbits([2, 2, 2, 2], selftranspose = True)
        q^8 + q^7 + 3*q^6 + 3*q^5 + 3*q^4 + q^3 + q^2
        sage: ext_orbits([2, [6, 1]])
        q^14 + q^12 + q^10
        sage: ext_orbits([[2, [6, 1]]])
        q^14 + q^12 + q^10
    """
def matrix_similarity_classes_length_two(n, q=None, selftranspose: bool = False, invertible: bool = False):
    """
    Return the number of similarity classes of matrices of order ``n`` with
    entries in a principal ideal local ring of length two.

    INPUT:

    - ``n`` -- the order
    - ``q`` -- (default: `q`) an integer or an indeterminate
    - ``selftranspose`` -- boolean (default: ``False``); stating if we only want
      selftranspose type
    - ``invertible`` -- boolean (default: ``False``); stating if we only want
      invertible type

    EXAMPLES:

    We can generate Table 6 of [PSS13]_::

        sage: from sage.combinat.similarity_class_type import matrix_similarity_classes_length_two
        sage: matrix_similarity_classes_length_two(2)
        q^4 + q^3 + q^2
        sage: matrix_similarity_classes_length_two(2, invertible = True)
        q^4 - q
        sage: matrix_similarity_classes_length_two(3)
        q^6 + q^5 + 2*q^4 + q^3 + 2*q^2
        sage: matrix_similarity_classes_length_two(3, invertible = true)
        q^6 - q^3 + 2*q^2 - 2*q
        sage: matrix_similarity_classes_length_two(4)
        q^8 + q^7 + 3*q^6 + 3*q^5 + 5*q^4 + 3*q^3 + 3*q^2
        sage: matrix_similarity_classes_length_two(4, invertible = True)
        q^8 + q^6 - q^5 + 2*q^4 - 2*q^3 + 2*q^2 - 3*q

    And also Table 7::

        sage: matrix_similarity_classes_length_two(2, selftranspose = True)
        q^4 + q^3 + q^2
        sage: matrix_similarity_classes_length_two(2, selftranspose = True, invertible = True)
        q^4 - q
        sage: matrix_similarity_classes_length_two(3, selftranspose = True)
        q^6 + q^5 + 2*q^4 + q^3
        sage: matrix_similarity_classes_length_two(3, selftranspose = True, invertible = True)
        q^6 - q^3
        sage: matrix_similarity_classes_length_two(4, selftranspose = True)
        q^8 + q^7 + 3*q^6 + 3*q^5 + 3*q^4 + q^3 + q^2
        sage: matrix_similarity_classes_length_two(4, selftranspose = True, invertible = True)
        q^8 + q^6 - q^5 - q
    """
def ext_orbit_centralizers(input_data, q=None, selftranspose: bool = False) -> Generator[Incomplete, None, Incomplete]:
    """
    Generate pairs consisting of centralizer cardinalities of orbits in
    `\\mathrm{Ext}^1(M, M)` for the action of `\\mathrm{Aut}(M, M)`, where `M` is
    the `\\GF{q[t]}`-module constructed from ``input`` and their frequencies.

    INPUT:

    - ``input_data`` -- input for :func:`input_parsing()`
    - ``q`` -- (default: `q`) an integer or an indeterminate
    - ``selftranspose`` -- boolean (default: ``False``); stating if we only want
      selftranspose type

    TESTS::

        sage: from sage.combinat.similarity_class_type import ext_orbit_centralizers
        sage: list(ext_orbit_centralizers([6, 1]))
        [(q^9 - 2*q^8 + q^7, q^6),
         (q^7 - 2*q^6 + q^5, q^7 - q^6),
         (q^7 - q^6, q^6 + q^5)]
        sage: list(ext_orbit_centralizers([6, 1], selftranspose = True))
        [(q^9 - 2*q^8 + q^7, q^6),
         (q^7 - 2*q^6 + q^5, q^7 - q^6),
         (q^7 - q^6, q^6 - q^5)]
        sage: list(ext_orbit_centralizers([6, 1, 1]))
        [(q^12 - 3*q^11 + 3*q^10 - q^9, 1/2*q^7 - 1/2*q^6),
         (q^8 - 3*q^7 + 3*q^6 - q^5, 1/2*q^8 - q^7 + 1/2*q^6),
         (q^12 - 2*q^11 + q^10, q^6),
         (q^8 - 2*q^7 + q^6, q^7 - q^6),
         (q^14 - 2*q^13 + 2*q^11 - q^10, q^6),
         (q^10 - 2*q^9 + 2*q^7 - q^6, q^7 - q^6),
         (q^12 - q^11 - q^10 + q^9, 1/2*q^7 - 1/2*q^6),
         (q^8 - q^7 - q^6 + q^5, 1/2*q^8 - q^7 + 1/2*q^6),
         (q^8 - 2*q^7 + q^6, q^7 - q^6),
         (q^8 - q^7, q^6 + 2*q^5),
         (q^10 - 2*q^9 + q^8, 2*q^6)]
        sage: list(ext_orbit_centralizers([6, 1, 1], selftranspose = True))
        [(q^12 - 3*q^11 + 3*q^10 - q^9, 1/2*q^7 - 1/2*q^6),
         (q^8 - 3*q^7 + 3*q^6 - q^5, 1/2*q^8 - q^7 + 1/2*q^6),
         (q^12 - 2*q^11 + q^10, q^6),
         (q^8 - 2*q^7 + q^6, q^7 - q^6),
         (q^14 - 2*q^13 + 2*q^11 - q^10, q^6),
         (q^10 - 2*q^9 + 2*q^7 - q^6, q^7 - q^6),
         (q^12 - q^11 - q^10 + q^9, 1/2*q^7 - 1/2*q^6),
         (q^8 - q^7 - q^6 + q^5, 1/2*q^8 - q^7 + 1/2*q^6),
         (q^8 - 2*q^7 + q^6, q^7 - q^6),
         (q^8 - q^7, q^6)]
        sage: list(ext_orbit_centralizers([2, [6, 1, 1]], selftranspose = True))
        [(q^24 - 3*q^22 + 3*q^20 - q^18, 1/2*q^14 - 1/2*q^12),
         (q^16 - 3*q^14 + 3*q^12 - q^10, 1/2*q^16 - q^14 + 1/2*q^12),
         (q^24 - 2*q^22 + q^20, q^12),
         (q^16 - 2*q^14 + q^12, q^14 - q^12),
         (q^28 - 2*q^26 + 2*q^22 - q^20, q^12),
         (q^20 - 2*q^18 + 2*q^14 - q^12, q^14 - q^12),
         (q^24 - q^22 - q^20 + q^18, 1/2*q^14 - 1/2*q^12),
         (q^16 - q^14 - q^12 + q^10, 1/2*q^16 - q^14 + 1/2*q^12),
         (q^16 - 2*q^14 + q^12, q^14 - q^12),
         (q^16 - q^14, q^12)]
        sage: list(ext_orbit_centralizers([[2, [6, 1, 1]]], selftranspose = True))
        [(q^24 - 3*q^22 + 3*q^20 - q^18, 1/2*q^14 - 1/2*q^12),
         (q^16 - 3*q^14 + 3*q^12 - q^10, 1/2*q^16 - q^14 + 1/2*q^12),
         (q^24 - 2*q^22 + q^20, q^12),
         (q^16 - 2*q^14 + q^12, q^14 - q^12),
         (q^28 - 2*q^26 + 2*q^22 - q^20, q^12),
         (q^20 - 2*q^18 + 2*q^14 - q^12, q^14 - q^12),
         (q^24 - q^22 - q^20 + q^18, 1/2*q^14 - 1/2*q^12),
         (q^16 - q^14 - q^12 + q^10, 1/2*q^16 - q^14 + 1/2*q^12),
         (q^16 - 2*q^14 + q^12, q^14 - q^12),
         (q^16 - q^14, q^12)]
    """
def matrix_centralizer_cardinalities_length_two(n, q=None, selftranspose: bool = False, invertible: bool = False) -> Generator[Incomplete]:
    """
    Generate pairs consisting of centralizer cardinalities of matrices over a
    principal ideal local ring of length two with residue field of order ``q``
    and their frequencies.

    INPUT:

    - ``n`` -- the order
    - ``q`` -- (default: `q`) an integer or an indeterminate
    - ``selftranspose`` -- boolean (default: ``False``); stating if we only want
      selftranspose type
    - ``invertible`` -- boolean (default: ``False``); stating if we only want
      invertible type

    TESTS::

        sage: from sage.combinat.similarity_class_type import matrix_centralizer_cardinalities_length_two
        sage: list(matrix_centralizer_cardinalities_length_two(1))
        [(q^2 - q, q^2)]
        sage: list(matrix_centralizer_cardinalities_length_two(2))
        [(q^4 - 2*q^3 + q^2, 1/2*q^4 - 1/2*q^3),
        (q^4 - q^3, q^3),
        (q^6 - 2*q^5 + q^4, 1/2*q^3 - 1/2*q^2),
        (q^6 - q^5, q^2),
        (q^8 - q^7 - q^6 + q^5, q^2),
        (q^6 - q^4, 1/2*q^3 - 1/2*q^2),
        (q^4 - q^2, 1/2*q^4 - 1/2*q^3)]
        sage: from sage.combinat.similarity_class_type import dictionary_from_generator
        sage: dictionary_from_generator(matrix_centralizer_cardinalities_length_two(2, q = 2))
        {4: 4, 8: 8, 12: 4, 16: 2, 32: 4, 48: 2, 96: 4}
    """
