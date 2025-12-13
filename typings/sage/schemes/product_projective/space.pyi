from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polydict import ETuple as ETuple
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme
from sage.schemes.generic.ambient_space import AmbientSpace as AmbientSpace
from sage.schemes.product_projective.homset import SchemeHomset_points_product_projective_spaces_field as SchemeHomset_points_product_projective_spaces_field, SchemeHomset_points_product_projective_spaces_ring as SchemeHomset_points_product_projective_spaces_ring
from sage.schemes.product_projective.morphism import ProductProjectiveSpaces_morphism_ring as ProductProjectiveSpaces_morphism_ring
from sage.schemes.product_projective.point import ProductProjectiveSpaces_point_field as ProductProjectiveSpaces_point_field, ProductProjectiveSpaces_point_finite_field as ProductProjectiveSpaces_point_finite_field, ProductProjectiveSpaces_point_ring as ProductProjectiveSpaces_point_ring
from sage.schemes.product_projective.subscheme import AlgebraicScheme_subscheme_product_projective as AlgebraicScheme_subscheme_product_projective
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, ProjectiveSpace_ring as ProjectiveSpace_ring

def is_ProductProjectiveSpaces(x):
    """
    Return ``True`` if ``x`` is a product of projective spaces.

    This is an ambient space defined by `\\mathbb{P}^n_R \\times \\cdots \\times \\mathbb{P}^m_R`,
    where `R` is a ring and `n,\\ldots, m\\geq 0` are integers.

    OUTPUT: boolean

    EXAMPLES::

        sage: is_ProductProjectiveSpaces(ProjectiveSpace(5, names='x'))
        doctest:warning...
        DeprecationWarning: The function is_ProductProjectiveSpaces is deprecated; use 'isinstance(..., ProductProjectiveSpaces_ring)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
        sage: is_ProductProjectiveSpaces(ProductProjectiveSpaces([1, 2, 3], ZZ, 'x'))
        True
    """
def ProductProjectiveSpaces(n, R=None, names: str = 'x'):
    """
    Return the Cartesian product of projective spaces.

    The input ``n`` is either a list of projective space over the same base
    ring or the list of dimensions, ``R`` the base ring, and ``names`` the
    variable names.

    INPUT:

    - ``n`` -- list of integers or a list of projective spaces

    - ``R`` -- a ring

    - ``names`` -- string or list of strings

    EXAMPLES::

        sage: P1 = ProjectiveSpace(QQ, 2, 'x')
        sage: P2 = ProjectiveSpace(QQ, 3, 'y')
        sage: ProductProjectiveSpaces([P1, P2])
        Product of projective spaces P^2 x P^3 over Rational Field

    ::

        sage: ProductProjectiveSpaces([2, 2], GF(7), 'y')
        Product of projective spaces P^2 x P^2 over Finite Field of size 7

    ::

        sage: P1 = ProjectiveSpace(ZZ, 2, 'x')
        sage: P2 = ProjectiveSpace(QQ, 3, 'y')
        sage: ProductProjectiveSpaces([P1, P2])
        Traceback (most recent call last):
        ...
        AttributeError: components must be over the same base ring
    """

