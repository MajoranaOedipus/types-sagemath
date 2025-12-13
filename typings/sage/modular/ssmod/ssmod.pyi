from _typeshed import Incomplete
from sage.arith.misc import kronecker as kronecker, next_prime as next_prime
from sage.categories.fields import Fields as Fields
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modular.hecke.module import HeckeModule_free_module as HeckeModule_free_module
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

ZZy: Incomplete

def Phi2_quad(J3, ssJ1, ssJ2):
    """
    Return a certain quadratic polynomial over a finite
    field in indeterminate J3.

    The roots of the polynomial along with ssJ1 are the
    neighboring/2-isogenous supersingular j-invariants of ssJ2.

    INPUT:

    - ``J3`` -- indeterminate of a univariate polynomial ring defined over a finite
      field with p^2 elements where p is a prime number

    - ``ssJ2``, ``ssJ2`` -- supersingular j-invariants over the finite field

    OUTPUT: polynomial; defined over the finite field

    EXAMPLES:

    The following code snippet produces a factor of the modular polynomial
    `\\Phi_{2}(x,j_{in})`, where `j_{in}` is a supersingular j-invariant
    defined over the finite field with `37^2` elements::

        sage: F = GF(37^2, 'a')
        sage: X = PolynomialRing(F, 'x').gen()
        sage: j_in = supersingular_j(F)
        sage: poly = sage.modular.ssmod.ssmod.Phi_polys(2,X,j_in)
        sage: poly.roots()
        [(8, 1), (27*a + 23, 1), (10*a + 20, 1)]
        sage: sage.modular.ssmod.ssmod.Phi2_quad(X, F(8), j_in)
        x^2 + 31*x + 31

    .. NOTE::

        Given a root (j1,j2) to the polynomial `Phi_2(J1,J2)`, the pairs
        (j2,j3) not equal to (j2,j1) which solve `Phi_2(j2,j3)` are roots of
        the quadratic equation:

        J3^2 + (-j2^2 + 1488*j2 + (j1 - 162000))*J3 + (-j1 + 1488)*j2^2 +
        (1488*j1 + 40773375)*j2 + j1^2 - 162000*j1 + 8748000000

        This will be of use to extend the 2-isogeny graph, once the initial
        three roots are determined for `Phi_2(J1,J2)`.

    AUTHORS:

    - David Kohel -- kohel@maths.usyd.edu.au

    - Iftikhar Burhanuddin -- burhanud@usc.edu
    """
def Phi_polys(L, x, j):
    """
    Return a certain polynomial of degree `L+1` in the
    indeterminate x over a finite field.

    The roots of the **modular** polynomial `\\Phi(L, x, j)` are the
    `L`-isogenous supersingular j-invariants of j.

    INPUT:

    - ``L`` -- integer

    - ``x`` -- indeterminate of a univariate polynomial ring defined over a
      finite field with p^2 elements, where p is a prime number

    - ``j`` -- supersingular j-invariant over the finite field

    OUTPUT: polynomial; defined over the finite field

    EXAMPLES:

    The following code snippet produces the modular polynomial
    `\\Phi_{L}(x,j_{in})`, where `j_{in}` is a supersingular j-invariant
    defined over the finite field with `7^2` elements::

        sage: F = GF(7^2, 'a')
        sage: X = PolynomialRing(F, 'x').gen()
        sage: j_in = supersingular_j(F)
        sage: sage.modular.ssmod.ssmod.Phi_polys(2,X,j_in)
        x^3 + 3*x^2 + 3*x + 1
        sage: sage.modular.ssmod.ssmod.Phi_polys(3,X,j_in)
        x^4 + 4*x^3 + 6*x^2 + 4*x + 1
        sage: sage.modular.ssmod.ssmod.Phi_polys(5,X,j_in)
        x^6 + 6*x^5 + x^4 + 6*x^3 + x^2 + 6*x + 1
        sage: sage.modular.ssmod.ssmod.Phi_polys(7,X,j_in)
        x^8 + x^7 + x + 1
        sage: sage.modular.ssmod.ssmod.Phi_polys(11,X,j_in)
        x^12 + 5*x^11 + 3*x^10 + 3*x^9 + 5*x^8 + x^7 + x^5 + 5*x^4 + 3*x^3 + 3*x^2 + 5*x + 1
        sage: sage.modular.ssmod.ssmod.Phi_polys(13,X,j_in)
        x^14 + 2*x^7 + 1
    """
