from _typeshed import Incomplete
from sage.arith.misc import is_prime_power as is_prime_power
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.rest_index_of_methods import gen_rest_table_index as gen_rest_table_index
from sage.misc.unknown import Unknown as Unknown
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def group_law(G):
    """
    Return a triple ``(identity, operation, inverse)`` that define the
    operations on the group ``G``.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import group_law
        sage: group_law(Zmod(3))
        (0, <built-in function add>, <built-in function neg>)
        sage: group_law(SymmetricGroup(5))                                              # needs sage.groups
        ((), <built-in function mul>, <built-in function inv>)
        sage: group_law(VectorSpace(QQ, 3))                                             # needs sage.modules
        ((0, 0, 0), <built-in function add>, <built-in function neg>)
    """
def block_stabilizer(G, B):
    """
    Compute the left stabilizer of the block ``B`` under the action of ``G``.

    This function return the list of all `x\\in G` such that `x\\cdot B=B` (as a
    set).

    INPUT:

    - ``G`` -- a group (additive or multiplicative)
    - ``B`` -- a subset of ``G``

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import block_stabilizer

        sage: Z8 = Zmod(8)
        sage: block_stabilizer(Z8, [Z8(0),Z8(2),Z8(4),Z8(6)])
        [0, 2, 4, 6]
        sage: block_stabilizer(Z8, [Z8(0),Z8(2)])
        [0]

        sage: C = cartesian_product([Zmod(4),Zmod(3)])
        sage: block_stabilizer(C, [C((0,0)),C((2,0)),C((0,1)),C((2,1))])
        [(0, 0), (2, 0)]

        sage: b = list(map(Zmod(45),[1, 3, 7, 10, 22, 25, 30, 35, 37, 38, 44]))
        sage: block_stabilizer(Zmod(45),b)
        [0]
    """
def is_difference_family(G, D, v=None, k=None, l=None, verbose: bool = False):
    """
    Check whether ``D`` forms a difference family in the group ``G``.

    INPUT:

    - ``G`` -- group of cardinality ``v``
    - ``D`` -- set of ``k``-subsets of ``G``
    - ``v``, ``k``, ``l`` -- (optional) parameters of the difference family
    - ``verbose`` -- boolean (default: ``False``); whether to print additional
      information

    .. SEEALSO::

        :func:`difference_family`

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import is_difference_family
        sage: G = Zmod(21)
        sage: D = [[0,1,4,14,16]]
        sage: is_difference_family(G, D, 21, 5)
        True

        sage: G = Zmod(41)
        sage: D = [[0,1,4,11,29],[0,2,8,17,21]]
        sage: is_difference_family(G, D, verbose=True)
        Too few:
          5 is obtained 0 times in blocks []
          14 is obtained 0 times in blocks []
          27 is obtained 0 times in blocks []
          36 is obtained 0 times in blocks []
        Too much:
          4 is obtained 2 times in blocks [0, 1]
          13 is obtained 2 times in blocks [0, 1]
          28 is obtained 2 times in blocks [0, 1]
          37 is obtained 2 times in blocks [0, 1]
        False
        sage: D = [[0,1,4,11,29],[0,2,8,17,22]]
        sage: is_difference_family(G, D)
        True

        sage: G = Zmod(61)
        sage: D = [[0,1,3,13,34],[0,4,9,23,45],[0,6,17,24,32]]
        sage: is_difference_family(G, D)
        True

        sage: # needs sage.modules
        sage: G = AdditiveAbelianGroup([3]*4)
        sage: a,b,c,d = G.gens()
        sage: D = [[d, -a+d, -c+d, a-b-d, b+c+d],
        ....:      [c, a+b-d, -b+c, a-b+d, a+b+c],
        ....:      [-a-b+c+d, a-b-c-d, -a+c-d, b-c+d, a+b],
        ....:      [-b-d, a+b+d, a-b+c-d, a-b+c, -b+c+d]]
        sage: is_difference_family(G, D)
        True

    The following example has a third block with a non-trivial stabilizer::

        sage: G = Zmod(15)
        sage: D = [[0,1,4],[0,2,9],[0,5,10]]
        sage: is_difference_family(G,D,verbose=True)
        It is a (15,3,1)-difference family
        True

    The function also supports multiplicative groups (non necessarily Abelian)::

        sage: # needs sage.groups
        sage: G = DihedralGroup(8)
        sage: x,y = G.gens()
        sage: i = G.one()
        sage: D1 = [[i,x,x^4], [i,x^2, y*x], [i,x^5,y], [i,x^6,y*x^2], [i,x^7,y*x^5]]
        sage: is_difference_family(G, D1, 16, 3, 2)
        True
        sage: from sage.combinat.designs.bibd import BIBD_from_difference_family
        sage: bibd = BIBD_from_difference_family(G, D1, lambd=2)

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: K = GF(3^2,'z')
        sage: z = K.gen()
        sage: D = [[1,z+1,2]]
        sage: _ = is_difference_family(K, D, verbose=True)
        the number of differences (=6) must be a multiple of v-1=8
        sage: _
        False
    """
def singer_difference_set(q, d):
    """
    Return a difference set associated to the set of hyperplanes in a projective
    space of dimension `d` over `GF(q)`.

    A Singer difference set has parameters:

    .. MATH::

        v = \\frac{q^{d+1}-1}{q-1}, \\quad
        k = \\frac{q^d-1}{q-1}, \\quad
        \\lambda = \\frac{q^{d-1}-1}{q-1}.

    The idea of the construction is as follows. One consider the finite field
    `GF(q^{d+1})` as a vector space of dimension `d+1` over `GF(q)`. The set of
    `GF(q)`-lines in `GF(q^{d+1})` is a projective plane and its set of
    hyperplanes form a balanced incomplete block design.

    Now, considering a multiplicative generator `z` of `GF(q^{d+1})`, we get a
    transitive action of a cyclic group on our projective plane from which it is
    possible to build a difference set.

    The construction is given in details in [Stinson2004]_, section 3.3.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import singer_difference_set, is_difference_family
        sage: G,D = singer_difference_set(3,2)                                          # needs sage.rings.finite_rings
        sage: is_difference_family(G, D, verbose=True)                                  # needs sage.rings.finite_rings
        It is a (13,4,1)-difference family
        True

        sage: G,D = singer_difference_set(4,2)                                          # needs sage.rings.finite_rings
        sage: is_difference_family(G, D, verbose=True)                                  # needs sage.rings.finite_rings
        It is a (21,5,1)-difference family
        True

        sage: G,D = singer_difference_set(3,3)                                          # needs sage.rings.finite_rings
        sage: is_difference_family(G, D, verbose=True)                                  # needs sage.rings.finite_rings
        It is a (40,13,4)-difference family
        True

        sage: G,D = singer_difference_set(9,3)                                          # needs sage.rings.finite_rings
        sage: is_difference_family(G, D, verbose=True)                                  # needs sage.rings.finite_rings
        It is a (820,91,10)-difference family
        True
    """
def df_q_6_1(K, existence: bool = False, check: bool = True):
    """
    Return a `(q,6,1)`-difference family over the finite field `K`.

    The construction uses Theorem 11 of [Wi72]_.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.combinat.designs.difference_family import is_difference_family, df_q_6_1
        sage: prime_powers = [v for v in range(31,500,30) if is_prime_power(v)]
        sage: parameters = [v for v in prime_powers
        ....:               if df_q_6_1(GF(v,'a'), existence=True) is True]
        sage: parameters
        [31, 151, 181, 211, 241, 271, 331, 361, 421]
        sage: for v in parameters:
        ....:     K = GF(v, 'a')
        ....:     df = df_q_6_1(K, check=True)
        ....:     assert is_difference_family(K, df, v, 6, 1)

    .. TODO::

        Do improvements due to Zhen and Wu 1999.
    """
def radical_difference_set(K, k, l: int = 1, existence: bool = False, check: bool = True):
    '''
    Return a difference set made of a cyclotomic coset in the finite field
    ``K`` and with parameters ``k`` and ``l``.

    Most of these difference sets appear in chapter VI.18.48 of the Handbook of
    combinatorial designs.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import radical_difference_set

        sage: D = radical_difference_set(GF(7), 3, 1); D                                # needs sage.rings.finite_rings
        [[1, 2, 4]]
        sage: sorted(x-y for x in D[0] for y in D[0] if x != y)                         # needs sage.rings.finite_rings
        [1, 2, 3, 4, 5, 6]

        sage: D = radical_difference_set(GF(16,\'a\'), 6, 2)                              # needs sage.rings.finite_rings
        sage: sorted(x-y for x in D[0] for y in D[0] if x != y)                         # needs sage.rings.finite_rings
        [1,
         1,
         a,
         a,
         a + 1,
         a + 1,
         a^2,
         a^2,
         ...
         a^3 + a^2 + a + 1,
         a^3 + a^2 + a + 1]

        sage: for k in range(2,50):                                                     # needs sage.rings.finite_rings
        ....:     for l in reversed(divisors(k*(k-1))):
        ....:         v = k*(k-1)//l + 1
        ....:         if is_prime_power(v) and radical_difference_set(GF(v,\'a\'),k,l,existence=True) is True:
        ....:             _ = radical_difference_set(GF(v,\'a\'),k,l)
        ....:             print("{:3} {:3} {:3}".format(v,k,l))
          3   2   1
          4   3   2
          7   3   1
          5   4   3
          7   4   2
         13   4   1
         11   5   2
          7   6   5
         11   6   3
         16   6   2
          8   7   6
          9   8   7
         19   9   4
         37   9   2
         73   9   1
         11  10   9
         19  10   5
         23  11   5
         13  12  11
         23  12   6
         27  13   6
         27  14   7
         16  15  14
         31  15   7
        ...
         41  40  39
         79  40  20
         83  41  20
         43  42  41
         83  42  21
         47  46  45
         49  48  47
        197  49  12
    '''
