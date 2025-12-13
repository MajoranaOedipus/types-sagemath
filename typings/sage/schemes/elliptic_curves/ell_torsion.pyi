import sage.groups.additive_abelian.additive_abelian_wrapper as groups
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.rational_field import RationalField as RationalField
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

class EllipticCurveTorsionSubgroup(groups.AdditiveAbelianGroupWrapper):
    """
    The torsion subgroup of an elliptic curve over a number field.

    EXAMPLES:

    Examples over `\\QQ`::

        sage: E = EllipticCurve([-4, 0]); E
        Elliptic Curve defined by y^2 = x^3 - 4*x over Rational Field
        sage: G = E.torsion_subgroup(); G
        Torsion Subgroup isomorphic to Z/2 + Z/2 associated to the
         Elliptic Curve defined by y^2 = x^3 - 4*x over Rational Field
        sage: G.order()
        4
        sage: G.gen(0)
        (-2 : 0 : 1)
        sage: G.gen(1)
        (0 : 0 : 1)
        sage: G.ngens()
        2

    ::

        sage: E = EllipticCurve([17, -120, -60, 0, 0]); E
        Elliptic Curve defined by y^2 + 17*x*y - 60*y = x^3 - 120*x^2 over Rational Field
        sage: G = E.torsion_subgroup(); G
        Torsion Subgroup isomorphic to Trivial group associated to the
         Elliptic Curve defined by y^2 + 17*x*y - 60*y = x^3 - 120*x^2 over Rational Field
        sage: G.gens()
        ()
        sage: e = EllipticCurve([0, 33076156654533652066609946884, 0,
        ....:     347897536144342179642120321790729023127716119338758604800,
        ....:     1141128154369274295519023032806804247788154621049857648870032370285851781352816640000])
        sage: e.torsion_order()
        16

    Constructing points from the torsion subgroup::

        sage: E = EllipticCurve('14a1')
        sage: T = E.torsion_subgroup()
        sage: [E(t) for t in T]
        [(0 : 1 : 0),
         (9 : 23 : 1),
         (2 : 2 : 1),
         (1 : -1 : 1),
         (2 : -5 : 1),
         (9 : -33 : 1)]

    An example where the torsion subgroup is not cyclic::

        sage: E = EllipticCurve([0,0,0,-49,0])
        sage: T = E.torsion_subgroup()
        sage: [E(t) for t in T]
        [(0 : 1 : 0), (0 : 0 : 1), (-7 : 0 : 1), (7 : 0 : 1)]

    An example where the torsion subgroup is trivial::

        sage: E = EllipticCurve('37a1')
        sage: T = E.torsion_subgroup()
        sage: T
        Torsion Subgroup isomorphic to Trivial group associated to the
         Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        sage: [E(t) for t in T]
        [(0 : 1 : 0)]

    Examples over other Number Fields::

        sage: # needs sage.rings.number_field
        sage: E = EllipticCurve('11a1')
        sage: x = polygen(ZZ, 'x')
        sage: K.<i> = NumberField(x^2 + 1)
        sage: EK = E.change_ring(K)
        sage: from sage.schemes.elliptic_curves.ell_torsion import EllipticCurveTorsionSubgroup
        sage: EllipticCurveTorsionSubgroup(EK)
        Torsion Subgroup isomorphic to Z/5 associated to the
         Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
          over Number Field in i with defining polynomial x^2 + 1

        sage: E = EllipticCurve('11a1')
        sage: K.<i> = NumberField(x^2 + 1)                                              # needs sage.rings.number_field
        sage: EK = E.change_ring(K)                                                     # needs sage.rings.number_field
        sage: T = EK.torsion_subgroup()                                                 # needs sage.rings.number_field
        sage: T.ngens()
        1
        sage: T.gen(0)
        (5 : -6 : 1)

    Note: this class is normally constructed indirectly as follows::

        sage: # needs sage.rings.number_field
        sage: T = EK.torsion_subgroup(); T
        Torsion Subgroup isomorphic to Z/5 associated to the
         Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
          over Number Field in i with defining polynomial x^2 + 1
        sage: type(T)
        <class 'sage.schemes.elliptic_curves.ell_torsion.EllipticCurveTorsionSubgroup_with_category'>

    AUTHORS:

    - Nick Alexander: initial implementation over `\\QQ`.
    - Chris Wuthrich: initial implementation over number fields.
    - John Cremona: additional features and unification.
    """
    def __init__(self, E) -> None:
        """
        Initialization function for EllipticCurveTorsionSubgroup class.

        INPUT:

        - ``E`` -- an elliptic curve defined over a number field (including `\\QQ`)

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_torsion import EllipticCurveTorsionSubgroup
            sage: E = EllipticCurve('11a1')
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)                                          # needs sage.rings.number_field
            sage: EK = E.change_ring(K)                                                 # needs sage.rings.number_field
            sage: EllipticCurveTorsionSubgroup(EK)                                      # needs sage.rings.number_field
            Torsion Subgroup isomorphic to Z/5 associated to the
             Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
              over Number Field in i with defining polynomial x^2 + 1

        Note: this class is normally constructed indirectly as follows::

            sage: T = EK.torsion_subgroup(); T                                          # needs sage.rings.number_field
            Torsion Subgroup isomorphic to Z/5 associated to the
             Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
              over Number Field in i with defining polynomial x^2 + 1
            sage: type(T)                                                               # needs sage.rings.number_field
            <class 'sage.schemes.elliptic_curves.ell_torsion.EllipticCurveTorsionSubgroup_with_category'>

            sage: T == loads(dumps(T))  # known bug, see https://github.com/sagemath/sage/issues/11599#comment:7
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare two torsion groups by simply comparing the elliptic curves.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: tor = E.torsion_subgroup()
            sage: tor == tor
            True
        """
    def curve(self):
        """
        Return the curve of this torsion subgroup.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: E = EllipticCurve('11a1')
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: EK = E.change_ring(K)
            sage: T = EK.torsion_subgroup()
            sage: T.curve() is EK
            True
        """
    @cached_method
    def points(self):
        """
        Return a list of all the points in this torsion subgroup.

        The list is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: E = EllipticCurve(K, [0,0,0,1,0])
            sage: tor = E.torsion_subgroup()
            sage: tor.points()
            [(0 : 1 : 0), (0 : 0 : 1), (-i : 0 : 1), (i : 0 : 1)]
        """

