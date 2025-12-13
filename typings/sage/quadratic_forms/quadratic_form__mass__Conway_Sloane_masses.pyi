from sage.arith.misc import fundamental_discriminant as fundamental_discriminant, is_prime as is_prime, legendre_symbol as legendre_symbol, prime_divisors as prime_divisors
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def parity(self, allow_rescaling_flag: bool = True):
    '''
    Return the parity ("even" or "odd") of an integer-valued quadratic
    form over `\\ZZ`, defined up to similitude/rescaling of the form so that
    its Jordan component of smallest scale is unimodular.  After this
    rescaling, we say a form is even if it only represents even numbers,
    and odd if it represents some odd number.

    If the ``allow_rescaling_flag`` is set to False, then we require that
    the quadratic form have a Gram matrix with coefficients in `\\ZZ`, and
    look at the unimodular Jordan block to determine its parity.  This
    returns an error if the form is not integer-matrix, meaning that it
    has Jordan components at `p=2` which do not have an integer scale.

    We determine the parity by looking for a `1 \\times 1` block in the 0-th
    Jordan component, after a possible rescaling.

    INPUT:

    - ``self`` -- a quadratic form with base ring `\\ZZ`, which we may
      require to have integer Gram matrix

    OUTPUT: one of the strings: ``\'even\'`` or ``\'odd\'``

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [4, -2, 0, 2, 3, 2]); Q
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 4 -2 0 ]
        [ * 2 3 ]
        [ * * 2 ]
        sage: Q.parity()
        \'even\'

    ::

        sage: Q = QuadraticForm(ZZ, 3, [4, -2, 0, 2, 3, 1]); Q
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 4 -2 0 ]
        [ * 2 3 ]
        [ * * 1 ]
        sage: Q.parity()
        \'even\'

    ::

        sage: Q = QuadraticForm(ZZ, 3, [4, -2, 0, 2, 2, 2]); Q
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 4 -2 0 ]
        [ * 2 2 ]
        [ * * 2 ]
        sage: Q.parity()
        \'even\'

    ::

        sage: Q = QuadraticForm(ZZ, 3, [4, -2, 0, 2, 2, 1]); Q
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 4 -2 0 ]
        [ * 2 2 ]
        [ * * 1 ]
        sage: Q.parity()
        \'odd\'
    '''
def is_even(self, allow_rescaling_flag: bool = True) -> bool:
    """
    Return true iff after rescaling by some appropriate factor, the
    form represents no odd integers.  For more details, see :meth:`parity`.

    Requires that `Q` is defined over `\\ZZ`.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [1, 0, 1])
        sage: Q.is_even()
        False
        sage: Q = QuadraticForm(ZZ, 2, [1, 1, 1])
        sage: Q.is_even()
        True
    """
def is_odd(self, allow_rescaling_flag: bool = True) -> bool:
    """
    Return true iff after rescaling by some appropriate factor, the
    form represents some odd integers.  For more details, see :meth:`parity`.

    Requires that `Q` is defined over `\\ZZ`.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [1, 0, 1])
        sage: Q.is_odd()
        True
        sage: Q = QuadraticForm(ZZ, 2, [1, 1, 1])
        sage: Q.is_odd()
        False
    """
def conway_species_list_at_odd_prime(self, p):
    """
    Return an integer called the 'species' which determines the type
    of the orthogonal group over the finite field `\\GF{p}`.

    This assumes that the given quadratic form is a unimodular Jordan
    block at an odd prime `p`.  When the dimension is odd then this
    number is always positive, otherwise it may be positive or
    negative (or zero, but that is considered positive by convention).

    .. NOTE::

        The species of a zero dimensional form is always 0+, so we
        interpret the return value of zero as positive here! =)

    INPUT:

    - ``p`` -- a positive prime number

    OUTPUT: list of integers

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,10))
        sage: Q.conway_species_list_at_odd_prime(3)
        [6, 2, 1]

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,8))
        sage: Q.conway_species_list_at_odd_prime(3)
        [5, 2]
        sage: Q.conway_species_list_at_odd_prime(5)
        [-6, 1]
    """
