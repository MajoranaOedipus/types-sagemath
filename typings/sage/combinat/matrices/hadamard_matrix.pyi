from sage.arith.misc import divisors as divisors, is_prime as is_prime, is_prime_power as is_prime_power, is_square as is_square
from sage.combinat.designs.difference_family import complementary_difference_sets as complementary_difference_sets, get_fixed_relative_difference_set as get_fixed_relative_difference_set, relative_difference_set_from_homomorphism as relative_difference_set_from_homomorphism, skew_supplementary_difference_set as skew_supplementary_difference_set
from sage.combinat.t_sequences import T_sequences_smallcases as T_sequences_smallcases
from sage.matrix.constructor import block_diagonal_matrix as block_diagonal_matrix, block_matrix as block_matrix, diagonal_matrix as diagonal_matrix, matrix as matrix, matrix_method as matrix_method, zero_matrix as zero_matrix
from sage.misc.unknown import Unknown as Unknown
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def normalise_hadamard(H, skew: bool = False):
    """
    Return the normalised Hadamard matrix corresponding to ``H``.

    The normalised Hadamard matrix corresponding to a Hadamard matrix `H` is a
    matrix whose every entry in the first row and column is +1.

    If ``skew`` is True, the matrix returned will be skew-normal: a skew Hadamard
    matrix with first row of all `+1`.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import normalise_hadamard, is_hadamard_matrix, skew_hadamard_matrix
        sage: H = normalise_hadamard(hadamard_matrix(4))
        sage: H == hadamard_matrix(4)
        True
        sage: H = normalise_hadamard(skew_hadamard_matrix(20, skew_normalize=False), skew=True)
        sage: is_hadamard_matrix(H, skew=True, normalized=True)
        True

    If ``skew`` is ``True`` but the Hadamard matrix is not skew, the matrix returned
    will not be normalized::

        sage: H = normalise_hadamard(hadamard_matrix(92), skew=True)
        sage: is_hadamard_matrix(H, normalized=True)
        False
    """
def hadamard_matrix_paleyI(n, normalize: bool = True):
    """
    Implement the Paley type I construction.

    The Paley type I case corresponds to the case `p=n-1 \\cong 3 \\mod{4}` for a
    prime power `p` (see [Hora]_).

    INPUT:

    - ``n`` -- the matrix size
    - ``normalize`` -- boolean (default: ``True``); whether to normalize the result

    EXAMPLES:

    We note that this method by default returns a normalised Hadamard matrix ::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_paleyI
        sage: hadamard_matrix_paleyI(4)
        [ 1  1  1  1]
        [ 1 -1  1 -1]
        [ 1 -1 -1  1]
        [ 1  1 -1 -1]

    Otherwise, it returns a skew Hadamard matrix `H`, i.e. `H=S+I`, with
    `S=-S^\\top`  ::

        sage: M = hadamard_matrix_paleyI(4, normalize=False); M
        [ 1  1  1  1]
        [-1  1  1 -1]
        [-1 -1  1  1]
        [-1  1 -1  1]
        sage: S = M - identity_matrix(4); -S == S.T
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: test_cases = [x+1 for x in range(100) if is_prime_power(x) and x%4==3]
        sage: all(is_hadamard_matrix(hadamard_matrix_paleyI(n),normalized=True,verbose=True)
        ....:     for n in test_cases)
        True
        sage: all(is_hadamard_matrix(hadamard_matrix_paleyI(n,normalize=False),verbose=True)
        ....:     for n in test_cases)
        True
    """
def symmetric_conference_matrix_paley(n):
    """
    Construct a symmetric conference matrix of order n.

    A conference matrix is an `n\\times n` matrix `C` with 0s on the main diagonal
    and 1s and -1s elsewhere, satisfying `CC^\\top=(n-1)I`. This construction assumes
    that `q = n-1` is a prime power, with `q \\cong 1 \\mod 4`. See [Hora]_ or [Lon2013]_.

    These matrices are used in :func:`hadamard_matrix_paleyII`.

    INPUT:

    - ``n`` -- integer; the order of the symmetric conference matrix to construct

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import symmetric_conference_matrix_paley
        sage: symmetric_conference_matrix_paley(6)
        [ 0  1  1  1  1  1]
        [ 1  0  1 -1 -1  1]
        [ 1  1  0  1 -1 -1]
        [ 1 -1  1  0  1 -1]
        [ 1 -1 -1  1  0  1]
        [ 1  1 -1 -1  1  0]

    TESTS::

        sage: symmetric_conference_matrix_paley(5)
        Traceback (most recent call last):
        ...
        ValueError: The order 5 is not covered by Paley construction of symmetric conference matrices.
    """
def hadamard_matrix_paleyII(n):
    """
    Implement the Paley type II construction.

    The Paley type II case corresponds to the case `p=n/2-1 \\cong 1 \\mod{4}` for a
    prime power `p` (see [Hora]_).

    EXAMPLES::

        sage: sage.combinat.matrices.hadamard_matrix.hadamard_matrix_paleyII(12).det()
        2985984
        sage: 12^6
        2985984

    We note that the method returns a normalised Hadamard matrix ::

        sage: sage.combinat.matrices.hadamard_matrix.hadamard_matrix_paleyII(12)
        [ 1  1| 1  1| 1  1| 1  1| 1  1| 1  1]
        [ 1 -1|-1  1|-1  1|-1  1|-1  1|-1  1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1| 1 -1| 1  1|-1 -1|-1 -1| 1  1]
        [ 1  1|-1 -1| 1 -1|-1  1|-1  1| 1 -1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1| 1  1| 1 -1| 1  1|-1 -1|-1 -1]
        [ 1  1| 1 -1|-1 -1| 1 -1|-1  1|-1  1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1|-1 -1| 1  1| 1 -1| 1  1|-1 -1]
        [ 1  1|-1  1| 1 -1|-1 -1| 1 -1|-1  1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1|-1 -1|-1 -1| 1  1| 1 -1| 1  1]
        [ 1  1|-1  1|-1  1| 1 -1|-1 -1| 1 -1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1| 1  1|-1 -1|-1 -1| 1  1| 1 -1]
        [ 1  1| 1 -1|-1  1|-1  1| 1 -1|-1 -1]

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import (hadamard_matrix_paleyII, is_hadamard_matrix)
        sage: test_cases = [2*(x+1) for x in range(50) if is_prime_power(x) and x%4==1]
        sage: all(is_hadamard_matrix(hadamard_matrix_paleyII(n),normalized=True,verbose=True)
        ....:     for n in test_cases)
        True
    """
def hadamard_matrix_from_symmetric_conference_matrix(n, existence: bool = False, check: bool = True):
    """
    Construct a Hadamard matrix of order `n` from a symmetric conference matrix
    of order `n/2`.

    The construction is described in Theorem 4.3.24 of [IS2006]_.
    The symmetric conference matrices are obtained from
    :func:`sage.combinat.matrices.hadamard_matrix.symmetric_conference_matrix`.

    INPUT:

    - ``n`` -- integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if
      the matrix exists
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard before returning

    OUTPUT:

    If ``existence=False``, returns the Hadamard matrix of order `n`. It raises
    an error if no data is available to construct the matrix of the given order,
    or if `n` does not satisfies the constraints.
    If ``existence=True``, returns a boolean representing whether the matrix
    can be constructed or not.

    EXAMPLES:

    By default the function returns the Hadamard matrix ::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_from_symmetric_conference_matrix
        sage: hadamard_matrix_from_symmetric_conference_matrix(20)
        20 x 20 dense matrix over Integer Ring...

    If ``existence`` is set to True, the function returns True if the matrix exists,
    False if the conference matrix does not exist, and Unknown if the conference
    matrix cannot be constructed yet ::

        sage: hadamard_matrix_from_symmetric_conference_matrix(12, existence=True)
        True
        sage: hadamard_matrix_from_symmetric_conference_matrix(4*787, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: is_hadamard_matrix(hadamard_matrix_from_symmetric_conference_matrix(60, check=False))
        True
        sage: hadamard_matrix_from_symmetric_conference_matrix(64, existence=True)
        False
        sage: hadamard_matrix_from_symmetric_conference_matrix(4*787, existence=True)
        True
        sage: hadamard_matrix_from_symmetric_conference_matrix(64)
        Traceback (most recent call last):
        ...
        ValueError: Cannot construct Hadamard matrix of order 64, a symmetric conference matrix of order 32 is not available in sage.
        sage: hadamard_matrix_from_symmetric_conference_matrix(14)
        Traceback (most recent call last):
        ...
        ValueError: No Hadamard matrix of order 14 exists.
    """
def hadamard_matrix_miyamoto_construction(n, existence: bool = False, check: bool = True):
    """
    Construct Hadamard matrix using the Miyamoto construction.

    If `q = n/4` is a prime power, and there exists a Hadamard matrix of order
    `q-1`, then a Hadamard matrix of order `n` can be constructed (see [Miy1991]_).

    INPUT:

    - ``n`` -- integer; the order of the matrix to be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard before returning
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if
      the matrix exists

    OUTPUT:

    If ``existence=False``, returns the Hadamard matrix of order `n`. It raises
    an error if no data is available to construct the matrix of the given order,
    or if `n` does not satisfies the constraints.
    If ``existence=True``, returns a boolean representing whether the matrix
    can be constructed or not.

    EXAMPLES:

    By default the function returns the Hadamard matrix ::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_miyamoto_construction
        sage: hadamard_matrix_miyamoto_construction(20)
        20 x 20 dense matrix over Integer Ring...

    If ``existence`` is set to True, the function returns a boolean ::

        sage: hadamard_matrix_miyamoto_construction(36, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: is_hadamard_matrix(hadamard_matrix_miyamoto_construction(68, check=False))
        True
        sage: hadamard_matrix_miyamoto_construction(64, existence=True)
        False
        sage: hadamard_matrix_miyamoto_construction(4*65, existence=True)
        True
        sage: is_hadamard_matrix(hadamard_matrix_miyamoto_construction(4*65, check=False))
        True
        sage: hadamard_matrix_miyamoto_construction(64)
        Traceback (most recent call last):
        ...
        ValueError: The order 64 is not covered by Miyamoto construction.
        sage: hadamard_matrix_miyamoto_construction(14)
        Traceback (most recent call last):
        ...
        ValueError: No Hadamard matrix of order 14 exists.
    """
