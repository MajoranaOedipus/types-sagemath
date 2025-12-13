from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.geometry.fan_morphism import FanMorphism as FanMorphism
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.homset import SchemeHomset_generic as SchemeHomset_generic, SchemeHomset_points as SchemeHomset_points
from sage.structure.element import Matrix as Matrix

class SchemeHomset_toric_variety(SchemeHomset_generic):
    """
    Set of homomorphisms between two toric varieties.

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1 = toric_varieties.P1()
        sage: hom_set = P1xP1.Hom(P1);  hom_set
        Set of morphisms
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   1-d CPR-Fano toric variety covered by 2 affine patches
        sage: type(hom_set)
        <class 'sage.schemes.toric.homset.SchemeHomset_toric_variety_with_category'>

        sage: hom_set(matrix([[1],[0]]))
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   1-d CPR-Fano toric variety covered by 2 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                to Rational polyhedral fan in 1-d lattice N.
    """
    def __init__(self, X, Y, category=None, check: bool = True, base=...) -> None:
        """
        The Python constructor.

        INPUT:

        The same as for any homset, see
        :mod:`~sage.categories.homset`.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: hom_set = P1xP1.Hom(P1);  hom_set
            Set of morphisms
              From: 2-d CPR-Fano toric variety covered by 4 affine patches
              To:   1-d CPR-Fano toric variety covered by 2 affine patches

        An integral matrix defines a fan morphism, since we think of
        the matrix as a linear map on the toric lattice. This is why
        we need to ``register_conversion`` in the constructor
        below. The result is::

            sage: hom_set(matrix([[1],[0]]))
            Scheme morphism:
              From: 2-d CPR-Fano toric variety covered by 4 affine patches
              To:   1-d CPR-Fano toric variety covered by 2 affine patches
              Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                    to Rational polyhedral fan in 1-d lattice N.
        """

class SchemeHomset_points_toric_base(SchemeHomset_points):
    """
    Base class for homsets with toric ambient spaces.

    INPUT:

    - same as for :class:`SchemeHomset_points`.

    OUTPUT: a scheme morphism of type :class:`SchemeHomset_points_toric_base`

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1xP1(QQ)
        Set of rational points of 2-d CPR-Fano toric variety
        covered by 4 affine patches

    TESTS::

        sage: import sage.schemes.toric.homset as HOM
        sage: HOM.SchemeHomset_points_toric_base(Spec(QQ), P1xP1)
        Set of rational points of 2-d CPR-Fano toric variety covered by 4 affine patches
    """
    def is_finite(self):
        """
        Return whether there are finitely many points.

        OUTPUT: boolean

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.point_set().is_finite()
            False
            sage: P2.change_ring(GF(7)).point_set().is_finite()
            True
        """

