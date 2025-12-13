from _typeshed import Incomplete
from sage.arith.misc import is_square as is_square, prime_divisors as prime_divisors, valuation as valuation
from sage.misc.functional import denominator as denominator, numerator as numerator
from sage.quadratic_forms.extras import least_quadratic_nonresidue as least_quadratic_nonresidue
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class QuadraticFormLocalRepresentationConditions:
    """
    A class for dealing with the local conditions of a
    quadratic form, and checking local representability of numbers.

    EXAMPLES::

        sage: Q4 = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q4.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [].  For these and the reals, we have:
             Reals:   [0, +Infinity]
        sage: Q4.is_locally_represented_number(1)
        True
        sage: Q4.is_locally_universal_at_all_primes()
        True
        sage: Q4.is_locally_universal_at_all_places()
        False
        sage: L = [m  for m in range(-5, 100)  if Q4.is_locally_represented_number(m)]
        sage: L == list(range(100))
        True

    ::

        sage: Q3 = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q3.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [2].  For these and the reals, we have:
             Reals:   [0, +Infinity]
             p = 2:   [0, 0, 0, +Infinity, 0, 0, 0, 0]
        sage: E = [m  for m in range(100)  if not Q3.is_locally_represented_number(m)]
        sage: E1 = [m  for m in range(1,100)  if m / 2**(2 * (valuation(m,2) // 2)) % 8 == 7]
        sage: E == E1
        True
        sage: E
        [7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, 79, 87, 92, 95]

    ::

        sage: Q2 = DiagonalQuadraticForm(ZZ, [1,1])
        sage: Q2.local_representation_conditions()
        This 2-dimensional form represents the p-adic integers of even
        valuation for all primes p except [2].
        For these and the reals, we have:
             Reals:   [0, +Infinity]
             p = 2:   [0, +Infinity, 0, +Infinity, 0, +Infinity, 0, +Infinity]
        sage: Q2.is_locally_universal_at_all_places()
        False
        sage: Q2.is_locally_universal_at_all_primes()
        False
        sage: L = [m  for m in range(-5, 25)  if Q2.is_locally_represented_number(m)]
        sage: L1 = [0] + [m for m in range(1, 25)
        ....:             if len([p for p in prime_factors(squarefree_part(ZZ(m)))
        ....:                       if (p % 4) == 3]) % 2 == 0]
        sage: L == L1
        True
        sage: L
        [0, 1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 21]

    ::

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1])
        sage: Q1.local_representation_conditions()
        This 1-dimensional form only represents square multiples of 1.
        sage: L = [m  for m in range(100)  if Q1.is_locally_represented_number(m)]
        sage: L
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    ::

        sage: Q0 = DiagonalQuadraticForm(ZZ, [])
        sage: Q0.local_representation_conditions()
        This 0-dimensional form only represents zero.
        sage: L = [m  for m in range(100)  if Q0.is_locally_represented_number(m)]
        sage: L
        [0]
    """
    local_repn_array: Incomplete
    dim: Incomplete
    exceptional_primes: Incomplete
    coeff: Incomplete
    def __init__(self, Q) -> None:
        """
        Take a :class:`QuadraticForm` and computes its local conditions (if
        they do not already exist).  The ``recompute_flag`` overrides the
        previously computed conditions if they exist, and stores the
        new conditions.

        INPUT:

        - ``Q`` -- Quadratic form over `\\ZZ`

        OUTPUT: a :class:`QuadraticFormLocalRepresentationConditions` object

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions
            sage: QuadraticFormLocalRepresentationConditions(Q)
            This form represents the p-adic integers Z_p for all primes p except
            [].  For these and the reals, we have:
                 Reals:   [0, +Infinity]
        """
    def __eq__(self, right) -> bool:
        """
        Determine if two sets of local conditions are equal.

        INPUT:

        - ``right`` -- a QuadraticFormLocalRepresentationConditions object

        OUTPUT: boolean

        EXAMPLES::

             sage: Q1 = DiagonalQuadraticForm(ZZ, [1,1])
             sage: Q2 = DiagonalQuadraticForm(ZZ, [1,1,1])
             sage: Q3 = DiagonalQuadraticForm(ZZ, [1,3,5,7])
             sage: Q4 = DiagonalQuadraticForm(ZZ, [1,1,1,1])

             sage: Q1.local_representation_conditions() == Q2.local_representation_conditions()
             False
             sage: Q1.local_representation_conditions() == Q3.local_representation_conditions()
             False
             sage: Q1.local_representation_conditions() == Q4.local_representation_conditions()
             False
             sage: Q2.local_representation_conditions() == Q3.local_representation_conditions()
             False
             sage: Q3.local_representation_conditions() == Q4.local_representation_conditions()
             True
        """
    def squareclass_vector(self, p) -> list:
        '''
        Return a list of integers which are normalized
        representatives for the `p`-adic rational squareclasses
        (or the real squareclasses) at the prime `p`.

        INPUT:

        - ``p`` -- a positive prime number or "infinity"

        OUTPUT: list of integers

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.squareclass_vector(5)
            [1, 2, 5, 10]
        '''
    def local_conditions_vector_for_prime(self, p) -> list:
        """
        Return a local representation vector for the (possibly infinite) prime `p`.

        INPUT:

        - ``p`` -- a positive prime number.  (Is 'infinity' allowed here?)

        OUTPUT: list of integers

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.local_conditions_vector_for_prime(2)
            [2, 0, 0, 0, +Infinity, 0, 0, 0, 0]
            sage: C.local_conditions_vector_for_prime(3)
            [3, 0, 0, 0, 0, None, None, None, None]
        """
    def is_universal_at_prime(self, p) -> bool:
        '''
        Determine if the (integer-valued/rational) quadratic form represents all of `\\ZZ_p`.

        INPUT:

        - ``p`` -- a positive prime number or "infinity"

        OUTPUT: boolean

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_universal_at_prime(2)
            False
            sage: C.is_universal_at_prime(3)
            True
            sage: C.is_universal_at_prime(infinity)
            False
        '''
    def is_universal_at_all_finite_primes(self) -> bool:
        """
        Determine if the quadratic form represents `\\ZZ_p` for all finite/non-archimedean primes.

        OUTPUT: boolean

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_universal_at_all_finite_primes()
            False

        ::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_universal_at_all_finite_primes()
            True
        """
    def is_universal_at_all_places(self) -> bool:
        """
        Determine if the quadratic form represents `\\ZZ_p` for all
        finite/non-archimedean primes, and represents all real numbers.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions

        ::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_universal_at_all_places()
            False

        ::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_universal_at_all_places()
            False

        ::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,-1])
            sage: C = QuadraticFormLocalRepresentationConditions(Q)     # long time (8.5 s)
            sage: C.is_universal_at_all_places()                        # long time
            True
        """
    def is_locally_represented_at_place(self, m, p) -> bool:
        '''
        Determine if the rational number `m` is locally represented by the
        quadratic form at the (possibly infinite) prime `p`.

        INPUT:

        - ``m`` -- integer

        - ``p`` -- a positive prime number or "infinity"

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_locally_represented_at_place(7, 2)
            False
            sage: C.is_locally_represented_at_place(1, 3)
            True
            sage: C.is_locally_represented_at_place(-1, infinity)
            False
            sage: C.is_locally_represented_at_place(1, infinity)
            True
            sage: C.is_locally_represented_at_place(0, infinity)
            True
        '''
    def is_locally_represented(self, m) -> bool:
        """
        Determine if the rational number `m` is locally represented by
        the quadratic form (allowing vectors with coefficients in `\\ZZ_p` at all
        places).

        INPUT:

        - ``m`` -- integer

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.quadratic_forms.quadratic_form__local_representation_conditions import QuadraticFormLocalRepresentationConditions

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: C = QuadraticFormLocalRepresentationConditions(Q)
            sage: C.is_locally_represented(7)
            False
            sage: C.is_locally_represented(28)
            False
            sage: C.is_locally_represented(11)
            True
            sage: C.is_locally_represented(QQ(1)/QQ(2))
            False
        """

