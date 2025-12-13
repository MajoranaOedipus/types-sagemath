from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.fields import Fields as Fields
from sage.categories.map import Map as Map
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.latex import latex as latex
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.affine.affine_homset import SchemeHomset_points_affine as SchemeHomset_points_affine, SchemeHomset_polynomial_affine_space as SchemeHomset_polynomial_affine_space
from sage.schemes.affine.affine_morphism import SchemeMorphism_polynomial_affine_space as SchemeMorphism_polynomial_affine_space, SchemeMorphism_polynomial_affine_space_field as SchemeMorphism_polynomial_affine_space_field, SchemeMorphism_polynomial_affine_space_finite_field as SchemeMorphism_polynomial_affine_space_finite_field
from sage.schemes.affine.affine_point import SchemeMorphism_point_affine as SchemeMorphism_point_affine, SchemeMorphism_point_affine_field as SchemeMorphism_point_affine_field, SchemeMorphism_point_affine_finite_field as SchemeMorphism_point_affine_finite_field
from sage.schemes.generic.ambient_space import AmbientSpace as AmbientSpace
from sage.schemes.generic.scheme import AffineScheme as AffineScheme
from sage.structure.category_object import normalize_names as normalize_names

def is_AffineSpace(x) -> bool:
    """
    Return ``True`` if ``x`` is an affine space.

    EXAMPLES::

        sage: from sage.schemes.affine.affine_space import is_AffineSpace
        sage: is_AffineSpace(AffineSpace(5, names='x'))
        doctest:warning...
        DeprecationWarning: The function is_AffineSpace is deprecated; use 'isinstance(..., AffineSpace_generic)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: is_AffineSpace(AffineSpace(5, GF(9, 'alpha'), names='x'))                 # needs sage.rings.finite_rings
        True
        sage: is_AffineSpace(Spec(ZZ))
        False
    """
def AffineSpace(n, R=None, names=None, ambient_projective_space=None, default_embedding_index=None):
    """
    Return affine space of dimension ``n`` over the ring ``R``.

    EXAMPLES:

    The dimension and ring can be given in either order::

        sage: AffineSpace(3, QQ, 'x')
        Affine Space of dimension 3 over Rational Field
        sage: AffineSpace(5, QQ, 'x')
        Affine Space of dimension 5 over Rational Field
        sage: A = AffineSpace(2, QQ, names='XY'); A
        Affine Space of dimension 2 over Rational Field
        sage: A.coordinate_ring()
        Multivariate Polynomial Ring in X, Y over Rational Field

    Use the divide operator for base extension::

        sage: AffineSpace(5, names='x')/GF(17)
        Affine Space of dimension 5 over Finite Field of size 17

    The default base ring is `\\ZZ`::

        sage: AffineSpace(5, names='x')
        Affine Space of dimension 5 over Integer Ring

    There is also an affine space associated to each polynomial ring::

        sage: R = GF(7)['x, y, z']
        sage: A = AffineSpace(R); A
        Affine Space of dimension 3 over Finite Field of size 7
        sage: A.coordinate_ring() is R
        True

    TESTS::

        sage: R.<w> = QQ[]
        sage: A.<w> = AffineSpace(R)
        sage: A.gens() == R.gens()
        True

        sage: R.<x> = QQ[]
        sage: A.<z> = AffineSpace(R)
        Traceback (most recent call last):
        ...
        NameError: variable names passed to AffineSpace conflict with names in ring
    """