def one_cyclic_tiling(A, n):
    """
    Given a subset ``A`` of the cyclic additive group `G = Z / nZ` return
    another subset `B` so that `A + B = G` and `|A| |B| = n` (i.e. any element
    of `G` is uniquely expressed as a sum `a+b` with `a` in `A` and `b` in `B`).

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import one_cyclic_tiling
        sage: tile = [0,2,4]
        sage: m = one_cyclic_tiling(tile,6); m
        [0, 3]
        sage: sorted((i+j)%6 for i in tile for j in m)
        [0, 1, 2, 3, 4, 5]

        sage: def print_tiling(tile, translat, n):
        ....:     for x in translat:
        ....:         print(''.join('X' if (i-x)%n in tile else '.' for i in range(n)))

        sage: tile = [0, 1, 2, 7]
        sage: m = one_cyclic_tiling(tile, 12)
        sage: print_tiling(tile, m, 12)
        XXX....X....
        ....XXX....X
        ...X....XXX.

        sage: tile = [0, 1, 5]
        sage: m = one_cyclic_tiling(tile, 12)
        sage: print_tiling(tile, m, 12)
        XX...X......
        ...XX...X...
        ......XX...X
        ..X......XX.

        sage: tile = [0, 2]
        sage: m = one_cyclic_tiling(tile, 8)
        sage: print_tiling(tile, m, 8)
        X.X.....
        ....X.X.
        .X.X....
        .....X.X

    ALGORITHM:

    Uses dancing links :mod:`sage.combinat.dlx`
    """
def one_radical_difference_family(K, k):
    """
    Search for a radical difference family on ``K`` using dancing links
    algorithm.

    For the definition of radical difference family, see
    :func:`radical_difference_family`. Here, we consider only radical difference
    family with `\\lambda = 1`.

    INPUT:

    - ``K`` -- a finite field of cardinality `q`
    - ``k`` -- positive integer so that `k(k-1)` divides `q-1`

    OUTPUT: either a difference family or ``None`` if it does not exist

    ALGORITHM:

    The existence of a radical difference family is equivalent to a one
    dimensional tiling (or packing) problem in a cyclic group. This subsequent
    problem is solved by a call to the function :func:`one_cyclic_tiling`.

        Let `K^*` be the multiplicative group of the finite field `K`. A radical
        family has the form `\\mathcal B = \\{x_1 B, \\ldots, x_k B\\}`, where
        `B=\\{x:x^{k}=1\\}` (for `k` odd) or `B=\\{x:x^{k-1}=1\\}\\cup \\{0\\}` (for
        `k` even). Equivalently, `K^*` decomposes as:

        .. MATH::

            K^* = \\Delta (x_1 B) \\cup \\cdots \\cup \\Delta (x_k B)
            = x_1 \\Delta B \\cup \\cdots \\cup x_k \\Delta B.

        We observe that `C=B\\backslash 0` is a subgroup of the (cyclic) group
        `K^*`, that can thus be generated by some element `r`. Furthermore, we
        observe that `\\Delta B` is always a union of cosets of `\\pm C` (which is
        twice larger than `C`).

        .. MATH::

            \\begin{array}{llll}
            (k\\text{ odd} ) & \\Delta B &= \\{r^i-r^j:r^i\\neq r^j\\} &= \\pm C\\cdot \\{r^i-1: 0 < i \\leq m\\}\\\\\n            (k\\text{ even}) & \\Delta B &= \\{r^i-r^j:r^i\\neq r^j\\}\\cup C &= \\pm C\\cdot \\{r^i-1: 0 < i < m\\}\\cup \\pm C
            \\end{array}

        where

        .. MATH::

            (k\\text{ odd})\\ m = (k-1)/2 \\quad \\text{and} \\quad (k\\text{ even})\\ m = k/2.

        Consequently, `\\mathcal B = \\{x_1 B, \\ldots, x_k B\\}` is a radical
        difference family if and only if `\\{x_1 (\\Delta B/(\\pm C)), \\ldots, x_k
        (\\Delta B/(\\pm C))\\}` is a partition of the cyclic group `K^*/(\\pm C)`.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import (
        ....:    one_radical_difference_family,
        ....:    is_difference_family)

        sage: one_radical_difference_family(GF(13),4)                                   # needs sage.rings.finite_rings
        [[0, 1, 3, 9]]

    The parameters that appear in [Bu95]_::

        sage: df = one_radical_difference_family(GF(449), 8); df                        # needs sage.rings.finite_rings
        [[0, 1, 18, 25, 176, 324, 359, 444],
         [0, 9, 88, 162, 222, 225, 237, 404],
         [0, 11, 140, 198, 275, 357, 394, 421],
         [0, 40, 102, 249, 271, 305, 388, 441],
         [0, 49, 80, 93, 161, 204, 327, 433],
         [0, 70, 99, 197, 230, 362, 403, 435],
         [0, 121, 141, 193, 293, 331, 335, 382],
         [0, 191, 285, 295, 321, 371, 390, 392]]
        sage: is_difference_family(GF(449), df, 449, 8, 1)                              # needs sage.rings.finite_rings
        True
    """
def radical_difference_family(K, k, l: int = 1, existence: bool = False, check: bool = True):
    '''
    Return a ``(v,k,l)``-radical difference family.

    Let fix an integer `k` and a prime power `q = t k(k-1) + 1`. Let `K` be a
    field of cardinality `q`. A `(q,k,1)`-difference family is *radical* if
    its base blocks are either: a coset of the `k`-th root of unity for `k` odd
    or a coset of `k-1`-th root of unity and `0` if `k` is even (the number `t`
    is the number of blocks of that difference family).

    The terminology comes from M. Buratti article [Bu95]_ but the first
    constructions go back to R. Wilson [Wi72]_.

    INPUT:

    - ``K`` -- a finite field
    - ``k`` -- positive integer; the size of the blocks
    - ``l`` -- integer (default: `1`); the `\\lambda` parameter
    - ``existence`` -- if ``True``, then return either ``True`` if Sage knows
      how to build such design, ``Unknown`` if it does not and ``False`` if it
      knows that the design does not exist
    - ``check`` -- boolean (default: ``True``); if ``True`` then the result of
      the computation is checked before being returned. This should not be
      needed but ensures that the output is correct

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import radical_difference_family

        sage: radical_difference_family(GF(73), 9)                                      # needs sage.rings.finite_rings
        [[1, 2, 4, 8, 16, 32, 37, 55, 64]]

        sage: radical_difference_family(GF(281), 5)                                     # needs sage.rings.finite_rings
        [[1, 86, 90, 153, 232],
         [4, 50, 63, 79, 85],
         [5, 36, 149, 169, 203],
         [7, 40, 68, 219, 228],
         [9, 121, 212, 248, 253],
         [29, 81, 222, 246, 265],
         [31, 137, 167, 247, 261],
         [32, 70, 118, 119, 223],
         [39, 56, 66, 138, 263],
         [43, 45, 116, 141, 217],
         [98, 101, 109, 256, 279],
         [106, 124, 145, 201, 267],
         [111, 123, 155, 181, 273],
         [156, 209, 224, 264, 271]]

        sage: for k in range(5,10):                                                     # needs sage.rings.finite_rings
        ....:     print("k = {}".format(k))
        ....:     list_q = []
        ....:     for q in range(k*(k-1)+1, 2000, k*(k-1)):
        ....:          if is_prime_power(q):
        ....:              K = GF(q,\'a\')
        ....:              if radical_difference_family(K, k, existence=True) is True:
        ....:                  list_q.append(q)
        ....:                  _ = radical_difference_family(K,k)
        ....:     print(" ".join(str(p) for p in list_q))
        k = 5
        41 61 81 241 281 401 421 601 641 661 701 761 821 881 1181 1201 1301 1321
        1361 1381 1481 1601 1681 1801 1901
        k = 6
        181 211 241 631 691 1531 1831 1861
        k = 7
        337 421 463 883 1723
        k = 8
        449 1009
        k = 9
        73 1153 1873
    '''
def twin_prime_powers_difference_set(p, check: bool = True):
    """
    Return a difference set on `GF(p) \\times GF(p+2)`.

    The difference set is built from the following element of the Cartesian
    product of finite fields `GF(p) \\times GF(p+2)`:

    - `(x,0)` with any `x`
    - `(x,y)` with `x` and `y` squares
    - `(x,y)` with `x` and `y` non-squares

    For more information see :wikipedia:`Difference_set`.

    INPUT:

    - ``check`` -- boolean (default: ``True``); if ``True``, then the result of
      the computation is checked before being returned. This should not be
      needed but ensures that the output is correct

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import twin_prime_powers_difference_set
        sage: G, D = twin_prime_powers_difference_set(3)
        sage: G
        The Cartesian product of (Finite Field of size 3, Finite Field of size 5)
        sage: D
        [[(1, 1), (1, 4), (2, 2), (2, 3), (0, 0), (1, 0), (2, 0)]]
    """
def are_mcfarland_1973_parameters(v, k, lmbda, return_parameters: bool = False):
    '''
    Test whether ``(v,k,lmbda)`` is a triple that can be obtained from the
    construction from [McF1973]_.

    See :func:`mcfarland_1973_construction`.

    INPUT:

    - ``v``, ``k``, ``lmbda`` -- integers; parameters of the difference family
    - ``return_parameters`` -- boolean (default: ``False``); if ``True``, return a
      pair ``(True, (q, s))`` so that ``(q,s)`` can be used in the function
      :func:`mcfarland_1973_construction` to actually build a
      ``(v,k,lmbda)``-difference family. Or ``(False, None)`` if the
      construction is not possible

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.combinat.designs.difference_family import are_mcfarland_1973_parameters
        sage: are_mcfarland_1973_parameters(64, 28, 12)
        True
        sage: are_mcfarland_1973_parameters(64, 28, 12, return_parameters=True)
        (True, (2, 2))
        sage: are_mcfarland_1973_parameters(60, 13, 5)
        False
        sage: are_mcfarland_1973_parameters(98125, 19500, 3875)
        True
        sage: are_mcfarland_1973_parameters(98125, 19500, 3875, True)
        (True, (5, 3))

        sage: from sage.combinat.designs.difference_family import are_mcfarland_1973_parameters
        sage: for v in range(1, 100):                                                   # needs sage.rings.finite_rings
        ....:     for k in range(1,30):
        ....:         for l in range(1,15):
        ....:             if are_mcfarland_1973_parameters(v,k,l):
        ....:                 answer, (q,s) = are_mcfarland_1973_parameters(v,k,l,return_parameters=True)
        ....:                 print("{} {} {} {} {}".format(v,k,l,q,s))
        ....:                 assert answer is True
        ....:                 assert designs.difference_family(v,k,l,existence=True) is True
        ....:                 G,D = designs.difference_family(v,k,l)
        16 6 2 2 1
        45 12 3 3 1
        64 28 12 2 2
        96 20 4 4 1
    '''
