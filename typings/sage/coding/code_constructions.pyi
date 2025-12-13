from .linear_code import LinearCode as LinearCode
from sage.arith.misc import gcd as gcd, quadratic_residues as quadratic_residues
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.matrix.special import random_matrix as random_matrix
from sage.misc.misc_c import prod as prod
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.sequence import Sequence as Sequence, Sequence_generic as Sequence_generic

def permutation_action(g, v):
    '''
    Return permutation of rows `g * v`.

    Works on lists, matrices,
    sequences and vectors (by permuting coordinates). The code requires
    switching from `i` to `i+1` (and back again) since the :class:`SymmetricGroup`
    is, by convention, the symmetric group on the "letters" `1`, `2`, ...,
    `n` (not `0`, `1`, ..., `n-1`).

    EXAMPLES::

        sage: # needs sage.groups
        sage: V = VectorSpace(GF(3),5)
        sage: v = V([0,1,2,0,1])
        sage: G = SymmetricGroup(5)
        sage: g = G([(1,2,3)])
        sage: permutation_action(g,v)
        (1, 2, 0, 0, 1)
        sage: g = G([()])
        sage: permutation_action(g,v)
        (0, 1, 2, 0, 1)
        sage: g = G([(1,2,3,4,5)])
        sage: permutation_action(g,v)
        (1, 2, 0, 1, 0)
        sage: L = Sequence([1,2,3,4,5])
        sage: permutation_action(g,L)
        [2, 3, 4, 5, 1]
        sage: MS = MatrixSpace(GF(3),3,7)
        sage: A = MS([[1,0,0,0,1,1,0],[0,1,0,1,0,1,0],[0,0,0,0,0,0,1]])
        sage: S5 = SymmetricGroup(5)
        sage: g = S5([(1,2,3)])
        sage: A
        [1 0 0 0 1 1 0]
        [0 1 0 1 0 1 0]
        [0 0 0 0 0 0 1]
        sage: permutation_action(g,A)
        [0 1 0 1 0 1 0]
        [0 0 0 0 0 0 1]
        [1 0 0 0 1 1 0]

    It also works on lists and is a "left action"::

        sage: # needs sage.groups
        sage: v = [0,1,2,0,1]
        sage: G = SymmetricGroup(5)
        sage: g = G([(1,2,3)])
        sage: gv = permutation_action(g,v); gv
        [1, 2, 0, 0, 1]
        sage: permutation_action(g,v) == g(v)
        True
        sage: h = G([(3,4)])
        sage: gv = permutation_action(g,v)
        sage: hgv = permutation_action(h,gv)
        sage: hgv == permutation_action(h*g,v)
        True

    AUTHORS:

    - David Joyner, licensed under the GPL v2 or greater.
    '''
def walsh_matrix(m0):
    """
    This is the generator matrix of a Walsh code. The matrix of
    codewords correspond to a Hadamard matrix.

    EXAMPLES::

        sage: walsh_matrix(2)
        [0 0 1 1]
        [0 1 0 1]
        sage: walsh_matrix(3)
        [0 0 0 0 1 1 1 1]
        [0 0 1 1 0 0 1 1]
        [0 1 0 1 0 1 0 1]
        sage: C = LinearCode(walsh_matrix(4)); C
        [16, 4] linear code over GF(2)
        sage: C.spectrum()
        [1, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0]

    This last code has minimum distance 8.

    REFERENCES:

    - :wikipedia:`Hadamard_matrix`
    """
def DuadicCodeEvenPair(F, S1, S2):
    '''
    Construct the "even pair" of duadic codes associated to the
    "splitting" (see the docstring for ``_is_a_splitting``
    for the definition) S1, S2 of n.

    .. warning::

       Maybe the splitting should be associated to a sum of
       q-cyclotomic cosets mod n, where q is a *prime*.

    EXAMPLES::

        sage: from sage.coding.code_constructions import _is_a_splitting
        sage: n = 11; q = 3
        sage: C = Zmod(n).cyclotomic_cosets(q); C
        [[0], [1, 3, 4, 5, 9], [2, 6, 7, 8, 10]]
        sage: S1 = C[1]
        sage: S2 = C[2]
        sage: _is_a_splitting(S1,S2,11)
        True
        sage: codes.DuadicCodeEvenPair(GF(q),S1,S2)
        ([11, 5] Cyclic Code over GF(3),
         [11, 5] Cyclic Code over GF(3))
    '''
