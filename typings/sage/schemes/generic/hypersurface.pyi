from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.schemes.affine.affine_subscheme import AlgebraicScheme_subscheme_affine as AlgebraicScheme_subscheme_affine
from sage.schemes.projective.projective_subscheme import AlgebraicScheme_subscheme_projective as AlgebraicScheme_subscheme_projective

def is_Hypersurface(self):
    """
    Return ``True`` if ``self`` is a hypersurface, i.e. an object of the type
    :class:`ProjectiveHypersurface` or :class:`AffineHypersurface`.

    EXAMPLES::

        sage: from sage.schemes.generic.hypersurface import is_Hypersurface
        sage: R.<x, y, z> = ZZ[]
        sage: H = ProjectiveHypersurface(x*z + y^2)
        sage: is_Hypersurface(H)
        doctest:warning...
        DeprecationWarning: The function is_Hypersurface is deprecated; use 'isinstance(..., (ProjectiveHypersurface, AffineHypersurface))' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True

    ::

        sage: H = AffineHypersurface(x*z + y^2)
        sage: is_Hypersurface(H)
        True

    ::

        sage: H = ProjectiveSpace(QQ, 5)
        sage: is_Hypersurface(H)
        False
    """

class ProjectiveHypersurface(AlgebraicScheme_subscheme_projective):
    """
    The projective hypersurface defined by the given polynomial.

    EXAMPLES::

        sage: P.<x, y, z> = ProjectiveSpace(ZZ, 2)
        sage: ProjectiveHypersurface(x - y, P)
        Projective hypersurface defined by x - y
         in Projective Space of dimension 2 over Integer Ring

    ::

        sage: R.<x, y, z> = QQ[]
        sage: ProjectiveHypersurface(x - y)
        Projective hypersurface defined by x - y
         in Projective Space of dimension 2 over Rational Field
    """
    def __init__(self, poly, ambient=None) -> None:
        """
        Return the projective hypersurface in the space ambient
        defined by the polynomial ``poly``.

        If ambient is not given, it will be constructed based on ``poly``.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(ZZ, 2)
            sage: ProjectiveHypersurface(x - y, P)
            Projective hypersurface defined by x - y in Projective Space of dimension 2 over Integer Ring

        ::

            sage: R.<x, y, z> = QQ[]
            sage: ProjectiveHypersurface(x - y)
            Projective hypersurface defined by x - y in Projective Space of dimension 2 over Rational Field

        TESTS::

            sage: H = ProjectiveHypersurface(x - y)
            sage: H == loads(dumps(H))
            True
        """
    def defining_polynomial(self):
        """
        Return the polynomial equation that cuts out this projective
        hypersurface.

        EXAMPLES::

            sage: R.<x, y, z> = ZZ[]
            sage: H = ProjectiveHypersurface(x*z + y^2)
            sage: H.defining_polynomial()
            y^2 + x*z
        """

class AffineHypersurface(AlgebraicScheme_subscheme_affine):
    """
    The affine hypersurface defined by the given polynomial.

    EXAMPLES::

        sage: A.<x, y, z> = AffineSpace(ZZ, 3)
        sage: AffineHypersurface(x*y - z^3, A)
        Affine hypersurface defined by -z^3 + x*y
         in Affine Space of dimension 3 over Integer Ring

    ::

        sage: A.<x, y, z> = QQ[]
        sage: AffineHypersurface(x*y - z^3)
        Affine hypersurface defined by -z^3 + x*y
         in Affine Space of dimension 3 over Rational Field
    """
    def __init__(self, poly, ambient=None) -> None:
        """
        Return the affine hypersurface in the space ambient
        defined by the polynomial poly.

        If ambient is not given, it will be constructed based on
        poly.

        EXAMPLES::

            sage: A.<x, y, z> = AffineSpace(ZZ, 3)
            sage: AffineHypersurface(x*y - z^3, A)
            Affine hypersurface defined by -z^3 + x*y
             in Affine Space of dimension 3 over Integer Ring

        ::

            sage: A.<x, y, z> = QQ[]
            sage: AffineHypersurface(x*y - z^3)
            Affine hypersurface defined by -z^3 + x*y
             in Affine Space of dimension 3 over Rational Field

        TESTS::

            sage: H = AffineHypersurface(x*y - z^3)
            sage: H == loads(dumps(H))
            True
        """
    def defining_polynomial(self):
        """
        Return the polynomial equation that cuts out this affine
        hypersurface.

        EXAMPLES::

            sage: R.<x, y, z> = ZZ[]
            sage: H = AffineHypersurface(x*z + y^2)
            sage: H.defining_polynomial()
            y^2 + x*z
        """
