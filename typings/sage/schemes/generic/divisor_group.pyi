from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.generic.divisor import Divisor_curve as Divisor_curve, Divisor_generic as Divisor_generic
from sage.structure.formal_sum import FormalSums as FormalSums
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def DivisorGroup(scheme, base_ring=None):
    """
    Return the group of divisors on the scheme.

    INPUT:

    - ``scheme`` -- a scheme

    - ``base_ring`` -- usually either `\\ZZ` (default) or `\\QQ`. The
      coefficient ring of the divisors. Not to be confused with the
      base ring of the scheme!

    OUTPUT: an instance of ``DivisorGroup_generic``

    EXAMPLES::

        sage: from sage.schemes.generic.divisor_group import DivisorGroup
        sage: DivisorGroup(Spec(ZZ))
        Group of ZZ-Divisors on Spectrum of Integer Ring
        sage: DivisorGroup(Spec(ZZ), base_ring=QQ)
        Group of QQ-Divisors on Spectrum of Integer Ring
    """
def is_DivisorGroup(x):
    """
    Return whether ``x`` is a :class:`DivisorGroup_generic`.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.schemes.generic.divisor_group import is_DivisorGroup, DivisorGroup
        sage: Div = DivisorGroup(Spec(ZZ), base_ring=QQ)
        sage: is_DivisorGroup(Div)
        doctest:warning...
        DeprecationWarning: The function is_DivisorGroup is deprecated; use 'isinstance(..., DivisorGroup_generic)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: is_DivisorGroup('not a divisor')
        False
    """

class DivisorGroup_generic(FormalSums):
    """
    The divisor group on a variety.
    """
    @staticmethod
    def __classcall__(cls, scheme, base_ring=...):
        """
        Set the default value for the base ring.

        EXAMPLES::

            sage: from sage.schemes.generic.divisor_group import DivisorGroup_generic
            sage: DivisorGroup_generic(Spec(ZZ),ZZ) == DivisorGroup_generic(Spec(ZZ))    # indirect test
            True
        """
    def __init__(self, scheme, base_ring) -> None:
        """
        Construct a :class:`DivisorGroup_generic`.

        INPUT:

        - ``scheme`` -- a scheme

        - ``base_ring`` -- the coefficient ring of the divisor group

        Implementation note: :meth:`__classcall__` sets default value
        for ``base_ring``.

        EXAMPLES::

            sage: from sage.schemes.generic.divisor_group import DivisorGroup_generic
            sage: DivisorGroup_generic(Spec(ZZ), QQ)
            Group of QQ-Divisors on Spectrum of Integer Ring

        TESTS::

            sage: from sage.schemes.generic.divisor_group import DivisorGroup
            sage: D1 = DivisorGroup(Spec(ZZ))
            sage: D2 = DivisorGroup(Spec(ZZ), base_ring=QQ)
            sage: D3 = DivisorGroup(Spec(QQ))
            sage: D1 == D1
            True
            sage: D1 == D2
            False
            sage: D1 != D3
            True
            sage: D2 == D2
            True
            sage: D2 == D3
            False
            sage: D3 != D3
            False
            sage: D1 == 'something'
            False
        """
    def scheme(self):
        """
        Return the scheme supporting the divisors.

        EXAMPLES::

            sage: from sage.schemes.generic.divisor_group import DivisorGroup
            sage: Div = DivisorGroup(Spec(ZZ))   # indirect test
            sage: Div.scheme()
            Spectrum of Integer Ring
        """
    def base_extend(self, R):
        """
        EXAMPLES::

            sage: from sage.schemes.generic.divisor_group import DivisorGroup
            sage: DivisorGroup(Spec(ZZ), ZZ).base_extend(QQ)
            Group of QQ-Divisors on Spectrum of Integer Ring
            sage: DivisorGroup(Spec(ZZ), ZZ).base_extend(GF(7))
            Group of (Finite Field of size 7)-Divisors on Spectrum of Integer Ring

        Divisor groups are unique::

            sage: A.<x, y> = AffineSpace(2, CC)                                         # needs sage.rings.real_mpfr
            sage: C = Curve(y^2 - x^9 - x)                                              # needs sage.rings.real_mpfr sage.schemes
            sage: DivisorGroup(C, ZZ).base_extend(QQ) is DivisorGroup(C, QQ)            # needs sage.rings.real_mpfr sage.schemes
            True
        """

class DivisorGroup_curve(DivisorGroup_generic):
    """
    Special case of the group of divisors on a curve.
    """
