from sage.arith.misc import binomial as binomial, gcd as gcd
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.categories.number_fields import NumberFields as NumberFields
from sage.categories.rings import Rings as Rings
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.permutation import Permutation as Permutation
from sage.combinat.subset import Subsets as Subsets
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ, RationalField as RationalField
from sage.schemes.generic.ambient_space import AmbientSpace as AmbientSpace
from sage.schemes.projective.projective_homset import SchemeHomset_points_projective_field as SchemeHomset_points_projective_field, SchemeHomset_points_projective_ring as SchemeHomset_points_projective_ring, SchemeHomset_polynomial_projective_space as SchemeHomset_polynomial_projective_space
from sage.schemes.projective.projective_morphism import SchemeMorphism_polynomial_projective_space as SchemeMorphism_polynomial_projective_space, SchemeMorphism_polynomial_projective_space_field as SchemeMorphism_polynomial_projective_space_field, SchemeMorphism_polynomial_projective_space_finite_field as SchemeMorphism_polynomial_projective_space_finite_field
from sage.schemes.projective.projective_point import SchemeMorphism_point_projective_field as SchemeMorphism_point_projective_field, SchemeMorphism_point_projective_finite_field as SchemeMorphism_point_projective_finite_field, SchemeMorphism_point_projective_ring as SchemeMorphism_point_projective_ring
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_ProjectiveSpace(x):
    """
    Return ``True`` if ``x`` is a projective space.

    In other words, if ``x`` is an ambient space `\\mathbb{P}^n_R`,
    where `R` is a ring and `n\\geq 0` is an integer.

    EXAMPLES::

        sage: from sage.schemes.projective.projective_space import is_ProjectiveSpace
        sage: is_ProjectiveSpace(ProjectiveSpace(5, names='x'))
        doctest:warning...
        DeprecationWarning: The function is_ProjectiveSpace is deprecated; use 'isinstance(..., ProjectiveSpace_ring)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: is_ProjectiveSpace(ProjectiveSpace(5, GF(9, 'alpha'), names='x'))         # needs sage.rings.finite_rings
        True
        sage: is_ProjectiveSpace(Spec(ZZ))
        False
    """
def ProjectiveSpace(n, R=None, names=None):
    """
    Return projective space of dimension ``n`` over the ring ``R``.

    EXAMPLES: The dimension and ring can be given in either order.

    ::

        sage: ProjectiveSpace(3, QQ)
        Projective Space of dimension 3 over Rational Field
        sage: ProjectiveSpace(5, QQ)
        Projective Space of dimension 5 over Rational Field
        sage: P = ProjectiveSpace(2, QQ, names='XYZ'); P
        Projective Space of dimension 2 over Rational Field
        sage: P.coordinate_ring()
        Multivariate Polynomial Ring in X, Y, Z over Rational Field

    The divide operator does base extension.

    ::

        sage: ProjectiveSpace(5)/GF(17)
        Projective Space of dimension 5 over Finite Field of size 17

    The default base ring is `\\ZZ`.

    ::

        sage: ProjectiveSpace(5)
        Projective Space of dimension 5 over Integer Ring

    There is also a projective space associated each polynomial ring.

    ::

        sage: R = GF(7)['x,y,z']
        sage: P = ProjectiveSpace(R); P
        Projective Space of dimension 2 over Finite Field of size 7
        sage: P.coordinate_ring()
        Multivariate Polynomial Ring in x, y, z over Finite Field of size 7
        sage: P.coordinate_ring() is R
        True

    ::

        sage: ProjectiveSpace(3, Zp(5), 'y')                                            # needs sage.rings.padics
        Projective Space of dimension 3 over 5-adic Ring with capped relative precision 20

    ::

        sage: ProjectiveSpace(2, QQ, 'x,y,z')
        Projective Space of dimension 2 over Rational Field

    ::

        sage: PS.<x,y> = ProjectiveSpace(1, CC); PS                                     # needs sage.rings.real_mpfr
        Projective Space of dimension 1 over Complex Field with 53 bits of precision

    ::

        sage: R.<x,y,z> = QQ[]
        sage: ProjectiveSpace(R).variable_names()
        ('x', 'y', 'z')

    Projective spaces are not cached, i.e., there can be several with
    the same base ring and dimension (to facilitate gluing
    constructions).

    ::

        sage: R.<x> = QQ[]
        sage: ProjectiveSpace(R)
        Projective Space of dimension 0 over Rational Field

    TESTS::

        sage: R.<x,y> = QQ[]
        sage: P.<z,w> = ProjectiveSpace(R)
        Traceback (most recent call last):
        ...
        NameError: variable names passed to ProjectiveSpace conflict with names in ring

    ::

        sage: R.<x,y> = QQ[]
        sage: P.<x,y> = ProjectiveSpace(R)
        sage: P.gens() == R.gens()
        True
    """

