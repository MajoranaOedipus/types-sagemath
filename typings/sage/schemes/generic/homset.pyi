from _typeshed import Incomplete
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.homset import HomsetWithBase as HomsetWithBase
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.ring import CommutativeRing as CommutativeRing
from sage.schemes.generic.morphism import SchemeMorphism as SchemeMorphism, SchemeMorphism_spec as SchemeMorphism_spec, SchemeMorphism_structure_map as SchemeMorphism_structure_map
from sage.schemes.generic.scheme import AffineScheme as AffineScheme
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Set_generic as Set_generic

def is_SchemeHomset(H):
    """
    Test whether ``H`` is a scheme Hom-set.

    EXAMPLES::

        sage: f = Spec(QQ).identity_morphism();  f
        Scheme endomorphism of Spectrum of Rational Field
          Defn: Identity map
        sage: from sage.schemes.generic.homset import is_SchemeHomset
        sage: is_SchemeHomset(f)
        doctest:warning...
        DeprecationWarning: The function is_SchemeHomset is deprecated; use 'isinstance(..., SchemeHomset_generic)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
        sage: is_SchemeHomset(f.parent())
        True
        sage: is_SchemeHomset('a string')
        False
    """

class SchemeHomsetFactory(UniqueFactory):
    """
    Factory for Hom-sets of schemes.

    EXAMPLES::

        sage: A2 = AffineSpace(QQ, 2)
        sage: A3 = AffineSpace(QQ, 3)
        sage: Hom = A3.Hom(A2)

    The Hom-sets are uniquely determined by domain and codomain::

        sage: Hom is copy(Hom)
        True
        sage: Hom is A3.Hom(A2)
        True

    The Hom-sets are identical if the domains and codomains are
    identical::

        sage: loads(Hom.dumps()) is Hom
        True
        sage: A3_iso = AffineSpace(QQ, 3)
        sage: A3_iso is A3
        True
        sage: Hom_iso = A3_iso.Hom(A2)
        sage: Hom_iso is Hom
        True

    TESTS::

        sage: Hom.base()
        Rational Field
        sage: Hom.base_ring()
        Rational Field
    """
    def create_key_and_extra_args(self, X, Y, category=None, base=None, check: bool = True, as_point_homset: bool = False):
        """
        Create a key that uniquely determines the Hom-set.

        INPUT:

        - ``X`` -- a scheme; the domain of the morphisms

        - ``Y`` -- a scheme; the codomain of the morphisms

        - ``category`` -- a category for the Hom-sets (default: schemes over
          given base)

        - ``base`` -- a scheme or a ring; the base scheme of domain
          and codomain schemes. If a ring is specified, the spectrum
          of that ring will be used as base scheme.

        - ``check`` -- boolean (default: ``True``)

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A3 = AffineSpace(QQ, 3)
            sage: A3.Hom(A2)    # indirect doctest
            Set of morphisms
              From: Affine Space of dimension 3 over Rational Field
              To:   Affine Space of dimension 2 over Rational Field
            sage: from sage.schemes.generic.homset import SchemeHomsetFactory
            sage: SHOMfactory = SchemeHomsetFactory('test')
            sage: key, extra = SHOMfactory.create_key_and_extra_args(A3, A2, check=False)
            sage: key
            (..., ..., Category of schemes over Rational Field, False)
            sage: extra
            {'X': Affine Space of dimension 3 over Rational Field,
             'Y': Affine Space of dimension 2 over Rational Field,
             'base_ring': Rational Field,
             'check': False}
        """
    def create_object(self, version, key, **extra_args):
        """
        Create a :class:`SchemeHomset_generic`.

        INPUT:

        - ``version`` -- object version; currently not used

        - ``key`` -- a key created by :meth:`create_key_and_extra_args`

        - ``extra_args`` -- dictionary of extra keyword arguments

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A3 = AffineSpace(QQ, 3)
            sage: A3.Hom(A2) is A3.Hom(A2)   # indirect doctest
            True
            sage: from sage.schemes.generic.homset import SchemeHomsetFactory
            sage: SHOMfactory = SchemeHomsetFactory('test')
            sage: SHOMfactory.create_object(0, [id(A3), id(A2), A3.category(), False],
            ....:                           check=True, X=A3, Y=A2, base_ring=QQ)
            Set of morphisms
              From: Affine Space of dimension 3 over Rational Field
              To:   Affine Space of dimension 2 over Rational Field
        """

