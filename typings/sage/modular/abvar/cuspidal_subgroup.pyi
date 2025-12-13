from .finite_subgroup import FiniteSubgroup as FiniteSubgroup
from sage.matrix.constructor import matrix as matrix
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.cusps import Cusp as Cusp
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class CuspidalSubgroup_generic(FiniteSubgroup): ...

class CuspidalSubgroup(CuspidalSubgroup_generic):
    """
    EXAMPLES::

        sage: a = J0(65)[2]
        sage: t = a.cuspidal_subgroup()
        sage: t.order()
        6
    """
    def lattice(self):
        """
        Returned cached tuple of vectors that define elements of the
        rational homology that generate this finite subgroup.

        OUTPUT: tuple (cached)

        EXAMPLES::

            sage: J = J0(27)
            sage: G = J.cuspidal_subgroup()
            sage: G.lattice()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1/3   0]
            [  0 1/3]

        Test that the result is cached::

            sage: G.lattice() is G.lattice()
            True
        """

class RationalCuspSubgroup(CuspidalSubgroup_generic):
    """
    EXAMPLES::

        sage: a = J0(65)[2]
        sage: t = a.rational_cusp_subgroup()
        sage: t.order()
        6
    """
    def lattice(self):
        """
        Return lattice that defines this group.

        OUTPUT: lattice

        EXAMPLES::

            sage: G = J0(27).rational_cusp_subgroup()
            sage: G.lattice()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1/3   0]
            [  0   1]

        Test that the result is cached.

        ::

            sage: G.lattice() is G.lattice()
            True
        """

class RationalCuspidalSubgroup(CuspidalSubgroup_generic):
    """
    EXAMPLES::

        sage: a = J0(65)[2]
        sage: t = a.rational_cuspidal_subgroup()
        sage: t.order()
        6
    """
    def lattice(self):
        """
        Return lattice that defines this group.

        OUTPUT: lattice

        EXAMPLES::

            sage: G = J0(27).rational_cuspidal_subgroup()
            sage: G.lattice()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1/3   0]
            [  0   1]

        Test that the result is cached.

        ::

            sage: G.lattice() is G.lattice()
            True
        """

def is_rational_cusp_gamma0(c, N, data) -> bool:
    """
    Return ``True`` if the rational number c is a rational cusp of level N.

    This uses remarks in Glenn Steven's Ph.D. thesis.

    INPUT:

    - ``c`` -- a cusp

    - ``N`` -- positive integer

    - ``data`` -- the list [n for n in range(2,N) if gcd(n,N) == 1], which is
      passed in as a parameter purely for efficiency reasons.

    EXAMPLES::

        sage: from sage.modular.abvar.cuspidal_subgroup import is_rational_cusp_gamma0
        sage: N = 27
        sage: data = [n for n in range(2,N) if gcd(n,N) == 1]
        sage: is_rational_cusp_gamma0(Cusp(1/3), N, data)
        False
        sage: is_rational_cusp_gamma0(Cusp(1), N, data)
        True
        sage: is_rational_cusp_gamma0(Cusp(oo), N, data)
        True
        sage: is_rational_cusp_gamma0(Cusp(2/9), N, data)
        False
    """