def mcfarland_1973_construction(q, s):
    '''
    Return a difference set.

    The difference set returned has the following parameters

    .. MATH::

        v = \\frac{q^{s+1}(q^{s+1}+q-2)}{q-1},
        k = \\frac{q^s (q^{s+1}-1)}{q-1},
        \\lambda = \\frac{q^s(q^s-1)}{q-1}

    This construction is due to [McF1973]_.

    INPUT:

    - ``q``, ``s`` -- integers; parameters for the difference set (see the above
      formulas for the expression of ``v``, ``k``, ``l`` in terms of ``q`` and
      ``s``)

    .. SEEALSO::

        The function :func:`are_mcfarland_1973_parameters` makes the translation
        between the parameters `(q,s)` corresponding to a given triple
        `(v,k,\\lambda)`.

    REFERENCES:

    .. [McF1973] Robert L. McFarland
       "A family of difference sets in non-cyclic groups"
       J. Combinatorial Theory (A) 15 (1973) 1--10.
       :doi:`10.1016/0097-3165(73)90031-9`

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import (
        ....:    mcfarland_1973_construction, is_difference_family)

        sage: G,D = mcfarland_1973_construction(3, 1)                                   # needs sage.modules
        sage: assert is_difference_family(G, D, 45, 12, 3)                              # needs sage.modules

        sage: G,D = mcfarland_1973_construction(2, 2)                                   # needs sage.modules
        sage: assert is_difference_family(G, D, 64, 28, 12)                             # needs sage.modules
    '''
def are_hadamard_difference_set_parameters(v, k, lmbda):
    """
    Check whether ``(v,k,lmbda)`` is of the form ``(4N^2, 2N^2 - N, N^2 - N)``.

    INPUT:

    - ``(v, k, lmbda)`` -- parameters of a difference set

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import are_hadamard_difference_set_parameters
        sage: are_hadamard_difference_set_parameters(36, 15, 6)
        True
        sage: are_hadamard_difference_set_parameters(60, 13, 5)
        False
    """
@cached_function
def hadamard_difference_set_product_parameters(N):
    """
    Check whether a product construction is available for Hadamard difference
    set with parameter ``N``.

    This function looks for two integers `N_1` and `N_2` greater than `1`
    and so that `N = 2 N_1 N_2` and there exists Hadamard difference set with
    parameters `(4 N_i^2, 2N_i^2 - N_i, N_i^2 - N_i)`. If such pair exists,
    the output is the pair ``(N_1, N_2)`` otherwise it is ``None``.

    INPUT:

    - ``N`` -- positive integer

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import hadamard_difference_set_product_parameters
        sage: hadamard_difference_set_product_parameters(8)                             # needs sage.rings.finite_rings
        (2, 2)
    """
def hadamard_difference_set_product(G1, D1, G2, D2):
    """
    Make a product of two Hadamard difference sets.

    This product construction appears in [Tu1984]_.

    INPUT:

    - ``G1, D1``, ``G2, D2`` -- two Hadamard difference sets

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import hadamard_difference_set_product
        sage: from sage.combinat.designs.difference_family import is_difference_family

        sage: G1,D1 = designs.difference_family(16,6,2)                                 # needs sage.rings.finite_rings
        sage: G2,D2 = designs.difference_family(36,15,6)                                # needs sage.rings.finite_rings

        sage: G11,D11 = hadamard_difference_set_product(G1,D1,G1,D1)                    # needs sage.rings.finite_rings
        sage: assert is_difference_family(G11, D11, 256, 120, 56)                       # needs sage.rings.finite_rings
        sage: assert designs.difference_family(256, 120, 56, existence=True) is True    # needs sage.rings.finite_rings

        sage: G12,D12 = hadamard_difference_set_product(G1,D1,G2,D2)                    # needs sage.rings.finite_rings
        sage: assert is_difference_family(G12, D12, 576, 276, 132)                      # needs sage.rings.finite_rings
        sage: assert designs.difference_family(576, 276, 132, existence=True) is True   # needs sage.rings.finite_rings
    """
def turyn_1965_3x3xK(k: int = 4):
    """
    Return a difference set in either `C_3 \\times C_3 \\times C_4` or `C_3 \\times
    C_3 \\times C_2 \\times C_2` with parameters `v=36`, `k=15`, `\\lambda=6`.

    This example appears in [Tu1965]_.

    INPUT:

    - ``k`` -- either ``2`` (to get a difference set in `C_3 \\times C_3 \\times
      C_2 \\times C_2`) or ``4`` (to get a difference set in `C_3 \\times C_3
      \\times C_3 \\times C_4`)

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import turyn_1965_3x3xK
        sage: from sage.combinat.designs.difference_family import is_difference_family
        sage: G,D = turyn_1965_3x3xK(4)
        sage: assert is_difference_family(G, D, 36, 15, 6)
        sage: G,D = turyn_1965_3x3xK(2)
        sage: assert is_difference_family(G, D, 36, 15, 6)
    """
def relative_difference_set_from_m_sequence(q, N, check: bool = True, return_group: bool = False):
    """
    Construct `R((q^N-1)/(q-1), q-1, q^{N-1}, q^{N-2})` where ``q`` is a prime power and `N\\ge 2`.

    The relative difference set is constructed over the set of additive integers modulo `q^N-1`,
    as described in Theorem 5.1 of [EB1966]_. Given an m-sequence `(a_i)` of period `q^N-1`, the
    set is: `R=\\{i | 0 \\le i \\le q^{N-1}, a_i=1\\}`.

    INPUT:

    - ``q`` -- a prime power
    - ``N`` -- a nonnegative number
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the
      result is a relative difference set before returning it
    - ``return_group`` -- boolean (default: ``False``); if ``True``, the function
      will also return the group from which the set is created

    OUTPUT:

    If ``return_group=False``, the function return only the relative difference
    set. Otherwise, it returns a tuple containing the group and the set.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import relative_difference_set_from_m_sequence
        sage: relative_difference_set_from_m_sequence(2, 4,               # random      # needs sage.modules sage.rings.finite_rings
        ....:                                         return_group=True)
        (Additive abelian group isomorphic to Z/15,
         [(0), (4), (5), (6), (7), (9), (11), (12)])
        sage: relative_difference_set_from_m_sequence(8, 2, check=False)  # random      # needs sage.modules sage.rings.finite_rings
        [(0), (6), (30), (40), (41), (44), (56), (61)]
        sage: relative_difference_set_from_m_sequence(6, 2)                             # needs sage.modules
        Traceback (most recent call last):
        ...
        ValueError: q must be a prime power

    TESTS::

        sage: from sage.combinat.designs.difference_family import is_relative_difference_set, _get_submodule_of_order
        sage: q, N = 5, 3
        sage: G, D = relative_difference_set_from_m_sequence(q, N, check=False,         # needs sage.modules sage.rings.finite_rings
        ....:                                                return_group=True)
        sage: H = _get_submodule_of_order(G, q-1)                                       # needs sage.modules sage.rings.finite_rings
        sage: is_relative_difference_set(D, G, H,                                       # needs sage.modules sage.rings.finite_rings
        ....:                            ((q^N-1)//(q-1), q-1, q^(N-1), q^(N-2)))
        True
        sage: q, N = 13, 2
        sage: G, D = relative_difference_set_from_m_sequence(q, N, check=False,         # needs sage.modules sage.rings.finite_rings
        ....:                                                return_group=True)
        sage: H = _get_submodule_of_order(G, q-1)                                       # needs sage.modules sage.rings.finite_rings
        sage: is_relative_difference_set(D, G, H,                                       # needs sage.modules sage.rings.finite_rings
        ....:                            ((q^N-1)//(q-1), q-1, q^(N-1), q^(N-2)))
        True
    """
def relative_difference_set_from_homomorphism(q, N, d, check: bool = True, return_group: bool = False):
    """
    Construct `R((q^N-1)/(q-1), n, q^{N-1}, q^{N-2}d)` where `nd = q-1`.

    Given a prime power `q`, a number `N \\ge 2` and integers `d` such that `d | q-1` we create the
    relative difference set using the construction from Corollary 5.1.1 of [EB1966]_.

    INPUT:

    - ``q`` -- a prime power
    - ``N`` -- integer greater than 1
    - ``d`` -- integer which divides `q-1`
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the
      result is a relative difference set before returning it
    - ``return_group`` -- boolean (default: ``False``); if ``True``, the function
      will also return the group from which the set is created

    OUTPUT:

    If ``return_group=False``, the function return only the relative difference
    set. Otherwise, it returns a tuple containing the group and the set.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import relative_difference_set_from_homomorphism
        sage: relative_difference_set_from_homomorphism(7, 2, 3)        # random        # needs sage.modules sage.rings.finite_rings
        [(0), (3), (4), (2), (13), (7), (14)]
        sage: relative_difference_set_from_homomorphism(9, 2, 4,        # random        # needs sage.modules sage.rings.finite_rings
        ....:                                           check=False, return_group=True)
        (Additive abelian group isomorphic to Z/80,
         [(0), (4), (6), (13), (7), (12), (15), (8), (9)])
        sage: relative_difference_set_from_homomorphism(9, 2, 5)                        # needs sage.modules sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        ValueError: q-1 must be a multiple of d

    TESTS::

        sage: from sage.combinat.designs.difference_family import is_relative_difference_set, _get_submodule_of_order
        sage: q, N, d = 11, 2, 5
        sage: G, D = relative_difference_set_from_homomorphism(q, N, d, check=False,    # needs sage.modules sage.rings.finite_rings
        ....:                                                  return_group=True)
        sage: H = _get_submodule_of_order(G, (q-1)//d)                                  # needs sage.modules sage.rings.finite_rings
        sage: is_relative_difference_set(D, G, H,                                       # needs sage.modules sage.rings.finite_rings
        ....:                            ((q**N-1)//(q-1), (q-1)//d, q**(N-1), q**(N-2)*d))
        True
        sage: q, N, d = 9, 2, 4
        sage: G, D = relative_difference_set_from_homomorphism(q, N, d, check=False,    # needs sage.modules sage.rings.finite_rings
        ....:                                                  return_group=True)
        sage: H = _get_submodule_of_order(G, (q-1)//d)                                  # needs sage.modules sage.rings.finite_rings
        sage: is_relative_difference_set(D, G, H,                                       # needs sage.modules sage.rings.finite_rings
        ....:                            ((q**N-1)//(q-1), (q-1)//d, q**(N-1), q**(N-2)*d))
        True
    """
