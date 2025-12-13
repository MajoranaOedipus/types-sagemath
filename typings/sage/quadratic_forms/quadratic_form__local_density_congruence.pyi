from sage.arith.misc import valuation as valuation
from sage.misc.verbose import verbose as verbose
from sage.quadratic_forms.count_local_2 import count_all_local_good_types_normal_form as count_all_local_good_types_normal_form, count_modp__by_gauss_sum as count_modp__by_gauss_sum
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set

def count_modp_solutions__by_Gauss_sum(self, p, m):
    '''
    Return the number of solutions of `Q(x) = m` (mod `p`) of a
    non-degenerate quadratic form over the finite field `\\ZZ/p\\ZZ`,
    where `p` is a prime number > 2.

    .. NOTE::

        We adopt the useful convention that a zero-dimensional
        quadratic form has exactly one solution always (i.e. the empty
        vector).

    These are defined in Table 1 on p363 of Hanke\'s "Local Densities..." paper.

    INPUT:

    - ``p`` -- a prime number > 2

    - ``m`` -- integer

    OUTPUT: integer `\\geq 0`

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: [Q.count_modp_solutions__by_Gauss_sum(3, m)  for m in range(3)]
        [9, 6, 12]

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,2])
        sage: [Q.count_modp_solutions__by_Gauss_sum(3, m)  for m in range(3)]
        [9, 12, 6]
    '''
def local_good_density_congruence_odd(self, p, m, Zvec, NZvec):
    """
    Find the Good-type local density of `Q` representing `m` at `p`.
    (Assuming that `p > 2` and `Q` is given in local diagonal form.)

    The additional congruence condition arguments ``Zvec`` and ``NZvec`` can
    be either a list of indices or None.  ``Zvec=[]`` is equivalent to
    ``Zvec=None``, which both impose no additional conditions, but
    ``NZvec=[]`` returns no solutions always while ``NZvec=None`` imposes no
    additional condition.

    .. TODO::

        Add type checking for ``Zvec``, ``NZvec``, and that `Q` is in local
        normal form.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_good_density_congruence_odd(3, 1, None, None)
        2/3

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_good_density_congruence_odd(3, 1, None, None)
        8/9
    """
def local_good_density_congruence_even(self, m, Zvec, NZvec):
    """
    Find the Good-type local density of `Q` representing `m` at `p=2`.
    (Assuming `Q` is given in local diagonal form.)

    The additional congruence condition arguments ``Zvec`` and ``NZvec`` can
    be either a list of indices or None.  ``Zvec=[]`` is equivalent to
    ``Zvec=None`` which both impose no additional conditions, but
    ``NZvec=[]`` returns no solutions always while ``NZvec=None`` imposes no
    additional condition.

    .. WARNING::

        Here the indices passed in ``Zvec`` and ``NZvec`` represent
        indices of the solution vector `x` of `Q(x) = m` (mod `p^k`), and *not*
        the Jordan components of `Q`.  They therefore are required (and
        assumed) to include either all or none of the indices of a given
        Jordan component of `Q`.  This is only important when `p=2` since
        otherwise all Jordan blocks are `1 \\times 1`, and so there the indices and
        Jordan blocks coincide.

    .. TODO::

        Add type checking for ``Zvec`` and ``NZvec``, and that `Q` is in local
        normal form.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and 2-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_good_density_congruence_even(1, None, None)
        1

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_good_density_congruence_even(1, None, None)
        1
        sage: Q.local_good_density_congruence_even(2, None, None)
        3/2
        sage: Q.local_good_density_congruence_even(3, None, None)
        1
        sage: Q.local_good_density_congruence_even(4, None, None)
        1/2

    ::

        sage: Q = QuadraticForm(ZZ, 4, range(10))
        sage: Q[0,0] = 5
        sage: Q[1,1] = 10
        sage: Q[2,2] = 15
        sage: Q[3,3] = 20
        sage: Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 5 1 2 3 ]
        [ * 10 5 6 ]
        [ * * 15 8 ]
        [ * * * 20 ]
        sage: Q.theta_series(20)                                                        # needs sage.libs.pari
        1 + 2*q^5 + 2*q^10 + 2*q^14 + 2*q^15 + 2*q^16 + 2*q^18 + O(q^20)
        sage: Q_local = Q.local_normal_form(2)                                          # needs sage.libs.pari sage.rings.padics
        sage: Q_local.local_good_density_congruence_even(1, None, None)                 # needs sage.libs.pari sage.rings.padics
        3/4
        sage: Q_local.local_good_density_congruence_even(2, None, None)                 # needs sage.libs.pari sage.rings.padics
        9/8
        sage: Q_local.local_good_density_congruence_even(5, None, None)                 # needs sage.libs.pari sage.rings.padics
        3/4
    """