def hadamard_matrix_williamson_type(a, b, c, d, check: bool = True):
    """
    Construction of Williamson type Hadamard matrix.

    Given `n\\times n` circulant matrices `A`, `B`, `C`, `D` with 1,-1 entries,
    and satisfying `AA^\\top + BB^\\top + CC^\\top + DD^\\top = 4nI`,
    one can construct a  Hadamard matrix of order `4n`, cf. [Ha83]_.

    INPUT:

    - ``a`` -- (1,-1) list; the 1st row of `A`
    - ``b`` -- (1,-1) list; the 1st row of `B`
    - ``d`` -- (1,-1) list; the 1st row of `C`
    - ``c`` -- (1,-1) list; the 1st row of `D`
    - ``check`` -- boolean (default: ``True``); whether to check that the output
      is a Hadamard matrix before returning it

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_williamson_type
        sage: a = [ 1,  1, 1]
        sage: b = [ 1, -1, -1]
        sage: c = [ 1, -1, -1]
        sage: d = [ 1, -1, -1]
        sage: M = hadamard_matrix_williamson_type(a,b,c,d,check=True)

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_williamson_type, is_hadamard_matrix
        sage: a = [ 1,  1, 1]
        sage: b = [ 1, -1, -1]
        sage: c = [ 1, -1, -1]
        sage: d = [ 1, -1, -1]
        sage: is_hadamard_matrix(hadamard_matrix_williamson_type(a,b,c,d))
        True
        sage: e = [1, 1, 1]
        sage: hadamard_matrix_williamson_type(a,b,c,e, check=True)
        Traceback (most recent call last):
        ...
        AssertionError
        sage: f = [1, -1, 1, -1]
        sage: hadamard_matrix_williamson_type(a,b,c,f, check=True)
        Traceback (most recent call last):
        ...
        AssertionError
    """
def williamson_type_quadruples_smallcases(n, existence: bool = False):
    """
    Quadruples of matrices that can be used to construct Williamson type Hadamard matrices.

    This function contains for some values of n, four `n\\times n` matrices used in the
    Williamson construction of Hadamard matrices. Namely, the function returns the first row of
    4 `n\\times n` circulant matrices with the properties described in
    :func:`sage.combinat.matrices.hadamard_matrix.hadamard_matrix_williamson_type`.
    The matrices for `n = 3, 5, ..., 29, 37, 43` are given in [Ha83]_. The matrices
    for `n = 31, 33, 39, 41, 45, 49, 51, 55, 57, 61, 63` are given in [Lon2013]_.

    INPUT:

    - ``n`` -- integer; the order of the matrices to be returned
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check that
      we have the quadruple

    OUTPUT:

    If ``existence`` is false, returns a tuple containing four vectors, each being the first line
    of one of the four matrices. It raises an error if no such matrices are available.
    If ``existence`` is true, returns a boolean representing whether the matrices are available or not.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import williamson_type_quadruples_smallcases
        sage: williamson_type_quadruples_smallcases(29)
        ((1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1),
         (1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1),
         (1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1),
         (1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1))
        sage: williamson_type_quadruples_smallcases(43, existence=True)
        True

    TESTS::

        sage: williamson_type_quadruples_smallcases(123, existence=True)
        False
        sage: williamson_type_quadruples_smallcases(123)
        Traceback (most recent call last):
        ...
        ValueError: The Williamson type quadruple of order 123 is not yet implemented.
    """
def williamson_hadamard_matrix_smallcases(n, existence: bool = False, check: bool = True):
    """
    Construct Williamson type Hadamard matrices for some small values of n.

    This function uses the data contained in
    :func:`sage.combinat.matrices.hadamard_matrix.williamson_type_quadruples_smallcases`
    to create Hadamard matrices of the Williamson type, using the construction from
    :func:`sage.combinat.matrices.hadamard_matrix.hadamard_matrix_williamson_type`.

    INPUT:

    - ``n`` -- integer; the order of the matrix
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check that
      we can do the construction
    - ``check`` -- boolean (default: ``True``); if ``True`` check the result

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import williamson_hadamard_matrix_smallcases
        sage: williamson_hadamard_matrix_smallcases(116)
        116 x 116 dense matrix over Integer Ring...
        sage: williamson_hadamard_matrix_smallcases(172)
        172 x 172 dense matrix over Integer Ring...
        sage: williamson_hadamard_matrix_smallcases(1000)
        Traceback (most recent call last):
        ...
        ValueError: The Williamson type Hadamard matrix of order 1000 is not yet implemented.
    """
def hadamard_matrix_156():
    """
    Construct a Hadamard matrix of order 156.

    The matrix is created using the construction detailed in [BH1965]_.
    This uses four circulant matrices of size `13\\times 13`,
    which are composed into a `156\\times 156` block matrix.

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix, hadamard_matrix_156
        sage: is_hadamard_matrix(hadamard_matrix_156())
        True
        sage: hadamard_matrix_156()
        156 x 156 dense matrix over Integer Ring...
    """
def construction_four_symbol_delta_code_I(X, Y, Z, W):
    """
    Construct 4-symbol `\\delta` code of length `2n+1`.

    The 4-symbol `\\delta` code is constructed from sequences `X, Y, Z, W` of
    length `n+1`, `n+1`, `n`, `n` satisfying for all `s > 0`:

    .. MATH::

        N_X(s) + N_Y(s) + N_Z(s) + N_W(s) = 0

    where `N_A(s)` is the nonperiodic correlation function:

    .. MATH::

        N_A(s) = \\sum_{i=1}^{n-s}a_ia_{i+s}

    The construction (detailed in [Tur1974]_) is as follows:

    .. MATH::

        \\begin{aligned}
        T_1 &= X;Z \\\\\n        T_2 &= X;-Z \\\\\n        T_3 &= Y;W \\\\\n        T_4 &= Y;-W
        \\end{aligned}

    INPUT:

    - ``X`` -- list; the first sequence (length `n+1`)
    - ``Y`` -- list; the second sequence (length `n+1`)
    - ``Z`` -- list; the third sequence (length `n`)
    - ``W`` -- list; the fourth sequence (length `n`)

    OUTPUT: tuple containing the 4-symbol `\\delta` code of length `2n+1`

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import construction_four_symbol_delta_code_I
        sage: construction_four_symbol_delta_code_I([1, 1], [1, -1], [1], [1])
        ([1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1])

    TESTS::

        sage: construction_four_symbol_delta_code_I([1, 1], [1, -1], [1, 1], [1])
        Traceback (most recent call last):
        ...
        AssertionError
        sage: construction_four_symbol_delta_code_I([1, 1], [1, 1], [-1], [1])
        Traceback (most recent call last):
        ...
        AssertionError
    """
def construction_four_symbol_delta_code_II(X, Y, Z, W):
    """
    Construct 4-symbol `\\delta` code of length `4n+3`.

    The 4-symbol `\\delta` code is constructed from sequences  `X, Y, Z, W` of
    length `n+1`, `n+1`, `n`, `n` satisfying for all `s > 0`:

    .. MATH::
        N_X(s) + N_Y(s) + N_Z(s) + N_W(s) = 0

    where `N_A(s)` is the nonperiodic correlation function:

    .. MATH::

        N_A(s) = \\sum_{i=1}^{n-s}a_ia_{i+s}

    The construction (detailed in [Tur1974]_) is as follows (writing
    `A/B` to mean `A` alternated with `B`):

    .. MATH::

        \\begin{aligned}
        T_1 &= X/Z;Y/W;1 \\\\\n        T_2 &= X/Z;Y/-W;-1 \\\\\n        T_3 &= X/Z;-Y/-W;1 \\\\\n        T_4 &= X/Z;-Y/W;-1
        \\end{aligned}

    INPUT:

    - ``X`` -- list; the first sequence (length `n+1`)
    - ``Y`` -- list; the second sequence (length `n+1`)
    - ``Z`` -- list; the third sequence (length `n`)
    - ``W`` -- list; the fourth sequence (length `n`)

    OUTPUT: tuple containing the four 4-symbol `\\delta` code of length `4n+3`

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import construction_four_symbol_delta_code_II
        sage: construction_four_symbol_delta_code_II([1, 1], [1, -1], [1], [1])
        ([1, 1, 1, 1, 1, -1, 1],
         [1, 1, 1, 1, -1, -1, -1],
         [1, 1, 1, -1, -1, 1, 1],
         [1, 1, 1, -1, 1, 1, -1])

    TESTS::

        sage: construction_four_symbol_delta_code_II([1, 1], [1, -1], [1, 1], [1])
        Traceback (most recent call last):
        ...
        AssertionError
        sage: construction_four_symbol_delta_code_II([1, 1], [1, 1], [-1], [1, 1])
        Traceback (most recent call last):
        ...
        AssertionError
    """
def four_symbol_delta_code_smallcases(n, existence: bool = False):
    """
    Return the 4-symobl `\\delta` code of length ``n`` if available.

    The 4-symbol `\\delta` codes are constructed using :func:`construction_four_symbol_delta_code_I`
    or :func:`construction_four_symbol_delta_code_II`.
    The base sequences used are taken from [Tur1974]_.

    INPUT:

    - ``n`` -- integer; the length of the desired 4-symbol `\\delta` code
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if
      the sequences are available

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import four_symbol_delta_code_smallcases
        sage: four_symbol_delta_code_smallcases(3)
        ([1, -1, 1], [1, -1, -1], [1, 1, 1], [1, 1, -1])
        sage: four_symbol_delta_code_smallcases(3, existence=True)
        True

    TESTS::

        sage: four_symbol_delta_code_smallcases(17)
        Traceback (most recent call last):
        ...
        ValueError: The four-symbol delta code of length 17 have not yet been implemented
        sage: four_symbol_delta_code_smallcases(17, existence=True)
        False
    """
