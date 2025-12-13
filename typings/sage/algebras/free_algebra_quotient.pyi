from sage.algebras.free_algebra import FreeAlgebra_generic as FreeAlgebra_generic
from sage.algebras.free_algebra_quotient_element import FreeAlgebraQuotientElement as FreeAlgebraQuotientElement
from sage.categories.algebras import Algebras as Algebras
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module import FreeModule as FreeModule
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FreeAlgebraQuotient(UniqueRepresentation, Parent):
    @staticmethod
    def __classcall__(cls, A, mons, mats, names):
        """
        Used to support unique representation.

        EXAMPLES::

            sage: H = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0]  # indirect doctest
            sage: H1 = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0]
            sage: H is H1
            True
        """
    Element = FreeAlgebraQuotientElement
    def __init__(self, A, mons, mats, names) -> None:
        """
        Return a quotient algebra defined via the action of a free algebra
        A on a (finitely generated) free module.

        The input for the quotient algebra is a list of monomials (in
        the underlying monoid for A) which form a free basis for the
        module of A, and a list of matrices, which give the action of
        the free generators of A on this monomial basis.

        EXAMPLES:

        Quaternion algebra defined in terms of three generators::

            sage: n = 3
            sage: A = FreeAlgebra(QQ,n,'i')
            sage: F = A.monoid()
            sage: i, j, k = F.gens()
            sage: mons = [F(1), i, j, k]
            sage: M = MatrixSpace(QQ,4)
            sage: mats = [M([0,1,0,0, -1,0,0,0, 0,0,0,-1, 0,0,1,0]),
            ....:         M([0,0,1,0, 0,0,0,1, -1,0,0,0, 0,-1,0,0]),
            ....:         M([0,0,0,1, 0,0,-1,0, 0,1,0,0, -1,0,0,0]) ]
            sage: H3.<i,j,k> = FreeAlgebraQuotient(A,mons,mats)
            sage: x = 1 + i + j + k
            sage: x
            1 + i + j + k
            sage: x**128
            -170141183460469231731687303715884105728
             + 170141183460469231731687303715884105728*i
             + 170141183460469231731687303715884105728*j
             + 170141183460469231731687303715884105728*k

        Same algebra defined in terms of two generators, with some penalty
        on already slow arithmetic.

        ::

            sage: n = 2
            sage: A = FreeAlgebra(QQ,n,'x')
            sage: F = A.monoid()
            sage: i, j = F.gens()
            sage: mons = [ F(1), i, j, i*j ]
            sage: r = len(mons)
            sage: M = MatrixSpace(QQ,r)
            sage: mats = [M([0,1,0,0, -1,0,0,0, 0,0,0,-1, 0,0,1,0]),
            ....:         M([0,0,1,0, 0,0,0,1, -1,0,0,0, 0,-1,0,0]) ]
            sage: H2.<i,j> = A.quotient(mons,mats)
            sage: k = i*j
            sage: x = 1 + i + j + k
            sage: x
            1 + i + j + i*j
            sage: x**128
            -170141183460469231731687303715884105728
             + 170141183460469231731687303715884105728*i
             + 170141183460469231731687303715884105728*j
             + 170141183460469231731687303715884105728*i*j

        TESTS::

            sage: TestSuite(H2).run()
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of the algebra.

        EXAMPLES::

            sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)
            sage: H.gen(0)
            i
            sage: H.gen(2)
            k

        An :exc:`IndexError` is raised if an invalid generator is requested::

            sage: H.gen(3)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 3) must be between 0 and 2

        Negative indexing into the generators is not supported::

            sage: H.gen(-1)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= -1) must be between 0 and 2
        """
    def gens(self) -> tuple:
        """
        Return the tuple of generators of ``self``.

        EXAMPLES::

            sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)
            sage: H.gens()
            (i, j, k)
        """
    def ngens(self):
        """
        Return the number of generators of the algebra.

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].ngens()
            3
        """
    def dimension(self):
        """
        Return the rank of the algebra (as a free module).

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].dimension()
            4
        """
    def matrix_action(self):
        """
        Return the matrix action used to define the algebra.

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].matrix_action()
            (
            [ 0  1  0  0]  [ 0  0  1  0]  [ 0  0  0  1]
            [-1  0  0  0]  [ 0  0  0  1]  [ 0  0 -1  0]
            [ 0  0  0 -1]  [-1  0  0  0]  [ 0  1  0  0]
            [ 0  0  1  0], [ 0 -1  0  0], [-1  0  0  0]
            )
        """
    def monomial_basis(self):
        """
        The free monoid of generators of the algebra as elements of a free
        monoid.

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].monomial_basis()
            (1, i0, i1, i2)
        """
    def rank(self):
        """
        Return the rank of the algebra (as a free module).

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].rank()
            4
        """
    def module(self):
        """
        Return the free module of the algebra.

        EXAMPLES::

            sage: H = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0]; H
            Free algebra quotient on 3 generators ('i', 'j', 'k') and dimension 4 over Rational Field
            sage: H.module()
            Vector space of dimension 4 over Rational Field
        """
    def monoid(self):
        """
        Return the free monoid of generators of the algebra.

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].monoid()
            Free monoid on 3 generators (i0, i1, i2)
        """
    def free_algebra(self):
        """
        Return the free algebra generating the algebra.

        EXAMPLES::

            sage: sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)[0].free_algebra()
            Free Algebra on 3 generators (i0, i1, i2) over Rational Field
        """

def hamilton_quatalg(R):
    """
    Hamilton quaternion algebra over the commutative ring ``R``,
    constructed as a free algebra quotient.

    INPUT:

    - ``R`` -- a commutative ring

    OUTPUT:

    - ``Q`` -- quaternion algebra
    - ``gens`` -- generators for ``Q``

    EXAMPLES::

        sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(ZZ)
        sage: H
        Free algebra quotient on 3 generators ('i', 'j', 'k') and dimension 4
         over Integer Ring
        sage: i^2
        -1
        sage: i in H
        True

    Note that there is another vastly more efficient model for
    quaternion algebras in Sage; the one here is mainly for testing
    purposes::

        sage: R.<i,j,k> = QuaternionAlgebra(QQ,-1,-1)  # much fast than the above
    """
