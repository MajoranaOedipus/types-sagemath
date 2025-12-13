from .orthogonal_arrays import is_orthogonal_array as is_orthogonal_array, orthogonal_array as orthogonal_array, wilson_construction as wilson_construction

def construction_3_3(k, n, m, i, explain_construction: bool = False):
    """
    Return an `OA(k,nm+i)`.

    This is Wilson's construction with `i` truncated columns of size 1 and such
    that a block `B_0` of the incomplete OA intersects all truncated columns. As
    a consequence, all other blocks intersect only `0` or `1` of the last `i`
    columns. This allow to consider the block `B_0` only up to its first `k`
    coordinates and then use a `OA(k,i)` instead of a `OA(k,m+i) - i.OA(k,1)`.

    This is construction 3.3 from [AC07]_.

    INPUT:

    - ``k``, ``n``, ``m``, ``i`` -- integers such that the following designs are
      available: `OA(k,n)`, `OA(k,m)`, `OA(k,m+1)`, `OA(k,r)`

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_construction_3_3`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_find_recursive import find_construction_3_3
        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import construction_3_3
        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: k = 11; n = 177
        sage: is_orthogonal_array(construction_3_3(*find_construction_3_3(k,n)[1]),k,n,2)           # needs sage.schemes
        True

        sage: print(designs.orthogonal_arrays.explain_construction(9,91))
        Construction 3.3 with n=11,m=8,i=3 from:
           Julian R. Abel, Nicholas Cavenagh
           Concerning eight mutually orthogonal latin squares,
           Vol. 15, n.3, pp. 255-261,
           Journal of Combinatorial Designs, 2007
    """
def construction_3_4(k, n, m, r, s, explain_construction: bool = False):
    """
    Return a `OA(k,nm+rs)`.

    This is Wilson's construction applied to a truncated `OA(k+r+1,n)` with `r`
    columns of size `1` and one column of size `s`.

    The unique elements of the `r` truncated columns are picked so that a block
    `B_0` contains them all.

    - If there exists an `OA(k,m+r+1)` the column of size `s` is truncated in
      order to intersect `B_0`.

    - Otherwise, if there exists an `OA(k,m+r)`, the last column must not
      intersect `B_0`

    This is construction 3.4 from [AC07]_.

    INPUT:

    - ``k``, ``n``, ``m``, ``r``, ``s`` -- integers; we assume that `s<n` and
      `1\\leq r,s`

      The following designs must be available: `OA(k,n)`, `OA(k,m)`,
      `OA(k,m+1)`, `OA(k,m+2)`, `OA(k,s)`. Additionally, it requires either a
      `OA(k,m+r)` or a `OA(k,m+r+1)`.

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_construction_3_4`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_find_recursive import find_construction_3_4
        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import construction_3_4
        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: k = 8; n = 196
        sage: is_orthogonal_array(construction_3_4(*find_construction_3_4(k,n)[1]),k,n,2)           # needs sage.schemes
        True

        sage: print(designs.orthogonal_arrays.explain_construction(8,164))
        Construction 3.4 with n=23,m=7,r=2,s=1 from:
           Julian R. Abel, Nicholas Cavenagh
           Concerning eight mutually orthogonal latin squares,
           Vol. 15, n.3, pp. 255-261,
           Journal of Combinatorial Designs, 2007
    """