def hadamard_matrix_from_sds(n, existence: bool = False, check: bool = True):
    """
    Construction of Hadamard matrices from supplementary difference sets.

    Given four SDS with parameters `4-\\{n; n_1, n_2, n_3, n_4; \\lambda\\}` with
    `n_1 + n_2 + n_3 + n_4 = n+\\lambda` we can construct four (-1,+1) sequences `a_i = (a_{i,0},...,a_{i,n-1})`
    where `a_{i,j} = -1` iff `j \\in S_i`. These will be the fist rows of four circulant
    matrices `A_1, A_2, A_3, A_4` which, when plugged into the Goethals-Seidel array, create an
    Hadamard matrix of order `4n` (see [Djo1994b]_).

    The supplementary difference sets are taken from
    :func:`sage.combinat.designs.difference_family.supplementary_difference_set`.

    INPUT:

    - ``n`` -- integer; the order of the matrix to be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard before returning
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if the
      matrix exists

    OUTPUT:

    If ``existence=False``, returns the Hadamard matrix of order `n`. It raises
    an error if no data is available to construct the matrix of the given order,
    or if `n` is not a multiple of `4`.
    If ``existence=True``, returns a boolean representing whether the matrix
    can be constructed or not.

    EXAMPLES:

    By default The function returns the Hadamard matrix ::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_from_sds
        sage: hadamard_matrix_from_sds(148)
        148 x 148 dense matrix over Integer Ring...

    If ``existence`` is set to True, the function returns a boolean ::

        sage: hadamard_matrix_from_sds(764, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_from_sds, is_hadamard_matrix
        sage: is_hadamard_matrix(hadamard_matrix_from_sds(172))
        True
        sage: hadamard_matrix_from_sds(64, existence=True)
        False
        sage: hadamard_matrix_from_sds(64)
        Traceback (most recent call last):
        ...
        ValueError: SDS of order 16 not yet implemented.
        sage: hadamard_matrix_from_sds(14)
        Traceback (most recent call last):
        ...
        ValueError: n must be a positive multiple of four
    """
def hadamard_matrix_cooper_wallis_construction(x1, x2, x3, x4, A, B, C, D, check: bool = True):
    """
    Create a Hadamard matrix using the construction detailed in [CW1972]_.

    Given four circulant matrices `X_1`, X_2, X_3, X_4` of order `n` with entries (0, 1, -1)
    such that the entrywise product of two distinct matrices is always equal to `0` and that
    `\\sum_{i=1}^{4}X_iX_i^\\top = nI_n` holds, and four matrices `A, B, C, D` of order `m` with
    elements (1, -1) such that `MN^\\top = NM^\\top` for all distinct `M`, `N` and
    `AA^\\top + BB^\\top + CC^\\top + DD^\\top =  4mI_n` holds, we construct a Hadamard matrix
    of order `4nm`.

    INPUT:

    - ``x1`` -- list or vector; the first row of the circulant matrix `X_1`
    - ``x2`` -- list or vector; the first row of the circulant matrix `X_2`
    - ``x3`` -- list or vector; the first row of the circulant matrix `X_3`
    - ``x4`` -- list or vector; the first row of the circulant matrix `X_4`
    - ``A`` -- the matrix described above
    - ``B`` -- the matrix described above
    - ``C`` -- the matrix described above
    - ``D`` -- the matrix described above
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the resulting
      matrix is Hadamard before returning it

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_cooper_wallis_construction
        sage: from sage.combinat.t_sequences import T_sequences_smallcases
        sage: seqs = T_sequences_smallcases(19)
        sage: hadamard_matrix_cooper_wallis_construction(seqs[0], seqs[1], seqs[2], seqs[3], matrix([1]), matrix([1]), matrix([1]), matrix([1]))
        76 x 76 dense matrix over Integer Ring...

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_cooper_wallis_construction, is_hadamard_matrix
        sage: seqs = T_sequences_smallcases(13)
        sage: H = hadamard_matrix_cooper_wallis_construction(seqs[0], seqs[1], seqs[2], seqs[3], matrix([1]), matrix([1]), matrix([1]), matrix([1]))
        sage: is_hadamard_matrix(H)
        True
        sage: len(H[0]) == 13*4*1
        True
        sage: hadamard_matrix_cooper_wallis_construction(seqs[0], seqs[1], seqs[2], seqs[3], matrix([1]), matrix([1, -1]), matrix([1]), matrix([1]))
        Traceback (most recent call last):
        ...
        AssertionError
        sage: hadamard_matrix_cooper_wallis_construction([1,-1], [1, 1], [1,1], [1,1], matrix([1]), matrix([1]), matrix([1]), matrix([1]))
        Traceback (most recent call last):
        ...
        AssertionError
    """
def hadamard_matrix_cooper_wallis_smallcases(n, check: bool = True, existence: bool = False):
    """
    Construct Hadamard matrices using the Cooper-Wallis construction for some small values of `n`.

    This function calls the function :func:`hadamard_matrix_cooper_wallis_construction`
    with the appropriate arguments.
    It constructs the matrices `X_1`, `X_2`, `X_3`, `X_4` using either
    T-matrices or the T-sequences from :func:`sage.combinat.t_sequences.T_sequences_smallcases`.
    The matrices `A`, `B`, `C`, `D` are taken from :func:`williamson_type_quadruples_smallcases`.

    Data for T-matrices of order 67 is taken from [Saw1985]_.

    INPUT:

    - ``n`` -- integer; the order of the matrix to be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard matrix before returning
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if
      the matrix exists

    OUTPUT:

    If ``existence=False``, returns the Hadamard matrix of order `n`. It raises an error if no data
    is available to construct the matrix of the given order.
    If ``existence=True``, returns a boolean representing whether the matrix can be constructed or not.

    .. SEEALSO::

        :func:`hadamard_matrix_cooper_wallis_construction`

    EXAMPLES:

    By default The function returns the Hadamard matrix ::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_cooper_wallis_smallcases
        sage: hadamard_matrix_cooper_wallis_smallcases(28)
        28 x 28 dense matrix over Integer Ring...

    If ``existence`` is set to True, the function returns a boolean ::

        sage: hadamard_matrix_cooper_wallis_smallcases(20, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_cooper_wallis_smallcases, is_hadamard_matrix
        sage: is_hadamard_matrix(hadamard_matrix_cooper_wallis_smallcases(188))
        True
        sage: hadamard_matrix_cooper_wallis_smallcases(64, existence=True)
        False
        sage: hadamard_matrix_cooper_wallis_smallcases(64)
        Traceback (most recent call last):
        ...
        ValueError: The Cooper-Wallis construction for Hadamard matrices of order 64 is not yet implemented.
        sage: hadamard_matrix_cooper_wallis_smallcases(14)
        Traceback (most recent call last):
        ...
        AssertionError
    """
def hadamard_matrix_turyn_type(a, b, c, d, e1, e2, e3, e4, check: bool = True):
    """
    Construction of Turyn type Hadamard matrix.

    Given `n\\times n` circulant matrices `A`, `B`, `C`, `D` with 1,-1 entries,
    satisfying `AA^\\top + BB^\\top + CC^\\top + DD^\\top = 4nI`, and a set of
    Baumert-Hall units of order `4t`, one can construct a Hadamard matrix of order
    `4tn` as detailed by Turyn in [Tur1974]_.

    INPUT:

    - ``a`` -- 1,-1 list; the 1st row of `A`
    - ``b`` -- 1,-1 list; the 1st row of `B`
    - ``d`` -- 1,-1 list; the 1st row of `C`
    - ``c`` -- 1,-1 list; the 1st row of `D`
    - ``e1`` -- matrix; the first Baumert-Hall unit
    - ``e2`` -- matrix; the second Baumert-Hall unit
    - ``e3`` -- matrix; the third Baumert-Hall unit
    - ``e4`` -- matrix; the fourth Baumert-Hall unit
    - ``check`` -- boolean (default: ``True``); whether to check that the output
      is a Hadamard matrix before returning it

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_turyn_type, _get_baumert_hall_units
        sage: A, B, C, D = _get_baumert_hall_units(28)
        sage: hadamard_matrix_turyn_type([1], [1], [1], [1], A, B, C, D)
        28 x 28 dense matrix over Integer Ring...

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_turyn_type, _get_baumert_hall_units, is_hadamard_matrix
        sage: A, B, C, D = _get_baumert_hall_units(12)
        sage: is_hadamard_matrix(hadamard_matrix_turyn_type([1], [1], [1], [1], A, B, C, D))
        True
        sage: hadamard_matrix_turyn_type([1, -1], [1], [1], [1], A, B, C, D)
        Traceback (most recent call last):
        ...
        AssertionError
        sage: hadamard_matrix_turyn_type([1, -1], [1, 1], [1, 1], [1, 1], A, B, C, D)
        Traceback (most recent call last):
        ...
        AssertionError
    """
def turyn_type_hadamard_matrix_smallcases(n, existence: bool = False, check: bool = True):
    """
    Construct a Hadamard matrix of order `n` from available 4-symbol `\\delta` codes and Williamson quadruples.

    The function looks for Baumert-Hall units and Williamson type matrices from
    :func:`four_symbol_delta_code_smallcases` and :func:`williamson_type_quadruples_smallcases`
    and use them to construct a Hadamard matrix with the Turyn construction
    defined in :func:`hadamard_matrix_turyn_type`.

    INPUT:

    - ``n`` -- integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if
      the matrix exists
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard matrix before returning

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import turyn_type_hadamard_matrix_smallcases
        sage: turyn_type_hadamard_matrix_smallcases(28, existence=True)
        True
        sage: turyn_type_hadamard_matrix_smallcases(28)
        28 x 28 dense matrix over Integer Ring...

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import turyn_type_hadamard_matrix_smallcases, is_hadamard_matrix
        sage: is_hadamard_matrix(turyn_type_hadamard_matrix_smallcases(236)) # long time
        True
        sage: turyn_type_hadamard_matrix_smallcases(64, existence=True)
        False
        sage: turyn_type_hadamard_matrix_smallcases(64)
        Traceback (most recent call last):
        ...
        ValueError: The Turyn type construction for Hadamard matrices of order 64 is not yet implemented.
    """
