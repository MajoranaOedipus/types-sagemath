from .designs_pyx import is_orthogonal_array as is_orthogonal_array
from .group_divisible_designs import GroupDivisibleDesign as GroupDivisibleDesign
from _typeshed import Incomplete
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.misc.unknown import Unknown as Unknown

def transversal_design(k, n, resolvable: bool = False, check: bool = True, existence: bool = False):
    '''
    Return a transversal design of parameters `k,n`.

    A transversal design of parameters `k, n` is a collection `\\mathcal{S}` of
    subsets of `V = V_1 \\cup \\cdots \\cup V_k` (where the *groups* `V_i` are
    disjoint and have cardinality `n`) such that:

    * Any `S \\in \\mathcal{S}` has cardinality `k` and intersects each group on
      exactly one element.

    * Any two elements from distincts groups are contained in exactly one
      element of `\\mathcal{S}`.

    More general definitions sometimes involve a `\\lambda` parameter, and we
    assume here that `\\lambda=1`.

    For more information on transversal designs, see
    `<http://mathworld.wolfram.com/TransversalDesign.html>`_.

    INPUT:

    - ``n``, ``k`` -- integers; if ``k is None`` it is set to the largest value
      available

    - ``resolvable`` -- boolean; set to ``True`` if you want the design to be
      resolvable (see
      :meth:`sage.combinat.designs.incidence_structures.IncidenceStructure.is_resolvable`). The
      `n` classes of the resolvable design are obtained as the first `n` blocks,
      then the next `n` blocks, etc ... Set to ``False`` by default.

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
          integer, i.e. the largest `k` such that we can build a `TD(k,n)`.

    OUTPUT: the kind of output depends on the input:

    - if ``existence=False`` (the default) then the output is a list of lists
      that represent a `TD(k,n)` with
      `V_1=\\{0,\\dots,n-1\\},\\dots,V_k=\\{(k-1)n,\\dots,kn-1\\}`

    - if ``existence=True`` and ``k`` is an integer, then the function returns a
      troolean: either ``True``, ``Unknown`` or ``False``

    - if ``existence=True`` and ``k=None`` then the output is the largest value
      of ``k`` for which Sage knows how to compute a `TD(k,n)`.

    .. SEEALSO::

        :func:`orthogonal_array` -- a transversal design `TD(k,n)` is equivalent to an
        orthogonal array `OA(k,n,2)`.

    EXAMPLES::

        sage: TD = designs.transversal_design(5,5); TD
        Transversal Design TD(5,5)
        sage: TD.blocks()
        [[0, 5, 10, 15, 20], [0, 6, 12, 18, 24], [0, 7, 14, 16, 23],
         [0, 8, 11, 19, 22], [0, 9, 13, 17, 21], [1, 5, 14, 18, 22],
         [1, 6, 11, 16, 21], [1, 7, 13, 19, 20], [1, 8, 10, 17, 24],
         [1, 9, 12, 15, 23], [2, 5, 13, 16, 24], [2, 6, 10, 19, 23],
         [2, 7, 12, 17, 22], [2, 8, 14, 15, 21], [2, 9, 11, 18, 20],
         [3, 5, 12, 19, 21], [3, 6, 14, 17, 20], [3, 7, 11, 15, 24],
         [3, 8, 13, 18, 23], [3, 9, 10, 16, 22], [4, 5, 11, 17, 23],
         [4, 6, 13, 15, 22], [4, 7, 10, 18, 21], [4, 8, 12, 16, 20],
         [4, 9, 14, 19, 24]]

    Some examples of the maximal number of transversal Sage is able to build::

        sage: TD_4_10 = designs.transversal_design(4,10)
        sage: designs.transversal_design(5,10,existence=True)
        Unknown

    For prime powers, there is an explicit construction which gives a
    `TD(n+1,n)`::

        sage: designs.transversal_design(4, 3, existence=True)
        True
        sage: designs.transversal_design(674, 673, existence=True)
        True

    For other values of ``n`` it depends::

        sage: designs.transversal_design(7, 6, existence=True)
        False
        sage: designs.transversal_design(4, 6, existence=True)
        Unknown
        sage: designs.transversal_design(3, 6, existence=True)
        True

        sage: designs.transversal_design(11, 10, existence=True)
        False
        sage: designs.transversal_design(4, 10, existence=True)
        True
        sage: designs.transversal_design(5, 10, existence=True)
        Unknown

        sage: designs.transversal_design(7, 20, existence=True)
        Unknown
        sage: designs.transversal_design(6, 12, existence=True)
        True
        sage: designs.transversal_design(7, 12, existence=True)
        True
        sage: designs.transversal_design(8, 12, existence=True)
        Unknown

        sage: designs.transversal_design(6, 20, existence = True)
        True
        sage: designs.transversal_design(7, 20, existence = True)
        Unknown

    If you ask for a transversal design that Sage is not able to build then an
    :exc:`EmptySetError` or a :exc:`NotImplementedError` is raised::

        sage: designs.transversal_design(47, 100)
        Traceback (most recent call last):
        ...
        NotImplementedError: I don\'t know how to build a TD(47,100)!
        sage: designs.transversal_design(55, 54)
        Traceback (most recent call last):
        ...
        EmptySetError: There exists no TD(55,54)!

    Those two errors correspond respectively to the cases where Sage answer
    ``Unknown`` or ``False`` when the parameter ``existence`` is set to
    ``True``::

        sage: designs.transversal_design(47, 100, existence=True)
        Unknown
        sage: designs.transversal_design(55, 54, existence=True)
        False

    If for a given `n` you want to know the largest `k` for which Sage is able
    to build a `TD(k,n)` just call the function with `k` set to ``None`` and
    ``existence`` set to ``True`` as follows::

        sage: designs.transversal_design(None, 6, existence=True)
        3
        sage: designs.transversal_design(None, 20, existence=True)
        6
        sage: designs.transversal_design(None, 30, existence=True)
        6
        sage: designs.transversal_design(None, 120, existence=True)
        9

    TESTS:

    The case when `n=1`::

        sage: designs.transversal_design(5,1).blocks()
        [[0, 1, 2, 3, 4]]

    Obtained through Wilson\'s decomposition::

        sage: _ = designs.transversal_design(4,38)

    Obtained through product decomposition::

        sage: _ = designs.transversal_design(6,60)
        sage: _ = designs.transversal_design(5,60) # checks some tricky divisibility error

    For small values of the parameter ``n`` we check the coherence of the
    function :func:`transversal_design`::

        sage: for n in range(2,25):                               # long time (15s)
        ....:     i = 2
        ....:     while designs.transversal_design(i, n, existence=True) is True:
        ....:         i += 1
        ....:     _ = designs.transversal_design(i-1, n)
        ....:     assert designs.transversal_design(None, n, existence=True) == i - 1
        ....:     j = i
        ....:     while designs.transversal_design(j, n, existence=True) is Unknown:
        ....:         try:
        ....:             _ = designs.transversal_design(j, n)
        ....:             raise AssertionError("no NotImplementedError")
        ....:         except NotImplementedError:
        ....:             pass
        ....:         j += 1
        ....:     k = j
        ....:     while k < n+4:
        ....:         assert designs.transversal_design(k, n, existence=True) is False
        ....:         try:
        ....:             _ = designs.transversal_design(k, n)
        ....:             raise AssertionError("no EmptySetError")
        ....:         except EmptySetError:
        ....:             pass
        ....:         k += 1
        ....:     print("%2d: (%2d, %2d)"%(n,i,j))
         2: ( 4,  4)
         3: ( 5,  5)
         4: ( 6,  6)
         5: ( 7,  7)
         6: ( 4,  7)
         7: ( 9,  9)
         8: (10, 10)
         9: (11, 11)
        10: ( 5, 11)
        11: (13, 13)
        12: ( 8, 14)
        13: (15, 15)
        14: ( 7, 15)
        15: ( 7, 17)
        16: (18, 18)
        17: (19, 19)
        18: ( 8, 20)
        19: (21, 21)
        20: ( 7, 22)
        21: ( 8, 22)
        22: ( 6, 23)
        23: (25, 25)
        24: (10, 26)

    The special case `n=1`::

        sage: designs.transversal_design(3, 1).blocks()
        [[0, 1, 2]]
        sage: designs.transversal_design(None, 1, existence=True)
        +Infinity
        sage: designs.transversal_design(None, 1)
        Traceback (most recent call last):
        ...
        ValueError: there is no upper bound on k when 0<=n<=1

    Resolvable TD::

        sage: k,n = 5,15
        sage: TD = designs.transversal_design(k,n,resolvable=True)
        sage: TD.is_resolvable()
        True
        sage: r     = designs.transversal_design(None,n,resolvable=True,existence=True)
        sage: non_r = designs.transversal_design(None,n,existence=True)
        sage: r + 1 == non_r
        True
    '''

