from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic as NamedMatrixGroup_generic, normalize_args_invariant_form as normalize_args_invariant_form, normalize_args_vectorspace as normalize_args_vectorspace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField

def Sp(n, R, var: str = 'a', invariant_form=None):
    """
    Return the symplectic group.

    The special linear group `GL( d, R )` consists of all `d \\times d`
    matrices that are invertible over the ring `R` with determinant one.

    .. NOTE::

        This group is also available via ``groups.matrix.Sp()``.

    INPUT:

    - ``n`` -- positive integer

    - ``R`` -- ring or an integer; if an integer is specified, the
      corresponding finite field is used

    - ``var`` -- (default: ``'a'``) variable used to
      represent generator of the finite field, if needed

    - ``invariant_form`` -- (optional) instances being accepted by
      the matrix-constructor which define a `n \\times n` square matrix
      over ``R`` describing the alternating form to be kept invariant
      by the symplectic group

    EXAMPLES::

        sage: Sp(4, 5)
        Symplectic Group of degree 4 over Finite Field of size 5

        sage: Sp(4, IntegerModRing(15))
        Symplectic Group of degree 4 over Ring of integers modulo 15

        sage: Sp(3, GF(7))
        Traceback (most recent call last):
        ...
        ValueError: the degree must be even

    Using the ``invariant_form`` option::

        sage: m = matrix(QQ, 4,4, [[0, 0, 1, 0], [0, 0, 0, 2], [-1, 0, 0, 0], [0, -2, 0, 0]])
        sage: Sp4m = Sp(4, QQ, invariant_form=m)
        sage: Sp4 = Sp(4, QQ)
        sage: Sp4 == Sp4m
        False
        sage: Sp4.invariant_form()
        [ 0  0  0  1]
        [ 0  0  1  0]
        [ 0 -1  0  0]
        [-1  0  0  0]
        sage: Sp4m.invariant_form()
        [ 0  0  1  0]
        [ 0  0  0  2]
        [-1  0  0  0]
        [ 0 -2  0  0]
        sage: pm = Permutation([2,1,4,3]).to_matrix()
        sage: g = Sp4(pm); g in Sp4; g
        True
        [0 1 0 0]
        [1 0 0 0]
        [0 0 0 1]
        [0 0 1 0]
        sage: Sp4m(pm)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be symplectic with respect to the alternating form
        [ 0  0  1  0]
        [ 0  0  0  2]
        [-1  0  0  0]
        [ 0 -2  0  0]

        sage: Sp(4,3, invariant_form=[[0,0,0,1],[0,0,1,0],[0,2,0,0], [2,0,0,0]])
        Traceback (most recent call last):
        ...
        NotImplementedError: invariant_form for finite groups is fixed by GAP

    TESTS::

        sage: TestSuite(Sp4).run()
        sage: TestSuite(Sp4m).run()
        sage: groups.matrix.Sp(2, 3)                                                    # needs sage.modules sage.rings.finite_rings
        Symplectic Group of degree 2 over Finite Field of size 3

        sage: # needs sage.libs.gap
        sage: G = Sp(4,5)
        sage: TestSuite(G).run()
    """

class SymplecticMatrixGroup_generic(NamedMatrixGroup_generic):
    """
    Symplectic Group over arbitrary rings.

    EXAMPLES::

        sage: Sp43 = Sp(4,3); Sp43
        Symplectic Group of degree 4 over Finite Field of size 3
        sage: latex(Sp43)
        \\text{Sp}_{4}(\\Bold{F}_{3})

        sage: Sp4m = Sp(4, QQ, invariant_form=(0, 0, 1, 0,  0, 0, 0, 2,
        ....:                                  -1, 0, 0, 0, 0, -2, 0, 0)); Sp4m
        Symplectic Group of degree 4 over Rational Field
         with respect to alternating bilinear form
        [ 0  0  1  0]
        [ 0  0  0  2]
        [-1  0  0  0]
        [ 0 -2  0  0]
        sage: latex(Sp4m)
        \\text{Sp}_{4}(\\Bold{Q})\\text{ with respect to alternating bilinear form}\\left(\\begin{array}{rrrr}
        0 & 0 & 1 & 0 \\\\\n        0 & 0 & 0 & 2 \\\\\n        -1 & 0 & 0 & 0 \\\\\n        0 & -2 & 0 & 0
        \\end{array}\\right)
    """
    @cached_method
    def invariant_form(self):
        """
        Return the quadratic form preserved by the symplectic group.

        OUTPUT: a matrix

        EXAMPLES::

            sage: Sp(4, QQ).invariant_form()
            [ 0  0  0  1]
            [ 0  0  1  0]
            [ 0 -1  0  0]
            [-1  0  0  0]
        """