def local_representation_conditions(self, recompute_flag: bool = False, silent_flag: bool = False):
    """
    .. WARNING::

        This only works correctly for forms in >=3 variables,
        which are locally universal at almost all primes!

    This class finds the local conditions for a number to be integrally
    represented by an integer-valued quadratic form.  These conditions
    are stored in ``self.__local_representability_conditions`` and
    consist of a list of 9 element vectors, with one for each prime
    with a local obstruction (though only the first 5 are meaningful
    unless `p=2`).  The first element is always the prime `p` where the
    local obstruction occurs, and the next 8 (or 4) entries represent
    square-classes in the `p`-adic integers `\\ZZ_p`, and are labeled by the
    `\\QQ_p` square-classes `t\\cdot (\\QQ_p)^2` with `t` given as follows:

    - for `p > 2`, ``[ *  1  u  p  u p  *  *  *  * ]``,

    - for `p = 2`, ``[ *  1  3  5  7  2  6  10  14 ]``.

    The integer appearing in each place tells us how `p`-divisible a
    number needs to be in that square-class in order to be locally
    represented by `Q`.  A negative number indicates that the entire `\\QQ_p`
    square-class is not represented, while a positive number `x` indicates
    that `t\\cdot p^{(2\\cdot x)} (\\ZZ_p)^2` is locally represented but `t\\cdot p^{(2\\cdot (x-1))}`
    `(\\ZZ_p)^2` is not.

    As an example, the vector ``[2  3  0  0  0  0  2  0  infinity]``
    tells us that all positive integers are locally represented at `p=2`
    except those of the forms:

    - `2^6\\cdot u\\cdot r^2` with `u = 1` (mod 8)

    - `2^5\\cdot u\\cdot r^2` with `u = 3` (mod 8)

    - `2\\cdot u\\cdot r^2` with `u = 7` (mod 8)

    At the real numbers, the vector which looks like ``[infinity, 0, infinity, None, None, None, None, None, None]``
    means that `Q` is negative definite (i.e., the 0 tells us all
    positive reals are represented).  The real vector always appears,
    and is listed before the other ones.

    OUTPUT:

    A list of 9-element vectors describing the representation
    obstructions at primes dividing the level.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [])
        sage: Q.local_representation_conditions()
        This 0-dimensional form only represents zero.

        sage: Q = DiagonalQuadraticForm(ZZ, [5])
        sage: Q.local_representation_conditions()
        This 1-dimensional form only represents square multiples of 5.

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1,1])
        sage: Q1.local_representation_conditions()
        This 2-dimensional form represents the p-adic integers of even
        valuation for all primes p except [2].
        For these and the reals, we have:
         Reals:   [0, +Infinity]
         p = 2:   [0, +Infinity, 0, +Infinity, 0, +Infinity, 0, +Infinity]

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q1.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [2].  For these and the reals, we have:
         Reals:   [0, +Infinity]
         p = 2:   [0, 0, 0, +Infinity, 0, 0, 0, 0]

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q1.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [].  For these and the reals, we have:
         Reals:   [0, +Infinity]

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,3,3])
        sage: Q1.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [3].  For these and the reals, we have:
         Reals:   [0, +Infinity]
         p = 3:   [0, 1, 0, 0]

        sage: Q2 = DiagonalQuadraticForm(ZZ, [2,3,3,3])
        sage: Q2.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [3].  For these and the reals, we have:
         Reals:   [0, +Infinity]
         p = 3:   [1, 0, 0, 0]

        sage: Q3 = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q3.local_representation_conditions()
        This form represents the p-adic integers Z_p for all primes p except
        [].  For these and the reals, we have:
         Reals:   [0, +Infinity]
    """
