from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.padics.polynomial_padic import Polynomial_padic as Polynomial_padic
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial, Polynomial_generic_dense as Polynomial_generic_dense

class Polynomial_padic_flat(Polynomial_generic_dense, Polynomial_padic):
    def __init__(self, parent, x=None, check: bool = True, is_gen: bool = False, construct: bool = False, absprec=None) -> None:
        """
        TESTS:

        Check that :issue:`13620` has been fixed::

            sage: K = ZpFM(3)
            sage: R.<t> = K[]
            sage: R(R.zero())
            0
        """