def is_relative_difference_set(R, G, H, params, verbose: bool = False):
    """
    Check if ``R`` is a difference set of ``G`` relative to ``H``, with the given parameters.

    This function checks that `G`, `H` and `R` have the orders specified in the parameters, and
    that `R` satisfies the definition of relative difference set (from [EB1966]_): the collection of
    differences `r-s`, `r,s \\in R`, `r \\neq s` contains only elements of `G` which are not in `H`, and contains
    every such element exactly `d` times.

    INPUT:

    - ``R`` -- list; the relative diffeence set of length `k`
    - ``G`` -- an additive abelian group of order `mn`
    - ``H`` -- list; a submodule of ``G`` of order `n`
    - ``params`` -- tuple in the form `(m, n, k, d)`
    - ``verbose`` -- boolean (default: ``False``); if ``True``, the function
      will be verbose when the sequences do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import _get_submodule_of_order, relative_difference_set_from_m_sequence, is_relative_difference_set
        sage: q, N = 5, 2
        sage: params = ((q^N-1) // (q-1), q - 1, q^(N-1), q^(N-2))
        sage: G, R = relative_difference_set_from_m_sequence(q, N, return_group=True)   # needs sage.libs.pari sage.modules
        sage: H = _get_submodule_of_order(G, q - 1)                                     # needs sage.libs.pari sage.modules
        sage: is_relative_difference_set(R, G, H, params)                               # needs sage.libs.pari sage.modules
        True

    If we pass the ``verbose`` argument, the function will explain why it failed::

        sage: R2 = [G[1], G[2], G[3], G[5], G[6]]                                       # needs sage.libs.pari sage.modules
        sage: is_relative_difference_set(R2, G, H, params, verbose=True)                # needs sage.libs.pari sage.modules
        There is a value in the difference set which is not repeated d times
        False
    """
def is_supplementary_difference_set(Ks, v=None, lmbda=None, G=None, verbose: bool = False):
    """
    Check that the sets in ``Ks`` are `n-\\{v; k_1, ..., k_n; \\lambda \\}` supplementary
    difference sets over group ``G`` of order ``v``.

    From the definition in [Spe1975]_: let  `S_1, S_2, ..., S_n` be `n` subsets of a group `G` of order `v`
    such that `|S_i| = k_i`. If, for each `g \\in G`, `g \\neq 0`, the total number of solutions of `a_i - a'_i = g`, with
    `a_i, a'_i \\in S_i` is `\\lambda`, then `S_1, S_2, ..., S_n` are `n-\\{v; k_1, ..., k_n; \\lambda\\}` supplementary difference sets.

    One of the parameters ``v`` or ``G`` must always be specified. If ``G`` is not
    given, the function will use an ``AdditiveAbelianGroup`` of order ``v``.

    INPUT:

    - ``Ks`` -- list of sets to be checked
    - ``v`` -- integer; the parameter `v` of the supplementary difference sets
    - ``lmbda`` -- integer; the parameter `\\lambda` of the supplementary difference sets
    - ``G`` -- a group of order `v`
    - ``verbose`` -- boolean (default: ``False``); if ``True``, the function will
      be verbose when the sets do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import supplementary_difference_set_from_rel_diff_set, is_supplementary_difference_set
        sage: G, [S1, S2, S3, S4] = supplementary_difference_set_from_rel_diff_set(17)  # needs sage.modules sage.rings.finite_rings
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=16, G=G)          # needs sage.modules sage.rings.finite_rings
        True

    The parameter ``v`` can be given instead of ``G``::

        sage: is_supplementary_difference_set([S1, S2, S3, S4], v=16, lmbda=16)         # needs sage.modules sage.rings.finite_rings
        True
        sage: is_supplementary_difference_set([S1, S2, S3, S4], v=20, lmbda=16)         # needs sage.modules sage.rings.finite_rings
        False

    If ``verbose=True``, the function will be verbose::

        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=14, G=G,          # needs sage.modules sage.rings.finite_rings
        ....:                                 verbose=True)
        Number of pairs with difference (1) is 16, but lambda is 14
        False

    TESTS::

        sage: # needs sage.modules sage.rings.finite_rings
        sage: is_supplementary_difference_set([[1], [1]], lmbda=0, G=Zmod(3))
        True
        sage: is_supplementary_difference_set([S1, S2, S3, S4], v=17, lmbda=16, G=G)
        False
        sage: is_supplementary_difference_set([S1, S2, S3, S4], G=G)
        True
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=16)
        Traceback (most recent call last):
        ...
        ValueError: one of G or v must be specified

    .. SEEALSO::

        :func:`supplementary_difference_set_from_rel_diff_set`
    """
def supplementary_difference_set_from_rel_diff_set(q, existence: bool = False, check: bool = True):
    """
    Construct `4-\\{2v; v, v+1, v, v; 2v\\}` supplementary difference sets where `q=2v+1`.

    The sets are created from relative difference sets as detailed in Theorem 3.3 of [Spe1975]_. this construction
    requires that `q` is an odd prime power and that there exists `s \\ge 0` such that `(q-(2^{s+1}+1))/2^{s+1}` is
    an odd prime power.

    Note that the construction from [Spe1975]_ states that the resulting sets are `4-\\{2v; v+1, v, v, v; 2v\\}`
    supplementary difference sets. However, the implementation of that construction returns
    `4-\\{2v; v, v+1, v, v; 2v\\}` supplementary difference sets. This is not important, since the supplementary
    difference sets are not ordered.

    INPUT:

    - ``q`` -- an odd prime power
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the supplementary difference sets can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are supplementary difference sets before returning them

    OUTPUT:

    If ``existence=False``, the function returns the 4 sets (containing integers),
    or raises an error if ``q`` does not satisfy the constraints.
    If ``existence=True``, the function returns a boolean representing whether
    supplementary difference sets can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import supplementary_difference_set_from_rel_diff_set
        sage: supplementary_difference_set_from_rel_diff_set(17)  #random               # needs sage.libs.pari
        (Additive abelian group isomorphic to Z/16,
         [[(1), (5), (6), (7), (9), (13), (14), (15)],
          [(0), (2), (3), (5), (6), (10), (11), (13), (14)],
          [(0), (1), (2), (3), (5), (6), (7), (12)],
          [(0), (2), (3), (5), (6), (7), (9), (12)]])

    If ``existence=True``, the function returns a boolean::

        sage: supplementary_difference_set_from_rel_diff_set(7, existence=True)
        False
        sage: supplementary_difference_set_from_rel_diff_set(17, existence=True)
        True

    TESTS::

        sage: # needs sage.libs.pari
        sage: from sage.combinat.designs.difference_family import is_supplementary_difference_set
        sage: G, sets = supplementary_difference_set_from_rel_diff_set(17, check=False)
        sage: is_supplementary_difference_set(sets, lmbda=16, G=G)
        True
        sage: G, sets = supplementary_difference_set_from_rel_diff_set(9, check=False)
        sage: is_supplementary_difference_set(sets, lmbda=8, G=G)
        True
        sage: supplementary_difference_set_from_rel_diff_set(7)
        Traceback (most recent call last):
        ...
        ValueError: There is no s for which m-1 is an odd prime power
        sage: supplementary_difference_set_from_rel_diff_set(8)
        Traceback (most recent call last):
        ...
        ValueError: q must be an odd prime power
        sage: supplementary_difference_set_from_rel_diff_set(8, existence=True)
        False
        sage: supplementary_difference_set_from_rel_diff_set(7, existence=True)
        False
        sage: supplementary_difference_set_from_rel_diff_set(1, existence=True)
        False

    Check that the function works even when s > 1::

        sage: G, sets = supplementary_difference_set_from_rel_diff_set(353, check=False)  # long time, needs sage.libs.pari
        sage: is_supplementary_difference_set(sets, lmbda=352, G=G)     # long time, needs sage.libs.pari
        True

    .. SEEALSO::

        :func:`is_supplementary_difference_set`
    """
def supplementary_difference_set(q, existence: bool = False, check: bool = True):
    """
    Construct `4-\\{2v; v, v+1, v, v; 2v\\}` supplementary difference sets where `q=2v+1`.

    This is a deprecated version of :func:`supplementary_difference_set_from_rel_diff_set`,
    please use that instead.
    """
