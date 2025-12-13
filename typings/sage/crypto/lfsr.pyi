from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.all import Sequence as Sequence

def lfsr_sequence(key, fill, n):
    """
    Create an LFSR sequence.

    INPUT:

    - ``key`` -- list of finite field elements, `[c_0, c_1,\\dots, c_k]`

    - ``fill`` -- the list of the initial terms of the LFSR sequence, `[x_0,x_1,\\dots,x_k]`

    - ``n`` -- number of terms of the sequence that the function returns

    OUTPUT:

    The LFSR sequence defined by `x_{n+1} = c_kx_n+...+c_0x_{n-k}` for `n \\geq k`.

    EXAMPLES::

        sage: F = GF(2); l = F(1); o = F(0)
        sage: F = GF(2); S = LaurentSeriesRing(F,'x'); x = S.gen()
        sage: fill = [l,l,o,l]; key = [1,o,o,l]; n = 20
        sage: L = lfsr_sequence(key,fill,20); L
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        sage: from sage.matrix.berlekamp_massey import berlekamp_massey
        sage: g = berlekamp_massey(L); g
        x^4 + x^3 + 1
        sage: (1)/(g.reverse()+O(x^20))
        1 + x + x^2 + x^3 + x^5 + x^7 + x^8 + x^11 + x^15 + x^16 + x^17 + x^18 + O(x^20)
        sage: (1+x^2)/(g.reverse()+O(x^20))
        1 + x + x^4 + x^8 + x^9 + x^10 + x^11 + x^13 + x^15 + x^16 + x^19 + O(x^20)
        sage: (1+x^2+x^3)/(g.reverse()+O(x^20))
        1 + x + x^3 + x^5 + x^6 + x^9 + x^13 + x^14 + x^15 + x^16 + x^18 + O(x^20)
        sage: fill = [l,l,o,l]; key = [l,o,o,o]; n = 20
        sage: L = lfsr_sequence(key,fill,20); L
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
        sage: g = berlekamp_massey(L); g
        x^4 + 1
        sage: (1+x)/(g.reverse()+O(x^20))
        1 + x + x^4 + x^5 + x^8 + x^9 + x^12 + x^13 + x^16 + x^17 + O(x^20)
        sage: (1+x+x^3)/(g.reverse()+O(x^20))
        1 + x + x^3 + x^4 + x^5 + x^7 + x^8 + x^9 + x^11 + x^12 + x^13 + x^15 + x^16 + x^17 + x^19 + O(x^20)
    """
def lfsr_autocorrelation(L, p, k):
    """
    INPUT:

    - ``L`` -- a periodic sequence of elements of ZZ or GF(2); must have length `p`

    - ``p`` -- the period of `L`

    - ``k`` -- integer between `0` and `p`

    OUTPUT: autocorrelation sequence of `L`

    EXAMPLES::

        sage: F = GF(2)
        sage: o = F(0)
        sage: l = F(1)
        sage: key = [l,o,o,l]; fill = [l,l,o,l]; n = 20
        sage: s = lfsr_sequence(key,fill,n)
        sage: lfsr_autocorrelation(s,15,7)
        4/15
        sage: lfsr_autocorrelation(s,int(15),7)
        4/15
    """
def lfsr_connection_polynomial(s):
    """
    INPUT:

    - ``s`` -- a sequence of elements of a finite field of even length

    OUTPUT:

    - ``C(x)`` -- the connection polynomial of the minimal LFSR

    This implements the algorithm in section 3 of J. L. Massey's article
    [Mas1969]_.

    EXAMPLES::

        sage: F = GF(2)
        sage: F
        Finite Field of size 2
        sage: o = F(0); l = F(1)
        sage: key = [l,o,o,l]; fill = [l,l,o,l]; n = 20
        sage: s = lfsr_sequence(key,fill,n); s
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        sage: lfsr_connection_polynomial(s)
        x^4 + x + 1
        sage: from sage.matrix.berlekamp_massey import berlekamp_massey
        sage: berlekamp_massey(s)
        x^4 + x^3 + 1

    Notice that ``berlekamp_massey`` returns the reverse of the connection
    polynomial (and is potentially must faster than this implementation).
    """
