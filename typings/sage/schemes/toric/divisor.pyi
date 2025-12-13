from sage.combinat.combination import Combinations as Combinations
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.geometry.toric_lattice_element import ToricLatticeElement as ToricLatticeElement
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import FreeModule_ambient_field as FreeModule_ambient_field, FreeModule_ambient_pid as FreeModule_ambient_pid
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.generic.divisor import Divisor_generic as Divisor_generic
from sage.schemes.generic.divisor_group import DivisorGroup_generic as DivisorGroup_generic
from sage.schemes.toric.divisor_class import ToricRationalDivisorClass as ToricRationalDivisorClass
from sage.schemes.toric.variety import CohomologyRing as CohomologyRing, ToricVariety_field as ToricVariety_field
from sage.structure.element import Vector as Vector
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_ToricDivisor(x):
    """
    Test whether ``x`` is a toric divisor.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    - ``True`` if ``x`` is an instance of :class:`ToricDivisor_generic` and
      ``False`` otherwise.

    EXAMPLES::

        sage: from sage.schemes.toric.divisor import is_ToricDivisor
        sage: is_ToricDivisor(1)
        doctest:warning...
        DeprecationWarning: The function is_ToricDivisor is deprecated;
        use 'isinstance(..., ToricDivisor_generic)' instead.
        See https://github.com/sagemath/sage/issues/38277 for details.
        False
        sage: P2 = toric_varieties.P2()
        sage: D = P2.divisor(0); D
        V(x)
        sage: is_ToricDivisor(D)
        True
    """
def ToricDivisor(toric_variety, arg=None, ring=None, check: bool = True, reduce: bool = True):
    """
    Construct a divisor of ``toric_variety``.

    INPUT:

    - ``toric_variety`` -- a :class:`toric variety
      <sage.schemes.toric.variety.ToricVariety_field>`

    - ``arg`` -- one of the following description of the toric divisor to be
      constructed:

      * ``None`` or 0 (the trivial divisor);

      * monomial in the homogeneous coordinates;

      * one-dimensional cone of the fan of ``toric_variety`` or a lattice
        point generating such a cone;

      * sequence of rational numbers, specifying multiplicities for each of
        the toric divisors.

    - ``ring`` -- usually either `\\ZZ` or `\\QQ`. The base ring of the
      divisor group. If ``ring`` is not specified, a coefficient ring
      suitable for ``arg`` is derived.

    - ``check`` -- boolean (default: ``True``); whether to coerce
      coefficients into base ring. Setting it to ``False`` can speed
      up construction.

    - ``reduce`` -- reduce (default: ``True``); whether to combine common
      terms. Setting it to ``False`` can speed up construction.

    .. WARNING::

        The coefficients of the divisor must be in the base ring and
        the terms must be reduced. If you set ``check=False`` and/or
        ``reduce=False`` it is your responsibility to pass valid input
        data ``arg``.

    OUTPUT: a :class:`sage.schemes.toric.divisor.ToricDivisor_generic`

    EXAMPLES::

        sage: from sage.schemes.toric.divisor import ToricDivisor
        sage: dP6 = toric_varieties.dP6()
        sage: ToricDivisor(dP6, [(1,dP6.gen(2)), (1,dP6.gen(1))])
        V(u) + V(y)
        sage: ToricDivisor(dP6, (0,1,1,0,0,0), ring=QQ)
        V(u) + V(y)
        sage: dP6.inject_variables()
        Defining x, u, y, v, z, w
        sage: ToricDivisor(dP6, u + y)
        Traceback (most recent call last):
        ...
        ValueError: u + y is not a monomial
        sage: ToricDivisor(dP6, u*y)
        V(u) + V(y)
        sage: ToricDivisor(dP6, dP6.fan(dim=1)[2] )
        V(y)
        sage: cone = Cone(dP6.fan(dim=1)[2])
        sage: ToricDivisor(dP6, cone)
        V(y)
        sage: N = dP6.fan().lattice()
        sage: ToricDivisor(dP6, N(1,1) )
        V(w)

    We attempt to guess the correct base ring::

        sage: ToricDivisor(dP6, [(1/2,u)])
        1/2*V(u)
        sage: _.parent()
        Group of toric QQ-Weil divisors on
        2-d CPR-Fano toric variety covered by 6 affine patches
        sage: ToricDivisor(dP6, [(1/2,u), (1/2,u)])
        V(u)
        sage: _.parent()
        Group of toric ZZ-Weil divisors on
        2-d CPR-Fano toric variety covered by 6 affine patches
        sage: ToricDivisor(dP6, [(u,u)])
        Traceback (most recent call last):
        ...
        TypeError: cannot deduce coefficient ring for [(u, u)]
    """