def hadamard_matrix_spence_construction(n, existence: bool = False, check: bool = True):
    """
    Create a Hadamard matrix of order `n` using the Spence construction.

    This construction (detailed in [Spe1975]_), uses supplementary difference sets implemented in
    :func:`sage.combinat.designs.difference_family.supplementary_difference_set_from_rel_diff_set` to create the
    desired matrix.

    INPUT:

    - ``n`` -- integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check if
      the matrix exists
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard matrix before returning

    OUTPUT:

    If ``existence=True``, returns a boolean representing whether the Hadamard
    matrix can be constructed. Otherwise, returns the Hadamard matrix, or raises
    an error if it cannot be constructed.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import hadamard_matrix_spence_construction
        sage: hadamard_matrix_spence_construction(36)
        36 x 36 dense matrix over Integer Ring...

    If ``existence`` is ``True``, the function returns a boolean ::

        sage: hadamard_matrix_spence_construction(52, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: is_hadamard_matrix(hadamard_matrix_spence_construction(100))
        True
        sage: hadamard_matrix_spence_construction(48, existence=True)
        False
        sage: hadamard_matrix_spence_construction(48)
        Traceback (most recent call last):
        ...
        ValueError: The order 48 is not covered by Spence construction.
        sage: hadamard_matrix_spence_construction(5)
        Traceback (most recent call last):
        ...
        AssertionError
        sage: hadamard_matrix_spence_construction(0)
        Traceback (most recent call last):
        ...
        AssertionError
    """
def is_hadamard_matrix(M, normalized: bool = False, skew: bool = False, verbose: bool = False):
    """
    Test if ``M`` is a Hadamard matrix.

    INPUT:

    - ``M`` -- a matrix
    - ``normalized`` -- boolean (default: ``False``); whether to test if ``M``
      is a normalized  Hadamard matrix, i.e. has its first row/column filled with +1
    - ``skew`` -- boolean (default: ``False``); whether to test if ``M`` is a skew
      Hadamard matrix, i.e. `M=S+I` for `-S=S^\\top`, and `I` the identity matrix
    - ``verbose`` -- boolean (default: ``False``); whether to be verbose when
      the matrix is not Hadamard

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: h = matrix.hadamard(12)
        sage: is_hadamard_matrix(h)
        True
        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix
        sage: h = skew_hadamard_matrix(12)
        sage: is_hadamard_matrix(h, skew=True)
        True
        sage: h = matrix.hadamard(12)
        sage: h[0,0] = 2
        sage: is_hadamard_matrix(h,verbose=True)
        The matrix does not only contain +1 and -1 entries, e.g. 2
        False
        sage: h = matrix.hadamard(12)
        sage: for i in range(12):
        ....:     h[i,2] = -h[i,2]
        sage: is_hadamard_matrix(h,verbose=True,normalized=True)
        The matrix is not normalized
        False

    TESTS::

        sage: h = matrix.hadamard(12)
        sage: is_hadamard_matrix(h, skew=True)
        False
        sage: is_hadamard_matrix(h, skew=True, verbose=True)
        The matrix is not skew
        False
        sage: h = skew_hadamard_matrix(12)
        sage: is_hadamard_matrix(h, skew=True, verbose=True)
        True
        sage: is_hadamard_matrix(h, skew=False, verbose=True)
        True
        sage: h = -h
        sage: is_hadamard_matrix(h, skew=True, verbose=True)
        The matrix is not skew - diagonal entries must be all 1
        False
        sage: is_hadamard_matrix(h, skew=False, verbose=True)
        True
        sage: h = skew_hadamard_matrix(20, skew_normalize=False)
        sage: is_hadamard_matrix(h, skew=True, normalized=True, verbose=True)
        The matrix is not skew-normalized
        False
        sage: from sage.combinat.matrices.hadamard_matrix import normalise_hadamard
        sage: h = normalise_hadamard(h, skew=True)
        sage: is_hadamard_matrix(h, skew=True, normalized=True, verbose=True)
        True
    """
def is_skew_hadamard_matrix(M, normalized: bool = False, verbose: bool = False):
    """
    Test if ``M`` is a skew Hadamard matrix.

    this is a wrapper around the function :func:`is_hadamard_matrix`

    INPUT:

    - ``M`` -- a matrix
    - ``normalized`` -- boolean (default: ``False``); whether to test if ``M``
      is a skew-normalized Hadamard matrix, i.e. has its first row filled with +1
    - ``verbose`` -- boolean (default: ``False``); whether to be verbose when the
      matrix is not skew Hadamard

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import is_skew_hadamard_matrix, skew_hadamard_matrix
        sage: h = matrix.hadamard(12)
        sage: is_skew_hadamard_matrix(h, verbose=True)
        The matrix is not skew
        False
        sage: h = skew_hadamard_matrix(12)
        sage: is_skew_hadamard_matrix(h)
        True
        sage: from sage.combinat.matrices.hadamard_matrix import normalise_hadamard
        sage: h = normalise_hadamard(skew_hadamard_matrix(12), skew=True)
        sage: is_skew_hadamard_matrix(h, verbose=True, normalized=True)
        True
    """
@matrix_method
def hadamard_matrix(n, existence: bool = False, check: bool = True, construction_name: bool = False):
    """
    Try to construct a Hadamard matrix using the available methods.

    Currently all orders `\\le 1200` for which a construction is
    known are implemented. For `n > 1200`, only some orders are available.

    INPUT:

    - ``n`` -- integer; dimension of the matrix
    - ``existence`` -- boolean (default: ``False``); whether to build the matrix
      or merely query if a construction is available in Sage. When set to ``True``,
      the function returns:

        - ``True`` -- meaning that Sage knows how to build the matrix
        - ``Unknown`` -- meaning that Sage does not know how to build the
          matrix, although the matrix may exist (see :mod:`sage.misc.unknown`).
        - ``False`` -- meaning that the matrix does not exist

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.
    - ``construction_name`` -- boolean (default: ``False``); if it is ``True``,
      ``existence`` is ``True``, and a matrix exists, output the construction name.
      It has no effect if ``existence`` is set to ``False``.

    EXAMPLES::

        sage: hadamard_matrix(12).det()
        2985984
        sage: 12^6
        2985984
        sage: hadamard_matrix(1)
        [1]
        sage: hadamard_matrix(2)
        [ 1  1]
        [ 1 -1]
        sage: hadamard_matrix(8) # random
        [ 1  1  1  1  1  1  1  1]
        [ 1 -1  1 -1  1 -1  1 -1]
        [ 1  1 -1 -1  1  1 -1 -1]
        [ 1 -1 -1  1  1 -1 -1  1]
        [ 1  1  1  1 -1 -1 -1 -1]
        [ 1 -1  1 -1 -1  1 -1  1]
        [ 1  1 -1 -1 -1 -1  1  1]
        [ 1 -1 -1  1 -1  1  1 -1]
        sage: hadamard_matrix(8).det() == 8^4
        True

    We note that :func:`hadamard_matrix` returns a normalised Hadamard matrix
    (the entries in the first row and column are all +1) ::

        sage: hadamard_matrix(12) # random
        [ 1  1| 1  1| 1  1| 1  1| 1  1| 1  1]
        [ 1 -1|-1  1|-1  1|-1  1|-1  1|-1  1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1| 1 -1| 1  1|-1 -1|-1 -1| 1  1]
        [ 1  1|-1 -1| 1 -1|-1  1|-1  1| 1 -1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1| 1  1| 1 -1| 1  1|-1 -1|-1 -1]
        [ 1  1| 1 -1|-1 -1| 1 -1|-1  1|-1  1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1|-1 -1| 1  1| 1 -1| 1  1|-1 -1]
        [ 1  1|-1  1| 1 -1|-1 -1| 1 -1|-1  1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1|-1 -1|-1 -1| 1  1| 1 -1| 1  1]
        [ 1  1|-1  1|-1  1| 1 -1|-1 -1| 1 -1]
        [-----+-----+-----+-----+-----+-----]
        [ 1 -1| 1  1|-1 -1|-1 -1| 1  1| 1 -1]
        [ 1  1| 1 -1|-1  1|-1  1| 1 -1|-1 -1]

    To find how the matrix is obtained, use ``construction_name`` ::

        sage: matrix.hadamard(476, existence=True, construction_name=True)
        'cooper-wallis small cases: 476'

    TESTS::

        sage: matrix.hadamard(10,existence=True)
        False
        sage: matrix.hadamard(12,existence=True)
        True
        sage: matrix.hadamard(668,existence=True)
        Unknown
        sage: matrix.hadamard(10)
        Traceback (most recent call last):
        ...
        ValueError: The Hadamard matrix of order 10 does not exist
        sage: matrix.hadamard(312, existence=True)
        True
        sage: matrix.hadamard(1904, existence=True)
        True
        sage: matrix.hadamard(324, existence=True)
        True
    """