def construction_3_5(k, n, m, r, s, t, explain_construction: bool = False):
    """
    Return an `OA(k,nm+r+s+t)`.

    This is exactly Wilson's construction with three truncated groups
    except we make sure that all blocks have size `>k`, so we don't
    need a `OA(k,m+0)` but only `OA(k,m+1)`, `OA(k,m+2)` ,`OA(k,m+3)`.

    This is construction 3.5 from [AC07]_.

    INPUT:

    - ``k``, ``n``, ``m`` -- integers

    - ``r``, ``s``, ``t`` -- integers; sizes of the three truncated groups,
      such that `r\\leq s` and `(q-r-1)(q-s) \\geq (q-s-1)*(q-r)`

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    The following designs must be available : `OA(k,n)`, `OA(k,r)`, `OA(k,s)`,
    `OA(k,t)`, `OA(k,m+1)`, `OA(k,m+2)`, `OA(k,m+3)`.

    .. SEEALSO::

        :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_construction_3_5`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_find_recursive import find_construction_3_5
        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import construction_3_5
        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: k=8;n=111
        sage: is_orthogonal_array(construction_3_5(*find_construction_3_5(k,n)[1]),k,n,2)           # needs sage.schemes
        True

        sage: print(designs.orthogonal_arrays.explain_construction(8,90))
        Construction 3.5 with n=11,m=6,r=8,s=8,t=8 from:
           Julian R. Abel, Nicholas Cavenagh
           Concerning eight mutually orthogonal latin squares,
           Vol. 15, n.3, pp. 255-261,
           Journal of Combinatorial Designs, 2007
    """
def construction_3_6(k, n, m, i, explain_construction: bool = False):
    """
    Return a `OA(k,nm+i)`.

    This is Wilson's construction with `r` columns of order `1`, in which each
    block intersects at most two truncated columns. Such a design exists when
    `n` is a prime power and is returned by :func:`OA_and_oval`.

    INPUT:

    - ``k``, ``n``, ``m``, ``i`` -- integers; `n` must be a prime power. The
      following designs must be available: `OA(k+r,q)`, `OA(k,m)`, `OA(k,m+1)`,
      `OA(k,m+2)`

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    This is construction 3.6 from [AC07]_.

    .. SEEALSO::

        - :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_construction_3_6`

        - :func:`OA_and_oval`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_find_recursive import find_construction_3_6
        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import construction_3_6
        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: k=8;n=95
        sage: is_orthogonal_array(construction_3_6(*find_construction_3_6(k,n)[1]),k,n,2)           # needs sage.schemes
        True

        sage: print(designs.orthogonal_arrays.explain_construction(10,756))
        Construction 3.6 with n=16,m=47,i=4 from:
           Julian R. Abel, Nicholas Cavenagh
           Concerning eight mutually orthogonal latin squares,
           Vol. 15, n.3, pp. 255-261,
           Journal of Combinatorial Designs, 2007
    """
def OA_and_oval(q, *, solver=None, integrality_tolerance: float = 0.001):
    """
    Return a `OA(q+1,q)` whose blocks contains `\\leq 2` zeroes in the last `q`
    columns.

    This `OA` is build from a projective plane of order `q`, in which there
    exists an oval `O` of size `q+1` (i.e. a set of `q+1` points no three of
    which are [colinear/contained in a common set of the projective plane]).

    Removing an element `x\\in O` and all sets that contain it, we obtain a
    `TD(q+1,q)` in which `O` intersects all columns except one. As `O` is an
    oval, no block of the `TD` intersects it more than twice.

    INPUT:

    - ``q`` -- a prime power

    - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear
      Programming (MILP) solver to be used. If set to ``None``, the default one
      is used. For more information on MILP solvers and which default solver is
      used, see the method :meth:`solve
      <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
      :class:`MixedIntegerLinearProgram
      <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``integrality_tolerance`` -- parameter for use with MILP solvers over an
      inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

    .. NOTE::

        This function is called by :func:`construction_3_6`, an implementation
        of Construction 3.6 from [AC07]_.

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import OA_and_oval
        sage: _ = OA_and_oval
    """