class ProductProjectiveSpaces_ring(AmbientSpace):
    """
    Cartesian product of projective spaces `\\mathbb{P}^{n_1} \\times \\cdots \\times \\mathbb{P}^{n_r}`.

    EXAMPLES::

        sage: P.<x0,x1,x2,x3,x4> = ProductProjectiveSpaces([1, 2], QQ); P
        Product of projective spaces P^1 x P^2 over Rational Field
        sage: P.coordinate_ring()
        Multivariate Polynomial Ring in x0, x1, x2, x3, x4 over Rational Field
        sage: P[0]
        Projective Space of dimension 1 over Rational Field
        sage: P[1]
        Projective Space of dimension 2 over Rational Field
        sage: Q = P(6, 3, 2, 2, 2); Q
        (2 : 1 , 1 : 1 : 1)
        sage: Q[0]
        (2 : 1)
        sage: H = Hom(P,P)
        sage: f = H([x0^2*x3, x2*x1^2, x2^2, 2*x3^2, x4^2])
        sage: f(Q)
        (4 : 1 , 1 : 2 : 1)
    """
    def __init__(self, N, R=..., names=None) -> None:
        """
        The Python constructor.

        INPUT:

        - ``N`` -- list or tuple of positive integers

        - ``R`` -- a ring

        - ``names`` -- tuple or list of strings; this must either be a single
          variable name or the complete list of variables

        EXAMPLES::

            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], QQ)
            sage: T
            Product of projective spaces P^2 x P^2 over Rational Field
            sage: T.coordinate_ring()
            Multivariate Polynomial Ring in x, y, z, u, v, w over Rational Field
            sage: T[1].coordinate_ring()
            Multivariate Polynomial Ring in u, v, w over Rational Field

        ::

            sage: ProductProjectiveSpaces([1,1,1],ZZ, ['x', 'y', 'z', 'u', 'v', 'w'])
            Product of projective spaces P^1 x P^1 x P^1 over Integer Ring

        ::

            sage: T = ProductProjectiveSpaces([1, 1], QQ, 'z')
            sage: T.coordinate_ring()
            Multivariate Polynomial Ring in z0, z1, z2, z3 over Rational Field
        """
    def __getitem__(self, i):
        """
        Return the `i`-th component of the product.

        INPUT:

        - ``i`` -- positive integer

        OUTPUT: a projective space

        EXAMPLES::

            sage: T.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T[0]
            Projective Space of dimension 3 over Rational Field
        """
    def __eq__(self, right):
        """
        Check equality of two products of projective spaces.

        INPUT:

        - ``right`` -- a product of projective spaces

        OUTPUT: boolean

        EXAMPLES::

            sage: S.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], QQ)
            sage: S == T
            False
        """
    def __ne__(self, other):
        """
        Check non-equality of two products of projective spaces.

        INPUT:

        - ``other`` -- a product of projective spaces

        OUTPUT: boolean

        EXAMPLES::

            sage: S.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], QQ)
            sage: S != T
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: S.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], QQ)
            sage: U.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: hash(S) == hash(T)
            False
            sage: hash(S) == hash(U)
            True
        """
    def __pow__(self, m):
        """
        Return the Cartesian power of this space.

        INPUT:

        - ``m`` -- integer

        OUTPUT: product of projective spaces

        EXAMPLES::

            sage: P1 = ProductProjectiveSpaces([2, 1], QQ, 'x')
            sage: P1^3
            Product of projective spaces P^2 x P^1 x P^2 x P^1 x P^2 x P^1
             over Rational Field

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

            sage: S.<t,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.<a,b> = ProjectiveSpace(QQ, 1)
            sage: S*T
            Product of projective spaces P^3 x P^2 x P^1 over Rational Field

        ::

            sage: S = ProductProjectiveSpaces([3, 2], QQ, 'x')
            sage: T = ProductProjectiveSpaces([2, 2], QQ, 'y')
            sage: S*T
            Product of projective spaces P^3 x P^2 x P^2 x P^2 over Rational Field

        ::

            sage: S = ProductProjectiveSpaces([1, 2, 1], ZZ, 't')
            sage: T = ProductProjectiveSpaces([2, 2], ZZ, 'x')
            sage: T.inject_variables()
            Defining x0, x1, x2, x3, x4, x5
            sage: X = T.subscheme([x0*x4 - x1*x3])
            sage: S*X
            Closed subscheme of Product of projective spaces P^1 x P^2 x P^1 x P^2 x P^2 over Integer Ring defined by:
              -x1*x3 + x0*x4

        ::

            sage: S = ProductProjectiveSpaces([3, 2], QQ,'x')
            sage: T = AffineSpace(2, QQ, 'y')
            sage: S*T
            Traceback (most recent call last):
            ...
            TypeError: Affine Space of dimension 2 over Rational Field must be a projective space,
            product of projective spaces, or subscheme
        """
    def components(self):
        """
        Return the components of this product of projective spaces.

        OUTPUT: list of projective spaces

        EXAMPLES::

            sage: P.<x,y,z,u,v> = ProductProjectiveSpaces(QQ, [2, 1])
            sage: P.components()
            [Projective Space of dimension 2 over Rational Field,
            Projective Space of dimension 1 over Rational Field]
        """
    def dimension_relative(self):
        """
        Return the relative dimension of the product of projective spaces.

        OUTPUT: a positive integer

        EXAMPLES::

            sage: T.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.dimension_relative()
            5
        """
    def dimension_absolute(self):
        """
        Return the absolute dimension of the product of projective spaces.

        OUTPUT: a positive integer

        EXAMPLES::

            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], GF(17))
            sage: T.dimension_absolute()
            4
            sage: T.dimension()
            4
        """
    dimension = dimension_absolute
    def dimension_relative_components(self):
        """
        Return the relative dimension of the product of projective spaces.

        OUTPUT: list of positive integers

        EXAMPLES::

            sage: T.<a,x,y,z,u,v,w> = ProductProjectiveSpaces([3, 2], QQ)
            sage: T.dimension_relative_components()
            [3, 2]
        """
    def dimension_absolute_components(self):
        """
        Return the absolute dimension of the product of projective spaces.

        OUTPUT: list of positive integers

        EXAMPLES::

            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], GF(17))
            sage: T.dimension_absolute_components()
            [2, 2]
            sage: T.dimension_components()
            [2, 2]
        """
    dimension_components = dimension_absolute_components
    def num_components(self):
        """
        Return the number of components of this space.

        OUTPUT: integer

        EXAMPLES::

            sage: T = ProductProjectiveSpaces([1, 1, 1], GF(5), 'x')
            sage: T.num_components()
            3
        """
    def ngens(self):
        """
        Return the number of generators of this space.

        This is the number of variables in the coordinate ring of the
        projective space.

        OUTPUT: integer

        EXAMPLES::

            sage: T = ProductProjectiveSpaces([1, 1, 1], GF(5), 'x')
            sage: T.ngens()
            6
        """
    def subscheme(self, X):
        """
        Return the closed subscheme defined by ``X``.

        INPUT:

        - ``X`` -- list or tuple of equations

        OUTPUT: :class:`AlgebraicScheme_subscheme_projective_cartesian_product`

        EXAMPLES::

            sage: P.<x,y,z,w> = ProductProjectiveSpaces([1, 1], GF(5))
            sage: X = P.subscheme([x - y, z - w]); X
            Closed subscheme of Product of projective spaces P^1 x P^1
             over Finite Field of size 5 defined by:
              x - y,
              z - w
            sage: X.defining_polynomials()
            [x - y, z - w]
            sage: I = X.defining_ideal(); I
            Ideal (x - y, z - w) of Multivariate Polynomial Ring in x, y, z, w
             over Finite Field of size 5
            sage: X.dimension()                                                         # needs sage.libs.singular
            0
            sage: X.base_ring()
            Finite Field of size 5
            sage: X.base_scheme()
            Spectrum of Finite Field of size 5
            sage: X.structure_morphism()
            Scheme morphism:
              From: Closed subscheme of Product of projective spaces P^1 x P^1
                    over Finite Field of size 5 defined by: x - y, z - w
              To:   Spectrum of Finite Field of size 5
              Defn: Structure map
        """
    def change_ring(self, R):
        """
        Return a product of projective spaces over a ring ``R`` and otherwise
        the same as this projective space.

        INPUT:

        - ``R`` -- commutative ring or morphism

        OUTPUT: product of projective spaces over ``R``

        .. NOTE::

            There is no need to have any relation between ``R`` and the base ring
            of this space, if you want to have such a relation, use
            ``self.base_extend(R)`` instead.

        EXAMPLES::

            sage: T.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], QQ)
            sage: T.change_ring(GF(17))
            Product of projective spaces P^2 x P^2 over Finite Field of size 17
        """
    def affine_patch(self, I, return_embedding: bool = False):
        """
        Return the `I`-th affine patch of this projective space product
        where ``I`` is a multi-index.

        INPUT:

        - ``I`` -- list or tuple of positive integers

        - ``return_embedding`` -- boolean; if ``True`` the projective embedding
          is also returned

        OUTPUT:

        - An affine space.

        - An embedding into a product of projective spaces (optional).

        EXAMPLES::

            sage: PP = ProductProjectiveSpaces([2, 2, 2], ZZ, 'x')
            sage: phi = PP.affine_patch([0, 1, 2], True)
            sage: phi.domain()
            Affine Space of dimension 6 over Integer Ring
            sage: phi
            Scheme morphism:
              From: Affine Space of dimension 6 over Integer Ring
              To:   Product of projective spaces P^2 x P^2 x P^2 over Integer Ring
              Defn: Defined on coordinates by sending (x0, x1, x2, x3, x4, x5) to
                    (1 : x0 : x1 , x2 : 1 : x3 , x4 : x5 : 1)
        """
    @cached_method
    def segre_embedding(self, PP=None, var: str = 'u'):
        """
        Return the Segre embedding of this space into the appropriate
        projective space.

        INPUT:

        - ``PP`` -- (default: ``None``) ambient image projective space;
            this is constructed if it is not given

        - ``var`` -- string (default: ``'u'``); variable name of the image
          projective space

        OUTPUT: Hom; from this space to the appropriate subscheme of projective
        space

        .. TODO::

            Cartesian products with more than two components.

        EXAMPLES::

            sage: X.<y0,y1,y2,y3,y4,y5> = ProductProjectiveSpaces(ZZ, [2, 2])
            sage: phi = X.segre_embedding(); phi                                        # needs sage.libs.singular
            Scheme morphism:
              From: Product of projective spaces P^2 x P^2 over Integer Ring
              To:   Closed subscheme of Projective Space of dimension 8 over Integer Ring
                    defined by:
                      -u5*u7 + u4*u8,       -u5*u6 + u3*u8,       -u4*u6 + u3*u7,
                      -u2*u7 + u1*u8,       -u2*u4 + u1*u5,       -u2*u6 + u0*u8,
                      -u1*u6 + u0*u7,       -u2*u3 + u0*u5,       -u1*u3 + u0*u4
              Defn: Defined by sending (y0 : y1 : y2 , y3 : y4 : y5) to
                    (y0*y3 : y0*y4 : y0*y5 : y1*y3 : y1*y4 : y1*y5 : y2*y3 : y2*y4 : y2*y5).

            ::

            sage: T = ProductProjectiveSpaces([1, 2], CC, 'z')                          # needs sage.rings.real_mpfr
            sage: T.segre_embedding()                                                   # needs sage.libs.singular sage.rings.real_mpfr
            Scheme morphism:
              From: Product of projective spaces P^1 x P^2
                    over Complex Field with 53 bits of precision
              To:   Closed subscheme of Projective Space of dimension 5
                    over Complex Field with 53 bits of precision defined by:
                      -u2*u4 + u1*u5,       -u2*u3 + u0*u5,       -u1*u3 + u0*u4
              Defn: Defined by sending (z0 : z1 , z2 : z3 : z4) to
                    (z0*z2 : z0*z3 : z0*z4 : z1*z2 : z1*z3 : z1*z4).

            ::

            sage: T = ProductProjectiveSpaces([1, 2, 1], QQ, 'z')
            sage: T.segre_embedding()                                                   # needs sage.libs.singular
            Scheme morphism:
              From: Product of projective spaces P^1 x P^2 x P^1 over Rational Field
              To:   Closed subscheme of Projective Space of dimension 11
                    over Rational Field defined by:
                      -u9*u10 + u8*u11,     -u7*u10 + u6*u11,     -u7*u8 + u6*u9,
                      -u5*u10 + u4*u11,     -u5*u8 + u4*u9,       -u5*u6 + u4*u7,
                      -u5*u9 + u3*u11,      -u5*u8 + u3*u10,      -u5*u8 + u2*u11,
                      -u4*u8 + u2*u10,      -u3*u8 + u2*u9,       -u3*u6 + u2*u7,
                      -u3*u4 + u2*u5,       -u5*u7 + u1*u11,      -u5*u6 + u1*u10,
                      -u3*u7 + u1*u9,       -u3*u6 + u1*u8,       -u5*u6 + u0*u11,
                      -u4*u6 + u0*u10,      -u3*u6 + u0*u9,       -u2*u6 + u0*u8,
                      -u1*u6 + u0*u7,       -u1*u4 + u0*u5,       -u1*u2 + u0*u3
              Defn: Defined by sending (z0 : z1 , z2 : z3 : z4 , z5 : z6) to
                    (z0*z2*z5 : z0*z2*z6 : z0*z3*z5 : z0*z3*z6 : z0*z4*z5 : z0*z4*z6
                     : z1*z2*z5 : z1*z2*z6 : z1*z3*z5 : z1*z3*z6 : z1*z4*z5 : z1*z4*z6).
        """