def hadamard_matrix_www(url_file, comments: bool = False):
    '''
    Pull file from Sloane\'s database and return the corresponding Hadamard
    matrix as a Sage matrix.

    You must input a filename of the form "had.n.xxx.txt" as described
    on the webpage http://neilsloane.com/hadamard/, where
    "xxx" could be empty or a number of some characters.

    If ``comments=True`` then the "Automorphism..." line of the had.n.xxx.txt
    file is printed if it exists. Otherwise nothing is done.

    EXAMPLES::

        sage: hadamard_matrix_www("had.4.txt")      # optional - internet
        [ 1  1  1  1]
        [ 1 -1  1 -1]
        [ 1  1 -1 -1]
        [ 1 -1 -1  1]
        sage: hadamard_matrix_www("had.16.2.txt",comments=True)   # optional - internet
        Automorphism group has order = 49152 = 2^14 * 3
        [ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1]
        [ 1 -1  1 -1  1 -1  1 -1  1 -1  1 -1  1 -1  1 -1]
        [ 1  1 -1 -1  1  1 -1 -1  1  1 -1 -1  1  1 -1 -1]
        [ 1 -1 -1  1  1 -1 -1  1  1 -1 -1  1  1 -1 -1  1]
        [ 1  1  1  1 -1 -1 -1 -1  1  1  1  1 -1 -1 -1 -1]
        [ 1 -1  1 -1 -1  1 -1  1  1 -1  1 -1 -1  1 -1  1]
        [ 1  1 -1 -1 -1 -1  1  1  1  1 -1 -1 -1 -1  1  1]
        [ 1 -1 -1  1 -1  1  1 -1  1 -1 -1  1 -1  1  1 -1]
        [ 1  1  1  1  1  1  1  1 -1 -1 -1 -1 -1 -1 -1 -1]
        [ 1  1  1  1 -1 -1 -1 -1 -1 -1 -1 -1  1  1  1  1]
        [ 1  1 -1 -1  1 -1  1 -1 -1 -1  1  1 -1  1 -1  1]
        [ 1  1 -1 -1 -1  1 -1  1 -1 -1  1  1  1 -1  1 -1]
        [ 1 -1  1 -1  1 -1 -1  1 -1  1 -1  1 -1  1  1 -1]
        [ 1 -1  1 -1 -1  1  1 -1 -1  1 -1  1  1 -1 -1  1]
        [ 1 -1 -1  1  1  1 -1 -1 -1  1  1 -1 -1 -1  1  1]
        [ 1 -1 -1  1 -1 -1  1  1 -1  1  1 -1  1  1 -1 -1]
    '''
def regular_symmetric_hadamard_matrix_with_constant_diagonal(n, e, existence: bool = False):
    """
    Return a Regular Symmetric Hadamard Matrix with Constant Diagonal.

    A Hadamard matrix is said to be *regular* if its rows all sum to the same
    value.

    For `\\epsilon\\in\\{-1,+1\\}`, we say that `M` is a `(n,\\epsilon)-RSHCD` if
    `M` is a regular symmetric Hadamard matrix with constant diagonal
    `\\delta\\in\\{-1,+1\\}` and row sums all equal to `\\delta \\epsilon
    \\sqrt(n)`. For more information, see [HX2010]_ or 10.5.1 in
    [BH2012]_. For the case `n=324`, see :func:`RSHCD_324` and [CP2016]_.

    INPUT:

    - ``n`` -- integer; side of the matrix
    - ``e`` -- `-1` or `+1`; the value of `\\epsilon`

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import regular_symmetric_hadamard_matrix_with_constant_diagonal
        sage: regular_symmetric_hadamard_matrix_with_constant_diagonal(4,1)
        [ 1  1  1 -1]
        [ 1  1 -1  1]
        [ 1 -1  1  1]
        [-1  1  1  1]
        sage: regular_symmetric_hadamard_matrix_with_constant_diagonal(4,-1)
        [ 1 -1 -1 -1]
        [-1  1 -1 -1]
        [-1 -1  1 -1]
        [-1 -1 -1  1]

    Other hardcoded values::

        sage: for n,e in [(36,1),(36,-1),(100,1),(100,-1),(196, 1)]:  # long time
        ....:     print(repr(regular_symmetric_hadamard_matrix_with_constant_diagonal(n,e)))
        36 x 36 dense matrix over Integer Ring
        36 x 36 dense matrix over Integer Ring
        100 x 100 dense matrix over Integer Ring
        100 x 100 dense matrix over Integer Ring
        196 x 196 dense matrix over Integer Ring

        sage: for n,e in [(324,1),(324,-1)]: # not tested - long time, tested in RSHCD_324
        ....:     print(repr(regular_symmetric_hadamard_matrix_with_constant_diagonal(n,e)))
        324 x 324 dense matrix over Integer Ring
        324 x 324 dense matrix over Integer Ring

    From two close prime powers::

        sage: regular_symmetric_hadamard_matrix_with_constant_diagonal(64,-1)
        64 x 64 dense matrix over Integer Ring (use the '.str()' method to see the entries)

    From a prime power and a conference matrix::

        sage: regular_symmetric_hadamard_matrix_with_constant_diagonal(676,1)  # long time
        676 x 676 dense matrix over Integer Ring (use the '.str()' method to see the entries)

    Recursive construction::

        sage: regular_symmetric_hadamard_matrix_with_constant_diagonal(144,-1)
        144 x 144 dense matrix over Integer Ring (use the '.str()' method to see the entries)

    REFERENCE:

    - [BH2012]_

    - [HX2010]_
    """
def RSHCD_324(e):
    '''
    Return a size 324x324 Regular Symmetric Hadamard Matrix with Constant Diagonal.

    We build the matrix `M` for the case `n=324`, `\\epsilon=1` directly from
    :meth:`JankoKharaghaniTonchevGraph
    <sage.graphs.graph_generators.GraphGenerators.JankoKharaghaniTonchevGraph>`
    and for the case `\\epsilon=-1` from the "twist" `M\'` of `M`, using Lemma 11
    in [HX2010]_. Namely, it turns out that the matrix

    .. MATH::

        M\'=\\begin{pmatrix} M_{12} & M_{11}\\\\ M_{11}^\\top & M_{21} \\end{pmatrix},
        \\quad\\text{where}\\quad
        M=\\begin{pmatrix} M_{11} & M_{12}\\\\ M_{21} & M_{22} \\end{pmatrix},

    and the `M_{ij}` are 162x162-blocks, also RSHCD, its diagonal blocks having zero row
    sums, as needed by [loc.cit.]. Interestingly, the corresponding
    `(324,152,70,72)`-strongly regular graph
    has a vertex-transitive automorphism group of order 2592, twice the order of the
    (intransitive) automorphism group of the graph corresponding to `M`. Cf. [CP2016]_.

    INPUT:

    - ``e`` -- `-1` or `+1`; the value of `\\epsilon`

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import RSHCD_324, is_hadamard_matrix
        sage: for e in [1,-1]:  # long time
        ....:     M = RSHCD_324(e)
        ....:     print("{} {} {}".format(M==M.T,is_hadamard_matrix(M),all(M[i,i]==1 for i in range(324))))
        ....:     print(list(set(sum(x) for x in M)))
        True True True
        [18]
        True True True
        [-18]

    REFERENCE:

    - [CP2016]_
    '''
def rshcd_from_close_prime_powers(n):
    """
    Return a `(n^2,1)`-RSHCD when `n-1` and `n+1` are odd prime powers and `n=0\\pmod{4}`.

    The construction implemented here appears in Theorem 4.3 from [GS1970]_.

    Note that the authors of [SWW1972]_ claim in Corollary 5.12 (page 342) to have
    proved the same result without the `n=0\\pmod{4}` restriction with a *very*
    similar construction. So far, however, I (Nathann Cohen) have not been able
    to make it work.

    INPUT:

    - ``n`` -- integer congruent to `0\\pmod{4}`

    .. SEEALSO::

        :func:`regular_symmetric_hadamard_matrix_with_constant_diagonal`

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import rshcd_from_close_prime_powers
        sage: rshcd_from_close_prime_powers(4)
        [-1 -1  1 -1  1 -1 -1  1 -1  1 -1 -1  1 -1  1 -1]
        [-1 -1 -1  1  1 -1 -1  1 -1 -1  1 -1 -1  1 -1  1]
        [ 1 -1 -1  1  1  1  1 -1 -1 -1 -1 -1 -1 -1  1 -1]
        [-1  1  1 -1  1  1 -1 -1 -1 -1 -1  1 -1 -1 -1  1]
        [ 1  1  1  1 -1 -1 -1 -1 -1 -1  1 -1  1 -1 -1 -1]
        [-1 -1  1  1 -1 -1  1 -1 -1  1 -1  1 -1  1 -1 -1]
        [-1 -1  1 -1 -1  1 -1 -1  1 -1  1 -1 -1  1  1 -1]
        [ 1  1 -1 -1 -1 -1 -1 -1 -1  1 -1 -1 -1  1  1  1]
        [-1 -1 -1 -1 -1 -1  1 -1 -1 -1  1  1  1 -1  1  1]
        [ 1 -1 -1 -1 -1  1 -1  1 -1 -1 -1  1  1  1 -1 -1]
        [-1  1 -1 -1  1 -1  1 -1  1 -1 -1 -1  1  1 -1 -1]
        [-1 -1 -1  1 -1  1 -1 -1  1  1 -1 -1  1 -1 -1  1]
        [ 1 -1 -1 -1  1 -1 -1 -1  1  1  1  1 -1 -1 -1 -1]
        [-1  1 -1 -1 -1  1  1  1 -1  1  1 -1 -1 -1 -1 -1]
        [ 1 -1  1 -1 -1 -1  1  1  1 -1 -1 -1 -1 -1 -1  1]
        [-1  1 -1  1 -1 -1 -1  1  1 -1 -1  1 -1 -1  1 -1]

    REFERENCE:

    - [SWW1972]_
    """