def construction_q_x(k, q, x, check: bool = True, explain_construction: bool = False):
    """
    Return an `OA(k,(q-1)*(q-x)+x+2)` using the `q-x` construction.

    Let `v=(q-1)*(q-x)+x+2`. If there exists a projective plane of order `q`
    (e.g. when `q` is a prime power) and `0<x<q` then there exists a
    `(v-1,\\{q-x-1,q-x+1\\})`-GDD of type `(q-1)^{q-x}(x+1)^1` (see [Greig99]_ or
    Theorem 2.50, section IV.2.3 of [DesignHandbook]_). By adding to the ground
    set one point contained in all groups of the GDD, one obtains a
    `(v,\\{q-x-1,q-x+1,q,x+2\\})`-PBD with exactly one set of size `x+2`.

    Thus, assuming that we have the following:

    - `OA(k,q-x-1)-(q-x-1).OA(k,1)`
    - `OA(k,q-x+1)-(q-x+1).OA(k,1)`
    - `OA(k,q)-q.OA(k,1)`
    - `OA(k,x+2)`

    Then we can build from the PBD an `OA(k,v)`.

    Construction of the PBD (shared by Julian R. Abel):

        Start with a resolvable `(q^2,q,1)`-BIBD and put the points into a `q\\times q`
        array so that rows form a parallel class and columns form another.

        Now delete:

        - All `x(q-1)` points from the first `x` columns and not in the first
          row

        - All `q-x` points in the last `q-x` columns AND the first row.

        Then add a point `p_1` to the blocks that are rows. Add a second point
        `p_2` to the `q-x` blocks that are columns of size `q-1`, plus the first
        row of size `x+1`.

    INPUT:

    - ``k``, ``q``, ``x`` -- integers such that `0<x<q` and such that Sage can
      build:

        - A projective plane of order `q`
        - `OA(k,q-x-1)-(q-x-1).OA(k,1)`
        - `OA(k,q-x+1)-(q-x+1).OA(k,1)`
        - `OA(k,q)-q.OA(k,1)`
        - `OA(k,x+2)`

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        - :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_q_x`
        - :func:`~sage.combinat.designs.block_design.projective_plane`
        - :func:`~sage.combinat.designs.orthogonal_arrays.orthogonal_array`
        - :func:`~sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import construction_q_x
        sage: _ = construction_q_x(9,16,6)                                                          # needs sage.schemes

        sage: print(designs.orthogonal_arrays.explain_construction(9,158))
        (q-x)-construction with q=16,x=6 from:
           Malcolm Greig,
           Designs from projective planes and PBD bases,
           vol. 7, num. 5, pp. 341--374,
           Journal of Combinatorial Designs, 1999

    REFERENCES:

    .. [Greig99] Designs from projective planes and PBD bases
      Malcolm Greig
      Journal of Combinatorial Designs
      vol. 7, num. 5, pp. 341--374
      1999
    """
