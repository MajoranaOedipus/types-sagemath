from . import ambient_space as ambient_space, scheme as scheme
from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.latex import latex as latex
from sage.misc.misc import is_iterator as is_iterator
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import RationalField as RationalField
from sage.structure.all import Sequence as Sequence
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

def is_AlgebraicScheme(x):
    """
    Test whether ``x`` is an algebraic scheme.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    boolean; whether ``x`` is an algebraic scheme, that is, a
    subscheme of an ambient space over a ring defined by polynomial
    equations.

    EXAMPLES::

        sage: A2 = AffineSpace(2, QQ, 'x, y')
        sage: A2.coordinate_ring().inject_variables()
        Defining x, y
        sage: V = A2.subscheme([x^2 + y^2]); V
        Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
          x^2 + y^2
        sage: from sage.schemes.generic.algebraic_scheme import is_AlgebraicScheme
        sage: is_AlgebraicScheme(V)
        doctest:warning...
        DeprecationWarning: The function is_AlgebraicScheme is deprecated; use 'isinstance(..., AlgebraicScheme)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True

    Affine space is itself not an algebraic scheme, though the closed
    subscheme defined by no equations is::

        sage: from sage.schemes.generic.algebraic_scheme import is_AlgebraicScheme
        sage: is_AlgebraicScheme(AffineSpace(10, QQ))
        False
        sage: V = AffineSpace(10, QQ).subscheme([]); V
        Closed subscheme of Affine Space of dimension 10 over Rational Field defined by:
          (no polynomials)
        sage: is_AlgebraicScheme(V)
        True

    We create a more complicated closed subscheme::

        sage: A,x = AffineSpace(10, QQ).objgens()
        sage: X = A.subscheme([sum(x)]); X
        Closed subscheme of Affine Space of dimension 10 over Rational Field defined by:
          x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
        sage: is_AlgebraicScheme(X)
        True

    ::

        sage: is_AlgebraicScheme(QQ)
        False
        sage: S = Spec(QQ)
        sage: is_AlgebraicScheme(S)
        False
    """

