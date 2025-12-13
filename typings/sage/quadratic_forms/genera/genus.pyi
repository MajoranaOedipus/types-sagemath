from _typeshed import Incomplete
from sage.arith.misc import fundamental_discriminant as fundamental_discriminant
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.verbose import verbose as verbose
from sage.quadratic_forms.special_values import quadratic_L_function__exact as quadratic_L_function__exact
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def genera(sig_pair, determinant, max_scale=None, even: bool = False):
    """
    Return a list of all global genera with the given conditions.

    Here a genus is called global if it is non-empty.

    INPUT:

    - ``sig_pair`` -- a pair of nonnegative integers giving the signature

    - ``determinant`` -- integer; the sign is ignored

    - ``max_scale`` -- (default: ``None``) an integer; the maximum scale of a
      jordan block

    - ``even`` -- boolean (default: ``False``)

    OUTPUT:

    A list of all (non-empty) global genera with the given conditions.

    EXAMPLES::

        sage: QuadraticForm.genera((4,0), 125, even=True)
        [Genus of
        None
        Signature:  (4, 0)
        Genus symbol at 2:    1^-4
        Genus symbol at 5:     1^1 5^3, Genus of
        None
        Signature:  (4, 0)
        Genus symbol at 2:    1^-4
        Genus symbol at 5:     1^-2 5^1 25^-1, Genus of
        None
        Signature:  (4, 0)
        Genus symbol at 2:    1^-4
        Genus symbol at 5:     1^2 5^1 25^1, Genus of
        None
        Signature:  (4, 0)
        Genus symbol at 2:    1^-4
        Genus symbol at 5:     1^3 125^1]
    """

genera: Incomplete

def Genus(A, factored_determinant=None):
    """
    Given a nonsingular symmetric matrix `A`, return the genus of `A`.

    INPUT:

    - ``A`` -- a symmetric matrix with integer coefficients

    - ``factored_determinant`` -- (default: ``None``) a :class:`Factorization` object,
      the factored determinant of ``A``

    OUTPUT:

    A :class:`GenusSymbol_global_ring` object, encoding the Conway-Sloane
    genus symbol of the quadratic form whose Gram matrix is `A`.

    EXAMPLES::

        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
        sage: Genus(A)
        Genus of
        [1 1]
        [1 2]
        Signature:  (2, 0)
        Genus symbol at 2:    [1^2]_2

        sage: A = Matrix(ZZ, 2, 2, [2, 1, 1, 2])
        sage: Genus(A, A.det().factor())
        Genus of
        [2 1]
        [1 2]
        Signature:  (2, 0)
        Genus symbol at 2:    1^-2
        Genus symbol at 3:     1^-1 3^-1
    """
def LocalGenusSymbol(A, p):
    """
    Return the local symbol of `A` at the prime `p`.

    INPUT:

    - ``A`` -- a symmetric, non-singular matrix with coefficients in `\\ZZ`
    - ``p`` -- a prime number

    OUTPUT:

    A :class:`Genus_Symbol_p_adic_ring` object, encoding the Conway-Sloane
    genus symbol at `p` of the quadratic form whose Gram matrix is `A`.

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
        sage: LocalGenusSymbol(A, 2)
        Genus symbol at 2:    [1^2]_2
        sage: LocalGenusSymbol(A, 3)
        Genus symbol at 3:     1^2

        sage: A = Matrix(ZZ, 2, 2, [1, 0, 0, 2])
        sage: LocalGenusSymbol(A, 2)
        Genus symbol at 2:    [1^1 2^1]_2
        sage: LocalGenusSymbol(A, 3)
        Genus symbol at 3:     1^-2
    """
def is_GlobalGenus(G) -> bool:
    """
    Return if `G` represents the genus of a global quadratic form or lattice.

    INPUT:

    - ``G`` -- :class:`GenusSymbol_global_ring` object

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import is_GlobalGenus
        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
        sage: G = Genus(A)
        sage: is_GlobalGenus(G)
        True
        sage: G = Genus(matrix.diagonal([2, 2, 2, 2]))
        sage: G._local_symbols[0]._symbol = [[0,2,3,0,0], [1,2,5,1,0]]
        sage: G._representative=None
        sage: is_GlobalGenus(G)
        False
    """
def is_2_adic_genus(genus_symbol_quintuple_list) -> bool:
    """
    Given a `2`-adic local symbol (as the underlying list of quintuples)
    check whether it is the `2`-adic symbol of a `2`-adic form.

    INPUT:

    - ``genus_symbol_quintuple_list`` -- a quintuple of integers (with certain
      restrictions)

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol, is_2_adic_genus

        sage: A = Matrix(ZZ, 2, 2, [1,1,1,2])
        sage: G2 = LocalGenusSymbol(A, 2)
        sage: is_2_adic_genus(G2.symbol_tuple_list())
        True

        sage: A = Matrix(ZZ, 2, 2, [1,1,1,2])
        sage: G3 = LocalGenusSymbol(A, 3)
        sage: is_2_adic_genus(G3.symbol_tuple_list())  # This raises an error
        Traceback (most recent call last):
        ...
        TypeError: The genus symbols are not quintuples,
        so it's not a genus symbol for the prime p=2.

        sage: A = Matrix(ZZ, 2, 2, [1,0,0,2])
        sage: G2 = LocalGenusSymbol(A, 2)
        sage: is_2_adic_genus(G2.symbol_tuple_list())
        True
    """