def thwart_lemma_3_5(k, n, m, a, b, c, d: int = 0, complement: bool = False, explain_construction: bool = False):
    """
    Return an `OA(k,nm+a+b+c+d)`.

    *(When `d=0`)*

    According to [Thwarts]_ when `n` is a prime power and `a+b+c\\leq n+1`, one
    can build an `OA(k+3,n)` with three truncated columns of sizes `a,b,c` in
    such a way that all blocks have size `\\leq k+2`.

    (in order to build a `OA(k,nm+a+b+c)` the following designs must also exist:
    `OA(k,a)`, `OA(k,b)`, `OA(k,c)`, `OA(k,m+0)`, `OA(k,m+1)`, `OA(k,m+2)`)

    Considering the complement of each truncated column, it is also possible to
    build an `OA(k+3,n)` with three truncated columns of sizes `a,b,c` in such a
    way that all blocks have size `>k` whenever `(n-a)+(n-b)+(n-c)\\leq n+1`.

    (in order to build a `OA(k,nm+a+b+c)` the following designs must also exist:
    `OA(k,a)`, `OA(k,b)`, `OA(k,c)`, `OA(k,m+1)`, `OA(k,m+2)`, `OA(k,m+3)`)

    Here is the proof of Lemma 3.5 from [Thwarts]_ enriched with explanations
    from Julian R. Abel:

        For any prime power `n` one can build `k-1` MOLS by associating to every
        nonzero `x\\in \\mathbb F_n` the latin square:

        .. MATH::

            M_x(i,j) = i+x*j \\text{ where }i,j\\in \\mathbb F_n

        In particular `M_1(i,j)=i+j`, whose `n` columns and lines are indexed by
        the elements of `\\mathbb F_n`. If we order the elements of `\\mathbb F_n`
        as `0,1,...,n-1,x+0,...,x+n-1,x^2+0,...` and reorder the columns
        and lines of `M_1` accordingly, the top-left `a\\times b` squares
        contains at most `a+b-1` distinct symbols.

    *(When* `d\\neq 0` *)*

    If there exists an `OA(k+3,n)` with three truncated columns of sizes `a,b,c`
    in such a way that all blocks have size `\\leq k+2`, by truncating
    arbitrarily another column to size `d` one obtains an `OA` with 4 truncated
    columns whose blocks miss at least one value. Thus, following the proof
    again one can build an `OA(k+4)` with four truncated columns of sizes
    `a,b,c,d` with blocks of size `\\leq k+3`.

    (in order to build a `OA(k,nm+a+b+c+d)` the following designs must also
    exist: `OA(k,a)`, `OA(k,b)`, `OA(k,c)`, `OA(k,d)`, `OA(k,m+0)`, `OA(k,m+1)`,
    `OA(k,m+2)`, `OA(k,m+3)`)

    As before, this also shows that one can build an `OA(k+4,n)` with four
    truncated columns of sizes `a,b,c,d` in such a way that all blocks have size
    `>k` whenever `(n-a)+(n-b)+(n-c)\\leq n+1`

    (in order to build a `OA(k,nm+a+b+c+d)` the following designs must also
    exist: `OA(k,n-a)`, `OA(k,n-b)`, `OA(k,n-c)`, `OA(k,d)`, `OA(k,m+1)`,
    `OA(k,m+2)`, `OA(k,m+3)`, `OA(k,m+4)`)

    INPUT:

    - ``k``, ``n``, ``m``, ``a``, ``b``, ``c``, ``d`` -- integers which must
      satisfy the constraints above. In particular, `a+b+c\\leq n+1` must hold
      By default, `d=0`.

    - ``complement`` -- boolean; whether to complement the sets, i.e. follow
      the `n-a,n-b,n-c` variant described above

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        - :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_thwart_lemma_3_5`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import thwart_lemma_3_5
        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: OA = thwart_lemma_3_5(6,23,7,5,7,8)                                                   # needs sage.schemes
        sage: is_orthogonal_array(OA,6,23*7+5+7+8,2)                                                # needs sage.schemes
        True

        sage: print(designs.orthogonal_arrays.explain_construction(10,408))                         # needs sage.schemes
        Lemma 4.1 with n=13,m=28 from:
           Charles J.Colbourn, Jeffrey H. Dinitz, Mieczyslaw Wojtas,
           Thwarts in transversal designs,
           Designs, Codes and Cryptography 5, no. 3 (1995): 189-197.

    With sets of parameters from [Thwarts]_::

        sage: l = [
        ....:    [11, 27, 78, 16, 17, 25, 0],
        ....:    [12, 19, 208, 11, 13, 16, 0],
        ....:    [12, 19, 208, 13, 13, 16, 0],
        ....:    [10, 13, 78, 9, 9, 13, 1],
        ....:    [10, 13, 79, 9, 9, 13, 1]]
        sage: for k,n,m,a,b,c,d in l:                                       # not tested -- too long
        ....:     OA = thwart_lemma_3_5(k,n,m,a,b,c,d,complement=True)
        ....:     assert is_orthogonal_array(OA,k,n*m+a+b+c+d,verbose=True)

        sage: print(designs.orthogonal_arrays.explain_construction(10,1046))
        Lemma 3.5 with n=13,m=79,a=9,b=1,c=0,d=9 from:
           Charles J.Colbourn, Jeffrey H. Dinitz, Mieczyslaw Wojtas,
           Thwarts in transversal designs,
           Designs, Codes and Cryptography 5, no. 3 (1995): 189-197.

    REFERENCE:

    .. [Thwarts] Thwarts in transversal designs
      Charles J.Colbourn, Jeffrey H. Dinitz, Mieczyslaw Wojtas.
      Designs, Codes and Cryptography 5, no. 3 (1995): 189-197.
    """
