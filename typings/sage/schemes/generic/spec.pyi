from _typeshed import Incomplete
from sage.categories.functor import Functor as Functor
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.scheme import AffineScheme as AffineScheme
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def Spec(R, S=None):
    """
    Apply the Spec functor to `R`.

    INPUT:

    - ``R`` -- either a commutative ring or a ring homomorphism

    - ``S`` -- a commutative ring (optional), the base ring

    OUTPUT:

    - ``AffineScheme`` -- the affine scheme `\\mathrm{Spec}(R)`

    EXAMPLES::

        sage: Spec(QQ)
        Spectrum of Rational Field
        sage: Spec(PolynomialRing(QQ, 'x'))
        Spectrum of Univariate Polynomial Ring in x over Rational Field
        sage: Spec(PolynomialRing(QQ, 'x', 3))
        Spectrum of Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
        sage: X = Spec(PolynomialRing(GF(49,'a'), 3, 'x')); X                           # needs sage.rings.finite_rings
        Spectrum of Multivariate Polynomial Ring in x0, x1, x2
         over Finite Field in a of size 7^2
        sage: TestSuite(X).run()                                                        # needs sage.rings.finite_rings

    Applying ``Spec`` twice to the same ring gives identical output
    (see :issue:`17008`)::

        sage: A = Spec(ZZ); B = Spec(ZZ)
        sage: A is B
        True

    A :exc:`TypeError` is raised if the input is not a commutative ring::

        sage: Spec(5)
        Traceback (most recent call last):
        ...
        TypeError: x (=5) is not in Category of commutative rings
        sage: Spec(FreeAlgebra(QQ, 2, 'x'))                                             # needs sage.combinat sage.modules
        Traceback (most recent call last):
        ...
        TypeError: x (=Free Algebra on 2 generators (x0, x1) over Rational Field)
        is not in Category of commutative rings

    TESTS::

        sage: X = Spec(ZZ)
        sage: X
        Spectrum of Integer Ring
        sage: X.base_scheme()
        Spectrum of Integer Ring
        sage: X.base_ring()
        Integer Ring
        sage: X.dimension()
        1
        sage: Spec(QQ, QQ).base_scheme()
        Spectrum of Rational Field
        sage: Spec(RDF, QQ).base_scheme()
        Spectrum of Rational Field
    """

class SpecFunctor(Functor, UniqueRepresentation):
    """
    The Spec functor.
    """
    def __init__(self, base_ring=None) -> None:
        """
        EXAMPLES::

            sage: from sage.schemes.generic.spec import SpecFunctor
            sage: SpecFunctor()
            Spec functor from Category of commutative rings to Category of schemes
            sage: SpecFunctor(QQ)
            Spec functor from Category of commutative rings to
             Category of schemes over Rational Field
        """

SpecZ: Incomplete