def canonical_2_adic_compartments(genus_symbol_quintuple_list):
    """
    Given a `2`-adic local symbol (as the underlying list of quintuples)
    this returns a list of lists of indices of the
    ``genus_symbol_quintuple_list`` which are in the same compartment.  A
    compartment is defined to be a maximal interval of Jordan
    components all (scaled) of type I (i.e. odd).

    INPUT:

    - ``genus_symbol_quintuple_list`` -- a quintuple of integers (with certain
      restrictions)

    OUTPUT: list of lists of integers

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        sage: from sage.quadratic_forms.genera.genus import canonical_2_adic_compartments

        sage: A = Matrix(ZZ, 2, 2, [1,1,1,2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 2, 1, 1, 2]]
        sage: canonical_2_adic_compartments(G2.symbol_tuple_list())
        [[0]]

        sage: A = Matrix(ZZ, 2, 2, [1,0,0,2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        sage: canonical_2_adic_compartments(G2.symbol_tuple_list())
        [[0, 1]]

        sage: A = DiagonalQuadraticForm(ZZ, [1,2,3,4]).Hessian_matrix()
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]
        sage: canonical_2_adic_compartments(G2.symbol_tuple_list())
        [[0, 1, 2]]

        sage: A = Matrix(ZZ, 2, 2, [2,1,1,2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 2, 3, 0, 0]]
        sage: canonical_2_adic_compartments(G2.symbol_tuple_list())   # No compartments here!
        []

    .. NOTE::

        See [CS1999]_ Conway-Sloane 3rd edition, pp. 381-382 for definitions
        and examples.
    """
def canonical_2_adic_trains(genus_symbol_quintuple_list, compartments=None):
    """
    Given a `2`-adic local symbol (as the underlying list of quintuples)
    this returns a list of lists of indices of the
    ``genus_symbol_quintuple_list`` which are in the same train.  A train
    is defined to be a maximal interval of Jordan components so that
    at least one of each adjacent pair (allowing zero-dimensional
    Jordan components) is (scaled) of type I (i.e. odd).
    Note that an interval of length one respects this condition as
    there is no pair in this interval.
    In particular, every Jordan component is part of a train.

    INPUT:

    - ``genus_symbol_quintuple_list`` -- a quintuple of integers (with certain
      restrictions).
    - ``compartments`` -- this argument is deprecated

    OUTPUT: list of lists of distinct integers

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        sage: from sage.quadratic_forms.genera.genus import canonical_2_adic_compartments
        sage: from sage.quadratic_forms.genera.genus import canonical_2_adic_trains

        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 2, 1, 1, 2]]
        sage: canonical_2_adic_trains(G2.symbol_tuple_list())
        [[0]]

        sage: A = Matrix(ZZ, 2, 2, [1,0,0,2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        sage: canonical_2_adic_compartments(G2.symbol_tuple_list())
        [[0, 1]]

        sage: A = DiagonalQuadraticForm(ZZ, [1,2,3,4]).Hessian_matrix()
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]
        sage: canonical_2_adic_trains(G2.symbol_tuple_list())
        [[0, 1, 2]]

        sage: A = Matrix(ZZ, 2, 2, [2, 1, 1, 2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 2, 3, 0, 0]]
        sage: canonical_2_adic_trains(G2.symbol_tuple_list())
        [[0]]
        sage: symbol = [[0, 1,  1, 1, 1], [1, 2, -1, 0, 0], [2, 1,  1, 1, 1],
        ....:           [3, 1,  1, 1, 1], [4, 1,  1, 1, 1], [5, 2, -1, 0, 0],
        ....:           [7, 1,  1, 1, 1], [10, 1, 1, 1, 1], [11, 1, 1, 1, 1], [12, 1, 1, 1, 1]]
        sage: canonical_2_adic_trains(symbol)
        [[0, 1, 2, 3, 4, 5], [6], [7, 8, 9]]

    Check that :issue:`24818` is fixed::

        sage: symbol = [[0, 1,  1, 1, 1], [1, 3, 1, 1, 1]]
        sage: canonical_2_adic_trains(symbol)
        [[0, 1]]

    .. NOTE::

        See [CS1999]_, pp. 381-382 for definitions and examples.
    """
def canonical_2_adic_reduction(genus_symbol_quintuple_list):
    '''
    Given a `2`-adic local symbol (as the underlying list of quintuples)
    this returns a canonical `2`-adic symbol (again as a raw list of
    quintuples of integers) which has at most one minus sign per train
    and this sign appears on the smallest dimensional Jordan component
    in each train.  This results from applying the "sign-walking" and
    "oddity fusion" equivalences.

    INPUT:

    - ``genus_symbol_quintuple_list`` -- a quintuple of integers (with certain
      restrictions)

    - ``compartments`` -- list of lists of distinct integers (optional)

    OUTPUT: list of lists of distinct integers

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        sage: from sage.quadratic_forms.genera.genus import canonical_2_adic_reduction

        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 2, 1, 1, 2]]
        sage: canonical_2_adic_reduction(G2.symbol_tuple_list())
        [[0, 2, 1, 1, 2]]

        sage: A = Matrix(ZZ, 2, 2, [1, 0, 0, 2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        sage: canonical_2_adic_reduction(G2.symbol_tuple_list())   # Oddity fusion occurred here!
        [[0, 1, 1, 1, 2], [1, 1, 1, 1, 0]]

        sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]
        sage: canonical_2_adic_reduction(G2.symbol_tuple_list())   # Oddity fusion occurred here!
        [[1, 2, -1, 1, 6], [2, 1, 1, 1, 0], [3, 1, 1, 1, 0]]

        sage: A = Matrix(ZZ, 2, 2, [2, 1, 1, 2])
        sage: G2 = LocalGenusSymbol(A, 2); G2.symbol_tuple_list()
        [[0, 2, 3, 0, 0]]
        sage: canonical_2_adic_reduction(G2.symbol_tuple_list())
        [[0, 2, -1, 0, 0]]

    .. NOTE::

        See [CS1999]_ Conway-Sloane 3rd edition, pp. 381-382 for definitions
        and examples.

    .. TODO::

        Add an example where sign walking occurs!
    '''
def basis_complement(B):
    """
    Given an echelonized basis matrix `B` (over a field), calculate a
    matrix whose rows form a basis complement (to the rows of `B`).

    INPUT:

    - ``B`` -- matrix over a field in row echelon form

    OUTPUT: a rectangular matrix over a field

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import basis_complement

        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 1])
        sage: B = A.kernel().echelonized_basis_matrix(); B
        [ 1 -1]
        sage: basis_complement(B)
        [0 1]
    """
