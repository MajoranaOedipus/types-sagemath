from sage.categories.rings import Rings as Rings
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.search import search as search
from sage.misc.verbose import verbose as verbose
from sage.modular.modsym.manin_symbol_list import ManinSymbolList as ManinSymbolList
from sage.rings.rational_field import RationalField as RationalField

SPARSE: bool

def modS_relations(syms):
    """
    Compute quotient of Manin symbols by the S relations.

    Here S is the 2x2 matrix [0, -1; 1, 0].

    INPUT:

    - ``syms`` -- :class:`ManinSymbolList`

    OUTPUT:

    - ``rels`` -- set of pairs of pairs (j, s), where if
      mod[i] = (j,s), then x_i = s\\*x_j (mod S relations)

    EXAMPLES::

        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
        sage: from sage.modular.modsym.relation_matrix import modS_relations

    ::

        sage: syms = ManinSymbolList_gamma0(2, 4); syms
        Manin Symbol List of weight 4 for Gamma0(2)
        sage: modS_relations(syms)
        {((0, 1), (7, 1)),
         ((1, 1), (6, 1)),
         ((2, 1), (8, 1)),
         ((3, -1), (4, 1)),
         ((3, 1), (4, -1)),
         ((5, -1), (5, 1))}

    ::

        sage: syms = ManinSymbolList_gamma0(7, 2); syms
        Manin Symbol List of weight 2 for Gamma0(7)
        sage: modS_relations(syms)
        {((0, 1), (1, 1)), ((2, 1), (7, 1)), ((3, 1), (4, 1)), ((5, 1), (6, 1))}

    Next we do an example with Gamma1::

        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma1
        sage: syms = ManinSymbolList_gamma1(3,2); syms
        Manin Symbol List of weight 2 for Gamma1(3)
        sage: modS_relations(syms)
        {((0, 1), (2, 1)),
         ((0, 1), (5, 1)),
         ((1, 1), (2, 1)),
         ((1, 1), (5, 1)),
         ((3, 1), (4, 1)),
         ((3, 1), (6, 1)),
         ((4, 1), (7, 1)),
         ((6, 1), (7, 1))}
    """
def modI_relations(syms, sign):
    """
    Compute quotient of Manin symbols by the I relations.

    INPUT:

    - ``syms`` -- :class:`ManinSymbolList`

    - ``sign`` -- integer (either -1, 0, or 1)

    OUTPUT:

    - ``rels`` -- set of pairs of pairs (j, s), where if
      mod[i] = (j,s), then x_i = s\\*x_j (mod S relations)

    EXAMPLES::

        sage: L = sage.modular.modsym.manin_symbol_list.ManinSymbolList_gamma1(4, 3)
        sage: sage.modular.modsym.relation_matrix.modI_relations(L, 1)
        {((0, 1), (0, -1)),
         ((1, 1), (1, -1)),
         ((2, 1), (8, -1)),
         ((3, 1), (9, -1)),
         ((4, 1), (10, -1)),
         ((5, 1), (11, -1)),
         ((6, 1), (6, -1)),
         ((7, 1), (7, -1)),
         ((8, 1), (2, -1)),
         ((9, 1), (3, -1)),
         ((10, 1), (4, -1)),
         ((11, 1), (5, -1)),
         ((12, 1), (12, 1)),
         ((13, 1), (13, 1)),
         ((14, 1), (20, 1)),
         ((15, 1), (21, 1)),
         ((16, 1), (22, 1)),
         ((17, 1), (23, 1)),
         ((18, 1), (18, 1)),
         ((19, 1), (19, 1)),
         ((20, 1), (14, 1)),
         ((21, 1), (15, 1)),
         ((22, 1), (16, 1)),
         ((23, 1), (17, 1))}

    .. warning::

       We quotient by the involution eta((u,v)) = (-u,v), which has
       the opposite sign as the involution in Merel's Springer LNM
       1585 paper! Thus our +1 eigenspace is his -1 eigenspace,
       etc. We do this for consistency with MAGMA.
    """