def dimension_supersingular_module(prime, level: int = 1):
    """
    Return the dimension of the Supersingular module, which is
    equal to the dimension of the space of modular forms of weight `2`
    and conductor equal to ``prime`` times ``level``.

    INPUT:

    - ``prime`` -- integer; prime

    - ``level`` -- integer; positive

    OUTPUT: dimension; integer, nonnegative

    EXAMPLES:

    The code below computes the dimensions of Supersingular modules
    with level=1 and prime = 7, 15073 and 83401::

        sage: dimension_supersingular_module(7)
        1

        sage: dimension_supersingular_module(15073)
        1256

        sage: dimension_supersingular_module(83401)
        6950

    .. NOTE::

        The case of level > 1 has not been implemented yet.

    AUTHORS:

    - David Kohel -- kohel@maths.usyd.edu.au

    - Iftikhar Burhanuddin - burhanud@usc.edu
    """
def supersingular_D(prime):
    """
    Return a fundamental discriminant `D` of an
    imaginary quadratic field, where the given prime does not split.

    See Silverman's Advanced Topics in the Arithmetic of Elliptic
    Curves, page 184, exercise 2.30(d).

    INPUT:

    - ``prime`` -- integer, prime

    OUTPUT: d; integer, negative

    EXAMPLES:

    These examples return *supersingular discriminants* for 7,
    15073 and 83401::

        sage: supersingular_D(7)
        -4

        sage: supersingular_D(15073)
        -15

        sage: supersingular_D(83401)
        -7

    AUTHORS:

    - David Kohel - kohel@maths.usyd.edu.au

    - Iftikhar Burhanuddin - burhanud@usc.edu
    """
def supersingular_j(FF):
    """
    Return a supersingular j-invariant over the finite
    field FF.

    INPUT:

    - ``FF`` -- finite field with p^2 elements, where p is a prime number

    OUTPUT:

    - finite field element -- a supersingular j-invariant
      defined over the finite field FF

    EXAMPLES:

    The following examples calculate supersingular j-invariants for a
    few finite fields::

        sage: supersingular_j(GF(7^2, 'a'))
        6

    Observe that in this example the j-invariant is not defined over
    the prime field::

        sage: supersingular_j(GF(15073^2, 'a'))
        4443*a + 13964
        sage: supersingular_j(GF(83401^2, 'a'))
        67977

    AUTHORS:

    - David Kohel -- kohel@maths.usyd.edu.au

    - Iftikhar Burhanuddin -- burhanud@usc.edu
    """