class ToricDivisor_generic(Divisor_generic):
    """
    Construct a :class:`(toric Weil) divisor <ToricDivisor_generic>` on the
    given toric variety.

    INPUT:

    - ``v`` -- list of tuples (multiplicity, coordinate)

    - ``parent`` -- :class:`ToricDivisorGroup`; the parent divisor group

    - ``check`` -- boolean; type-check the entries of ``v``, see
      :class:`~sage.schemes.generic.divisor_group.DivisorGroup_generic`

    - ``reduce`` -- boolean; combine coefficients in ``v``, see
      :class:`~sage.schemes.generic.divisor_group.DivisorGroup_generic`

    .. WARNING::

        Do not construct :class:`ToricDivisor_generic` objects manually.
        Instead, use either the function :func:`ToricDivisor` or the method
        :meth:`~sage.schemes.toric.variety.ToricVariety_field.divisor`
        of toric varieties.

    EXAMPLES::

        sage: dP6 = toric_varieties.dP6()
        sage: ray = dP6.fan().ray(0)
        sage: ray
        N(0, 1)
        sage: D = dP6.divisor(ray); D
        V(x)
        sage: D.parent()
        Group of toric ZZ-Weil divisors
        on 2-d CPR-Fano toric variety covered by 6 affine patches
    """
    def __init__(self, v, parent, check: bool = True, reduce: bool = True) -> None:
        """
        See :class:`ToricDivisor_generic` for documentation.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: from sage.schemes.toric.divisor import ToricDivisor_generic
            sage: TDiv = dP6.toric_divisor_group()
            sage: ToricDivisor_generic([], TDiv)
            0
            sage: ToricDivisor_generic([(2,dP6.gen(1))], TDiv)
            2*V(u)
        """
    def coefficient(self, x):
        """
        Return the coefficient of ``x``.

        INPUT:

        - ``x`` -- one of the homogeneous coordinates, either given by
          the variable or its index

        OUTPUT: the coefficient of ``x``

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: D = P2.divisor((11,12,13)); D
            11*V(x) + 12*V(y) + 13*V(z)
            sage: D.coefficient(1)
            12
            sage: P2.inject_variables()
            Defining x, y, z
            sage: D.coefficient(y)
            12
        """
    def function_value(self, point):
        """
        Return the value of the support function at ``point``.

        Let `X` be the ambient toric variety of ``self``, `\\Sigma` the fan
        associated to `X`, and `N` the ambient lattice of `\\Sigma`.

        INPUT:

        - ``point`` -- either an integer, interpreted as the index of a ray of
          `\\Sigma`, or a point of the lattice `N`

        OUTPUT: integer or a rational number

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: D = P2.divisor([11,22,44])   # total degree 77
            sage: D.function_value(0)
            11
            sage: N = P2.fan().lattice()
            sage: D.function_value( N(1,1) )
            33
            sage: D.function_value( P2.fan().ray(0) )
            11
        """
    def m(self, cone):
        """
        Return `m_\\sigma` representing `\\phi_D` on ``cone``.

        Let `X` be the ambient toric variety of this divisor `D` associated to
        the fan `\\Sigma` in lattice `N`. Let `M` be the lattice dual to `N`.
        Given the cone `\\sigma =\\langle v_1, \\dots, v_k \\rangle` in `\\Sigma`,
        this method searches for a vector `m_\\sigma \\in M_\\QQ` such that
        `\\phi_D(v_i) = \\langle m_\\sigma, v_i \\rangle` for all `i=1, \\dots, k`,
        where `\\phi_D` is the support function of `D`.

        INPUT:

        - ``cone`` -- a cone in the fan of the toric variety

        OUTPUT: if possible, a point of lattice `M`

        - If the dual vector cannot be chosen integral, a rational vector is
          returned.

        - If there is no such vector (i.e. ``self`` is not even a
          `\\QQ`-Cartier divisor), a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: F = Fan(cones=[(0,1,2,3), (0,1,4)],
            ....:         rays=[(1,1,1), (1,-1,1), (1,-1,-1), (1,1,-1), (0,0,1)])
            sage: X = ToricVariety(F)
            sage: square_cone = X.fan().cone_containing(0,1,2,3)
            sage: triangle_cone = X.fan().cone_containing(0,1,4)
            sage: ray = X.fan().cone_containing(0)
            sage: QQ_Cartier = X.divisor([2,2,1,1,1])
            sage: QQ_Cartier.m(ray)
            M(0, 2, 0)
            sage: QQ_Cartier.m(square_cone)
            (3/2, 0, 1/2)
            sage: QQ_Cartier.m(triangle_cone)
            M(1, 0, 1)
            sage: QQ_Cartier.m(Cone(triangle_cone))
            M(1, 0, 1)
            sage: Weil = X.divisor([1,1,1,0,0])
            sage: Weil.m(square_cone)
            Traceback (most recent call last):
            ...
            ValueError: V(z0) + V(z1) + V(z2) is not QQ-Cartier,
            cannot choose a dual vector on 3-d cone
            of Rational polyhedral fan in 3-d lattice N
            sage: Weil.m(triangle_cone)
            M(1, 0, 0)
        """
    def is_Weil(self):
        """
        Return whether the divisor is a Weil-divisor.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: D = P2.divisor([1,2,3])
            sage: D.is_Weil()
            True
            sage: (D/2).is_Weil()
            False
        """
    def is_QQ_Weil(self):
        """
        Return whether the divisor is a `\\QQ`-Weil-divisor.

        .. NOTE::

            This function returns always ``True`` since
            :class:`ToricDivisor <ToricDivisor_generic>` can only
            describe `\\QQ`-Weil divisors.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: D = P2.divisor([1,2,3])
            sage: D.is_QQ_Weil()
            True
            sage: (D/2).is_QQ_Weil()
            True
        """
    def is_Cartier(self):
        """
        Return whether the divisor is a Cartier-divisor.

        .. NOTE::

            The sheaf `\\mathcal{O}(D)` associated to the given divisor
            `D` is a line bundle if and only if the divisor is
            Cartier.

        EXAMPLES::

            sage: X = toric_varieties.P4_11169()
            sage: D = X.divisor(3)
            sage: D.is_Cartier()
            False
            sage: D.is_QQ_Cartier()
            True
        """
    def is_QQ_Cartier(self):
        """
        Return whether the divisor is a `\\QQ`-Cartier divisor.

        A `\\QQ`-Cartier divisor is a divisor such that some multiple
        of it is Cartier.

        EXAMPLES::

            sage: X = toric_varieties.P4_11169()
            sage: D = X.divisor(3)
            sage: D.is_QQ_Cartier()
            True

            sage: X = toric_varieties.Cube_face_fan()
            sage: D = X.divisor(3)
            sage: D.is_QQ_Cartier()
            False
        """
    def is_integral(self):
        """
        Return whether the coefficients of the divisor are all integral.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: DZZ = P2.toric_divisor_group(base_ring=ZZ).gen(0); DZZ
            V(x)
            sage: DQQ = P2.toric_divisor_group(base_ring=QQ).gen(0); DQQ
            V(x)
            sage: DZZ.is_integral()
            True
            sage: DQQ.is_integral()
            True
        """
    def move_away_from(self, cone):
        """
        Move the divisor away from the orbit closure of ``cone``.

        INPUT:

        - A ``cone`` of the fan of the toric variety.

        OUTPUT:

        A (rationally equivalent) divisor that is moved off the
        orbit closure of the given cone.

        .. NOTE::

            A divisor that is Weil but not Cartier might be impossible
            to move away. In this case, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: F = Fan(cones=[(0,1,2,3), (0,1,4)],
            ....:         rays=[(1,1,1), (1,-1,1), (1,-1,-1), (1,1,-1), (0,0,1)])
            sage: X = ToricVariety(F)
            sage: square_cone = X.fan().cone_containing(0,1,2,3)
            sage: triangle_cone = X.fan().cone_containing(0,1,4)
            sage: line_cone = square_cone.intersection(triangle_cone)
            sage: Cartier = X.divisor([2,2,1,1,1])
            sage: Cartier
            2*V(z0) + 2*V(z1) + V(z2) + V(z3) + V(z4)
            sage: Cartier.move_away_from(line_cone)
            3*V(z2) + 3*V(z3) - V(z4)
            sage: QQ_Weil = X.divisor([1,0,1,1,0])
            sage: QQ_Weil.move_away_from(line_cone)
            2*V(z2) + V(z3) - 1/2*V(z4)
        """
    def cohomology_class(self):
        """
        Return the degree-2 cohomology class associated to the divisor.

        OUTPUT:

        The corresponding cohomology class as an instance of
        :class:`~sage.schemes.toric.variety.CohomologyClass`.
        The cohomology class is the first Chern class of the
        associated line bundle `\\mathcal{O}(D)`.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: D = dP6.divisor(dP6.fan().ray(0))
            sage: D.cohomology_class()                                                  # needs sage.libs.singular
            [y + v - w]
        """
    def Chern_character(self):
        """
        Return the Chern character of the sheaf `\\mathcal{O}(D)`
        defined by the divisor `D`.

        You can also use a shortcut :meth:`ch`.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: N = dP6.fan().lattice()
            sage: D3 = dP6.divisor(dP6.fan().cone_containing( N(0,1)   ))
            sage: D5 = dP6.divisor(dP6.fan().cone_containing( N(-1,-1) ))
            sage: D6 = dP6.divisor(dP6.fan().cone_containing( N(0,-1)  ))
            sage: D = -D3 + 2*D5 - D6
            sage: D.Chern_character()                                                   # needs sage.libs.singular
            [5*w^2 + y - 2*v + w + 1]
            sage: dP6.integrate(D.ch() * dP6.Td())                                      # needs sage.libs.singular
            -4
        """
    ch = Chern_character
    def divisor_class(self):
        """
        Return the linear equivalence class of the divisor.

        OUTPUT:

        The class of the divisor in `\\mathop{Cl}(X)
        \\otimes_\\ZZ \\QQ` as an instance of
        :class:`ToricRationalDivisorClassGroup`.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: D = dP6.divisor(0)
            sage: D.divisor_class()
            Divisor class [1, 0, 0, 0]
        """
    def Chow_cycle(self, ring=...):
        """
        Return the Chow homology class of the divisor.

        INPUT:

        - ``ring`` -- either ``ZZ`` (default) or ``QQ``; the base ring
          of the Chow group

        OUTPUT:

        The :class:`~sage.schemes.toric.chow_group.ChowCycle`
        represented by the divisor.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: cone = dP6.fan(1)[5]
            sage: D = dP6.divisor(cone); D
            V(w)
            sage: D.Chow_cycle()
            ( 0 | -1, 0, 1, 1 | 0 )
            sage: dP6.Chow_group()(cone)
            ( 0 | -1, 0, 1, 1 | 0 )
        """
    def is_ample(self):
        """
        Return whether a `\\QQ`-Cartier divisor is ample.

        OUTPUT: ``True`` if the divisor is in the ample cone, ``False`` otherwise

        .. NOTE::

            * For a `\\QQ`-Cartier divisor, some positive integral
              multiple is Cartier. We return whether this associated
              divisor is ample, i.e. corresponds to an ample line bundle.

            * In the orbifold case, the ample cone is an open
              and full-dimensional cone in the rational divisor class
              group :class:`ToricRationalDivisorClassGroup`.

            * If the variety has worse than orbifold singularities,
              the ample cone is a full-dimensional cone within the
              (not full-dimensional) subspace spanned by the Cartier
              divisors inside the rational (Weil) divisor class group,
              that is, :class:`ToricRationalDivisorClassGroup`. The
              ample cone is then relative open (open in this
              subspace).

            * See also :meth:`is_nef`.

            * A toric divisor is ample if and only if its support
              function is strictly convex.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: K = P2.K()
            sage: (+K).is_ample()
            False
            sage: (0*K).is_ample()
            False
            sage: (-K).is_ample()
            True

        Example 6.1.3, 6.1.11, 6.1.17 of [CLS2011]_::

            sage: from itertools import product
            sage: fan = Fan(cones=[(0,1), (1,2), (2,3), (3,0)],
            ....:           rays=[(-1,2), (0,1), (1,0), (0,-1)])
            sage: F2 = ToricVariety(fan,'u1, u2, u3, u4')
            sage: def D(a, b): return a*F2.divisor(2) + b*F2.divisor(3)
            sage: [ (a,b) for a,b in product(range(-3,3), repeat=2)
            ....:         if D(a,b).is_ample() ]
            [(1, 1), (1, 2), (2, 1), (2, 2)]
            sage: [ (a,b) for a,b in product(range(-3,3), repeat=2)
            ....:         if D(a,b).is_nef() ]
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        A (worse than orbifold) singular Fano threefold::

            sage: points = [(1,0,0),(0,1,0),(0,0,1),(-2,0,-1),(-2,-1,0),(-3,-1,-1),(1,1,1)]
            sage: facets = [[0,1,3],[0,1,6],[0,2,4],[0,2,6],[0,3,5],[0,4,5],[1,2,3,4,5,6]]
            sage: X = ToricVariety(Fan(cones=facets, rays=points))
            sage: X.rational_class_group().dimension()
            4
            sage: X.Kaehler_cone().rays()
            Divisor class [1, 0, 0, 0]
            in Basis lattice of The toric rational divisor class group
            of a 3-d toric variety covered by 7 affine patches
            sage: antiK = -X.K()
            sage: antiK.divisor_class()
            Divisor class [2, 0, 0, 0]
            sage: antiK.is_ample()
            True
        """
    def is_nef(self):
        """
        Return whether a `\\QQ`-Cartier divisor is nef.

        OUTPUT:

        - ``True`` if the divisor is in the closure of the ample cone,
          ``False`` otherwise.

        .. NOTE::

            * For a `\\QQ`-Cartier divisor, some positive integral multiple is
              Cartier. We return whether this associated divisor is nef.

            * The nef cone is the closure of the ample cone.

            * See also :meth:`is_ample`.

            * A toric divisor is nef if and only if its support
              function is convex (but not necessarily strictly
              convex).

            * A toric Cartier divisor is nef if and only if its linear
              system is basepoint free.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: K = P2.K()
            sage: (+K).is_nef()
            False
            sage: (0*K).is_nef()
            True
            sage: (-K).is_nef()
            True

        Example 6.1.3, 6.1.11, 6.1.17 of [CLS2011]_::

            sage: from itertools import product
            sage: fan = Fan(cones=[(0,1), (1,2), (2,3), (3,0)],
            ....:           rays=[(-1,2), (0,1), (1,0), (0,-1)])
            sage: F2 = ToricVariety(fan,'u1, u2, u3, u4')
            sage: def D(a, b): return a*F2.divisor(2) + b*F2.divisor(3)
            sage: [ (a,b) for a,b in product(range(-3,3), repeat=2)
            ....:         if D(a,b).is_ample() ]
            [(1, 1), (1, 2), (2, 1), (2, 2)]
            sage: [ (a,b) for a,b in product(range(-3,3), repeat=2)
            ....:         if D(a,b).is_nef() ]
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        """
    def polyhedron(self):
        """
        Return the polyhedron `P_D\\subset M` associated to a toric
        divisor `D`.

        OUTPUT: `P_D` as an instance of :class:`~sage.geometry.polyhedron.base.Polyhedron_base`

        EXAMPLES::

            sage: dP7 = toric_varieties.dP7()
            sage: D = dP7.divisor(2)
            sage: P_D = D.polyhedron(); P_D
            A 0-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: P_D.Vrepresentation()
            (A vertex at (0, 0),)
            sage: D.is_nef()
            False
            sage: dP7.integrate(D.ch() * dP7.Td())                                      # needs sage.libs.singular
            1
            sage: P_antiK = (-dP7.K()).polyhedron(); P_antiK
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices
            sage: P_antiK.Vrepresentation()
            (A vertex at (1, -1), A vertex at (0, 1), A vertex at (1, 0),
             A vertex at (-1, 1), A vertex at (-1, -1))
            sage: P_antiK.integral_points()
            ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0))

        Example 6.1.3, 6.1.11, 6.1.17 of [CLS2011]_::

            sage: fan = Fan(cones=[(0,1), (1,2), (2,3), (3,0)],
            ....:           rays=[(-1,2), (0,1), (1,0), (0,-1)])
            sage: F2 = ToricVariety(fan,'u1, u2, u3, u4')
            sage: D = F2.divisor(3)
            sage: D.polyhedron().Vrepresentation()
            (A vertex at (0, 0), A vertex at (2, 1), A vertex at (0, 1))
            sage: Dprime = F2.divisor(1) + D
            sage: Dprime.polyhedron().Vrepresentation()
            (A vertex at (2, 1), A vertex at (0, 1), A vertex at (0, 0))
            sage: D.is_ample()
            False
            sage: D.is_nef()
            True
            sage: Dprime.is_nef()
            False

        A more complicated example where `P_D` is not a lattice polytope::

            sage: X = toric_varieties.BCdlOG_base()
            sage: antiK = -X.K()
            sage: P_D = antiK.polyhedron()
            sage: P_D
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 8 vertices
            sage: P_D.Vrepresentation()
            (A vertex at (1, -1, 0), A vertex at (1, -3, 1),
             A vertex at (1, 1, 1), A vertex at (-5, 1, 1),
             A vertex at (1, 1, -1/2), A vertex at (1, 1/2, -1/2),
             A vertex at (-1, -1, 0), A vertex at (-5, -3, 1))
            sage: P_D.Hrepresentation()
            (An inequality (-1, 0, 0) x + 1 >= 0, An inequality (0, -1, 0) x + 1 >= 0,
             An inequality (0, 0, -1) x + 1 >= 0, An inequality (1, 0, 4) x + 1 >= 0,
             An inequality (0, 1, 3) x + 1 >= 0, An inequality (0, 1, 2) x + 1 >= 0)
            sage: P_D.integral_points()
            ((-1, -1, 0), (0, -1, 0), (1, -1, 0), (-1, 0, 0), (0, 0, 0),
             (1, 0, 0), (-1, 1, 0), (0, 1, 0), (1, 1, 0), (-5, -3, 1),
             (-4, -3, 1), (-3, -3, 1), (-2, -3, 1), (-1, -3, 1), (0, -3, 1),
             (1, -3, 1), (-5, -2, 1), (-4, -2, 1), (-3, -2, 1), (-2, -2, 1),
             (-1, -2, 1), (0, -2, 1), (1, -2, 1), (-5, -1, 1), (-4, -1, 1),
             (-3, -1, 1), (-2, -1, 1), (-1, -1, 1), (0, -1, 1), (1, -1, 1),
             (-5, 0, 1), (-4, 0, 1), (-3, 0, 1), (-2, 0, 1), (-1, 0, 1),
             (0, 0, 1), (1, 0, 1), (-5, 1, 1), (-4, 1, 1), (-3, 1, 1),
             (-2, 1, 1), (-1, 1, 1), (0, 1, 1), (1, 1, 1))
        """
    def sections(self):
        """
        Return the global sections (as points of the `M`-lattice) of
        the line bundle (or reflexive sheaf) associated to the
        divisor.

        OUTPUT: a :class:`tuple` of points of lattice `M`

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.fan().nrays()
            3
            sage: P2.divisor(0).sections()
            (M(-1, 0), M(-1, 1), M(0, 0))
            sage: P2.divisor(1).sections()
            (M(0, -1), M(0, 0), M(1, -1))
            sage: P2.divisor(2).sections()
            (M(0, 0), M(0, 1), M(1, 0))

        The divisor can be non-nef yet still have sections::

            sage: rays = [(1,0,0),(0,1,0),(0,0,1),(-2,0,-1),(-2,-1,0),(-3,-1,-1),(1,1,1),(-1,0,0)]
            sage: cones = [[0,1,3],[0,1,6],[0,2,4],[0,2,6],[0,3,5],[0,4,5],[1,3,7],[1,6,7],[2,4,7],[2,6,7],[3,5,7],[4,5,7]]
            sage: X = ToricVariety(Fan(rays=rays, cones=cones))
            sage: D = X.divisor(2); D
            V(z2)
            sage: D.is_nef()
            False
            sage: D.sections()
            (M(0, 0, 0),)
            sage: D.cohomology(dim=True)
            (1, 0, 0, 0)
        """
    def sections_monomials(self):
        """
        Return the global sections of the line bundle associated to the
        Cartier divisor.

        The sections are described as monomials in the generalized homogeneous
        coordinates.

        OUTPUT: tuple of monomials in the coordinate ring of ``self``

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.fan().nrays()
            3
            sage: P2.divisor(0).sections_monomials()
            (z, y, x)
            sage: P2.divisor(1).sections_monomials()
            (z, y, x)
            sage: P2.divisor(2).sections_monomials()
            (z, y, x)

        From [Cox]_ page 38::

            sage: lp = LatticePolytope([(1,0), (1,1), (0,1), (-1,0), (0,-1)])
            sage: lp
            2-d reflexive polytope #5 in 2-d lattice M
            sage: dP7 = ToricVariety(FaceFan(lp), 'x1, x2, x3, x4, x5')
            sage: AK = -dP7.K()
            sage: AK.sections()
            (N(-1, 0), N(-1, 1), N(0, -1), N(0, 0),
             N(0, 1), N(1, -1), N(1, 0), N(1, 1))
            sage: AK.sections_monomials()
            (x3*x4^2*x5, x2*x3^2*x4^2, x1*x4*x5^2, x1*x2*x3*x4*x5,
             x1*x2^2*x3^2*x4, x1^2*x2*x5^2, x1^2*x2^2*x3*x5, x1^2*x2^3*x3^2)
        """
    def monomial(self, point):
        """
        Return the monomial in the homogeneous coordinate ring
        associated to the ``point`` in the dual lattice.

        INPUT:

        - ``point`` -- a point in ``self.variety().fan().dual_lattice()``

        OUTPUT:

        For a fixed divisor ``D``, the sections are generated by
        monomials in :meth:`ToricVariety.coordinate_ring
        <sage.schemes.toric.variety.ToricVariety_field.coordinate_ring>`.
        Alternatively, the monomials can be described as `M`-lattice
        points in the polyhedron ``D.polyhedron()``. This method
        converts the points `m\\in M` into homogeneous polynomials.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: O3_P2 = -P2.K()
            sage: M = P2.fan().dual_lattice()
            sage: O3_P2.monomial( M(0,0) )
            x*y*z
        """
    def Kodaira_map(self, names: str = 'z'):
        """
        Return the Kodaira map.

        The Kodaira map is the rational map `X_\\Sigma \\to
        \\mathbb{P}^{n-1}`, where `n` equals the number of sections. It
        is defined by the monomial sections of the line bundle.

        If the divisor is ample and the toric variety smooth or of
        dimension 2, then this is an embedding.

        INPUT:

        - ``names`` -- string (default: ``'z'``); the
          variable names for the destination projective space

        EXAMPLES::

            sage: P1.<u,v> = toric_varieties.P1()
            sage: D = -P1.K()
            sage: D.Kodaira_map()                                                       # needs fpylll sage.libs.singular
            Scheme morphism:
              From: 1-d CPR-Fano toric variety covered by 2 affine patches
              To:   Closed subscheme of Projective Space of dimension 2
                    over Rational Field defined by: -z1^2 + z0*z2
              Defn: Defined on coordinates by sending [u : v] to (v^2 : u*v : u^2)

            sage: dP6 = toric_varieties.dP6()
            sage: D = -dP6.K()
            sage: D.Kodaira_map(names='x')                                              # needs fpylll sage.libs.singular
            Scheme morphism:
              From: 2-d CPR-Fano toric variety covered by 6 affine patches
              To:   Closed subscheme of Projective Space of dimension 6
                    over Rational Field defined by:
                      -x1*x5 + x0*x6,       -x2*x3 + x0*x5,       -x1*x3 + x0*x4,
                      x4*x5 - x3*x6,        -x1*x2 + x0*x3,       x3*x5 - x2*x6,
                      x3*x4 - x1*x6,        x3^2 - x1*x5,         x2*x4 - x1*x5,
                      -x1*x5^2 + x2*x3*x6, -x1*x5^3 + x2^2*x6^2
              Defn: Defined on coordinates by sending [x : u : y : v : z : w] to
                    (x*u^2*y^2*v : x^2*u^2*y*w : u*y^2*v^2*z : x*u*y*v*z*w :
                     x^2*u*z*w^2 : y*v^2*z^2*w : x*v*z^2*w^2)
        """
    def cohomology(self, weight=None, deg=None, dim: bool = False):
        '''
        Return the cohomology of the line bundle associated to the
        Cartier divisor or reflexive sheaf associated to the Weil
        divisor.

        .. NOTE::

            The cohomology of a toric line bundle/reflexive sheaf is
            graded by the usual degree as well as by the `M`-lattice.

        INPUT:

        - ``weight`` -- (optional) a point of the `M`-lattice

        - ``deg`` -- (optional) the degree of the cohomology group

        - ``dim`` -- boolean; if ``False`` (default), the cohomology
          groups are returned as vector spaces. If ``True``, only the
          dimension of the vector space(s) is returned.

        OUTPUT:

        The vector space `H^\\text{deg}(X,\\mathcal{O}(D))` (if ``deg``
        is specified) or a dictionary ``{degree:cohomology(degree)}``
        of all degrees between 0 and the dimension of the variety.

        If ``weight`` is specified, return only the subspace
        `H^\\text{deg}(X,\\mathcal{O}(D))_\\text{weight}` of the
        cohomology of the given weight.

        If ``dim==True``, the dimension of the cohomology vector space
        is returned instead of actual vector space. Moreover, if
        ``deg`` was not specified, a vector whose entries are the
        dimensions is returned instead of a dictionary.

        ALGORITHM:

        Roughly, Chech cohomology is used to compute the
        cohomology. For toric divisors, the local sections can be
        chosen to be monomials (instead of general homogeneous
        polynomials), this is the reason for the extra grading by
        `m\\in M`. General references would be [Ful1993]_, [CLS2011]_. Here
        are some salient features of our implementation:

        * First, a finite set of `M`-lattice points is identified that
          supports the cohomology. The toric divisor determines a
          (polyhedral) chamber decomposition of `M_\\RR`, see Section
          9.1 and Figure 4 of [CLS2011]_. The cohomology vanishes on the
          non-compact chambers. Hence, the convex hull of the vertices
          of the chamber decomposition contains all non-vanishing
          cohomology groups. This is returned by the private method
          :meth:`_sheaf_cohomology_support`.

          It would be more efficient, but more difficult to implement,
          to keep track of all of the individual chambers. We leave
          this for future work.

        * For each point `m\\in M`, the weight-`m` part of the
          cohomology can be rewritten as the cohomology of a
          simplicial complex, see Exercise 9.1.10 of [CLS2011]_,
          [Per2007]_. This is returned by the private method
          :meth:`_sheaf_complex`.

          The simplicial complex is the same for all points in a
          chamber, but we currently do not make use of this and
          compute each point `m\\in M` separately.

        * Finally, the cohomology (over `\\QQ`) of this simplicial
          complex is computed in the private method
          :meth:`_sheaf_cohomology`. Summing over the supporting
          points `m\\in M` yields the cohomology of the sheaf`.

        EXAMPLES:

        Example 9.1.7 of Cox, Little, Schenck: "Toric Varieties" [CLS2011]_::

            sage: F = Fan(cones=[(0,1), (1,2), (2,3), (3,4), (4,5), (5,0)],
            ....:         rays=[(1,0), (1,1), (0,1), (-1,0), (-1,-1), (0,-1)])
            sage: dP6 = ToricVariety(F)
            sage: D3 = dP6.divisor(2)
            sage: D5 = dP6.divisor(4)
            sage: D6 = dP6.divisor(5)
            sage: D = -D3 + 2*D5 - D6
            sage: D.cohomology()
            {0: Vector space of dimension 0 over Rational Field,
             1: Vector space of dimension 4 over Rational Field,
             2: Vector space of dimension 0 over Rational Field}
            sage: D.cohomology(deg=1)
            Vector space of dimension 4 over Rational Field
            sage: M = F.dual_lattice()
            sage: D.cohomology( M(0,0) )
            {0: Vector space of dimension 0 over Rational Field,
             1: Vector space of dimension 1 over Rational Field,
             2: Vector space of dimension 0 over Rational Field}
            sage: D.cohomology( weight=M(0,0), deg=1 )
            Vector space of dimension 1 over Rational Field
            sage: dP6.integrate(D.ch() * dP6.Td())                                      # needs sage.libs.singular
            -4

        Note the different output options::

            sage: D.cohomology()
            {0: Vector space of dimension 0 over Rational Field,
             1: Vector space of dimension 4 over Rational Field,
             2: Vector space of dimension 0 over Rational Field}
            sage: D.cohomology(dim=True)
            (0, 4, 0)
            sage: D.cohomology(weight=M(0,0))
            {0: Vector space of dimension 0 over Rational Field,
             1: Vector space of dimension 1 over Rational Field,
             2: Vector space of dimension 0 over Rational Field}
            sage: D.cohomology(weight=M(0,0), dim=True)
            (0, 1, 0)
            sage: D.cohomology(deg=1)
            Vector space of dimension 4 over Rational Field
            sage: D.cohomology(deg=1, dim=True)
            4
            sage: D.cohomology(weight=M(0,0), deg=1)
            Vector space of dimension 1 over Rational Field
            sage: D.cohomology(weight=M(0,0), deg=1, dim=True)
            1

        Here is a Weil (non-Cartier) divisor example::

            sage: K = toric_varieties.Cube_nonpolyhedral().K()
            sage: K.is_Weil()
            True
            sage: K.is_QQ_Cartier()
            False
            sage: K.cohomology(dim=True)
            (0, 0, 0, 1)
        '''
    def cohomology_support(self):
        """
        Return the weights for which the cohomology groups do not vanish.

        OUTPUT:

        A tuple of dual lattice points. ``self.cohomology(weight=m)``
        does not vanish if and only if ``m`` is in the output.

        .. NOTE::

            This method is provided for educational purposes and it is
            not an efficient way of computing the cohomology groups.

        EXAMPLES::

            sage: F = Fan(cones=[(0,1), (1,2), (2,3), (3,4), (4,5), (5,0)],
            ....:         rays=[(1,0), (1,1), (0,1), (-1,0), (-1,-1), (0,-1)])
            sage: dP6 = ToricVariety(F)
            sage: D3 = dP6.divisor(2)
            sage: D5 = dP6.divisor(4)
            sage: D6 = dP6.divisor(5)
            sage: D = -D3 + 2*D5 - D6
            sage: D.cohomology_support()
            (M(0, 0), M(1, 0), M(2, 0), M(1, 1))
        """