class TransversalDesign(GroupDivisibleDesign):
    """
    Class for Transversal Designs.

    INPUT:

    - ``blocks`` -- collection of blocks

    - ``k``, ``n`` -- integers; parameters of the transversal design. They can
      be set to ``None`` (default) in which case their value is determined by
      the blocks.

    - ``check`` -- boolean (default: ``True``); whether to check that the
      design is indeed a transversal design with the right parameters

    EXAMPLES::

        sage: designs.transversal_design(None,5)
        Transversal Design TD(6,5)
        sage: designs.transversal_design(None,30)
        Transversal Design TD(6,30)
        sage: designs.transversal_design(None,36)
        Transversal Design TD(10,36)
    """
    def __init__(self, blocks, k=None, n=None, check: bool = True, **kwds) -> None:
        """
        Constructor of the class.

        EXAMPLES::

            sage: designs.transversal_design(None,5)
            Transversal Design TD(6,5)
        """

def is_transversal_design(B, k, n, verbose: bool = False):
    """
    Check that a given set of blocks ``B`` is a transversal design.

    See :func:`~sage.combinat.designs.orthogonal_arrays.transversal_design`
    for a definition.

    INPUT:

    - ``B`` -- the list of blocks

    - ``k``, ``n`` -- integers

    - ``verbose`` -- boolean; whether to display information about what is
      going wrong

    .. NOTE::

        The transversal design must have `\\{0, \\ldots, kn-1\\}` as a ground set,
        partitioned as `k` sets of size `n`: `\\{0, \\ldots, k-1\\} \\sqcup
        \\{k, \\ldots, 2k-1\\} \\sqcup \\cdots \\sqcup \\{k(n-1), \\ldots, kn-1\\}`.

    EXAMPLES::

        sage: TD = designs.transversal_design(5, 5, check=True) # indirect doctest
        sage: from sage.combinat.designs.orthogonal_arrays import is_transversal_design
        sage: is_transversal_design(TD, 5, 5)
        True
        sage: is_transversal_design(TD, 4, 4)
        False
    """
def wilson_construction(OA, k, r, m, u, check: bool = True, explain_construction: bool = False):
    """
    Return a `OA(k,rm+\\sum_i u_i)` from a truncated `OA(k+s,r)` by Wilson's
    construction.

    **Simple form:**

    Let `OA` be a truncated `OA(k+s,r)` with `s` truncated columns of sizes
    `u_1,...,u_s`, whose blocks have sizes in `\\{k+b_1,...,k+b_t\\}`. If there
    exist:

    - An `OA(k,m+b_i) - b_i.OA(k,1)` for every `1\\leq i\\leq t`

    - An `OA(k,u_i)` for every `1\\leq i\\leq s`

    Then there exists an `OA(k,rm+\\sum u_i)`. The construction is a
    generalization of Lemma 3.16 in [HananiBIBD]_.

    **Brouwer-Van Rees form:**

    Let `OA` be a truncated `OA(k+s,r)` with `s` truncated columns of sizes
    `u_1,...,u_s`. Let the set `H_i` of the `u_i` points of column `k+i` be
    partitionned into `\\sum_j H_{ij}`. Let `m_{ij}` be integers
    such that:

    - For `0\\leq i <l` there exists an `OA(k,\\sum_j m_{ij}|H_{ij}|)`

    - For any block `B\\in OA` intersecting the sets `H_{ij(i)}` there exists an
      `OA(k,m+\\sum_i m_{ij})-\\sum_i OA(k,m_{ij(j)})`.

    Then there exists an `OA(k,rm+\\sum_{i,j}m_{ij})`. This construction appears
    in [BvR1982]_.

    INPUT:

    - ``OA`` -- an incomplete orthogonal array with `k+s` columns. The elements
      of a column of size `c` must belong to `\\{0,...,c\\}`. The missing entries
      of a block are represented by ``None`` values. If ``OA=None``, it is
      defined as a truncated orthogonal arrays with `k+s` columns.

    - ``k``, ``r``, ``m`` -- integers

    - ``u`` -- list; two cases depending on the form to use:

        - Simple form: a list of length `s` such that column ``k+i`` has size
          ``u[i]``. The untruncated points of column ``k+i`` are assumed to be
          ``[0,...,u[i]-1]``.

        - Brouwer-Van Rees form: a list of length `s` such that ``u[i]`` is the
          list of pairs `(m_{i0},|H_{i0}|),...,(m_{ip_i},|H_{ip_i}|)`. The
          untruncated points of column ``k+i`` are assumed to be `[0,...,u_i-1]`
          where `u_i=\\sum_j |H_{ip_i}|`. Besides, the first `|H_{i0}|` points
          represent `H_{i0}`, the next `|H_{i1}|` points represent `H_{i1}`,
          etc...

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    REFERENCE:

    .. [HananiBIBD] Balanced incomplete block designs and related designs,
      Haim Hanani,
      Discrete Mathematics 11.3 (1975) pages 255-369.

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import wilson_construction
        sage: from sage.combinat.designs.orthogonal_arrays import OA_relabel
        sage: from sage.combinat.designs.orthogonal_arrays_find_recursive import find_wilson_decomposition_with_one_truncated_group
        sage: total = 0
        sage: for k in range(3,8):
        ....:    for n in range(1,30):
        ....:        if find_wilson_decomposition_with_one_truncated_group(k,n):
        ....:            total += 1
        ....:            f, args = find_wilson_decomposition_with_one_truncated_group(k,n)
        ....:            _ = f(*args)
        sage: total
        41

        sage: print(designs.orthogonal_arrays.explain_construction(7,58))
        Wilson's construction n=8.7+1+1 with master design OA(7+2,8)
        sage: print(designs.orthogonal_arrays.explain_construction(9,115))
        Wilson's construction n=13.8+11 with master design OA(9+1,13)
        sage: print(wilson_construction(None,5,11,21,[[(5,5)]],explain_construction=True))
        Brouwer-van Rees construction n=11.21+(5.5) with master design OA(5+1,11)
        sage: print(wilson_construction(None,71,17,21,[[(4,9),(1,1)],[(9,9),(1,1)]],explain_construction=True))
        Brouwer-van Rees construction n=17.21+(9.4+1.1)+(9.9+1.1) with master design OA(71+2,17)

    An example using the Brouwer-van Rees generalization::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.orthogonal_arrays import wilson_construction
        sage: OA = designs.orthogonal_arrays.build(6,11)
        sage: OA = [[x if (i<5 or x<5) else None for i,x in enumerate(R)] for R in OA]
        sage: OAb = wilson_construction(OA,5,11,21,[[(5,5)]])
        sage: is_orthogonal_array(OAb,5,256)
        True
    """