class AffineSpace_generic(AmbientSpace, AffineScheme):
    """
    Affine space of dimension `n` over the ring `R`.

    EXAMPLES::

        sage: X.<x,y,z> = AffineSpace(3, QQ)
        sage: X.base_scheme()
        Spectrum of Rational Field
        sage: X.base_ring()
        Rational Field
        sage: X.category()
        Category of schemes over Rational Field
        sage: X.structure_morphism()
        Scheme morphism:
          From: Affine Space of dimension 3 over Rational Field
          To:   Spectrum of Rational Field
          Defn: Structure map

    Loading and saving::

        sage: loads(X.dumps()) == X
        True

    We create several other examples of affine spaces::

        sage: AffineSpace(5, PolynomialRing(QQ, 'z'), 'Z')
        Affine Space of dimension 5 over Univariate Polynomial Ring in z over Rational Field

        sage: AffineSpace(RealField(), 3, 'Z')                                          # needs sage.rings.real_mpfr
        Affine Space of dimension 3 over Real Field with 53 bits of precision

        sage: AffineSpace(Qp(7), 2, 'x')                                                # needs sage.rings.padics
        Affine Space of dimension 2 over 7-adic Field with capped relative precision 20

    Even 0-dimensional affine spaces are supported::

        sage: AffineSpace(0)
        Affine Space of dimension 0 over Integer Ring
    """
    def __init__(self, n, R, names, ambient_projective_space, default_embedding_index) -> None:
        """
        EXAMPLES::

            sage: AffineSpace(3, Zp(5), 'y')                                            # needs sage.rings.padics
            Affine Space of dimension 3 over 5-adic Ring with capped relative precision 20
        """
    def __iter__(self):
        """
        Return iterator over the elements of this affine space when defined over a finite field.

        EXAMPLES::

            sage: FF = FiniteField(3)
            sage: AA = AffineSpace(FF, 0)
            sage: [ x for x in AA ]
            [()]
            sage: AA = AffineSpace(FF, 1, 'Z')
            sage: [ x for x in AA ]
            [(0), (1), (2)]
            sage: AA.<z,w> = AffineSpace(FF, 2)
            sage: [ x for x in AA ]
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        AUTHOR:

        - David Kohel
        """
    def ngens(self):
        """
        Return the number of generators of ``self``, i.e. the number of
        variables in the coordinate ring of ``self``.

        EXAMPLES::

            sage: AffineSpace(3, QQ).ngens()
            3
            sage: AffineSpace(7, ZZ).ngens()
            7
        """
    def rational_points(self, F=None):
        """
        Return the list of ``F``-rational points on the affine space ``self``,
        where ``F`` is a given finite field, or the base ring of ``self``.

        EXAMPLES::

            sage: A = AffineSpace(1, GF(3))
            sage: A.rational_points()
            [(0), (1), (2)]
            sage: A.rational_points(GF(3^2, 'b'))                                       # needs sage.rings.finite_rings
            [(0), (b), (b + 1), (2*b + 1), (2), (2*b), (2*b + 2), (b + 2), (1)]

            sage: AffineSpace(2, ZZ).rational_points(GF(2))
            [(0, 0), (0, 1), (1, 0), (1, 1)]

        TESTS::

            sage: AffineSpace(2, QQ).rational_points()
            Traceback (most recent call last):
            ...
            TypeError: base ring (= Rational Field) must be a finite field
            sage: AffineSpace(1, GF(3)).rational_points(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: second argument (= Integer Ring) must be a finite field
        """
    def __eq__(self, right):
        """
        Compare the space with ``right``.

        EXAMPLES::

            sage: AffineSpace(QQ, 3, 'a') == AffineSpace(ZZ, 3, 'a')
            False
            sage: AffineSpace(ZZ, 1, 'a') == AffineSpace(ZZ, 0, 'a')
            False
            sage: A = AffineSpace(ZZ, 1, 'x')
            sage: loads(A.dumps()) == A
            True
        """
    def __ne__(self, other):
        """
        Check whether the space is not equal to ``other``.

        EXAMPLES::

            sage: AffineSpace(QQ, 3, 'a') != AffineSpace(ZZ, 3, 'a')
            True
            sage: AffineSpace(ZZ, 1, 'a') != AffineSpace(ZZ, 0, 'a')
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: hash(AffineSpace(QQ, 3, 'a')) == hash(AffineSpace(ZZ, 3, 'a'))
            False
            sage: hash(AffineSpace(ZZ, 1, 'a')) == hash(AffineSpace(ZZ, 0, 'a'))
            False
        """
    def __pow__(self, m):
        '''
        Return the Cartesian power of this space.

        INPUT:

        - ``m`` -- integer

        OUTPUT: affine ambient space

        EXAMPLES::

            sage: A = AffineSpace(1, QQ, \'x\')
            sage: A5 = A^5; A5
            Affine Space of dimension 5 over Rational Field
            sage: A5.variable_names()
            (\'x0\', \'x1\', \'x2\', \'x3\', \'x4\')
            sage: A2 = AffineSpace(2, QQ, "x, y")
            sage: A4 = A2^2; A4
            Affine Space of dimension 4 over Rational Field
            sage: A4.variable_names()
            (\'x0\', \'x1\', \'x2\', \'x3\')

        As you see, custom variable names are not preserved by power operator,
        since there is no natural way to make new ones in general.
        '''
    def __mul__(self, right):
        """
        Create the product of affine spaces.

        INPUT:

        - ``right`` -- an affine space or subscheme

        OUTPUT: an affine space.= or subscheme

        EXAMPLES::

            sage: A1 = AffineSpace(QQ, 1, 'x')
            sage: A2 = AffineSpace(QQ, 2, 'y')
            sage: A3 = A1*A2; A3
            Affine Space of dimension 3 over Rational Field
            sage: A3.variable_names()
            ('x', 'y0', 'y1')

            ::

            sage: A2 = AffineSpace(ZZ, 2, 't')
            sage: A3 = AffineSpace(ZZ, 3, 'x')
            sage: A3.inject_variables()
            Defining x0, x1, x2
            sage: X = A3.subscheme([x0*x2 - x1])
            sage: A2*X
            Closed subscheme of Affine Space of dimension 5 over Integer Ring defined by:
              x0*x2 - x1

        ::

            sage: S = ProjectiveSpace(QQ, 3, 'x')
            sage: T = AffineSpace(2, QQ, 'y')
            sage: T*S
            Traceback (most recent call last):
            ...
            TypeError: Projective Space of dimension 3 over Rational Field
            must be an affine space or affine subscheme
        """
    def change_ring(self, R):
        """
        Return an affine space over ring ``R`` and otherwise the same as this space.

        INPUT:

        - ``R`` -- commutative ring or morphism

        OUTPUT: an affine space over ``R``

        .. NOTE::

            There is no need to have any relation between ``R`` and the base ring
            of  this space, if you want to have such a relation, use
            ``self.base_extend(R)`` instead.

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(3, ZZ)
            sage: AQ = A.change_ring(QQ); AQ
            Affine Space of dimension 3 over Rational Field
            sage: AQ.change_ring(GF(5))
            Affine Space of dimension 3 over Finite Field of size 5

        ::

            sage: K.<w> = QuadraticField(5)                                             # needs sage.rings.number_field
            sage: A = AffineSpace(K, 2, 't')                                            # needs sage.rings.number_field
            sage: A.change_ring(K.embeddings(CC)[1])                                    # needs sage.rings.number_field
            Affine Space of dimension 2 over Complex Field with 53 bits of precision
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring of this scheme, if defined.

        EXAMPLES::

            sage: R = AffineSpace(2, GF(9,'alpha'), 'z').coordinate_ring(); R           # needs sage.rings.finite_rings
            Multivariate Polynomial Ring in z0, z1 over Finite Field in alpha of size 3^2
            sage: AffineSpace(3, R, 'x').coordinate_ring()                              # needs sage.rings.finite_rings
            Multivariate Polynomial Ring in x0, x1, x2 over Multivariate Polynomial Ring
            in z0, z1 over Finite Field in alpha of size 3^2
        """
    def projective_embedding(self, i=None, PP=None):
        """
        Return a morphism from this space into an ambient projective space
        of the same dimension.

        INPUT:

        - ``i`` -- integer (default: dimension of self = last coordinate)
          determines which projective embedding to compute. The embedding is
          that which has a 1 in the `i`-th coordinate, numbered from 0.

        - ``PP`` -- (default: ``None``) ambient projective space, i.e.,
          codomain of morphism; this is constructed if it is not given.

        EXAMPLES::

            sage: AA = AffineSpace(2, QQ, 'x')
            sage: pi = AA.projective_embedding(0); pi
            Scheme morphism:
              From: Affine Space of dimension 2 over Rational Field
              To:   Projective Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x0, x1) to (1 : x0 : x1)
            sage: z = AA(3, 4)
            sage: pi(z)
            (1/4 : 3/4 : 1)
            sage: pi(AA(0,2))
            (1/2 : 0 : 1)
            sage: pi = AA.projective_embedding(1); pi
            Scheme morphism:
              From: Affine Space of dimension 2 over Rational Field
              To:   Projective Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x0, x1) to (x0 : 1 : x1)
            sage: pi(z)
            (3/4 : 1/4 : 1)
            sage: pi = AA.projective_embedding(2)
            sage: pi(z)
            (3 : 4 : 1)

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: A.projective_embedding(2).codomain().affine_patch(2) == A
            True

        TESTS:

        Check that :issue:`25897` is fixed::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: A.projective_embedding(4)
            Traceback (most recent call last):
            ...
            ValueError: argument i (=4) must be between 0 and 2, inclusive
        """
    def subscheme(self, X, **kwds):
        """
        Return the closed subscheme defined by ``X``.

        INPUT:

        - ``X`` -- list or tuple of equations

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme([x, y^2, x*y^2]); X
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x,
              y^2,
              x*y^2

        ::

            sage: # needs sage.libs.singular
            sage: X.defining_polynomials ()
            (x, y^2, x*y^2)
            sage: I = X.defining_ideal(); I
            Ideal (x, y^2, x*y^2) of Multivariate Polynomial Ring in x, y over Rational Field
            sage: I.groebner_basis()
            [y^2, x]
            sage: X.dimension()
            0
            sage: X.base_ring()
            Rational Field
            sage: X.base_scheme()
            Spectrum of Rational Field
            sage: X.structure_morphism()
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                    defined by: x, y^2, x*y^2
              To:   Spectrum of Rational Field
              Defn: Structure map
            sage: X.dimension()
            0
        """
    def chebyshev_polynomial(self, n, kind: str = 'first', monic: bool = False):
        """
        Generate an endomorphism of this affine line by a Chebyshev polynomial.

        Chebyshev polynomials are a sequence of recursively defined orthogonal
        polynomials. Chebyshev of the first kind are defined as `T_0(x) = 1`,
        `T_1(x) = x`, and `T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x)`. Chebyshev of
        the second kind are defined as `U_0(x) = 1`,
        `U_1(x) = 2x`, and `U_{n+1}(x) = 2xU_n(x) - U_{n-1}(x)`.

        INPUT:

        - ``n`` -- nonnegative integer

        - ``kind`` -- ``'first'`` (default) or ``'second'`` specifying which
          kind of Chebyshev the user would like to generate

        - ``monic`` -- boolean (default: ``False``) specifying if the
          polynomial defining the system should be monic or not

        OUTPUT: :class:`DynamicalSystem_affine`

        EXAMPLES::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: A.chebyshev_polynomial(5, 'first')                                    # needs sage.schemes
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to (16*x^5 - 20*x^3 + 5*x)

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: A.chebyshev_polynomial(3, 'second')                                   # needs sage.schemes
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to (8*x^3 - 4*x)

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: A.chebyshev_polynomial(3, 2)                                          # needs sage.schemes
            Traceback (most recent call last):
            ...
            ValueError: keyword 'kind' must have a value of either 'first' or 'second'

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: A.chebyshev_polynomial(-4, 'second')
            Traceback (most recent call last):
            ...
            ValueError: first parameter 'n' must be a nonnegative integer

        ::

            sage: A = AffineSpace(QQ, 2, 'x')
            sage: A.chebyshev_polynomial(2)
            Traceback (most recent call last):
            ...
            TypeError: affine space must be of dimension 1

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: A.chebyshev_polynomial(7, monic=True)                                 # needs sage.schemes
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to (x^7 - 7*x^5 + 14*x^3 - 7*x)

        ::

            sage: F.<t> = FunctionField(QQ)
            sage: A.<x> = AffineSpace(F, 1)
            sage: A.chebyshev_polynomial(4, monic=True)                                 # needs sage.schemes
            Dynamical System of Affine Space of dimension 1
            over Rational function field in t over Rational Field
              Defn: Defined on coordinates by sending (x) to (x^4 + (-4)*x^2 + 2)
        """
    def origin(self):
        """
        Return the rational point at the origin of this affine space.

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: A.origin()
            (0, 0, 0)
            sage: _ == A(0,0,0)
            True
        """