class SupersingularModule(HeckeModule_free_module):
    """
    The module of supersingular points in a given characteristic, with
    given level structure.

    The characteristic must not divide the level.

    .. NOTE:: Currently, only level 1 is implemented.

    EXAMPLES::

        sage: S = SupersingularModule(17)
        sage: S
        Module of supersingular points on X_0(1)/F_17 over Integer Ring
        sage: S = SupersingularModule(16)
        Traceback (most recent call last):
        ...
        ValueError: the argument prime must be a prime number
        sage: S = SupersingularModule(prime=17, level=34)
        Traceback (most recent call last):
        ...
        ValueError: the argument level must be coprime to the argument prime
        sage: S = SupersingularModule(prime=17, level=5)
        Traceback (most recent call last):
        ...
        NotImplementedError: supersingular modules of level > 1 not yet implemented
    """
    def __init__(self, prime: int = 2, level: int = 1, base_ring=...) -> None:
        """
        Create a supersingular module.

        EXAMPLES::

            sage: SupersingularModule(3)
            Module of supersingular points on X_0(1)/F_3 over Integer Ring
        """
    def __richcmp__(self, other, op) -> bool:
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: SupersingularModule(37) == ModularForms(37, 2)
            False
            sage: SupersingularModule(37) == SupersingularModule(37, base_ring=Qp(7))
            False
            sage: SupersingularModule(37) == SupersingularModule(37)
            True
        """
    def free_module(self):
        """
        EXAMPLES::

            sage: X = SupersingularModule(37)
            sage: X.free_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring

        This illustrates the fix at :issue:`4306`::

            sage: X = SupersingularModule(389)
            sage: X.basis()
            ((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1))
        """
    @cached_method
    def dimension(self):
        """
        Return the dimension of the space of modular forms of weight 2
        and level equal to the level associated to ``self``.

        INPUT:

        - ``self`` -- SupersingularModule object

        OUTPUT: integer; dimension, nonnegative

        EXAMPLES::

            sage: S = SupersingularModule(7)
            sage: S.dimension()
            1

            sage: S = SupersingularModule(15073)
            sage: S.dimension()
            1256

            sage: S = SupersingularModule(83401)
            sage: S.dimension()
            6950

        .. NOTE::

           The case of level > 1 has not yet been implemented.

        AUTHORS:

        - David Kohel -- kohel@maths.usyd.edu.au

        - Iftikhar Burhanuddin -- burhanud@usc.edu
        """
    rank = dimension
    def level(self):
        """
        This function returns the level associated to ``self``.

        INPUT:

        - ``self`` -- SupersingularModule object

        OUTPUT: integer; the level, positive

        EXAMPLES::

            sage: S = SupersingularModule(15073)
            sage: S.level()
            1

        AUTHORS:

        - David Kohel -- kohel@maths.usyd.edu.au

        - Iftikhar Burhanuddin -- burhanud@usc.edu
        """
    def prime(self):
        """
        Return the characteristic of the finite field associated to ``self``.

        INPUT:

        - ``self`` -- SupersingularModule object

        OUTPUT: integer; characteristic, positive

        EXAMPLES::

            sage: S = SupersingularModule(19)
            sage: S.prime()
            19

        AUTHORS:

        - David Kohel -- kohel@maths.usyd.edu.au

        - Iftikhar Burhanuddin -- burhanud@usc.edu
        """
    def weight(self):
        """
        Return the weight associated to ``self``.

        INPUT:

        - ``self`` -- SupersingularModule object

        OUTPUT: integer; weight, positive

        EXAMPLES::

            sage: S = SupersingularModule(19)
            sage: S.weight()
            2

        AUTHORS:

        - David Kohel -- kohel@maths.usyd.edu.au

        - Iftikhar Burhanuddin -- burhanud@usc.edu
        """
    @cached_method
    def supersingular_points(self):
        """
        Compute the supersingular j-invariants over the
        finite field associated to ``self``.

        INPUT:

        - ``self`` -- SupersingularModule object

        OUTPUT:

        - list_j, dict_j -- list_j is the list of supersingular
            j-invariants, dict_j is a dictionary with these
            j-invariants as keys and their indexes as values. The
            latter is used to speed up j-invariant look-up. The
            indexes are based on the order of their *discovery*.

        EXAMPLES:

        The following examples calculate supersingular j-invariants
        over finite fields with characteristic 7, 11 and 37::

            sage: S = SupersingularModule(7)
            sage: S.supersingular_points()
            ([6], {6: 0})

            sage: S = SupersingularModule(11)
            sage: S.supersingular_points()[0]
            [1, 0]

            sage: S = SupersingularModule(37)
            sage: S.supersingular_points()[0]
            [8, 27*a + 23, 10*a + 20]

        AUTHORS:

        - David Kohel -- kohel@maths.usyd.edu.au

        - Iftikhar Burhanuddin -- burhanud@usc.edu
        """
    def upper_bound_on_elliptic_factors(self, p=None, ellmax: int = 2):
        """
        Return an upper bound (provably correct) on the number of
        elliptic curves of conductor equal to the level of this
        supersingular module.

        INPUT:

        - ``p`` -- (default: 997) prime to work modulo

        ALGORITHM: Currently we only use `T_2`.  Function will be
        extended to use more Hecke operators later.

        The prime p is replaced by the smallest prime that does not
        divide the level.

        EXAMPLES::

            sage: SupersingularModule(37).upper_bound_on_elliptic_factors()
            2

        (There are 4 elliptic curves of conductor 37, but only 2 isogeny
        classes.)
        """
    def hecke_matrix(self, L):
        """
        Return the `L^{\\text{th}}` Hecke matrix.

        INPUT:

        - ``self`` -- SupersingularModule object

        - ``L`` -- integer; positive

        OUTPUT: matrix; sparse integer matrix

        EXAMPLES:

        This example computes the action of the Hecke operator `T_2`
        on the module of supersingular points on `X_0(1)/F_{37}`::

            sage: S = SupersingularModule(37)
            sage: M = S.hecke_matrix(2)
            sage: M
            [1 1 1]
            [1 0 2]
            [1 2 0]

        This example computes the action of the Hecke operator `T_3`
        on the module of supersingular points on `X_0(1)/F_{67}`::

            sage: S = SupersingularModule(67)
            sage: M = S.hecke_matrix(3)
            sage: M
            [0 0 0 0 2 2]
            [0 0 1 1 1 1]
            [0 1 0 2 0 1]
            [0 1 2 0 1 0]
            [1 1 0 1 0 1]
            [1 1 1 0 1 0]

        .. NOTE::

            The first list --- list_j --- returned by the supersingular_points
            function are the rows *and* column indexes of the above hecke
            matrices and its ordering should be kept in mind when interpreting
            these matrices.

        AUTHORS:

        - David Kohel -- kohel@maths.usyd.edu.au

        - Iftikhar Burhanuddin -- burhanud@usc.edu
        """