class AlgebraicScheme(scheme.Scheme):
    """
    An algebraic scheme presented as a subscheme in an ambient space.

    This is the base class for all algebraic schemes, that is, schemes
    defined by equations in affine, projective, or toric ambient
    spaces.
    """
    def __init__(self, A, category=None) -> None:
        """
        TESTS::

            sage: from sage.schemes.generic.algebraic_scheme import AlgebraicScheme
            sage: P = ProjectiveSpace(3, ZZ)
            sage: P.category()
            Category of schemes over Integer Ring
            sage: S = AlgebraicScheme(P); S
            Subscheme of Projective Space of dimension 3 over Integer Ring
            sage: S.category()
            Category of schemes over Integer Ring
        """
    def is_projective(self):
        """
        Return ``True`` if ``self`` is presented as a subscheme of an ambient
        projective space.

        OUTPUT: boolean

        EXAMPLES::

            sage: PP.<x,y,z,w> = ProjectiveSpace(3, QQ)
            sage: f = x^3 + y^3 + z^3 + w^3
            sage: R = f.parent()
            sage: I = [f] + [f.derivative(zz) for zz in PP.gens()]
            sage: V = PP.subscheme(I)
            sage: V.is_projective()
            True
            sage: AA.<x,y,z,w> = AffineSpace(4, QQ)
            sage: V = AA.subscheme(I)
            sage: V.is_projective()
            False

        Note that toric varieties are implemented differently than
        projective spaces. This is why this method returns ``False``
        for toric varieties::

            sage: # needs sage.geometry.polyhedron sage.graphs
            sage: PP.<x,y,z,w> = toric_varieties.P(3)
            sage: V = PP.subscheme(x^3 + y^3 + z^3 + w^3)
            sage: V.is_projective()
            False
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring of this algebraic scheme.  The
        result is cached.

        OUTPUT:

        The coordinate ring. Usually a polynomial ring, or a quotient
        thereof.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([x - y, x - z])
            sage: S.coordinate_ring()
            Quotient of Multivariate Polynomial Ring in x, y, z over Integer Ring
             by the ideal (x - y, x - z)
        """
    def ambient_space(self):
        """
        Return the ambient space of this algebraic scheme.

        EXAMPLES::

            sage: A.<x, y> = AffineSpace(2, GF(5))
            sage: S = A.subscheme([])
            sage: S.ambient_space()
            Affine Space of dimension 2 over Finite Field of size 5

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([x - y, x - z])
            sage: S.ambient_space() is P
            True
        """
    def identity_morphism(self):
        """
        Return the identity morphism.

        OUTPUT: the identity morphism of the scheme ``self``

        EXAMPLES::

            sage: X = Spec(QQ)
            sage: X.identity_morphism()
            Scheme endomorphism of Spectrum of Rational Field
              Defn: Identity map
        """
    def embedding_morphism(self):
        """
        Return the default embedding morphism of ``self``.

        If the scheme `Y` was constructed as a neighbourhood of a
        point `p \\in X`, then :meth:`embedding_morphism` returns a
        local isomorphism `f:Y\\to X` around the preimage point
        `f^{-1}(p)`. The latter is returned by
        :meth:`embedding_center`.

        If the algebraic scheme `Y` was not constructed as a
        neighbourhood of a point, then the embedding in its
        :meth:`ambient_space` is returned.

        OUTPUT:

        A scheme morphism whose
        :meth:`~morphism.SchemeMorphism.domain` is ``self``.

        * By default, it is the tautological embedding into its own
          ambient space :meth:`ambient_space`.

        * If the algebraic scheme (which itself is a subscheme of an
          auxiliary :meth:`ambient_space`) was constructed as a patch
          or neighborhood of a point then the embedding is the
          embedding into the original scheme.

        * A :exc:`NotImplementedError` is raised if the construction of
          the embedding morphism is not implemented yet.

        EXAMPLES::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: C = A2.subscheme(x^2 + y^2 - 1)
            sage: C.embedding_morphism()                                                # needs sage.libs.singular
              Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                    defined by: x^2 + y^2 - 1
              To:   Affine Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x, y) to (x, y)

            sage: # needs sage.geometry.polyhedron sage.graphs sage.libs.singular
            sage: P1xP1.<x,y,u,v> = toric_varieties.P1xP1()
            sage: P1 = P1xP1.subscheme(x - y)
            sage: P1.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of 2-d CPR-Fano toric variety covered
                    by 4 affine patches defined by: x - y
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [x : y : u : v] to [y : y : u : v]

        So far, the embedding was just in the own ambient space. Now a
        bit more interesting examples::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P2.subscheme((x^2-y^2)*z)
            sage: p = (1,1,0)
            sage: nbhd = X.neighborhood(p); nbhd
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              -y^2*z - 2*y*z

        Note that `p=(1,1,0)` is a singular point of `X`. So the
        neighborhood of `p` is not just affine space. The
        :meth:`neighborhood` method returns a presentation of
        the neighborhood as a subscheme of an auxiliary 2-dimensional
        affine space::

            sage: nbhd.ambient_space()
            Affine Space of dimension 2 over Rational Field

        But its :meth:`embedding_morphism` is not into this auxiliary
        affine space, but the original subscheme `X`::

            sage: nbhd.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                    defined by: -y^2*z - 2*y*z
              To:   Closed subscheme of Projective Space of dimension 2 over Rational Field
                    defined by: x^2*z - y^2*z
              Defn: Defined on coordinates by sending (y, z) to (1 : y + 1 : z)

        A couple more examples::

            sage: # needs sage.geometry.polyhedron sage.graphs sage.libs.singular
            sage: patch1 = P1xP1.affine_patch(1); patch1
            2-d affine toric variety
            sage: patch1.embedding_morphism()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [y : u] to [1 : y : u : 1]
            sage: subpatch = P1.affine_patch(1); subpatch
            Closed subscheme of 2-d affine toric variety defined by:
              -y + 1
            sage: subpatch.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of 2-d affine toric variety defined by: -y + 1
              To:   Closed subscheme of 2-d CPR-Fano toric variety covered
                    by 4 affine patches defined by: x - y
              Defn: Defined on coordinates by sending [y : u] to [1 : y : u : 1]
        """
    def embedding_center(self):
        """
        Return the distinguished point, if there is any.

        If the scheme `Y` was constructed as a neighbourhood of a
        point `p \\in X`, then :meth:`embedding_morphism` returns a
        local isomorphism `f:Y\\to X` around the preimage point
        `f^{-1}(p)`. The latter is returned by
        :meth:`embedding_center`.

        OUTPUT:

        A point of ``self``. This raises :exc:`AttributeError` if there
        is no distinguished point, depending on how ``self`` was constructed.

        EXAMPLES::

            sage: P3.<w,x,y,z> = ProjectiveSpace(QQ, 3)
            sage: X = P3.subscheme( (w^2-x^2)*(y^2-z^2) )
            sage: p = [1,-1,3,4]
            sage: nbhd = X.neighborhood(p); nbhd
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              w^2*y^2 - x^2*y^2 + 6*w^2*y - 6*x^2*y + 2*w*y^2 +
              2*x*y^2 - 7*w^2 + 7*x^2 + 12*w*y + 12*x*y - 14*w - 14*x
            sage: nbhd.embedding_center()
            (0, 0, 0)
            sage: nbhd.embedding_morphism()(nbhd.embedding_center())
            (1/4 : -1/4 : 3/4 : 1)
            sage: nbhd.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 3 over Rational Field
                    defined by: w^2*y^2 - x^2*y^2 + 6*w^2*y - 6*x^2*y + 2*w*y^2 + 2*x*y^2
                                - 7*w^2 + 7*x^2 + 12*w*y + 12*x*y - 14*w - 14*x
              To:   Closed subscheme of Projective Space of dimension 3 over Rational Field
                    defined by: w^2*y^2 - x^2*y^2 - w^2*z^2 + x^2*z^2
              Defn: Defined on coordinates by sending (w, x, y) to
                    (w + 1 : x - 1 : y + 3 : 4)
        """
    def ngens(self):
        """
        Return the number of generators of the ambient space of this
        algebraic scheme.

        EXAMPLES::

            sage: A.<x, y> = AffineSpace(2, GF(5))
            sage: S = A.subscheme([])
            sage: S.ngens()
            2
            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([x - y, x - z])
            sage: P.ngens()
            3
        """