def get_fixed_relative_difference_set(G, rel_diff_set, as_elements: bool = False):
    """
    Construct an equivalent relative difference set fixed by the size of the set.

    Given a relative difference set `R(q+1, q-1, q, 1)`, it is possible to find a translation
    of this set fixed by `q` (see Section 3 of [Spe1975]_). We say that a set is fixed by `t` if
    `\\{td | d\\in R\\}= R`.

    In addition, the set returned by this function will contain the element `0`. This is needed in the
    construction of supplementary difference sets (see :func:`supplementary_difference_set_from_rel_diff_set`).

    INPUT:

    - ``G`` -- a group, of which ``rel_diff_set`` is a subset
    - ``rel_diff_set`` -- the relative difference set
    - ``as_elements`` -- boolean (default: ``False``); if ``True``, the list
      returned will contain elements of the abelian group (this may slow down
      the computation considerably)

    OUTPUT:

    By default, this function returns the set as a list of integers. However, if
    ``as_elements=True`` it will return the set as a list containing elements of
    the abelian group.
    If no such set can be found, the function will raise an error.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import relative_difference_set_from_m_sequence, get_fixed_relative_difference_set
        sage: G, s1 = relative_difference_set_from_m_sequence(5, 2, return_group=True)  # needs sage.libs.pari sage.modules
        sage: get_fixed_relative_difference_set(G, s1)  # random                        # needs sage.libs.pari sage.modules
        [2, 10, 19, 23, 0]

    If ``as_elements=True``, the result will contain elements of the group::

        sage: get_fixed_relative_difference_set(G, s1, as_elements=True)  # random      # needs sage.libs.pari sage.modules
        [(2), (10), (19), (23), (0)]

    TESTS::

        sage: # needs sage.libs.pari sage.modules
        sage: from sage.combinat.designs.difference_family import is_fixed_relative_difference_set
        sage: G, s1 = relative_difference_set_from_m_sequence(5, 2, return_group=True)
        sage: s2 = get_fixed_relative_difference_set(G, s1, as_elements=True)
        sage: is_fixed_relative_difference_set(s2, len(s2))
        True
        sage: G, s1 = relative_difference_set_from_m_sequence(9, 2, return_group=True)
        sage: s2 = get_fixed_relative_difference_set(G, s1, as_elements=True)
        sage: is_fixed_relative_difference_set(s2, len(s2))
        True
        sage: type(s2[0])
        <class 'sage.groups.additive_abelian.additive_abelian_group.AdditiveAbelianGroup_fixed_gens_with_category.element_class'>
        sage: s2 = get_fixed_relative_difference_set(G, s1)
        sage: type(s2[0])
        <class 'sage.rings.integer.Integer'>
    """
def is_fixed_relative_difference_set(R, q):
    """
    Check if the relative difference set ``R`` is fixed by ``q``.

    A relative difference set  `R` is fixed by `q` if  `\\{qd | d \\in R\\}= R` (see Section 3 of [Spe1975]_).

    INPUT:

    - ``R`` -- list containing elements of an abelian group; the relative
      difference set
    - ``q`` -- integer

    EXAMPLES::

        sage: # needs sage.modules
        sage: from sage.combinat.designs.difference_family import relative_difference_set_from_m_sequence, get_fixed_relative_difference_set, is_fixed_relative_difference_set
        sage: G, s1 = relative_difference_set_from_m_sequence(7, 2, return_group=True)  # needs sage.libs.pari
        sage: s2 = get_fixed_relative_difference_set(G, s1, as_elements=True)           # needs sage.libs.pari
        sage: is_fixed_relative_difference_set(s2, len(s2))                             # needs sage.libs.pari
        True
        sage: G = AdditiveAbelianGroup([15])
        sage: s3 = [G[1], G[2], G[3], G[4]]
        sage: is_fixed_relative_difference_set(s3, len(s3))
        False

    If the relative difference set does not contain elements of the group, the method returns false::

        sage: G, s1 = relative_difference_set_from_m_sequence(7, 2, return_group=True)  # needs sage.libs.pari sage.modules
        sage: s2 = get_fixed_relative_difference_set(G, s1, as_elements=False)          # needs sage.libs.pari sage.modules
        sage: is_fixed_relative_difference_set(s2, len(s2))                             # needs sage.libs.pari sage.modules
        False
    """
def skew_supplementary_difference_set_over_polynomial_ring(n, existence: bool = False, check: bool = True):
    """
    Construct skew supplementary difference sets over a polynomial ring of order ``n``.

    The skew supplementary difference sets for `n=81, 169` are taken from [Djo1994a]_.

    INPUT:

    - ``n`` -- integer; the parameter of the supplementary difference sets
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the supplementary difference sets can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are supplementary difference sets with `S_1` skew before returning them;
      setting this parameter to ``False`` may speed up the computation considerably

    OUTPUT:

    If ``existence=False``, the function returns a Polynomial Ring of order ``n``
    and a list containing 4 sets, or raises an error if data for the given ``n``
    is not available.
    If ``existence=True``, the function returns a boolean representing whether
    skew supplementary difference sets can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import skew_supplementary_difference_set_over_polynomial_ring
        sage: G, [S1, S2, S3, S4] = skew_supplementary_difference_set_over_polynomial_ring(81)      # needs sage.libs.pari

    If ``existence=True``, the function returns a boolean::

        sage: skew_supplementary_difference_set_over_polynomial_ring(81, existence=True)
        True
        sage: skew_supplementary_difference_set_over_polynomial_ring(17, existence=True)
        False

    TESTS::

        sage: skew_supplementary_difference_set_over_polynomial_ring(7)
        Traceback (most recent call last):
        ...
        NotImplementedError: skew SDS of order 7 not yet implemented
    """
def skew_supplementary_difference_set_with_paley_todd(n, existence: bool = False, check: bool = True):
    """
    Construct `4-\\{n; n_1, n_2, n_3, n_4; \\lambda\\}` skew supplementary difference sets where `S_1` is the Paley-Todd difference set.

    The skew SDS returned have the property that `n_1 + n_2 + n_3 + n_4 = n + \\lambda`.

    This construction is described in [DK2016]_. The function contains, for each
    value of `n`, a set `H` containing integers modulo `n`, and four sets `J, K, L`.
    Then, these are used to construct `(n; k_2, k_3, k_4; \\lambda_2)` difference family,
    with `\\lambda_2 = k_2 + k_3 + k_4 + (3n - 1) / 4`. Finally, these sets together
    with the Paley-Todd difference set form a skew supplementary difference set.

    INPUT:

    - ``n`` -- integer; the parameter of the supplementary difference set
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the supplementary difference sets can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are supplementary difference sets with `S_1` skew before returning them;
      setting this parameter to ``False`` may speed up the computation considerably

    OUTPUT:

    If ``existence=False``, the function returns the group G of integers modulo
    ``n`` and a list containing 4 sets, or raises an error if data for the given
    ``n`` is not available.
    If ``existence=True``, the function returns a boolean representing whether
    skew supplementary difference sets can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import skew_supplementary_difference_set_with_paley_todd
        sage: G, [S1, S2, S3, S4] = skew_supplementary_difference_set_with_paley_todd(239)

    If existence is ``True``, the function returns a boolean::

        sage: skew_supplementary_difference_set_with_paley_todd(239, existence=True)
        True
        sage: skew_supplementary_difference_set_with_paley_todd(17, existence=True)
        False

    TESTS::

        sage: skew_supplementary_difference_set_with_paley_todd(7)
        Traceback (most recent call last):
        ...
        NotImplementedError: data for skew SDS of order 7 not yet implemented
    """
def spin_goethals_seidel_difference_family(n, existence: bool = False, check: bool = True):
    """
    Construct a spin type Goethals-Seidel difference family with parameters
    `(n; k_1, k_2, k_3, k_4; \\lambda)`.

    The construction is described in [Djo2024]_. This function contains, for
    each value of `n`, either a full representation of `S_1, S_2` together with
    the multiplier `\\mu`, or a subgroup `H`, two sets of representatives, and the
    multiplier.
    This data is used to construct the difference family using the functions
    :func:`_construct_gs_difference_family_from_full` and
    :func:`_construct_gs_difference_family_from_compact`.

    Additionally, this function also checks if a (skew) difference family can be
    constructed using :func:`skew_spin_goethals_seidel_difference_family`.

    INPUT:

    - ``n`` -- integer; the parameter of the GS difference family
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the difference family can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are a difference family before returning them;
      setting this parameter to ``False`` may speed up the computation considerably

    OUTPUT:

    If ``existence=False``, the function returns the group G of integers modulo
    ``n`` and a list containing 4 sets, or raises an error if data for the given
    ``n`` is not available.
    If ``existence=True``, the function returns a boolean representing whether
    the difference family can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import spin_goethals_seidel_difference_family
        sage: G, [S1, S2, S3, S4] = spin_goethals_seidel_difference_family(73)

    If existence is ``True``, the function returns a boolean::

        sage: spin_goethals_seidel_difference_family(73, existence=True)
        True
        sage: spin_goethals_seidel_difference_family(5, existence=True)
        False

    TESTS::

        sage: from sage.combinat.designs.difference_family import is_supplementary_difference_set
        sage: G, [S1, S2, S3, S4] = spin_goethals_seidel_difference_family(9, check=False)
        sage: lmbda = len(S1) + len(S2) + len(S3) + len(S4) - 9
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=lmbda, G=G)
        True
        sage: spin_goethals_seidel_difference_family(5)
        Traceback (most recent call last):
        ...
        NotImplementedError: Data for spin type Goethals Seidel family of order 5 not yet implemented
    """