SchemeHomset: Incomplete

class SchemeHomset_generic(HomsetWithBase):
    """
    The base class for Hom-sets of schemes.

    INPUT:

    - ``X`` -- a scheme; the domain of the Hom-set

    - ``Y`` -- a scheme; the codomain of the Hom-set

    - ``category`` -- a category (optional); the category of the
      Hom-set

    - ``check`` -- boolean (default: ``True``); whether to
      check the defining data for consistency

    EXAMPLES::

        sage: from sage.schemes.generic.homset import SchemeHomset_generic
        sage: A2 = AffineSpace(QQ,2)
        sage: Hom = SchemeHomset_generic(A2, A2); Hom
        Set of morphisms
          From: Affine Space of dimension 2 over Rational Field
          To:   Affine Space of dimension 2 over Rational Field
        sage: Hom.category()
        Category of endsets of schemes over Rational Field
    """
    Element = SchemeMorphism
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A3 = AffineSpace(QQ, 3)
            sage: Hom = A3.Hom(A2)
            sage: loads(Hom.dumps()) == Hom
            True
        """
    def __call__(self, *args, **kwds):
        """
        Make Hom-sets callable.

        See the ``_call_()`` method of the derived class. All
        arguments are handed through.

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A2(4,5)
            (4, 5)
        """
    def natural_map(self):
        """
        Return a natural map in the Hom space.

        OUTPUT:

        A :class:`SchemeMorphism` if there is a natural map from
        domain to codomain. Otherwise, a :exc:`NotImplementedError` is raised.

        EXAMPLES::

            sage: A = AffineSpace(4, QQ)
            sage: A.structure_morphism()   # indirect doctest
            Scheme morphism:
              From: Affine Space of dimension 4 over Rational Field
              To:   Spectrum of Rational Field
              Defn: Structure map
        """

class SchemeHomset_points(SchemeHomset_generic):
    """
    Set of rational points of the scheme.

    Recall that the `K`-rational points of a scheme `X` over `k` can be
    identified with the set of morphisms `\\mathrm{Spec}(K) \\to X`. In Sage, the
    rational points are implemented by such scheme morphisms.

    If a scheme has a finite number of points, then the homset is
    supposed to implement the Python iterator interface. See
    :class:`~sage.schemes.toric.homset.SchemeHomset_points_toric_field`
    for example.

    INPUT:

    See :class:`SchemeHomset_generic`.

    EXAMPLES::

        sage: from sage.schemes.generic.homset import SchemeHomset_points
        sage: SchemeHomset_points(Spec(QQ), AffineSpace(ZZ,2))
        Set of rational points of Affine Space of dimension 2 over Rational Field
    """
    def __init__(self, X, Y, category=None, check: bool = True, base=...) -> None:
        """
        Python constructor.

        INPUT:

        See :class:`SchemeHomset_generic`.

        EXAMPLES::

            sage: from sage.schemes.generic.homset import SchemeHomset_points
            sage: SchemeHomset_points(Spec(QQ), AffineSpace(ZZ,2))
            Set of rational points of Affine Space of dimension 2 over Rational Field
        """
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: Hom = A2(QQ)
            sage: loads(Hom.dumps()) == Hom
            True
        """
    def __iter__(self):
        """
        Return an iterator for the set of rational points on this scheme.

        By default, this calls the :meth:`points` method, which is implemented
        when the base ring is a field

        - for affine homsets at :meth:`sage.schemes.affine.affine_homset.SchemeHomset_points_affine.points`;
        - for projective homsets at :meth:`sage.schemes.projective.projective_homset.SchemeHomset_points_projective_field.points`;
        - and toric homsets at :meth:`sage.schemes.toric.homset.SchemeHomset_points_toric_field._enumerator`.

        OUTPUT: iterator over points

        TESTS::

            sage: E = EllipticCurve(GF(19), [1, 0])
            sage: list(E.point_homset())
            [(0 : 1 : 0), (0 : 0 : 1), (3 : 7 : 1), (3 : 12 : 1), (4 : 7 : 1),
             (4 : 12 : 1), (5 : 4 : 1), (5 : 15 : 1), (8 : 8 : 1), (8 : 11 : 1),
             (9 : 4 : 1), (9 : 15 : 1), (12 : 7 : 1), (12 : 12 : 1), (13 : 5 : 1),
             (13 : 14 : 1), (17 : 3 : 1), (17 : 16 : 1), (18 : 6 : 1), (18 : 13 : 1)]
            sage: _ == list(E)
            True
            sage: E.point_homset().cardinality()
            20

        ::

            sage: A.<x, y> = AffineSpace(2, GF(5))
            sage: list(A.point_homset())
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
            sage: _ == list(A)
            True
            sage: A.point_homset().cardinality()
            25

        ::

            sage: P1 = toric_varieties.P1(base_ring=GF(3))
            sage: list(P1.point_homset())
            [[0 : 1], [1 : 0], [1 : 1], [1 : 2]]
            sage: P1.point_homset().cardinality()
            4
        """
    def extended_codomain(self):
        """
        Return the codomain with extended base, if necessary.

        OUTPUT:

        The codomain scheme, with its base ring extended to the
        codomain. That is, the codomain is of the form `\\mathrm{Spec}(R)` and
        the base ring of the domain is extended to `R`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P2 = ProjectiveSpace(QQ, 2)
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x - (3^3-3))
            sage: K_points = P2(K);  K_points
            Set of rational points of Projective Space of dimension 2
             over Number Field in a with defining polynomial x^2 + x - 24
            sage: K_points.codomain()
            Projective Space of dimension 2 over Rational Field
            sage: K_points.extended_codomain()
            Projective Space of dimension 2
             over Number Field in a with defining polynomial x^2 + x - 24
        """
    def zero(self):
        """
        Return the identity of the codomain with extended base, if necessary.
        """
    def value_ring(self):
        """
        Return `R` for a point Hom-set `X(\\mathrm{Spec}(R))`.

        OUTPUT: a commutative ring

        EXAMPLES::

            sage: P2 = ProjectiveSpace(ZZ, 2)
            sage: P2(QQ).value_ring()
            Rational Field
        """
    def cardinality(self):
        """
        Return the number of points.

        OUTPUT: integer or infinity

        EXAMPLES::

            sage: toric_varieties.P2().point_set().cardinality()                        # needs sage.geometry.polyhedron sage.graphs
            +Infinity

            sage: P2 = toric_varieties.P2(base_ring=GF(3))                              # needs sage.geometry.polyhedron sage.graphs
            sage: P2.point_set().cardinality()                                          # needs sage.geometry.polyhedron sage.graphs
            13
        """
    __len__ = cardinality
    def list(self):
        """
        Return a tuple containing all points.

        OUTPUT: a tuple containing all points of the toric variety

        EXAMPLES::

            sage: P1 = toric_varieties.P1(base_ring=GF(3))                              # needs sage.geometry.polyhedron sage.graphs
            sage: P1.point_set().list()                                                 # needs sage.geometry.polyhedron sage.graphs
            ([0 : 1], [1 : 0], [1 : 1], [1 : 2])
        """
