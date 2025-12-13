from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic as NamedMatrixGroup_generic, normalize_args_invariant_form as normalize_args_invariant_form, normalize_args_vectorspace as normalize_args_vectorspace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.finite_rings.finite_field_constructor import GF as GF

def finite_field_sqrt(ring):
    """
    Helper function.

    OUTPUT: integer `q` such that ``ring`` is the finite field with `q^2` elements

    EXAMPLES::

        sage: from sage.groups.matrix_gps.unitary import finite_field_sqrt
        sage: finite_field_sqrt(GF(4, 'a'))                                             # needs sage.rings.finite_rings
        2
    """
def GU(n, R, var: str = 'a', invariant_form=None):
    """
    Return the general unitary group.

    The general unitary group `GU( d, R )` consists of all `d \\times d`
    matrices that preserve a nondegenerate sesquilinear form over the
    ring `R`.

    .. NOTE::

        For a finite field, the matrices that preserve a sesquilinear
        form over `\\GF{q}` live over `\\GF{q^2}`. So ``GU(n,q)`` for
        a prime power `q` constructs the matrix group over the base
        ring ``GF(q^2)``.

    .. NOTE::

        This group is also available via ``groups.matrix.GU()``.

    INPUT:

    - ``n`` -- positive integer

    - ``R`` -- ring or an integer; if an integer is specified, the
      corresponding finite field is used

    - ``var`` -- (default: ``'a'``) variable used to
      represent generator of the finite field, if needed

    - ``invariant_form`` -- (optional) instances being accepted by
      the matrix-constructor which define a `n \\times n` square matrix
      over `R` describing the hermitian form to be kept invariant
      by the unitary group; the form is checked to be
      non-degenerate and hermitian but not to be positive definite

    OUTPUT: the general unitary group

    EXAMPLES::

        sage: G = GU(3, 7); G                                                           # needs sage.rings.finite_rings
        General Unitary Group of degree 3 over Finite Field in a of size 7^2
        sage: G.gens()                                                                  # needs sage.libs.gap sage.rings.finite_rings
        (
        [  a   0   0]  [6*a   6   1]
        [  0   1   0]  [  6   6   0]
        [  0   0 5*a], [  1   0   0]
        )
        sage: GU(2, QQ)
        General Unitary Group of degree 2 over Rational Field

        sage: G = GU(3, 5, var='beta')                                                  # needs sage.rings.finite_rings
        sage: G.base_ring()                                                             # needs sage.rings.finite_rings
        Finite Field in beta of size 5^2
        sage: G.gens()                                                                  # needs sage.libs.gap sage.rings.finite_rings
        (
        [  beta      0      0]  [4*beta      4      1]
        [     0      1      0]  [     4      4      0]
        [     0      0 3*beta], [     1      0      0]
        )

    Using the ``invariant_form`` option::

        sage: # needs sage.libs.gap sage.rings.number_field
        sage: UCF = UniversalCyclotomicField(); e5 = UCF.gen(5)
        sage: m = matrix(UCF, 3, 3, [[1,e5,0], [e5.conjugate(),2,0], [0,0,1]])
        sage: G  = GU(3, UCF)
        sage: Gm = GU(3, UCF, invariant_form=m)
        sage: G == Gm
        False
        sage: G.invariant_form()
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: Gm.invariant_form()
        [     1   E(5)      0]
        [E(5)^4      2      0]
        [     0      0      1]
        sage: pm = Permutation((1,2,3)).to_matrix()
        sage: g = G(pm); g in G; g                                                      # needs sage.combinat
        True
        [0 0 1]
        [1 0 0]
        [0 1 0]
        sage: Gm(pm)                                                                    # needs sage.combinat
        Traceback (most recent call last):
        ...
        TypeError: matrix must be unitary with respect to the hermitian form
        [     1   E(5)      0]
        [E(5)^4      2      0]
        [     0      0      1]

        sage: GU(3, 3, invariant_form=[[1,0,0], [0,2,0], [0,0,1]])                      # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        NotImplementedError: invariant_form for finite groups is fixed by GAP

        sage: GU(2, QQ, invariant_form=[[1,0], [2,0]])
        Traceback (most recent call last):
        ...
        ValueError: invariant_form must be non-degenerate

    TESTS::

        sage: TestSuite(G).run()                                                        # needs sage.libs.gap sage.rings.number_field
        sage: groups.matrix.GU(2, 3)                                                    # needs sage.groups sage.rings.finite_rings
        General Unitary Group of degree 2 over Finite Field in a of size 3^2
    """