class ProjectiveSpace_ring(UniqueRepresentation, AmbientSpace):
    """
    Projective space of dimension `n` over the ring
    `R`.

    EXAMPLES::

        sage: X.<x,y,z,w> = ProjectiveSpace(3, QQ)
        sage: X.base_scheme()
        Spectrum of Rational Field
        sage: X.base_ring()
        Rational Field
        sage: X.structure_morphism()
        Scheme morphism:
          From: Projective Space of dimension 3 over Rational Field
          To:   Spectrum of Rational Field
          Defn: Structure map
        sage: X.coordinate_ring()
        Multivariate Polynomial Ring in x, y, z, w over Rational Field

    Loading and saving::

        sage: loads(X.dumps()) == X
        True
        sage: P = ProjectiveSpace(ZZ, 1, 'x')
        sage: loads(P.dumps()) is P
        True

    Equality and hashing::

        sage: ProjectiveSpace(QQ, 3, 'a') == ProjectiveSpace(ZZ, 3, 'a')
        False
        sage: ProjectiveSpace(ZZ, 1, 'a') == ProjectiveSpace(ZZ, 0, 'a')
        False
        sage: ProjectiveSpace(ZZ, 2, 'a') == AffineSpace(ZZ, 2, 'a')
        False

        sage: ProjectiveSpace(QQ, 3, 'a') != ProjectiveSpace(ZZ, 3, 'a')
        True
        sage: ProjectiveSpace(ZZ, 1, 'a') != ProjectiveSpace(ZZ, 0, 'a')
        True
        sage: ProjectiveSpace(ZZ, 2, 'a') != AffineSpace(ZZ, 2, 'a')
        True

        sage: hash(ProjectiveSpace(QQ, 3, 'a')) == hash(ProjectiveSpace(ZZ, 3, 'a'))
        False
        sage: hash(ProjectiveSpace(ZZ, 1, 'a')) == hash(ProjectiveSpace(ZZ, 0, 'a'))
        False
        sage: hash(ProjectiveSpace(ZZ, 2, 'a')) == hash(AffineSpace(ZZ, 2, 'a'))
        False
    """
    @staticmethod
    def __classcall__(cls, n, R=..., names=None):
        """
        EXAMPLES::

            sage: ProjectiveSpace(QQ, 2, names='XYZ') is ProjectiveSpace(QQ, 2, names='XYZ')
            True
        """
    def __init__(self, n, R=..., names=None) -> None:
        """
        Initialization function.

        EXAMPLES::

            sage: ProjectiveSpace(3, Zp(5), 'y')                                        # needs sage.rings.padics
            Projective Space of dimension 3 over 5-adic Ring with capped relative precision 20
        """
    def ngens(self):
        """
        Return the number of generators of this projective space.

        This is the number of variables in the coordinate ring of ``self``.

        EXAMPLES::

            sage: ProjectiveSpace(3, QQ).ngens()
            4
            sage: ProjectiveSpace(7, ZZ).ngens()
            8
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring of this scheme.

        EXAMPLES::

            sage: ProjectiveSpace(3, GF(19^2,'alpha'), 'abcd').coordinate_ring()        # needs sage.rings.finite_rings
            Multivariate Polynomial Ring in a, b, c, d over Finite Field in alpha of size 19^2

        ::

            sage: ProjectiveSpace(3).coordinate_ring()
            Multivariate Polynomial Ring in x0, x1, x2, x3 over Integer Ring

        ::

            sage: ProjectiveSpace(2, QQ, ['alpha', 'beta', 'gamma']).coordinate_ring()
            Multivariate Polynomial Ring in alpha, beta, gamma over Rational Field
        """
    def __pow__(self, m):
        """
        Return the Cartesian power of this space.

        INPUT:

        - ``m`` -- integer

        OUTPUT: product of projective spaces

        EXAMPLES::

            sage: P = ProjectiveSpace(1, QQ, 'x')
            sage: P3 = P^3; P3
            Product of projective spaces P^1 x P^1 x P^1 over Rational Field
            sage: P3.variable_names()
            ('x0', 'x1', 'x2', 'x3', 'x4', 'x5')

        As you see, custom variable names are not preserved by power operator,
        since there is no natural way to make new ones in general.
        """
    def __mul__(self, right):
        """
        Create the product of projective spaces.

        INPUT:

        - ``right`` -- a projective space, product of projective spaces, or subscheme

        OUTPUT: a product of projective spaces or subscheme

        EXAMPLES::

            sage: P1 = ProjectiveSpace(QQ, 1, 'x')
            sage: P2 = ProjectiveSpace(QQ, 2, 'y')
            sage: P1*P2
            Product of projective spaces P^1 x P^2 over Rational Field

            ::

            sage: S.<t,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.<a,b> = ProjectiveSpace(QQ, 1)
            sage: T*S
            Product of projective spaces P^1 x P^3 x P^2 over Rational Field

        ::

            sage: S = ProjectiveSpace(ZZ, 2, 't')
            sage: T = ProjectiveSpace(ZZ, 3, 'x')
            sage: T.inject_variables()
            Defining x0, x1, x2, x3
            sage: X = T.subscheme([x0*x2 - x1*x3])
            sage: S*X
            Closed subscheme of Product of projective spaces P^2 x P^3 over Integer Ring defined by:
              x0*x2 - x1*x3

        ::

            sage: S = ProjectiveSpace(QQ, 3, 'x')
            sage: T = AffineSpace(2, QQ, 'y')
            sage: S*T
            Traceback (most recent call last):
            ...
            TypeError: Affine Space of dimension 2 over Rational Field must be a
            projective space, product of projective spaces, or subscheme
        """
    def point(self, v, check: bool = True):
        """
        Create a point on this projective space.

        INPUT:

        - ``v`` -- anything that defines a point

        - ``check`` -- boolean (default: ``True``); whether
          to check the defining data for consistency

        OUTPUT: a point of this projective space

        EXAMPLES::

            sage: P2 = ProjectiveSpace(QQ, 2)
            sage: P2.point([4,5])
            (4 : 5 : 1)

        ::

            sage: P = ProjectiveSpace(QQ, 1)
            sage: P.point(infinity)
            (1 : 0)

        ::

            sage: P = ProjectiveSpace(QQ, 2)
            sage: P.point(infinity)
            Traceback (most recent call last):
            ...
            ValueError: +Infinity not well defined in dimension > 1

        ::

            sage: P = ProjectiveSpace(ZZ, 2)
            sage: P.point([infinity])
            Traceback (most recent call last):
             ...
            ValueError: [+Infinity] not well defined in dimension > 1
        """
    def change_ring(self, R):
        """
        Return a projective space over ring ``R``.

        INPUT:

        - ``R`` -- commutative ring or morphism

        OUTPUT: projective space over ``R``

        .. NOTE::

            There is no need to have any relation between ``R`` and the base ring
            of this space, if you want to have such a relation, use
            ``self.base_extend(R)`` instead.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: PQ = P.change_ring(QQ); PQ
            Projective Space of dimension 2 over Rational Field
            sage: PQ.change_ring(GF(5))
            Projective Space of dimension 2 over Finite Field of size 5

        ::

            sage: K.<w> = QuadraticField(2)                                             # needs sage.rings.number_field
            sage: P = ProjectiveSpace(K, 2, 't')                                        # needs sage.rings.number_field
            sage: P.change_ring(K.embeddings(QQbar)[0])                                 # needs sage.rings.number_field
            Projective Space of dimension 2 over Algebraic Field
        """
    def is_projective(self):
        """
        Return that this ambient space is projective `n`-space.

        EXAMPLES::

            sage: ProjectiveSpace(3,QQ).is_projective()
            True
        """
    def subscheme(self, X):
        '''
        Return the closed subscheme defined by ``X``.

        INPUT:

        - ``X`` -- list or tuple of equations

        EXAMPLES::

            sage: A.<x,y,z> = ProjectiveSpace(2, QQ)
            sage: X = A.subscheme([x*z^2, y^2*z, x*y^2]); X
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x*z^2,
              y^2*z,
              x*y^2
            sage: X.defining_polynomials ()
            (x*z^2, y^2*z, x*y^2)
            sage: I = X.defining_ideal(); I
            Ideal (x*z^2, y^2*z, x*y^2) of Multivariate Polynomial Ring in x, y, z
             over Rational Field
            sage: I.groebner_basis()                                                    # needs sage.libs.singular
            [x*y^2, y^2*z,  x*z^2]
            sage: X.dimension()                                                         # needs sage.libs.singular
            0
            sage: X.base_ring()
            Rational Field
            sage: X.base_scheme()
            Spectrum of Rational Field
            sage: X.structure_morphism()
            Scheme morphism:
              From: Closed subscheme of Projective Space of dimension 2
                    over Rational Field defined by: x*z^2, y^2*z, x*y^2
              To:   Spectrum of Rational Field
              Defn: Structure map

        TESTS::

            sage: TestSuite(X).run(skip=["_test_an_element", "_test_elements",            ....: "_test_elements_eq", "_test_some_elements", "_test_elements_eq_reflexive",            ....: "_test_elements_eq_symmetric", "_test_elements_eq_transitive",            ....: "_test_elements_neq"])
        '''
    def points_of_bounded_height(self, **kwds):
        """
        Return an iterator of the points in ``self`` of absolute multiplicative
        height of at most the given bound.

        ALGORITHM:

        This is an implementation of Algorithm 6 in [Krumm2016]_.

        INPUT: keyword arguments:

        - ``bound`` -- a real number

        - ``precision`` -- (default: 53) a positive integer

        OUTPUT: an iterator of points of bounded height

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: sorted(list(P.points_of_bounded_height(bound=2)))
            [(-2 : 1), (-1 : 1), (-1/2 : 1), (0 : 1),
             (1/2 : 1), (1 : 0), (1 : 1), (2 : 1)]

        ::

            sage: u = QQ['u'].0
            sage: P.<x,y,z> = ProjectiveSpace(NumberField(u^2 - 2, 'v'), 2)             # needs sage.rings.number_field
            sage: len(list(P.points_of_bounded_height(bound=2)))                        # needs sage.rings.number_field
            265

        ::

            sage: # needs sage.rings.number_field
            sage: CF.<a> = CyclotomicField(3)
            sage: R.<x> = CF[]
            sage: L.<l> = CF.extension(x^3 + 2)
            sage: Q.<x,y> = ProjectiveSpace(L, 1)
            sage: sorted(list(Q.points_of_bounded_height(bound=1)))
            [(0 : 1), (1 : 0), (a + 1 : 1), (a : 1),
             (-1 : 1), (-a - 1 : 1), (-a : 1), (1 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: F.<a> = NumberField(x^4 - 8*x^2 + 3)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2)
            sage: all(exp(p.global_height()) <= 1                                       # needs sage.symbolic
            ....:     for p in P.points_of_bounded_height(bound=1))
            True

        ::

            sage: K.<a> = CyclotomicField(3)                                            # needs sage.rings.number_field
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)                                     # needs sage.rings.number_field
            sage: len(list(P.points_of_bounded_height(bound=1)))                        # needs sage.rings.number_field
            57

        ::

            sage: u = QQ['u'].0
            sage: K.<k> = NumberField(u^2 - 2)                                          # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(K, 1)                                       # needs sage.rings.number_field
            sage: len(list(P.points_of_bounded_height(bound=2)))                        # needs sage.rings.number_field
            24

        ::

            sage: R.<x> = QQ[]
            sage: K.<k> = NumberField(x^4 - 8*x^2 + 3)                                  # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(K, 1)                                       # needs sage.rings.number_field
            sage: len(list(P.points_of_bounded_height(bound=2)))                        # needs sage.rings.number_field
            108

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<v> = NumberField(x^5 + x^3 + 1)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: L = P.points_of_bounded_height(bound=1.2)
            sage: len(list(L))
            109

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: sorted(list(P.points_of_bounded_height(bound=2)))
            [(-v - 2 : 1), (-v - 1 : 1), (-2 : 1), (-1/2*v - 1 : 1), (-v : 1), (-1 : 1),
             (-1/2*v : 1), (v - 2 : 1), (-1/2 : 1), (-v + 1 : 1), (1/2*v - 1 : 1), (0 : 1),
             (-1/2*v + 1 : 1), (v - 1 : 1), (1/2 : 1), (-v + 2 : 1), (1/2*v : 1), (1 : 0),
             (1 : 1), (v : 1), (1/2*v + 1 : 1), (2 : 1), (v + 1 : 1), (v + 2 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(3*x^2 + 1)
            sage: P.<z,w> = ProjectiveSpace(K, 1)
            sage: sorted(list(P.points_of_bounded_height(bound=1)))
            [(-1 : 1), (-3/2*a - 1/2 : 1), (3/2*a - 1/2 : 1), (0 : 1),
             (-3/2*a + 1/2 : 1), (3/2*a + 1/2 : 1), (1 : 0), (1 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(3*x^2 + 1)
            sage: O = K.maximal_order()
            sage: P.<z,w> = ProjectiveSpace(O, 1)
            sage: len(sorted(list(P.points_of_bounded_height(bound=2))))
            44

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 7)
            sage: O = K.maximal_order()
            sage: P.<z,w> = ProjectiveSpace(O, 1)
            sage: len(sorted(list(P.points_of_bounded_height(bound=2))))
            28

        ::

            sage: P.<w,z> = ProjectiveSpace(ZZ, 1)
            sage: sorted(list(P.points_of_bounded_height(bound=2)))
            [(-2 : -1), (-2 : 1), (-1 : -2), (-1 : -1),
             (-1 : 0), (-1 : 1), (-1 : 2), (0 : -1)]

        ::

            sage: R.<x> = QQ[]
            sage: P.<z,w> = ProjectiveSpace(R, 1)
            sage: P.points_of_bounded_height(bound=2)
            Traceback (most recent call last):
            ...
            NotImplementedError: self must be a projective space over
            a number field or a ring of integers

        ::

            sage: # needs sage.rings.number_field
            sage: K.<i> = NumberField(x^2 + 1)
            sage: PK.<t> = K[]
            sage: L.<a> = K.extension(t^4  - i)
            sage: P.<z,w> = ProjectiveSpace(L, 1)
            sage: sorted(list(P.points_of_bounded_height(bound=1)))
            [(0 : 1), (1 : 0), (a : 1), (a^2 : 1), (a^3 : 1), (i : 1),
             (i*a : 1), (i*a^2 : 1), (i*a^3 : 1), (-1 : 1), (-a : 1), (-a^2 : 1),
             (-a^3 : 1), (-i : 1), (-i*a : 1), (-i*a^2 : 1), (-i*a^3 : 1), (1 : 1)]
        """
    def affine_patch(self, i, AA=None):
        '''
        Return the `i`-th affine patch of this projective space.

        This is an ambient affine space `\\mathbb{A}^n_R,` where
        `R` is the base ring of ``self``, whose "projective embedding"
        map is `1` in the `i`-th factor.

        INPUT:

        - ``i`` -- integer between 0 and dimension of ``self``, inclusive

        - ``AA`` -- (default: ``None``) ambient affine space, this is constructed
          if it is not given

        OUTPUT: an ambient affine space with fixed projective_embedding map

        EXAMPLES::

            sage: PP = ProjectiveSpace(5) / QQ
            sage: AA = PP.affine_patch(2)
            sage: AA
            Affine Space of dimension 5 over Rational Field
            sage: AA.projective_embedding()
            Scheme morphism:
              From: Affine Space of dimension 5 over Rational Field
              To:   Projective Space of dimension 5 over Rational Field
              Defn: Defined on coordinates by sending (x0, x1, x3, x4, x5) to
                    (x0 : x1 : 1 : x3 : x4 : x5)
            sage: AA.projective_embedding(0)
            Scheme morphism:
              From: Affine Space of dimension 5 over Rational Field
              To:   Projective Space of dimension 5 over Rational Field
              Defn: Defined on coordinates by sending (x0, x1, x3, x4, x5) to
                    (1 : x0 : x1 : x3 : x4 : x5)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P.affine_patch(0).projective_embedding(0).codomain() == P
            True
        '''
    def Lattes_map(self, E, m):
        """
        Given an elliptic curve ``E`` and an integer ``m`` return
        the Lattes map associated to multiplication by `m`.

        In other words, the rational map on the quotient
        `E/\\{\\pm 1\\} \\cong \\mathbb{P}^1` associated to `[m]:E \\to E`.

        INPUT:

        - ``E`` -- an elliptic curve

        - ``m`` -- integer

        OUTPUT: a dynamical system on this projective space

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: E = EllipticCurve(QQ,[-1, 0])                                         # needs sage.schemes
            sage: P.Lattes_map(E, 2)                                                    # needs sage.schemes
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (1/4*x^4 + 1/2*x^2*y^2 + 1/4*y^4 : x^3*y - x*y^3)

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(GF(37), 1)
            sage: E = EllipticCurve([1, 1])                                             # needs sage.rings.finite_rings sage.schemes
            sage: f = P.Lattes_map(E, 2); f                                             # needs sage.rings.finite_rings sage.schemes
            Dynamical System of Projective Space of dimension 1 over Finite Field of size 37
              Defn: Defined on coordinates by sending (x : y) to
                    (-9*x^4 + 18*x^2*y^2 - 2*x*y^3 - 9*y^4 : x^3*y + x*y^3 + y^4)
        """
    def cartesian_product(self, other):
        """
        Return the Cartesian product of this projective space and
        ``other``.

        INPUT:

        - ``other`` -- a projective space with the same base ring as this space

        OUTPUT: a Cartesian product of projective spaces

        EXAMPLES::

            sage: P1 = ProjectiveSpace(QQ, 1, 'x')
            sage: P2 = ProjectiveSpace(QQ, 2, 'y')
            sage: PP = P1.cartesian_product(P2); PP
            Product of projective spaces P^1 x P^2 over Rational Field
            sage: PP.gens()
            (x0, x1, y0, y1, y2)
        """
    def chebyshev_polynomial(self, n, kind: str = 'first', monic: bool = False):
        """
        Generates an endomorphism of this projective line by a Chebyshev polynomial.

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

        OUTPUT: :class:`DynamicalSystem_projective`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P.chebyshev_polynomial(5, 'first')                                    # needs sage.symbolic
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (16*x^5 - 20*x^3*y^2 + 5*x*y^4 : y^5)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P.chebyshev_polynomial(3, 'second')                                   # needs sage.symbolic
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (8*x^3 - 4*x*y^2 : y^3)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P.chebyshev_polynomial(3, 2)                                          # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: keyword 'kind' must have a value of either 'first' or 'second'

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P.chebyshev_polynomial(-4, 'second')
            Traceback (most recent call last):
            ...
            ValueError: first parameter 'n' must be a nonnegative integer

        ::

            sage: P = ProjectiveSpace(QQ, 2, 'x')
            sage: P.chebyshev_polynomial(2)
            Traceback (most recent call last):
            ...
            TypeError: projective space must be of dimension 1

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P.chebyshev_polynomial(3, monic=True)                                 # needs sage.symbolic
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^3 - 3*x*y^2 : y^3)

        ::

            sage: F.<t> = FunctionField(QQ)
            sage: P.<y,z> = ProjectiveSpace(F, 1)
            sage: P.chebyshev_polynomial(4, monic=True)                                 # needs sage.symbolic
            Dynamical System of Projective Space of dimension 1
             over Rational function field in t over Rational Field
              Defn: Defined on coordinates by sending (y : z) to
                    (y^4 + (-4)*y^2*z^2 + 2*z^4 : z^4)
        """
    def veronese_embedding(self, d, CS=None, order: str = 'lex'):
        """
        Return the degree ``d`` Veronese embedding from this projective space.

        INPUT:

        - ``d`` -- positive integer

        - ``CS`` -- (default: ``None``) a projective ambient space to embed
          into. If this projective space has dimension `N`, the dimension of
          ``CS`` must be `\\binom{N + d}{d} - 1`. This is constructed if not
          specified.

        - ``order`` -- string (default: ``'lex'``); a monomial order to use to
          arrange the monomials defining the embedding. The monomials will be
          arranged from greatest to least with respect to this order.

        OUTPUT: a scheme morphism from this projective space to ``CS``

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: vd = P.veronese_embedding(4, order='invlex')                          # needs sage.combinat
            sage: vd                                                                    # needs sage.combinat
            Scheme morphism:
              From: Projective Space of dimension 1 over Rational Field
              To:   Projective Space of dimension 4 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (y^4 : x*y^3 : x^2*y^2 : x^3*y : x^4)

        Veronese surface::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: Q.<q,r,s,t,u,v> = ProjectiveSpace(QQ, 5)
            sage: vd = P.veronese_embedding(2, Q)                                       # needs sage.combinat
            sage: vd                                                                    # needs sage.combinat
            Scheme morphism:
              From: Projective Space of dimension 2 over Rational Field
              To:   Projective Space of dimension 5 over Rational Field
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^2 : x*y : x*z : y^2 : y*z : z^2)
            sage: vd(P.subscheme([]))                                                   # needs sage.combinat sage.libs.singular
            Closed subscheme of Projective Space of dimension 5 over Rational Field
             defined by:
              -u^2 + t*v,
              -s*u + r*v,
              -s*t + r*u,
              -s^2 + q*v,
              -r*s + q*u,
              -r^2 + q*t
        """
    def point_transformation_matrix(self, points_source, points_target, normalize: bool = True):
        """
        Returns a unique element of PGL that transforms one set of points to another.

        Given a projective space of dimension n and a set of n+2 source points and a set of n+2 target
        points in the same projective space, such that no n+1 points of each set are linearly dependent
        find the unique element of PGL that translates the source points to the target points.

        .. warning::
            over non-exact rings such as the ComplexField, the returned matrix could
            be very far from correct.

        INPUT:

        - ``points_source`` -- points in source projective space

        - ``points_target`` -- points in target projective space

        - ``normalize`` -- boolean (default: ``True``); if the returned matrix
          should be normalized. Only works over exact rings. If the base ring
          is a field, the matrix is normalized so that the last nonzero entry
          in the last row is 1. If the base ring is a ring, then the matrix is
          normalized so that the entries are elements of the base ring.

        OUTPUT: transformation matrix - element of PGL

        ALGORITHM:

        See [Hutz2007]_, Proposition 2.16 for details.

        EXAMPLES::

            sage: P1.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: points_source = [P1([1, 4, 1]), P1([1, 2, 2]), P1([3, 5, 1]), P1([1, -1, 1])]
            sage: points_target = [P1([5, -2, 7]), P1([3, -2, 3]), P1([6, -5, 9]), P1([3, 6, 7])]
            sage: m = P1.point_transformation_matrix(points_source, points_target); m   # needs sage.modules
            [ -13/59 -128/59  -25/59]
            [538/177    8/59  26/177]
            [ -45/59 -196/59       1]
            sage: [m*points_source[i] == points_target[i] for i in range(4)]            # needs sage.modules
            [True, True, True, True]

        ::

            sage: P.<a,b> = ProjectiveSpace(GF(13),  1)
            sage: points_source = [P([-6, 7]), P([1, 4]), P([3, 2])]
            sage: points_target = [P([-1, 2]), P([0, 2]), P([-1, 6])]
            sage: P.point_transformation_matrix(points_source, points_target)           # needs sage.modules
            [10  4]
            [10  1]

        ::

            sage: P.<a,b> = ProjectiveSpace(QQ, 1)
            sage: points_source = [P([-6, -4]), P([1, 4]), P([3, 2])]
            sage: points_target = [P([-1, 2]), P([0, 2]), P([-7, -3])]
            sage: P.point_transformation_matrix(points_source, points_target)           # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: source points not independent

        ::

            sage: R.<t> = FunctionField(QQ)
            sage: P.<a,b> = ProjectiveSpace(R, 1)
            sage: points_source = [P([-6*t, 7]), P([1, 4]), P([3, 2])]
            sage: points_target = [P([-1, 2*t]), P([0, 2]), P([-1, 6])]
            sage: P.point_transformation_matrix(points_source, points_target)           # needs sage.modules
            [             (1/3*t + 7/12)/(t^2 - 53/24*t)       (-1/12*t - 7/48)/(t^2 - 53/24*t)]
            [(-2/3*t^2 - 7/36*t - 35/12)/(t^2 - 53/24*t)                                      1]

        ::

            sage: P1.<a,b,c> = ProjectiveSpace(RR, 2)
            sage: points_source = [P1([1, 4, 1]), P1([1, 2, 2]), P1([3, 5, 1]), P1([1, -1, 1])]
            sage: points_target = [P1([5, -2, 7]), P1([3, -2, 3]), P1([6, -5, 9]), P1([3, 6, 7])]
            sage: P1.point_transformation_matrix(points_source,        # abs tol 1e-13  # needs sage.modules
            ....:                                points_target)
            [-0.0619047619047597  -0.609523809523810  -0.119047619047621]
            [  0.853968253968253  0.0380952380952380  0.0412698412698421]
            [ -0.214285714285712  -0.933333333333333   0.280952380952379]

        ::

            sage: P1.<a,b,c> = ProjectiveSpace(ZZ, 2)
            sage: points_source = [P1([1, 4, 1]), P1([1, 2, 2]), P1([3, 5, 1]), P1([1, -1, 1])]
            sage: points_target = [P1([5, -2, 7]), P1([3, -2, 3]), P1([6, -5, 9]), P1([3, 6, 7])]
            sage: P1.point_transformation_matrix(points_source, points_target)          # needs sage.modules
            [ -39 -384  -75]
            [ 538   24   26]
            [-135 -588  177]

        ::

            sage: P1.<a,b,c> = ProjectiveSpace(ZZ, 2)
            sage: points_source = [P1([1, 4, 1]), P1([1, 2, 2]), P1([3, 5, 1]), P1([1, -1, 1])]
            sage: points_target = [P1([5, -2, 7]), P1([3, -2, 3]), P1([6, -5, 9]), P1([3, 6, 7])]
            sage: P1.point_transformation_matrix(points_source, points_target,          # needs sage.modules
            ....:                                normalize=False)
            [-13/30 -64/15   -5/6]
            [269/45   4/15  13/45]
            [  -3/2 -98/15  59/30]

        ::

            sage: R.<t> = ZZ[]
            sage: P.<a,b> = ProjectiveSpace(R, 1)
            sage: points_source = [P([-6*t, 7]), P([1, 4]), P([3, 2])]
            sage: points_target = [P([-1, 2*t]), P([0, 2]), P([-1, 6])]
            sage: P.point_transformation_matrix(points_source, points_target)           # needs sage.modules
            [         -48*t - 84           12*t + 21]
            [96*t^2 + 28*t + 420    -144*t^2 + 318*t]

        TESTS::

            sage: P.<a,b> = ProjectiveSpace(QQ, 1)
            sage: points_source = [P([-6, -1]), P([1, 4]), P([3, 2])]
            sage: points_target = [P([-1, 2]), P([0, 2]), P([-2, 4])]
            sage: P.point_transformation_matrix(points_source, points_target)           # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: target points not independent

        ::

            sage: P.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: points_source = [P([1, 4, 1]), P([2, -7, 9]), P([3, 5, 1])]
            sage: points_target = [P([5, -2, 7]), P([3, -2, 3]), P([6, -5, 9]), P([6, -1, 1])]
            sage: P.point_transformation_matrix(points_source, points_target)
            Traceback (most recent call last):
            ...
            ValueError: incorrect number of points in source, need 4 points

        ::

            sage: P.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: points_source = [P([1, 4, 1]), P([2, -7, 9]), P([3, 5, 1]), P([1, -1, 1])]
            sage: points_target = [P([5, -2, 7]), P([3, -2, 3]), P([6, -5, 9]), P([6, -1, 1]), P([7, 8, -9])]
            sage: P.point_transformation_matrix(points_source, points_target)
            Traceback (most recent call last):
            ...
            ValueError: incorrect number of points in target, need 4 points

        ::

            sage: P.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: P1.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: points_source = [P([1, 4, 1]), P([2, -7, 9]), P([3, 5, 1]), P1([1, -1, 1])]
            sage: points_target=[P([5, -2, 7]), P([3, -2, 3]), P([6, -5, 9]), P([6, -1, 1])]
            sage: P.point_transformation_matrix(points_source, points_target)
            Traceback (most recent call last):
            ...
            ValueError: source points not in self

        ::

            sage: P.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: P1.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: points_source = [P([1, 4, 1]), P([2, -7, 9]), P([3, 5, 1]), P([1, -1, 1])]
            sage: points_target = [P([5, -2, 7]), P([3, -2, 3]), P([6, -5, 9]), P1([6, -1, 1])]
            sage: P.point_transformation_matrix(points_source, points_target)
            Traceback (most recent call last):
            ...
            ValueError: target points not in self

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: points_source = [P(1, 0, 0), P(0, 1, 0), P(0, 0, 1), P(1, -1, -1)]
            sage: points_target = [P(0, 1, 0), P(-2, 0, 1), P(0, 0, 1), P(1, -1, -1)]
            sage: P.point_transformation_matrix(points_source, points_target,           # needs sage.modules
            ....:                               normalize=True)
            [ 0 -2  0]
            [-2  0  0]
            [ 0  1  1]
        """
    def hyperplane_transformation_matrix(self, plane_1, plane_2):
        """
        Return a PGL element sending ``plane_1`` to ``plane_2``.

        ``plane_1`` and ``plane_2`` must be hyperplanes (subschemes of
        codimension 1, each defined by a single linear homogeneous equation).

        INPUT:

        - ``plane_1``, ``plane_2`` -- hyperplanes of this projective space

        OUTPUT: an element of PGL

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: plane1 = P.subscheme(x)
            sage: plane2 = P.subscheme(y)
            sage: m = P.hyperplane_transformation_matrix(plane1, plane2); m             # needs sage.modules
            [0 1]
            [1 0]
            sage: plane2(m*P((0,1)))                                                    # needs sage.modules
            (1 : 0)

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: plane1 = P.subscheme(x + 2*y + z)
            sage: plane2 = P.subscheme(2*x + y + z)
            sage: P.hyperplane_transformation_matrix(plane1, plane2)                    # needs sage.modules
            [1 0 0 0]
            [0 4 0 0]
            [0 0 2 0]
            [0 0 0 1]

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: plane1 = P.subscheme(x + y)
            sage: plane2 = P.subscheme(y)
            sage: P.hyperplane_transformation_matrix(plane1, plane2)                    # needs sage.modules
            [-1  0]
            [ 1  1]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = CyclotomicField(3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: plane1 = P.subscheme(x - 2*v*y + z)
            sage: plane2 = P.subscheme(x + v*y + v*z)
            sage: m = P.hyperplane_transformation_matrix(plane1, plane2); m             # needs sage.modules
            [   v    0    0]
            [   0 -2*v    0]
            [   0    0    1]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<k> = NumberField(x^2 + 1)
            sage: P.<x,y,z,w> = ProjectiveSpace(K, 3)
            sage: plane1 = P.subscheme(k*x + 2*k*y + z)
            sage: plane2 = P.subscheme(7*k*x + y + 9*z)
            sage: m = P.hyperplane_transformation_matrix(plane1, plane2); m             # needs sage.modules
            [   1    0    0    0]
            [   0 14*k    0    0]
            [   0    0  7/9    0]
            [   0    0    0    1]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = CyclotomicField(3)
            sage: R.<t> = K[]
            sage: F.<w> = K.extension(t^5 + 2)
            sage: G.<u> = F.absolute_field()
            sage: P.<x,y,z> = ProjectiveSpace(G, 2)
            sage: plane1 = P.subscheme(x - 2*u*y + z)
            sage: plane2 = P.subscheme(x + u*y + z)
            sage: m = P.hyperplane_transformation_matrix(plane1, plane2)                # needs sage.modules
            sage: plane2(m*P((2*u, 1, 0)))                                              # needs sage.modules
            (-u : 1 : 0)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(FiniteField(2), 2)
            sage: plane1 = P.subscheme(x + y + z)
            sage: plane2 = P.subscheme(z)
            sage: P.hyperplane_transformation_matrix(plane1, plane2)                    # needs sage.modules
            [1 0 0]
            [1 1 0]
            [1 1 1]

        ::

            sage: R.<t> = QQ[]
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: plane1 = P.subscheme(x + 9*t*y + z)
            sage: plane2 = P.subscheme(x + z)
            sage: P.hyperplane_transformation_matrix(plane1, plane2)                    # needs sage.modules
            [  1 9*t   0]
            [  1   0   0]
            [  0   0   1]

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: plane1 = P.subscheme(x^2)
            sage: plane2 = P.subscheme(y)
            sage: P.hyperplane_transformation_matrix(plane1, plane2)
            Traceback (most recent call last):
            ...
            ValueError: plane_1 must be defined by a single degree 1 equation
        """
    def is_linearly_independent(self, points, n=None):
        """
        Return whether the set of points is linearly independent.

        Alternatively, specify ``n`` to check if every subset of
        size ``n`` is linearly independent.

        INPUT:

        - ``points`` -- list of points in this projective space

        - ``n`` -- (optional) positive integer less than or equal to the length
          of ``points``. Specifies the size of the subsets to check for
          linear independence.

        OUTPUT: ``True`` if ``points`` is linearly independent, ``False`` otherwise

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: points = [P((1, 0, 1)), P((1, 2, 1)), P((1, 3, 4))]
            sage: P.is_linearly_independent(points)                                     # needs sage.modules
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: points = [P((1, 0, 1)), P((1, 2, 1)), P((1, 3, 4)), P((0, 0, 1))]
            sage: P.is_linearly_independent(points, 2)                                  # needs sage.modules
            True

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: points = [P((c, 0, 1)), P((0, c, 1)), P((1, 0, 4)), P((0, 0, 1))]
            sage: P.is_linearly_independent(points, 3)                                  # needs sage.modules
            False

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y,z> = ProjectiveSpace(FractionField(R), 2)
            sage: points = [P((c, 0, 1)), P((0, c, 1)), P((1, 3, 4)), P((0, 0, 1))]
            sage: P.is_linearly_independent(points, 3)                                  # needs sage.modules
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<k> = CyclotomicField(3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: points = [P((k, k^2, 1)), P((0, k, 1)), P((1, 0, 4)), P((0, 0, 1))]
            sage: P.is_linearly_independent(points, 3)                                  # needs sage.modules
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: points = [P((1, 0)), P((1, 1))]
            sage: P.is_linearly_independent(points)                                     # needs sage.modules
            True

        TESTS::

            sage: points = [P(1, 0), P(1, 1), P(2, 1)]
            sage: P.is_linearly_independent(points, 5)
            Traceback (most recent call last):
            ...
            ValueError: n must be a nonnegative integer not greater than the length of points
        """

