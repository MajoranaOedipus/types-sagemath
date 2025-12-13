from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.scheme import Scheme as Scheme

def is_AmbientSpace(x):
    """
    Return ``True`` if `x` is an ambient space.

    EXAMPLES::

        sage: from sage.schemes.generic.ambient_space import is_AmbientSpace
        sage: is_AmbientSpace(ProjectiveSpace(3, ZZ))
        doctest:warning...
        DeprecationWarning: The function is_AmbientSpace is deprecated; use 'isinstance(..., AmbientSpace)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: is_AmbientSpace(AffineSpace(2, QQ))
        True
        sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
        sage: is_AmbientSpace(P.subscheme([x + y + z]))
        False
    """

class AmbientSpace(Scheme):
    """
    Base class for ambient spaces over a ring.

    INPUT:

    - ``n`` -- dimension

    - ``R`` -- ring
    """
    def __init__(self, n, R=...) -> None:
        """
        TESTS::

            sage: from sage.schemes.generic.ambient_space import AmbientSpace
            sage: A = AmbientSpace(5, ZZ)
            sage: TestSuite(A).run() # not tested (abstract scheme with no elements?)
        """
    def change_ring(self, R) -> None:
        '''
        Return an ambient space over ring `R` and otherwise the same as ``self``.

        INPUT:

        - ``R`` -- commutative ring

        OUTPUT: ambient space over ``R``

        .. NOTE::

            There is no need to have any relation between `R` and the base ring
            of  self, if you want to have such a relation, use
            ``self.base_extend(R)`` instead.

        TESTS::

            sage: from sage.schemes.generic.ambient_space import AmbientSpace
            sage: A = AmbientSpace(5)
            sage: A.change_ring(QQ)
            Traceback (most recent call last):
            ...
            NotImplementedError: ambient spaces must override "change_ring" method!
        '''
    def is_projective(self):
        """
        Return whether this ambient space is projective n-space.

        EXAMPLES::

            sage: AffineSpace(3, QQ).is_projective()
            False
            sage: ProjectiveSpace(3, QQ).is_projective()
            True
        """
    def base_extend(self, R):
        """
        Return the natural extension of ``self`` over ``R``.

        INPUT:

        - ``R`` -- a commutative ring, such that there is a natural map from
          the base ring of ``self`` to ``R``

        OUTPUT: an ambient space over ``R`` of the same structure as ``self``

        .. NOTE::

            A :exc:`ValueError` is raised if there is no such natural map.
            If you need to drop this condition, use ``self.change_ring(R)``.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: PQ = P.base_extend(QQ); PQ
            Projective Space of dimension 2 over Rational Field
            sage: PQ.base_extend(GF(5))
            Traceback (most recent call last):
            ...
            ValueError: no natural map from the base ring (=Rational Field)
            to R (=Finite Field of size 5)!
        """
    def ambient_space(self):
        """
        Return the ambient space of the scheme self, in this case self
        itself.

        EXAMPLES::

            sage: P = ProjectiveSpace(4, ZZ)
            sage: P.ambient_space() is P
            True

            sage: A = AffineSpace(2, GF(3))
            sage: A.ambient_space()
            Affine Space of dimension 2 over Finite Field of size 3
        """
    def defining_polynomials(self):
        """
        Return the defining polynomials of the scheme ``self``.  Since
        ``self`` is an ambient space, this is an empty list.

        EXAMPLES::

            sage: ProjectiveSpace(2, QQ).defining_polynomials()
            ()
            sage: AffineSpace(0, ZZ).defining_polynomials()
            ()
        """
    def identity_morphism(self):
        """
        Return the identity morphism.

        OUTPUT: the identity morphism of the scheme ``self``

        EXAMPLES::

            sage: A = AffineSpace(2, GF(3))
            sage: A.identity_morphism()
            Scheme endomorphism of Affine Space of dimension 2 over Finite Field of size 3
              Defn: Identity map

            sage: P = ProjectiveSpace(3, ZZ)
            sage: P.identity_morphism()
            Scheme endomorphism of Projective Space of dimension 3 over Integer Ring
              Defn: Identity map
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of the coordinate ring of the
        scheme ``self``.

        EXAMPLES::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: P.gen(1)
            y
        """
    def gens(self) -> tuple:
        """
        Return the generators of the coordinate ring of the scheme
        ``self``.

        EXAMPLES::

            sage: AffineSpace(0, QQ).gens()
            ()

            sage: P.<x, y, z> = ProjectiveSpace(2, GF(5))
            sage: P.gens()
            (x, y, z)
        """
    def ngens(self):
        """
        Return the number of generators of the coordinate ring of the
        scheme ``self``.

        EXAMPLES::

            sage: AffineSpace(0, QQ).ngens()
            0

            sage: ProjectiveSpace(50, ZZ).ngens()
            51
        """
    def dimension_absolute(self):
        """
        Return the absolute dimension of this scheme.

        EXAMPLES::

            sage: A2Q = AffineSpace(2, QQ)
            sage: A2Q.dimension_absolute()
            2
            sage: A2Q.dimension()
            2
            sage: A2Z = AffineSpace(2, ZZ)
            sage: A2Z.dimension_absolute()
            3
            sage: A2Z.dimension()
            3
        """
    dimension = dimension_absolute
    def dimension_relative(self):
        """
        Return the relative dimension of this scheme over its base.

        EXAMPLES::

            sage: A2Q = AffineSpace(2, QQ)
            sage: A2Q.dimension_relative()
            2
            sage: A2Z = AffineSpace(2, ZZ)
            sage: A2Z.dimension_relative()
            2
        """