def signature_pair_of_matrix(A):
    """
    Compute the signature pair `(p, n)` of a non-degenerate symmetric
    matrix, where

    - `p` is the number of positive eigenvalues of `A`
    - `n` is the number of negative eigenvalues of `A`

    INPUT:

    - ``A`` -- symmetric matrix (assumed to be non-degenerate)

    OUTPUT: `(p, n)` -- a pair (tuple) of integers.

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import signature_pair_of_matrix

        sage: A = Matrix(ZZ, 2, 2, [-1, 0, 0, 3])
        sage: signature_pair_of_matrix(A)
        (1, 1)

        sage: A = Matrix(ZZ, 2, 2, [-1, 1, 1, 7])
        sage: signature_pair_of_matrix(A)
        (1, 1)

        sage: A = Matrix(ZZ, 2, 2, [3, 1, 1, 7])
        sage: signature_pair_of_matrix(A)
        (2, 0)

        sage: A = Matrix(ZZ, 2, 2, [-3, 1, 1, -11])
        sage: signature_pair_of_matrix(A)
        (0, 2)


        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 1])
        sage: signature_pair_of_matrix(A)
        Traceback (most recent call last):
        ...
        ArithmeticError: given matrix is not invertible
    """
def p_adic_symbol(A, p, val):
    """
    Given a symmetric matrix `A` and prime `p`, return the genus symbol at `p`.

    .. TODO::

        Some description of the definition of the genus symbol.

    INPUT:

    - ``A`` -- symmetric matrix with integer coefficients
    - ``p`` -- prime number
    - ``val`` -- nonnegative integer; valuation of the maximal elementary
      divisor of `A` needed to obtain enough precision.
      Calculation is modulo `p` to the ``val+3``.

    OUTPUT: list of lists of integers

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import p_adic_symbol

        sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
        sage: p_adic_symbol(A, 2, 2)
        [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]

        sage: p_adic_symbol(A, 3, 1)
        [[0, 3, 1], [1, 1, -1]]
    """
def is_even_matrix(A) -> tuple[bool, int]:
    """
    Determine if the integral symmetric matrix `A` is even
    (i.e. represents only even numbers).  If not, then it returns the
    index of an odd diagonal entry.  If it is even, then we return the
    index `-1`.

    INPUT:

    - ``A`` -- symmetric integer matrix

    OUTPUT: a pair of the form (boolean, integer)

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import is_even_matrix

        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 1])
        sage: is_even_matrix(A)
        (False, 0)

        sage: A = Matrix(ZZ, 2, 2, [2, 1, 1, 2])
        sage: is_even_matrix(A)
        (True, -1)
    """
def split_odd(A):
    """
    Given a non-degenerate Gram matrix `A (\\mod 8)`, return a splitting
    ``[u] + B`` such that u is odd and `B` is not even.

    INPUT:

    - ``A`` -- an odd symmetric matrix with integer coefficients (which admits a
      splitting as above)

    OUTPUT:

    a pair ``(u, B)`` consisting of an odd integer `u` and an odd
    integral symmetric matrix `B`.

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import is_even_matrix
        sage: from sage.quadratic_forms.genera.genus import split_odd

        sage: A = Matrix(ZZ, 2, 2, [1, 2, 2, 3])
        sage: is_even_matrix(A)
        (False, 0)
        sage: split_odd(A)
        (1, [-1])

        sage: A = Matrix(ZZ, 2, 2, [1, 2, 2, 5])
        sage: split_odd(A)
        (1, [1])

        sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 1])
        sage: is_even_matrix(A)
        (False, 0)
        sage: split_odd(A)      # This fails because no such splitting exists. =(
        Traceback (most recent call last):
        ...
        RuntimeError: The matrix A does not admit a non-even splitting.

        sage: A = Matrix(ZZ, 2, 2, [1, 2, 2, 6])
        sage: split_odd(A)      # This fails because no such splitting exists. =(
        Traceback (most recent call last):
        ...
        RuntimeError: The matrix A does not admit a non-even splitting.
    """
def trace_diag_mod_8(A):
    """
    Return the trace of the diagonalised form of `A` of an integral
    symmetric matrix which is diagonalizable mod `8`.  (Note that since
    the Jordan decomposition into blocks of size `\\leq 2` is not unique
    here, this is not the same as saying that `A` is always diagonal in
    any `2`-adic Jordan decomposition!)

    INPUT:

    - ``A`` -- symmetric matrix with coefficients in `\\ZZ` which is odd in
      `\\ZZ/2\\ZZ` and has determinant not divisible by `8`

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import is_even_matrix
        sage: from sage.quadratic_forms.genera.genus import split_odd
        sage: from sage.quadratic_forms.genera.genus import trace_diag_mod_8

        sage: A = Matrix(ZZ, 2, 2, [1, 2, 2, 3])
        sage: is_even_matrix(A)
        (False, 0)
        sage: split_odd(A)
        (1, [-1])
        sage: trace_diag_mod_8(A)
        0

        sage: A = Matrix(ZZ, 2, 2, [1, 2, 2, 5])
        sage: split_odd(A)
        (1, [1])
        sage: trace_diag_mod_8(A)
        2
    """
def two_adic_symbol(A, val):
    """
    Given a symmetric matrix `A` and prime `p`, return the genus symbol at `p`.

    The genus symbol of a component `2^m f` is of the form ``(m,n,s,d[,o])``,
    where

    - ``m`` = valuation of the component
    - ``n`` = dimension of `f`
    - ``d`` = det(`f`) in {1,3,5,7}
    - ``s`` = 0 (or 1) if even (or odd)
    - ``o`` = oddity of `f` (= 0 if s = 0) in `\\ZZ/8\\ZZ`

    INPUT:

    - ``A`` -- symmetric matrix with integer coefficients, non-degenerate
    - ``val`` -- nonnegative integer; valuation of maximal `2`-elementary divisor

    OUTPUT:

    a list of lists of integers (representing a Conway-Sloane `2`-adic symbol)

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import two_adic_symbol

        sage: A = diagonal_matrix(ZZ, [1, 2, 3, 4])
        sage: two_adic_symbol(A, 2)
        [[0, 2, 3, 1, 4], [1, 1, 1, 1, 1], [2, 1, 1, 1, 1]]
    """

