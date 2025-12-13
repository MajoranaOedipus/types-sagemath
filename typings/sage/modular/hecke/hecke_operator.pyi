from . import algebra as algebra, morphism as morphism
from sage.categories.homset import End as End
from sage.rings.integer import Integer as Integer
from sage.structure.element import AlgebraElement as AlgebraElement
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

def is_HeckeOperator(x):
    """
    Return ``True`` if x is of type HeckeOperator.

    EXAMPLES::

        sage: from sage.modular.hecke.hecke_operator import is_HeckeOperator
        sage: M = ModularSymbols(Gamma0(7), 4)
        sage: is_HeckeOperator(M.T(3))
        doctest:warning...
        DeprecationWarning: the function is_HeckeOperator is deprecated;
        use 'isinstance(..., HeckeOperator)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        True
        sage: is_HeckeOperator(M.T(3) + M.T(5))
        False
    """
def is_HeckeAlgebraElement(x):
    """
    Return ``True`` if x is of type HeckeAlgebraElement.

    EXAMPLES::

        sage: from sage.modular.hecke.hecke_operator import is_HeckeAlgebraElement
        sage: M = ModularSymbols(Gamma0(7), 4)
        sage: is_HeckeAlgebraElement(M.T(3))
        doctest:warning...
        DeprecationWarning: the function is_HeckeAlgebraElement is deprecated;
        use 'isinstance(..., HeckeAlgebraElement)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        True
        sage: is_HeckeAlgebraElement(M.T(3) + M.T(5))
        True
    """