def local_good_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the Good-type local density of `Q` representing `m` at `p`.
    (Front end routine for parity specific routines for `p`.)

    .. TODO::

        Add documentation about the additional congruence
        conditions ``Zvec`` and ``NZvec``.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_good_density_congruence(2, 1, None, None)
        1
        sage: Q.local_good_density_congruence(3, 1, None, None)
        2/3

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_good_density_congruence(2, 1, None, None)
        1
        sage: Q.local_good_density_congruence(3, 1, None, None)
        8/9
    """
def local_zero_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the Zero-type local density of `Q` representing `m` at `p`,
    allowing certain congruence conditions mod `p`.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_zero_density_congruence(2, 2, None, None)
        0
        sage: Q.local_zero_density_congruence(2, 4, None, None)
        1/2
        sage: Q.local_zero_density_congruence(3, 6, None, None)
        0
        sage: Q.local_zero_density_congruence(3, 9, None, None)
        2/9

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_zero_density_congruence(2, 2, None, None)
        0
        sage: Q.local_zero_density_congruence(2, 4, None, None)
        1/4
        sage: Q.local_zero_density_congruence(3, 6, None, None)
        0
        sage: Q.local_zero_density_congruence(3, 9, None, None)
        8/81
    """
def local_badI_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the Bad-type I local density of `Q` representing `m` at `p`.
    (Assuming that `p > 2` and `Q` is given in local diagonal form.)

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_badI_density_congruence(2, 1, None, None)
        0
        sage: Q.local_badI_density_congruence(2, 2, None, None)
        1
        sage: Q.local_badI_density_congruence(2, 4, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 1, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 6, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 9, None, None)
        0

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_badI_density_congruence(2, 1, None, None)
        0
        sage: Q.local_badI_density_congruence(2, 2, None, None)
        0
        sage: Q.local_badI_density_congruence(2, 4, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 2, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 6, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 9, None, None)
        0

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,3,9])
        sage: Q.local_badI_density_congruence(3, 1, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 3, None, None)
        4/3
        sage: Q.local_badI_density_congruence(3, 6, None, None)
        4/3
        sage: Q.local_badI_density_congruence(3, 9, None, None)
        0
        sage: Q.local_badI_density_congruence(3, 18, None, None)
        0
    """
def local_badII_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the Bad-type II local density of `Q` representing `m` at `p`.
    (Assuming that `p > 2` and `Q` is given in local diagonal form.)

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_badII_density_congruence(2, 1, None, None)
        0
        sage: Q.local_badII_density_congruence(2, 2, None, None)
        0
        sage: Q.local_badII_density_congruence(2, 4, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 1, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 6, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 9, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 27, None, None)
        0

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,3,9,9])
        sage: Q.local_badII_density_congruence(3, 1, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 3, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 6, None, None)
        0
        sage: Q.local_badII_density_congruence(3, 9, None, None)
        4/27
        sage: Q.local_badII_density_congruence(3, 18, None, None)
        4/9
    """