class Genus_Symbol_p_adic_ring:
    """
    Local genus symbol over a `p`-adic ring.

    The genus symbol of a component `p^m A` for odd prime `= p` is of the
    form `(m,n,d)`, where

    - `m` = valuation of the component
    - `n` = rank of `A`
    - `d = det(A) \\in \\{1,u\\}` for a normalized quadratic non-residue `u`.

    The genus symbol of a component `2^m A` is of the form `(m, n, s, d, o)`,
    where

    - `m` = valuation of the component
    - `n` = rank of `A`
    - `d` = det(A) in `\\{1,3,5,7\\}`
    - `s` = 0 (or 1) if even (or odd)
    - `o` = oddity of `A` (= 0 if s = 0) in `Z/8Z` = the trace of the diagonalization of `A`

    The genus symbol is a list of such symbols (ordered by `m`) for each
    of the Jordan blocks `A_1,...,A_t`.

    REFERENCE:

    [CS1999]_ Conway and Sloane 3rd edition, Chapter 15, Section 7.


    .. WARNING::

        This normalization seems non-standard, and we
        should review this entire class to make sure that we have our
        doubling conventions straight throughout!  This is especially
        noticeable in the determinant and excess methods!!

    INPUT:

    - ``prime`` -- a prime number
    - ``symbol`` -- the list of invariants for Jordan blocks `A_t,...,A_t` given
      as a list of lists of integers

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
        sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

        sage: A = diagonal_matrix(ZZ, [1, 2, 3, 4])
        sage: p = 2
        sage: s2 = p_adic_symbol(A, p, 2); s2
        [[0, 2, 3, 1, 4], [1, 1, 1, 1, 1], [2, 1, 1, 1, 1]]
        sage: G2 = Genus_Symbol_p_adic_ring(p,s2); G2
        Genus symbol at 2:    [1^-2 2^1 4^1]_6

        sage: A = diagonal_matrix(ZZ, [1, 2, 3, 4])
        sage: p = 3
        sage: s3 = p_adic_symbol(A, p, 1); s3
        [[0, 3, -1], [1, 1, 1]]
        sage: G3 = Genus_Symbol_p_adic_ring(p,s3); G3
        Genus symbol at 3:     1^-3 3^1
    """
    def __init__(self, prime, symbol, check: bool = True) -> None:
        """
        Create the local genus symbol of given prime and local invariants.

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring
            sage: A = diagonal_matrix(ZZ, [1,2,3,4])
            sage: p = 2
            sage: s2 = p_adic_symbol(A, p, 2); s2
            [[0, 2, 3, 1, 4], [1, 1, 1, 1, 1], [2, 1, 1, 1, 1]]
            sage: G2 = Genus_Symbol_p_adic_ring(p,s2);G2
            Genus symbol at 2:    [1^-2 2^1 4^1]_6

            sage: A = diagonal_matrix(ZZ, [1,2,3,4])
            sage: p = 3
            sage: s3 = p_adic_symbol(A, p, 1); s3
            [[0, 3, -1], [1, 1, 1]]
            sage: G3 = Genus_Symbol_p_adic_ring(p,s3);G3
            Genus symbol at 3:     1^-3 3^1
            sage: G2 == loads(dumps(G2))
            True
            sage: G3 == loads(dumps(G3))
            True
        """
    def __eq__(self, other):
        """
        Determines if two genus symbols are equal (not just equivalent!).

        INPUT:

        - ``other`` -- a :class:`Genus_Symbol_p_adic_ring` object

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = diagonal_matrix(ZZ, [1, 2, 3, 4])
            sage: p = 2
            sage: G2 =  Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2))
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 1))

            sage: G2 == G3
            False
            sage: G3 == G2
            False
            sage: G2 == G2
            True
            sage: G3 == G3
            True
        """
    def __ne__(self, other):
        """
        Determines if two genus symbols are unequal (not just inequivalent!).

        INPUT:

        - ``other`` -- a :class:`Genus_Symbol_p_adic_ring` object

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = diagonal_matrix(ZZ, [1, 2, 3, 4])
            sage: p = 2
            sage: G2 =  Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2))
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 1))

            sage: G2 != G3
            True
            sage: G3 != G2
            True
            sage: G2 != G2
            False
            sage: G3 != G3
            False
        """
    def automorphous_numbers(self):
        """
        Return generators of the automorphous square classes at this prime.

        A `p`-adic square class `r` is called automorphous if it is
        the spinor norm of a proper `p`-adic integral automorphism of this form.
        These classes form a group. See [CS1999]_ Chapter 15, 9.6 for details.

        OUTPUT:

        a list of integers representing the square classes of generators of
        the automorphous numbers

        EXAMPLES:

        The following examples are given in
        [CS1999]_ 3rd edition, Chapter 15, 9.6 pp. 392::

            sage: A = matrix.diagonal([3, 16])
            sage: G = Genus(A)
            sage: sym2 = G.local_symbols()[0]; sym2
            Genus symbol at 2:    [1^-1]_3:[16^1]_1
            sage: sym2.automorphous_numbers()
            [3, 5]

            sage: A = matrix(ZZ, 3, [2,1,0, 1,2,0, 0,0,18])
            sage: G = Genus(A)
            sage: sym = G.local_symbols()
            sage: sym[0]
            Genus symbol at 2:    1^-2 [2^1]_1
            sage: sym[0].automorphous_numbers()
            [1, 3, 5, 7]
            sage: sym[1]
            Genus symbol at 3:     1^-1 3^-1 9^-1
            sage: sym[1].automorphous_numbers()
            [1, 3]

        Note that the generating set given is not minimal.
        The first supplementation rule is used here::

            sage: A = matrix.diagonal([2, 2, 4])
            sage: G = Genus(A)
            sage: sym = G.local_symbols()
            sage: sym[0]
            Genus symbol at 2:    [2^2 4^1]_3
            sage: sym[0].automorphous_numbers()
            [1, 2, 3, 5, 7]

        but not there::

            sage: A = matrix.diagonal([2, 2, 32])
            sage: G = Genus(A)
            sage: sym = G.local_symbols()
            sage: sym[0]
            Genus symbol at 2:    [2^2]_2:[32^1]_1
            sage: sym[0].automorphous_numbers()
            [1, 2, 5]

        Here the second supplementation rule is used::

            sage: A = matrix.diagonal([2, 2, 64])
            sage: G = Genus(A)
            sage: sym = G.local_symbols()
            sage: sym[0]
            Genus symbol at 2:    [2^2]_2:[64^1]_1
            sage: sym[0].automorphous_numbers()
            [1, 2, 5]
        """
    def canonical_symbol(self):
        """
        Return (and cache) the canonical `p`-adic genus symbol.  This is
        only really affects the `2`-adic symbol, since when `p > 2` the
        symbol is already canonical.

        OUTPUT: list of lists of integers

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2.symbol_tuple_list()
            [[0, 2, 1, 1, 2]]
            sage: G2.canonical_symbol()
            [[0, 2, 1, 1, 2]]

            sage: A = Matrix(ZZ, 2, 2, [1, 0, 0, 2])
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2.symbol_tuple_list()
            [[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
            sage: G2.canonical_symbol()   # Oddity fusion occurred here!
            [[0, 1, 1, 1, 2], [1, 1, 1, 1, 0]]

            sage: A = DiagonalQuadraticForm(ZZ, [1,2,3,4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2.symbol_tuple_list()
            [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]
            sage: G2.canonical_symbol()   # Oddity fusion occurred here!
            [[1, 2, -1, 1, 6], [2, 1, 1, 1, 0], [3, 1, 1, 1, 0]]

            sage: A = Matrix(ZZ, 2, 2, [2, 1, 1, 2])
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2.symbol_tuple_list()
            [[0, 2, 3, 0, 0]]
            sage: G2.canonical_symbol()
            [[0, 2, -1, 0, 0]]


            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G3.symbol_tuple_list()
            [[0, 3, 1], [1, 1, -1]]
            sage: G3.canonical_symbol()
            [[0, 3, 1], [1, 1, -1]]

        .. NOTE::

            See [CS1999]_ Conway-Sloane 3rd edition, pp. 381-382 for definitions
            and examples.

        .. TODO::

            Add an example where sign walking occurs!
        """
    def gram_matrix(self, check: bool = True):
        """
        Return a Gram matrix of a representative of this local genus.

        INPUT:

        - ``check`` -- boolean (default: ``True``); double check the result

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring
            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2))
            sage: G2.gram_matrix()
            [2 0|0|0]
            [0 6|0|0]
            [---+-+-]
            [0 0|4|0]
            [---+-+-]
            [0 0|0|8]
        """
    def mass(self):
        """
        Return the local mass `m_p` of this genus as defined by Conway.

        See Equation (3) in [CS1988]_.

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([1, 3, 9]))
            sage: G.local_symbol(3).mass()
            9/8

        TESTS::

            sage: G = Genus(matrix([1]))
            sage: G.local_symbol(2).mass()
            Traceback (most recent call last):
            ....
            ValueError: the dimension must be at least 2
        """
    def prime(self):
        """
        Return the prime number `p` of this `p`-adic local symbol.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol
            sage: M1 = matrix(ZZ, [2])
            sage: p = 2
            sage: G0 = LocalGenusSymbol(M1, 2)
            sage: G0.prime()
            2
        """
    def is_even(self) -> bool:
        """
        Return if the underlying `p`-adic lattice is even.

        If `p` is odd, every lattice is even.

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import LocalGenusSymbol
            sage: M0 = matrix(ZZ, [1])
            sage: G0 = LocalGenusSymbol(M0, 2)
            sage: G0.is_even()
            False
            sage: G1 = LocalGenusSymbol(M0, 3)
            sage: G1.is_even()
            True
            sage: M2 = matrix(ZZ, [2])
            sage: G2 = LocalGenusSymbol(M2, 2)
            sage: G2.is_even()
            True
        """
    def symbol_tuple_list(self):
        """
        Return a copy of the underlying list of lists of integers
        defining the genus symbol.

        OUTPUT: list of lists of integers

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G3
            Genus symbol at 3:     1^3 3^-1
            sage: G3.symbol_tuple_list()
            [[0, 3, 1], [1, 1, -1]]
            sage: type(G3.symbol_tuple_list())
            <... 'list'>

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2
            Genus symbol at 2:    [2^-2 4^1 8^1]_6
            sage: G2.symbol_tuple_list()
            [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]
            sage: type(G2.symbol_tuple_list())
            <... 'list'>
        """
    def number_of_blocks(self):
        """
        Return the number of positive dimensional symbols/Jordan blocks.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2))
            sage: G2.symbol_tuple_list()
            [[1, 2, 3, 1, 4], [2, 1, 1, 1, 1], [3, 1, 1, 1, 1]]
            sage: G2.number_of_blocks()
            3

            sage: A = DiagonalQuadraticForm(ZZ, [1,2,3,4]).Hessian_matrix()
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2))
            sage: G3.symbol_tuple_list()
            [[0, 3, 1], [1, 1, -1]]
            sage: G3.number_of_blocks()
            2
        """
    def determinant(self):
        """
        Return the (`p`-part of the) determinant (square-class) of the
        Hessian matrix of the quadratic form (given by regarding the
        integral symmetric matrix which generated this genus symbol as
        the Gram matrix of `Q`) associated to this local genus symbol.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2
            Genus symbol at 2:    [2^-2 4^1 8^1]_6
            sage: G2.determinant()
            128

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G3
            Genus symbol at 3:     1^3 3^-1
            sage: G3.determinant()
            3
        """
    det = determinant
    def dimension(self):
        """
        Return the dimension of a quadratic form associated to this genus symbol.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2
            Genus symbol at 2:    [2^-2 4^1 8^1]_6
            sage: G2.dimension()
            4

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 3
            sage: G3 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G3
            Genus symbol at 3:     1^3 3^-1
            sage: G3.dimension()
            4
        """
    dim = dimension
    rank = dimension
    def direct_sum(self, other):
        """
        Return the local genus of the direct sum of two representatives.

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring
            sage: A = matrix.diagonal([1, 2, 3, 4])
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2
            Genus symbol at 2:    [1^-2 2^1 4^1]_6
            sage: G2.direct_sum(G2)
            Genus symbol at 2:    [1^4 2^2 4^2]_4

        TESTS::

            sage: G = Genus(matrix([6]))
            sage: G2 = G.local_symbol(2)
            sage: G3 = G.local_symbol(3)
            sage: G2.direct_sum(G3)
            Traceback (most recent call last):
            ...
            ValueError: the local genus symbols must be over the same prime
        """
    def excess(self):
        """
        Return the `p`-excess of the quadratic form whose Hessian
        matrix is the symmetric matrix `A`.  When `p = 2`, the `p`-excess is
        called the oddity.

        .. WARNING::

            This normalization seems non-standard, and we
            should review this entire class to make sure that we have our
            doubling conventions straight throughout!

        REFERENCE:

        [CS1999]_ Conway and Sloane Book, 3rd edition, pp 370-371.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: AC = diagonal_matrix(ZZ, [1, 3, -3])
            sage: p=2; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            1
            sage: p=3; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0
            sage: p=5; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0
            sage: p=7; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0
            sage: p=11; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0

            sage: AC = 2 * diagonal_matrix(ZZ, [1, 3, -3])
            sage: p=2; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            1
            sage: p=3; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0
            sage: p=5; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0
            sage: p=7; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0
            sage: p=11; Genus_Symbol_p_adic_ring(p, p_adic_symbol(AC, p, 2)).excess()
            0

            sage: A = 2*diagonal_matrix(ZZ, [1, 2, 3, 4])
            sage: p = 2; Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)).excess()
            2
            sage: p = 3; Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)).excess()
            6
            sage: p = 5; Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)).excess()
            0
            sage: p = 7; Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)).excess()
            0
            sage: p = 11; Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)).excess()
            0
        """
    def scale(self):
        """
        Return the scale of this local genus.

        Let `L` be a lattice with bilinear form `b`.
        The scale of `(L,b)` is defined as the ideal
        `b(L,L)`.

        OUTPUT: integer

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([2, 4, 18]))
            sage: G.local_symbol(2).scale()
            2
            sage: G.local_symbol(3).scale()
            1
        """
    def norm(self):
        """
        Return the norm of this local genus.

        Let `L` be a lattice with bilinear form `b`.
        The norm of `(L,b)` is defined as the ideal
        generated by `\\{b(x,x) | x \\in L\\}`.

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([2, 4, 18]))
            sage: G.local_symbol(2).norm()
            2
            sage: G = Genus(matrix(ZZ,2,[0, 1, 1, 0]))
            sage: G.local_symbol(2).norm()
            2
        """
    def level(self):
        """
        Return the maximal scale of a Jordan component.

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([2, 4, 18]))
            sage: G.local_symbol(2).level()
            4
        """
    def trains(self) -> list:
        """
        Compute the indices for each of the trains in this local genus
        symbol if it is associated to the prime `p=2` (and raise an
        error for all other primes).

        OUTPUT: list of nonnegative integers

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2
            Genus symbol at 2:    [2^-2 4^1 8^1]_6
            sage: G2.trains()
            [[0, 1, 2]]
        """
    def compartments(self) -> list:
        """
        Compute the indices for each of the compartments in this local genus
        symbol if it is associated to the prime `p=2` (and raise an
        error for all other primes).

        OUTPUT: list of nonnegative integers

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import p_adic_symbol
            sage: from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: p = 2
            sage: G2 = Genus_Symbol_p_adic_ring(p, p_adic_symbol(A, p, 2)); G2
            Genus symbol at 2:    [2^-2 4^1 8^1]_6
            sage: G2.compartments()
            [[0, 1, 2]]
        """