def TD_product(k, TD1, n1, TD2, n2, check: bool = True):
    """
    Return the product of two transversal designs.

    From a transversal design `TD_1` of parameters `k,n_1` and a transversal
    design `TD_2` of parameters `k,n_2`, this function returns a transversal
    design of parameters `k,n` where `n=n_1\\times n_2`.

    Formally, if the groups of `TD_1` are `V^1_1,\\dots,V^1_k` and the groups of
    `TD_2` are `V^2_1,\\dots,V^2_k`, the groups of the product design are
    `V^1_1\\times V^2_1,\\dots,V^1_k\\times V^2_k` and its blocks are the
    `\\{(x^1_1,x^2_1),\\dots,(x^1_k,x^2_k)\\}` where `\\{x^1_1,\\dots,x^1_k\\}` is a
    block of `TD_1` and `\\{x^2_1,\\dots,x^2_k\\}` is a block of `TD_2`.

    INPUT:

    - ``TD1``, ``TD2`` -- transversal designs

    - ``k``, ``n1``, ``n2`` -- integers

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    .. NOTE::

        This function uses transversal designs with
        `V_1=\\{0,\\dots,n-1\\},\\dots,V_k=\\{(k-1)n,\\dots,kn-1\\}` both as input and
        output.

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import TD_product
        sage: TD1 = designs.transversal_design(6,7)
        sage: TD2 = designs.transversal_design(6,12)
        sage: TD6_84 = TD_product(6,TD1,7,TD2,12)
    """
def orthogonal_array(k, n, t: int = 2, resolvable: bool = False, check: bool = True, existence: bool = False, explain_construction: bool = False):
    """
    Return an orthogonal array of parameters `k,n,t`.

    An orthogonal array of parameters `k,n,t` is a matrix with `k` columns
    filled with integers from `[n]` in such a way that for any `t` columns, each
    of the `n^t` possible rows occurs exactly once. In
    particular, the matrix has `n^t` rows.

    More general definitions sometimes involve a `\\lambda` parameter, and we
    assume here that `\\lambda=1`.

    An orthogonal array is said to be *resolvable* if it corresponds to a
    resolvable transversal design (see
    :meth:`sage.combinat.designs.incidence_structures.IncidenceStructure.is_resolvable`).

    For more information on orthogonal arrays, see
    :wikipedia:`Orthogonal_array`.

    INPUT:

    - ``k`` -- integer; number of columns. If ``k`` is ``None`` it is set to the
      largest value available.

    - ``n`` -- integer; number of symbols

    - ``t`` -- integer (default: 2); strength of the array

    - ``resolvable`` -- boolean (default: ``False``); set to ``True`` if you
      want the design to be resolvable. The `n` classes of the resolvable
      design are obtained as the first `n` blocks, then the next `n` blocks,
      etc.

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
          integer, i.e. the largest `k` such that we can build a `OA(k,n)`.

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    OUTPUT: the kind of output depends on the input:

    - if ``existence=False`` (the default) then the output is a list of lists
      that represent an orthogonal array with parameters ``k`` and ``n``

    - if ``existence=True`` and ``k`` is an integer, then the function returns a
      troolean: either ``True``, ``Unknown`` or ``False``

    - if ``existence=True`` and ``k=None`` then the output is the largest value
      of ``k`` for which Sage knows how to compute a `TD(k,n)`.

    .. NOTE::

        This method implements theorems from [Stinson2004]_. See the code's
        documentation for details.

    .. SEEALSO::

        When `t=2` an orthogonal array is also a transversal design (see
        :func:`transversal_design`) and a family of mutually orthogonal latin
        squares (see
        :func:`~sage.combinat.designs.latin_squares.mutually_orthogonal_latin_squares`).

    TESTS:

    The special cases `n=0,1`::

        sage: designs.orthogonal_arrays.build(3,0)
        []
        sage: designs.orthogonal_arrays.build(3,1)
        [[0, 0, 0]]
        sage: designs.orthogonal_arrays.largest_available_k(0)
        +Infinity
        sage: designs.orthogonal_arrays.largest_available_k(1)
        +Infinity
        sage: designs.orthogonal_arrays.build(16,0)
        []
        sage: designs.orthogonal_arrays.build(16,1)
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    when `t>2` and `k=None`::

        sage: t = 3
        sage: designs.orthogonal_arrays.largest_available_k(5,t=t) == t
        True
        sage: _ = designs.orthogonal_arrays.build(t,5,t)
    """