def williamson_goethals_seidel_skew_hadamard_matrix(a, b, c, d, check: bool = True):
    """
    Williamson-Goethals-Seidel construction of a skew Hadamard matrix.

    Given `n\\times n` (anti)circulant matrices `A`, `B`, `C`, `D` with 1,-1 entries,
    and satisfying `A+A^\\top = 2I`, `AA^\\top + BB^\\top + CC^\\top + DD^\\top = 4nI`,
    one can construct a skew Hadamard matrix of order `4n`, cf. [GS70s]_.

    INPUT:

    - ``a`` -- 1,-1 list; the 1st row of `A`
    - ``b`` -- 1,-1 list; the 1st row of `B`
    - ``d`` -- 1,-1 list; the 1st row of `C`
    - ``c`` -- 1,-1 list; the 1st row of `D`
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the
      resulting matrix is skew Hadamard before returning it

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import williamson_goethals_seidel_skew_hadamard_matrix as WGS
        sage: a = [ 1,  1, 1, -1,  1, -1,  1, -1, -1]
        sage: b = [ 1, -1, 1,  1, -1, -1,  1,  1, -1]
        sage: c = [-1, -1]+[1]*6+[-1]
        sage: d = [ 1,  1, 1, -1,  1,  1, -1,  1,  1]
        sage: M = WGS(a,b,c,d,check=True)

    REFERENCES:

    - [GS70s]_

    - [Wall71]_

    - [KoSt08]_
    """
def skew_hadamard_matrix_spence_construction(n, check: bool = True):
    """
    Construct skew Hadamard matrix of order `n` using Spence construction.

    This function will construct skew Hadamard matrix of order `n=2(q+1)` where `q` is
    a prime power with `q = 5` (mod 8). The construction is taken from [Spe1977]_, and the
    relative difference sets are constructed using :func:`sage.combinat.designs.difference_family.relative_difference_set_from_homomorphism`.

    INPUT:

    - ``n`` -- positive integer
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the
      resulting matrix is Hadamard before returning it

    OUTPUT:

    If ``n`` satisfies the requirements described above, the function returns a
    `n\\times n` Hadamard matrix. Otherwise, an exception is raised.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_spence_construction
        sage: skew_hadamard_matrix_spence_construction(28)
        28 x 28 dense matrix over Integer Ring...

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: is_hadamard_matrix(skew_hadamard_matrix_spence_construction(12, check=False), skew=True)
        True
        sage: is_hadamard_matrix(skew_hadamard_matrix_spence_construction(60, check=False), skew=True)
        True
        sage: skew_hadamard_matrix_spence_construction(31)
        Traceback (most recent call last):
        ...
        ValueError: The order 31 is not covered by the Spence construction.
        sage: skew_hadamard_matrix_spence_construction(16)
        Traceback (most recent call last):
        ...
        ValueError: The order 16 is not covered by the Spence construction.
    """
def skew_hadamard_matrix_spence_1975(n, existence: bool = False, check: bool = True):
    """
    Construct a skew Hadamard matrix of order `n = 4(1 + q + q^2)` using the
    Spence construction.

    If `n = 4(1 + q + q^2)` where `q` is a prime power such that either
    `1 + q + q^2` is a prime congruent to `3, 5, 7 \\mod 8` or `3 + 2q + 2q^2` is
    a prime power, then a skew Hadamard matrix of order `n` can be constructed using
    the Goethals Seidel array. The four matrices `A, B, C, D` plugged into the
    GS-array are created using complementary difference sets of order `1 + q + q^2`
    (which exist if `q` satisfies the conditions above), and a cyclic planar
    difference set with parameters `(1 + q^2 + q^4, 1 + q^2, 1)`.
    These are constructed by the functions :func:`sage.combinat.designs.difference_family.complementary_difference_sets`
    and :func:`sage.combinat.designs.difference_family.difference_family`.

    For more details, see [Spe1975b]_.

    INPUT:

    - ``n`` -- positive integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether the Hadamard matrix can be constructed
    - ``check`` -- boolean (default: ``True``); check that the result
      is a skew Hadamard matrix before returning it

    OUTPUT:

    If ``existence=False``, returns the skew Hadamard matrix of order `n`. It
    raises an error if `n` does not satisfy the required conditions.
    If ``existence=True``, returns a boolean representing whether the matrix
    can be constructed or not.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_spence_1975
        sage: skew_hadamard_matrix_spence_1975(52)
        52 x 52 dense matrix over Integer Ring...

    If ``existence`` is True, the function returns a boolean::

        sage: skew_hadamard_matrix_spence_1975(52, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_skew_hadamard_matrix
        sage: is_skew_hadamard_matrix(skew_hadamard_matrix_spence_1975(52, check=False))
        True
        sage: skew_hadamard_matrix_spence_1975(100, existence=True)
        False
        sage: skew_hadamard_matrix_spence_1975(31)
        Traceback (most recent call last):
        ...
        ValueError: n is not in the form 4*(1+q+q^2)
        sage: skew_hadamard_matrix_spence_1975(16)
        Traceback (most recent call last):
        ...
        ValueError: n is not in the form 4*(1+q+q^2)
        sage: skew_hadamard_matrix_spence_1975(292)
        Traceback (most recent call last):
        ...
        ValueError: q=8 is not a valid parameter for this construction
    """
def GS_skew_hadamard_smallcases(n, existence: bool = False, check: bool = True):
    """
    Data for Williamson-Goethals-Seidel construction of skew Hadamard matrices.

    Here we keep the data for this construction.
    Namely, it needs 4 circulant matrices with extra properties, as described in
    :func:`sage.combinat.matrices.hadamard_matrix.williamson_goethals_seidel_skew_hadamard_matrix`
    Matrices are taken from:

    * `n=36, 52`: [GS70s]_
    * `n=92`: [Wall71]_
    * `n=188`: [Djo2008a]_
    * `n=236`: [FKS2004]_
    * `n=276`: [Djo2023a]_

    Additional data is obtained from skew supplementary difference sets contained in
    :func:`sage.combinat.designs.difference_family.skew_supplementary_difference_set`, using the
    construction described in [Djo1992a]_.

    INPUT:

    - ``n`` -- integer; the order of the matrix
    - ``existence`` -- boolean (default: ``True``); if ``True``, only check that
      we can do the construction
    - ``check`` -- boolean (default: ``False``); if ``True``, check the result

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import GS_skew_hadamard_smallcases, is_skew_hadamard_matrix
        sage: GS_skew_hadamard_smallcases(36)
        36 x 36 dense matrix over Integer Ring...
        sage: GS_skew_hadamard_smallcases(52)
        52 x 52 dense matrix over Integer Ring...
        sage: GS_skew_hadamard_smallcases(92)
        92 x 92 dense matrix over Integer Ring...
        sage: GS_skew_hadamard_smallcases(100)
        sage: is_skew_hadamard_matrix(GS_skew_hadamard_smallcases(324, check=False))
        True
        sage: is_skew_hadamard_matrix(GS_skew_hadamard_smallcases(156, check=False))
        True
    """
def skew_hadamard_matrix_from_orthogonal_design(n, existence: bool = False, check: bool = True):
    """
    Construct skew Hadamard matrices of order `mn(n - 1)` if suitable orthogonal designs exist.

    In [Seb1978]_ is proved that if amicable Hadamard matrices of order `n` and an orthogonal
    design of type `(1, m, mn - m - 1)` in order `mn` exist, then a skew Hadamard matrix
    of order `mn(n - 1)` can be constructed. The paper uses amicable orthogonal designs
    instead of amicable Hadamard matrices, but the two are equivalent (see [Seb2017]_).

    Amicable Hadamard matrices are constructed using :func:`amicable_hadamard_matrices`,
    and the orthogonal designs are constructed using the Goethals-Seidel array,
    with data taken from [Seb2017]_.

    INPUT:

    - ``n`` -- positive integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether the skew Hadamard matrix can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the result
      is a skew Hadamard matrix before returning it

    OUTPUT:

    If ``existence=False``, returns the skew Hadamard matrix of order `n`. It
    raises an error if a construction for order `n` is not yet implemented, or if
    `n` does not satisfy the constraint.
    If ``existence=True``, returns a boolean representing whether the matrix
    can be constructed or not.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_from_orthogonal_design
        sage: skew_hadamard_matrix_from_orthogonal_design(756)
        756 x 756 dense matrix over Integer Ring...

    If ``existence`` is True, the function returns a boolean::

        sage: skew_hadamard_matrix_from_orthogonal_design(200, existence=True)
        False

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_skew_hadamard_matrix
        sage: is_skew_hadamard_matrix(skew_hadamard_matrix_from_orthogonal_design(756, check=False))
        True
        sage: skew_hadamard_matrix_from_orthogonal_design(31)
        Traceback (most recent call last):
        ...
        ValueError: n must be a multiple of 4
        sage: skew_hadamard_matrix_from_orthogonal_design(16)
        Traceback (most recent call last):
        ...
        NotImplementedError: orthogonal designs for matrix of order 16 not yet implemented
    """
def skew_hadamard_matrix_from_complementary_difference_sets(n, existence: bool = False, check: bool = True):
    """
    Construct a skew Hadamard matrix of order `n=4(m+1)` from complementary difference sets.

    If `A, B` are complementary difference sets over a group of order `2m+1`, then
    they can be used to construct a skew Hadamard matrix, as described in [BS1969]_.

    The complementary difference sets are constructed using the function
    :func:`sage.combinat.designs.difference_family.complementary_difference_sets`.

    INPUT:

    - ``n`` -- positive integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether the skew Hadamard matrix can be constructed
    - ``check`` -- boolean (default: ``True``);  if ``True``, check that the
      result is a skew Hadamard matrix before returning it

    OUTPUT:

    If ``existence=False``, returns the skew Hadamard matrix of order `n`. It
    raises an error if `n` does not satisfy the required conditions.
    If ``existence=True``, returns a boolean representing whether the matrix
    can be constructed or not.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_from_complementary_difference_sets
        sage: skew_hadamard_matrix_from_complementary_difference_sets(20)
        20 x 20 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix_from_complementary_difference_sets(52, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_skew_hadamard_matrix
        sage: is_skew_hadamard_matrix(skew_hadamard_matrix_from_complementary_difference_sets(24, check=False))
        True
        sage: is_skew_hadamard_matrix(skew_hadamard_matrix_from_complementary_difference_sets(12, check=False))
        True
        sage: skew_hadamard_matrix_from_complementary_difference_sets(31)
        Traceback (most recent call last):
        ...
        ValueError: n must be 1, 2 or a multiple of four.
        sage: skew_hadamard_matrix_from_complementary_difference_sets(100)
        Traceback (most recent call last):
        ...
        NotImplementedError: hadamard matrix of order 100 from complementary difference sets is not implemented yet
        sage: skew_hadamard_matrix_from_complementary_difference_sets(100, existence=True)
        False
    """