class GenusSymbol_global_ring:
    """
    This represents a collection of local genus symbols (at primes)
    and signature information which represent the genus of a
    non-degenerate integral lattice.

    INPUT:

    - ``signature_pair`` -- tuple of two nonnegative integers

    - ``local_symbols`` -- list of :class:`Genus_Symbol_p_adic_ring` instances
      sorted by their primes

    - ``representative`` -- (default: ``None``) integer symmetric matrix;
      the Gram matrix of a representative of this genus

    - ``check`` -- boolean (default: ``True``); checks the input

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring, LocalGenusSymbol
        sage: A = matrix.diagonal(ZZ, [2, 4, 6, 8])
        sage: local_symbols = [LocalGenusSymbol(A, p) for p in (2*A.det()).prime_divisors()]
        sage: G = GenusSymbol_global_ring((4, 0),local_symbols, representative=A);G
        Genus of
        [2 0 0 0]
        [0 4 0 0]
        [0 0 6 0]
        [0 0 0 8]
        Signature:  (4, 0)
        Genus symbol at 2:    [2^-2 4^1 8^1]_6
        Genus symbol at 3:     1^3 3^-1

    .. SEEALSO::

        :func:`Genus` to create a :class:`GenusSymbol_global_ring` from the Gram matrix directly.
    """
    def __init__(self, signature_pair, local_symbols, representative=None, check: bool = True) -> None:
        """
        Initialize a global genus symbol.

        EXAMPLES::

            sage: A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: G = Genus(A)
            sage: G == loads(dumps(G))
            True
        """
    def __eq__(self, other) -> bool:
        """
        Determines if two global genus symbols are equal (not just equivalent!).

        INPUT:

        - ``other`` -- a :class:`GenusSymbol_global_ring` object

        OUTPUT: boolean

        EXAMPLES::

            sage: A1 = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: GS1 = Genus(A1)
            sage: A2 = DiagonalQuadraticForm(ZZ, [1, 2, 3, 5]).Hessian_matrix()
            sage: GS2 = Genus(A2)

            sage: GS1 == GS2
            False

            sage: GS2 == GS1
            False

            sage: GS1 == GS1
            True

            sage: GS2 == GS2
            True

        TESTS::

            sage: D4 = QuadraticForm(Matrix(ZZ, 4, 4, [2,0,0,-1, 0,2,0,-1, 0,0,2,-1, -1,-1,-1,2]))
            sage: G = D4.global_genus_symbol()
            sage: sage.quadratic_forms.genera.genus.is_GlobalGenus(G)
            True
            sage: G == deepcopy(G)
            True
            sage: sage.quadratic_forms.genera.genus.is_GlobalGenus(G)
            True
        """
    def __ne__(self, other) -> bool:
        """
        Determine if two global genus symbols are unequal (not just inequivalent!).

        INPUT:

        - ``other`` -- a ``GenusSymbol_global_ring`` object

        OUTPUT: boolean

        EXAMPLES::

            sage: A1 = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
            sage: GS1 = Genus(A1)
            sage: A2 = DiagonalQuadraticForm(ZZ, [1, 2, 3, 5]).Hessian_matrix()
            sage: GS2 = Genus(A2)

            sage: GS1 != GS2
            True

            sage: GS2 != GS1
            True

            sage: GS1 != GS1
            False

            sage: GS2 != GS2
            False
        """
    def is_even(self) -> bool:
        """
        Return if this genus is even.

        EXAMPLES::

            sage: G = Genus(Matrix(ZZ,2,[2,1,1,2]))
            sage: G.is_even()
            True
        """
    def signature_pair(self):
        """
        Return the signature pair `(p, n)` of the (non-degenerate)
        global genus symbol, where `p` is the number of positive
        eigenvalues and `n` is the number of negative eigenvalues.

        OUTPUT: a pair of integers `(p, n)`, each `\\geq 0`

        EXAMPLES::

            sage: A = matrix.diagonal(ZZ, [1, -2, 3, 4, 8, -11])
            sage: GS = Genus(A)
            sage: GS.signature_pair()
            (4, 2)
        """
    signature_pair_of_matrix = signature_pair
    def spinor_generators(self, proper) -> list:
        """
        Return the spinor generators.

        INPUT:

        - ``proper`` -- boolean

        OUTPUT: list of primes not dividing the determinant

        EXAMPLES::

            sage: g = matrix(ZZ, 3, [2,1,0, 1,2,0, 0,0,18])
            sage: gen = Genus(g)
            sage: gen.spinor_generators(False)
            [5]
        """
    def signature(self):
        """
        Return the signature of this genus.

        The signature is `p - n` where `p` is the number of positive eigenvalues
        and `n` the number of negative eigenvalues.

        EXAMPLES::

            sage: A = matrix.diagonal(ZZ, [1, -2, 3, 4, 8, -11])
            sage: GS = Genus(A)
            sage: GS.signature()
            2
        """
    def determinant(self):
        """
        Return the determinant of this genus.

        The determinant is the Hessian determinant of the quadratic
        form whose Gram matrix is the Gram matrix giving rise to this
        global genus symbol.

        OUTPUT: integer

        EXAMPLES::

            sage: A = matrix.diagonal(ZZ, [1, -2, 3, 4])
            sage: GS = Genus(A)
            sage: GS.determinant()
            -24
        """
    det = determinant
    def dimension(self):
        """
        Return the dimension of this genus.

        EXAMPLES::

            sage: A = Matrix(ZZ, 2, 2, [1, 1, 1, 2])
            sage: G = Genus(A)
            sage: G.dimension()
            2
        """
    dim = dimension
    rank = dimension
    def direct_sum(self, other):
        '''
        Return the genus of the direct sum of ``self`` and ``other``.

        The direct sum is defined as the direct sum of representatives.

        EXAMPLES::

            sage: G = IntegralLattice("A4").twist(3).genus()
            sage: G.direct_sum(G)
            Genus of
            None
            Signature:  (8, 0)
            Genus symbol at 2:    1^8
            Genus symbol at 3:     3^8
            Genus symbol at 5:     1^6 5^2
        '''
    def discriminant_form(self):
        """
        Return the discriminant form associated to this genus.

        EXAMPLES::

            sage: A = matrix.diagonal(ZZ, [2, -4, 6, 8])
            sage: GS = Genus(A)
            sage: GS.discriminant_form()
            Finite quadratic module over Integer Ring with invariants (2, 2, 4, 24)
            Gram matrix of the quadratic form with values in Q/2Z:
            [  1/2     0   1/2     0]
            [    0   3/2     0     0]
            [  1/2     0   3/4     0]
            [    0     0     0 25/24]
            sage: A = matrix.diagonal(ZZ, [1, -4, 6, 8])
            sage: GS = Genus(A)
            sage: GS.discriminant_form()
            Finite quadratic module over Integer Ring with invariants (2, 4, 24)
            Gram matrix of the quadratic form with values in Q/Z:
            [ 1/2  1/2    0]
            [ 1/2  3/4    0]
            [   0    0 1/24]
        """
    def rational_representative(self):
        """
        Return a representative of the rational
        bilinear form defined by this genus.

        OUTPUT: a diagonal_matrix

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import genera
            sage: G = genera((8,0), 1)[0]
            sage: G
            Genus of
            None
            Signature:  (8, 0)
            Genus symbol at 2:    1^8
            sage: G.rational_representative()
            [1 0 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0]
            [0 0 0 1 0 0 0 0]
            [0 0 0 0 1 0 0 0]
            [0 0 0 0 0 2 0 0]
            [0 0 0 0 0 0 1 0]
            [0 0 0 0 0 0 0 2]
        """
    def representative(self):
        """
        Return a representative in this genus.

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import genera
            sage: g = genera([1,3], 24)[0]
            sage: g
            Genus of
            None
            Signature:  (1, 3)
            Genus symbol at 2:    [1^-1 2^3]_0
            Genus symbol at 3:     1^3 3^1

        A representative of ``g`` is not known yet.
        Let us trigger its computation::

            sage: g.representative()
            [ 0  0  0  2]
            [ 0 -1  0  0]
            [ 0  0 -6  0]
            [ 2  0  0  0]
            sage: g == Genus(g.representative())
            True
        """
    def representatives(self, backend=None, algorithm=None):
        """
        Return a list of representatives for the classes in this genus.

        INPUT:

        - ``backend`` -- (default: ``None``)
        - ``algorithm`` -- (default: ``None``)

        OUTPUT: list of Gram matrices

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import genera
            sage: G = Genus(matrix.diagonal([1, 1, 7]))
            sage: G.representatives()
            (
            [1 0 0]  [1 0 0]
            [0 2 1]  [0 1 0]
            [0 1 4], [0 0 7]
            )

        Indefinite genera work as well::

            sage: G = Genus(matrix(ZZ, 3, [6,3,0, 3,6,0, 0,0,2]))
            sage: G.representatives()
            (
            [2 0 0]  [ 2  1  0]
            [0 6 3]  [ 1  2  0]
            [0 3 6], [ 0  0 18]
            )

        For positive definite forms the magma backend is available::

            sage: G = Genus(matrix.diagonal([1, 1, 7]))
            sage: G.representatives(backend='magma')  # optional - magma
            (
            [1 0 0]  [ 1  0  0]
            [0 1 0]  [ 0  2 -1]
            [0 0 7], [ 0 -1  4]
            )
        """
    def local_symbols(self):
        """
        Return a copy of the list of local symbols of this symbol.

        EXAMPLES::

            sage: A = matrix.diagonal(ZZ, [2, -4, 6, 8])
            sage: GS = Genus(A)
            sage: GS.local_symbols()
            [Genus symbol at 2:    [2^-2 4^1 8^1]_4,
             Genus symbol at 3:     1^-3 3^-1]
        """
    def local_symbol(self, p):
        """
        Return a copy of the local symbol at the prime `p`.

        EXAMPLES::

            sage: A = matrix.diagonal(ZZ, [2, -4, 6, 8])
            sage: GS = Genus(A)
            sage: GS.local_symbol(3)
            Genus symbol at 3:     1^-3 3^-1
        """
    @cached_method
    def mass(self, backend: str = 'sage'):
        """
        Return the mass of this genus.

        The genus must be definite.
        Let `L_1, ... L_n` be a complete list of representatives
        of the isometry classes in this genus.
        Its mass is defined as

        .. MATH::

            \\sum_{i=1}^n \\frac{1}{|O(L_i)|}.

        INPUT:

        - ``backend`` -- ``'sage'`` (default) or ``'magma'``

        OUTPUT: a rational number

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.genus import genera
            sage: G = genera((8,0), 1, even=True)[0]
            sage: G.mass()                                                              # needs sage.symbolic
            1/696729600
            sage: G.mass(backend='magma')  # optional - magma
            1/696729600

        The `E_8` lattice is unique in its genus::

            sage: E8 = QuadraticForm(G.representative())
            sage: E8.number_of_automorphisms()
            696729600

        TESTS:

        Check a random genus with magma::

            sage: d = ZZ.random_element(1, 1000)
            sage: n = ZZ.random_element(2, 10)
            sage: L = genera((n,0), d, d, even=False)
            sage: k = ZZ.random_element(0, len(L))
            sage: G = L[k]
            sage: G.mass()==G.mass(backend='magma')  # optional - magma
            True

        Error messages::

            sage: G.mass(backend='foo')
            Traceback (most recent call last):
            ...
            ValueError: unknown backend: foo
            sage: G = Genus(matrix(ZZ, 2, [0, 1, 1, 0]))
            sage: G.mass()
            Traceback (most recent call last):
            ...
            ValueError: the genus must be definite.
        """
    def level(self):
        """
        Return the level of this genus.

        This is the denominator of the inverse Gram matrix
        of a representative.

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([2, 4, 18]))
            sage: G.level()
            36
        """
    def scale(self):
        """
        Return the scale of this genus.

        Let `L` be a lattice with bilinear form `b`.
        The scale of `(L,b)` is defined as the ideal
        `b(L,L)`.

        OUTPUT: integer

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([2, 4, 18]))
            sage: G.scale()
            2
        """
    def norm(self):
        """
        Return the norm of this genus.

        Let `L` be a lattice with bilinear form `b`.
        The scale of `(L,b)` is defined as the ideal
        generated by `\\{b(x,x) | x \\in L\\}`.

        EXAMPLES::

            sage: G = Genus(matrix.diagonal([6, 4, 18]))
            sage: G.norm()
            2
            sage: G = Genus(matrix(ZZ, 2, [0, 1, 1, 0]))
            sage: G.norm()
            2
        """

