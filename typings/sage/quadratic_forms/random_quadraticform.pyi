from sage.categories.rings import Rings as Rings
from sage.quadratic_forms.quadratic_form import QuadraticForm as QuadraticForm
from sage.quadratic_forms.ternary_qf import TernaryQF as TernaryQF
from sage.rings.integer_ring import ZZ as ZZ

def random_quadraticform(R, n, rand_arg_list=None):
    """
    Create a random quadratic form in `n` variables defined over the ring `R`.

    The last (and optional) argument ``rand_arg_list`` is a list of at most 3
    elements which is passed (as at most 3 separate variables) into the method
    ``R.random_element()``.

    INPUT:

    - ``R`` -- a ring
    - ``n`` -- integer `\\ge 0`
    - ``rand_arg_list`` -- list of at most 3 arguments which can be taken by
      ``R.random_element()``

    OUTPUT: a quadratic form over the ring `R`

    EXAMPLES::

        sage: random_quadraticform(ZZ, 3, [1,5])    # random
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 3 2 3 ]
        [ * 1 4 ]
        [ * * 3 ]

        sage: random_quadraticform(ZZ, 3, [-5,5])    # random
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 3 2 -5 ]
        [ * 2 -2 ]
        [ * * -5 ]

        sage: random_quadraticform(ZZ, 3, [-50,50])    # random
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 8 -23 ]
        [ * 0 0 ]
        [ * * 6 ]

    TESTS::

        sage: random_quadraticform(ZZ, 3, [1,2,3,4])
        Traceback (most recent call last):
        ...
        TypeError: the list of randomness arguments can have at most 3 elements
    """
def random_quadraticform_with_conditions(R, n, condition_list=[], rand_arg_list=None):
    """
    Create a random quadratic form in `n` variables defined over the ring `R`
    satisfying a list of boolean (i.e. True/False) conditions.

    The conditions `c` appearing in the list must be boolean functions which
    can be called either as ``Q.c()`` or ``c(Q)``, where ``Q`` is the random
    quadratic form.

    The last (and optional) argument ``rand_arg_list`` is a list of at most 3
    elements which is passed (as at most 3 separate variables) into the method
    ``R.random_element()``.

    EXAMPLES::

        sage: check = QuadraticForm.is_positive_definite
        sage: Q = random_quadraticform_with_conditions(ZZ, 3, [check], [-5, 5])
        sage: Q    # random
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 3 -2 -5 ]
        [ * 2 2 ]
        [ * * 3 ]
    """
def random_ternaryqf(rand_arg_list=None):
    '''
    Create a random ternary quadratic form.

    The last (and optional) argument ``rand_arg_list`` is a list of at most 3
    elements which is passed (as at most 3 separate variables) into the method
    ``R.random_element()``.

    INPUT:

    - ``rand_arg_list`` -- list of at most 3 arguments which can be taken by
      ``R.random_element()``

    OUTPUT: a ternary quadratic form

    EXAMPLES::

        sage: random_ternaryqf()  # random
        Ternary quadratic form with integer coefficients:
        [1 1 4]
        [-1 1 -1]
        sage: random_ternaryqf([-1, 2])  # random
        Ternary quadratic form with integer coefficients:
        [1 0 1]
        [-1 -1 -1]
        sage: random_ternaryqf([-10, 10, "uniform"])  # random
        Ternary quadratic form with integer coefficients:
        [7 -8 2]
        [0 3 -6]
    '''
def random_ternaryqf_with_conditions(condition_list=[], rand_arg_list=None):
    """
    Create a random ternary quadratic form satisfying a list of boolean
    (i.e. True/False) conditions.

    The conditions `c` appearing in the list must be boolean functions which
    can be called either as ``Q.c()`` or ``c(Q)``, where ``Q`` is the random
    ternary quadratic form.

    The last (and optional) argument ``rand_arg_list`` is a list of at most 3
    elements which is passed (as at most 3 separate variables) into the method
    ``R.random_element()``.

    EXAMPLES::

        sage: check = TernaryQF.is_positive_definite
        sage: Q = random_ternaryqf_with_conditions([check], [-5, 5])
        sage: Q    # random
        Ternary quadratic form with integer coefficients:
        [3 4 2]
        [2 -2 -1]
    """