def thwart_lemma_4_1(k, n, m, explain_construction: bool = False):
    """
    Return an `OA(k,nm+4(n-2))`.

    Implements Lemma 4.1 from [Thwarts]_.

        If `n\\equiv 0,1\\pmod{3}` is a prime power, then there exists a truncated
        `OA(n+1,n)` whose last four columns have size `n-2` and intersect every
        block on `1,3` or `4` values. Consequently, if there exists an
        `OA(k,m+1)`, `OA(k,m+3)`, `OA(k,m+4)` and a `OA(k,n-2)` then there
        exists an `OA(k,nm+4(n-2)`

        Proof: form the transversal design by removing one point of the
        `AG(2,3)` (Affine Geometry) contained in the Desarguesian Projective
        Plane `PG(2,n)`.

    The affine geometry on 9 points contained in the projective geometry
    `PG(2,n)` is given explicitly in [OS64]_ (Thanks to Julian R. Abel for
    finding the reference!).

    INPUT:

    - ``k``, ``n``, ``m`` -- integers

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        - :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_thwart_lemma_4_1`

    EXAMPLES::

        sage: print(designs.orthogonal_arrays.explain_construction(10,408))                         # needs sage.schemes
        Lemma 4.1 with n=13,m=28 from:
           Charles J.Colbourn, Jeffrey H. Dinitz, Mieczyslaw Wojtas,
           Thwarts in transversal designs,
           Designs, Codes and Cryptography 5, no. 3 (1995): 189-197.


    REFERENCES:

    .. [OS64] Finite projective planes with affine subplanes,
      T. G. Ostrom and F. A. Sherk.
      Canad. Math. Bull vol7 num.4 (1964)
    """
