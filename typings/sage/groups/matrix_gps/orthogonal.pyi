from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic as NamedMatrixGroup_generic, normalize_args_invariant_form as normalize_args_invariant_form, normalize_args_vectorspace as normalize_args_vectorspace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer_ring import ZZ as ZZ

def normalize_args_e(degree, ring, e):
    """
    Normalize the arguments that relate the choice of quadratic form
    for special orthogonal groups over finite fields.

    INPUT:

    - ``degree`` -- integer; the degree of the affine group, that is,
      the dimension of the affine space the group is acting on

    - ``ring`` -- a ring; the base ring of the affine space

    - ``e`` -- integer; one of `+1`, `0`, `-1`.  Only relevant for
      finite fields and if the degree is even. A parameter that
      distinguishes inequivalent invariant forms.

    OUTPUT: the integer ``e`` with values required by GAP

    TESTS::

        sage: from sage.groups.matrix_gps.orthogonal import normalize_args_e
        sage: normalize_args_e(2, GF(3), +1)
        1
        sage: normalize_args_e(3, GF(3), 0)
        0
        sage: normalize_args_e(3, GF(3), +1)
        0
        sage: normalize_args_e(2, GF(3), 0)
        Traceback (most recent call last):
        ...
        ValueError: must have e=-1 or e=1 for even degree
    """
def GO(n, R, e: int = 0, var: str = 'a', invariant_form=None):
    """
    Return the general orthogonal group.

    The general orthogonal group `GO(n,R)` consists of all `n \\times n`
    matrices over the ring `R` preserving an `n`-ary positive definite
    quadratic form. In cases where there are multiple non-isomorphic
    quadratic forms, additional data needs to be specified to
    disambiguate.

    In the case of a finite field and if the degree `n` is even, then
    there are two inequivalent quadratic forms and a third parameter
    ``e`` must be specified to disambiguate these two possibilities.

    .. NOTE::

        This group is also available via ``groups.matrix.GO()``.

    INPUT:

    - ``n`` -- integer; the degree

    - ``R`` -- ring or an integer; if an integer is specified, the
      corresponding finite field is used

    - ``e`` -- ``+1`` or ``-1``, and ignored by default; only relevant
      for finite fields and if the degree is even: a parameter that
      distinguishes inequivalent invariant forms

    - ``var`` -- (default: ``'a'``) variable used to
      represent generator of the finite field, if needed

    - ``invariant_form`` -- (optional) instances being accepted by
      the matrix-constructor which define a `n \\times n` square matrix
      over ``R`` describing the symmetric form to be kept invariant
      by the orthogonal group; the form is checked to be
      non-degenerate and symmetric but not to be positive definite

    OUTPUT: the general orthogonal group of given degree, base ring, and
    choice of invariant form

    EXAMPLES::

        sage: GO(3, GF(7))
        General Orthogonal Group of degree 3 over Finite Field of size 7

        sage: # needs sage.libs.gap
        sage: GO(3, GF(7)).order()
        672
        sage: GO(3, GF(7)).gens()
        (
        [3 0 0]  [0 1 0]
        [0 5 0]  [1 6 6]
        [0 0 1], [0 2 1]
        )

    Using the ``invariant_form`` option::

        sage: m = matrix(QQ, 3, 3, [[0, 1, 0], [1, 0, 0], [0, 0, 3]])
        sage: GO3  = GO(3, QQ)
        sage: GO3m = GO(3, QQ, invariant_form=m)
        sage: GO3 == GO3m
        False
        sage: GO3.invariant_form()
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: GO3m.invariant_form()
        [0 1 0]
        [1 0 0]
        [0 0 3]
        sage: pm = Permutation([2,3,1]).to_matrix()
        sage: g = GO3(pm); g in GO3; g
        True
        [0 0 1]
        [1 0 0]
        [0 1 0]
        sage: GO3m(pm)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be orthogonal with respect to the symmetric form
        [0 1 0]
        [1 0 0]
        [0 0 3]

        sage: GO(3,3, invariant_form=[[1,0,0], [0,2,0], [0,0,1]])
        Traceback (most recent call last):
        ...
        NotImplementedError: invariant_form for finite groups is fixed by GAP
        sage: 5 + 5
        10
        sage: R.<x> = ZZ[]
        sage: GO(2, R, invariant_form=[[x,0], [0,1]])
        General Orthogonal Group of degree 2 over
         Univariate Polynomial Ring in x over Integer Ring with respect to symmetric form
        [x 0]
        [0 1]

    TESTS::

        sage: # needs sage.libs.gap
        sage: TestSuite(GO3).run()
        sage: groups.matrix.GO(2, 3, e=-1)
        General Orthogonal Group of degree 2 and form parameter -1 over Finite Field of size 3
    """