class HeckeAlgebraElement(AlgebraElement):
    """
    Base class for elements of Hecke algebras.
    """
    def __init__(self, parent) -> None:
        """
        Create an element of a Hecke algebra.

        EXAMPLES::

            sage: R = ModularForms(Gamma0(7), 4).hecke_algebra()
            sage: sage.modular.hecke.hecke_operator.HeckeAlgebraElement(R)  # please don't do this!
            Generic element of a structure
        """
    def domain(self):
        """
        The domain of this operator. This is the Hecke module associated to the
        parent Hecke algebra.

        EXAMPLES::

            sage: R = ModularForms(Gamma0(7), 4).hecke_algebra()
            sage: sage.modular.hecke.hecke_operator.HeckeAlgebraElement(R).domain()
            Modular Forms space of dimension 3 for Congruence Subgroup Gamma0(7)
             of weight 4 over Rational Field
        """
    def codomain(self):
        """
        The codomain of this operator. This is the Hecke module associated to the
        parent Hecke algebra.

        EXAMPLES::

            sage: R = ModularForms(Gamma0(7), 4).hecke_algebra()
            sage: sage.modular.hecke.hecke_operator.HeckeAlgebraElement(R).codomain()
            Modular Forms space of dimension 3 for Congruence Subgroup Gamma0(7)
             of weight 4 over Rational Field
        """
    def hecke_module_morphism(self):
        """
        Return the endomorphism of Hecke modules defined by the matrix
        attached to this Hecke operator.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma1(13))
            sage: t = M.hecke_operator(2)
            sage: t
            Hecke operator T_2 on Modular Symbols space of dimension 15 for Gamma_1(13)
             of weight 2 with sign 0 over Rational Field
            sage: t.hecke_module_morphism()
            Hecke module morphism T_2 defined by the matrix
            [ 2  0  0  0  0  0  0  1  0  0  1  0  0  0  0]
            [ 0  2  0  1  0  1  0  0 -1  0  0  0  0  0  1]
            [ 0  1  2  0  0  0  0  0  0  0  0 -1  1  0  0]
            [ 1  0  0  2  0 -1  1  0  1  0 -1  1 -1  0  0]
            [ 0  0  1  0  2  0 -1  0  0  0  0  0  0  0  0]
            [ 0  0  0  0  0  0  0  0  0  0  0  1 -2  2 -1]
            [ 0  0  0  0  0  2 -1  0 -1  0  0  0  0  1  0]
            [ 0  0  0  0  1  0  0  2  0  0  0  0  0  0 -1]
            [ 0  0  0  0  0  1  0  0 -1  0  2 -1  0  2 -1]
            [ 0  0  0  0  0  1  1  0  0 -1  0  1 -1  2  0]
            [ 0  0  0  0  0  2  0  0 -1 -1  1 -1  0  1  0]
            [ 0  0  0  0  0  1  1  0  1  0  0  0 -1  1  0]
            [ 0  0  0  0  0  1  1  0  0  1  0  0  0  0  0]
            [ 0  0  0  0  0  1  0  0  1 -1  2  0  0  0 -1]
            [ 0  0  0  0  0  0  0  0  0  1  0 -1  2  0 -1]
            Domain:   Modular Symbols space of dimension 15 for Gamma_1(13) of weight ...
            Codomain: Modular Symbols space of dimension 15 for Gamma_1(13) of weight ...
        """
    def __call__(self, x):
        """
        Apply this Hecke operator to `x`.

        EXAMPLES::

            sage: M = ModularSymbols(11); t2 = M.hecke_operator(2)
            sage: t2(M.gen(0))
            3*(1,0) - (1,9)

        ::

            sage: t2 = M.hecke_operator(2); t3 = M.hecke_operator(3)
            sage: t3(t2(M.gen(0)))
            12*(1,0) - 2*(1,9)
            sage: (t3*t2)(M.gen(0))
            12*(1,0) - 2*(1,9)
        """
    def __rmul__(self, left):
        """
        EXAMPLES::

            sage: M = ModularSymbols(11); t2 = M.hecke_operator(2)
            sage: 2*t2
            Hecke operator on Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field defined by:
            [ 6  0 -2]
            [ 0 -4  0]
            [ 0  0 -4]
        """
    def apply_sparse(self, x):
        """
        Apply this Hecke operator to x, where we avoid computing the matrix
        of x if possible.

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: T = M.hecke_operator(23)
            sage: T.apply_sparse(M.gen(0))
            24*(1,0) - 5*(1,9)
        """
    def charpoly(self, var: str = 'x'):
        """
        Return the characteristic polynomial of this Hecke operator.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        OUTPUT: a monic polynomial in the given variable

        EXAMPLES::

            sage: M = ModularSymbols(Gamma1(6),4)
            sage: M.hecke_operator(2).charpoly('x')
            x^6 - 14*x^5 + 29*x^4 + 172*x^3 - 124*x^2 - 320*x + 256
        """
    def decomposition(self):
        """
        Decompose the Hecke module under the action of this Hecke
        operator.

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: t2 = M.hecke_operator(2)
            sage: t2.decomposition()
            [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field]

        ::

            sage: M = ModularSymbols(33, sign=1).new_submodule()
            sage: T = M.hecke_operator(2)
            sage: T.decomposition()
            [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 6 for Gamma_0(33) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 6 for Gamma_0(33) of weight 2 with sign 1 over Rational Field]
        """
    def det(self):
        """
        Return the determinant of this Hecke operator.

        EXAMPLES::

            sage: M = ModularSymbols(23)
            sage: T = M.hecke_operator(3)
            sage: T.det()
            100
        """
    def fcp(self, var: str = 'x'):
        """
        Return the factorization of the characteristic polynomial of this
        Hecke operator.

        EXAMPLES::

            sage: M = ModularSymbols(23)
            sage: T = M.hecke_operator(3)
            sage: T.fcp('x')
            (x - 4) * (x^2 - 5)^2
        """
    def image(self):
        """
        Return the image of this Hecke operator.

        EXAMPLES::

            sage: M = ModularSymbols(23)
            sage: T = M.hecke_operator(3)
            sage: T.fcp('x')
            (x - 4) * (x^2 - 5)^2
            sage: T.image()
            Modular Symbols subspace of dimension 5 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
            sage: (T-4).image()
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
            sage: (T**2-5).image()
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
        """
    def kernel(self):
        """
        Return the kernel of this Hecke operator.

        EXAMPLES::

            sage: M = ModularSymbols(23)
            sage: T = M.hecke_operator(3)
            sage: T.fcp('x')
            (x - 4) * (x^2 - 5)^2
            sage: T.kernel()
            Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
            sage: (T-4).kernel()
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
            sage: (T**2-5).kernel()
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
        """
    def trace(self):
        """
        Return the trace of this Hecke operator.

        ::

            sage: M = ModularSymbols(1,12)
            sage: T = M.hecke_operator(2)
            sage: T.trace()
            2001
        """
    def __getitem__(self, ij):
        """
        EXAMPLES::

            sage: M = ModularSymbols(1,12)
            sage: T = M.hecke_operator(2).matrix_form()
            sage: T[0,0]
            -24
        """

