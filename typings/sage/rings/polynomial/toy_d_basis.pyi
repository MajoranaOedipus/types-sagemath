from sage.arith.functions import lcm as lcm
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.toy_buchberger import inter_reduction as inter_reduction
from sage.structure.sequence import Sequence as Sequence

def spol(g1, g2):
    """
    Return the S-Polynomial of ``g_1`` and ``g_2``.

    Let `a_i t_i` be `LT(g_i)`, `b_i = a/a_i` with `a = LCM(a_i,a_j)`,
    and `s_i = t/t_i` with `t = LCM(t_i,t_j)`. Then the S-Polynomial
    is defined as: `b_1s_1g_1 - b_2s_2g_2`.

    INPUT:

    - ``g1`` -- polynomial
    - ``g2`` -- polynomial

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_d_basis import spol
        sage: P.<x, y, z> = PolynomialRing(IntegerRing(), 3, order='lex')
        sage: f = x^2 - 1
        sage: g = 2*x*y - z
        sage: spol(f,g)
        x*z - 2*y
    """
def gpol(g1, g2):
    """
    Return the G-Polynomial of ``g_1`` and ``g_2``.

    Let `a_i t_i` be `LT(g_i)`, `a = a_i*c_i + a_j*c_j` with `a =
    GCD(a_i,a_j)`, and `s_i = t/t_i` with `t = LCM(t_i,t_j)`. Then the
    G-Polynomial is defined as: `c_1s_1g_1 - c_2s_2g_2`.

    INPUT:

    - ``g1`` -- polynomial
    - ``g2`` -- polynomial

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_d_basis import gpol
        sage: P.<x, y, z> = PolynomialRing(IntegerRing(), 3, order='lex')
        sage: f = x^2 - 1
        sage: g = 2*x*y - z
        sage: gpol(f,g)
        x^2*y - y
    """
def LM(f): ...
def LC(f): ...
def d_basis(F, strat: bool = True):
    """
    Return the `d`-basis for the Ideal ``F`` as defined in [BW1993]_.

    INPUT:

    - ``F`` -- an ideal
    - ``strat`` -- use update strategy (default: ``True``)

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_d_basis import d_basis
        sage: A.<x,y> = PolynomialRing(ZZ, 2)
        sage: f = -y^2 - y + x^3 + 7*x + 1
        sage: fx = f.derivative(x)
        sage: fy = f.derivative(y)
        sage: I = A.ideal([f,fx,fy])
        sage: gb = d_basis(I); gb                                                       # needs sage.libs.singular
        [x - 2020, y - 11313, 22627]
    """
def select(P):
    """
    The normal selection strategy.

    INPUT:

    - ``P`` -- list of critical pairs

    OUTPUT: an element of P

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_d_basis import select
        sage: A.<x,y> = PolynomialRing(ZZ, 2)
        sage: f = -y^2 - y + x^3 + 7*x + 1
        sage: fx = f.derivative(x)
        sage: fy = f.derivative(y)
        sage: G = [f, fx, fy]
        sage: B = set((f1, f2) for f1 in G for f2 in G if f1 != f2)
        sage: select(B)
        (-2*y - 1, 3*x^2 + 7)
    """
def update(G, B, h):
    """
    Update ``G`` using the list of critical pairs ``B`` and the
    polynomial ``h`` as presented in [BW1993]_, page 230. For this,
    Buchberger's first and second criterion are tested.

    This function uses the Gebauer-Moeller Installation.

    INPUT:

    - ``G`` -- an intermediate Groebner basis
    - ``B`` -- list of critical pairs
    - ``h`` -- a polynomial

    OUTPUT: ``G,B`` where ``G`` and ``B`` are updated

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_d_basis import update
        sage: A.<x,y> = PolynomialRing(ZZ, 2)
        sage: G = set([3*x^2 + 7, 2*y + 1, x^3 - y^2 + 7*x - y + 1])
        sage: B = set()
        sage: h = x^2*y - x^2 + y - 3
        sage: update(G,B,h)
        ({2*y + 1, 3*x^2 + 7, x^2*y - x^2 + y - 3, x^3 - y^2 + 7*x - y + 1},
         {(x^2*y - x^2 + y - 3, 2*y + 1),
          (x^2*y - x^2 + y - 3, 3*x^2 + 7),
          (x^2*y - x^2 + y - 3, x^3 - y^2 + 7*x - y + 1)})
    """
