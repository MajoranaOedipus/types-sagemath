from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.modular.hecke.module import HeckeModule_free_module as HeckeModule_free_module
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal

class Homology(HeckeModule_free_module):
    """
    A homology group of an abelian variety, equipped with a Hecke
    action.
    """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Return the `n`-th Hecke polynomial in the given variable.

        INPUT:

        - ``n`` -- positive integer

        - ``var`` -- string (default: ``'x'``); the variable name

        OUTPUT: a polynomial over `\\ZZ` in the given variable

        EXAMPLES::

            sage: H = J0(43).integral_homology(); H
            Integral Homology of Abelian variety J0(43) of dimension 3
            sage: f = H.hecke_polynomial(3); f
            x^6 + 4*x^5 - 16*x^3 - 12*x^2 + 16*x + 16
            sage: parent(f)
            Univariate Polynomial Ring in x over Integer Ring
            sage: H.hecke_polynomial(3,'w')
            w^6 + 4*w^5 - 16*w^3 - 12*w^2 + 16*w + 16
        """

class Homology_abvar(Homology):
    """
    The homology of a modular abelian variety.
    """
    def __init__(self, abvar, base) -> None:
        """
        This is an abstract base class, so it is called implicitly in the
        following examples.

        EXAMPLES::

            sage: H = J0(43).integral_homology()
            sage: type(H)
            <class 'sage.modular.abvar.homology.IntegralHomology_with_category'>

        TESTS::

            sage: H = J0(43).integral_homology()
            sage: loads(dumps(H)) == H
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: J0(37).integral_homology() == J0(41).integral_homology()
            False
            sage: J0(37).integral_homology() == J0(37).rational_homology()
            False
            sage: J0(37).integral_homology() == loads(dumps(J0(37).integral_homology()))
            True
        """
    def gens(self) -> None:
        """
        Return generators of ``self``.

        This is not yet implemented!

        EXAMPLES::

            sage: H = J0(37).homology()
            sage: H.gens()    # this will change
            Traceback (most recent call last):
            ...
            NotImplementedError: homology classes not yet implemented
        """
    def gen(self, n) -> None:
        """
        Return `n`-th generator of ``self``.

        This is not yet implemented!

        EXAMPLES::

            sage: H = J0(37).homology()
            sage: H.gen(0)    # this will change
            Traceback (most recent call last):
            ...
            NotImplementedError: homology classes not yet implemented
        """
    def abelian_variety(self):
        """
        Return the abelian variety that this is the homology of.

        EXAMPLES::

            sage: H = J0(48).homology()
            sage: H.abelian_variety()
            Abelian variety J0(48) of dimension 3
        """
    def ambient_hecke_module(self):
        """
        Return the ambient Hecke module that this homology is contained
        in.

        EXAMPLES::

            sage: H = J0(48).homology(); H
            Integral Homology of Abelian variety J0(48) of dimension 3
            sage: H.ambient_hecke_module()
            Integral Homology of Abelian variety J0(48) of dimension 3
        """
    def free_module(self):
        """
        Return the underlying free module of this homology group.

        EXAMPLES::

            sage: H = J0(48).homology()
            sage: H.free_module()
            Ambient free module of rank 6 over the principal ideal domain Integer Ring
        """
    def hecke_bound(self):
        """
        Return bound on the number of Hecke operators needed to generate
        the Hecke algebra as a `\\ZZ`-module acting on this
        space.

        EXAMPLES::

            sage: J0(48).homology().hecke_bound()
            16
            sage: J1(15).homology().hecke_bound()
            32
        """
    def hecke_matrix(self, n) -> None:
        """
        Return the matrix of the `n`-th Hecke operator acting on this
        homology group.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT: a matrix over the coefficient ring of this homology group

        EXAMPLES::

            sage: H = J0(23).integral_homology()
            sage: H.hecke_matrix(3)
            [-1 -2  2  0]
            [ 0 -3  2 -2]
            [ 2 -4  3 -2]
            [ 2 -2  0  1]

        The matrix is over the coefficient ring::

            sage: J = J0(23)
            sage: J.homology(QQ[I]).hecke_matrix(3).parent()
            Full MatrixSpace of 4 by 4 dense matrices over
             Number Field in I with defining polynomial x^2 + 1 with I = 1*I
        """
    def rank(self):
        """
        Return the rank as a module or vector space of this homology
        group.

        EXAMPLES::

            sage: H = J0(5077).homology(); H
            Integral Homology of Abelian variety J0(5077) of dimension 422
            sage: H.rank()
            844
        """
    def submodule(self, U, check: bool = True):
        """
        Return the submodule of this homology group given by `U`,
        which should be a submodule of the free module associated to this
        homology group.

        INPUT:

        - ``U`` -- submodule of ambient free module (or
          something that defines one)

        - ``check`` -- currently ignored


        .. NOTE::

           We do *not* check that U is invariant under all Hecke
           operators.

        EXAMPLES::

            sage: H = J0(23).homology(); H
            Integral Homology of Abelian variety J0(23) of dimension 2
            sage: F = H.free_module()
            sage: U = F.span([[1,2,3,4]])
            sage: M = H.submodule(U); M
            Submodule of rank 1 of Integral Homology of Abelian variety J0(23) of dimension 2

        Note that the submodule command doesn't actually check that the
        object defined is a homology group or is invariant under the Hecke
        operators. For example, the fairly random `M` that we just
        defined is not invariant under the Hecke operators, so it is not a
        Hecke submodule - it is only a `\\ZZ`-submodule.

        ::

            sage: M.hecke_matrix(3)
            Traceback (most recent call last):
            ...
            ArithmeticError: subspace is not invariant under matrix
        """

class IntegralHomology(Homology_abvar):
    """
    The integral homology `H_1(A,\\ZZ)` of a modular
    abelian variety.
    """
    def __init__(self, abvar) -> None:
        """
        Create the integral homology of a modular abelian variety.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        EXAMPLES::

            sage: H = J0(23).integral_homology(); H
            Integral Homology of Abelian variety J0(23) of dimension 2
            sage: type(H)
            <class 'sage.modular.abvar.homology.IntegralHomology_with_category'>

        TESTS::

            sage: loads(dumps(H)) == H
            True
        """
    def hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on this
        homology group.

        EXAMPLES::

            sage: J0(48).integral_homology().hecke_bound()
            16
            sage: t = J1(13).integral_homology().hecke_matrix(3); t
            [-2  2  2 -2]
            [-2  0  2  0]
            [ 0  0  0 -2]
            [ 0  0  2 -2]
            sage: t.base_ring()
            Integer Ring
        """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Return the `n`-th Hecke polynomial on this integral homology group.

        EXAMPLES::

            sage: f = J0(43).integral_homology().hecke_polynomial(2)
            sage: f.base_ring()
            Integer Ring
            sage: factor(f)
            (x + 2)^2 * (x^2 - 2)^2
        """

class RationalHomology(Homology_abvar):
    """
    The rational homology `H_1(A,\\QQ)` of a modular
    abelian variety.
    """
    def __init__(self, abvar) -> None:
        """
        Create the rational homology of a modular abelian variety.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        EXAMPLES::

            sage: H = J0(23).rational_homology(); H
            Rational Homology of Abelian variety J0(23) of dimension 2

        TESTS::

            sage: loads(dumps(H)) == H
            True
        """
    def hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on this
        homology group.

        EXAMPLES::

            sage: t = J1(13).homology(QQ).hecke_matrix(3); t
            [-2  2  2 -2]
            [-2  0  2  0]
            [ 0  0  0 -2]
            [ 0  0  2 -2]
            sage: t.base_ring()
            Rational Field
            sage: t = J1(13).homology(GF(3)).hecke_matrix(3); t
            [1 2 2 1]
            [1 0 2 0]
            [0 0 0 1]
            [0 0 2 1]
            sage: t.base_ring()
            Finite Field of size 3
        """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Return the `n`-th Hecke polynomial on this rational homology group.

        EXAMPLES::

            sage: f = J0(43).rational_homology().hecke_polynomial(2)
            sage: f.base_ring()
            Rational Field
            sage: factor(f)
            (x + 2) * (x^2 - 2)
        """

class Homology_over_base(Homology_abvar):
    """
    The homology over a modular abelian variety over an arbitrary base
    commutative ring (not `\\ZZ` or `\\QQ`).
    """
    def __init__(self, abvar, base_ring) -> None:
        """
        Called when creating homology with coefficients not
        `\\ZZ` or `\\QQ`.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        - ``base_ring`` -- a commutative ring

        EXAMPLES::

            sage: H = J0(23).homology(GF(5)); H
            Homology with coefficients in Finite Field of size 5 of Abelian variety J0(23) of dimension 2
            sage: type(H)
            <class 'sage.modular.abvar.homology.Homology_over_base_with_category'>

        TESTS::

            sage: loads(dumps(H)) == H
            True
        """
    def hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on this
        homology group.

        EXAMPLES::

            sage: t = J1(13).homology(GF(3)).hecke_matrix(3); t
            [1 2 2 1]
            [1 0 2 0]
            [0 0 0 1]
            [0 0 2 1]
            sage: t.base_ring()
            Finite Field of size 3
        """

