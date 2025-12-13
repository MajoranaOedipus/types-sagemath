from .l_series_gross_zagier_coeffs import gross_zagier_L_series as gross_zagier_L_series
from sage.lfunctions.dokchitser import Dokchitser as Dokchitser
from sage.modular.dirichlet import kronecker_character as kronecker_character
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class GrossZagierLseries(SageObject):
    def __init__(self, E, A, prec: int = 53) -> None:
        """
        Class for the Gross-Zagier `L`-series.

        This is attached to a pair `(E,A)` where `E` is an elliptic curve over
        `\\QQ` and `A` is an ideal class in an imaginary quadratic number field.

        For the exact definition, in the more general setting of modular forms
        instead of elliptic curves, see section IV of [GZ1986]_.

        INPUT:

        - ``E`` -- an elliptic curve over `\\QQ`

        - ``A`` -- an ideal class in an imaginary quadratic number field

        - ``prec`` -- integer (default: 53); giving the required precision

        EXAMPLES::

            sage: e = EllipticCurve('37a')
            sage: K.<a> = QuadraticField(-40)
            sage: A = K.class_group().gen(0)
            sage: from sage.modular.modform.l_series_gross_zagier import GrossZagierLseries
            sage: G = GrossZagierLseries(e, A)

        TESTS::

            sage: K.<b> = QuadraticField(131)
            sage: A = K.class_group().one()
            sage: G = GrossZagierLseries(e, A)
            Traceback (most recent call last):
            ...
            ValueError: A is not an ideal class in an imaginary quadratic field
        """
    def __call__(self, s, der: int = 0):
        """
        Return the value at `s`.

        INPUT:

        - ``s`` -- complex number

        - ``der`` -- order of derivative (default: 0)

        EXAMPLES::

            sage: e = EllipticCurve('37a')
            sage: K.<a> = QuadraticField(-40)
            sage: A = K.class_group().gen(0)
            sage: from sage.modular.modform.l_series_gross_zagier import GrossZagierLseries
            sage: G = GrossZagierLseries(e, A)
            sage: G(3)
            -0.272946890617590
            sage: G(3, 1)
            0.212442670030741
        """
    def taylor_series(self, s: int = 1, series_prec: int = 6, var: str = 'z'):
        """
        Return the Taylor series at `s`.

        INPUT:

        - ``s`` -- complex number (default: 1)
        - ``series_prec`` -- number of terms (default: 6) in the Taylor series
        - ``var`` -- variable (default: ``'z'``)

        EXAMPLES::

            sage: e = EllipticCurve('37a')
            sage: K.<a> = QuadraticField(-40)
            sage: A = K.class_group().gen(0)
            sage: from sage.modular.modform.l_series_gross_zagier import GrossZagierLseries
            sage: G = GrossZagierLseries(e, A)
            sage: G.taylor_series(2,3)
            -0.613002046122894 + 0.490374999263514*z - 0.122903033710382*z^2 + O(z^3)
        """