def M_p(species, p):
    """
    Return the diagonal factor `M_p` as a function of the species.

    EXAMPLES:

    These examples are taken from Table 2 of [CS1988]_::

        sage: from sage.quadratic_forms.genera.genus import M_p
        sage: M_p(0, 2)
        1
        sage: M_p(1, 2)
        1/2
        sage: M_p(-2, 2)
        1/3
        sage: M_p(2, 2)
        1
        sage: M_p(3, 2)
        2/3
        sage: M_p(-4, 2)
        8/15
        sage: M_p(4, 2)
        8/9
        sage: M_p(5, 2)
        32/45

    TESTS:

    More values of the table for testing::

        sage: M_p(0, 3)
        1
        sage: M_p(1, 3)
        1/2
        sage: M_p(-2, 3)
        3/8
        sage: M_p(2, 3)
        3/4
        sage: M_p(3, 3)
        9/16
        sage: M_p(-4, 3)
        81/160
        sage: M_p(4, 3)
        81/128
        sage: M_p(5, 3)
        729/1280

        sage: M_p(0, 5)
        1
        sage: M_p(1, 5)
        1/2
        sage: M_p(-2, 5)
        5/12
        sage: M_p(2, 5)
        5/8
        sage: M_p(3, 5)
        25/48
        sage: M_p(-4, 5)
        625/1248
        sage: M_p(4, 5)
        625/1152
    """