class SchemeHomset_points_toric_field(SchemeHomset_points_toric_base):
    """
    Set of rational points of a toric variety.

    You should not use this class directly. Instead, use the
    :meth:`~sage.schemes.generic.scheme.Scheme.point_set` method to
    construct the point set of a toric variety.

    INPUT:

    - same as for :class:`~sage.schemes.generic.homset.SchemeHomset_points`.

    OUTPUT: a scheme morphism of type :class:`SchemeHomset_points_toric_field`

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1xP1.point_set()
        Set of rational points of 2-d CPR-Fano toric variety
        covered by 4 affine patches
        sage: P1xP1(QQ)
        Set of rational points of 2-d CPR-Fano toric variety
        covered by 4 affine patches

    The quotient `\\mathbb{P}^2 / \\ZZ_3` over `GF(7)` by the diagonal
    action. This is tricky because the base field has a 3-rd root of
    unity::

        sage: fan = NormalFan(ReflexivePolytope(2, 0))
        sage: X = ToricVariety(fan, base_field=GF(7))
        sage: point_set = X.point_set()
        sage: point_set.cardinality()
        21
        sage: sorted(X.point_set().list())
        [[0 : 0 : 1], [0 : 1 : 0], [0 : 1 : 1], [0 : 1 : 3],
         [1 : 0 : 0], [1 : 0 : 1], [1 : 0 : 3], [1 : 1 : 0],
         [1 : 1 : 1], [1 : 1 : 2], [1 : 1 : 3], [1 : 1 : 4],
         [1 : 1 : 5], [1 : 1 : 6], [1 : 3 : 0], [1 : 3 : 1],
         [1 : 3 : 2], [1 : 3 : 3], [1 : 3 : 4], [1 : 3 : 5],
         [1 : 3 : 6]]

    As for a non-compact example, the blow-up of the plane is the line
    bundle `O_{\\mathbf{P}^1}(-1)`. Its point set is the Cartesian
    product of the points on the base `\\mathbf{P}^1` with the points
    on the fiber::

        sage: fan = Fan([Cone([(1,0), (1,1)]), Cone([(1,1), (0,1)])])
        sage: blowup_plane = ToricVariety(fan, base_ring=GF(3))
        sage: point_set = blowup_plane.point_set()
        sage: sorted(point_set.list())
        [[0 : 1 : 0], [0 : 1 : 1], [0 : 1 : 2],
         [1 : 0 : 0], [1 : 0 : 1], [1 : 0 : 2],
         [1 : 1 : 0], [1 : 1 : 1], [1 : 1 : 2],
         [1 : 2 : 0], [1 : 2 : 1], [1 : 2 : 2]]

    Toric varieties with torus factors (that is, where the fan is not
    full-dimensional) also work::

        sage: F_times_Fstar = ToricVariety(Fan([Cone([(1,0)])]), base_field=GF(3))
        sage: sorted(F_times_Fstar.point_set().list())
        [[0 : 1], [0 : 2], [1 : 1], [1 : 2], [2 : 1], [2 : 2]]

    TESTS::

        sage: import sage.schemes.toric.homset as HOM
        sage: HOM.SchemeHomset_points_toric_field(Spec(QQ), P1xP1)
        Set of rational points of 2-d CPR-Fano toric variety covered by 4 affine patches
    """
    def cardinality(self):
        '''
        Return the number of points of the toric variety.

        OUTPUT: integer or infinity; the cardinality of the set of points

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: V = ToricVariety(FaceFan(o))
            sage: V.change_ring(GF(2)).point_set().cardinality()
            27
            sage: V.change_ring(GF(8, "a")).point_set().cardinality()                   # needs sage.rings.finite_rings
            729
            sage: V.change_ring(GF(101)).point_set().cardinality()
            1061208

        For non-smooth varieties over finite fields, the homogeneous
        rescalings are solved. This is somewhat slower::

            sage: fan = NormalFan(ReflexivePolytope(2, 0))
            sage: X = ToricVariety(fan, base_field=GF(7))
            sage: X.point_set().cardinality()
            21

        Fulton\'s formula does not apply since the variety is not
        smooth. And, indeed, naive application gives a different
        result::

            sage: q = X.base_ring().order()
            sage: n = X.dimension()
            sage: d = map(len, fan().cones())
            sage: sum(dk * (q-1)**(n-k) for k, dk in enumerate(d))
            57

        Over infinite fields the number of points is not very tricky::

            sage: V.count_points()
            +Infinity

        ALGORITHM:

        Uses the formula in Fulton [Ful1993]_, section 4.5.

        AUTHORS:

        - Beth Malmskog (2013-07-14)

        - Adriana Salerno (2013-07-14)

        - Yiwei She (2013-07-14)

        - Christelle Vincent (2013-07-14)

        - Ursula Whitcher (2013-07-14)
        '''
    def __iter__(self):
        """
        Iterate over the points of the variety.

        OUTPUT: iterator over points

        EXAMPLES::

            sage: P123 = toric_varieties.P2_123(base_ring=GF(3))
            sage: point_set = P123.point_set()
            sage: next(iter(point_set.__iter__()))
            [0 : 0 : 1]
            sage: next(iter(point_set))  # syntactic sugar
            [0 : 0 : 1]
        """

class SchemeHomset_points_subscheme_toric_field(SchemeHomset_points_toric_base):
    def __iter__(self):
        """
        Iterate over the points of the variety.

        OUTPUT: iterator over points

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(5))
            sage: cubic = P2.subscheme([x^3 + y^3 + z^3])
            sage: list(cubic.point_set())
            [[0 : 1 : 4], [1 : 0 : 4], [1 : 4 : 0], [1 : 1 : 2], [1 : 2 : 1], [1 : 3 : 3]]
            sage: cubic.point_set().cardinality()
            6
        """
    def cardinality(self):
        """
        Return the number of points of the toric variety.

        OUTPUT: integer or infinity; the cardinality of the set of points

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(5))
            sage: cubic = P2.subscheme([x^3 + y^3 + z^3])
            sage: list(cubic.point_set())
            [[0 : 1 : 4], [1 : 0 : 4], [1 : 4 : 0], [1 : 1 : 2], [1 : 2 : 1], [1 : 3 : 3]]
            sage: cubic.point_set().cardinality()
            6
        """
