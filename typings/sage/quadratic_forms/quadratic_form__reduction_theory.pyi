from sage.matrix.constructor import matrix as matrix
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.mrange import mrange as mrange
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ

def reduced_binary_form1(self):
    """
    Reduce the form `ax^2 + bxy+cy^2` to satisfy the reduced condition `|b| \\le
    a \\le c`, with `b \\ge 0` if `a = c`. This reduction occurs within the
    proper class, so all transformations are taken to have determinant 1.

    EXAMPLES::

        sage: QuadraticForm(ZZ, 2, [5,5,2]).reduced_binary_form1()                      # needs sage.symbolic
        (
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 2 -1 ]
        [ * 2 ]                                                            ,
        <BLANKLINE>
        [ 0 -1]
        [ 1  1]
        )

    TESTS::

        sage: QuadraticForm(ZZ, 2, [4,-7,6]).reduced_binary_form1()[0]                  # needs sage.symbolic
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 3 -1 ]
        [ * 4 ]

        sage: QuadraticForm(ZZ, 3, [1,2,3,4,5,6]).reduced_binary_form1()                # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: only available for binary forms
    """
def reduced_ternary_form__Dickson(self) -> None:
    '''
    Find the unique reduced ternary form according to the conditions
    of Dickson\'s "Studies in the Theory of Numbers", pp164-171.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
        sage: Q.reduced_ternary_form__Dickson()
        Traceback (most recent call last):
        ...
        NotImplementedError
    '''
def reduced_binary_form(self):
    """
    Find a form which is reduced in the sense that no further binary
    form reductions can be done to reduce the original form.

    EXAMPLES::

        sage: QuadraticForm(ZZ, 2, [5,5,2]).reduced_binary_form()                       # needs sage.symbolic
        (
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 2 -1 ]
        [ * 2 ]                                                            ,
        <BLANKLINE>
        [ 0 -1]
        [ 1  1]
        )
    """
def minkowski_reduction(self):
    '''
    Find a Minkowski-reduced form equivalent to the given one.

    This means that

    .. MATH::

            Q(v_k) \\leq Q(s_1\\cdot v_1 + ... + s_n\\cdot v_n)

    for all `s_i` where `\\gcd(s_k, ... s_n) = 1`.

    .. NOTE::

        When `Q` has dim `\\leq 4` we can take all `s_i` in `\\{1, 0, -1\\}`.

    REFERENCES:

    - Schulze-Pillot\'s paper on "An algorithm for computing genera
      of ternary and quaternary quadratic forms", p138.
    - Donaldson\'s 1979 paper "Minkowski Reduction of Integral Matrices", p203.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 4, [30, 17, 11, 12, 29, 25, 62, 64, 25, 110])
        sage: Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 30 17 11 12 ]
        [ * 29 25 62 ]
        [ * * 64 25 ]
        [ * * * 110 ]
        sage: Q.minkowski_reduction()
        (
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 30 17 11 -5 ]
        [ * 29 25 4 ]
        [ * * 64 0 ]
        [ * * * 77 ]                                                       ,
        <BLANKLINE>
        [ 1  0  0  0]
        [ 0  1  0 -1]
        [ 0  0  1  0]
        [ 0  0  0  1]
        )

    ::

        sage: Q = QuadraticForm(ZZ,4,[1, -2, 0, 0, 2, 0, 0, 2, 0, 2])
        sage: Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 -2 0 0 ]
        [ * 2 0 0 ]
        [ * * 2 0 ]
        [ * * * 2 ]
        sage: Q.minkowski_reduction()
        (
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 0 0 0 ]
        [ * 1 0 0 ]
        [ * * 2 0 ]
        [ * * * 2 ]                                                        ,
        <BLANKLINE>
        [1 1 0 0]
        [0 1 0 0]
        [0 0 1 0]
        [0 0 0 1]
        )

    TESTS::

        sage: Q = QuadraticForm(ZZ,5,[2,2,0,0,0,2,2,0,0,2,2,0,2,2,2])
        sage: Q.Gram_matrix()
        [2 1 0 0 0]
        [1 2 1 0 0]
        [0 1 2 1 0]
        [0 0 1 2 1]
        [0 0 0 1 2]
        sage: Q.minkowski_reduction()
        Traceback (most recent call last):
        ...
        NotImplementedError: this algorithm is only for dimensions less than 5

        sage: Q = QuadraticForm(ZZ,2,[4,-11,6])
        sage: Q.minkowski_reduction()
        Traceback (most recent call last):
        ...
        TypeError: Minkowski reduction only works for positive definite forms
    '''
def minkowski_reduction_for_4vars__SP(self):
    '''
    Find a Minkowski-reduced form equivalent to the given one.
    This means that

    .. MATH::

        Q(v_k) \\leq Q(s_1\\cdot v_1 + ... + s_n\\cdot v_n)

    for all `s_i` where GCD(`s_k, ... s_n`) = 1.

    .. NOTE::

        When `Q` has dim `\\leq 4`, we can take all `s_i` in `\\{1, 0, -1\\}`.

    REFERENCES:

    - Schulze-Pillot\'s paper on "An algorithm for computing genera
      of ternary and quaternary quadratic forms", p138.
    - Donaldson\'s 1979 paper "Minkowski Reduction of Integral Matrices", p203.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 4, [30,17,11,12,29,25,62,64,25,110]); Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 30 17 11 12 ]
        [ * 29 25 62 ]
        [ * * 64 25 ]
        [ * * * 110 ]
        sage: Q.minkowski_reduction_for_4vars__SP()
        (
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 29 -17 25 4 ]
        [ * 30 -11 5 ]
        [ * * 64 0 ]
        [ * * * 77 ]                                                       ,
        <BLANKLINE>
        [ 0  1  0  0]
        [ 1  0  0 -1]
        [ 0  0  1  0]
        [ 0  0  0  1]
        )

    TESTS::

        sage: Q = QuadraticForm(ZZ, 2, [3,4,5])
        sage: Q.minkowski_reduction_for_4vars__SP()
        Traceback (most recent call last):
        ...
        TypeError: the given quadratic form has 2 != 4 variables
    '''