def SU(n, R, var: str = 'a', invariant_form=None):
    """
    The special unitary group `SU( d, R )` consists of all `d \\times d`
    matrices that preserve a nondegenerate sesquilinear form over the
    ring `R` and have determinant `1`.

    .. NOTE::

        For a finite field the matrices that preserve a sesquilinear
        form over `\\GF{q}` live over `\\GF{q^2}`. So ``SU(n,q)`` for
        a prime power `q` constructs the matrix group over the base
        ring ``GF(q^2)``.

    .. NOTE::

        This group is also available via ``groups.matrix.SU()``.

    INPUT:

    - ``n`` -- positive integer

    - ``R`` -- ring or an integer; if an integer is specified, the
      corresponding finite field is used

    - ``var`` -- (default: ``'a'``) variable used to
      represent generator of the finite field, if needed

    - ``invariant_form`` -- (optional) instances being accepted by
      the matrix-constructor which define a `n \\times n` square matrix
      over R describing the hermitian form to be kept invariant
      by the unitary group; the form is checked to be
      non-degenerate and hermitian but not to be positive definite

    OUTPUT: the special unitary group

    EXAMPLES::

        sage: SU(3,5)                                                                   # needs sage.rings.finite_rings
        Special Unitary Group of degree 3 over Finite Field in a of size 5^2
        sage: SU(3, GF(5))                                                              # needs sage.rings.finite_rings
        Special Unitary Group of degree 3 over Finite Field in a of size 5^2
        sage: SU(3, QQ)
        Special Unitary Group of degree 3 over Rational Field

    Using the ``invariant_form`` option::

        sage: # needs sage.rings.number_field
        sage: CF3 = CyclotomicField(3); e3 = CF3.gen()
        sage: m = matrix(CF3, 3, 3, [[1,e3,0], [e3.conjugate(),2,0], [0,0,1]])
        sage: G  = SU(3, CF3)
        sage: Gm = SU(3, CF3, invariant_form=m)
        sage: G == Gm
        False
        sage: G.invariant_form()
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: Gm.invariant_form()
        [         1      zeta3          0]
        [-zeta3 - 1          2          0]
        [         0          0          1]
        sage: pm = Permutation((1,2,3)).to_matrix()
        sage: G(pm)                                                                     # needs sage.combinat
        [0 0 1]
        [1 0 0]
        [0 1 0]
        sage: Gm(pm)                                                                    # needs sage.combinat
        Traceback (most recent call last):
        ...
        TypeError: matrix must be unitary with respect to the hermitian form
        [         1      zeta3          0]
        [-zeta3 - 1          2          0]
        [         0          0          1]

        sage: SU(3, 5, invariant_form=[[1,0,0], [0,2,0], [0,0,3]])                      # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        NotImplementedError: invariant_form for finite groups is fixed by GAP

    TESTS::

        sage: TestSuite(Gm).run()                                                       # needs sage.rings.number_field
        sage: groups.matrix.SU(2, 3)                                                    # needs sage.modules sage.rings.finite_rings
        Special Unitary Group of degree 2 over Finite Field in a of size 3^2
    """

class UnitaryMatrixGroup_generic(NamedMatrixGroup_generic):
    """
    General Unitary Group over arbitrary rings.

    EXAMPLES::

        sage: G = GU(3, GF(7)); G                                                       # needs sage.rings.finite_rings
        General Unitary Group of degree 3 over Finite Field in a of size 7^2
        sage: latex(G)                                                                  # needs sage.rings.finite_rings
        \\text{GU}_{3}(\\Bold{F}_{7^{2}})

        sage: G = SU(3, GF(5));  G                                                      # needs sage.rings.finite_rings
        Special Unitary Group of degree 3 over Finite Field in a of size 5^2
        sage: latex(G)                                                                  # needs sage.rings.finite_rings
        \\text{SU}_{3}(\\Bold{F}_{5^{2}})

        sage: # needs sage.rings.number_field
        sage: CF3 = CyclotomicField(3); e3 = CF3.gen()
        sage: m = matrix(CF3, 3, 3, [[1,e3,0], [e3.conjugate(),2,0], [0,0,1]])
        sage: G = SU(3, CF3, invariant_form=m)
        sage: latex(G)
        \\text{SU}_{3}(\\Bold{Q}(\\zeta_{3}))\\text{ with respect to positive definite hermitian form }\\left(\\begin{array}{rrr}
        1 & \\zeta_{3} & 0 \\\\\n        -\\zeta_{3} - 1 & 2 & 0 \\\\\n        0 & 0 & 1
        \\end{array}\\right)
    """
    @cached_method
    def invariant_form(self):
        """
        Return the hermitian form preserved by the unitary
        group.

        OUTPUT: a square matrix describing the bilinear form

        EXAMPLES::

            sage: SU4 = SU(4, QQ)
            sage: SU4.invariant_form()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
        """