def skew_spin_goethals_seidel_difference_family(n, existence: bool = False, check: bool = True):
    """
    Construct skew spin type Goethals-Seidel difference family with parameters
    `(n; k_1, k_2, k_3, k_4; \\lambda)`.

    The construction is described in [Djo2024]_. This function contains, for
    each value of `n`, either a full representation of `S_1, S_2` together with
    the multiplier `\\mu`, or a subgroup `H`, two sets of representatives, and the
    multiplier.

    This data is used to construct the difference family using the functions
    :func:`_construct_gs_difference_family_from_full` and
    :func:`_construct_gs_difference_family_from_compact`.

    INPUT:

    - ``n`` -- integer; the parameter of the GS difference family
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the skew difference family can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are a skew difference family before returning them;
      setting this parameter to ``False`` may speed up the computation considerably

    OUTPUT:

    If ``existence=False``, the function returns the group G of integers modulo
    ``n`` and a list containing 4 sets, or raises an error if data for the given
    ``n`` is not available.
    If ``existence=True``, the function returns a boolean representing whether
    the skew difference family can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import skew_spin_goethals_seidel_difference_family
        sage: G, [S1, S2, S3, S4] = skew_spin_goethals_seidel_difference_family(61)

    If existence is ``True``, the function returns a boolean::

        sage: skew_spin_goethals_seidel_difference_family(61, existence=True)
        True
        sage: skew_spin_goethals_seidel_difference_family(5, existence=True)
        False

    TESTS::
        sage: from sage.combinat.designs.difference_family import is_supplementary_difference_set, _is_skew_set
        sage: G, [S1, S2, S3, S4] = skew_spin_goethals_seidel_difference_family(7, check=False)
        sage: lmbda = len(S1) + len(S2) + len(S3) + len(S4) - 7
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=lmbda, G=G)
        True
        sage: _is_skew_set(G, S1)
        True
        sage: skew_spin_goethals_seidel_difference_family(5)
        Traceback (most recent call last):
        ...
        NotImplementedError: Data for skew spin type Goethals Seidel family of order 5 not yet implemented
    """
def skew_supplementary_difference_set(n, existence: bool = False, check: bool = True, return_group: bool = False):
    """
    Construct `4-\\{n; n_1, n_2, n_3, n_4; \\lambda\\}` supplementary difference sets,
    where `S_1` is skew and `n_1 + n_2 + n_3 + n_4 = n+\\lambda`.

    These sets are constructed from available data, as described in [Djo1994a]_. The set `S_1 \\subset G` is
    always skew, i.e. `S_1 \\cap (-S_1) = \\emptyset` and `S_1 \\cup (-S_1) = G \\setminus \\{0\\}`.

    The data is taken from:

    * `n = 103, 151`: [Djo1994a]_
    * `n = 67, 113, 127, 157, 163, 181, 241`: [Djo1992a]_
    * `n = 37, 43`: [Djo1992b]_
    * `n = 39, 49, 65, 93, 121, 129, 133, 217, 219, 267`: [Djo1992c]_
    * `n = 97`: [Djo2008a]_
    * `n = 109, 145, 247`: [Djo2008b]_
    * `n = 73`: [Djo2023b]_
    * `n = 213, 631`: [DGK2014]_
    * `n = 331`: [DK2016]_

    Additional skew Supplementary difference sets are built using the function
    :func:`skew_supplementary_difference_set_over_polynomial_ring`, and
    :func:`skew_supplementary_difference_set_with_paley_todd`.

    INPUT:

    - ``n`` -- integer; the parameter of the supplementary difference set
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the supplementary difference sets can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are supplementary difference sets with `S_1` skew before returning them;
      setting this parameter to ``False`` may speed up the computation considerably
    - ``return_group`` -- boolean (default: ``False``); if ``True``, the function
      will also return the group from which the sets are created

    OUTPUT:

    If ``existence=False``, the function returns a list containing 4 sets,
    or raises an error if data for the given ``n`` is not available. If
    ``return_group=True`` the function will additionally return the group from
    which the sets are created.
    If ``existence=True``, the function returns a boolean representing whether
    skew supplementary difference sets can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import skew_supplementary_difference_set
        sage: [S1, S2, S3, S4] = skew_supplementary_difference_set(39)

    If ``return_group=True``, the function will also return the group::

        sage: G, [S1, S2, S3, S4] = skew_supplementary_difference_set(103, return_group=True)

    If ``existence=True``, the function returns a boolean::

        sage: skew_supplementary_difference_set(103, existence=True)
        True
        sage: skew_supplementary_difference_set(17, existence=True)
        False

    TESTS::

        sage: from sage.combinat.designs.difference_family import is_supplementary_difference_set, _is_skew_set
        sage: G, [S1, S2, S3, S4] = skew_supplementary_difference_set(113, check=False, return_group=True)
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=len(S1)+len(S2)+len(S3)+len(S4)-113, G=G)
        True
        sage: _is_skew_set(G, S1)
        True
        sage: G, [S1, S2, S3, S4] = skew_supplementary_difference_set(67, check=False, return_group=True)
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=len(S1)+len(S2)+len(S3)+len(S4)-67, G=G)
        True
        sage: _is_skew_set(G, S1)
        True
        sage: skew_supplementary_difference_set(17)
        Traceback (most recent call last):
        ...
        ValueError: Skew SDS of order 17 not yet implemented.
        sage: skew_supplementary_difference_set(17, existence=True)
        False
        sage: skew_supplementary_difference_set(127, existence=True)
        True
        sage: skew_supplementary_difference_set(81, existence=True)
        True

    .. NOTE::

        The data for `n=247` in [Djo2008b]_ contains a typo: the set `\\alpha_2` should contain `223` instead of `233`.
        This can be verified by checking the resulting sets, which are given explicitly in the paper.
    """
def supplementary_difference_set_hadamard(n, existence: bool = False, check: bool = True):
    """
    Construct `4-\\{n; n_1, n_2, n_3, n_4; \\lambda\\}` supplementary difference sets,
    where `n_1 + n_2 + n_3 + n_4 = n+\\lambda`.

    These sets are constructed from available data, as described in [Djo1994a]_.
    The data is taken from:

    * `n = 191`: [Djo2008c]_
    * `n = 239`: [Djo1994b]_
    * `n = 251`: [DGK2014]_

    Additional SDS are constructed using :func:`skew_supplementary_difference_set`.

    INPUT:

    - ``n`` -- integer; the parameter of the supplementary difference set
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the supplementary difference sets can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are supplementary difference sets before returning them; Setting this
      parameter to ``False`` may speed up the computation considerably

    OUTPUT:

    If ``existence=False``, the function returns the ring of integers modulo
    ``n`` and a list containing the 4 sets, or raises an error if data for the
    given ``n`` is not available.
    If ``existence=True``, the function returns a boolean representing whether
    skew supplementary difference sets can be constructed.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import supplementary_difference_set_hadamard
        sage: G, [S1, S2, S3, S4] = supplementary_difference_set_hadamard(191)

    If ``existence=True``, the function returns a boolean::

        sage: supplementary_difference_set_hadamard(191, existence=True)
        True
        sage: supplementary_difference_set_hadamard(17, existence=True)
        False

    TESTS::

        sage: from sage.combinat.designs.difference_family import is_supplementary_difference_set
        sage: G, [S1, S2, S3, S4] = supplementary_difference_set_hadamard(191, check=False)
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=len(S1)+len(S2)+len(S3)+len(S4)-191, G=G)
        True
        sage: G, [S1, S2, S3, S4] = supplementary_difference_set_hadamard(37, check=False)
        sage: is_supplementary_difference_set([S1, S2, S3, S4], lmbda=len(S1)+len(S2)+len(S3)+len(S4)-37, G=G)
        True
        sage: supplementary_difference_set_hadamard(11)
        Traceback (most recent call last):
        ...
        ValueError: SDS of order 11 not yet implemented.
        sage: supplementary_difference_set_hadamard(11, existence=True)
        False
        sage: supplementary_difference_set_hadamard(127, existence=True)
        True
    """
def are_complementary_difference_sets(G, A, B, verbose: bool = False):
    """
    Check if ``A`` and ``B`` are complementary difference sets over the group ``G``.

    According to [Sze1971]_, two sets `A`, `B` of size `m` are complementary
    difference sets over a group `G` of size `2m+1` if:

    1. they are `2-\\{2m+1; m, m; m-1\\}` supplementary difference sets
    2. `A` is skew, i.e. `a \\in A` implies `-a \\not \\in A`

    INPUT:

    - ``G`` -- a group of odd order
    - ``A`` -- set of elements of ``G``
    - ``B`` -- set of elements of ``G``
    - ``verbose`` -- boolean (default: ``False``); if ``True`` the function will
      be verbose when the sets do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import are_complementary_difference_sets
        sage: are_complementary_difference_sets(Zmod(7), [1, 2, 4], [1, 2, 4])
        True

    If ``verbose=True``, the function will be verbose::

        sage: are_complementary_difference_sets(Zmod(7), [1, 2, 5], [1, 2, 4], verbose=True)
        The sets are not supplementary difference sets with lambda = 2
        False

    TESTS::

        sage: are_complementary_difference_sets(Zmod(16), [1, 2, 4], [1, 2, 4])
        False
        sage: are_complementary_difference_sets(Zmod(7), [1, 2, 4], [1, 2, 3, 4])
        False
        sage: are_complementary_difference_sets(Zmod(19), [1, 4, 5, 6, 7, 9, 11, 16, 17], [1, 4, 5, 6, 7, 9, 11, 16, 17])
        True

    .. SEEALSO::

        :func:`is_supplementary_difference_set`
    """
def complementary_difference_setsI(n, check: bool = True):
    """
    Construct complementary difference sets in a group of order `n \\cong 3 \\mod 4`, `n` a prime power.

    Let `G` be a Galois Field of order `n`, where `n` satisfies the requirements
    above. Let `A` be the set of nonzero quadratic elements in `G`, and `B = A`.
    Then `A` and `B` are complementary difference sets over a group of order `n`.
    This construction is described in [Sze1971]_.

    INPUT:

    - ``n`` -- integer; the order of the group `G`
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are complementary difference sets before returning them

    OUTPUT:

    The function returns the Galois field of order ``n`` and the two sets, or raises
    an error if ``n`` does not satisfy the requirements of this construction.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import complementary_difference_setsI
        sage: complementary_difference_setsI(19)
        (Finite Field of size 19,
         [1, 4, 5, 6, 7, 9, 11, 16, 17],
         [1, 4, 5, 6, 7, 9, 11, 16, 17])

    TESTS::

        sage: from sage.combinat.designs.difference_family import are_complementary_difference_sets
        sage: G, A, B = complementary_difference_setsI(23, check=False)
        sage: are_complementary_difference_sets(G, A, B)
        True
        sage: complementary_difference_setsI(17)
        Traceback (most recent call last):
        ...
        ValueError: the parameter 17 is not valid
        sage: complementary_difference_setsI(15)                                        # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        ValueError: the parameter 15 is not valid

    .. SEEALSO::

        :func:`are_complementary_difference_sets`
        :func:`complementary_difference_sets`
    """
