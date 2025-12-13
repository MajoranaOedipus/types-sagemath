from sage.structure.element import Element as Element
from sage.structure.richcmp import richcmp as richcmp

class SchemePoint(Element):
    """
    Base class for points on a scheme, either topological or defined
    by a morphism.
    """
    def __init__(self, S, parent=None) -> None:
        """
        INPUT:

        - ``S`` -- a scheme

        - ``parent`` -- the parent in which to construct this point

        TESTS::

            sage: from sage.schemes.generic.point import SchemePoint
            sage: S = Spec(ZZ)
            sage: P = SchemePoint(S); P
            Point on Spectrum of Integer Ring
        """
    def scheme(self):
        """
        Return the scheme on which ``self`` is a point.

        EXAMPLES::

            sage: from sage.schemes.generic.point import SchemePoint
            sage: S = Spec(ZZ)
            sage: P = SchemePoint(S)
            sage: P.scheme()
            Spectrum of Integer Ring
        """

def is_SchemeTopologicalPoint(x): ...

class SchemeTopologicalPoint(SchemePoint):
    """
    Base class for topological points on schemes.
    """
    def __init__(self, S) -> None:
        """
        INPUT:

        - ``S`` -- a scheme

        TESTS:

        The parent of a topological point is the scheme on which it
        lies (see :issue:`7946`)::

            sage: R = Zmod(8)
            sage: S = Spec(R)
            sage: x = S(R.ideal(2))
            sage: isinstance(x, sage.schemes.generic.point.SchemeTopologicalPoint)
            True
            sage: x.parent() is S
            True
        """

class SchemeTopologicalPoint_affine_open(SchemeTopologicalPoint):
    def __init__(self, u, x) -> None:
        """
        INPUT:

        - ``u`` -- morphism with domain an affine scheme `U`

        - ``x`` -- topological point on `U`
        """
    def point_on_affine(self):
        """
        Return the scheme point on the affine open `U`.
        """
    def affine_open(self):
        """
        Return the affine open subset `U`.
        """
    def embedding_of_affine_open(self):
        """
        Return the embedding from the affine open subset `U` into this scheme.
        """

class SchemeTopologicalPoint_prime_ideal(SchemeTopologicalPoint):
    def __init__(self, S, P, check: bool = False) -> None:
        """
        INPUT:

        - ``S`` -- an affine scheme

        - ``P`` -- a prime ideal of the coordinate ring of `S`, or
          anything that can be converted into such an ideal

        TESTS::

            sage: from sage.schemes.generic.point import SchemeTopologicalPoint_prime_ideal
            sage: S = Spec(ZZ)
            sage: P = SchemeTopologicalPoint_prime_ideal(S, 3); P
            Point on Spectrum of Integer Ring defined by the Principal ideal (3) of Integer Ring
            sage: SchemeTopologicalPoint_prime_ideal(S, 6, check=True)
            Traceback (most recent call last):
            ...
            ValueError: The argument Principal ideal (6) of Integer Ring must be a prime ideal of Integer Ring
            sage: SchemeTopologicalPoint_prime_ideal(S, ZZ.ideal(7))
            Point on Spectrum of Integer Ring defined by the Principal ideal (7) of Integer Ring

        We define a parabola in the projective plane as a point
        corresponding to a prime ideal::

            sage: P2.<x, y, z> = ProjectiveSpace(2, QQ)
            sage: SchemeTopologicalPoint_prime_ideal(P2, y*z - x^2)
            Point on Projective Space of dimension 2 over Rational Field defined by
             the Ideal (-x^2 + y*z) of Multivariate Polynomial Ring in x, y, z over Rational Field
        """
    def prime_ideal(self):
        """
        Return the prime ideal that defines this scheme point.

        EXAMPLES::

            sage: from sage.schemes.generic.point import SchemeTopologicalPoint_prime_ideal
            sage: P2.<x, y, z> = ProjectiveSpace(2, QQ)
            sage: pt = SchemeTopologicalPoint_prime_ideal(P2, y*z - x^2)
            sage: pt.prime_ideal()
            Ideal (-x^2 + y*z) of Multivariate Polynomial Ring in x, y, z over Rational Field
        """
