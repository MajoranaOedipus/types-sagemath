from _typeshed import Incomplete
from sage.geometry.fan import Fan as Fan
from sage.geometry.lattice_polytope import LatticePolytope as LatticePolytope
from sage.geometry.toric_lattice import ToricLattice as ToricLattice
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import identity_matrix as identity_matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.toric.fano_variety import CPRFanoToricVariety as CPRFanoToricVariety
from sage.schemes.toric.variety import DEFAULT_PREFIX as DEFAULT_PREFIX, ToricVariety as ToricVariety, normalize_names as normalize_names
from sage.structure.sage_object import SageObject as SageObject

toric_varieties_rays_cones: Incomplete

class ToricVarietyFactory(SageObject):
    """
    The methods of this class construct toric varieties.

    .. WARNING::

        You need not create instances of this class. Use the
        already-provided object ``toric_varieties`` instead.
    """
    def dP6(self, names: str = 'x u y v z w', base_ring=...):
        """
        Construct the del Pezzo surface of degree 6 (`\\mathbb{P}^2`
        blown up at 3 points) as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6(); dP6
            2-d CPR-Fano toric variety covered by 6 affine patches
            sage: dP6.fan().rays()
            N( 0,  1),        N(-1,  0),        N(-1, -1),
            N( 0, -1),        N( 1,  0),        N( 1,  1)
            in 2-d lattice N
            sage: dP6.gens()
            (x, u, y, v, z, w)
        """
    def dP7(self, names: str = 'x u y v z', base_ring=...):
        """
        Construct the del Pezzo surface of degree 7 (`\\mathbb{P}^2`
        blown up at 2 points) as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: dP7 = toric_varieties.dP7(); dP7
            2-d CPR-Fano toric variety covered by 5 affine patches
            sage: dP7.fan().rays()
            N( 0,  1),        N(-1,  0),        N(-1, -1),
            N( 0, -1),        N( 1,  0)
            in 2-d lattice N
            sage: dP7.gens()
            (x, u, y, v, z)
        """
    def dP8(self, names: str = 't x y z', base_ring=...):
        """
        Construct the del Pezzo surface of degree 8 (`\\mathbb{P}^2`
        blown up at 1 point) as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: dP8 = toric_varieties.dP8(); dP8
            2-d CPR-Fano toric variety covered by 4 affine patches
            sage: dP8.fan().rays()
            N( 1,  1),        N( 0,  1),
            N(-1, -1),        N( 1,  0)
            in 2-d lattice N
            sage: dP8.gens()
            (t, x, y, z)
        """
    def P1xP1(self, names: str = 's t x y', base_ring=...):
        """
        Construct the del Pezzo surface `\\mathbb{P}^1 \\times
        \\mathbb{P}^1` as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1(); P1xP1
            2-d CPR-Fano toric variety covered by 4 affine patches
            sage: P1xP1.fan().rays()
            N( 1,  0),        N(-1,  0),
            N( 0,  1),        N( 0, -1)
            in 2-d lattice N
            sage: P1xP1.gens()
            (s, t, x, y)
        """
    def P1xP1_Z2(self, names: str = 's t x y', base_ring=...):
        """
        Construct the toric `\\ZZ_2`-orbifold of the del Pezzo
        surface `\\mathbb{P}^1 \\times \\mathbb{P}^1` as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P1xP1_Z2 = toric_varieties.P1xP1_Z2(); P1xP1_Z2
            2-d CPR-Fano toric variety covered by 4 affine patches
            sage: P1xP1_Z2.fan().rays()
            N( 1,  1),        N(-1, -1),
            N(-1,  1),        N( 1, -1)
            in 2-d lattice N
            sage: P1xP1_Z2.gens()
            (s, t, x, y)
            sage: P1xP1_Z2.Chow_group().degree(1)
            C2 x Z^2
        """
    def P1(self, names: str = 's t', base_ring=...):
        """
        Construct the projective line `\\mathbb{P}^1` as a toric
        variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P1 = toric_varieties.P1(); P1
            1-d CPR-Fano toric variety covered by 2 affine patches
            sage: P1.fan().rays()
            N( 1),
            N(-1)
            in 1-d lattice N
            sage: P1.gens()
            (s, t)
        """
    def P2(self, names: str = 'x y z', base_ring=...):
        """
        Construct the projective plane `\\mathbb{P}^2` as a toric
        variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P2 = toric_varieties.P2(); P2
            2-d CPR-Fano toric variety covered by 3 affine patches
            sage: P2.fan().rays()
            N( 1,  0),
            N( 0,  1),
            N(-1, -1)
            in 2-d lattice N
            sage: P2.gens()
            (x, y, z)
        """
    def P(self, n, names: str = 'z+', base_ring=...):
        """
        Construct the ``n``-dimensional projective space `\\mathbb{P}^n`.

        INPUT:

        - ``n`` -- positive integer; the dimension of the projective space

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P3 = toric_varieties.P(3); P3
            3-d CPR-Fano toric variety covered by 4 affine patches
            sage: P3.fan().rays()
            N( 1,  0,  0),
            N( 0,  1,  0),
            N( 0,  0,  1),
            N(-1, -1, -1)
            in 3-d lattice N
            sage: P3.gens()
            (z0, z1, z2, z3)
        """
    def A1(self, names: str = 'z', base_ring=...):
        """
        Construct the affine line `\\mathbb{A}^1` as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: A1 = toric_varieties.A1(); A1
            1-d affine toric variety
            sage: A1.fan().rays()
            N(1)
            in 1-d lattice N
            sage: A1.gens()
            (z,)
        """
    def A2(self, names: str = 'x y', base_ring=...):
        """
        Construct the affine plane `\\mathbb{A}^2` as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: A2 = toric_varieties.A2(); A2
            2-d affine toric variety
            sage: A2.fan().rays()
            N(1, 0),
            N(0, 1)
            in 2-d lattice N
            sage: A2.gens()
            (x, y)
        """
    def A(self, n, names: str = 'z+', base_ring=...):
        """
        Construct the ``n``-dimensional affine space.

        INPUT:

        - ``n`` -- positive integer; the dimension of the affine space

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: A3 = toric_varieties.A(3); A3
            3-d affine toric variety
            sage: A3.fan().rays()
            N(1, 0, 0),
            N(0, 1, 0),
            N(0, 0, 1)
            in 3-d lattice N
            sage: A3.gens()
            (z0, z1, z2)
        """
    def A2_Z2(self, names: str = 'x y', base_ring=...):
        """
        Construct the orbifold `\\mathbb{A}^2 / \\ZZ_2` as a toric
        variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: A2_Z2 = toric_varieties.A2_Z2(); A2_Z2
            2-d affine toric variety
            sage: A2_Z2.fan().rays()
            N(1, 0),
            N(1, 2)
            in 2-d lattice N
            sage: A2_Z2.gens()
            (x, y)
        """
    def P1xA1(self, names: str = 's t z', base_ring=...):
        """
        Construct the Cartesian product `\\mathbb{P}^1 \\times \\mathbb{A}^1` as
        a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: P1xA1 = toric_varieties.P1xA1(); P1xA1
            2-d toric variety covered by 2 affine patches
            sage: P1xA1.fan().rays()
            N( 1, 0),
            N(-1, 0),
            N( 0, 1)
            in 2-d lattice N
            sage: P1xA1.gens()
            (s, t, z)
        """
    def Conifold(self, names: str = 'u x y v', base_ring=...):
        """
        Construct the conifold as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: Conifold = toric_varieties.Conifold(); Conifold
            3-d affine toric variety
            sage: Conifold.fan().rays()
            N(0, 0, 1),       N(0, 1, 1),
            N(1, 0, 1),       N(1, 1, 1)
            in 3-d lattice N
            sage: Conifold.gens()
            (u, x, y, v)
        """
    def dP6xdP6(self, names: str = 'x0 x1 x2 x3 x4 x5 y0 y1 y2 y3 y4 y5', base_ring=...):
        """
        Construct the product of two del Pezzo surfaces of degree 6
        (`\\mathbb{P}^2` blown up at 3 points) as a toric variety.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: dP6xdP6 = toric_varieties.dP6xdP6(); dP6xdP6
            4-d CPR-Fano toric variety covered by 36 affine patches
            sage: dP6xdP6.fan().rays()
            N( 0,  1,  0,  0),      N(-1,  0,  0,  0),      N(-1, -1,  0,  0),
            N( 0, -1,  0,  0),      N( 1,  0,  0,  0),      N( 1,  1,  0,  0),
            N( 0,  0,  0,  1),      N( 0,  0, -1,  0),      N( 0,  0, -1, -1),
            N( 0,  0,  0, -1),      N( 0,  0,  1,  0),      N( 0,  0,  1,  1)
            in 4-d lattice N
            sage: dP6xdP6.gens()
            (x0, x1, x2, x3, x4, x5, y0, y1, y2, y3, y4, y5)
        """
    def Cube_face_fan(self, names: str = 'z+', base_ring=...):
        """
        Construct the toric variety given by the face fan of the
        3-dimensional unit lattice cube.

        This variety has 6 conifold singularities but the fan is still
        polyhedral.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: Cube_face_fan = toric_varieties.Cube_face_fan(); Cube_face_fan
            3-d CPR-Fano toric variety covered by 6 affine patches
            sage: Cube_face_fan.fan().rays()
            N( 1,  1,  1),    N( 1, -1,  1),    N(-1,  1,  1),    N(-1, -1,  1),
            N(-1, -1, -1),    N(-1,  1, -1),    N( 1, -1, -1),    N( 1,  1, -1)
            in 3-d lattice N
            sage: Cube_face_fan.gens()
            (z0, z1, z2, z3, z4, z5, z6, z7)
        """
    def Cube_sublattice(self, names: str = 'z+', base_ring=...):
        """
        Construct the toric variety defined by a face fan over a
        3-dimensional cube, but not the unit cube in the
        N-lattice. See p. 65 of [Ful1993]_.

        Its Chow group is `A_2(X)=\\ZZ^5`, which distinguishes
        it from the face fan of the unit cube.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: Cube_sublattice = toric_varieties.Cube_sublattice(); Cube_sublattice
            3-d CPR-Fano toric variety covered by 6 affine patches
            sage: Cube_sublattice.fan().rays()
            N( 1,  0,  0),    N( 0,  1,  0),    N( 0,  0,  1),    N(-1,  1,  1),
            N(-1,  0,  0),    N( 0, -1,  0),    N( 0,  0, -1),    N( 1, -1, -1)
            in 3-d lattice N
            sage: Cube_sublattice.gens()
            (z0, z1, z2, z3, z4, z5, z6, z7)
        """
    def Cube_nonpolyhedral(self, names: str = 'z+', base_ring=...):
        """
        Construct the toric variety defined by a fan that is not the
        face fan of a polyhedron.

        This toric variety is defined by a fan that is topologically
        like the face fan of a 3-dimensional cube, but with a
        different N-lattice structure.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        .. NOTE::

            * This is an example of a non-polyhedral fan.

            * Its Chow group has torsion: `A_2(X)=\\ZZ^5 \\oplus \\ZZ_2`

        EXAMPLES::

            sage: Cube_nonpolyhedral = toric_varieties.Cube_nonpolyhedral()
            sage: Cube_nonpolyhedral
            3-d toric variety covered by 6 affine patches
            sage: Cube_nonpolyhedral.fan().rays()
            N( 1,  2,  3),    N( 1, -1,  1),    N(-1,  1,  1),    N(-1, -1,  1),
            N(-1, -1, -1),    N(-1,  1, -1),    N( 1, -1, -1),    N( 1,  1, -1)
            in 3-d lattice N
            sage: Cube_nonpolyhedral.gens()
            (z0, z1, z2, z3, z4, z5, z6, z7)
        """
    def Cube_deformation(self, k, names=None, base_ring=...):
        """
        Construct, for each `k\\in\\ZZ_{\\geq 0}`, a toric variety with
        `\\ZZ_k`-torsion in the Chow group.

        The fans of this sequence of toric varieties all equal the
        face fan of a unit cube topologically, but the
        ``(1,1,1)``-vertex is moved to ``(1,1,2k+1)``. This example
        was studied in [FS1994]_.

        INPUT:

        - ``k`` -- integer; the case ``k=0`` is the same as
          :meth:`Cube_face_fan`

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT:

        A :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`
        `X_k`. Its Chow group is `A_1(X_k)=\\ZZ_k`.

        EXAMPLES::

            sage: X_2 = toric_varieties.Cube_deformation(2); X_2
            3-d toric variety covered by 6 affine patches
            sage: X_2.fan().rays()
            N( 1,  1,  5),    N( 1, -1,  1),    N(-1,  1,  1),    N(-1, -1,  1),
            N(-1, -1, -1),    N(-1,  1, -1),    N( 1, -1, -1),    N( 1,  1, -1)
            in 3-d lattice N
            sage: X_2.gens()
            (z0, z1, z2, z3, z4, z5, z6, z7)
        """
    def BCdlOG(self, names: str = 'v1 v2 c1 c2 v4 v5 b e1 e2 e3 f g v6', base_ring=...):
        """
        Construct the 5-dimensional toric variety studied in
        [BCdlOG2000]_, [HLY2002]_

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: X = toric_varieties.BCdlOG(); X
            5-d CPR-Fano toric variety covered by 54 affine patches
            sage: X.fan().rays()
            N(-1,  0,  0,  2,  3),          N( 0, -1,  0,  2,  3),
            N( 0,  0, -1,  2,  3),          N( 0,  0, -1,  1,  2),
            N( 0,  0,  0, -1,  0),          N( 0,  0,  0,  0, -1),
            N( 0,  0,  0,  2,  3),          N( 0,  0,  1,  2,  3),
            N( 0,  0,  2,  2,  3),          N( 0,  0,  1,  1,  1),
            N( 0,  1,  2,  2,  3),          N( 0,  1,  3,  2,  3),
            N( 1,  0,  4,  2,  3)
            in 5-d lattice N
            sage: X.gens()
            (v1, v2, c1, c2, v4, v5, b, e1, e2, e3, f, g, v6)
        """
    def BCdlOG_base(self, names: str = 'd4 d3 r2 r1 d2 u d1', base_ring=...):
        """
        Construct the base of the `\\mathbb{P}^2(1,2,3)` fibration
        :meth:`BCdlOG`.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: base = toric_varieties.BCdlOG_base(); base
            3-d toric variety covered by 10 affine patches
            sage: base.fan().rays()
            N(-1,  0,  0),    N( 0, -1,  0),    N( 0,  0, -1),    N( 0,  0,  1),
            N( 0,  1,  2),    N( 0,  1,  3),    N( 1,  0,  4)
            in 3-d lattice N
            sage: base.gens()
            (d4, d3, r2, r1, d2, u, d1)
        """
    def P2_112(self, names: str = 'z+', base_ring=...):
        """
        Construct the weighted projective space
        `\\mathbb{P}^2(1,1,2)`.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P2_112 = toric_varieties.P2_112(); P2_112
            2-d CPR-Fano toric variety covered by 3 affine patches
            sage: P2_112.fan().rays()
            N( 1,  0),
            N( 0,  1),
            N(-1, -2)
            in 2-d lattice N
            sage: P2_112.gens()
            (z0, z1, z2)
        """
    def P2_123(self, names: str = 'z+', base_ring=...):
        """
        Construct the weighted projective space
        `\\mathbb{P}^2(1,2,3)`.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P2_123 = toric_varieties.P2_123(); P2_123
            2-d CPR-Fano toric variety covered by 3 affine patches
            sage: P2_123.fan().rays()
            N( 1,  0),
            N( 0,  1),
            N(-2, -3)
            in 2-d lattice N
            sage: P2_123.gens()
            (z0, z1, z2)
        """
    def P4_11169(self, names: str = 'z+', base_ring=...):
        """
        Construct the weighted projective space
        `\\mathbb{P}^4(1,1,1,6,9)`.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P4_11169 = toric_varieties.P4_11169(); P4_11169
            4-d CPR-Fano toric variety covered by 5 affine patches
            sage: P4_11169.fan().rays()
            N( 1,  0,  0,  0),      N( 0,  1,  0,  0),      N( 0,  0,  1,  0),
            N( 0,  0,  0,  1),      N(-9, -6, -1, -1)
            in 4-d lattice N
            sage: P4_11169.gens()
            (z0, z1, z2, z3, z4)
        """
    def P4_11169_resolved(self, names: str = 'z+', base_ring=...):
        """
        Construct the blow-up of the weighted projective space
        `\\mathbb{P}^4(1,1,1,6,9)` at its curve of `\\ZZ_3` orbifold
        fixed points.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P4_11169_resolved = toric_varieties.P4_11169_resolved()
            sage: P4_11169_resolved
            4-d CPR-Fano toric variety covered by 9 affine patches
            sage: P4_11169_resolved.fan().rays()
            N( 1,  0,  0,  0),      N( 0,  1,  0,  0),      N( 0,  0,  1,  0),
            N( 0,  0,  0,  1),      N(-9, -6, -1, -1),      N(-3, -2,  0,  0)
            in 4-d lattice N
            sage: P4_11169_resolved.gens()
            (z0, z1, z2, z3, z4, z5)
        """
    def P4_11133(self, names: str = 'z+', base_ring=...):
        """
        Construct the weighted projective space
        `\\mathbb{P}^4(1,1,1,3,3)`.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P4_11133 = toric_varieties.P4_11133(); P4_11133
            4-d CPR-Fano toric variety covered by 5 affine patches
            sage: P4_11133.fan().rays()
            N( 1,  0,  0,  0),      N( 0,  1,  0,  0),      N( 0,  0,  1,  0),
            N( 0,  0,  0,  1),      N(-3, -3, -1, -1)
            in 4-d lattice N
            sage: P4_11133.gens()
            (z0, z1, z2, z3, z4)
        """
    def P4_11133_resolved(self, names: str = 'z+', base_ring=...):
        """
        Construct the weighted projective space
        `\\mathbb{P}^4(1,1,1,3,3)`.

        INPUT:

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`CPR-Fano toric variety
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field>`.

        EXAMPLES::

            sage: P4_11133_resolved = toric_varieties.P4_11133_resolved()
            sage: P4_11133_resolved
            4-d CPR-Fano toric variety covered by 9 affine patches
            sage: P4_11133_resolved.fan().rays()
            N( 1,  0,  0,  0),      N( 0,  1,  0,  0),      N( 0,  0,  1,  0),
            N( 0,  0,  0,  1),      N(-3, -3, -1, -1),      N(-1, -1,  0,  0)
            in 4-d lattice N
            sage: P4_11133_resolved.gens()
            (z0, z1, z2, z3, z4, z5)
        """
    def WP(self, *q, **kw):
        """
        Construct weighted projective `n`-space over a field.

        INPUT:

        - ``q`` -- a sequence of positive integers relatively prime to
          one another. The weights ``q`` can be given either as a list
          or tuple, or as positional arguments.

        Two keyword arguments:

        - ``base_ring`` -- a field (default: `\\QQ`)

        - ``names`` -- string or list (tuple) of strings (default: ``'z+'``);
          see :func:`~sage.schemes.toric.variety.normalize_names` for
          acceptable formats.

        OUTPUT:

        - A :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>`.  If
          `q=(q_0,\\dots,q_n)`, then the output is the weighted
          projective space `\\mathbb{P}(q_0,\\dots,q_n)` over
          ``base_ring``. ``names`` are the names of the generators of
          the homogeneous coordinate ring.

        EXAMPLES:

        A hyperelliptic curve `C` of genus 2 as a subscheme of the weighted
        projective plane `\\mathbb{P}(1,3,1)`::

            sage: X = toric_varieties.WP([1,3,1], names='x y z')
            sage: X.inject_variables()
            Defining x, y, z
            sage: g = y^2 - (x^6-z^6)
            sage: C = X.subscheme([g]); C
            Closed subscheme of 2-d toric variety covered by 3 affine patches defined by:
              -x^6 + z^6 + y^2
        """
    def torus(self, n, names: str = 'z+', base_ring=...):
        """
        Construct the ``n``-dimensional algebraic torus `(\\mathbb{F}^\\times)^n`.

        INPUT:

        - ``n`` -- nonnegative integer. The dimension of the algebraic torus

        - ``names`` -- string; names for the homogeneous coordinates. See
          :func:`~sage.schemes.toric.variety.normalize_names` for acceptable
          formats.

        - ``base_ring`` -- a ring (default: `\\QQ`); the base ring for
          the toric variety

        OUTPUT: a :class:`toric variety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: T3 = toric_varieties.torus(3);  T3
            3-d affine toric variety
            sage: T3.fan().rays()
            Empty collection
            in 3-d lattice N
            sage: T3.fan().virtual_rays()
            N(1, 0, 0),
            N(0, 1, 0),
            N(0, 0, 1)
            in 3-d lattice N
            sage: T3.gens()
            (z0, z1, z2)
            sage: sorted(T3.change_ring(GF(3)).point_set().list())
            [[1 : 1 : 1], [1 : 1 : 2], [1 : 2 : 1], [1 : 2 : 2],
             [2 : 1 : 1], [2 : 1 : 2], [2 : 2 : 1], [2 : 2 : 2]]
        """

toric_varieties: Incomplete