def complementary_difference_setsII(n, check: bool = True):
    """
    Construct complementary difference sets in a group of order `n = p^t`, where `p \\cong 5 \\mod 8` and `t \\cong 1, 2, 3 \\mod 4`.

    Consider a finite field `G` of order `n` and let `\\rho` be the generator of
    the corresponding multiplicative group. Then, there are two different constructions,
    depending on whether `t` is even or odd.

    If `t \\cong 2 \\mod 4`, let `C_0` be the set of nonzero octic residues in `G`,
    and let `C_i = \\rho^i C_0` for `1 \\le i \\le  7`.
    Then, `A = C_0 \\cup C_1 \\cup C_2 \\cup C_3` and  `B = C_0 \\cup C_1 \\cup C_6 \\cup C_7`.

    If `t` is odd, let `C_0` be the set of nonzero fourth powers in `G`, and let
    `C_i = \\rho^i C_0` for `1 \\le i \\le  3`.
    Then, `A = C_0 \\cup C_1` and  `B = C_0 \\cup C_3`.

    For more details on this construction, see [Sze1971]_.

    INPUT:

    - ``n`` -- integer; the order of the group `G`
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are complementary difference sets before returning them; setting this to
      ``False`` might speed up the computation for large values of ``n``

    OUTPUT:

    The function returns the Galois field of order ``n`` and the two sets, or raises
    an error if ``n`` does not satisfy the requirements of this construction.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import complementary_difference_setsII
        sage: complementary_difference_setsII(5)                                        # needs sage.libs.pari
        (Finite Field of size 5, [1, 2], [1, 3])

    TESTS::

        sage: # needs sage.libs.pari
        sage: from sage.combinat.designs.difference_family import are_complementary_difference_sets
        sage: G, A, B = complementary_difference_setsII(25, check=False)
        sage: are_complementary_difference_sets(G, A, B)
        True
        sage: G, A, B = complementary_difference_setsII(13, check=False)
        sage: are_complementary_difference_sets(G, A, B)
        True
        sage: complementary_difference_setsII(49)
        Traceback (most recent call last):
        ...
        ValueError: the parameter 49 is not valid
        sage: complementary_difference_setsII(15)
        Traceback (most recent call last):
        ...
        ValueError: the parameter 15 is not valid

    .. SEEALSO::

        :func:`are_complementary_difference_sets`
        :func:`complementary_difference_sets`
    """
def complementary_difference_setsIII(n, check: bool = True):
    """
    Construct complementary difference sets in a group of order `n = 2m + 1`, where `4m + 3` is a prime power.

    Consider a finite field `G` of order `n` and let `\\rho` be a primite element
    of this group. Now let `Q` be the set of nonzero quadratic residues in `G`,
    and let `A = \\{ a | \\rho^{2a} - 1 \\in Q\\}`, `B' = \\{ b | -(\\rho^{2b} + 1) \\in Q\\}`.
    Then `A` and `B = Q \\setminus B'` are complementary difference sets over the ring
    of integers modulo `n`. For more details, see [Sz1969]_.

    INPUT:

    - ``n`` -- integer; the order of the group over which the sets are constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are complementary difference sets before returning them; setting this to
      ``False`` might speed up the computation for large values of ``n``

    OUTPUT:

    The function returns the Galois field of order ``n`` and the two sets, or raises
    an error if ``n`` does not satisfy the requirements of this construction.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import complementary_difference_setsIII
        sage: complementary_difference_setsIII(11)                                      # needs sage.libs.pari
        (Ring of integers modulo 11, [1, 2, 5, 7, 8], [0, 1, 3, 8, 10])

    TESTS::

        sage: from sage.combinat.designs.difference_family import are_complementary_difference_sets
        sage: G, A, B = complementary_difference_setsIII(21, check=False)               # needs sage.libs.pari
        sage: are_complementary_difference_sets(G, A, B)                                # needs sage.libs.pari
        True
        sage: G, A, B = complementary_difference_setsIII(65, check=False)               # needs sage.libs.pari
        sage: are_complementary_difference_sets(G, A, B)                                # needs sage.libs.pari
        True
        sage: complementary_difference_setsIII(10)
        Traceback (most recent call last):
        ...
        ValueError: the parameter 10 is not valid
        sage: complementary_difference_setsIII(17)                                      # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        ValueError: the parameter 17 is not valid

    .. SEEALSO::

        :func:`are_complementary_difference_sets`
        :func:`complementary_difference_sets`
    """
def complementary_difference_sets(n, existence: bool = False, check: bool = True):
    """
    Compute complementary difference sets over a group of order `n = 2m + 1`.

    According to [Sze1971]_, two sets `A`, `B` of size `m` are complementary
    difference sets over a group `G` of size `n = 2m + 1` if:

    1. they are `2-\\{2m+1; m, m; m-1\\}` supplementary difference sets
    2. `A` is skew, i.e. `a \\in A` implies `-a \\not \\in A`

    This method tries to call :func:`complementary_difference_setsI`,
    :func:`complementary_difference_setsII` or :func:`complementary_difference_setsIII`
    if the parameter `n` satisfies the requirements of one of these functions.

    INPUT:

    - ``n`` -- integer; the order of the group over which the sets are constructed
    - ``existence`` -- boolean (default: ``False``); if ``True``, only check
      whether the supplementary difference sets can be constructed
    - ``check`` -- boolean (default: ``True``); if ``True``, check that the sets
      are complementary difference sets before returning them; setting this to
      ``False`` might speed up the computation for large values of ``n``

    OUTPUT:

    If ``existence=False``, the function returns group ``G`` and two complementary
    difference sets, or raises an error if data for the given ``n`` is not available.
    If ``existence=True``, the function returns a boolean representing whether
    complementary difference sets can be constructed for the given ``n``.

    EXAMPLES::

        sage: from sage.combinat.designs.difference_family import complementary_difference_sets
        sage: complementary_difference_sets(15)                                         # needs sage.libs.pari
        (Ring of integers modulo 15, [1, 2, 4, 6, 7, 10, 12], [0, 1, 2, 6, 9, 13, 14])

    If ``existence=True``, the function returns a boolean::

        sage: complementary_difference_sets(15, existence=True)                         # needs sage.libs.pari
        True
        sage: complementary_difference_sets(16, existence=True)
        False

    TESTS::

        sage: from sage.combinat.designs.difference_family import are_complementary_difference_sets
        sage: G, A, B = complementary_difference_sets(29)                               # needs sage.libs.pari
        sage: are_complementary_difference_sets(G, A, B)                                # needs sage.libs.pari
        True
        sage: G, A, B = complementary_difference_sets(65)                               # needs sage.libs.pari
        sage: are_complementary_difference_sets(G, A, B)                                # needs sage.libs.pari
        True
        sage: complementary_difference_sets(10)
        Traceback (most recent call last):
        ...
        ValueError: the parameter n must be odd
        sage: complementary_difference_sets(17)                                         # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        NotImplementedError: complementary difference sets of order 17 are not implemented yet

    .. SEEALSO::

        :func:`are_complementary_difference_sets`
    """