class ProjectiveSpace_field(ProjectiveSpace_ring):
    def subscheme_from_Chow_form(self, Ch, dim):
        """
        Return the subscheme defined by the Chow equations associated to the Chow form ``Ch``.

        These equations define the subscheme set-theoretically, but only for smooth
        subschemes and hypersurfaces do they define the subscheme as a scheme.

        ALGORITHM:

        The Chow form is a polynomial in the Plucker coordinates. The Plucker coordinates
        are the bracket polynomials. We first re-write the Chow form in terms of the dual
        Plucker coordinates. Then we expand `Ch(span(p,L)` for a generic point `p` and a
        generic linear subspace `L`. The coefficients as polynomials in the coordinates
        of `p` are the equations defining the subscheme. [DalbecSturmfels].

        INPUT:

        - ``Ch`` -- a homogeneous polynomial

        - ``dim`` -- the dimension of the associated scheme

        OUTPUT: a projective subscheme

        EXAMPLES::

            sage: P = ProjectiveSpace(QQ, 4, 'z')
            sage: R.<x0,x1,x2,x3,x4> = PolynomialRing(QQ)
            sage: H = x1^2 + x2^2 + 5*x3*x4
            sage: P.subscheme_from_Chow_form(H, 3)                                      # needs sage.modules
            Closed subscheme of Projective Space of dimension 4 over Rational Field defined by:
              -5*z0*z1 + z2^2 + z3^2

        ::

            sage: P = ProjectiveSpace(QQ, 3, 'z')
            sage: R.<x0,x1,x2,x3,x4,x5> = PolynomialRing(QQ)
            sage: H = x1 - x2 - x3 + x5 + 2*x0
            sage: P.subscheme_from_Chow_form(H, 1)                                      # needs sage.modules
            Closed subscheme of Projective Space of dimension 3 over Rational Field
            defined by:
              -z1 + z3,
              z0 + z2 + z3,
              -z1 - 2*z3,
              -z0 - z1 + 2*z2

        ::

            sage: # needs sage.libs.singular
            sage: P.<x0,x1,x2,x3> = ProjectiveSpace(GF(7), 3)
            sage: X = P.subscheme([x3^2 + x1*x2, x2 - x0])
            sage: Ch = X.Chow_form(); Ch
            t0^2 - 2*t0*t3 + t3^2 - t2*t4 - t4*t5
            sage: Y = P.subscheme_from_Chow_form(Ch, 1); Y
            Closed subscheme of Projective Space of dimension 3
             over Finite Field of size 7 defined by:
              x1*x2 + x3^2,
              -x0*x2 + x2^2,
              -x0*x1 - x1*x2 - 2*x3^2,
              x0^2 - x0*x2,
              x0*x1 + x3^2,
              -2*x0*x3 + 2*x2*x3,
              2*x0*x3 - 2*x2*x3,
              x0^2 - 2*x0*x2 + x2^2
            sage: I = Y.defining_ideal()
            sage: I.saturation(I.ring().ideal(list(I.ring().gens())))[0]
            Ideal (x0 - x2, x1*x2 + x3^2) of Multivariate Polynomial Ring
             in x0, x1, x2, x3 over Finite Field of size 7
        """
    def curve(self, F):
        """
        Return a curve defined by ``F`` in this projective space.

        INPUT:

        - ``F`` -- a polynomial, or a list or tuple of polynomials in
          the coordinate ring of this projective space

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P.curve([y^2 - x*z])                                                  # needs sage.schemes
            Projective Plane Curve over Rational Field defined by y^2 - x*z
        """
    def line_through(self, p, q):
        """
        Return the line through ``p`` and ``q``.

        INPUT:

        - ``p``, ``q`` -- distinct rational points of the projective space

        EXAMPLES::

            sage: P3.<x0,x1,x2,x3> = ProjectiveSpace(3, QQ)
            sage: p1 = P3(1, 2, 3, 4)
            sage: p2 = P3(4, 3, 2, 1)
            sage: P3.line_through(p1, p2)                                               # needs sage.libs.singular sage.schemes
            Projective Curve over Rational Field defined by
              -5/4*x0 + 5/2*x1 - 5/4*x2,        -5/2*x0 + 15/4*x1 - 5/4*x3,
              -5/4*x0 + 15/4*x2 - 5/2*x3,       -5/4*x1 + 5/2*x2 - 5/4*x3
            sage: p3 = P3(2,4,6,8)
            sage: P3.line_through(p1, p3)
            Traceback (most recent call last):
            ...
            ValueError: not distinct points
        """

