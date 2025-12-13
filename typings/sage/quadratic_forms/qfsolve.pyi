from sage.matrix.constructor import Matrix as Matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def qfsolve(G):
    """
    Find a solution `x = (x_0,...,x_n)` to `x G x^t = 0` for an
    `n \\times n`-matrix ``G`` over `\\QQ`.

    OUTPUT:

    If a solution exists, return a vector of rational numbers `x`.
    Otherwise, returns `-1` if no solution exists over the reals or a
    prime `p` if no solution exists over the `p`-adic field `\\QQ_p`.

    ALGORITHM:

    Uses PARI/GP function :pari:`qfsolve`.

    EXAMPLES::

        sage: from sage.quadratic_forms.qfsolve import qfsolve
        sage: M = Matrix(QQ, [[0, 0, -12], [0, -12, 0], [-12, 0, -1]]); M
        [  0   0 -12]
        [  0 -12   0]
        [-12   0  -1]
        sage: sol = qfsolve(M); sol
        (1, 0, 0)
        sage: sol.parent()
        Vector space of dimension 3 over Rational Field

        sage: M = Matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        sage: ret = qfsolve(M); ret
        -1
        sage: ret.parent()
        Integer Ring

        sage: M = Matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, -7]])
        sage: qfsolve(M)
        7

        sage: M = Matrix(QQ, [[3, 0, 0, 0], [0, 5, 0, 0], [0, 0, -7, 0], [0, 0, 0, -11]])
        sage: qfsolve(M)
        (3, 4, -3, -2)
    """
def qfparam(G, sol):
    """
    Parametrize the conic defined by the matrix `G`.

    INPUT:

    - ``G`` -- a `3 \\times 3`-matrix over `\\QQ`

    - ``sol`` -- a triple of rational numbers providing a solution
      to `x\\cdot G\\cdot x^t = 0`

    OUTPUT:

    A triple of polynomials that parametrizes all solutions of
    `x\\cdot G\\cdot x^t = 0` up to scaling.

    ALGORITHM:

    Uses PARI/GP function :pari:`qfparam`.

    EXAMPLES::

        sage: from sage.quadratic_forms.qfsolve import qfsolve, qfparam
        sage: M = Matrix(QQ, [[0, 0, -12], [0, -12, 0], [-12, 0, -1]]); M
        [  0   0 -12]
        [  0 -12   0]
        [-12   0  -1]
        sage: sol = qfsolve(M)
        sage: ret = qfparam(M, sol); ret
        (-12*t^2 - 1, 24*t, 24)
        sage: ret.parent()
        Ambient free module of rank 3 over the principal ideal domain
         Univariate Polynomial Ring in t over Rational Field
    """
def solve(self, c: int = 0):
    """
    Return a vector `x` such that ``self(x) == c``.

    INPUT:

    - ``c`` -- (default: 0) a rational number

    OUTPUT: a nonzero vector `x` satisfying ``self(x) == c``

    ALGORITHM:

    Uses PARI's :pari:`qfsolve`. Algorithm described by Jeroen Demeyer; see comments on :issue:`19112`

    EXAMPLES::

        sage: F = DiagonalQuadraticForm(QQ, [1, -1]); F
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1 0 ]
        [ * -1 ]
        sage: F.solve()
        (1, 1)
        sage: F.solve(1)
        (1, 0)
        sage: F.solve(2)
        (3/2, -1/2)
        sage: F.solve(3)
        (2, -1)

    ::

        sage: F = DiagonalQuadraticForm(QQ, [1, 1, 1, 1])
        sage: F.solve(7)
        (1, 2, -1, -1)
        sage: F.solve()
        Traceback (most recent call last):
        ...
        ArithmeticError: no solution found (local obstruction at -1)

    ::

        sage: Q = QuadraticForm(QQ, 2, [17, 94, 130])
        sage: x = Q.solve(5); x
        (17, -6)
        sage: Q(x)
        5

        sage: Q.solve(6)
        Traceback (most recent call last):
        ...
        ArithmeticError: no solution found (local obstruction at 3)

        sage: G = DiagonalQuadraticForm(QQ, [5, -3, -2])
        sage: x = G.solve(10); x
        (3/2, -1/2, 1/2)
        sage: G(x)
        10

        sage: F = DiagonalQuadraticForm(QQ, [1, -4])
        sage: x = F.solve(); x
        (2, 1)
        sage: F(x)
        0

    ::

        sage: F = QuadraticForm(QQ, 4, [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]); F
        Quadratic form in 4 variables over Rational Field with coefficients:
        [ 0 0 1 0 ]
        [ * 0 0 1 ]
        [ * * 0 0 ]
        [ * * * 0 ]
        sage: F.solve(23)
        (23, 0, 1, 0)

    Other fields besides the rationals are currently not supported::

        sage: F = DiagonalQuadraticForm(GF(11), [1, 1])
        sage: F.solve()
        Traceback (most recent call last):
        ...
        TypeError: solving quadratic forms is only implemented over QQ
    """