class AlgebraicScheme_quasi(AlgebraicScheme):
    """
    The quasi-affine or quasi-projective scheme `X - Y`, where `X` and `Y`
    are both closed subschemes of a common ambient affine or projective
    space.

    .. WARNING::

        You should not create objects of this class directly. The
        preferred method to construct such subschemes is to use
        :meth:`complement` method of algebraic schemes.

    OUTPUT: an instance of :class:`AlgebraicScheme_quasi`

    EXAMPLES::

        sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
        sage: S = P.subscheme([])
        sage: T = P.subscheme([x - y])
        sage: T.complement(S)
        Quasi-projective subscheme X - Y
         of Projective Space of dimension 2 over Integer Ring,
         where X is defined by:
           (no polynomials)
         and Y is defined by:
           x - y
    """
    def __init__(self, X, Y) -> None:
        """
        The constructor.

        INPUT:

        - ``X``, ``Y`` -- two subschemes of the same ambient space

        TESTS::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([])
            sage: T = P.subscheme([x - y])
            sage: from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_quasi
            sage: AlgebraicScheme_quasi(S, T)
            Quasi-projective subscheme X - Y of Projective Space of dimension 2 over Integer Ring,
             where X is defined by:
               (no polynomials)
             and Y is defined by:
               x - y
        """
    def X(self):
        """
        Return the scheme `X` such that ``self`` is represented as `X - Y`.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([])
            sage: T = P.subscheme([x - y])
            sage: U = T.complement(S)
            sage: U.X() is S
            True
        """
    def Y(self):
        """
        Return the scheme `Y` such that ``self`` is represented as `X - Y`.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([])
            sage: T = P.subscheme([x - y])
            sage: U = T.complement(S)
            sage: U.Y() is T
            True
        """
    def rational_points(self, **kwds):
        """
        Return the set of rational points on this algebraic scheme
        over the field `F`.

        INPUT: keyword arguments:

        - ``bound`` -- integer (default: 0); the bound for the coordinates for
          subschemes with dimension at least 1

        - ``F`` -- field (default: base ring); the field to compute
          the rational points over

        EXAMPLES::

            sage: A.<x, y> = AffineSpace(2, GF(7))
            sage: S = A.subscheme([x^2 - y])
            sage: T = A.subscheme([x - y])
            sage: U = T.complement(S)
            sage: U.rational_points()
            [(2, 4), (3, 2), (4, 2), (5, 4), (6, 1)]
            sage: U.rational_points(F=GF(7^2, 'b'))                                     # needs sage.rings.finite_rings
            [(2, 4), (3, 2), (4, 2), (5, 4), (6, 1), (b, b + 4), (b + 1, 3*b + 5),
             (b + 2, 5*b + 1), (b + 3, 6), (b + 4, 2*b + 6), (b + 5, 4*b + 1),
             (b + 6, 6*b + 5), (2*b, 4*b + 2), (2*b + 1, b + 3), (2*b + 2, 5*b + 6),
             (2*b + 3, 2*b + 4), (2*b + 4, 6*b + 4), (2*b + 5, 3*b + 6), (2*b + 6, 3),
             (3*b, 2*b + 1), (3*b + 1, b + 2), (3*b + 2, 5), (3*b + 3, 6*b + 3),
             (3*b + 4, 5*b + 3), (3*b + 5, 4*b + 5), (3*b + 6, 3*b + 2),
             (4*b, 2*b + 1), (4*b + 1, 3*b + 2), (4*b + 2, 4*b + 5),
             (4*b + 3, 5*b + 3), (4*b + 4, 6*b + 3), (4*b + 5, 5), (4*b + 6, b + 2),
             (5*b, 4*b + 2), (5*b + 1, 3), (5*b + 2, 3*b + 6), (5*b + 3, 6*b + 4),
             (5*b + 4, 2*b + 4), (5*b + 5, 5*b + 6), (5*b + 6, b + 3), (6*b, b + 4),
             (6*b + 1, 6*b + 5), (6*b + 2, 4*b + 1), (6*b + 3, 2*b + 6), (6*b + 4, 6),
             (6*b + 5, 5*b + 1), (6*b + 6, 3*b + 5)]
        """