class HeckeAlgebraElement_matrix(HeckeAlgebraElement):
    """
    An element of the Hecke algebra represented by a matrix.
    """
    def __init__(self, parent, A) -> None:
        """
        Initialise an element from a matrix. This *must* be over the base ring
        of ``self`` and have the right size.

        This is a bit overkill as similar checks will be performed by the call
        and coerce methods of the parent of self, but it can't hurt to be
        paranoid. Any fancy coercion / base_extension / etc happens there, not
        here.

        TESTS::

            sage: T = ModularForms(Gamma0(7), 4).hecke_algebra()
            sage: M = sage.modular.hecke.hecke_operator.HeckeAlgebraElement_matrix(T, matrix(QQ,3,[2,3,0,1,2,3,7,8,9])); M
            Hecke operator on Modular Forms space of dimension 3 for Congruence Subgroup Gamma0(7) of weight 4 over Rational Field defined by:
            [2 3 0]
            [1 2 3]
            [7 8 9]
            sage: loads(dumps(M)) == M
            True
            sage: sage.modular.hecke.hecke_operator.HeckeAlgebraElement_matrix(T, matrix(Integers(2),3,[2,3,0,1,2,3,7,8,9]))
            Traceback (most recent call last):
            ...
            TypeError: base ring of matrix (Ring of integers modulo 2) does not match base ring of space (Rational Field)
            sage: sage.modular.hecke.hecke_operator.HeckeAlgebraElement_matrix(T, matrix(QQ,2,[2,3,0,1]))
            Traceback (most recent call last):
            ...
            TypeError: A must be a square matrix of rank 3
        """
    def matrix(self):
        """
        Return the matrix that defines this Hecke algebra element.

        EXAMPLES::

            sage: M = ModularSymbols(1,12)
            sage: T = M.hecke_operator(2).matrix_form()
            sage: T.matrix()
            [ -24    0    0]
            [   0  -24    0]
            [4860    0 2049]
        """

class DiamondBracketOperator(HeckeAlgebraElement_matrix):
    """
    The diamond bracket operator `\\langle d \\rangle` for some `d \\in \\ZZ /
    N\\ZZ` (which need not be a unit, although if it is not, the operator will
    be zero).
    """
    def __init__(self, parent, d) -> None:
        """
        Standard init function.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma1(5),6)
            sage: d = M.diamond_bracket_operator(2); d # indirect doctest
            Diamond bracket operator <2> on Modular Symbols space of dimension 10 for Gamma_1(5) of weight 6 with sign 0 over Rational Field
            sage: type(d)
            <class 'sage.modular.hecke.hecke_operator.DiamondBracketOperator'>
            sage: d.matrix()
            [    0     1     0     0     0     0     0     0     0     0]
            [    1     0     0     0     0     0     0     0     0     0]
            [    0     0     0     0     0     0     1     0     0     0]
            [    0     0     0     0     0     0     0     0     0     1]
            [    0     0     0     0     0     0     0     1     0     0]
            [    0     0 17/16 11/16  -3/4    -1 17/16  -3/4     0 11/16]
            [    0     0     1     0     0     0     0     0     0     0]
            [    0     0     0     0     1     0     0     0     0     0]
            [    0     0  -1/2   1/2     1     0  -1/2     1    -1   1/2]
            [    0     0     0     1     0     0     0     0     0     0]
            sage: d**4 == 1
            True
        """

class HeckeOperator(HeckeAlgebraElement):
    """
    The Hecke operator `T_n` for some `n` (which need not be coprime to the
    level). The matrix is not computed until it is needed.
    """
    def __init__(self, parent, n) -> None:
        """
        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: H = M.hecke_operator(2005); H
            Hecke operator T_2005 on Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: H == loads(dumps(H))
            True

        We create a Hecke operator of large index (greater than 32 bits)::

            sage: M1 =  ModularSymbols(21,2)
            sage: M1.hecke_operator(13^9)
            Hecke operator T_10604499373 on Modular Symbols space of dimension 5 for Gamma_0(21) of weight 2 with sign 0 over Rational Field
        """
    def index(self):
        """
        Return the index of this Hecke operator, i.e., if this Hecke
        operator is `T_n`, return the int `n`.

        EXAMPLES::

            sage: T = ModularSymbols(11).hecke_operator(17)
            sage: T.index()
            17
        """
    def matrix(self, *args, **kwds):
        """
        Return the matrix underlying this Hecke operator.

        EXAMPLES::

            sage: T = ModularSymbols(11).hecke_operator(17)
            sage: T.matrix()
            [18  0 -4]
            [ 0 -2  0]
            [ 0  0 -2]
        """
    def matrix_form(self):
        """
        Return the matrix form of this element of a Hecke algebra.

        ::

            sage: T = ModularSymbols(11).hecke_operator(17)
            sage: T.matrix_form()
            Hecke operator on Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field defined by:
            [18  0 -4]
            [ 0 -2  0]
            [ 0  0 -2]
        """