class ProjectiveSpace_finite_field(ProjectiveSpace_field):
    def __iter__(self):
        """
        Return iterator over the elements of this projective space.

        Note that iteration is over the decomposition
        `\\mathbb{P}^n = \\mathbb{A}^n \\cup \\mathbb{P}^n-1`, where
        `\\mathbb{A}^n` is the `n`-th affine patch and
        `\\mathbb{P}^n-1` is the hyperplane at infinity
        `x_n = 0`.

        EXAMPLES::

            sage: FF = FiniteField(3)
            sage: PP = ProjectiveSpace(0, FF)
            sage: [ x for x in PP ]
            [(1)]
            sage: PP = ProjectiveSpace(1, FF)
            sage: [ x for x in PP ]
            [(0 : 1), (1 : 1), (2 : 1), (1 : 0)]
            sage: PP = ProjectiveSpace(2, FF)
            sage: [ x for x in PP ]
            [(0 : 0 : 1),
             (0 : 1 : 1),
             (0 : 2 : 1),
             (1 : 0 : 1),
             (1 : 1 : 1),
             (1 : 2 : 1),
             (2 : 0 : 1),
             (2 : 1 : 1),
             (2 : 2 : 1),
             (0 : 1 : 0),
             (1 : 1 : 0),
             (2 : 1 : 0),
             (1 : 0 : 0)]

        AUTHORS:

        - David Kohel, John Cremona

        .. TODO::

            Iteration for point sets over finite fields, and return of
            iter of point set over base field. Note that the point set does not
            know whether this is a projective space or subscheme.
        """
    def rational_points(self, F=None):
        """
        Return the list of ``F``-rational points on this projective space,
        where ``F`` is a given finite field, or the base ring of this space.

        EXAMPLES::

            sage: P = ProjectiveSpace(1, GF(3))
            sage: P.rational_points()
            [(0 : 1), (1 : 1), (2 : 1), (1 : 0)]
            sage: sorted(P.rational_points(GF(3^2, 'b')), key=str)                      # needs sage.rings.finite_rings
            [(0 : 1), (1 : 0), (1 : 1), (2 : 1),
             (2*b + 1 : 1), (2*b + 2 : 1), (2*b : 1),
             (b + 1 : 1), (b + 2 : 1), (b : 1)]
        """
    def rational_points_dictionary(self):
        """
        Return dictionary of points.

        OUTPUT: dictionary

        EXAMPLES::

            sage: P1 = ProjectiveSpace(GF(7), 1, 'x')
            sage: P1.rational_points_dictionary()
            {(0 : 1): 0,
             (1 : 0): 7,
             (1 : 1): 1,
             (2 : 1): 2,
             (3 : 1): 3,
             (4 : 1): 4,
             (5 : 1): 5,
             (6 : 1): 6}
        """