class Homology_submodule(Homology):
    """
    A submodule of the homology of a modular abelian variety.
    """
    def __init__(self, ambient, submodule) -> None:
        """
        Create a submodule of the homology of a modular abelian variety.

        INPUT:

        - ``ambient`` -- the homology of some modular abelian
          variety with ring coefficients

        - ``submodule`` -- a submodule of the free module
          underlying ambient

        EXAMPLES::

            sage: H = J0(37).homology()
            sage: H.submodule([[1,0,0,0]])
            Submodule of rank 1 of Integral Homology of Abelian variety J0(37) of dimension 2

        TESTS::

            sage: loads(dumps(H)) == H
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: J0(37).homology().decomposition() # indirect doctest
            [Submodule of rank 2 of Integral Homology of Abelian variety J0(37) of dimension 2,
             Submodule of rank 2 of Integral Homology of Abelian variety J0(37) of dimension 2]
        """
    def ambient_hecke_module(self):
        """
        Return the ambient Hecke module that this homology is contained
        in.

        EXAMPLES::

            sage: H = J0(48).homology(); H
            Integral Homology of Abelian variety J0(48) of dimension 3
            sage: d = H.decomposition(); d
            [Submodule of rank 2 of Integral Homology of Abelian variety J0(48) of dimension 3,
             Submodule of rank 4 of Integral Homology of Abelian variety J0(48) of dimension 3]
            sage: d[0].ambient_hecke_module()
            Integral Homology of Abelian variety J0(48) of dimension 3
        """
    def free_module(self):
        """
        Return the underlying free module of the homology group.

        EXAMPLES::

            sage: H = J0(48).homology()
            sage: K = H.decomposition()[1]; K
            Submodule of rank 4 of Integral Homology of Abelian variety J0(48) of dimension 3
            sage: K.free_module()
            Free module of degree 6 and rank 4 over Integer Ring
            Echelon basis matrix:
            [ 1  0  0  0  0  0]
            [ 0  1  0  0  1 -1]
            [ 0  0  1  0 -1  1]
            [ 0  0  0  1  0 -1]
        """
    def hecke_bound(self):
        """
        Return a bound on the number of Hecke operators needed to generate
        the Hecke algebra acting on this homology group.

        EXAMPLES::

            sage: d = J0(43).homology().decomposition(2); d
            [Submodule of rank 2 of Integral Homology of Abelian variety J0(43) of dimension 3,
             Submodule of rank 4 of Integral Homology of Abelian variety J0(43) of dimension 3]

        Because the first factor has dimension 2 it corresponds to an
        elliptic curve, so we have a Hecke bound of 1.

        ::

            sage: d[0].hecke_bound()
            1
            sage: d[1].hecke_bound()
            8
        """
    def hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on this
        homology group.

        EXAMPLES::

            sage: d = J0(125).homology(GF(17)).decomposition(2); d
            [Submodule of rank 4 of Homology with coefficients in Finite Field of size 17 of Abelian variety J0(125) of dimension 8,
             Submodule of rank 4 of Homology with coefficients in Finite Field of size 17 of Abelian variety J0(125) of dimension 8,
             Submodule of rank 8 of Homology with coefficients in Finite Field of size 17 of Abelian variety J0(125) of dimension 8]
            sage: t = d[0].hecke_matrix(17); t
            [16 15 15  0]
            [ 0  5  0  2]
            [ 2  0  5 15]
            [ 0 15  0 16]
            sage: t.base_ring()
            Finite Field of size 17
            sage: t.fcp()
            (x^2 + 13*x + 16)^2
        """
    def rank(self):
        """
        Return the rank of this homology group.

        EXAMPLES::

            sage: d = J0(43).homology().decomposition(2)
            sage: [H.rank() for H in d]
            [2, 4]
        """