class AlgebraicScheme_subscheme(AlgebraicScheme):
    """
    An algebraic scheme presented as a closed subscheme is defined by
    explicit polynomial equations. This is as opposed to a general
    scheme, which could, e.g., be the Neron model of some object, and
    for which we do not want to give explicit equations.

    INPUT:

    - ``A`` -- ambient space (e.g. affine or projective `n`-space)

    - ``polynomials`` -- single polynomial, ideal or iterable of defining
      polynomials; in any case polynomials must belong to the coordinate
      ring of the ambient space and define valid polynomial functions (e.g.
      they should be homogeneous in the case of a projective space)

    OUTPUT: algebraic scheme

    EXAMPLES::

        sage: from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme
        sage: P.<x, y, z> = ProjectiveSpace(2, QQ)
        sage: P.subscheme([x^2 - y*z])
        Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
          x^2 - y*z
        sage: AlgebraicScheme_subscheme(P, [x^2 - y*z])
        Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
          x^2 - y*z
    """
    def __init__(self, A, polynomials, category=None) -> None:
        """
        See ``AlgebraicScheme_subscheme`` for documentation.

        TESTS::

            sage: from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme
            sage: P.<x, y, z> = ProjectiveSpace(2, QQ)
            sage: P.subscheme([x^2 - y*z])
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x^2 - y*z
            sage: AlgebraicScheme_subscheme(P, [x^2 - y*z])
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x^2 - y*z
        """
    def base_extend(self, R):
        """
        Return the base change to the ring `R` of this scheme.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, GF(11))
            sage: S = P.subscheme([x^2 - y*z])
            sage: S.base_extend(GF(11^2, 'b'))                                          # needs sage.rings.finite_rings
            Closed subscheme of Projective Space of dimension 2
             over Finite Field in b of size 11^2
             defined by: x^2 - y*z
            sage: S.base_extend(ZZ)
            Traceback (most recent call last):
            ...
            ValueError: no natural map from the base ring (=Finite Field of size 11)
            to R (=Integer Ring)!
        """
    def __richcmp__(self, other, op):
        """
        EXAMPLES::

            sage: A.<x, y, z> = AffineSpace(3, QQ)
            sage: X = A.subscheme([x*y, z])
            sage: X == A.subscheme([z, x*y])
            True
            sage: X == A.subscheme([x*y, z^2])                                          # needs sage.libs.singular
            False
            sage: B.<u, v, t> = AffineSpace(3, QQ)
            sage: X == B.subscheme([u*v, t])
            False
        """
    def defining_polynomials(self):
        """
        Return the polynomials that define this scheme as a subscheme
        of its ambient space.

        OUTPUT:

        A tuple of polynomials in the coordinate ring of the ambient
        space.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([x^2 - y*z, x^3 + z^3])
            sage: S.defining_polynomials()
            (x^2 - y*z, x^3 + z^3)
        """
    def normalize_defining_polynomials(self) -> None:
        """
        Function to normalize the coefficients of defining polynomials
        of given subscheme.

        Normalization as in removing denominator from all the coefficients,
        and then removing any common factor between the coefficients.
        It takes LCM of denominators and then removes common factor among
        coefficients, if any.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(2, QQ)
            sage: S = A.subscheme([2*x^2 + 4*x*y, 1/8*x + 1/3*y])
            sage: S.normalize_defining_polynomials()
            sage: S.defining_polynomials()
            (x^2 + 2*x*y, 3*x + 8*y)
        """
    def defining_ideal(self):
        """
        Return the ideal that defines this scheme as a subscheme
        of its ambient space.

        OUTPUT: an ideal in the coordinate ring of the ambient space

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([x^2 - y*z, x^3 + z^3])
            sage: S.defining_ideal()
            Ideal (x^2 - y*z, x^3 + z^3) of Multivariate Polynomial Ring in x, y, z
             over Integer Ring
        """
    def codimension(self):
        """
        Return the codimension of the algebraic subscheme.

        OUTPUT: integer

        EXAMPLES::

            sage: PP.<x,y,z,w,v> = ProjectiveSpace(4, QQ)
            sage: V = PP.subscheme(x*y)
            sage: V.codimension()                                                       # needs sage.libs.singular
            1
            sage: V.dimension()                                                         # needs sage.libs.singular
            3
        """
    def irreducible_components(self):
        """
        Return the irreducible components of this algebraic scheme, as
        subschemes of the same ambient space.

        OUTPUT:

        an immutable sequence of irreducible subschemes of the ambient
        space of this scheme

        The components are cached.

        EXAMPLES:

        We define what is clearly a union of four hypersurfaces in
        `\\P^4_{\\QQ}` then find the irreducible components::

            sage: PP.<x,y,z,w,v> = ProjectiveSpace(4, QQ)
            sage: V = PP.subscheme((x^2 - y^2 - z^2) * (w^5 - 2*v^2*z^3) * w * (v^3 - x^2*z))
            sage: V.irreducible_components()                                            # needs sage.libs.singular
            [Closed subscheme of Projective Space of dimension 4 over Rational Field defined by:
               w,
             Closed subscheme of Projective Space of dimension 4 over Rational Field defined by:
               x^2 - y^2 - z^2,
             Closed subscheme of Projective Space of dimension 4 over Rational Field defined by:
               x^2*z - v^3,
             Closed subscheme of Projective Space of dimension 4 over Rational Field defined by:
               w^5 - 2*z^3*v^2]

        We verify that the irrelevant ideal is not accidentally returned
        (see :issue:`6920`)::

            sage: PP.<x,y,z,w> = ProjectiveSpace(3, QQ)
            sage: f = x^3 + y^3 + z^3 + w^3
            sage: R = f.parent()
            sage: I = [f] + [f.derivative(zz) for zz in PP.gens()]
            sage: V = PP.subscheme(I)
            sage: V.irreducible_components()                                            # needs sage.libs.singular
            []

        The same polynomial as above defines a scheme with a
        nontrivial irreducible component in affine space (instead of
        the empty scheme as above)::

            sage: AA.<x,y,z,w> = AffineSpace(4, QQ)
            sage: V = AA.subscheme(I)
            sage: V.irreducible_components()                                            # needs sage.libs.singular
            [Closed subscheme of Affine Space of dimension 4 over Rational Field defined by:
               w,
               z,
               y,
               x]
        """
    def is_irreducible(self):
        """
        Return whether this subscheme is or is not irreducible.

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = QuadraticField(-3)
            sage: P.<x,y,z,w,t,u> = ProjectiveSpace(K, 5)
            sage: X = P.subscheme([x*y - z^2 - K.0*t^2, t*w*x + y*z^2 - u^3])
            sage: X.is_irreducible()                                                    # needs sage.libs.singular
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme([(y + x - z)^2])
            sage: X.is_irreducible()                                                    # needs sage.libs.singular
            False

        ::

            sage: A.<x,y,z,w> = AffineSpace(GF(17), 4)
            sage: X = A.subscheme([
            ....:         x*y*z^2 - x*y*z*w - z*w^2 + w^3,
            ....:         x^3*y*z*w - x*y^3*z - x^2*y*z*w - x^2*w^3 + y^2*w^2 + x*w^3
            ....:     ])
            sage: X.is_irreducible()                                                    # needs sage.libs.singular
            False
        """
    def Jacobian_matrix(self):
        """
        Return the matrix `\\frac{\\partial f_i}{\\partial x_j}` of
        (formal) partial derivatives.

        OUTPUT: a matrix of polynomials

        EXAMPLES::

            sage: P3.<w,x,y,z> = ProjectiveSpace(3, QQ)
            sage: twisted_cubic = P3.subscheme(matrix([[w, x, y],                       # needs sage.libs.singular
            ....:                                      [x, y, z]]).minors(2))
            sage: twisted_cubic.Jacobian_matrix()                                       # needs sage.libs.singular
            [   y -2*x    w    0]
            [   z   -y   -x    w]
            [   0    z -2*y    x]

        This example addresses issue :issue:`20512`::

            sage: X = P3.subscheme([])
            sage: X.Jacobian_matrix().base_ring() == P3.coordinate_ring()               # needs sage.libs.singular
            True
        """
    def Jacobian(self):
        """
        Return the Jacobian ideal.

        This is the ideal generated by

        * the `d\\times d` minors of the Jacobian matrix, where `d` is
          the :meth:`codimension` of the algebraic scheme, and

        * the defining polynomials of the algebraic scheme. Note that
          some authors do not include these in the definition of the
          Jacobian ideal. An example of a reference that does include
          the defining equations is [Laz2004]_, p. 181.

        OUTPUT: an ideal in the coordinate ring of the ambient space

        EXAMPLES::

            sage: P3.<w,x,y,z> = ProjectiveSpace(3, QQ)
            sage: twisted_cubic = P3.subscheme(matrix([[w, x, y],                       # needs sage.libs.singular
            ....:                                      [x, y, z]]).minors(2))
            sage: twisted_cubic.Jacobian()                                              # needs sage.libs.singular
            Ideal (-x^2 + w*y, -x*y + w*z, -y^2 + x*z, x*z, -2*w*z, w*y, 3*w*y,
                   -2*w*x, w^2, y*z, -2*x*z, w*z, 3*w*z, -2*w*y, w*x, z^2, -2*y*z,
                   x*z, 3*x*z, -2*w*z, w*y)
             of Multivariate Polynomial Ring in w, x, y, z over Rational Field
            sage: twisted_cubic.defining_ideal()                                        # needs sage.libs.singular
            Ideal (-x^2 + w*y, -x*y + w*z, -y^2 + x*z)
             of Multivariate Polynomial Ring in w, x, y, z over Rational Field

        This example addresses issue :issue:`20512`::

            sage: X = P3.subscheme([])
            sage: X.Jacobian() == P3.coordinate_ring().unit_ideal()                     # needs sage.libs.singular
            True
        """
    def reduce(self):
        """
        Return the corresponding reduced algebraic space associated to this
        scheme.

        EXAMPLES: First we construct the union of a doubled and tripled
        line in the affine plane over `\\QQ` ::

            sage: A.<x,y> = AffineSpace(2, QQ)
            sage: X = A.subscheme([(x-1)^2*(x-y)^3]); X
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x^5 - 3*x^4*y + 3*x^3*y^2 - x^2*y^3 - 2*x^4 + 6*x^3*y
              - 6*x^2*y^2 + 2*x*y^3 + x^3 - 3*x^2*y + 3*x*y^2 - y^3
            sage: X.dimension()                                                         # needs sage.libs.singular
            1

        Then we compute the corresponding reduced scheme::

            sage: Y = X.reduce(); Y                                                     # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x^2 - x*y - x + y

        Finally, we verify that the reduced scheme `Y` is the union
        of those two lines::

            sage: # needs sage.libs.singular
            sage: L1 = A.subscheme([x - 1]); L1
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x - 1
            sage: L2 = A.subscheme([x - y]); L2
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x - y
            sage: W = L1.union(L2); W             # taken in ambient space
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x^2 - x*y - x + y
            sage: Y == W
            True
        """
    def union(self, other):
        '''
        Return the scheme-theoretic union of ``self`` and ``other`` in their common
        ambient space.

        EXAMPLES: We construct the union of a line and a tripled-point on
        the line.

        ::

            sage: A.<x,y> = AffineSpace(2, QQ)
            sage: I = ideal([x, y])^3
            sage: P = A.subscheme(I)
            sage: L = A.subscheme([y - 1])
            sage: S = L.union(P); S                                                     # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              y^4 - y^3,
              x*y^3 - x*y^2,
              x^2*y^2 - x^2*y,
              x^3*y - x^3
            sage: S.dimension()                                                         # needs sage.libs.singular
            1
            sage: S.reduce()                                                            # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              y^2 - y,
              x*y - x

        We can also use the notation "+" for the union::

            sage: A.subscheme([x]) + A.subscheme([y^2 - (x^3+1)])                       # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x^4 - x*y^2 + x

        Saving and loading::

            sage: loads(S.dumps()) == S                                                 # needs sage.libs.singular
            True
        '''
    def __pow__(self, m):
        """
        Return the Cartesian power of this space.

        INPUT:

        - ``m`` -- integer

        OUTPUT: subscheme of product of ambient spaces

        EXAMPLES::

            sage: P2.<y0,y1,y2> = ProjectiveSpace(ZZ, 2)
            sage: Z = P2.subscheme([y0^2 - y1*y2, y2])
            sage: Z**3
            Closed subscheme of Product of projective spaces P^2 x P^2 x P^2 over
             Integer Ring defined by:
              x0^2 - x1*x2,
              x2,
              x3^2 - x4*x5,
              x5,
              x6^2 - x7*x8,
              x8

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: V = A2.subscheme([x^2 - y, x - 1])
            sage: V**4
            Closed subscheme of Affine Space of dimension 8 over Rational Field
             defined by:
              x0^2 - x1,
              x0 - 1,
              x2^2 - x3,
              x2 - 1,
              x4^2 - x5,
              x4 - 1,
              x6^2 - x7,
              x6 - 1

            sage: T.<x0,x1,x2,x3,x4,x5> = ProductProjectiveSpaces([2,2], ZZ)
            sage: X = T.subscheme([x0*x4 - x1*x3])
            sage: X^2
            Closed subscheme of Product of projective spaces P^2 x P^2 x P^2 x P^2
             over Integer Ring defined by:
              -x1*x3 + x0*x4,
              -x7*x9 + x6*x10

            sage: E = EllipticCurve([0,0,0,0,1])                                        # needs sage.schemes
            sage: E^2                                                                   # needs sage.schemes
            Closed subscheme of Product of projective spaces P^2 x P^2
             over Rational Field defined by:
              -x0^3 + x1^2*x2 - x2^3,
              -x3^3 + x4^2*x5 - x5^3
        """
    def __mul__(self, right):
        """
        Create the product of subschemes.

        INPUT:

        - ``right`` -- a subscheme of similar type

        OUTPUT: a subscheme of a the product of the ambient spaces

        EXAMPLES::

            sage: S = ProductProjectiveSpaces([1,2,1], ZZ, 't')
            sage: T = ProductProjectiveSpaces([2,2], ZZ, 'x')
            sage: T.inject_variables()
            Defining x0, x1, x2, x3, x4, x5
            sage: X = T.subscheme([x0*x4 - x1*x3])
            sage: X*S
            Closed subscheme of
             Product of projective spaces P^2 x P^2 x P^1 x P^2 x P^1 over Integer Ring
             defined by:
              -x1*x3 + x0*x4

        ::

            sage: S = ProjectiveSpace(ZZ, 2, 't')
            sage: T.<x0,x1,x2,x3> = ProjectiveSpace(ZZ, 3)
            sage: X = T.subscheme([x0*x2 - x1*x3])
            sage: X*S
            Closed subscheme of Product of projective spaces P^3 x P^2 over Integer Ring
             defined by:
              x0*x2 - x1*x3

        ::

            sage: A2 = AffineSpace(ZZ, 2, 't')
            sage: A3.<x0,x1,x2> = AffineSpace(ZZ, 3)
            sage: X = A3.subscheme([x0*x2 - x1])
            sage: X*A2
            Closed subscheme of Affine Space of dimension 5 over Integer Ring
             defined by:
              x0*x2 - x1

        ::

            sage: T.<x0,x1,x2,x3,x4,x5> = ProductProjectiveSpaces([2,2], ZZ)
            sage: X = T.subscheme([x0*x4 - x1*x3])
            sage: X*X
            Closed subscheme of Product of projective spaces P^2 x P^2 x P^2 x P^2
             over Integer Ring defined by:
              -x1*x3 + x0*x4,
              -x7*x9 + x6*x10

        ::

            sage: P1.<z0,z1> = ProjectiveSpace(ZZ, 1)
            sage: Y = P1.subscheme([z0 - z1])
            sage: T.<x0,x1,x2,x3,x4,x5> = ProductProjectiveSpaces([2,2], ZZ)
            sage: X = T.subscheme([x0*x4 - x1*x3])
            sage: X*Y
            Closed subscheme of Product of projective spaces P^2 x P^2 x P^1
             over Integer Ring defined by:
              -x1*x3 + x0*x4,
              z0 - z1

        ::

            sage: A3.<x0,x1,x2> = AffineSpace(ZZ, 3)
            sage: X = A3.subscheme([x0*x2 - x1])
            sage: P1.<u,v> = ProjectiveSpace(ZZ, 1)
            sage: Y = P1.subscheme([u - v])
            sage: X*Y
            Traceback (most recent call last):
            ...
            TypeError: Projective Space of dimension 1 over Integer Ring must be an affine space or affine subscheme
            sage: Y*X
            Traceback (most recent call last):
            ...
            TypeError: Affine Space of dimension 3 over Integer Ring must be a projective space,
            product of projective spaces, or subscheme
            sage: PP.<a,b,c,d> = ProductProjectiveSpaces(ZZ, [1,1])
            sage: Z = PP.subscheme([a*d - b*c])
            sage: X*Z
            Traceback (most recent call last):
            ...
            TypeError: Product of projective spaces P^1 x P^1 over Integer Ring must be an affine space or affine subscheme
            sage: Z*X
            Traceback (most recent call last):
            ...
            TypeError: Affine Space of dimension 3 over Integer Ring must be a projective space,
            product of projective spaces, or subscheme
        """
    __add__ = union
    def intersection(self, other):
        """
        Return the scheme-theoretic intersection of ``self`` and ``other`` in their
        common ambient space.

        EXAMPLES::

            sage: A.<x, y> = AffineSpace(2, ZZ)
            sage: X = A.subscheme([x^2 - y])
            sage: Y = A.subscheme([y])
            sage: X.intersection(Y)
            Closed subscheme of Affine Space of dimension 2 over Integer Ring defined by:
              x^2 - y,
              y
        """
    def complement(self, other=None):
        """
        Return the scheme-theoretic complement ``other - self``, where
        ``self`` and ``other`` are both closed algebraic subschemes of the
        same ambient space.

        If ``other`` is unspecified, it is taken to be the ambient space
        of ``self``.

        EXAMPLES::

            sage: A.<x, y, z> = AffineSpace(3, ZZ)
            sage: X = A.subscheme([x + y - z])
            sage: Y = A.subscheme([x - y + z])
            sage: Y.complement(X)
            Quasi-affine subscheme X - Y of
             Affine Space of dimension 3 over Integer Ring,
             where X is defined by:
               x + y - z
             and Y is defined by:
               x - y + z
            sage: Y.complement()
            Quasi-affine subscheme X - Y of
             Affine Space of dimension 3 over Integer Ring,
             where X is defined by:
               (no polynomials)
             and Y is defined by:
               x - y + z
            sage: P.<x, y, z> = ProjectiveSpace(2, QQ)
            sage: X = P.subscheme([x^2 + y^2 + z^2])
            sage: Y = P.subscheme([x*y + y*z + z*x])
            sage: Y.complement(X)
            Quasi-projective subscheme X - Y of
             Projective Space of dimension 2 over Rational Field,
             where X is defined by:
               x^2 + y^2 + z^2
             and Y is defined by:
               x*y + x*z + y*z
            sage: Y.complement(P)
            Quasi-projective subscheme X - Y of
             Projective Space of dimension 2 over Rational Field,
             where X is defined by:
               (no polynomials)
             and Y is defined by:
               x*y + x*z + y*z
        """
    def rational_points(self, **kwds):
        """
        Return the rational points on the algebraic subscheme.

        For a dimension 0 subscheme, if the base ring is a numerical field
        such as the ComplexField the results returned could be very far from correct.
        If the polynomials defining the subscheme are defined over a number field, you
        will get better results calling rational points with `F` defined as the number
        field and the base ring as the field of definition. If the base ring
        is a number field, the embedding into ``F`` must be known.

        In the case of numerically approximated points, the points are returned over as
        points of the ambient space.

        For a dimension greater than 0 scheme, depending on bound size, either the
        points in the ambient space are enumerated or a sieving algorithm lifting points
        modulo primes is used. See the documentation in homset for the details of the
        sieving algorithm.

        INPUT: keyword arguments:

        - ``bound`` -- integer (default: 0); the bound for the coordinates for
          subschemes with dimension at least 1

        - ``prec`` -- integer (default: 53); the precision to use to
          compute the elements of bounded height for number fields

        - ``F`` -- field (default: base ring). The field to compute
          the rational points over

        - ``point_tolerance`` -- positive real number (default: 10^(-10)).
          For numerically inexact fields, two points are considered the same
          if their coordinates are within tolerance.

        - ``zero_tolerance`` -- positive real number (default: 10^(-10)).
          For numerically inexact fields, points are on the subscheme if they
          satisfy the equations to within tolerance.

        - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm
          algorithm-4

        OUTPUT: list of points in subscheme or ambient space

        .. WARNING::

           For numerically inexact fields such as ComplexField or RealField the
           list of points returned is very likely to be incomplete at best.

        EXAMPLES:

        Enumerate over a projective scheme over a number field::

            sage: # needs sage.rings.number_field
            sage: u = QQ['u'].0
            sage: K.<v> = NumberField(u^2 + 3)
            sage: A.<x,y> = ProjectiveSpace(K, 1)
            sage: X = A.subscheme(x^2 - y^2)
            sage: X.rational_points(bound=3)                                            # needs sage.libs.singular
            [(-1 : 1), (1 : 1)]

        One can enumerate points up to a given bound on a projective scheme
        over the rationals::

            sage: E = EllipticCurve('37a')                                              # needs sage.schemes
            sage: E.rational_points(bound=8)                                            # needs sage.libs.singular sage.schemes
            [(-1 : -1 : 1), (-1 : 0 : 1), (0 : -1 : 1), (0 : 0 : 1), (0 : 1 : 0),
             (1/4 : -5/8 : 1), (1/4 : -3/8 : 1), (1 : -1 : 1), (1 : 0 : 1),
             (2 : -3 : 1), (2 : 2 : 1)]

        For a small finite field, the complete set of points can be
        enumerated. ::

            sage: Etilde = E.base_extend(GF(3))                                         # needs sage.schemes
            sage: Etilde.rational_points()                                              # needs sage.libs.singular sage.schemes
            [(0 : 1 : 0), (0 : 0 : 1), (0 : 2 : 1), (1 : 0 : 1),
             (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]

        The class of hyperelliptic curves does not (yet) support
        desingularization of the places at infinity into two points::

            sage: FF = FiniteField(7)
            sage: P.<x> = PolynomialRing(FiniteField(7))
            sage: C = HyperellipticCurve(x^8 + x + 1)                                   # needs sage.schemes
            sage: C.rational_points()                                                   # needs sage.libs.singular sage.schemes
            [(0 : 1 : 0), (0 : 1 : 1), (0 : 6 : 1), (2 : 0 : 1),
             (4 : 0 : 1), (6 : 1 : 1), (6 : 6 : 1)]

        ::

            sage: # needs sage.rings.number_field sage.rings.real_mpfr
            sage: K.<v> = QuadraticField(-3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: X = P.subscheme([x^2 - v^2*x*z, y*x - v*z^2])
            sage: X.rational_points(F=CC)                                               # needs sage.libs.singular
            [(-3.00000000000000 : -0.577350269189626*I : 1.00000000000000),
             (0.000000000000000 : 1.00000000000000 : 0.000000000000000)]

        ::

            sage: # needs sage.rings.number_field sage.rings.real_mpfr
            sage: K.<v> = QuadraticField(3)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: X = A.subscheme([x^2 - v^2*y, y*x - v])
            sage: X.rational_points(F=RR)                                               # needs sage.libs.singular
            [(1.73205080756888, 1.00000000000000)]

        .. TODO::

            Implement Stoll's model in weighted projective space to
            resolve singularities and find two points (1 : 1 : 0) and
            (-1 : 1 : 0) at infinity.
        """
    def change_ring(self, R):
        """
        Return a new algebraic subscheme which is this subscheme coerced to ``R``.

        INPUT:

        - ``R`` -- ring or morphism

        OUTPUT: a new algebraic subscheme which is this subscheme coerced to ``R``

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: X = P.subscheme([3*x^2 - y^2])
            sage: H = Hom(X, X)
            sage: X.change_ring(GF(3))
            Closed subscheme of Projective Space of dimension 1
             over Finite Field of size 3 defined by: -y^2

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(2)
            sage: R.<z> = K[]
            sage: L.<v> = K.extension(z^3 - 5)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: X = P.subscheme(x - w*y)                                              # needs sage.libs.singular
            sage: X.change_ring(L)                                                      # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1 over
             Number Field in v with defining polynomial z^3 - 5 over its base field
             defined by: x + (-w)*y

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(2)
            sage: R.<z> = K[]
            sage: L.<v> = K.extension(z^3 - 5)
            sage: P.<x,y,z> = AffineSpace(L, 3)
            sage: X = P.subscheme([x - w*y, z^2 - v*x])                                 # needs sage.libs.singular
            sage: emb = L.embeddings(QQbar)                                             # needs sage.libs.singular
            sage: X.change_ring(emb[0])                                                 # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Algebraic Field
             defined by:
              x + (-1.414213562373095? + 0.?e-16*I)*y,
              z^2 + (0.8549879733383485? + 1.480882609682365?*I)*x

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(2)
            sage: R.<z> = K[]
            sage: L.<v> = K.extension(z^3 - 5)
            sage: P.<x,y,z> = AffineSpace(L, 3)
            sage: X = P.subscheme([x - w*y, z^2 - v*x])                                 # needs sage.libs.singular
            sage: emb = L.embeddings(QQbar)                                             # needs sage.libs.singular
            sage: X.change_ring(emb[1])                                                 # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Algebraic Field
             defined by:
              x + (-1.414213562373095? + 0.?e-16*I)*y,
              z^2 + (0.8549879733383485? - 1.480882609682365?*I)*x

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(-3)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: X = P.subscheme(x - w*y)                                              # needs sage.libs.singular
            sage: X.change_ring(CC)                                                     # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1
             over Complex Field with 53 bits of precision defined by:
              x + (-1.73205080756888*I)*y

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(3)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: X = P.subscheme(x - w*y)                                              # needs sage.libs.singular
            sage: X.change_ring(RR)                                                     # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1
             over Real Field with 53 bits of precision defined by:
              x - 1.73205080756888*y

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = CyclotomicField(7)
            sage: O = K.maximal_order()
            sage: P.<x,y> = ProjectiveSpace(O, 1)
            sage: X = P.subscheme([x^2 + O(v)*y^2])                                     # needs sage.libs.singular
            sage: X.change_ring(CC)                                                     # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1
             over Complex Field with 53 bits of precision defined by:
              x^2 + (0.623489801858734 + 0.781831482468030*I)*y^2
            sage: X.change_ring(K).change_ring(K.embeddings(QQbar)[3])                  # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1
             over Algebraic Field defined by:
              x^2 + (-0.9009688679024191? - 0.4338837391175581?*I)*y^2

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: f = x^6 - 2
            sage: L.<b> = NumberField(f, embedding=f.roots(CC)[2][0])
            sage: A.<x,y> = AffineSpace(L, 2)
            sage: H = Hom(A, A)
            sage: X = A.subscheme([b*x^2, y^2])                                         # needs sage.libs.singular
            sage: X.change_ring(CC)                                                     # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2
             over Complex Field with 53 bits of precision defined by:
              (-0.561231024154687 - 0.972080648619833*I)*x^2,
              y^2
        """
    def weil_restriction(self):
        """
        Compute the Weil restriction of this variety over some extension
        field. If the field is a finite field, then this computes
        the Weil restriction to the prime subfield.

        A Weil restriction of scalars - denoted `Res_{L/k}` - is a
        functor which, for any finite extension of fields `L/k` and
        any algebraic variety `X` over `L`, produces another
        corresponding variety `Res_{L/k}(X)`, defined over `k`. It is
        useful for reducing questions about varieties over large
        fields to questions about more complicated varieties over
        smaller fields.

        This function does not compute this Weil restriction directly
        but computes on generating sets of polynomial ideals:

        Let `d` be the degree of the field extension `L/k`, let `a` a
        generator of `L/k` and `p` the minimal polynomial of
        `L/k`. Denote this ideal by `I`.

        Specifically, this function first maps each variable `x` to
        its representation over `k`: `\\sum_{i=0}^{d-1} a^i x_i`. Then
        each generator of `I` is evaluated over these representations
        and reduced modulo the minimal polynomial `p`. The result is
        interpreted as a univariate polynomial in `a` and its
        coefficients are the new generators of the returned ideal.

        If the input and the output ideals are radical, this is
        equivalent to the statement about algebraic varieties above.

        OUTPUT: affine subscheme; the Weil restriction of ``self``

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^5 - 2)
            sage: R.<x> = K[]
            sage: L.<v> = K.extension(x^2 + 1)
            sage: A.<x,y> = AffineSpace(L, 2)
            sage: X = A.subscheme([y^2 - L(w)*x^3 - v])                                 # needs sage.libs.singular
            sage: X.weil_restriction()                                                  # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 4
             over Number Field in w with defining polynomial x^5 - 2 defined by:
              (-w)*z0^3 + (3*w)*z0*z1^2 + z2^2 - z3^2,
              (-3*w)*z0^2*z1 + w*z1^3 + 2*z2*z3 - 1
            sage: X.weil_restriction().ambient_space() is A.weil_restriction()          # needs sage.libs.singular
            True

        ::

            sage: A.<x,y,z> = AffineSpace(GF(5^2, 't'), 3)                              # needs sage.rings.finite_rings
            sage: X = A.subscheme([y^2 - x*z, z^2 + 2*y])                               # needs sage.libs.singular sage.rings.finite_rings
            sage: X.weil_restriction()                                                  # needs sage.libs.singular sage.rings.finite_rings
            Closed subscheme of Affine Space of dimension 6
             over Finite Field of size 5 defined by:
              z2^2 - 2*z3^2 - z0*z4 + 2*z1*z5,
              2*z2*z3 + z3^2 - z1*z4 - z0*z5 - z1*z5,
              z4^2 - 2*z5^2 + 2*z2,
              2*z4*z5 + z5^2 + 2*z3
        """
    def specialization(self, D=None, phi=None):
        """
        Specialization of this subscheme.

        Given a family of maps defined over a polynomial ring. A specialization
        is a particular member of that family. The specialization can be specified either
        by a dictionary or a :class:`SpecializationMorphism`.

        INPUT:

        - ``D`` -- dictionary (optional)

        - ``phi`` -- :class:`SpecializationMorphism` (optional)

        OUTPUT: :class:`SchemeMorphism_polynomial`

        EXAMPLES::

            sage: R.<c> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: X = P.subscheme([x^2 + c*y^2])
            sage: X.specialization(dict({c:2}))
            Closed subscheme of Projective Space of dimension 1 over Rational Field defined by:
              x^2 + 2*y^2

        ::

            sage: R.<c> = PolynomialRing(QQ)
            sage: S.<a,b> = R[]
            sage: P.<x,y,z> = AffineSpace(S, 3)
            sage: X = P.subscheme([x^2 + a*c*y^2 - b*z^2])
            sage: from sage.rings.polynomial.flatten import SpecializationMorphism
            sage: phi = SpecializationMorphism(P.coordinate_ring(),
            ....:                              dict({c: 2, a: 1}))
            sage: X.specialization(phi=phi)                                             # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 3
             over Univariate Polynomial Ring in b over Rational Field defined by:
              x^2 + 2*y^2 + (-b)*z^2
        """