def is_locally_universal_at_prime(self, p) -> bool:
    '''
    Determine if the (integer-valued/rational) quadratic form represents all of `\\ZZ_p`.

    INPUT:

    - ``p`` -- a positive prime number or "infinity"

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.is_locally_universal_at_prime(2)
        True
        sage: Q.is_locally_universal_at_prime(3)
        True
        sage: Q.is_locally_universal_at_prime(5)
        True
        sage: Q.is_locally_universal_at_prime(infinity)
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.is_locally_universal_at_prime(2)
        False
        sage: Q.is_locally_universal_at_prime(3)
        True
        sage: Q.is_locally_universal_at_prime(5)
        True
        sage: Q.is_locally_universal_at_prime(infinity)
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,-1])
        sage: Q.is_locally_universal_at_prime(infinity)
        True
    '''
def is_locally_universal_at_all_primes(self) -> bool:
    """
    Determine if the quadratic form represents `\\ZZ_p` for all finite/non-archimedean primes.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.is_locally_universal_at_all_primes()
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.is_locally_universal_at_all_primes()
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.is_locally_universal_at_all_primes()
        False
    """
def is_locally_universal_at_all_places(self) -> bool:
    """
    Determine if the quadratic form represents `\\ZZ_p` for all
    finite/non-archimedean primes, and represents all real numbers.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.is_locally_universal_at_all_places()
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.is_locally_universal_at_all_places()
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,-1])
        sage: Q.is_locally_universal_at_all_places()        # long time (8.5 s)
        True
    """
def is_locally_represented_number_at_place(self, m, p) -> bool:
    """
    Determine if the rational number `m` is locally represented by the
    quadratic form at the (possibly infinite) prime `p`.

    INPUT:

    - ``m`` -- integer

    - ``p`` -- a prime number > 0 or 'infinity'

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.is_locally_represented_number_at_place(7, infinity)
        True
        sage: Q.is_locally_represented_number_at_place(7, 2)
        False
        sage: Q.is_locally_represented_number_at_place(7, 3)
        True
        sage: Q.is_locally_represented_number_at_place(7, 5)
        True
        sage: Q.is_locally_represented_number_at_place(-1, infinity)
        False
        sage: Q.is_locally_represented_number_at_place(-1, 2)
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,-1])
        sage: Q.is_locally_represented_number_at_place(7, infinity)     # long time (8.5 s)
        True
        sage: Q.is_locally_represented_number_at_place(7, 2)            # long time
        True
        sage: Q.is_locally_represented_number_at_place(7, 3)            # long time
        True
        sage: Q.is_locally_represented_number_at_place(7, 5)            # long time
        True
    """
def is_locally_represented_number(self, m) -> bool:
    """
    Determine if the rational number `m` is locally represented
    by the quadratic form.

    INPUT:

    - ``m`` -- integer

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.is_locally_represented_number(2)
        True
        sage: Q.is_locally_represented_number(7)
        False
        sage: Q.is_locally_represented_number(-1)
        False
        sage: Q.is_locally_represented_number(28)
        False
        sage: Q.is_locally_represented_number(0)
        True
    """
