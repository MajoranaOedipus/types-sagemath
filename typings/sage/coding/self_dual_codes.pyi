from sage.coding.linear_code import LinearCode as LinearCode
from sage.groups.perm_gps.permgroup import PermutationGroup as PermutationGroup
from sage.matrix.constructor import block_diagonal_matrix as block_diagonal_matrix, matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_function as cached_function
from sage.rings.integer_ring import ZZ as ZZ

def self_dual_binary_codes(n):
    '''
    Return the dictionary of inequivalent binary self dual codes of length `n`.

    For `n=4` even, returns the sd codes of a given length, up to (perm)
    equivalence, the (perm) aut gp, and the type.

    The number of inequivalent "diagonal" sd binary codes in the database of
    length n is ("diagonal" is defined by the conjecture above) is the
    same as the restricted partition number of `n`, where only integers
    from the set 1, 4, 6, 8, ... are allowed. This is the coefficient of
    `x^n` in the series expansion
    `(1-x)^{-1}\\prod_{2^\\infty (1-x^{2j})^{-1}}`. Typing the
    command ``f = (1-x)(-1)\\*prod([(1-x(2\\*j))(-1) for j in range(2,18)])``
    into Sage, we obtain for the coeffs of `x^4`,
    `x^6`, ... [1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 11, 11, 15, 15,
    22, 22, 30, 30, 42, 42, 56, 56, 77, 77, 101, 101, 135, 135, 176,
    176, 231] These numbers grow too slowly to account for all the sd
    codes (see Huffman+Pless\' Table 9.1, referenced above). In fact, in
    Table 9.10 of [HP2003]_, the number `B_n` of inequivalent sd binary codes
    of length `n` is given::

        n   2 4 6 8 10 12 14 16 18 20 22 24  26  28  30
        B_n 1 1 1 2  2  3  4  7  9 16 25 55 103 261 731

    According to http://oeis.org/classic/A003179,
    the next 2 entries are: 3295, 24147.

    EXAMPLES::

        sage: C = codes.databases.self_dual_binary_codes(10)
        sage: C["10"]["0"]["code"] == C["10"]["0"]["code"].dual_code()
        True
        sage: C["10"]["1"]["code"] == C["10"]["1"]["code"].dual_code()
        True
        sage: len(C["10"].keys())  # number of inequiv sd codes of length 10
        2
        sage: C = codes.databases.self_dual_binary_codes(12)
        sage: C["12"]["0"]["code"] == C["12"]["0"]["code"].dual_code()
        True
        sage: C["12"]["1"]["code"] == C["12"]["1"]["code"].dual_code()
        True
        sage: C["12"]["2"]["code"] == C["12"]["2"]["code"].dual_code()
        True
    '''