def difference_family(v, k, l: int = 1, existence: bool = False, explain_construction: bool = False, check: bool = True):
    '''
    Return a (``k``, ``l``)-difference family on an Abelian group of cardinality ``v``.

    Let `G` be a finite Abelian group. For a given subset `D` of `G`, we define
    `\\Delta D` to be the multi-set of differences `\\Delta D = \\{x - y; x \\in D,
    y \\in D, x \\not= y\\}`. A `(G,k,\\lambda)`-*difference family* is a collection
    of `k`-subsets of `G`, `D = \\{D_1, D_2, \\ldots, D_b\\}` such that the union
    of the difference sets `\\Delta D_i` for `i=1,...b`, seen as a multi-set,
    contains each element of `G \\backslash \\{0\\}` exactly `\\lambda`-times.

    When there is only one block, i.e. `\\lambda(v - 1) = k(k-1)`, then a
    `(G,k,\\lambda)`-difference family is also called a *difference set*.

    See also :wikipedia:`Difference_set`.

    If there is no such difference family, an :exc:`EmptySetError` is raised and
    if there is no construction at the moment :exc:`NotImplementedError`
    is raised.

    INPUT:

    - ``v``, ``k``, ``l`` -- parameters of the difference family. If ``l`` is
      not provided it is assumed to be ``1``
    - ``existence`` -- if ``True``, then return either ``True`` if Sage knows
      how to build such design, ``Unknown`` if it does not and ``False`` if it
      knows that the design does not exist
    - ``explain_construction`` -- instead of returning a difference family,
      returns a string that explains the construction used
    - ``check`` -- boolean (default: ``True``); if ``True``, then the result of
      the computation is checked before being returned. This should not be
      needed but ensures that the output is correct

    OUTPUT:

    A pair ``(G,D)`` made of a group `G` and a difference family `D` on that
    group. Or, if ``existence=True`` a troolean or if
    ``explain_construction=True`` a string.

    EXAMPLES::

        sage: G,D = designs.difference_family(73,4)                                     # needs sage.libs.pari
        sage: G                                                                         # needs sage.libs.pari
        Finite Field of size 73
        sage: D                                                                         # needs sage.libs.pari
        [[0, 1, 5, 18],
         [0, 3, 15, 54],
         [0, 9, 45, 16],
         [0, 27, 62, 48],
         [0, 8, 40, 71],
         [0, 24, 47, 67]]

        sage: print(designs.difference_family(73, 4, explain_construction=True))
        The database contains a (73,4)-evenly distributed set

        sage: # needs sage.libs.pari
        sage: G,D = designs.difference_family(15,7,3)
        sage: G
        Ring of integers modulo 15
        sage: D
        [[0, 1, 2, 4, 5, 8, 10]]
        sage: print(designs.difference_family(15,7,3,explain_construction=True))
        Singer difference set

        sage: # needs sage.libs.pari
        sage: print(designs.difference_family(91,10,1,explain_construction=True))
        Singer difference set
        sage: print(designs.difference_family(64,28,12, explain_construction=True))
        McFarland 1973 construction
        sage: print(designs.difference_family(576, 276, 132, explain_construction=True))
        Hadamard difference set product from N1=2 and N2=3

    For `k=6,7` we look at the set of small prime powers for which a
    construction is available::

        sage: def prime_power_mod(r, m):
        ....:     k = m+r
        ....:     while True:
        ....:         if is_prime_power(k):
        ....:             yield k
        ....:         k += m

        sage: # needs sage.libs.pari
        sage: from itertools import islice
        sage: l6 = {True: [], False: [], Unknown: []}
        sage: for q in islice(prime_power_mod(1,30), int(60)):
        ....:     l6[designs.difference_family(q,6,existence=True)].append(q)
        sage: l6[True]
        [31, 121, 151, 181, 211, ...,  3061, 3121, 3181]
        sage: l6[Unknown]
        [61]
        sage: l6[False]
        []

        sage: # needs sage.libs.pari
        sage: l7 = {True: [], False: [], Unknown: []}
        sage: for q in islice(prime_power_mod(1,42), int(60)):
        ....:     l7[designs.difference_family(q,7,existence=True)].append(q)
        sage: l7[True]
        [169, 337, 379, 421, 463, 547, 631, 673, 757, 841, 883, 967, ...,  4621, 4957, 5167]
        sage: l7[Unknown]
        [43, 127, 211, 2017, 2143, 2269, 2311, 2437, 2521, 2647, ..., 4999, 5041, 5209]
        sage: l7[False]
        []

    List available constructions::

        sage: for v in range(2,100):                                                    # needs sage.libs.pari
        ....:     constructions = []
        ....:     for k in range(2,10):
        ....:         for l in range(1,10):
        ....:             ret = designs.difference_family(v,k,l,existence=True)
        ....:             if ret is True:
        ....:                 constructions.append((k,l))
        ....:                 _ = designs.difference_family(v,k,l)
        ....:     if constructions:
        ....:         print("%2d: %s"%(v, \', \'.join(\'(%d,%d)\'%(k,l) for k,l in constructions)))
         3: (2,1)
         4: (3,2)
         5: (2,1), (4,3)
         6: (5,4)
         7: (2,1), (3,1), (3,2), (4,2), (6,5)
         8: (7,6)
         9: (2,1), (4,3), (8,7)
        10: (9,8)
        11: (2,1), (4,6), (5,2), (5,4), (6,3)
        13: (2,1), (3,1), (3,2), (4,1), (4,3), (5,5), (6,5)
        15: (3,1), (4,6), (5,6), (7,3), (7,6)
        16: (3,2), (5,4), (6,2)
        17: (2,1), (4,3), (5,5), (8,7)
        19: (2,1), (3,1), (3,2), (4,2), (6,5), (9,4), (9,8)
        21: (3,1), (4,3), (5,1), (6,3), (6,5)
        22: (4,2), (6,5), (7,4), (8,8)
        23: (2,1)
        25: (2,1), (3,1), (3,2), (4,1), (4,3), (6,5), (7,7), (8,7)
        27: (2,1), (3,1)
        28: (3,2), (6,5)
        29: (2,1), (4,3), (7,3), (7,6), (8,4), (8,6)
        31: (2,1), (3,1), (3,2), (4,2), (5,2), (5,4), (6,1), (6,5)
        33: (3,1), (5,5), (6,5)
        34: (4,2)
        35: (5,2)
        37: (2,1), (3,1), (3,2), (4,1), (4,3), (6,5), (9,2), (9,8)
        39: (3,1), (6,5)
        40: (3,2), (4,1)
        41: (2,1), (4,3), (5,1), (5,4), (6,3), (8,7)
        43: (2,1), (3,1), (3,2), (4,2), (6,5), (7,2), (7,3), (7,6), (8,4)
        45: (3,1), (5,1)
        46: (4,2), (6,2)
        47: (2,1)
        49: (2,1), (3,1), (3,2), (4,1), (4,3), (6,5), (8,7), (9,3)
        51: (3,1), (5,2), (6,3)
        52: (4,1)
        53: (2,1), (4,3)
        55: (3,1), (9,4)
        57: (3,1), (7,3), (8,1)
        59: (2,1)
        61: (2,1), (3,1), (3,2), (4,1), (4,3), (5,1), (5,4), (6,2), (6,3), (6,5)
        63: (3,1)
        64: (3,2), (4,1), (7,2), (7,6), (9,8)
        65: (5,1)
        67: (2,1), (3,1), (3,2), (6,5)
        69: (3,1)
        71: (2,1), (5,2), (5,4), (7,3), (7,6), (8,4)
        73: (2,1), (3,1), (3,2), (4,1), (4,3), (6,5), (8,7), (9,1), (9,8)
        75: (3,1), (5,2)
        76: (4,1)
        79: (2,1), (3,1), (3,2), (6,5)
        81: (2,1), (3,1), (4,3), (5,1), (5,4), (8,7)
        83: (2,1)
        85: (4,1), (7,2), (7,3), (8,2)
        89: (2,1), (4,3), (8,7)
        91: (6,1), (7,1)
        97: (2,1), (3,1), (3,2), (4,1), (4,3), (6,5), (8,7), (9,3)

    TESTS:

    Check more of the Wilson constructions from [Wi72]_::

        sage: Q5 = [241, 281,421,601,641, 661, 701, 821,881]
        sage: Q9 = [73, 1153, 1873, 2017]
        sage: Q15 = [76231]
        sage: Q4 = [13, 73, 97, 109, 181, 229, 241, 277, 337, 409, 421, 457]
        sage: Q8 = [1009, 3137, 3697]
        sage: for Q,k in [(Q4,4),(Q5,5),(Q8,8),(Q9,9),(Q15,15)]:                        # needs sage.libs.pari
        ....:     for q in Q:
        ....:         assert designs.difference_family(q,k,1,existence=True) is True
        ....:         _ = designs.difference_family(q,k,1)

    Check Singer difference sets::

        sage: sgp = lambda q,d: ((q**(d+1)-1)//(q-1), (q**d-1)//(q-1), (q**(d-1)-1)//(q-1))

        sage: for q in range(2,10):                                                     # needs sage.libs.pari
        ....:     if is_prime_power(q):
        ....:         for d in [2,3,4]:
        ....:           v,k,l = sgp(q,d)
        ....:           assert designs.difference_family(v,k,l,existence=True) is True
        ....:           _ = designs.difference_family(v,k,l)

    Check twin primes difference sets::

        sage: for p in [3,5,7,9,11]:                                                    # needs sage.libs.pari
        ....:     v = p*(p+2); k = (v-1)/2;  lmbda = (k-1)/2
        ....:     G,D = designs.difference_family(v,k,lmbda)

    Check Complementary difference sets::

        sage: for v in [15, 33, 35, 39, 51]:                                            # needs sage.libs.pari
        ....:     G, D = designs.difference_family(v, (v-1)//2, (v-1)//2-1)

    Check the database::

        sage: from sage.combinat.designs.database import DF,EDS
        sage: for v,k,l in DF:
        ....:     assert designs.difference_family(v,k,l,existence=True) is True
        ....:     df = designs.difference_family(v,k,l,check=True)

        sage: for k in EDS:                                                             # needs sage.libs.pari
        ....:     for v in EDS[k]:
        ....:         assert designs.difference_family(v,k,1,existence=True) is True
        ....:         df = designs.difference_family(v,k,1,check=True)

    Check the known Hadamard parameters::

        sage: for N in range(2,21):                                                     # needs sage.libs.pari
        ....:     v = 4*N^2; k = 2*N^2-N; l = N^2-N
        ....:     status = designs.difference_family(v,k,l,existence=True)
        ....:     print("{:2} {}".format(N,designs.difference_family(v,k,l,explain_construction=True) if status is True else status))
        2 McFarland 1973 construction
        3 Turyn 1965 construction
        4 McFarland 1973 construction
        5 False
        6 The database contains a (144,66,30)-difference family
        7 False
        8 McFarland 1973 construction
        9 Unknown
        10 Unknown
        11 False
        12 Hadamard difference set product from N1=2 and N2=3
        13 False
        14 Unknown
        15 Unknown
        16 McFarland 1973 construction
        17 False
        18 Hadamard difference set product from N1=3 and N2=3
        19 False
        20 Unknown

    Check a failing construction (:issue:`17528`)::

        sage: designs.difference_family(9,3)
        Traceback (most recent call last):
        ...
        NotImplementedError: No construction available for (9,3,1)-difference family

    Check that when ``existence=True`` we always obtain ``True``, ``False`` or ``Unknown``,
    and when ``explain_construction=True``, it is a string (see :issue:`24513`)::

        sage: designs.difference_family(3, 2, 1, existence=True)
        True
        sage: designs.difference_family(3, 2, 1, explain_construction=True)
        \'Trivial difference family\'

        sage: for _ in range(100):                                                      # needs sage.libs.pari
        ....:     v = randint(1, 30)
        ....:     k = randint(2, 30)
        ....:     l = randint(1, 30)
        ....:     res = designs.difference_family(v, k, l, existence=True)
        ....:     assert res is True or res is False or res is Unknown
        ....:     if res is True:
        ....:         assert isinstance(designs.difference_family(3, 2, 1, explain_construction=True), str)

    .. TODO::

        Implement recursive constructions from Buratti "Recursive for difference
        matrices and relative difference families" (1998) and Jungnickel
        "Composition theorems for difference families and regular planes" (1978)
    '''

__doc__: Incomplete