def three_factor_product(k, n1, n2, n3, check: bool = False, explain_construction: bool = False):
    """
    Return an `OA(k+1,n_1n_2n_3)`.

    The three factor product construction from [DukesLing14]_ does the following:

        If `n_1\\leq n_2\\leq n_3` are such that there exists an
        `OA(k,n_1)`, `OA(k+1,n_2)` and `OA(k+1,n_3)`, then there exists a
        `OA(k+1,n_1n_2n_3)`.

    It works with a modified product of orthogonal arrays ([Rees93]_, [Rees00]_)
    which keeps track of parallel classes in the `OA` (the definition is given
    for transversal designs).

        A subset of blocks in an `TD(k,n)` is called a `c`-parallel class if
        every point is covered exactly `c` times. A 1-parallel class is a
        parallel class.

    The modified product:

        If there exists an `OA(k,n_1)`, and if there exists an `OA(k,n_2)` whose
        blocks are partitionned into `s` `n_1`-parallel classes and `n_2-sn_1`
        parallel classes, then there exists an `OA(k,n_1n_2)` whose blocks can
        be partitionned into `sn_1^2` parallel classes and
        `(n_1n_2-sn_1^2)/n_1=n_2-sn_1` `n_1`-parallel classes.

        Proof:

        - The product of the blocks of a parallel class with an `OA(k,n_1)`
          yields an `n_1`-parallel class of an `OA(k,n_1n_2)`.

        - The product of the blocks of a `n_1`-parallel class of `OA(k,n_2)`
          with an `OA(k,n_1)` can be done in such a way that it yields `n_1n_2`
          parallel classes of `OA(k,n_1n_2)`. Those classes cover exactly the
          pairs that would have been covered with the usual product.

          This can be achieved by simple cyclic permutations. Let us build the
          product of the `n_1`-parallel class `\\mathcal P\\subseteq OA(k,n_2)`
          with `OA(k,n_1)`: when computing the product of `P\\in\\mathcal P` with
          `B^1\\in OA(k,n_1)` the `i`-th coordinate should not be `(B^1_i,P_i)`
          but `(B^1_i+r,P_i)` (the sum is mod `n_1`) where `r` is the number of
          blocks of `\\mathcal P` we have already processed whose `i`-th
          coordinate is equal to `P_i` (note that `r< n_1` as `\\mathcal P` is
          `n_1`-parallel).

    With these tools, one can obtain the designs promised by the three factors
    construction applied to `k,n_1,n_2,n_3` (thanks to Julian R. Abel's help):

        1) Let `s` be the largest integer `\\leq n_3/n_1`. Apply the product
           construction to `OA(k,n_1)` and a resolvable `OA(k,n_3)` whose blocks
           are partitionned into `s` `n_1`-parallel classes and `n_3-sn_1`
           parallel classes. It results in a `OA(k,n_1n_3)` partitionned into
           `sn_1^2` parallel classes plus `(n_1n_3-sn_1^2)/n_1=n_3-sn_1`
           `n_1`-parallel classes.

        2) Add `n_3-n_1` parallel classes to every `n_1`-parallel class to turn
           them into `n_3`-parallel classes. Apply the product construction to
           this partitionned `OA(k,n_1n_3)` with a resolvable `OA(k,n_2)`.

        3) As `OA(k,n_2)` is resolvable, the `n_2`-parallel classes of
           `OA(k,n_1n_2n_3)` are actually the union of `n_2` parallel classes,
           thus the `OA(k,n_1n_2n_3)` is resolvable and can be turned into an
           `OA(k+1,n_1n_2n_3)`

    INPUT:

    - ``k``, ``n1``, ``n2``, ``n3`` -- integers

    - ``check`` -- boolean; whether to check that everything is going smoothly
      while the design is being built. It is disabled by default, as the
      constructor of orthogonal arrays checks the final design anyway.

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        - :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_three_factor_product`

    EXAMPLES::

        sage: # needs sage.schemes
        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import three_factor_product
        sage: OA = three_factor_product(4,4,4,4)
        sage: is_orthogonal_array(OA,5,64)
        True
        sage: OA = three_factor_product(4,3,4,5)
        sage: is_orthogonal_array(OA,5,60)
        True
        sage: OA = three_factor_product(5,4,5,7)
        sage: is_orthogonal_array(OA,6,140)
        True
        sage: OA = three_factor_product(9,8,9,9) # long time
        sage: is_orthogonal_array(OA,10,8*9*9)   # long time
        True
        sage: print(designs.orthogonal_arrays.explain_construction(10,648))
        Three-factor product with n=8.9.9 from:
           Peter J. Dukes, Alan C.H. Ling,
           A three-factor product construction for mutually orthogonal latin squares,
           https://arxiv.org/abs/1401.1466

    REFERENCE:

    .. [DukesLing14] A three-factor product construction for mutually orthogonal latin squares,
      Peter J. Dukes, Alan C.H. Ling,
      :arxiv:`1401.1466`

    .. [Rees00] Truncated Transversal Designs: A New Lower Bound on the Number of Idempotent MOLS of Side,
      Rolf S. Rees,
      Journal of Combinatorial Theory, Series A 90.2 (2000): 257-266.

    .. [Rees93] Two new direct product-type constructions for resolvable group-divisible designs,
      Rolf S. Rees,
      Journal of Combinatorial Designs 1.1 (1993): 15-26.
    """
