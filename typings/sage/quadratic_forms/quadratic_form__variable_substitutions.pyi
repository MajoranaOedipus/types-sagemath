def swap_variables(self, r, s, in_place: bool = False):
    """
    Switch the variables `x_r` and `x_s` in the quadratic form
    (replacing the original form if the ``in_place`` flag is True).

    INPUT:

    - ``r``, ``s`` -- integers `\\geq 0`

    OUTPUT:

    a :class:`QuadraticForm` (by default, otherwise none)

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 4, range(1,11))
        sage: Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 2 3 4 ]
        [ * 5 6 7 ]
        [ * * 8 9 ]
        [ * * * 10 ]

        sage: Q.swap_variables(0,2)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 8 6 3 9 ]
        [ * 5 2 7 ]
        [ * * 1 4 ]
        [ * * * 10 ]

        sage: Q.swap_variables(0,2).swap_variables(0,2)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 2 3 4 ]
        [ * 5 6 7 ]
        [ * * 8 9 ]
        [ * * * 10 ]
    """
def multiply_variable(self, c, i, in_place: bool = False):
    """
    Replace the variables `x_i` by `c\\cdot x_i` in the quadratic form
    (replacing the original form if the ``in_place`` flag is True).

    Here `c` must be an element of the base ring defining the
    quadratic form.

    INPUT:

    - ``c`` -- an element of ``self.base_ring()``

    - ``i`` -- integer `\\geq 0`

    OUTPUT: a :class:`QuadraticForm` (by default, otherwise none)

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,9,5,7])
        sage: Q.multiply_variable(5, 0)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 25 0 0 0 ]
        [ * 9 0 0 ]
        [ * * 5 0 ]
        [ * * * 7 ]
    """
def divide_variable(self, c, i, in_place: bool = False):
    """
    Replace the variables `x_i` by `(x_i)/c` in the quadratic form
    (replacing the original form if the ``in_place`` flag is True).

    Here `c` must be an element of the base ring defining the
    quadratic form, and the division must be defined in the base
    ring.

    INPUT:

    - ``c`` -- an element of ``self.base_ring()``

    - ``i`` -- integer `\\geq 0`

    OUTPUT:

    a :class:`QuadraticForm` (by default, otherwise none)

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,9,5,7])
        sage: Q.divide_variable(3, 1)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 0 0 0 ]
        [ * 1 0 0 ]
        [ * * 5 0 ]
        [ * * * 7 ]
    """
def scale_by_factor(self, c, change_value_ring_flag: bool = False):
    """
    Scale the values of the quadratic form by the number `c`, if
    this is possible while still being defined over its base ring.

    If the flag is set to true, then this will alter the value ring
    to be the field of fractions of the original ring (if necessary).

    INPUT:

    - ``c`` -- a scalar in the fraction field of the value ring of the form

    OUTPUT: a quadratic form of the same dimension

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [3,9,18,27])
        sage: Q.scale_by_factor(3)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 9 0 0 0 ]
        [ * 27 0 0 ]
        [ * * 54 0 ]
        [ * * * 81 ]

        sage: Q.scale_by_factor(1/3)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 0 0 0 ]
        [ * 3 0 0 ]
        [ * * 6 0 ]
        [ * * * 9 ]
    """
def extract_variables(QF, var_indices):
    """
    Extract the variables (in order) whose indices are listed in
    ``var_indices``, to give a new quadratic form.

    INPUT:

    - ``var_indices`` -- list of integers `\\geq 0`

    OUTPUT: a :class:`QuadraticForm`

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 4, range(10)); Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 0 1 2 3 ]
        [ * 4 5 6 ]
        [ * * 7 8 ]
        [ * * * 9 ]
        sage: Q.extract_variables([1,3])
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 4 6 ]
        [ * 9 ]
    """
def elementary_substitution(self, c, i, j, in_place: bool = False):
    """
    Perform the substitution `x_i \\longmapsto x_i + c\\cdot x_j` (replacing the
    original form if the ``in_place`` flag is True).

    INPUT:

    - ``c`` -- an element of ``self.base_ring()``

    - ``i``, ``j`` -- integers `\\geq 0`

    OUTPUT:

    a :class:`QuadraticForm` (by default, otherwise none)

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 4, range(1,11)); Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 2 3 4 ]
        [ * 5 6 7 ]
        [ * * 8 9 ]
        [ * * * 10 ]

        sage: Q.elementary_substitution(c=1, i=0, j=3)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 2 3 6 ]
        [ * 5 6 9 ]
        [ * * 8 12 ]
        [ * * * 15 ]

    ::

        sage: R = QuadraticForm(ZZ, 4, range(1,11)); R
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 2 3 4 ]
        [ * 5 6 7 ]
        [ * * 8 9 ]
        [ * * * 10 ]

    ::

        sage: M = Matrix(ZZ, 4, 4, [1,0,0,1, 0,1,0,0, 0,0,1,0, 0,0,0,1]); M
        [1 0 0 1]
        [0 1 0 0]
        [0 0 1 0]
        [0 0 0 1]
        sage: R(M)
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 2 3 6 ]
        [ * 5 6 9 ]
        [ * * 8 12 ]
        [ * * * 15 ]
    """
def add_symmetric(self, c, i, j, in_place: bool = False):
    """
    Perform the substitution `x_j \\longmapsto x_j + c\\cdot x_i`, which has the
    effect (on associated matrices) of symmetrically adding
    `c` times the `j`-th row/column to the `i`-th row/column.

    NOTE: This is meant for compatibility with previous code,
    which implemented a matrix model for this class.  It is used
    in the method :meth:`local_normal_form`.

    INPUT:

    - ``c`` -- an element of ``self.base_ring()``

    - ``i``, ``j`` -- integers `\\geq 0`

    OUTPUT:

    a :class:`QuadraticForm` (by default, otherwise none)

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, range(1,7)); Q
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 2 3 ]
        [ * 4 5 ]
        [ * * 6 ]
        sage: Q.add_symmetric(-1, 1, 0)
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 0 3 ]
        [ * 3 2 ]
        [ * * 6 ]
        sage: Q.add_symmetric(-3/2, 2, 0)     # ERROR: -3/2 isn't in the base ring ZZ
        Traceback (most recent call last):
        ...
        RuntimeError: this coefficient cannot be coerced
        to an element of the base ring for the quadratic form

    ::

        sage: Q = QuadraticForm(QQ, 3, range(1,7)); Q
        Quadratic form in 3 variables over Rational Field with coefficients:
        [ 1 2 3 ]
        [ * 4 5 ]
        [ * * 6 ]
        sage: Q.add_symmetric(-3/2, 2, 0)
        Quadratic form in 3 variables over Rational Field with coefficients:
        [ 1 2 0 ]
        [ * 4 2 ]
        [ * * 15/4 ]
    """