def local_bad_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the Bad-type local density of `Q` representing
    `m` at `p`, allowing certain congruence conditions mod `p`.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_bad_density_congruence(2, 1, None, None)
        0
        sage: Q.local_bad_density_congruence(2, 2, None, None)
        1
        sage: Q.local_bad_density_congruence(2, 4, None, None)
        0
        sage: Q.local_bad_density_congruence(3, 1, None, None)
        0
        sage: Q.local_bad_density_congruence(3, 6, None, None)
        0
        sage: Q.local_bad_density_congruence(3, 9, None, None)
        0
        sage: Q.local_bad_density_congruence(3, 27, None, None)
        0

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,3,9,9])
        sage: Q.local_bad_density_congruence(3, 1, None, None)
        0
        sage: Q.local_bad_density_congruence(3, 3, None, None)
        4/3
        sage: Q.local_bad_density_congruence(3, 6, None, None)
        4/3
        sage: Q.local_bad_density_congruence(3, 9, None, None)
        4/27
        sage: Q.local_bad_density_congruence(3, 18, None, None)
        4/9
        sage: Q.local_bad_density_congruence(3, 27, None, None)
        8/27
    """
def local_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the local density of `Q` representing `m` at `p`,
    allowing certain congruence conditions mod `p`.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_density_congruence(p=2, m=1, Zvec=None, NZvec=None)
        1
        sage: Q.local_density_congruence(p=3, m=1, Zvec=None, NZvec=None)
        8/9
        sage: Q.local_density_congruence(p=5, m=1, Zvec=None, NZvec=None)
        24/25
        sage: Q.local_density_congruence(p=7, m=1, Zvec=None, NZvec=None)
        48/49
        sage: Q.local_density_congruence(p=11, m=1, Zvec=None, NZvec=None)
        120/121

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_density_congruence(2, 1, None, None)
        1
        sage: Q.local_density_congruence(2, 2, None, None)
        1
        sage: Q.local_density_congruence(2, 4, None, None)
        3/2
        sage: Q.local_density_congruence(3, 1, None, None)
        2/3
        sage: Q.local_density_congruence(3, 6, None, None)
        4/3
        sage: Q.local_density_congruence(3, 9, None, None)
        14/9
        sage: Q.local_density_congruence(3, 27, None, None)
        2

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,3,9,9])
        sage: Q.local_density_congruence(3, 1, None, None)
        2
        sage: Q.local_density_congruence(3, 3, None, None)
        4/3
        sage: Q.local_density_congruence(3, 6, None, None)
        4/3
        sage: Q.local_density_congruence(3, 9, None, None)
        2/9
        sage: Q.local_density_congruence(3, 18, None, None)
        4/9
    """
def local_primitive_density_congruence(self, p, m, Zvec=None, NZvec=None):
    """
    Find the primitive local density of `Q` representing
    `m` at `p`, allowing certain congruence conditions mod `p`.

    .. NOTE::

        The following routine is not used internally, but is included for consistency.

    INPUT:

    - ``self`` -- quadratic form `Q`, assumed to be block diagonal and `p`-integral

    - ``p`` -- a prime number

    - ``m`` -- integer

    - ``Zvec``, ``NZvec`` -- non-repeating lists of integers in ``range(self.dim())`` or ``None``

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.local_primitive_density_congruence(p=2, m=1, Zvec=None, NZvec=None)
        1
        sage: Q.local_primitive_density_congruence(p=3, m=1, Zvec=None, NZvec=None)
        8/9
        sage: Q.local_primitive_density_congruence(p=5, m=1, Zvec=None, NZvec=None)
        24/25
        sage: Q.local_primitive_density_congruence(p=7, m=1, Zvec=None, NZvec=None)
        48/49
        sage: Q.local_primitive_density_congruence(p=11, m=1, Zvec=None, NZvec=None)
        120/121

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,3])
        sage: Q.local_primitive_density_congruence(2, 1, None, None)
        1
        sage: Q.local_primitive_density_congruence(2, 2, None, None)
        1
        sage: Q.local_primitive_density_congruence(2, 4, None, None)
        1
        sage: Q.local_primitive_density_congruence(3, 1, None, None)
        2/3
        sage: Q.local_primitive_density_congruence(3, 6, None, None)
        4/3
        sage: Q.local_primitive_density_congruence(3, 9, None, None)
        4/3
        sage: Q.local_primitive_density_congruence(3, 27, None, None)
        4/3

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,3,9,9])
        sage: Q.local_primitive_density_congruence(3, 1, None, None)
        2
        sage: Q.local_primitive_density_congruence(3, 3, None, None)
        4/3
        sage: Q.local_primitive_density_congruence(3, 6, None, None)
        4/3
        sage: Q.local_primitive_density_congruence(3, 9, None, None)
        4/27
        sage: Q.local_primitive_density_congruence(3, 18, None, None)
        4/9
        sage: Q.local_primitive_density_congruence(3, 27, None, None)
        8/27
        sage: Q.local_primitive_density_congruence(3, 81, None, None)
        8/27
        sage: Q.local_primitive_density_congruence(3, 243, None, None)
        8/27
    """