def torsion_bound(E, number_of_places: int = 20):
    """
    Return an upper bound on the order of the torsion subgroup.

    INPUT:

    - ``E`` -- an elliptic curve over `\\QQ` or a number field

    - ``number_of_places`` -- positive integer (default: 20); the
      number of places that will be used to find the bound

    OUTPUT:

    (integer) An upper bound on the torsion order.

    ALGORITHM:

    An upper bound on the order of the torsion group of the elliptic
    curve is obtained by counting points modulo several primes of good
    reduction. Note that the upper bound returned by this function is
    a multiple of the order of the torsion group, and in general will
    be greater than the order.

    To avoid nontrivial arithmetic in the base field (in particular,
    to avoid having to compute the maximal order) we only use prime
    `P` above rational primes `p` which do not divide the discriminant
    of the equation order.

    EXAMPLES::

        sage: CDB = CremonaDatabase()
        sage: from sage.schemes.elliptic_curves.ell_torsion import torsion_bound
        sage: [torsion_bound(E) for E in CDB.iter([14])]
        [6, 6, 6, 6, 6, 6]
        sage: [E.torsion_order() for E in CDB.iter([14])]
        [6, 6, 2, 6, 2, 6]

    An example over a relative number field (see :issue:`16011`)::

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: F.<a> = QuadraticField(5)
        sage: K.<b> = F.extension(x^2 - 3)
        sage: E = EllipticCurve(K, [0,0,0,b,1])
        sage: E.torsion_subgroup().order()
        1

    An example of a base-change curve from `\\QQ` to a degree 16 field::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.ell_torsion import torsion_bound
        sage: f = PolynomialRing(QQ,'x')([5643417737593488384,0,
        ....:     -11114515801179776,0,-455989850911004,0,379781901872,
        ....:     0,14339154953,0,-1564048,0,-194542,0,-32,0,1])
        sage: K = NumberField(f,'a')
        sage: E = EllipticCurve(K, [1, -1, 1, 824579, 245512517])
        sage: torsion_bound(E)
        16
        sage: E.torsion_subgroup().invariants()
        (4, 4)
    """