def largest_available_k(n, t: int = 2):
    """
    Return the largest `k` such that Sage can build an `OA(k,n)`.

    INPUT:

    - ``n`` -- integer

    - ``t`` -- integer (default: 2); strength of the array

    EXAMPLES::

        sage: designs.orthogonal_arrays.largest_available_k(0)
        +Infinity
        sage: designs.orthogonal_arrays.largest_available_k(1)
        +Infinity
        sage: designs.orthogonal_arrays.largest_available_k(10)
        4
        sage: designs.orthogonal_arrays.largest_available_k(27)
        28
        sage: designs.orthogonal_arrays.largest_available_k(100)
        10
        sage: designs.orthogonal_arrays.largest_available_k(-1)
        Traceback (most recent call last):
        ...
        ValueError: n(=-1) was expected to be >=0
    """
def incomplete_orthogonal_array(k, n, holes, resolvable: bool = False, existence: bool = False):
    """
    Return an `OA(k,n)-\\sum_{1\\leq i\\leq x} OA(k,s_i)`.

    An `OA(k,n)-\\sum_{1\\leq i\\leq x} OA(k,s_i)` is an orthogonal array from
    which have been removed disjoint `OA(k,s_1),...,OA(k,s_x)`. If there exist
    `OA(k,s_1),...,OA(k,s_x)` they can be used to fill the holes and give rise
    to an `OA(k,n)`.

    A very useful particular case (see e.g. the Wilson construction in
    :func:`wilson_construction`) is when all `s_i=1`. In that case the
    incomplete design is a `OA(k,n)-x.OA(k,1)`. Such design is equivalent to
    transversal design `TD(k,n)` from which has been removed `x` disjoint
    blocks.

    INPUT:

    - ``k``, ``n`` -- integers

    - ``holes`` -- list of integers respective sizes of the holes to be found

    - ``resolvable`` -- boolean (default: ``False``); set to ``True`` if you
      want the design to be resolvable. The classes of the resolvable design
      are obtained as the first `n` blocks, then the next `n` blocks, etc.

    - ``existence`` -- boolean; instead of building the design, return:

        - ``True`` -- meaning that Sage knows how to build the design

        - ``Unknown`` -- meaning that Sage does not know how to build the
          design, but that the design may exist (see :mod:`sage.misc.unknown`)

        - ``False`` -- meaning that the design does not exist

    .. NOTE::

        By convention, the ground set is always `V = \\{0, ..., n-1\\}`.

        If all holes have size 1, in the incomplete orthogonal array returned by
        this function the holes are `\\{n-1, ..., n-s_1\\}^k`,
        `\\{n-s_1-1,...,n-s_1-s_2\\}^k`, etc.

        More generally, if ``holes`` is equal to `u1,...,uk`, the `i`-th hole is
        the set of points `\\{n-\\sum_{j\\geq i}u_j,...,n-\\sum_{j\\geq i+1}u_j\\}^k`.

    .. SEEALSO::

        :func:`OA_find_disjoint_blocks`

    EXAMPLES::

        sage: IOA = designs.incomplete_orthogonal_array(3,3,[1,1,1])
        sage: IOA
        [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        sage: missing_blocks = [[0,0,0],[1,1,1],[2,2,2]]
        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: is_orthogonal_array(IOA + missing_blocks,3,3,2)
        True

    TESTS:

    Affine planes and projective planes::

        sage: for q in range(2,100):
        ....:     if is_prime_power(q):
        ....:         assert designs.incomplete_orthogonal_array(q,q,[1]*q,existence=True)
        ....:         assert not designs.incomplete_orthogonal_array(q+1,q,[1]*2,existence=True)

    Further tests::

        sage: designs.incomplete_orthogonal_array(8,4,[1,1,1],existence=True)
        False
        sage: designs.incomplete_orthogonal_array(5,10,[1,1,1],existence=True)
        Unknown
        sage: designs.incomplete_orthogonal_array(5,10,[1,1,1])
        Traceback (most recent call last):
        ...
        NotImplementedError: I don't know how to build an OA(5,10)!
        sage: designs.incomplete_orthogonal_array(4,3,[1,1])
        Traceback (most recent call last):
        ...
        EmptySetError: There is no OA(n+1,n) - 2.OA(n+1,1) as all blocks intersect in a projective plane.
        sage: n=10
        sage: k=designs.orthogonal_arrays.largest_available_k(n)
        sage: designs.incomplete_orthogonal_array(k,n,[1,1,1],existence=True)
        True
        sage: _ = designs.incomplete_orthogonal_array(k,n,[1,1,1])
        sage: _ = designs.incomplete_orthogonal_array(k,n,[1])

    A resolvable `OA(k,n)-n.OA(k,1)`. We check that extending each class and
    adding the `[i,i,...]` blocks turns it into an `OA(k+1,n)`.::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: k,n=5,7
        sage: OA = designs.incomplete_orthogonal_array(k,n,[1]*n,resolvable=True)
        sage: classes = [OA[i*n:(i+1)*n] for i in range(n-1)]
        sage: for classs in classes: # The design is resolvable !
        ....:     assert(len(set(col))==n for col in zip(*classs))
        sage: OA.extend([[i]*(k) for i in range(n)])
        sage: for i,R in enumerate(OA):
        ....:     R.append(i//n)
        sage: is_orthogonal_array(OA,k+1,n)
        True

    Non-existent resolvable incomplete OA::

        sage: designs.incomplete_orthogonal_array(9,13,[1]*10,resolvable=True,existence=True)
        False
        sage: designs.incomplete_orthogonal_array(9,13,[1]*10,resolvable=True)
        Traceback (most recent call last):
        ...
        EmptySetError: There is no resolvable incomplete OA(9,13) whose holes' sizes sum to 10<n(=13)

    Error message for big holes::

        sage: designs.incomplete_orthogonal_array(6,4*9,[9,9,8])
        Traceback (most recent call last):
        ...
        NotImplementedError: I was not able to build this OA(6,36)-OA(6,8)-2.OA(6,9)

    10 holes of size 9 through the product construction::

        sage: # long time
        sage: iOA = designs.incomplete_orthogonal_array(10,153,[9]*10)
        sage: OA9 = designs.orthogonal_arrays.build(10,9)
        sage: for i in range(10):
        ....:     iOA.extend([[153-9*(i+1)+x for x in B] for B in OA9])
        sage: is_orthogonal_array(iOA,10,153)
        True

    An `OA(9,82)-OA(9,9)-OA(9,1)`::

        sage: ioa = designs.incomplete_orthogonal_array(9,82,[9,1])
        sage: ioa.extend([[x+72 for x in B] for B in designs.orthogonal_arrays.build(9,9)])
        sage: ioa.extend([[x+81 for x in B] for B in designs.orthogonal_arrays.build(9,1)])
        sage: is_orthogonal_array(ioa,9,82,verbose=1)
        True

    An `OA(9,82)-OA(9,9)-2.OA(9,1)` in different orders::

        sage: ioa = designs.incomplete_orthogonal_array(9,82,[1,9,1])
        sage: ioa.extend([[x+71 for x in B] for B in designs.orthogonal_arrays.build(9,1)])
        sage: ioa.extend([[x+72 for x in B] for B in designs.orthogonal_arrays.build(9,9)])
        sage: ioa.extend([[x+81 for x in B] for B in designs.orthogonal_arrays.build(9,1)])
        sage: is_orthogonal_array(ioa,9,82,verbose=1)
        True
        sage: ioa = designs.incomplete_orthogonal_array(9,82,[9,1,1])
        sage: ioa.extend([[x+71 for x in B] for B in designs.orthogonal_arrays.build(9,9)])
        sage: ioa.extend([[x+80 for x in B] for B in designs.orthogonal_arrays.build(9,1)])
        sage: ioa.extend([[x+81 for x in B] for B in designs.orthogonal_arrays.build(9,1)])
        sage: is_orthogonal_array(ioa,9,82,verbose=1)
        True

    Three holes of size 1::

        sage: ioa = designs.incomplete_orthogonal_array(3,6,[1,1,1])
        sage: ioa.extend([[i]*3 for i in [3,4,5]])
        sage: is_orthogonal_array(ioa,3,6,verbose=1)
        True
    """