def T_relation_matrix_wtk_g0(syms, mod, field, sparse):
    """
    Compute a matrix whose echelon form gives the quotient by 3-term T
    relations. Despite the name, this is used for all modular symbols spaces
    (including those with character and those for `\\Gamma_1` and `\\Gamma_H`
    groups), not just `\\Gamma_0`.

    INPUT:

    - ``syms`` -- :class:`ManinSymbolList`

    - ``mod`` -- list that gives quotient modulo some two-term relations, i.e.,
      the S relations, and if sign is nonzero, the I relations

    - ``field`` -- ``base_ring``

    - ``sparse`` -- boolean; whether to use sparse rather than dense
      linear algebra

    OUTPUT: a sparse matrix whose rows correspond to the reduction of
    the `T` relations modulo the `S` and `I` relations.

    EXAMPLES::

        sage: from sage.modular.modsym.relation_matrix import sparse_2term_quotient, T_relation_matrix_wtk_g0, modS_relations
        sage: L = sage.modular.modsym.manin_symbol_list.ManinSymbolList_gamma_h(GammaH(36, [17,19]), 2)
        sage: modS = sparse_2term_quotient(modS_relations(L), 216, QQ)
        sage: T_relation_matrix_wtk_g0(L, modS, QQ, False)
        72 x 216 dense matrix over Rational Field (use the '.str()' method to see the entries)
        sage: T_relation_matrix_wtk_g0(L, modS, GF(17), True)
        72 x 216 sparse matrix over Finite Field of size 17 (use the '.str()' method to see the entries)
    """
def gens_to_basis_matrix(syms, relation_matrix, mod, field, sparse):
    """
    Compute echelon form of 3-term relation matrix, and read off each
    generator in terms of basis.

    INPUT:

    - ``syms`` -- :class:`ManinSymbolList`

    - ``relation_matrix`` -- as output by
      ``__compute_T_relation_matrix(self, mod)``

    - ``mod`` -- quotient of modular symbols modulo the
      2-term S (and possibly I) relations

    - ``field`` -- base field

    - ``sparse`` -- boolean; whether or not matrix should be sparse

    OUTPUT:

    ``matrix`` -- a matrix whose `i`-th row expresses the Manin symbol
    generators in terms of a basis of Manin symbols (modulo the S, (possibly
    I,) and T rels). Note that the entries of the matrix need not be integers.

    - ``list`` -- integers `i`, such that the Manin symbols `x_i` are a basis

    EXAMPLES::

        sage: from sage.modular.modsym.relation_matrix import sparse_2term_quotient, T_relation_matrix_wtk_g0, gens_to_basis_matrix, modS_relations
        sage: L = sage.modular.modsym.manin_symbol_list.ManinSymbolList_gamma1(4, 3)
        sage: modS = sparse_2term_quotient(modS_relations(L), 24, GF(3))
        sage: gens_to_basis_matrix(L, T_relation_matrix_wtk_g0(L, modS, GF(3), 24), modS, GF(3), True)
        (24 x 2 sparse matrix over Finite Field of size 3, [13, 23])
    """
def compute_presentation(syms, sign, field, sparse=None):
    """
    Compute the presentation for self, as a quotient of Manin symbols
    modulo relations.

    INPUT:

    - ``syms`` -- :class:`ManinSymbolList`

    - ``sign`` -- integer (-1, 0, 1)

    - ``field`` -- a field

    OUTPUT:

    - sparse matrix whose rows give each generator
      in terms of a basis for the quotient

    - list of integers that give the basis for the
      quotient

    - mod: list where mod[i]=(j,s) means that x_i
      = s\\*x_j modulo the 2-term S (and possibly I) relations.


    ALGORITHM:

    #. Let `S = [0,-1; 1,0], T = [0,-1; 1,-1]`, and
       `I = [-1,0; 0,1]`.

    #. Let `x_0,\\ldots, x_{n-1}` by a list of all
       non-equivalent Manin symbols.

    #. Form quotient by 2-term S and (possibly) I relations.

    #. Create a sparse matrix `A` with `m` columns,
       whose rows encode the relations

       .. MATH::

                          [x_i] + [x_i T] + [x_i T^2] = 0.


       There are about n such rows. The number of nonzero entries per row
       is at most 3\\*(k-1). Note that we must include rows for *all* i,
       since even if `[x_i] = [x_j]`, it need not be the case
       that `[x_i T] = [x_j T]`, since `S` and
       `T` do not commute. However, in many cases we have an a
       priori formula for the dimension of the quotient by all these
       relations, so we can omit many relations and just check that there
       are enough at the end--if there aren't, we add in more.

    #. Compute the reduced row echelon form of `A` using sparse
       Gaussian elimination.

    #. Use what we've done above to read off a sparse matrix R that
       uniquely expresses each of the n Manin symbols in terms of a subset
       of Manin symbols, modulo the relations. This subset of Manin
       symbols is a basis for the quotient by the relations.

    EXAMPLES::

        sage: L = sage.modular.modsym.manin_symbol_list.ManinSymbolList_gamma0(8,2)
        sage: sage.modular.modsym.relation_matrix.compute_presentation(L, 1, GF(9,'a'), True)
        (
        [2 0 0]
        [1 0 0]
        [0 0 0]
        [0 2 0]
        [0 0 0]
        [0 0 2]
        [0 0 0]
        [0 2 0]
        [0 0 0]
        [0 1 0]
        [0 1 0]
        [0 0 1], [1, 9, 11], [(1, 2), (1, 1), (0, 0), (9, 2), (0, 0), (11, 2), (0, 0), (9, 2), (0, 0), (9, 1), (9, 1), (11, 1)]
        )
    """