def skew_hadamard_matrix_whiteman_construction(n, existence: bool = False, check: bool = True):
    """
    Construct a skew Hadamard matrix of order `n=2(q+1)` where `q=p^t` is a prime power with `p \\cong 5 \\mod 8` and `t \\cong 2 \\mod 4`.

    Assuming `n` satisfies the conditions above, it is possible to construct two supplementary difference sets
    `A, B` (see [Whi1971]_), and these can be used to construct a skew Hadamard matrix, as described in [BS1969]_.

    INPUT:

    - ``n`` -- positive integer; the order of the matrix to be constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether the Hadamard matrix can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the result
      is a skew Hadamard matrix before returning it

    OUTPUT:

    If ``existence=False``, returns the skew Hadamard matrix of order `n`. It
    raises an error if `n` does not satisfy the required conditions.
    If ``existence=True``, returns a boolean representing whether the matrix can
    be constructed or not.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_whiteman_construction
        sage: skew_hadamard_matrix_whiteman_construction(52)
        52 x 52 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix_whiteman_construction(52, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: is_hadamard_matrix(skew_hadamard_matrix_whiteman_construction(52, check=False), skew=True)
        True
        sage: is_hadamard_matrix(skew_hadamard_matrix_whiteman_construction(340, check=False), skew=True)
        True
        sage: skew_hadamard_matrix_whiteman_construction(31)
        Traceback (most recent call last):
        ...
        ValueError: The order 31 is not covered by the Whiteman construction.
        sage: skew_hadamard_matrix_whiteman_construction(100)
        Traceback (most recent call last):
        ...
        ValueError: The order 100 is not covered by the Whiteman construction.
        sage: skew_hadamard_matrix_whiteman_construction(100, existence=True)
        False

    .. NOTE::

        A more general version of this construction is :func:`skew_hadamard_matrix_from_complementary_difference_sets`.
    """
def skew_hadamard_matrix_from_good_matrices(a, b, c, d, check: bool = True):
    """
    Construct skew Hadamard matrix from good matrices.

    Given good matrices `A`, `B`, `C`, `D` (`A` circulant, `B, C, D` back-circulant) they can be used to construct
    a skew Hadamard matrix using the following block matrix (as described in [Sze1988]_):

    .. MATH::

        \\left(\\begin{array}{rrrr}
        A & B & C & D \\\\\n        -B & A & D & -C \\\\\n        -C & -D & A & B \\\\\n        -D & C & -B & A
        \\end{array}\\right)

    INPUT:

    - ``a`` -- (1,-1) list; the 1st row of `A`
    - ``b`` -- (1,-1) list; the 1st row of `B`
    - ``d`` -- (1,-1) list; the 1st row of `C`
    - ``c`` -- (1,-1) list; the 1st row of `D`
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a skew Hadamard matrix before returning it

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_from_good_matrices
        sage: a, b, c, d = ([1, 1, 1, -1, -1], [1, -1, 1, 1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1])
        sage: skew_hadamard_matrix_from_good_matrices(a, b, c, d)
        20 x 20 dense matrix over Integer Ring...

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: a, b, c, d = ([1, 1, 1, -1, -1], [1, -1, 1, 1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1])
        sage: is_hadamard_matrix(skew_hadamard_matrix_from_good_matrices(a, b, c, d, check=False), skew=True)
        True
        sage: a, b, c, d = ([1, 1, 1, -1, -1], [1, -1, 1, 1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, 1])
        sage: skew_hadamard_matrix_from_good_matrices(a, b, c, d)
        Traceback (most recent call last):
        ...
        AssertionError
        sage: a, b, c, d = ([1, 1, 1], [1, -1, 1, 1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1])
        sage: skew_hadamard_matrix_from_good_matrices(a, b, c, d)
        Traceback (most recent call last):
        ...
        AssertionError
    """
def skew_hadamard_matrix_from_good_matrices_smallcases(n, existence: bool = False, check: bool = True):
    """
    Construct skew Hadamard matrices from good matrices for some small values of `n=4m`, with `m` odd.

    The function stores good matrices of odd orders `\\le 31`, taken from [Sze1988]_.
    These are used to create skew Hadamard matrices of order `4m`, `1 \\le m \\le 31` (`m` odd), using the function
    :func:`skew_hadamard_matrix_from_good_matrices`.

    ALGORITHM:

    Given four sequences (stored in ``E_sequences``) of length `m`, they can be used to construct four `E-sequences`
    of length `n=2m+1`, as follows:

    .. MATH::

        \\begin{aligned}
        a &= 1, a_0, a_1, ..., a_m, -a_m, -a_{m-1}, ..., -a_0 \\\\\n        b &= 1, b_0, b_1, ..., b_m, b_m, b_{m-1}, ..., b_0 \\\\\n        c &= 1, c_0, c_1, ..., c_m, c_m, c_{m-1}, ..., c_0 \\\\\n        d &= 1, d_0, d_1, ..., d_m, d_m, d_{m-1}, ..., d_0 \\\\\n        \\end{aligned}

    These E-sequences will be the first rows of the four good matrices needed to construct a skew Hadamard matrix
    of order `4n`.

    INPUT:

    - ``n`` -- integer; the order of the skew Hadamard matrix to be constructed
    - ``existence`` -- boolean (default:  ``False``); if ``True``, only return
      whether the Hadamard matrix can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the matrix
      is a Hadamard matrix before returning it

    OUTPUT:

    If ``existence=False``, returns the skew Hadamard matrix of order `n`. It
    raises an error if no data is available to construct the matrix of the given
    order.
    If ``existence=True``, returns a boolean representing whether the matrix can
    be constructed or not.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix_from_good_matrices_smallcases
        sage: skew_hadamard_matrix_from_good_matrices_smallcases(20)
        20 x 20 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix_from_good_matrices_smallcases(20, existence=True)
        True

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: is_hadamard_matrix(skew_hadamard_matrix_from_good_matrices_smallcases(28, check=False), skew=True)
        True
        sage: skew_hadamard_matrix_from_good_matrices_smallcases(140)
        Traceback (most recent call last):
        ...
        ValueError: The Good matrices of order 35 are not yet implemented.
        sage: skew_hadamard_matrix_from_good_matrices_smallcases(14)
        Traceback (most recent call last):
        ...
        ValueError: The skew Hadamard matrix of order 14 from good matrices does not exist.
        sage: skew_hadamard_matrix_from_good_matrices_smallcases(140, existence=True)
        False
        sage: skew_hadamard_matrix_from_good_matrices_smallcases(14, existence=True)
        False
    """
def skew_hadamard_matrix(n, existence: bool = False, skew_normalize: bool = True, check: bool = True, construction_name: bool = False):
    """
    Try to construct a skew Hadamard matrix.

    A Hadamard matrix `H` is called skew if `H=S-I`, for `I` the identity matrix
    and `-S=S^\\top`. Currently all orders `\\le 1200` for which a construction is
    known are implemented. For `n > 1200`, only some orders are available.

    INPUT:

    - ``n`` -- integer; dimension of the matrix
    - ``existence`` -- boolean (default: ``False``); whether to build the matrix
      or merely query if a construction is available in Sage. When set to ``True``,
      the function returns:

        - ``True`` -- meaning that Sage knows how to build the matrix
        - ``Unknown`` -- meaning that Sage does not know how to build the
          matrix, but that the design may exist (see :mod:`sage.misc.unknown`).
        - ``False`` -- meaning that the matrix does not exist

    - ``skew_normalize`` -- boolean (default: ``True``); whether to make the 1st
      row all-one, and adjust the 1st column accordingly
    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.
    - ``construction_name`` -- boolean (default: ``False``); if it is ``True``,
      ``existence`` is ``True``, and a matrix exists, output the construction name.
      It has no effect if ``existence`` is set to ``False``.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import skew_hadamard_matrix
        sage: skew_hadamard_matrix(12).det()
        2985984
        sage: 12^6
        2985984
        sage: skew_hadamard_matrix(1)
        [1]
        sage: skew_hadamard_matrix(2)
        [ 1  1]
        [-1  1]
        sage: skew_hadamard_matrix(196, existence=True, construction_name=True)
        'Williamson-Goethals-Seidel: 196'

    TESTS::

        sage: skew_hadamard_matrix(10,existence=True)
        False
        sage: skew_hadamard_matrix(12,existence=True)
        True
        sage: skew_hadamard_matrix(784,existence=True)
        True
        sage: skew_hadamard_matrix(10)
        Traceback (most recent call last):
        ...
        ValueError: A skew Hadamard matrix of order 10 does not exist
        sage: skew_hadamard_matrix(36)
        36 x 36 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix(36)==skew_hadamard_matrix(36,skew_normalize=False)
        False
        sage: skew_hadamard_matrix(52)
        52 x 52 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix(92)
        92 x 92 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix(816)     # long time
        816 x 816 dense matrix over Integer Ring...
        sage: skew_hadamard_matrix(356)
        Traceback (most recent call last):
        ...
        ValueError: A skew Hadamard matrix of order 356 is not yet implemented.
        sage: skew_hadamard_matrix(356,existence=True)
        Unknown

    Check that :issue:`28526` is fixed::

        sage: skew_hadamard_matrix(0)
        Traceback (most recent call last):
        ...
        ValueError: parameter n must be strictly positive

    REFERENCES:

    - [Ha83]_
    """