def SO(n, R, e=None, var: str = 'a', invariant_form=None):
    """
    Return the special orthogonal group.

    The special orthogonal group `GO(n,R)` consists of all `n \\times n`
    matrices with determinant one over the ring `R` preserving an
    `n`-ary positive definite quadratic form. In cases where there are
    multiple non-isomorphic quadratic forms, additional data needs to
    be specified to disambiguate.

    .. NOTE::

        This group is also available via ``groups.matrix.SO()``.

    INPUT:

    - ``n`` -- integer; the degree

    - ``R`` -- ring or an integer; if an integer is specified, the
      corresponding finite field is used

    - ``e`` -- ``+1`` or ``-1``, and ignored by default; only relevant
      for finite fields and if the degree is even: a parameter that
      distinguishes inequivalent invariant forms

    - ``var`` -- (default: ``'a'``) variable used to
      represent generator of the finite field, if needed

    - ``invariant_form`` -- (optional) instances being accepted by
      the matrix-constructor which define a `n \\times n` square matrix
      over ``R`` describing the symmetric form to be kept invariant
      by the orthogonal group; the form is checked to be
      non-degenerate and symmetric but not to be positive definite

    OUTPUT: the special orthogonal group of given degree, base ring, and choice
    of invariant form

    EXAMPLES::

        sage: G = SO(3,GF(5)); G
        Special Orthogonal Group of degree 3 over Finite Field of size 5

        sage: # needs sage.libs.gap
        sage: G = SO(3,GF(5))
        sage: G.gens()
        (
        [2 0 0]  [3 2 3]  [1 4 4]
        [0 3 0]  [0 2 0]  [4 0 0]
        [0 0 1], [0 3 1], [2 0 4]
        )
        sage: G.as_matrix_group()
        Matrix group over Finite Field of size 5 with 3 generators (
        [2 0 0]  [3 2 3]  [1 4 4]
        [0 3 0]  [0 2 0]  [4 0 0]
        [0 0 1], [0 3 1], [2 0 4]
        )

    Using the ``invariant_form`` option::

        sage: # needs sage.rings.number_field
        sage: CF3 = CyclotomicField(3); e3 = CF3.gen()
        sage: m = matrix(CF3, 3, 3, [[1,e3,0], [e3,2,0], [0,0,1]])
        sage: SO3  = SO(3, CF3)
        sage: SO3m = SO(3, CF3, invariant_form=m)
        sage: SO3 == SO3m
        False
        sage: SO3.invariant_form()
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: SO3m.invariant_form()
        [    1 zeta3     0]
        [zeta3     2     0]
        [    0     0     1]
        sage: pm = Permutation([2,3,1]).to_matrix()
        sage: g = SO3(pm); g in SO3; g
        True
        [0 0 1]
        [1 0 0]
        [0 1 0]
        sage: SO3m(pm)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be orthogonal with respect to the symmetric form
        [    1 zeta3     0]
        [zeta3     2     0]
        [    0     0     1]

        sage: SO(3, 5, invariant_form=[[1,0,0], [0,2,0], [0,0,3]])
        Traceback (most recent call last):
        ...
        NotImplementedError: invariant_form for finite groups is fixed by GAP
        sage: 5+5
        10

    TESTS::

        sage: TestSuite(SO3m).run()                                                     # needs sage.rings.number_field
        sage: groups.matrix.SO(2, 3, e=1)
        Special Orthogonal Group of degree 2 and form parameter 1 over Finite Field of size 3
    """

class OrthogonalMatrixGroup_generic(NamedMatrixGroup_generic):
    """
    General Orthogonal Group over arbitrary rings.

    EXAMPLES::

        sage: G = GO(3, GF(7)); G
        General Orthogonal Group of degree 3 over Finite Field of size 7
        sage: latex(G)
        \\text{GO}_{3}(\\Bold{F}_{7})

        sage: G = SO(3, GF(5));  G
        Special Orthogonal Group of degree 3 over Finite Field of size 5
        sage: latex(G)
        \\text{SO}_{3}(\\Bold{F}_{5})

        sage: # needs sage.rings.number_field
        sage: CF3 = CyclotomicField(3); e3 = CF3.gen()
        sage: m = matrix(CF3, 3,3, [[1,e3,0],[e3,2,0],[0,0,1]])
        sage: G = SO(3, CF3, invariant_form=m)
        sage: latex(G)
        \\text{SO}_{3}(\\Bold{Q}(\\zeta_{3}))\\text{ with respect to non positive definite symmetric form }\\left(\\begin{array}{rrr}
        1 & \\zeta_{3} & 0 \\\\\n        \\zeta_{3} & 2 & 0 \\\\\n        0 & 0 & 1
        \\end{array}\\right)
    """
    @cached_method
    def invariant_bilinear_form(self):
        """
        Return the symmetric bilinear form preserved by ``self``.

        OUTPUT: a matrix

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: GO(2,3,+1).invariant_bilinear_form()
            [0 1]
            [1 0]
            sage: GO(2,3,-1).invariant_bilinear_form()
            [2 1]
            [1 1]
            sage: G = GO(4, QQ)
            sage: G.invariant_bilinear_form()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
            sage: GO3m = GO(3, QQ, invariant_form=(1,0,0, 0,2,0, 0,0,3))
            sage: GO3m.invariant_bilinear_form()
            [1 0 0]
            [0 2 0]
            [0 0 3]

        TESTS::

            sage: GO3m.invariant_form()                                                 # needs sage.libs.gap
            [1 0 0]
            [0 2 0]
            [0 0 3]
        """
    invariant_quadratic_form = invariant_bilinear_form
    invariant_form = invariant_bilinear_form