class ToricDivisorGroup(DivisorGroup_generic):
    """
    The group of (`\\QQ`-T-Weil) divisors on a toric variety.

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: P2.toric_divisor_group()
        Group of toric ZZ-Weil divisors
        on 2-d CPR-Fano toric variety covered by 3 affine patches
    """
    def __init__(self, toric_variety, base_ring) -> None:
        """
        Construct an instance of :class:`ToricDivisorGroup`.

        INPUT:

        - ``toric_variety`` -- a
          :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>``

        - ``base_ring`` -- the coefficient ring of this divisor group,
          usually `\\ZZ` (default) or `\\QQ`

        Implementation note: :meth:`__classcall__` sets the default
        value for ``base_ring``.

        OUTPUT: divisor group of the toric variety

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: from sage.schemes.toric.divisor import ToricDivisorGroup
            sage: ToricDivisorGroup(P2, base_ring=ZZ)
            Group of toric ZZ-Weil divisors
            on 2-d CPR-Fano toric variety covered by 3 affine patches

        Note that :class:`UniqueRepresentation` correctly distinguishes the
        parent classes even if the schemes are the same::

            sage: from sage.schemes.generic.divisor_group import DivisorGroup
            sage: DivisorGroup(P2, ZZ) is ToricDivisorGroup(P2, ZZ)
            False
        """
    def ngens(self):
        """
        Return the number of generators.

        OUTPUT:

        The number of generators of ``self``, which equals the number of
        rays in the fan of the toric variety.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: TDiv = P2.toric_divisor_group()
            sage: TDiv.ngens()
            3
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of the divisor group.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: TDiv = P2.toric_divisor_group()
            sage: TDiv.gens()
            (V(x), V(y), V(z))
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of the divisor group.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        The divisor `z_i=0`, where `z_i` is the `i`-th homogeneous
        coordinate.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: TDiv = P2.toric_divisor_group()
            sage: TDiv.gen(2)
            V(z)
        """
    def base_extend(self, R):
        """
        Extend the scalars of ``self`` to ``R``.

        INPUT:

        - ``R`` -- ring

        OUTPUT: toric divisor group

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: DivZZ = P2.toric_divisor_group()
            sage: DivQQ = P2.toric_divisor_group(base_ring=QQ)
            sage: DivZZ.base_extend(QQ) is DivQQ
            True
        """
    Element = ToricDivisor_generic

