from sage.categories.number_fields import NumberFields as NumberFields
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.morphism import SchemeMorphism as SchemeMorphism, SchemeMorphism_point as SchemeMorphism_point
from sage.structure.sequence import Sequence as Sequence

class SchemeMorphism_point_affine(SchemeMorphism_point):
    """
    A rational point on an affine scheme.

    INPUT:

    - ``X`` -- a subscheme of an ambient affine space over a ring `R`

    - ``v`` -- list/tuple/iterable of coordinates in `R`

    - ``check`` -- boolean (default: ``True``); whether to
      check the input for consistency

    EXAMPLES::

        sage: A = AffineSpace(2, QQ)
        sage: A(1, 2)
        (1, 2)
    """
    def __init__(self, X, v, check: bool = True) -> None:
        """
        The Python constructor.

        See :class:`SchemeMorphism_point_affine` for details.

        TESTS::

            sage: from sage.schemes.affine.affine_point import SchemeMorphism_point_affine
            sage: A3.<x,y,z> = AffineSpace(QQ, 3)
            sage: SchemeMorphism_point_affine(A3(QQ), [1, 2, 3])
            (1, 2, 3)
        """
    def __hash__(self):
        """
        Compute the hash value of this affine point.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: hash(A([1, 1])) == hash((1,1))
            True

        ::

            sage: A.<x,y,z> = AffineSpace(CC, 3)                                        # needs sage.rings.real_mpfr
            sage: pt = A([1, 2, -i])                                                    # needs sage.rings.real_mpfr sage.symbolic
            sage: hash(pt) == hash(tuple(pt))                                           # needs sage.rings.real_mpfr sage.symbolic
            True
        """
    def global_height(self, prec=None):
        """
        Return the logarithmic height of the point.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = AffineSpace(QQ, 2)
            sage: Q = P(41, 1/12)
            sage: Q.global_height()                                                     # needs sage.rings.real_mpfr
            3.71357206670431

        ::

            sage: P = AffineSpace(ZZ, 4, 'x')
            sage: Q = P(3, 17, -51, 5)
            sage: Q.global_height()                                                     # needs sage.rings.real_mpfr
            3.93182563272433

        ::

            sage: R.<x> = PolynomialRing(QQ)
            sage: k.<w> = NumberField(x^2 + 5)                                          # needs sage.rings.number_field
            sage: A = AffineSpace(k, 2, 'z')                                            # needs sage.rings.number_field
            sage: A([3, 5*w + 1]).global_height(prec=100)                               # needs sage.rings.number_field sage.rings.real_mpfr
            2.4181409534757389986565376694

        .. TODO::

            P-adic heights.
        """
    def homogenize(self, n):
        """
        Return the homogenization of the point at the ``nth`` coordinate.

        INPUT:

        - ``n`` -- integer between 0 and dimension of the map, inclusive

        OUTPUT: a point in the projectivization of the codomain of the map

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: Q = A(2, 3)
            sage: Q.homogenize(2).dehomogenize(2) == Q
            True

            ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: Q = A(2, 3)
            sage: P = A(0, 1)
            sage: Q.homogenize(2).codomain() == P.homogenize(2).codomain()
            True
        """

