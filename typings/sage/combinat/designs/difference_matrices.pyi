from .designs_pyx import is_difference_matrix as is_difference_matrix
from sage.arith.misc import divisors as divisors, is_prime_power as is_prime_power
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.unknown import Unknown as Unknown
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField

@cached_function
def find_product_decomposition(g, k, lmbda: int = 1):
    """
    Try to find a product decomposition construction for difference matrices.

    INPUT:

    - ``g``, ``k``, ``lmbda`` -- integers, parameters of the difference matrix

    OUTPUT:

    A pair of pairs ``(g1,lmbda),(g2,lmbda2)`` if Sage knows how to build
    `(g1,k,lmbda1)` and `(g2,k,lmbda2)` difference matrices and ``False``
    otherwise.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_matrices import find_product_decomposition
        sage: find_product_decomposition(77,6)
        ((7, 1), (11, 1))
        sage: find_product_decomposition(616,7)
        ((7, 1), (88, 1))
        sage: find_product_decomposition(24,10)
        False
    """
def difference_matrix_product(k, M1, G1, lmbda1, M2, G2, lmbda2, check: bool = True):
    """
    Return the product of the ``(G1, k, lmbda1)`` and ``(G2, k, lmbda2)``
    difference matrices ``M1`` and ``M2``.

    The result is a `(G1 \\times G2, k, \\lambda_1 \\lambda_2)`-difference matrix.

    INPUT:

    - ``k``, ``lmbda1``, ``lmbda2`` -- positive integers

    - ``G1``, ``G2`` -- groups

    - ``M1``, ``M2`` -- ``(G1, k, lmbda1)`` and ``(G, k, lmbda2)`` difference
      matrices

    - ``check`` -- boolean (default: ``True``); whether to check the output
      before it is returned

    EXAMPLES::

        sage: from sage.combinat.designs.difference_matrices import (
        ....:     difference_matrix_product,
        ....:     is_difference_matrix)
        sage: G1,M1 = designs.difference_matrix(11,6)
        sage: G2,M2 = designs.difference_matrix(7,6)
        sage: G,M = difference_matrix_product(6,M1,G1,1,M2,G2,1)
        sage: G1
        Finite Field of size 11
        sage: G2
        Finite Field of size 7
        sage: G
        The Cartesian product of (Finite Field of size 11, Finite Field of size 7)
        sage: is_difference_matrix(M,G,6,1)
        True
    """
def difference_matrix(g, k, lmbda: int = 1, existence: bool = False, check: bool = True):
    '''
    Return a `(g,k,\\lambda)`-difference matrix.

    A matrix `M` is a `(g,k,\\lambda)`-difference matrix if it has size `\\lambda
    g\\times k`, its entries belong to the group `G` of cardinality `g`, and
    for any two rows `R,R\'` of `M` and `x\\in G` there are exactly `\\lambda`
    values `i` such that `R_i-R\'_i=x`.

    INPUT:

    - ``k`` -- integer; number of columns. If ``k`` is ``None`` it is set to the
      largest value available

    - ``g`` -- integer; cardinality of the group `G`

    - ``lmbda`` -- integer (default: 1); number of times each element of `G`
      appears as a difference

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    - ``existence`` -- boolean; instead of building the design, return:

      - ``True`` -- meaning that Sage knows how to build the design

      - ``Unknown`` -- meaning that Sage does not know how to build the
        design, but that the design may exist (see :mod:`sage.misc.unknown`)

      - ``False`` -- meaning that the design does not exist

      .. NOTE::

          When ``k=None`` and ``existence=True`` the function returns an
          integer, i.e. the largest `k` such that we can build a
          `(g,k,\\lambda)`-DM.

    EXAMPLES::

        sage: G,M = designs.difference_matrix(25,10); G
        Finite Field in x of size 5^2
        sage: designs.difference_matrix(993,None,existence=1)
        32

    Here we print for each `g` the maximum possible `k` for which Sage knows
    how to build a `(g,k,1)`-difference matrix::

        sage: for g in range(2,30):
        ....:     k_max = designs.difference_matrix(g=g,k=None,existence=True)
        ....:     print("{:2} {}".format(g, k_max))
        ....:     _ = designs.difference_matrix(g,k_max)
         2 2
         3 3
         4 4
         5 5
         6 2
         7 7
         8 8
         9 9
        10 2
        11 11
        12 6
        13 13
        14 2
        15 3
        16 16
        17 17
        18 2
        19 19
        20 4
        21 6
        22 2
        23 23
        24 8
        25 25
        26 2
        27 27
        28 6
        29 29

    TESTS::

        sage: designs.difference_matrix(10,12,1,existence=True)
        False
        sage: designs.difference_matrix(10,12,1)
        Traceback (most recent call last):
        ...
        EmptySetError: No (10,12,1)-Difference Matrix exists as k(=12)>g(=10)
        sage: designs.difference_matrix(10,9,1,existence=True)
        Unknown
        sage: designs.difference_matrix(10,9,1)
        Traceback (most recent call last):
        ...
        NotImplementedError: I don\'t know how to build a (10,9,1)-Difference Matrix!
    '''