class ToricRationalDivisorClassGroup(FreeModule_ambient_field, UniqueRepresentation):
    """
    The rational divisor class group of a toric variety.

    The **T-Weil divisor class group** `\\mathop{Cl}(X)` of a toric
    variety `X` is a finitely generated abelian group and can contain
    torsion. Its rank equals the number of rays in the fan of `X`
    minus the dimension of `X`.

    The **rational divisor class group** is `\\mathop{Cl}(X)
    \\otimes_\\ZZ \\QQ` and never includes torsion. If `X` is *smooth*,
    this equals the **Picard group** `\\mathop{\\mathrm{Pic}}(X)`, whose
    elements are the isomorphism classes of line bundles on `X`. The
    group law (which we write as addition) is the tensor product of
    the line bundles. The Picard group of a toric variety is always
    torsion-free.

    .. WARNING::

        Do not instantiate this class yourself. Use
        :meth:`~sage.schemes.toric.variety.ToricVariety_field.rational_class_group`
        method of :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>` if you need
        the divisor class group. Or you can obtain it as the parent of any
        divisor class constructed, for example, via
        :meth:`ToricDivisor_generic.divisor_class`.

    INPUT:

    - ``toric_variety`` -- :class:`toric variety
      <sage.schemes.toric.variety.ToricVariety_field`

    OUTPUT: rational divisor class group of a toric variety

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: P2.rational_class_group()
        The toric rational divisor class group of a 2-d CPR-Fano
        toric variety covered by 3 affine patches
        sage: D = P2.divisor(0); D
        V(x)
        sage: Dclass = D.divisor_class(); Dclass
        Divisor class [1]
        sage: Dclass.lift()
        V(y)
        sage: Dclass.parent()
        The toric rational divisor class group of a 2-d CPR-Fano
        toric variety covered by 3 affine patches
    """
    def __init__(self, toric_variety) -> None:
        """
        Construct the toric rational divisor class group.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: from sage.schemes.toric.divisor import ToricRationalDivisorClassGroup
            sage: ToricRationalDivisorClassGroup(P2)
            The toric rational divisor class group of a 2-d CPR-Fano
            toric variety covered by 3 affine patches

        TESTS:

        Make sure we lift integral classes to integral divisors::

            sage: rays = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, -1)]
            sage: cones = [(0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4)]
            sage: X = ToricVariety(Fan(cones=cones, rays=rays))
            sage: Cl = X.rational_class_group()
            sage: Cl._projection_matrix
            [1 1 0 0 0]
            [0 2 1 1 1]
            sage: Cl._lift_matrix
            [ 0  0]
            [ 1  0]
            [ 0  0]
            [-2  1]
            [ 0  0]
            sage: Cl._lift_matrix.base_ring()
            Integer Ring
        """
    Element = ToricRationalDivisorClass

class ToricRationalDivisorClassGroup_basis_lattice(FreeModule_ambient_pid):
    """
    Construct the basis lattice of the ``group``.

    INPUT:

    - ``group`` -- :class:`toric rational divisor class group
      <ToricRationalDivisorClassGroup>`

    OUTPUT: the basis lattice of ``group``

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: L = P1xP1.Kaehler_cone().lattice()
        sage: L
        Basis lattice of The toric rational divisor class group of a
        2-d CPR-Fano toric variety covered by 4 affine patches
        sage: L.basis()
        [Divisor class [1, 0], Divisor class [0, 1]]
    """
    def __init__(self, group) -> None:
        """
        See :class:`ToricRationalDivisorClassGroup_basis_lattice` for
        documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: L = P1xP1.Kaehler_cone().lattice()
            sage: TestSuite(L).run()
        """
    Element = ToricRationalDivisorClass