class ProjectiveSpace_rational_field(ProjectiveSpace_field):
    def rational_points(self, bound: int = 0):
        """
        Return the projective points `(x_0:\\cdots:x_n)` over
        `\\QQ` with `|x_i| \\leq` bound.

        ALGORITHM:

        The very simple algorithm works as follows: every point
        `(x_0:\\cdots:x_n)` in projective space has a unique
        largest index `i` for which `x_i` is not
        zero. The algorithm then iterates downward on this
        index. We normalize by choosing `x_i` positive. Then,
        the points `x_0,\\ldots,x_{i-1}` are the points of
        affine `i`-space that are relatively prime to
        `x_i`. We access these by using the Tuples method.

        INPUT:

        - ``bound`` -- integer

        EXAMPLES::

            sage: PP = ProjectiveSpace(0, QQ)
            sage: PP.rational_points(1)
            [(1)]
            sage: PP = ProjectiveSpace(1, QQ)
            sage: PP.rational_points(2)
            [(-2 : 1), (-1 : 1), (0 : 1), (1 : 1), (2 : 1), (-1/2 : 1), (1/2 : 1), (1 : 0)]
            sage: PP = ProjectiveSpace(2, QQ)
            sage: PP.rational_points(2)
            [(-2 : -2 : 1), (-1 : -2 : 1), (0 : -2 : 1), (1 : -2 : 1), (2 : -2 : 1),
             (-2 : -1 : 1), (-1 : -1 : 1), (0 : -1 : 1), (1 : -1 : 1), (2 : -1 : 1),
             (-2 : 0 : 1), (-1 : 0 : 1), (0 : 0 : 1), (1 : 0 : 1), (2 : 0 : 1), (-2 : 1 : 1),
             (-1 : 1 : 1), (0 : 1 : 1), (1 : 1 : 1), (2 : 1 : 1), (-2 : 2 : 1),
             (-1 : 2 : 1), (0 : 2 : 1), (1 : 2 : 1), (2 : 2 : 1), (-1/2 : -1 : 1),
             (1/2 : -1 : 1), (-1 : -1/2 : 1), (-1/2 : -1/2 : 1), (0 : -1/2 : 1),
             (1/2 : -1/2 : 1), (1 : -1/2 : 1), (-1/2 : 0 : 1), (1/2 : 0 : 1), (-1 : 1/2 : 1),
             (-1/2 : 1/2 : 1), (0 : 1/2 : 1), (1/2 : 1/2 : 1), (1 : 1/2 : 1), (-1/2 : 1 : 1),
             (1/2 : 1 : 1), (-2 : 1 : 0), (-1 : 1 : 0), (0 : 1 : 0), (1 : 1 : 0),
             (2 : 1 : 0), (-1/2 : 1 : 0), (1/2 : 1 : 0), (1 : 0 : 0)]

        AUTHORS:

        - Benjamin Antieau (2008-01-12)
        """