class SchemeMorphism_point_affine_field(SchemeMorphism_point_affine):
    def __hash__(self):
        """
        Compute the hash value of this affine point.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme(x - y)
            sage: hash(X([1, 1])) == hash((1,1))
            True

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme(x^2 - y^3)
            sage: pt = X([1, 1])
            sage: hash(pt) == hash(tuple(pt))
            True
        """
    def weil_restriction(self):
        """
        Compute the Weil restriction of this point over some extension
        field.

        If the field is a finite field, then this computes
        the Weil restriction to the prime subfield.

        A Weil restriction of scalars - denoted `Res_{L/k}` - is a
        functor which, for any finite extension of fields `L/k` and
        any algebraic variety `X` over `L`, produces another
        corresponding variety `Res_{L/k}(X)`, defined over `k`. It is
        useful for reducing questions about varieties over large
        fields to questions about more complicated varieties over
        smaller fields. This functor applied to a point gives
        the equivalent point on the Weil restriction of its
        codomain.

        OUTPUT: scheme point on the Weil restriction of the codomain of this point

        EXAMPLES::

            sage: # needs sage.libs.singular sage.rings.finite_rings
            sage: A.<x,y,z> = AffineSpace(GF(5^3, 't'), 3)
            sage: X = A.subscheme([y^2 - x*z, z^2 + y])
            sage: Y = X.weil_restriction()
            sage: P = X([1, -1, 1])
            sage: Q = P.weil_restriction();Q
            (1, 0, 0, 4, 0, 0, 1, 0, 0)
            sage: Q.codomain() == Y
            True

        ::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^5 - 2)
            sage: R.<x> = K[]
            sage: L.<v> = K.extension(x^2 + w)
            sage: A.<x,y> = AffineSpace(L, 2)
            sage: P = A([w^3 - v, 1 + w + w*v])
            sage: P.weil_restriction()
            (w^3, -1, w + 1, w)
        """
    def intersection_multiplicity(self, X):
        """
        Return the intersection multiplicity of the codomain of this point and ``X`` at this point.

        This uses the intersection_multiplicity implementations for projective/affine subschemes. This
        point must be a point on an affine subscheme.

        INPUT:

        - ``X`` -- a subscheme in the same ambient space as that of the codomain of this point

        OUTPUT: integer

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: A.<x,y> = AffineSpace(GF(17), 2)
            sage: X = A.subscheme([y^2 - x^3 + 2*x^2 - x])
            sage: Y = A.subscheme([y - 2*x + 2])
            sage: Q1 = Y([1,0])
            sage: Q1.intersection_multiplicity(X)
            2
            sage: Q2 = X([4,6])
            sage: Q2.intersection_multiplicity(Y)
            1

        ::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: X = A.subscheme([x^2 - y*z^2, z - 2*w^2])
            sage: Q = A([2,1,2,-1])
            sage: Q.intersection_multiplicity(X)
            Traceback (most recent call last):
            ...
            TypeError: this point must be a point on an affine subscheme
        """
    def multiplicity(self):
        """
        Return the multiplicity of this point on its codomain.

        Uses the subscheme multiplicity implementation. This point must be a point on an
        affine subscheme.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A.subscheme([y^2 - x^7*z])
            sage: Q1 = X([1,1,1])
            sage: Q1.multiplicity()                                                     # needs sage.libs.singular
            1
            sage: Q2 = X([0,0,2])
            sage: Q2.multiplicity()                                                     # needs sage.libs.singular
            2
        """
    def as_subscheme(self):
        """
        Return the subscheme associated with this rational point.

        EXAMPLES::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: p1 = A2.point([0,0]).as_subscheme(); p1
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x, y
            sage: p2 = A2.point([1,1]).as_subscheme(); p2
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x - 1, y - 1
            sage: p1 + p2
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x - y, y^2 - y
        """

class SchemeMorphism_point_affine_finite_field(SchemeMorphism_point_affine_field):
    def __hash__(self):
        """
        Return the integer hash of the point.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z> = AffineSpace(GF(5), 3)
            sage: hash(P(2, 1, 2))
            57

        ::

            sage: P.<x,y,z> = AffineSpace(GF(7), 3)
            sage: X = P.subscheme(x^2 - y^2)
            sage: hash(X(1, 1, 2))
            106

        ::

            sage: P.<x,y> = AffineSpace(GF(13), 2)
            sage: hash(P(3, 4))
            55

        ::

            sage: P.<x,y> = AffineSpace(GF(13^3, 't'), 2)                               # needs sage.rings.finite_rings
            sage: hash(P(3, 4))                                                         # needs sage.rings.finite_rings
            8791
        """
