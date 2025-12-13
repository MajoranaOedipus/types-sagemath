from sage.arith.misc import GCD as GCD, is_prime as is_prime, valuation as valuation
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def find_entry_with_minimal_scale_at_prime(self, p):
    """
    Find the entry of the quadratic form with minimal scale at the
    prime `p`, preferring diagonal entries in case of a tie.

    (I.e.  If
    we write the quadratic form as a symmetric matrix `M`, then this
    entry ``M[i,j]`` has the minimal valuation at the prime `p`.)

    .. NOTE::

        This answer is independent of the kind of matrix (Gram or
        Hessian) associated to the form.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT: a pair of integers `\\geq 0`

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [6, 2, 20]); Q
        Quadratic form in 2 variables over Integer Ring with coefficients:
          [ 6 2 ]
          [ * 20 ]
        sage: Q.find_entry_with_minimal_scale_at_prime(2)
        (0, 1)
        sage: Q.find_entry_with_minimal_scale_at_prime(3)
        (1, 1)
        sage: Q.find_entry_with_minimal_scale_at_prime(5)
        (0, 0)
    """
def local_normal_form(self, p):
    """
    Return a locally integrally equivalent quadratic form over
    the `p`-adic integers `\\ZZ_p` which gives the Jordan decomposition.

    The Jordan components are written as sums of blocks of size `\\leq 2`
    and are arranged by increasing scale, and then by increasing norm.
    This is equivalent to saying that we put the `1 \\times 1` blocks before
    the `2 \\times 2` blocks in each Jordan component.

    INPUT:

    - ``p`` -- a positive prime number

    OUTPUT: a quadratic form over `\\ZZ`

    .. WARNING::

        Currently this only works for quadratic forms defined over `\\ZZ`.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [10,4,1])
        sage: Q.local_normal_form(5)
        Quadratic form in 2 variables over Integer Ring with coefficients:
          [ 1 0 ]
          [ * 6 ]

    ::

        sage: Q.local_normal_form(3)
        Quadratic form in 2 variables over Integer Ring with coefficients:
          [ 10 0 ]
          [ * 15 ]

        sage: Q.local_normal_form(2)
        Quadratic form in 2 variables over Integer Ring with coefficients:
          [ 1 0 ]
          [ * 6 ]
    """
def jordan_blocks_by_scale_and_unimodular(self, p, safe_flag: bool = True):
    """
    Return a list of pairs `(s_i, L_i)` where `L_i` is a maximal
    `p^{s_i}`-unimodular Jordan component which is further decomposed into
    block diagonals of block size `\\le 2`.

    For each `L_i` the `2 \\times 2` blocks are listed after the `1 \\times 1` blocks
    (which follows from the convention of the
    :meth:`local_normal_form` method).

    .. NOTE::

        The decomposition of each `L_i` into smaller blocks is not unique!

    The ``safe_flag`` argument allows us to select whether we want a copy of
    the output, or the original output.  By default ``safe_flag = True``, so we
    return a copy of the cached information.  If this is set to ``False``, then
    the routine is much faster but the return values are vulnerable to being
    corrupted by the user.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT:

    A list of pairs `(s_i, L_i)` where:

    - `s_i` is an integer,
    - `L_i` is a block-diagonal unimodular quadratic form over `\\ZZ_p`.

    .. NOTE::

        These forms `L_i` are defined over the `p`-adic integers, but by a
        matrix over `\\ZZ` (or `\\QQ`?).

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,9,5,7])
        sage: Q.jordan_blocks_by_scale_and_unimodular(3)
        [(0, Quadratic form in 3 variables over Integer Ring with coefficients:
               [ 1 0 0 ]
               [ * 5 0 ]
               [ * * 7 ]),
         (2, Quadratic form in 1 variables over Integer Ring with coefficients:
               [ 1 ])]

    ::

        sage: Q2 = QuadraticForm(ZZ, 2, [1,1,1])
        sage: Q2.jordan_blocks_by_scale_and_unimodular(2)
        [(-1, Quadratic form in 2 variables over Integer Ring with coefficients:
                [ 2 2 ]
                [ * 2 ])]
        sage: Q = Q2 + Q2.scale_by_factor(2)
        sage: Q.jordan_blocks_by_scale_and_unimodular(2)
        [(-1, Quadratic form in 2 variables over Integer Ring with coefficients:
                [ 2 2 ]
                [ * 2 ]),
         (0, Quadratic form in 2 variables over Integer Ring with coefficients:
                [ 2 2 ]
                [ * 2 ])]
    """
def jordan_blocks_in_unimodular_list_by_scale_power(self, p):
    """
    Return a list of Jordan components, whose component at index `i`
    should be scaled by the factor `p^i`.

    This is only defined for integer-valued quadratic forms
    (i.e., forms with base ring `\\ZZ`), and the indexing only works
    correctly for `p=2` when the form has an integer Gram matrix.

    INPUT:

    - ``self`` -- a quadratic form over `\\ZZ`, which has integer Gram matrix if `p = 2`
    - ``p`` -- a prime number > 0

    OUTPUT: list of `p`-unimodular quadratic forms

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [2, -2, 0, 3, -5, 4])
        sage: Q.jordan_blocks_in_unimodular_list_by_scale_power(2)
        Traceback (most recent call last):
        ...
        TypeError: the given quadratic form has a Jordan component with a negative scale exponent

        sage: Q.scale_by_factor(2).jordan_blocks_in_unimodular_list_by_scale_power(2)
        [Quadratic form in 2 variables over Integer Ring with coefficients:
           [ 0 2 ]
           [ * 0 ],
         Quadratic form in 0 variables over Integer Ring with coefficients:
           ,
         Quadratic form in 1 variables over Integer Ring with coefficients:
           [ 345 ]]

        sage: Q.jordan_blocks_in_unimodular_list_by_scale_power(3)
        [Quadratic form in 2 variables over Integer Ring with coefficients:
           [ 2 0 ]
           [ * 10 ],
         Quadratic form in 1 variables over Integer Ring with coefficients:
           [ 2 ]]
    """