def OA_find_disjoint_blocks(OA, k, n, x, *, solver=None, integrality_tolerance: float = 0.001):
    """
    Return `x` disjoint blocks contained in a given `OA(k,n)`.

    `x` blocks of an `OA` are said to be disjoint if they all have
    different values for a every given index, i.e. if they correspond to
    disjoint blocks in the `TD` associated with the `OA`.

    INPUT:

    - ``OA`` -- an orthogonal array

    - ``k``, ``n``, ``x`` -- integers

    - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``integrality_tolerance`` -- parameter for use with MILP solvers over an
      inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

    .. SEEALSO::

        :func:`incomplete_orthogonal_array`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import OA_find_disjoint_blocks
        sage: k=3;n=4;x=3
        sage: Bs = OA_find_disjoint_blocks(designs.orthogonal_arrays.build(k,n),k,n,x)
        sage: assert len(Bs) == x
        sage: for i in range(k):
        ....:     assert len(set([B[i] for B in Bs])) == x
        sage: OA_find_disjoint_blocks(designs.orthogonal_arrays.build(k,n),k,n,5)
        Traceback (most recent call last):
        ...
        ValueError: There does not exist 5 disjoint blocks in this OA(3,4)
    """
def OA_relabel(OA, k, n, blocks=..., matrix=None, symbol_list=None):
    '''
    Return a relabelled version of the OA.

    INPUT:

    - ``OA`` -- an OA, or rather a list of blocks of length `k`, each
      of which contains integers from `0` to `n-1`

    - ``k``, ``n`` -- integers

    - ``blocks`` -- list of blocks; relabels the integers of the OA
      from `[0..n-1]` into `[0..n-1]` in such a way that the `i`
      blocks from ``block`` are respectively relabeled as
      ``[n-i,...,n-i]``, ..., ``[n-1,...,n-1]``. Thus, the blocks from
      this list are expected to have disjoint values for each
      coordinate.

      If set to the empty list (default) no such relabelling is
      performed.

    - ``matrix`` -- a matrix of dimensions `k,n` such that if the i th
      coordinate of a block is `x`, this `x` will be relabelled with
      ``matrix[i][x]``. This is not necessarily an integer between `0`
      and `n-1`, and it is not necessarily an integer either. This is
      performed *after* the previous relabelling.

      If set to ``None`` (default) no such relabelling is performed.

    - ``symbol_list`` -- list of the desired symbols for the
      relabelled OA. If this is not ``None``, the same relabelling is
      done on all blocks such that the index of an element in
      symbol_list is its preimage in the relabelling map.

      .. NOTE::

          A ``None`` coordinate in one block remains a ``None``
          coordinate in the final block.

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import OA_relabel
        sage: OA = designs.orthogonal_arrays.build(3,2)
        sage: OA_relabel(OA,3,2,matrix=[["A","B"],["C","D"],["E","F"]])
        [[\'A\', \'C\', \'E\'], [\'A\', \'D\', \'F\'], [\'B\', \'C\', \'F\'], [\'B\', \'D\', \'E\']]

        sage: TD = OA_relabel(OA,3,2,matrix=[[0,1],[2,3],[4,5]]); TD
        [[0, 2, 4], [0, 3, 5], [1, 2, 5], [1, 3, 4]]
        sage: from sage.combinat.designs.orthogonal_arrays import is_transversal_design
        sage: is_transversal_design(TD,3,2)
        True

        sage: OA = designs.orthogonal_arrays.build(3,2)
        sage: OA_relabel(OA, 3, 2, symbol_list=[\'A\', \'B\'])
        [[\'A\', \'A\', \'A\'], [\'A\', \'B\', \'B\'], [\'B\', \'A\', \'B\'], [\'B\', \'B\', \'A\']]

    Making sure that ``[2,2,2,2]`` is a block of `OA(4,3)`. We do this
    by relabelling block ``[0,0,0,0]`` which belongs to the design::

        sage: designs.orthogonal_arrays.build(4,3)
        [[0, 0, 0, 0], [0, 1, 2, 1], [0, 2, 1, 2], [1, 0, 2, 2], [1, 1, 1, 0], [1, 2, 0, 1], [2, 0, 1, 1], [2, 1, 0, 2], [2, 2, 2, 0]]
        sage: OA_relabel(designs.orthogonal_arrays.build(4,3),4,3,blocks=[[0,0,0,0]])
        [[2, 2, 2, 2], [2, 0, 1, 0], [2, 1, 0, 1], [0, 2, 1, 1], [0, 0, 0, 2], [0, 1, 2, 0], [1, 2, 0, 0], [1, 0, 2, 1], [1, 1, 1, 2]]

    TESTS::

        sage: OA_relabel(designs.orthogonal_arrays.build(3,2),3,2,blocks=[[0,1],[0,1]])
        Traceback (most recent call last):
        ...
        RuntimeError: Two block have the same coordinate for one of the k dimensions
    '''