class AffineSpace_field(AffineSpace_generic):
    def points_of_bounded_height(self, **kwds) -> Generator[Incomplete]:
        """
        Return an iterator of the points in this affine space of
        absolute height of at most the given bound.

        Bound check  is strict for the rational field.
        Requires this space to be affine space over a number field. Uses the
        Doyle-Krumm algorithm 4 (algorithm 5 for imaginary quadratic) for
        computing algebraic numbers up to a given height [DK2013]_.

        The algorithm requires floating point arithmetic, so the user is
        allowed to specify the precision for such calculations.
        Additionally, due to floating point issues, points
        slightly larger than the bound may be returned. This can be controlled
        by lowering the tolerance.

        INPUT: keyword arguments:

        - ``bound`` -- a real number

        - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm algorithm-4

        - ``precision`` -- the precision to use for computing the elements of bounded height of number fields

        OUTPUT: an iterator of points in self

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: list(A.points_of_bounded_height(bound=3))
            [(0, 0), (1, 0), (-1, 0), (1/2, 0), (-1/2, 0), (2, 0), (-2, 0), (0, 1),
             (1, 1), (-1, 1), (1/2, 1), (-1/2, 1), (2, 1), (-2, 1), (0, -1), (1, -1),
             (-1, -1), (1/2, -1), (-1/2, -1), (2, -1), (-2, -1), (0, 1/2), (1, 1/2),
             (-1, 1/2), (1/2, 1/2), (-1/2, 1/2), (2, 1/2), (-2, 1/2), (0, -1/2), (1, -1/2),
             (-1, -1/2), (1/2, -1/2), (-1/2, -1/2), (2, -1/2), (-2, -1/2), (0, 2), (1, 2),
             (-1, 2), (1/2, 2), (-1/2, 2), (2, 2), (-2, 2), (0, -2), (1, -2), (-1, -2),
             (1/2, -2), (-1/2, -2), (2, -2), (-2, -2)]

        ::

            sage: u = QQ['u'].0
            sage: A.<x,y> = AffineSpace(NumberField(u^2 - 2, 'v'), 2)                   # needs sage.rings.number_field
            sage: len(list(A.points_of_bounded_height(bound=2, tolerance=0.1)))         # needs sage.rings.number_field
            529
        """
    def weil_restriction(self):
        """
        Compute the Weil restriction of this affine space over some extension
        field.

        If the field is a finite field, then this computes
        the Weil restriction to the prime subfield.

        OUTPUT: affine space of dimension ``d * self.dimension_relative()``
        over the base field of ``self.base_ring()``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^5 - 2)
            sage: AK.<x,y> = AffineSpace(K, 2)
            sage: AK.weil_restriction()
            Affine Space of dimension 10 over Rational Field
            sage: R.<x> = K[]
            sage: L.<v> = K.extension(x^2 + 1)
            sage: AL.<x,y> = AffineSpace(L, 2)
            sage: AL.weil_restriction()
            Affine Space of dimension 4 over Number Field in w
             with defining polynomial x^5 - 2
        """
    def curve(self, F):
        """
        Return a curve defined by ``F`` in this affine space.

        INPUT:

        - ``F`` -- a polynomial, or a list or tuple of polynomials in
          the coordinate ring of this affine space

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: A.curve([y - x^4, z - y^5])                                           # needs sage.schemes
            Affine Curve over Rational Field defined by -x^4 + y, -y^5 + z
        """
    def line_through(self, p, q):
        """
        Return the line through ``p`` and ``q``.

        INPUT:

        - ``p``, ``q`` -- distinct rational points of the affine space

        EXAMPLES::

            sage: # needs sage.libs.singular sage.schemes
            sage: A3.<x,y,z> = AffineSpace(3, QQ)
            sage: p1 = A3(1, 2, 3)
            sage: p2 = A3(4, 5, 6)
            sage: L = A3.line_through(p1, p2); L
            Affine Curve over Rational Field defined by -1/6*x + 1/6*y - 1/6,
              -1/6*x + 1/6*z - 1/3, -1/6*y + 1/6*z - 1/6, -1/6*x + 1/3*y - 1/6*z
            sage: L(p1)
            (1, 2, 3)
            sage: L(p2)
            (4, 5, 6)
            sage: A3.line_through(p1, p1)
            Traceback (most recent call last):
            ...
            ValueError: not distinct points
        """
    def translation(self, p, q=None):
        """
        Return the automorphism of the affine space translating ``p`` to the origin.

        If ``q`` is given, the automorphism translates ``p`` to ``q``.

        INPUT:

        - ``p`` -- a rational point

        - ``q`` -- (default: ``None``) a rational point

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: p = A(1,2,3)
            sage: q = A(4,5,6)
            sage: A.translation(p, q)
            Scheme endomorphism of Affine Space of dimension 3 over Rational Field
              Defn: Defined on coordinates by sending (x, y, z) to
                    (x + 3, y + 3, z + 3)
            sage: phi = A.translation(p)
            sage: psi = A.translation(A.origin(), q)
            sage: psi * phi
            Scheme endomorphism of Affine Space of dimension 3 over Rational Field
              Defn: Defined on coordinates by sending (x, y, z) to
                    (x + 3, y + 3, z + 3)
            sage: psi * phi == A.translation(p, q)
            True
        """

class AffineSpace_finite_field(AffineSpace_field): ...