def DuadicCodeOddPair(F, S1, S2):
    '''
    Construct the "odd pair" of duadic codes associated to the
    "splitting" S1, S2 of n.

    .. warning::

       Maybe the splitting should be associated to a sum of
       q-cyclotomic cosets mod n, where q is a *prime*.

    EXAMPLES::

        sage: from sage.coding.code_constructions import _is_a_splitting
        sage: n = 11; q = 3
        sage: C = Zmod(n).cyclotomic_cosets(q); C
        [[0], [1, 3, 4, 5, 9], [2, 6, 7, 8, 10]]
        sage: S1 = C[1]
        sage: S2 = C[2]
        sage: _is_a_splitting(S1,S2,11)
        True
        sage: codes.DuadicCodeOddPair(GF(q),S1,S2)
        ([11, 6] Cyclic Code over GF(3),
         [11, 6] Cyclic Code over GF(3))

    This is consistent with Theorem 6.1.3 in [HP2003]_.
    '''
def ExtendedQuadraticResidueCode(n, F):
    """
    The extended quadratic residue code (or XQR code) is obtained from
    a QR code by adding a check bit to the last coordinate. (These
    codes have very remarkable properties such as large automorphism
    groups and duality properties - see [HP2003]_, Section 6.6.3-6.6.4.)

    INPUT:

    - ``n`` -- an odd prime

    - ``F`` -- a finite prime field whose order must be a
      quadratic residue modulo `n`

    OUTPUT: an extended quadratic residue code

    EXAMPLES::

        sage: C1 = codes.QuadraticResidueCode(7, GF(2))
        sage: C2 = C1.extended_code()
        sage: C3 = codes.ExtendedQuadraticResidueCode(7, GF(2)); C3
        Extension of [7, 4] Cyclic Code over GF(2)
        sage: C2 == C3
        True
        sage: C = codes.ExtendedQuadraticResidueCode(17, GF(2))
        sage: C
        Extension of [17, 9] Cyclic Code over GF(2)
        sage: C3 = codes.QuadraticResidueCodeOddPair(7, GF(2))[0]
        sage: C3x = C3.extended_code()
        sage: C4 = codes.ExtendedQuadraticResidueCode(7, GF(2))
        sage: C3x == C4
        True

    AUTHORS:

    - David Joyner (07-2006)
    """
def from_parity_check_matrix(H):
    """
    Return the linear code that has ``H`` as a parity check matrix.

    If ``H`` has dimensions `h \\times n` then the linear code will have
    dimension `n-h` and length `n`.

    EXAMPLES::

        sage: C = codes.HammingCode(GF(2), 3); C
        [7, 4] Hamming Code over GF(2)
        sage: H = C.parity_check_matrix(); H
        [1 0 1 0 1 0 1]
        [0 1 1 0 0 1 1]
        [0 0 0 1 1 1 1]
        sage: C2 = codes.from_parity_check_matrix(H); C2
        [7, 4] linear code over GF(2)
        sage: C2.systematic_generator_matrix() == C.systematic_generator_matrix()
        True
    """
def QuadraticResidueCode(n, F):
    """
    A quadratic residue code (or QR code) is a cyclic code whose
    generator polynomial is the product of the polynomials
    `x-\\alpha^i` (`\\alpha` is a primitive
    `n`-th root of unity; `i` ranges over the set of
    quadratic residues modulo `n`).

    See :class:`QuadraticResidueCodeEvenPair` and
    :class:`QuadraticResidueCodeOddPair` for a more general construction.

    INPUT:

    - ``n`` -- an odd prime

    - ``F`` -- a finite prime field whose order must be a
      quadratic residue modulo `n`

    OUTPUT: a quadratic residue code

    EXAMPLES::

        sage: C = codes.QuadraticResidueCode(7, GF(2))
        sage: C
        [7, 4] Cyclic Code over GF(2)
        sage: C = codes.QuadraticResidueCode(17, GF(2))
        sage: C
        [17, 9] Cyclic Code over GF(2)
        sage: C1 = codes.QuadraticResidueCodeOddPair(7, GF(2))[0]
        sage: C2 = codes.QuadraticResidueCode(7, GF(2))
        sage: C1 == C2
        True
        sage: C1 = codes.QuadraticResidueCodeOddPair(17, GF(2))[0]
        sage: C2 = codes.QuadraticResidueCode(17, GF(2))
        sage: C1 == C2
        True

    AUTHORS:

    - David Joyner (11-2005)
    """