def OA_standard_label(OA):
    """
    Return the inputted OA with entries relabelled as integers [0,...,n-1].

    INPUT:

    - ``OA`` -- list of lists with symbols as entries that are not
      necessarily integers

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import OA_standard_label
        sage: C = [['a', 'a', 'a', 'b'],
        ....:      ['a', 'a', 'b', 'a'],
        ....:      ['a', 'b', 'a', 'a'],
        ....:      ['b', 'a', 'a', 'a'],
        ....:      ['b', 'b', 'b', 'b']]
        sage: OA_standard_label(C)
        [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]]
    """
def OA_n_times_2_pow_c_from_matrix(k, c, G, A, Y, check: bool = True):
    """
    Return an `OA(k, |G| \\cdot 2^c)` from a constrained `(G,k-1,2)`-difference
    matrix.

    This construction appears in [AC1994]_ and [Ab1995]_.

    Let `G` be an additive Abelian group. We denote by `H` a `GF(2)`-hyperplane
    in `GF(2^c)`.

    Let `A` be a `(k-1) \\times 2|G|` array with entries in `G \\times GF(2^c)`
    and `Y` be a vector with `k-1` entries in `GF(2^c)`. Let `B` and `C` be
    respectively the part of the array that belong to `G` and `GF(2^c)`.

    The input `A` and `Y` must satisfy the following conditions. For any `i \\neq
    j` and `g \\in G`:

    - there are exactly two values of `s` such that `B_{i,s} - B_{j,s} = g`
      (i.e. `B` is a `(G,k-1,2)`-difference matrix),

    - let `s_1` and `s_2` denote the two values of `s` given above, then exactly
      one of `C_{i,s_1} - C_{j,s_1}` and `C_{i,s_2} - C_{j,s_2}` belongs to the
      `GF(2)`-hyperplane `(Y_i - Y_j) \\cdot H` (we implicitly assumed that `Y_i
      \\not= Y_j`).

    Under these conditions, it is easy to check that the array whose `k-1` rows
    of length `|G|\\cdot 2^c` indexed by `1 \\leq i \\leq k-1` given by `A_{i,s} +
    (0, Y_i \\cdot v)` where `1\\leq s \\leq 2|G|,v\\in H` is a `(G \\times
    GF(2^c),k-1,1)`-difference matrix.

    INPUT:

    - ``k``, ``c`` -- integers

    - ``G`` -- an additive Abelian group

    - ``A`` -- a matrix with entries in `G \\times GF(2^c)`

    - ``Y`` -- a vector with entries in `GF(2^c)`

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    .. NOTE::

        By convention, a multiplicative generator `w` of `GF(2^c)^*` is fixed
        (inside the function). The hyperplane `H` is the one spanned by `w^0,
        w^1, \\ldots, w^{c-1}`. The `GF(2^c)` part of the input matrix `A` and
        vector `Y` are given in the following form: the integer `i` corresponds
        to the element `w^i` and ``None`` corresponds to `0`.

    .. SEEALSO::

        Several examples use this construction:

        - :func:`~sage.combinat.designs.database.OA_9_40`
        - :func:`~sage.combinat.designs.database.OA_11_80`
        - :func:`~sage.combinat.designs.database.OA_15_112`
        - :func:`~sage.combinat.designs.database.OA_11_160`
        - :func:`~sage.combinat.designs.database.OA_16_176`
        - :func:`~sage.combinat.designs.database.OA_16_208`
        - :func:`~sage.combinat.designs.database.OA_15_224`
        - :func:`~sage.combinat.designs.database.OA_20_352`
        - :func:`~sage.combinat.designs.database.OA_20_416`
        - :func:`~sage.combinat.designs.database.OA_20_544`
        - :func:`~sage.combinat.designs.database.OA_11_640`
        - :func:`~sage.combinat.designs.database.OA_15_896`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import OA_n_times_2_pow_c_from_matrix
        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: A = [
        ....: [(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None)],
        ....: [(0,None),(1,None),   (2,2),   (3,2),   (4,2),(2,None),(3,None),(4,None),   (0,2),   (1,2)],
        ....: [(0,None),   (2,5),   (4,5),   (1,2),   (3,6),   (3,4),   (0,0),   (2,1),   (4,1),   (1,6)],
        ....: [(0,None),   (3,4),   (1,4),   (4,0),   (2,5),(3,None),   (1,0),   (4,1),   (2,2),   (0,3)],
        ....: ]
        sage: Y = [None, 0, 1, 6]
        sage: OA = OA_n_times_2_pow_c_from_matrix(5,3,GF(5),A,Y)
        sage: is_orthogonal_array(OA,5,40,2)
        True

        sage: A[0][0] = (1,None)
        sage: OA_n_times_2_pow_c_from_matrix(5,3,GF(5),A,Y)
        Traceback (most recent call last):
        ...
        ValueError: the first part of the matrix A must be a
        (G,k-1,2)-difference matrix

        sage: A[0][0] = (0,0)
        sage: OA_n_times_2_pow_c_from_matrix(5,3,GF(5),A,Y)
        Traceback (most recent call last):
        ...
        ValueError: B_2,0 - B_0,0 = B_2,6 - B_0,6 but the associated part of the
        matrix C does not satisfies the required condition
    """