def relation_matrix_wtk_g0(syms, sign, field, sparse):
    """
    Compute the matrix of relations. Despite the name, this is used for all
    spaces (not just for Gamma0). For a description of the algorithm, see the
    docstring for ``compute_presentation``.

    INPUT:

    - ``syms`` -- :class:`ManinSymbolList`

    - ``sign`` -- integer (0, 1 or -1)

    - ``field`` -- the base field (non-field base rings not supported at present)

    - ``sparse`` -- boolean; whether to use sparse arithmetic

    Note that ManinSymbolList objects already have a specific weight, so there
    is no need for an extra ``weight`` parameter.

    OUTPUT: a pair (R, mod) where

    - R is a matrix as output by ``T_relation_matrix_wtk_g0``

    - mod is a set of 2-term relations as output by ``sparse_2term_quotient``

    EXAMPLES::

        sage: L = sage.modular.modsym.manin_symbol_list.ManinSymbolList_gamma0(8,2)
        sage: A = sage.modular.modsym.relation_matrix.relation_matrix_wtk_g0(L, 0, GF(2), True); A
        (
        [0 0 0 0 0 0 0 0 1 0 0 0]
        [0 0 0 0 0 0 0 0 1 1 1 0]
        [0 0 0 0 0 0 1 0 0 1 1 0]
        [0 0 0 0 0 0 1 0 0 0 0 0], [(1, 1), (1, 1), (8, 1), (10, 1), (6, 1), (11, 1), (6, 1), (9, 1), (8, 1), (9, 1), (10, 1), (11, 1)]
        )
        sage: A[0].is_sparse()
        True
    """
def sparse_2term_quotient(rels, n, F):
    '''
    Perform Sparse Gauss elimination on a matrix all of whose columns
    have at most 2 nonzero entries. We use an obvious algorithm, which
    runs fast enough. (Typically making the list of relations takes
    more time than computing this quotient.) This algorithm is more
    subtle than just "identify symbols in pairs", since complicated
    relations can cause generators to surprisingly equal 0.

    INPUT:

    - ``rels`` -- iterable made of pairs ((i,s), (j,t)). The pair
      represents the relation `s x_i + t x_j = 0`, where the `i, j` must
      be Python int\'s.

    - ``n`` -- integer, the `x_i` are `x_0, \\ldots, x_{n-1}`

    - ``F`` -- base field

    OUTPUT:

    ``mod`` -- list such that ``mod[i] = (j,s)``, which means that `x_i` is
    equivalent to `s x_j`, where the `x_j` are a basis for the quotient.

    EXAMPLES: We quotient out by the relations

    .. MATH::

        3*x0 - x1 = 0,\\qquad  x1 + x3 = 0,\\qquad   x2 + x3 = 0,\\qquad  x4 - x5 = 0

    to get::

        sage: rels = [((int(0),3), (int(1),-1)), ((int(1),1), (int(3),1)), ((int(2),1),(int(3),1)), ((int(4),1),(int(5),-1))]
        sage: n = 6
        sage: from sage.modular.modsym.relation_matrix import sparse_2term_quotient
        sage: sparse_2term_quotient(rels, n, QQ)
        [(3, -1/3), (3, -1), (3, -1), (3, 1), (5, 1), (5, 1)]
    '''