def QuadraticResidueCodeEvenPair(n, F):
    '''
    Quadratic residue codes of a given odd prime length and base ring
    either don\'t exist at all or occur as 4-tuples - a pair of
    "odd-like" codes and a pair of "even-like" codes. If `n > 2` is prime
    then (Theorem 6.6.2 in [HP2003]_) a QR code exists over `\\GF{q}` iff q is a
    quadratic residue mod `n`.

    They are constructed as "even-like" duadic codes associated the
    splitting `(Q,N)` mod `n`, where `Q` is the set of nonzero quadratic
    residues and `N` is the non-residues.

    EXAMPLES::

        sage: codes.QuadraticResidueCodeEvenPair(17, GF(13))  # known bug (#25896)
        ([17, 8] Cyclic Code over GF(13),
         [17, 8] Cyclic Code over GF(13))
        sage: codes.QuadraticResidueCodeEvenPair(17, GF(2))
        ([17, 8] Cyclic Code over GF(2),
         [17, 8] Cyclic Code over GF(2))
        sage: codes.QuadraticResidueCodeEvenPair(13, GF(9,"z"))  # known bug (#25896)
        ([13, 6] Cyclic Code over GF(9),
         [13, 6] Cyclic Code over GF(9))
        sage: C1,C2 = codes.QuadraticResidueCodeEvenPair(7, GF(2))
        sage: C1.is_self_orthogonal()
        True
        sage: C2.is_self_orthogonal()
        True
        sage: C3 = codes.QuadraticResidueCodeOddPair(17, GF(2))[0]
        sage: C4 = codes.QuadraticResidueCodeEvenPair(17, GF(2))[1]
        sage: C3.systematic_generator_matrix() == C4.dual_code().systematic_generator_matrix()
        True

    This is consistent with Theorem 6.6.9 and Exercise 365 in [HP2003]_.

    TESTS::

        sage: codes.QuadraticResidueCodeEvenPair(14,Zmod(4))
        Traceback (most recent call last):
        ...
        ValueError: the argument F must be a finite field
        sage: codes.QuadraticResidueCodeEvenPair(14, GF(2))
        Traceback (most recent call last):
        ...
        ValueError: the argument n must be an odd prime
        sage: codes.QuadraticResidueCodeEvenPair(5, GF(2))
        Traceback (most recent call last):
        ...
        ValueError: the order of the finite field must be a quadratic residue modulo n
    '''
def QuadraticResidueCodeOddPair(n, F):
    '''
    Quadratic residue codes of a given odd prime length and base ring
    either don\'t exist at all or occur as 4-tuples - a pair of
    "odd-like" codes and a pair of "even-like" codes. If n 2 is prime
    then (Theorem 6.6.2 in [HP2003]_) a QR code exists over `\\GF{q} iff `q` is a
    quadratic residue mod `n`.

    They are constructed as "odd-like" duadic codes associated the
    splitting `(Q,N)` mod `n`, where `Q` is the set of nonzero quadratic
    residues and `N` is the non-residues.

    EXAMPLES::

        sage: codes.QuadraticResidueCodeOddPair(17, GF(13))  # known bug (#25896)
        ([17, 9] Cyclic Code over GF(13),
         [17, 9] Cyclic Code over GF(13))
        sage: codes.QuadraticResidueCodeOddPair(17, GF(2))
        ([17, 9] Cyclic Code over GF(2),
         [17, 9] Cyclic Code over GF(2))
        sage: codes.QuadraticResidueCodeOddPair(13, GF(9,"z"))  # known bug (#25896)
        ([13, 7] Cyclic Code over GF(9),
         [13, 7] Cyclic Code over GF(9))
        sage: C1 = codes.QuadraticResidueCodeOddPair(17, GF(2))[1]
        sage: C1x = C1.extended_code()
        sage: C2 = codes.QuadraticResidueCodeOddPair(17, GF(2))[0]
        sage: C2x = C2.extended_code()
        sage: C2x.spectrum(); C1x.spectrum()
        [1, 0, 0, 0, 0, 0, 102, 0, 153, 0, 153, 0, 102, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 102, 0, 153, 0, 153, 0, 102, 0, 0, 0, 0, 0, 1]
        sage: C3 = codes.QuadraticResidueCodeOddPair(7, GF(2))[0]
        sage: C3x = C3.extended_code()
        sage: C3x.spectrum()
        [1, 0, 0, 0, 14, 0, 0, 0, 1]

    This is consistent with Theorem 6.6.14 in [HP2003]_.

    TESTS::

        sage: codes.QuadraticResidueCodeOddPair(9, GF(2))
        Traceback (most recent call last):
        ...
        ValueError: the argument n must be an odd prime
    '''