def OA_from_quasi_difference_matrix(M, G, add_col: bool = True, fill_hole: bool = True):
    '''
    Return an Orthogonal Array from a Quasi-Difference matrix.

    **Difference Matrices**

    Let `G` be a group of order `g`. A *difference matrix* `M` is a `g\\times k`
    matrix with entries from `G` such that for any `1\\leq i < j < k` the set
    `\\{d_{li}-d_{lj}:1\\leq l \\leq g\\}` is equal to `G`.

    By concatenating the `g` matrices `M+x` (where `x\\in G`), one obtains a
    matrix of size `g^2\\times x` which is also an `OA(k,g)`.

    **Quasi-difference Matrices**

    A quasi-difference matrix is a difference matrix with missing entries. The
    construction above can be applied again in this case, where the missing
    entries in each column of `M` are replaced by unique values on which `G` has
    a trivial action.

    This produces an incomplete orthogonal array with a "hole" (i.e. missing
    rows) of size \'u\' (i.e. the number of missing values per column of `M`). If
    there exists an `OA(k,u)`, then adding the rows of this `OA(k,u)` to the
    incomplete orthogonal array should lead to an OA...

    **Formal definition** (from the Handbook of Combinatorial Designs [DesignHandbook]_)

    Let `G` be an abelian group of order `n`. A
    `(n,k;\\lambda,\\mu;u)`-quasi-difference matrix (QDM) is a matrix `Q=(q_{ij})`
    with `\\lambda(n-1+2u)+\\mu` rows and `k` columns, with each entry either
    empty or containing an element of `G`. Each column contains exactly `\\lambda
    u` entries, and each row contains at most one empty entry. Furthermore, for
    each `1 \\leq i < j \\leq k` the multiset

    .. MATH::

        \\{ q_{li} - q_{lj}: 1 \\leq l \\leq \\lambda (n-1+2u)+\\mu, \\text{ with }q_{li}\\text{ and }q_{lj}\\text{ not  empty}\\}

    contains every nonzero element of `G` exactly `\\lambda` times, and contains
    0 exactly `\\mu` times.

    **Construction**

    If a `(n,k;\\lambda,\\mu;u)`-QDM exists and `\\mu \\leq \\lambda`, then an
    `ITD_\\lambda (k,n+u;u)` exists. Start with a `(n,k;\\lambda,\\mu;u)`-QDM `A`
    over the group `G`. Append `\\lambda-\\mu` rows of zeroes. Then select `u`
    elements `\\infty_1,\\dots,\\infty_u` not in `G`, and replace the empty
    entries, each by one of these infinite symbols, so that `\\infty_i` appears
    exactly once in each column. Develop the resulting matrix over the group `G`
    (leaving infinite symbols fixed), to obtain a `\\lambda (n^2+2nu)\\times k`
    matrix `T`. Then `T` is an orthogonal array with `k` columns and index
    `\\lambda`, having `n+u` symbols and one hole of size `u`.

    Adding to `T` an `OA(k,u)` with elements `\\infty_1,\\dots,\\infty_u` yields
    the `ITD_\\lambda(k,n+u;u)`.

    For more information, see the Handbook of Combinatorial Designs
    [DesignHandbook]_ or
    `<http://web.cs.du.edu/~petr/milehigh/2013/Colbourn.pdf>`_.

    INPUT:

    - ``M`` -- the difference matrix whose entries belong to ``G``

    - ``G`` -- a group

    - ``add_col`` -- boolean; whether to add a column to the final OA equal to
      `(x_1,\\dots,x_g,x_1,\\dots,x_g,\\dots)` where `G=\\{x_1,\\dots,x_g\\}`

    - ``fill_hole`` -- boolean; whether to return the incomplete orthogonal
      array, or complete it with the `OA(k,u)` (default). When ``fill_hole is
      None``, no block of the incomplete OA contains more than one value `\\geq
      |G|`.

    EXAMPLES::

        sage: _ = designs.orthogonal_arrays.build(6,20) # indirect doctest
    '''
def OA_from_Vmt(m, t, V):
    """
    Return an Orthogonal Array from a `V(m,t)`.

    INPUT:

    - ``m``, ``t`` -- integers

    - ``V`` -- the vector `V(m,t)`

    .. SEEALSO::

        - :func:`QDM_from_Vmt`

        - :func:`OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: _ = designs.orthogonal_arrays.build(6,46) # indirect doctest
    """
def QDM_from_Vmt(m, t, V):
    """
    Return a QDM from a `V(m,t)`.

    **Definition**

    Let `q` be a prime power and let `q=mt+1` for `m,t` integers. Let `\\omega`
    be a primitive element of `\\GF{q}`. A `V(m,t)` vector is a vector
    `(a_1,\\dots,a_{m+1}` for which, for each `1\\leq k < m`, the differences

    .. MATH::

        \\{a_{i+k}-a_i:1\\leq i \\leq m+1,i+k\\neq m+2\\}

    represent the `m` cyclotomic classes of `\\GF{mt+1}` (compute subscripts
    modulo `m+2`). In other words, for fixed `k`, is
    `a_{i+k}-a_i=\\omega^{mx+\\alpha}` and `a_{j+k}-a_j=\\omega^{my+\\beta}` then
    `\\alpha\\not\\equiv\\beta \\mod{m}`

    *Construction of a quasi-difference matrix from a `V(m,t)` vector*

    Starting with a `V(m,t)` vector `(a_1,\\dots,a_{m+1})`, form a single row of
    length `m+2` whose first entry is empty, and whose remaining entries are
    `(a_1,\\dots,a_{m+1})`. Form `t` rows by multiplying this row by the `t` th
    roots, i.e. the powers of `\\omega^m`. From each of these `t` rows, form
    `m+2` rows by taking the `m+2` cyclic shifts of the row. The result is a
    `(a,m+2;1,0;t)-QDM`.

    For more information, refer to the Handbook of Combinatorial Designs
    [DesignHandbook]_.

    INPUT:

    - ``m``, ``t`` -- integers

    - ``V`` -- the vector `V(m,t)`

    .. SEEALSO::

        :func:`OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: _ = designs.orthogonal_arrays.build(6,46) # indirect doctest
    """
def OA_from_PBD(k, n, PBD, check: bool = True):
    """
    Return an `OA(k,n)` from a PBD.

    **Construction**

    Let `\\mathcal B` be a `(n,K,1)`-PBD. If there exists for every `i\\in K` a
    `TD(k,i)-i\\times TD(k,1)` (i.e. if there exist `k` idempotent MOLS), then
    one can obtain a `OA(k,n)` by concatenating:

    - A `TD(k,i)-i\\times TD(k,1)` defined over the elements of `B` for every `B
      \\in \\mathcal B`.

    - The rows `(i,...,i)` of length `k` for every `i\\in [n]`.

    .. NOTE::

        This function raises an exception when Sage is unable to build the
        necessary designs.

    INPUT:

    - ``k``, ``n`` -- integers

    - ``PBD`` -- a PBD on `0, \\ldots, n-1`

    EXAMPLES:

    We start from the example VI.1.2 from the [DesignHandbook]_ to build an
    `OA(3,10)`::

        sage: from sage.combinat.designs.orthogonal_arrays import OA_from_PBD
        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: pbd = [[0,1,2,3],[0,4,5,6],[0,7,8,9],[1,4,7],[1,5,8],
        ....: [1,6,9],[2,4,9],[2,5,7],[2,6,8],[3,4,8],[3,5,9],[3,6,7]]
        sage: oa = OA_from_PBD(3,10,pbd)
        sage: is_orthogonal_array(oa, 3, 10)
        True

    But we cannot build an `OA(4,10)` for this PBD (although there
    exists an `OA(4,10)`::

        sage: OA_from_PBD(4,10,pbd)
        Traceback (most recent call last):
        ...
        EmptySetError: There is no OA(n+1,n) - 3.OA(n+1,1)
        as all blocks intersect in a projective plane.

    Or an `OA(3,6)` (as the PBD has 10 points)::

        sage: _ = OA_from_PBD(3,6,pbd)
        Traceback (most recent call last):
        ...
        RuntimeError: PBD is not a valid Pairwise Balanced Design on [0,...,5]
    """