def symmetric_conference_matrix(n, check: bool = True, existence: bool = False):
    """
    Try to construct a symmetric conference matrix.

    A conference matrix is an `n\\times n` matrix `C` with 0s on the main diagonal
    and 1s and -1s elsewhere, satisfying `CC^\\top=(n-1)I`.
    If `C=C^\\top` then `n \\cong 2 \\mod 4` and `C` is Seidel adjacency matrix of
    a graph, whose descendent graphs are strongly regular graphs with parameters
    `(n-1,(n-2)/2,(n-6)/4,(n-2)/4)`, see Sec.10.4 of [BH2012]_. Thus we build `C`
    from the Seidel adjacency matrix of the latter by adding row and column of 1s.

    INPUT:

    - ``n`` -- integer;  dimension of the matrix
    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.
    - ``existence`` -- boolean (default: ``False``); if true, only check that such
      a matrix exists.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import symmetric_conference_matrix
        sage: C = symmetric_conference_matrix(10); C
        [ 0  1  1  1  1  1  1  1  1  1]
        [ 1  0 -1 -1  1 -1  1  1  1 -1]
        [ 1 -1  0 -1  1  1 -1 -1  1  1]
        [ 1 -1 -1  0 -1  1  1  1 -1  1]
        [ 1  1  1 -1  0 -1 -1  1 -1  1]
        [ 1 -1  1  1 -1  0 -1  1  1 -1]
        [ 1  1 -1  1 -1 -1  0 -1  1  1]
        [ 1  1 -1  1  1  1 -1  0 -1 -1]
        [ 1  1  1 -1 -1  1  1 -1  0 -1]
        [ 1 -1  1  1  1 -1  1 -1 -1  0]
        sage: C^2 == 9*identity_matrix(10) and C == C.T
        True
    """
def szekeres_difference_set_pair(m, check: bool = True):
    """
    Construct Szekeres `(2m+1,m,1)`-cyclic difference family.

    Let `4m+3` be a prime power. Theorem 3 in [Sz1969]_ contains a construction of a pair
    of *complementary difference sets* `A`, `B` in the subgroup `G` of the quadratic
    residues in `F_{4m+3}^*`. Namely `|A|=|B|=m`, `a\\in A` whenever `a-1\\in G`, `b\\in B`
    whenever `b+1 \\in G`. See also Theorem 2.6 in [SWW1972]_ (there the formula for `B` is
    correct, as opposed to (4.2) in [Sz1969]_, where the sign before `1` is wrong.

    In modern terminology, for `m>1` the sets `A` and `B` form a
    :func:`difference family<sage.combinat.designs.difference_family>` with parameters `(2m+1,m,1)`.
    I.e. each non-identity `g \\in G` can be expressed uniquely as `xy^{-1}` for `x,y \\in A` or `x,y \\in B`.
    Other, specific to this construction, properties of `A` and `B` are: for `a` in `A` one has
    `a^{-1}` not in `A`, whereas for `b` in `B` one has `b^{-1}` in `B`.

    INPUT:

    - ``m`` -- integer; dimension of the matrix
    - ``check`` -- boolean (default: ``True``); whether to check `A` and `B` for
      correctness

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import szekeres_difference_set_pair
        sage: G,A,B=szekeres_difference_set_pair(6)
        sage: G,A,B=szekeres_difference_set_pair(7)

    REFERENCE:

    - [Sz1969]_
    """
def typeI_matrix_difference_set(G, A):
    """
    (1,-1)-incidence type I matrix of a difference set `A` in `G`.

    Let `A` be a difference set in a group `G` of order `n`. Return `n\\times n`
    matrix `M` with `M_{ij}=1` if `A_i A_j^{-1} \\in A`, and `M_{ij}=-1` otherwise.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import szekeres_difference_set_pair
        sage: from sage.combinat.matrices.hadamard_matrix import typeI_matrix_difference_set
        sage: G,A,B=szekeres_difference_set_pair(2)
        sage: typeI_matrix_difference_set(G,A)
        [-1  1 -1 -1  1]
        [-1 -1 -1  1  1]
        [ 1  1 -1 -1 -1]
        [ 1 -1  1 -1 -1]
        [-1 -1  1  1 -1]
    """
def rshcd_from_prime_power_and_conference_matrix(n):
    """
    Return a `((n-1)^2,1)`-RSHCD if `n` is prime power, and symmetric `(n-1)`-conference matrix exists.

    The construction implemented here is Theorem 16 (and Corollary 17) from [WW1972]_.

    In [SWW1972]_ this construction (Theorem 5.15 and Corollary 5.16)
    is reproduced with a typo. Note that [WW1972]_ refers to [Sz1969]_ for the construction,
    provided by :func:`szekeres_difference_set_pair`,
    of complementary difference sets, and the latter has a typo.

    From a :func:`symmetric_conference_matrix`, we only need the Seidel
    adjacency matrix of the underlying strongly regular conference (i.e. Paley
    type) graph, which we construct directly.

    INPUT:

    - ``n`` -- integer

    .. SEEALSO::

        :func:`regular_symmetric_hadamard_matrix_with_constant_diagonal`

    EXAMPLES:

    A 36x36 example ::

        sage: from sage.combinat.matrices.hadamard_matrix import rshcd_from_prime_power_and_conference_matrix
        sage: from sage.combinat.matrices.hadamard_matrix import is_hadamard_matrix
        sage: H = rshcd_from_prime_power_and_conference_matrix(7); H
        36 x 36 dense matrix over Integer Ring (use the '.str()' method to see the entries)
        sage: H == H.T and is_hadamard_matrix(H) and H.diagonal() == [1]*36 and list(sum(H)) == [6]*36
        True

    Bigger examples, only provided by this construction ::

        sage: H = rshcd_from_prime_power_and_conference_matrix(27)  # long time
        sage: H == H.T and is_hadamard_matrix(H)                    # long time
        True
        sage: H.diagonal() == [1]*676 and list(sum(H)) == [26]*676  # long time
        True

    In this example the conference matrix is not Paley, as 45 is not a prime power ::

        sage: H = rshcd_from_prime_power_and_conference_matrix(47)  # not tested (long time)

    REFERENCE:

    - [WW1972]_
    """
def are_amicable_hadamard_matrices(M, N, verbose: bool = False):
    """
    Check if ``M`` and ``N`` are amicable Hadamard matrices.

    Two matrices `M` and `N` of order `n` are called amicable if they
    satisfy the following conditions (see [Seb2017]_):

    * `M` is a skew Hadamard matrix
    * `N` is a symmetric Hadamard matrix
    * `MN^T = NM^T`

    INPUT:

    - ``M`` -- a square matrix
    - ``N`` -- a square matrix
    - ``verbose`` -- boolean (default: ``False``); whether to be verbose when the
      matrices are not amicable Hadamard matrices

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import are_amicable_hadamard_matrices
        sage: M = matrix([[1, 1], [-1, 1]])
        sage: N = matrix([[1, 1], [1, -1]])
        sage: are_amicable_hadamard_matrices(M, N)
        True

    If ``verbose`` is true, the function will be verbose when returning False::

        sage: N = matrix([[1, 1], [1, 1]])
        sage: are_amicable_hadamard_matrices(M, N, verbose=True)
        The second matrix is not Hadamard
        False

    TESTS::

        sage: N = matrix.hadamard(12)
        sage: are_amicable_hadamard_matrices(M, N)
        False
    """
def amicable_hadamard_matrices_wallis(n, check: bool = True):
    """
    Construct amicable Hadamard matrices of order `n = q + 1` where `q` is a prime power.

    If `q` is a prime power `\\equiv 3 \\mod 4`, then amicable Hadamard matrices
    of order `q+1` can be constructed as described in [Wal1970b]_.

    INPUT:

    - ``n`` -- integer; the order of the matrices to be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the
      resulting matrices are amicable Hadamard before returning them

    OUTPUT:

    The function returns two amicable Hadamard matrices, or raises an error if such
    matrices cannot be created using this construction.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import amicable_hadamard_matrices_wallis
        sage: M, N = amicable_hadamard_matrices_wallis(28)

    TESTS::

        sage: from sage.combinat.matrices.hadamard_matrix import are_amicable_hadamard_matrices
        sage: M, N = amicable_hadamard_matrices_wallis(20, check=False)
        sage: are_amicable_hadamard_matrices(M, N)
        True
        sage: amicable_hadamard_matrices_wallis(18)
        Traceback (most recent call last):
        ...
        ValueError: n must be a positive multiple of 4
        sage: amicable_hadamard_matrices_wallis(16)
        Traceback (most recent call last):
        ...
        ValueError: q = n-1 must be a prime power
    """
def amicable_hadamard_matrices(n, existence: bool = False, check: bool = True):
    """
    Construct amicable Hadamard matrices of order ``n`` using the available methods.

    INPUT:

    - ``n`` -- positive integer; the order of the amicable Hadamard matrices
    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether amicable Hadamard matrices of order `n` can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the
      matrices are amicable Hadamard matrices before returning them

    OUTPUT:

    If ``existence`` is true, the function returns a boolean representing whether
    amicable Hadamard matrices of order `n` can be constructed.
    If ``existence`` is false, returns two amicable Hadamard matrices, or raises
    an error if the matrices cannot be constructed.

    EXAMPLES::

        sage: from sage.combinat.matrices.hadamard_matrix import amicable_hadamard_matrices
        sage: amicable_hadamard_matrices(2)
        (
        [ 1  1]  [ 1  1]
        [-1  1], [ 1 -1]
        )

    If ``existence`` is true, the function returns a boolean::

        sage: amicable_hadamard_matrices(16, existence=True)
        False

    TESTS::

        sage: M, N = amicable_hadamard_matrices(20)
        sage: amicable_hadamard_matrices(18)
        Traceback (most recent call last):
        ...
        ValueError: Hadamard matrices of order 18 do not exist
        sage: amicable_hadamard_matrices(16)
        Traceback (most recent call last):
        ...
        NotImplementedError: construction for amicable Hadamard matrices of order 16 not yet implemented
    """
