from . import hyperelliptic_generic as hyperelliptic_generic
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.schemes.curves.projective_curve import ProjectivePlaneCurve_field as ProjectivePlaneCurve_field

class HyperellipticCurve_rational_field(hyperelliptic_generic.HyperellipticCurve_generic, ProjectivePlaneCurve_field):
    def matrix_of_frobenius(self, p, prec: int = 20):
        """
        Compute the matrix of Frobenius on Monsky-Washnitzer cohomology using
        the `p`-adic field with precision ``prec``.

        This function is essentially a wrapper function of
        :meth:`sage.schemes.hyperelliptic_curves.monsky_washnitzer.matrix_of_frobenius_hyperelliptic`.

        INPUT:

        - ``p`` -- prime integer or pAdic ring / field; if ``p`` is an integer,
          constructs a ``pAdicField`` with ``p`` to compute the matrix of
          Frobenius, otherwise uses the supplied pAdic ring or field

        - ``prec`` -- (optional) if ``p`` is an prime integer, the `p`-adic
          precision of the coefficient ring constructed

        EXAMPLES::

            sage: K = pAdicField(5, prec=3)
            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5 - 2*x + 3)
            sage: H.matrix_of_frobenius(K)
            [            4*5 + O(5^3)       5 + 2*5^2 + O(5^3) 2 + 3*5 + 2*5^2 + O(5^3)     2 + 5 + 5^2 + O(5^3)]
            [      3*5 + 5^2 + O(5^3)             3*5 + O(5^3)             4*5 + O(5^3)         2 + 5^2 + O(5^3)]
            [    4*5 + 4*5^2 + O(5^3)     3*5 + 2*5^2 + O(5^3)       5 + 3*5^2 + O(5^3)     2*5 + 2*5^2 + O(5^3)]
            [            5^2 + O(5^3)       5 + 4*5^2 + O(5^3)     4*5 + 3*5^2 + O(5^3)             2*5 + O(5^3)]

        You can also pass directly a prime `p` with to construct a pAdic field with precision
        ``prec``::

            sage: H.matrix_of_frobenius(3, prec=2)
            [        O(3^2)     3 + O(3^2)         O(3^2)         O(3^2)]
            [    3 + O(3^2)         O(3^2)         O(3^2) 2 + 3 + O(3^2)]
            [  2*3 + O(3^2)         O(3^2)         O(3^2)    3^-1 + O(3)]
            [        O(3^2)         O(3^2)     3 + O(3^2)         O(3^2)]
        """
    def lseries(self, prec: int = 53):
        """
        Return the `L`-series of this hyperelliptic curve of genus 2.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: C = HyperellipticCurve(x^2+x, x^3+x^2+1)
            sage: C.lseries()
            PARI L-function associated to Hyperelliptic Curve
            over Rational Field defined by y^2 + (x^3 + x^2 + 1)*y = x^2 + x
        """