class ProductProjectiveSpaces_field(ProductProjectiveSpaces_ring):
    def points_of_bounded_height(self, **kwds) -> Generator[Incomplete]:
        """
        Return an iterator of the points in this product of projective spaces
        with the absolute heights of the components of at most the given bound.

        Bound check is strict for the rational field. Requires the base field
        of this space to be a number field. Uses the Doyle-Krumm algorithm 4
        (algorithm 5 for imaginary quadratic) for computing algebraic numbers
        up to a given height [DK2013]_.

        The algorithm requires floating point arithmetic, so the user is
        allowed to specify the precision for such calculations.
        Additionally, due to floating point issues, points
        slightly larger than the bound may be returned. This can be controlled
        by lowering the tolerance.


        INPUT:

        - ``bound`` -- a real number

        - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm
          algorithm-4

        - ``precision`` -- the precision to use for computing the elements of
          bounded height of number fields

        OUTPUT: an iterator of points in this space

        EXAMPLES::

            sage: PP = ProductProjectiveSpaces(QQ, [1, 2])
            sage: sorted(list(PP.points_of_bounded_height(bound=1)))
            [(-1 : 1 , -1 : -1 : 1), (-1 : 1 , -1 : 0 : 1), (-1 : 1 , -1 : 1 : 0),
             (-1 : 1 , -1 : 1 : 1), (-1 : 1 , 0 : -1 : 1), (-1 : 1 , 0 : 0 : 1),
             (-1 : 1 , 0 : 1 : 0), (-1 : 1 , 0 : 1 : 1), (-1 : 1 , 1 : -1 : 1),
             (-1 : 1 , 1 : 0 : 0), (-1 : 1 , 1 : 0 : 1), (-1 : 1 , 1 : 1 : 0),
             (-1 : 1 , 1 : 1 : 1), (0 : 1 , -1 : -1 : 1), (0 : 1 , -1 : 0 : 1),
             (0 : 1 , -1 : 1 : 0), (0 : 1 , -1 : 1 : 1), (0 : 1 , 0 : -1 : 1),
             (0 : 1 , 0 : 0 : 1), (0 : 1 , 0 : 1 : 0), (0 : 1 , 0 : 1 : 1),
             (0 : 1 , 1 : -1 : 1), (0 : 1 , 1 : 0 : 0), (0 : 1 , 1 : 0 : 1),
             (0 : 1 , 1 : 1 : 0), (0 : 1 , 1 : 1 : 1), (1 : 0 , -1 : -1 : 1),
             (1 : 0 , -1 : 0 : 1), (1 : 0 , -1 : 1 : 0), (1 : 0 , -1 : 1 : 1),
             (1 : 0 , 0 : -1 : 1), (1 : 0 , 0 : 0 : 1), (1 : 0 , 0 : 1 : 0),
             (1 : 0 , 0 : 1 : 1), (1 : 0 , 1 : -1 : 1), (1 : 0 , 1 : 0 : 0),
             (1 : 0 , 1 : 0 : 1), (1 : 0 , 1 : 1 : 0), (1 : 0 , 1 : 1 : 1),
             (1 : 1 , -1 : -1 : 1), (1 : 1 , -1 : 0 : 1), (1 : 1 , -1 : 1 : 0),
             (1 : 1 , -1 : 1 : 1), (1 : 1 , 0 : -1 : 1), (1 : 1 , 0 : 0 : 1),
             (1 : 1 , 0 : 1 : 0), (1 : 1 , 0 : 1 : 1), (1 : 1 , 1 : -1 : 1),
             (1 : 1 , 1 : 0 : 0), (1 : 1 , 1 : 0 : 1), (1 : 1 , 1 : 1 : 0),
             (1 : 1 , 1 : 1 : 1)]

        ::

            sage: u = QQ['u'].0
            sage: P = ProductProjectiveSpaces([1, 1], NumberField(u^2 - 2, 'v'))        # needs sage.rings.number_field
            sage: sorted(list(P.points_of_bounded_height(bound=1.5)))                   # needs sage.rings.number_field
            [(-v : 1 , -v : 1), (-v : 1 , -1 : 1), (-v : 1 , -1/2*v : 1), (-v : 1 , 0 : 1),
             (-v : 1 , 1/2*v : 1), (-v : 1 , 1 : 0), (-v : 1 , 1 : 1), (-v : 1 , v : 1),
             (-1 : 1 , -v : 1), (-1 : 1 , -1 : 1), (-1 : 1 , -1/2*v : 1), (-1 : 1 , 0 : 1),
             (-1 : 1 , 1/2*v : 1), (-1 : 1 , 1 : 0), (-1 : 1 , 1 : 1), (-1 : 1 , v : 1),
             (-1/2*v : 1 , -v : 1), (-1/2*v : 1 , -1 : 1), (-1/2*v : 1 , -1/2*v : 1),
             (-1/2*v : 1 , 0 : 1), (-1/2*v : 1 , 1/2*v : 1), (-1/2*v : 1 , 1 : 0),
             (-1/2*v : 1 , 1 : 1), (-1/2*v : 1 , v : 1), (0 : 1 , -v : 1), (0 : 1 , -1 : 1),
             (0 : 1 , -1/2*v : 1), (0 : 1 , 0 : 1), (0 : 1 , 1/2*v : 1), (0 : 1 , 1 : 0),
             (0 : 1 , 1 : 1), (0 : 1 , v : 1), (1/2*v : 1 , -v : 1), (1/2*v : 1 , -1 : 1),
             (1/2*v : 1 , -1/2*v : 1), (1/2*v : 1 , 0 : 1), (1/2*v : 1 , 1/2*v : 1),
             (1/2*v : 1 , 1 : 0), (1/2*v : 1 , 1 : 1), (1/2*v : 1 , v : 1), (1 : 0 , -v : 1),
             (1 : 0 , -1 : 1), (1 : 0 , -1/2*v : 1), (1 : 0 , 0 : 1), (1 : 0 , 1/2*v : 1),
             (1 : 0 , 1 : 0), (1 : 0 , 1 : 1), (1 : 0 , v : 1), (1 : 1 , -v : 1),
             (1 : 1 , -1 : 1), (1 : 1 , -1/2*v : 1), (1 : 1 , 0 : 1), (1 : 1 , 1/2*v : 1),
             (1 : 1 , 1 : 0), (1 : 1 , 1 : 1), (1 : 1 , v : 1), (v : 1 , -v : 1),
             (v : 1 , -1 : 1), (v : 1 , -1/2*v : 1), (v : 1 , 0 : 1), (v : 1 , 1/2*v : 1),
             (v : 1 , 1 : 0), (v : 1 , 1 : 1), (v : 1 , v : 1)]
        """