def random_linear_code(F, length, dimension):
    """
    Generate a random linear code of length ``length``, dimension ``dimension``
    and over the field ``F``.

    This function is Las Vegas probabilistic: always correct, usually fast.
    Random matrices over the ``F`` are drawn until one with full rank is hit.

    If ``F`` is infinite, the distribution of the elements in the random
    generator matrix will be random according to the distribution of
    ``F.random_element()``.

    EXAMPLES::

        sage: C = codes.random_linear_code(GF(2), 10, 3)
        sage: C
        [10, 3] linear code over GF(2)
        sage: C.generator_matrix().rank()
        3
    """
def ToricCode(P, F):
    '''
    Let `P` denote a list of lattice points in
    `\\ZZ^d` and let `T` denote the set of all
    points in `(F^x)^d` (ordered in some fixed way). Put
    `n=|T|` and let `k` denote the dimension of the
    vector space of functions `V = \\mathrm{Span}\\{x^e \\ |\\ e \\in P\\}`.
    The associated toric code `C` is the evaluation code which
    is the image of the evaluation map

    .. MATH::

        \\operatorname{eval}_T : V \\rightarrow F^n,


    where `x^e` is the multi-index notation
    (`x=(x_1,...,x_d)`, `e=(e_1,...,e_d)`, and
    `x^e = x_1^{e_1}...x_d^{e_d}`), where
    `\\operatorname{eval}_T (f(x)) = (f(t_1),...,f(t_n))`, and where
    `T=\\{t_1,...,t_n\\}`. This function returns the toric
    codes discussed in [Joy2004]_.

    INPUT:

    - ``P`` -- all the integer lattice points in a polytope
      defining the toric variety

    - ``F`` -- a finite field

    OUTPUT: toric code with length `n`, dimension `k` over field `F`

    EXAMPLES::

         sage: C = codes.ToricCode([[0,0],[1,0],[2,0],[0,1],[1,1]], GF(7))
         sage: C
         [36, 5] linear code over GF(7)
         sage: C.minimum_distance()                                                     # needs sage.groups
         24
         sage: C.minimum_distance(algorithm=\'guava\')  # optional - gap_package_guava
         ...24
         sage: C = codes.ToricCode([[-2,-2],[-1,-2],[-1,-1],[-1,0],
         ....:                      [0,-1],[0,0],[0,1],[1,-1],[1,0]], GF(5))
         sage: C
         [16, 9] linear code over GF(5)
         sage: C.minimum_distance()                                                     # needs sage.groups
         6
         sage: C.minimum_distance(algorithm=\'guava\')  # optional - gap_package_guava
         6
         sage: C = codes.ToricCode([[0,0],[1,1],[1,2],[1,3],[1,4],[2,1],
         ....:                      [2,2],[2,3],[3,1],[3,2],[4,1]], GF(8,"a"))
         sage: C
         [49, 11] linear code over GF(8)

    This is in fact a [49,11,28] code over `\\GF{8}`. If you type next
    ``C.minimum_distance()`` and wait overnight (!), you
    should get 28.

    AUTHOR:

    - David Joyner (07-2006)
    '''
def WalshCode(m):
    """
    Return the binary Walsh code of length `2^m`.

    The matrix
    of codewords correspond to a Hadamard matrix. This is a (constant
    rate) binary linear `[2^m,m,2^{m-1}]` code.

    EXAMPLES::

        sage: C = codes.WalshCode(4); C
        [16, 4] linear code over GF(2)
        sage: C = codes.WalshCode(3); C
        [8, 3] linear code over GF(2)
        sage: C.spectrum()
        [1, 0, 0, 0, 7, 0, 0, 0, 0]
        sage: C.minimum_distance()                                                      # needs sage.libs.gap
        4
        sage: C.minimum_distance(algorithm='gap')  # check d=2^(m-1)                    # needs sage.libs.gap
        4

    REFERENCES:

    - :wikipedia:`Hadamard_matrix`

    - :wikipedia:`Walsh_code`
    """