def conway_species_list_at_2(self):
    """
    Return an integer called the 'species' which determines the type
    of the orthogonal group over the finite field `\\GF{p}`.

    This assumes that the given quadratic form is a unimodular Jordan
    block at an odd prime `p`.  When the dimension is odd then this
    number is always positive, otherwise it may be positive or
    negative.

    .. NOTE::

        The species of a zero dimensional form is always 0+, so we
        interpret the return value of zero as positive here! =)

    OUTPUT: list of integers

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,10))
        sage: Q.conway_species_list_at_2()
        [1, 5, 1, 1, 1, 1]

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,8))
        sage: Q.conway_species_list_at_2()
        [1, 3, 1, 1, 1]
    """
def conway_octane_of_this_unimodular_Jordan_block_at_2(self):
    """
    Determines the 'octane' of this full unimodular Jordan block at
    the prime `p=2`.  This is an invariant defined (mod 8), ad.

    This assumes that the form is given as a block diagonal form with
    unimodular blocks of size `\\leq 2` and the `1 \\times 1` blocks are all in the upper
    leftmost position.

    OUTPUT: integer `0 \\leq x \\leq 7`

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.conway_octane_of_this_unimodular_Jordan_block_at_2()
        0
        sage: Q = DiagonalQuadraticForm(ZZ, [1,5,13])
        sage: Q.conway_octane_of_this_unimodular_Jordan_block_at_2()
        3
        sage: Q = DiagonalQuadraticForm(ZZ, [3,7,13])
        sage: Q.conway_octane_of_this_unimodular_Jordan_block_at_2()
        7
    """
def conway_diagonal_factor(self, p):
    """
    Compute the diagonal factor of Conway's `p`-mass.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT: a rational number > 0

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,6))
        sage: Q.conway_diagonal_factor(3)
        81/256
    """
def conway_cross_product_doubled_power(self, p):
    """
    Compute twice the power of `p` which evaluates the 'cross product'
    term in Conway's mass formula.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,8))
        sage: Q.conway_cross_product_doubled_power(2)
        18
        sage: Q.conway_cross_product_doubled_power(3)
        10
        sage: Q.conway_cross_product_doubled_power(5)
        6
        sage: Q.conway_cross_product_doubled_power(7)
        6
        sage: Q.conway_cross_product_doubled_power(11)
        0
        sage: Q.conway_cross_product_doubled_power(13)
        0
    """
def conway_type_factor(self):
    """
    This is a special factor only present in the mass formula when `p=2`.

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1,8))
        sage: Q.conway_type_factor()
        4
    """
def conway_p_mass(self, p):
    """
    Compute Conway's `p`-mass.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT: a rational number > 0

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, range(1, 6))
        sage: Q.conway_p_mass(2)
        16/3
        sage: Q.conway_p_mass(3)
        729/256
    """
def conway_standard_p_mass(self, p):
    """
    Compute the standard (generic) Conway-Sloane `p`-mass.

    INPUT:

    - ``p`` -- a prime number > 0

    OUTPUT: a rational number > 0

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.conway_standard_p_mass(2)
        2/3
    """
def conway_standard_mass(self):
    """
    Return the infinite product of the standard mass factors.

    OUTPUT: a rational number > 0

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [2, -2, 0, 3, -5, 4])
        sage: Q.conway_standard_mass()                                                  # needs sage.symbolic
        1/6

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.conway_standard_mass()                                                  # needs sage.symbolic
        1/6
    """
def conway_mass(self):
    """
    Compute the mass by using the Conway-Sloane mass formula.

    OUTPUT: a rational number > 0

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.conway_mass()                                                           # needs sage.symbolic
        1/48

        sage: Q = DiagonalQuadraticForm(ZZ, [7,1,1])
        sage: Q.conway_mass()                                                           # needs sage.symbolic
        3/16

        sage: Q = QuadraticForm(ZZ, 3, [7, 2, 2, 2, 0, 2]) + DiagonalQuadraticForm(ZZ, [1])
        sage: Q.conway_mass()                                                           # needs sage.symbolic
        3/32

        sage: Q = QuadraticForm(Matrix(ZZ, 2, [2,1,1,2]))
        sage: Q.conway_mass()                                                           # needs sage.symbolic
        1/12
    """