class ProductProjectiveSpaces_finite_field(ProductProjectiveSpaces_field):
    def __iter__(self):
        """
        Return an iterator over the elements of this product of projective spaces.

        EXAMPLES::

            sage: P = ProductProjectiveSpaces([2, 1], GF(3))
            sage: [x for x in P]
            [(0 : 0 : 1 , 0 : 1),
             (0 : 1 : 1 , 0 : 1),
             (0 : 2 : 1 , 0 : 1),
             ...
             (1 : 1 : 0 , 1 : 0),
             (2 : 1 : 0 , 1 : 0),
             (1 : 0 : 0 , 1 : 0)]
        """
    def rational_points(self, F=None):
        """
        Return the list of `F`-rational points on this product of projective spaces,
        where `F` is a given finite field, or the base ring of this space.

        EXAMPLES::

            sage: P = ProductProjectiveSpaces([1, 1], GF(5))
            sage: P.rational_points()
            [(0 : 1 , 0 : 1), (1 : 1 , 0 : 1), (2 : 1 , 0 : 1), (3 : 1 , 0 : 1), (4 : 1 , 0 : 1), (1 : 0 , 0 : 1),
             (0 : 1 , 1 : 1), (1 : 1 , 1 : 1), (2 : 1 , 1 : 1), (3 : 1 , 1 : 1), (4 : 1 , 1 : 1), (1 : 0 , 1 : 1),
             (0 : 1 , 2 : 1), (1 : 1 , 2 : 1), (2 : 1 , 2 : 1), (3 : 1 , 2 : 1), (4 : 1 , 2 : 1), (1 : 0 , 2 : 1),
             (0 : 1 , 3 : 1), (1 : 1 , 3 : 1), (2 : 1 , 3 : 1), (3 : 1 , 3 : 1), (4 : 1 , 3 : 1), (1 : 0 , 3 : 1),
             (0 : 1 , 4 : 1), (1 : 1 , 4 : 1), (2 : 1 , 4 : 1), (3 : 1 , 4 : 1), (4 : 1 , 4 : 1), (1 : 0 , 4 : 1),
             (0 : 1 , 1 : 0), (1 : 1 , 1 : 0), (2 : 1 , 1 : 0), (3 : 1 , 1 : 0), (4 : 1 , 1 : 0), (1 : 0 , 1 : 0)]

        ::

            sage: P = ProductProjectiveSpaces([1, 1], GF(2))
            sage: sorted(P.rational_points(GF(2^2, 'a')), key=str)                      # needs sage.rings.finite_rings
            [(0 : 1 , 0 : 1), (0 : 1 , 1 : 0), (0 : 1 , 1 : 1), (0 : 1 , a + 1 : 1), (0 : 1 , a : 1),
             (1 : 0 , 0 : 1), (1 : 0 , 1 : 0), (1 : 0 , 1 : 1), (1 : 0 , a + 1 : 1), (1 : 0 , a : 1),
             (1 : 1 , 0 : 1), (1 : 1 , 1 : 0), (1 : 1 , 1 : 1), (1 : 1 , a + 1 : 1), (1 : 1 , a : 1),
             (a + 1 : 1 , 0 : 1), (a + 1 : 1 , 1 : 0), (a + 1 : 1 , 1 : 1), (a + 1 : 1 , a + 1 : 1), (a + 1 : 1 , a : 1),
             (a : 1 , 0 : 1), (a : 1 , 1 : 0), (a : 1 , 1 : 1), (a : 1 , a + 1 : 1), (a : 1 , a : 1)]
        """
