from sage.geometry.hyperplane_arrangement.arrangement import HyperplaneArrangementElement as HyperplaneArrangementElement, HyperplaneArrangements as HyperplaneArrangements
from sage.geometry.hyperplane_arrangement.hyperplane import Hyperplane as Hyperplane
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.matrix.constructor import matrix as matrix, vector as vector
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.qqbar import QQbar as QQbar
from sage.schemes.curves.plane_curve_arrangement import AffinePlaneCurveArrangements as AffinePlaneCurveArrangements, ProjectivePlaneCurveArrangements as ProjectivePlaneCurveArrangements

class OrderedHyperplaneArrangementElement(HyperplaneArrangementElement):
    """
    An ordered hyperplane arrangement.

    .. WARNING::

        You should never create
        :class:`OrderedHyperplaneArrangementElement` instances directly,
        always use the parent.
    """
    def __init__(self, parent, hyperplanes, check: bool = True, backend=None) -> None:
        """
        Construct an ordered hyperplane arrangement.

        INPUT:

        - ``parent`` -- the parent :class:`OrderedHyperplaneArrangements`

        - ``hyperplanes`` -- tuple of hyperplanes

        - ``check`` -- boolean (default: ``True``); whether
          to check input

        - ``backend`` -- string (default: ``None``); the backend to
          use for the related polyhedral objects

        EXAMPLES::

            sage: H.<x,y> = OrderedHyperplaneArrangements(QQ)
            sage: elt = H(x, y); elt
            Arrangement <x | y>
            sage: TestSuite(elt).run()
        """
    def hyperplane_section(self, proj: bool = True):
        """
        Compute a generic hyperplane section of ``self``.

        INPUT:

        - ``proj`` -- (default: ``True``) if the
          ambient space is affine or projective

        OUTPUT:

        An arrangement `\\mathcal{A}` obtained by intersecting with a
        generic hyperplane

        EXAMPLES::

            sage: L.<x, y, z> = OrderedHyperplaneArrangements(QQ)
            sage: L(x, y - 1, z).hyperplane_section()
            Traceback (most recent call last):
            ...
            TypeError: the arrangement is not projective

            sage: # needs sage.graphs
            sage: A0.<u,x,y,z> = hyperplane_arrangements.braid(4); A0
            Arrangement of 6 hyperplanes of dimension 4 and rank 3
            sage: L.<u,x,y,z> = OrderedHyperplaneArrangements(QQ)
            sage: A = L(A0)
            sage: M = A.matroid()
            sage: A1 = A.hyperplane_section()
            sage: A1
            Arrangement of 6 hyperplanes of dimension 3 and rank 3
            sage: M1 = A1.matroid()
            sage: A2 = A1.hyperplane_section(); A2
            Arrangement of 6 hyperplanes of dimension 2 and rank 2
            sage: M2 = A2.matroid()
            sage: T1 = M1.truncation()
            sage: T1.is_isomorphic(M2)
            True
            sage: T1.isomorphism(M2)
            {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

            sage: # needs sage.combinat
            sage: a0 = hyperplane_arrangements.semiorder(3); a0
            Arrangement of 6 hyperplanes of dimension 3 and rank 2
            sage: L.<t0, t1, t2> = OrderedHyperplaneArrangements(QQ)
            sage: a = L(a0)
            sage: ca = a.cone()
            sage: m = ca.matroid()
            sage: a1 = a.hyperplane_section(proj=False)
            sage: a1
            Arrangement of 6 hyperplanes of dimension 2 and rank 2
            sage: ca1 = a1.cone()
            sage: m1 = ca1.matroid()
            sage: m.isomorphism(m1)
            {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
            sage: p0 = hyperplane_arrangements.Shi(4)
            sage: L.<t0, t1, t2, t3> = OrderedHyperplaneArrangements(QQ)
            sage: p = L(p0)
            sage: a = p.hyperplane_section(proj=False); a
            Arrangement of 12 hyperplanes of dimension 3 and rank 3
            sage: ca = a.cone()
            sage: m = ca.matroid().truncation()
            sage: a1 = a.hyperplane_section(proj=False); a1
            Arrangement of 12 hyperplanes of dimension 2 and rank 2
            sage: ca1 = a1.cone()
            sage: m1 = ca1.matroid()
            sage: m1.is_isomorphism(m, {j: j for j in range(13)})
            True
        """
    def affine_fundamental_group(self):
        """
        Return the fundamental group of the complement of an affine
        hyperplane arrangement in `\\CC^n` whose equations have
        coefficients in a subfield of `\\QQbar`.

        OUTPUT: a finitely presented fundamental group

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: A.<x, y> = OrderedHyperplaneArrangements(QQ)
            sage: L = [y + x, y + x - 1]
            sage: H = A(L)
            sage: H.affine_fundamental_group()
            Finitely presented group < x0, x1 |  >
            sage: L = [x, y, x + 1, y + 1, x - y]
            sage: A(L).affine_fundamental_group()
            Finitely presented group
            < x0, x1, x2, x3, x4 | x4*x0*x4^-1*x0^-1,
                                   x0*x2*x3*x2^-1*x0^-1*x3^-1,
                                   x1*x2*x4*x2^-1*x1^-1*x4^-1,
                                   x2*x3*x0*x2^-1*x0^-1*x3^-1,
                                   x2*x4*x1*x2^-1*x1^-1*x4^-1,
                                   x4*x1*x4^-1*x3^-1*x2^-1*x1^-1*x2*x3 >
            sage: H = A(x, y, x + y)
            sage: H.affine_fundamental_group()
            Finitely presented group
            < x0, x1, x2 | x0*x1*x2*x1^-1*x0^-1*x2^-1, x1*x2*x0*x1^-1*x0^-1*x2^-1 >
            sage: H.affine_fundamental_group()  # repeat to use the attribute
            Finitely presented group
            < x0, x1, x2 | x0*x1*x2*x1^-1*x0^-1*x2^-1, x1*x2*x0*x1^-1*x0^-1*x2^-1 >
            sage: T.<t> = QQ[]
            sage: K.<a> = NumberField(t^3 + t + 1)
            sage: L.<x, y> = OrderedHyperplaneArrangements(K)
            sage: H = L(a*x + y -1, x + a*y + 1, x - 1, y - 1)
            sage: H.affine_fundamental_group()
            Traceback (most recent call last):
            ...
            TypeError: the base field is not in QQbar
            sage: L.<t> = OrderedHyperplaneArrangements(QQ)
            sage: L([t - j for j in range(4)]).affine_fundamental_group()
            Finitely presented group < x0, x1, x2, x3 |  >
            sage: L.<x, y, z> = OrderedHyperplaneArrangements(QQ)
            sage: L(L.gens() + (x + y + z + 1,)).affine_fundamental_group().sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3 | x3^-1*x2^-1*x3*x2, x3^-1*x1^-1*x3*x1,
                               x3^-1*x0^-1*x3*x0, x2^-1*x1^-1*x2*x1,
                               x2^-1*x0^-1*x2*x0, x1^-1*x0^-1*x1*x0 >
            sage: A = OrderedHyperplaneArrangements(QQ, names=())
            sage: H = A(); H
            Empty hyperplane arrangement of dimension 0
            sage: H.affine_fundamental_group()
            Finitely presented group <  |  >
        """
    def affine_meridians(self):
        """
        Return the meridians of each hyperplane (including the one at infinity).

        OUTPUT: a dictionary

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: A.<x, y> = OrderedHyperplaneArrangements(QQ)
            sage: L = [y + x, y + x - 1]
            sage: H = A(L)
            sage: g = H.affine_fundamental_group()
            sage: g
            Finitely presented group < x0, x1 |  >
            sage: H.affine_meridians()
            {0: [x0], 1: [x1], 2: [x1^-1*x0^-1]}
            sage: H1 = H.add_hyperplane(y - x)
            sage: H1.affine_meridians()
            {0: [x0], 1: [x1], 2: [x2], 3: [x2^-1*x1^-1*x0^-1]}
        """
    def projective_fundamental_group(self):
        """
        Return the fundamental group of the complement of a projective
        hyperplane arrangement.

        OUTPUT:

        The finitely presented group of the complement
        in the projective space whose equations have
        coefficients in a subfield of `\\QQbar`.

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: A.<x, y> = OrderedHyperplaneArrangements(QQ)
            sage: H = A(x, y, x + y)
            sage: H.projective_fundamental_group()
            Finitely presented group < x0, x1 |  >

            sage: # needs sirocco sage.graphs
            sage: A3.<x, y, z> = OrderedHyperplaneArrangements(QQ)
            sage: H = A3(hyperplane_arrangements.braid(4).essentialization())
            sage: G3 = H.projective_fundamental_group(); G3.sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3, x4 | x4^-1*x3^-1*x2^-1*x3*x4*x0*x2*x0^-1,
                                   x4^-1*x2^-1*x4*x2, x4^-1*x1^-1*x0^-1*x1*x4*x0,
                                   x4^-1*x1^-1*x0^-1*x4*x0*x1,
                                   x3^-1*x2^-1*x1^-1*x0^-1*x3*x0*x1*x2,
                                   x3^-1*x1^-1*x3*x1 >
            sage: G3.abelian_invariants()
            (0, 0, 0, 0, 0)
            sage: A4.<t1, t2, t3, t4> = OrderedHyperplaneArrangements(QQ)
            sage: H = A4(hyperplane_arrangements.braid(4))
            sage: G4 = H.projective_fundamental_group(); G4.sorted_presentation()
            Finitely presented group
            < x0, x1, x2, x3, x4 | x4^-1*x3^-1*x2^-1*x3*x4*x0*x2*x0^-1,
                                   x4^-1*x2^-1*x4*x2, x4^-1*x1^-1*x0^-1*x1*x4*x0,
                                   x4^-1*x1^-1*x0^-1*x4*x0*x1,
                                   x3^-1*x2^-1*x1^-1*x0^-1*x3*x0*x1*x2, x3^-1*x1^-1*x3*x1 >
            sage: G4.abelian_invariants()
            (0, 0, 0, 0, 0)

            sage: # needs sirocco
            sage: L.<t0, t1, t2, t3, t4> = OrderedHyperplaneArrangements(QQ)
            sage: H = hyperplane_arrangements.coordinate(5)
            sage: H = L(H)
            sage: g = H.projective_fundamental_group()
            sage: g.is_abelian(), g.abelian_invariants()
            (True, (0, 0, 0, 0))
            sage: L(t0, t1, t2, t3, t4, t0 - 1).projective_fundamental_group()
            Traceback (most recent call last):
            ...
            TypeError: the arrangement is not projective
            sage: T.<t> = QQ[]
            sage: K.<a> = NumberField(t^3 + t + 1)
            sage: L.<x, y, z> = OrderedHyperplaneArrangements(K)
            sage: H = L(a*x + y - z, x + a*y + z, x - z, y - z)
            sage: H.projective_fundamental_group()
            Traceback (most recent call last):
            ...
            TypeError: the base field is not in QQbar
            sage: A.<x> = OrderedHyperplaneArrangements(QQ)
            sage: H = A(); H
            Empty hyperplane arrangement of dimension 1
            sage: H.projective_fundamental_group()
            Finitely presented group <  |  >
        """
    def projective_meridians(self):
        """
        Return the meridian of each hyperplane.

        OUTPUT: a dictionary

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: A.<x, y> = OrderedHyperplaneArrangements(QQ)
            sage: H = A(x, y, x + y)
            sage: H.projective_meridians()
            {0: x0, 1: x1, 2: [x1^-1*x0^-1]}

            sage: # needs sirocco sage.graphs
            sage: A3.<x, y, z> = OrderedHyperplaneArrangements(QQ)
            sage: H = A3(hyperplane_arrangements.braid(4).essentialization())
            sage: H.projective_meridians()
            {0: [x2^-1*x0^-1*x4^-1*x3^-1*x1^-1],
             1: [x3], 2: [x4], 3: [x1], 4: [x2], 5: [x0]}
            sage: A4.<t1, t2, t3, t4> = OrderedHyperplaneArrangements(QQ)
            sage: H = A4(hyperplane_arrangements.braid(4))
            sage: H.projective_meridians()
            {0: [x2^-1*x0^-1*x4^-1*x3^-1*x1^-1], 1: [x3],
             2: [x4], 3: [x0], 4: [x2], 5: [x1]}

            sage: # needs sirocco
            sage: L.<t0, t1, t2, t3, t4> = OrderedHyperplaneArrangements(QQ)
            sage: H = hyperplane_arrangements.coordinate(5)
            sage: H = L(H)
            sage: H.projective_meridians()
            {0: [x2], 1: [x3], 2: [x0], 3: [x3^-1*x2^-1*x1^-1*x0^-1], 4: [x1]}
        """

class OrderedHyperplaneArrangements(HyperplaneArrangements):
    """
    Ordered Hyperplane arrangements.

    For more information on hyperplane arrangements, see
    :mod:`sage.geometry.hyperplane_arrangement.arrangement`.

    INPUT:

    - ``base_ring`` -- ring; the base ring

    - ``names`` -- tuple of strings; the variable names

    EXAMPLES::

        sage: H.<x,y> = HyperplaneArrangements(QQ)
        sage: x
        Hyperplane x + 0*y + 0
        sage: x + y
        Hyperplane x + y + 0
        sage: H(x, y, x-1, y-1)
        Arrangement <y - 1 | y | x - 1 | x>
    """
    Element = OrderedHyperplaneArrangementElement