def brouwer_separable_design(k, t, q, x, check: bool = False, verbose: bool = False, explain_construction: bool = False):
    """
    Return a `OA(k,t(q^2+q+1)+x)` using Brouwer's result on separable designs.

    This method is an implementation of Brouwer's construction presented in
    [Brouwer80]_. It consists in a systematic application of the usual
    transformation from PBD to OA, applied to a specific PBD.

    **Baer subplanes**

    When `q` is a prime power, the projective plane `PG(2,q^2)` can be
    partitionned into subplanes `PG(2,q)` (called Baer subplanes), giving
    `PG(2,q^2)=B_1\\cup \\dots\\cup B_{q^2-q+1}`. As a result, every line of the
    `PG(2,q^2)` intersects one of the subplane on `q+1` points and all others on
    `1` point.

    The `OA` are built by considering `B_1\\cup\\dots\\cup B_t`, for a total of
    `t(q^2+q+1)` points (to which `x` new points are then added). The blocks of
    this subdesign belong to two categories:

    * The blocks of size `t`: they come from the lines which intersect a
      `B_i` on `q+1` points for some `i>t`. The blocks of size `t` can be partitionned
      into `q^2-q+t-1` parallel classes according to their associated subplane `B_i`
      with `i>t`.

    * The blocks of size `q+t`: those blocks form a symmetric design, as every
      point is incident with `q+t` of them.

    **Constructions**

    In the following, we write `N=t(q^2+q+1)+x`. The code is also heavily
    commented, and will clear any doubt.

    * i) `x=0`: in that case we build a resolvable `OA(k-1,N)` that will then be
      completed into an `OA(k,N)`.

        * *Sets of size* `t`)

          We take the product of each parallel class with the parallel classes
          of a resolvable `OA(k-1,t)-t.OA(k-1,t)`, yielding new parallel
          classes.

        * *Sets of size* `q+t`)

          A `N \\times (q+t)` array is built whose rows are the sets of size
          `q+t` such that every value appears once per column. For each block of
          a `OA(k-1,q+t)-(q+t).OA(k-1,t)`, the product with the rows of the
          matrix yields a parallel class.

    * ii) `x=q+t`

        * *Sets of size* `t`)

          Each set of size `t` gives a `OA(k,t)-t.OA(k,1)`, except if there is
          only one parallel class in which case a `OA(k,t)` is sufficient.

        * *Sets of size* `q+t`)

          A `(N-x) \\times (q+t)` array `M` is built whose `N-x` rows are the
          sets of size `q+t` such that every value appears once per column. For
          each of the new `x=q+t` points `p_1,\\dots,p_{q+t}` we build a matrix
          `M_i` obtained from `M` by adding a column equal to `(p_i,p_i,p_i\\dots
          )`. We add to the OA the product of all rows of the `M_i` with the
          block of the `x=q+t` parallel classes of a resolvable
          `OA(k,t+q+1)-(t+q+1).OA(k,1)`.

        * *Set of size* `x`) An `OA(k,x)`

    * iii) `x = q^2-q+1-t`

        * *Sets of size* `t`)

          All blocks of the `i`-th parallel class are extended with the `i`-th
          new point. The blocks are then replaced by a `OA(k,t+1)-(t+1).OA(k,1)`
          or, if there is only one parallel class (i.e. `x=1`) by a
          `OA(k,t+1)-OA(k,1)`.

        * *Set of size* `q+t`)

          They are replaced by `OA(k,q+t)-(q+t).OA(k,1)`.

        * *Set of size* `x`) An `OA(k,x)`

    * iv) `x = q^2+1`

        * *Sets of size* `t`)

          All blocks of the `i`-th parallel class are extended with the `i`-th
          new point (the other `x-q-t` new points are not touched at this
          step). The blocks are then replaced by a `OA(k,t+1)-(t+1).OA(k,1)` or,
          if there is only one parallel class (i.e. `x=1`) by a
          `OA(k,t+1)-OA(k,1)`.

        * *Sets of size* `q+t`) Same as for ii)

        * *Set of size* `x`) An `OA(k,x)`

    * v) `0<x<q^2-q+1-t`

        * *Sets of size* `t`)

          The blocks of the first `x` parallel class are extended with the `x`
          new points, and replaced with `OA(k.t+1)-(t+1).OA(k,1)` or, if `x=1`,
          by `OA(k.t+1)-.OA(k,1)`

          The blocks of the other parallel classes are replaced by
          `OA(k,t)-t.OA(k,t)` or, if there is only one class left, by
          `OA(k,t)-OA(k,t)`

        * *Sets of size* `q+t`)

          They are replaced with `OA(k,q+t)-(q+t).OA(k,1)`.

        * *Set of size* `x`) An `OA(k,x)`

    * vi) `t+q<x<q^2+1`

        * *Sets of size* `t`) Same as in v) with an `x` equal to `x-q+t`.

        * *Sets of size* `t`) Same as in vii)

        * *Set of size* `x`) An `OA(k,x)`

    INPUT:

    - ``k``, ``t``, ``q``, ``x`` -- integers

    - ``check`` -- boolean (default: ``False``); whether to check that output
      is correct before returning it

    - ``verbose`` -- boolean; whether to print some information on the
      construction and parameters being used

    - ``explain_construction`` -- boolean; return a string describing
      the construction

    .. SEEALSO::

        - :func:`~sage.combinat.designs.orthogonal_arrays_find_recursive.find_brouwer_separable_design`

    REFERENCES:

    .. [Brouwer80] A Series of Separable Designs with Application to Pairwise Orthogonal Latin Squares,
      Andries E. Brouwer,
      Vol. 1, n. 1, pp. 39-41,
      European Journal of Combinatorics, 1980
      http://www.sciencedirect.com/science/article/pii/S0195669880800199

    EXAMPLES:

    Test all possible cases::

        sage: from sage.combinat.designs.orthogonal_arrays_build_recursive import brouwer_separable_design
        sage: k,q,t=4,4,3; _=brouwer_separable_design(k,q,t,0,verbose=True)
        Case i) with k=4,q=3,t=4,x=0
        sage: k,q,t=3,3,3; _=brouwer_separable_design(k,t,q,t+q,verbose=True,check=True)
        Case ii) with k=3,q=3,t=3,x=6,e3=1
        sage: k,q,t=3,3,6; _=brouwer_separable_design(k,t,q,t+q,verbose=True,check=True)
        Case ii) with k=3,q=3,t=6,x=9,e3=0
        sage: k,q,t=3,3,6; _=brouwer_separable_design(k,t,q,q**2-q+1-t,verbose=True,check=True)
        Case iii) with k=3,q=3,t=6,x=1,e2=0
        sage: k,q,t=3,4,6; _=brouwer_separable_design(k,t,q,q**2-q+1-t,verbose=True,check=True)
        Case iii) with k=3,q=4,t=6,x=7,e2=1
        sage: k,q,t=3,4,6; _=brouwer_separable_design(k,t,q,q**2+1,verbose=True,check=True)
        Case iv) with k=3,q=4,t=6,x=17,e4=1
        sage: k,q,t=3,2,2; _=brouwer_separable_design(k,t,q,q**2+1,verbose=True,check=True)
        Case iv) with k=3,q=2,t=2,x=5,e4=0
        sage: k,q,t=3,4,7; _=brouwer_separable_design(k,t,q,3,verbose=True,check=True)
        Case v) with k=3,q=4,t=7,x=3,e1=1,e2=1
        sage: k,q,t=3,4,7; _=brouwer_separable_design(k,t,q,1,verbose=True,check=True)
        Case v) with k=3,q=4,t=7,x=1,e1=1,e2=0
        sage: k,q,t=3,4,7; _=brouwer_separable_design(k,t,q,q**2-q-t,verbose=True,check=True)
        Case v) with k=3,q=4,t=7,x=5,e1=0,e2=1
        sage: k,q,t=5,4,7; _=brouwer_separable_design(k,t,q,t+q+3,verbose=True,check=True)
        Case vi) with k=5,q=4,t=7,x=14,e3=1,e4=1
        sage: k,q,t=5,4,8; _=brouwer_separable_design(k,t,q,t+q+1,verbose=True,check=True)
        Case vi) with k=5,q=4,t=8,x=13,e3=1,e4=0
        sage: k,q,t=5,4,8; _=brouwer_separable_design(k,t,q,q**2,verbose=True,check=True)
        Case vi) with k=5,q=4,t=8,x=16,e3=0,e4=1

        sage: print(designs.orthogonal_arrays.explain_construction(10,189))
        Brouwer's separable design construction with t=9,q=4,x=0 from:
           Andries E. Brouwer,
           A series of separable designs with application to pairwise orthogonal Latin squares
           Vol. 1, n. 1, pp. 39-41,
           European Journal of Combinatorics, 1980
    """