def OA_from_wider_OA(OA, k):
    """
    Return the first `k` columns of `OA`.

    If `OA` has `k` columns, this function returns `OA` immediately.

    INPUT:

    - ``OA`` -- an orthogonal array

    - ``k`` -- integer

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import OA_from_wider_OA
        sage: OA_from_wider_OA(designs.orthogonal_arrays.build(6,20,2),1)[:5]
        [(19,), (19,), (19,), (19,), (19,)]
        sage: _ = designs.orthogonal_arrays.build(5,46) # indirect doctest
    """

class OAMainFunctions:
    """
    Functions related to orthogonal arrays.

    An orthogonal array of parameters `k,n,t` is a matrix with `k` columns
    filled with integers from `[n]` in such a way that for any `t` columns, each
    of the `n^t` possible rows occurs exactly once. In particular, the matrix
    has `n^t` rows.

    For more information on orthogonal arrays, see
    :wikipedia:`Orthogonal_array`.

    From here you have access to:

    - :meth:`build(k,n,t=2) <build>`: return an orthogonal array with the given
      parameters.
    - :meth:`is_available(k,n,t=2) <is_available>`: answer whether there is a
      construction available in Sage for a given set of parameters.
    - :meth:`exists(k,n,t=2) <exists>`: answer whether an orthogonal array with
      these parameters exist.
    - :meth:`largest_available_k(n,t=2) <largest_available_k>`: return the
      largest integer `k` such that Sage knows how to build an `OA(k,n)`.
    - :meth:`explain_construction(k,n,t=2) <explain_construction>`: return a
      string that explains the construction that Sage uses to build an
      `OA(k,n)`.

    EXAMPLES::

        sage: designs.orthogonal_arrays.build(3,2)
        [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]

        sage: designs.orthogonal_arrays.build(5,5)
        [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 1, 3],
         [0, 3, 1, 4, 2], [0, 4, 3, 2, 1], [1, 0, 4, 3, 2],
         [1, 1, 1, 1, 1], [1, 2, 3, 4, 0], [1, 3, 0, 2, 4],
         [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 1, 0, 4, 3],
         [2, 2, 2, 2, 2], [2, 3, 4, 0, 1], [2, 4, 1, 3, 0],
         [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [3, 2, 1, 0, 4],
         [3, 3, 3, 3, 3], [3, 4, 0, 1, 2], [4, 0, 1, 2, 3],
         [4, 1, 3, 0, 2], [4, 2, 0, 3, 1], [4, 3, 2, 1, 0],
         [4, 4, 4, 4, 4]]

    What is the largest value of `k` for which Sage knows how to compute a
    `OA(k,14,2)`?::

        sage: designs.orthogonal_arrays.largest_available_k(14)
        6

    If you ask for an orthogonal array that does not exist, then you will
    either obtain an :exc:`EmptySetError` (if it knows that such an orthogonal
    array does not exist) or a :exc:`NotImplementedError`::

        sage: designs.orthogonal_arrays.build(4,2)
        Traceback (most recent call last):
        ...
        EmptySetError: There exists no OA(4,2) as k(=4)>n+t-1=3
        sage: designs.orthogonal_arrays.build(12,20)
        Traceback (most recent call last):
        ...
        NotImplementedError: I don't know how to build an OA(12,20)!
    """
    def __init__(self, *args, **kwds) -> None:
        """
        There is nothing here.

        TESTS::

            sage: designs.orthogonal_arrays(4,5) # indirect doctest
            Traceback (most recent call last):
            ...
            RuntimeError: This is not a function but a class. You want to call the designs.orthogonal_arrays.* functions
        """
    largest_available_k: Incomplete
    @staticmethod
    def explain_construction(k, n, t: int = 2):
        '''
        Return a string describing how to builds an `OA(k,n)`.

        INPUT:

        - ``k``, ``n``, ``t`` -- integers; parameters of the orthogonal array

        EXAMPLES::

            sage: designs.orthogonal_arrays.explain_construction(9,565)
            "Wilson\'s construction n=23.24+13 with master design OA(9+1,23)"
            sage: designs.orthogonal_arrays.explain_construction(10,154)
            \'the database contains a (137,10;1,0;17)-quasi difference matrix\'
        '''
    @staticmethod
    def build(k, n, t: int = 2, resolvable: bool = False):
        """
        Return an `OA(k,n)` of strength `t`.

        An orthogonal array of parameters `k,n,t` is a matrix with `k`
        columns filled with integers from `[n]` in such a way that for any
        `t` columns, each of the `n^t` possible rows occurs exactly
        once. In particular, the matrix has `n^t` rows.

        More general definitions sometimes involve a `\\lambda` parameter, and we
        assume here that `\\lambda=1`.

        For more information on orthogonal arrays, see
        :wikipedia:`Orthogonal_array`.

        INPUT:

        - ``k``, ``n``, ``t`` -- integers; parameters of the orthogonal array

        - ``resolvable`` -- boolean (default: ``False``); set to ``True`` if
          you want the design to be resolvable. The `n` classes of the
          resolvable design are obtained as the first `n` blocks, then the next
          `n` blocks, etc.

        EXAMPLES::

            sage: designs.orthogonal_arrays.build(3,3,resolvable=True) # indirect doctest
            [[0, 0, 0],
             [1, 2, 1],
             [2, 1, 2],
             [0, 2, 2],
             [1, 1, 0],
             [2, 0, 1],
             [0, 1, 1],
             [1, 0, 2],
             [2, 2, 0]]
            sage: OA_7_50 = designs.orthogonal_arrays.build(7,50)      # indirect doctest
        """
    @staticmethod
    def exists(k, n, t: int = 2):
        """
        Return the existence status of an `OA(k,n)`.

        INPUT:

        - ``k``, ``n``, ``t`` -- integers; parameters of the orthogonal array

        .. WARNING::

           The function does not only return booleans, but ``True``,
           ``False``, or ``Unknown``.

        .. SEEALSO::

            :meth:`is_available`

        EXAMPLES::

            sage: designs.orthogonal_arrays.exists(3,6) # indirect doctest
            True
            sage: designs.orthogonal_arrays.exists(4,6) # indirect doctest
            Unknown
            sage: designs.orthogonal_arrays.exists(7,6) # indirect doctest
            False
        """
    @staticmethod
    def is_available(k, n, t: int = 2):
        """
        Return whether Sage can build an `OA(k,n)`.

        INPUT:

        - ``k``, ``n``, ``t`` -- integers; parameters of the orthogonal array

        .. SEEALSO::

            :meth:`exists`

        EXAMPLES::

            sage: designs.orthogonal_arrays.is_available(3,6) # indirect doctest
            True
            sage: designs.orthogonal_arrays.is_available(4,6) # indirect doctest
            False
        """
