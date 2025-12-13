from sage.categories.homset import Hom as Hom
from sage.categories.schemes import Schemes as Schemes
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.schemes.projective.projective_subscheme import AlgebraicScheme_subscheme_projective as AlgebraicScheme_subscheme_projective

class KummerSurface(AlgebraicScheme_subscheme_projective):
    def __init__(self, J) -> None:
        """
        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: f = x^5 + x + 1
            sage: X = HyperellipticCurve(f)
            sage: J = Jacobian(X)
            sage: K = KummerSurface(J); K
            Closed subscheme of Projective Space of dimension 3 over Rational Field defined by:
            X0^4 - 4*X0*X1^3 + 4*X0^2*X1*X2 - 4*X0*X1^2*X2 + 2*X0^2*X2^2 + X2^4 - 4*X0^3*X3 - 2*X0^2*X1*X3 - 2*X1*X2^2*X3 + X1^2*X3^2 - 4*X0*X2*X3^2
        """
