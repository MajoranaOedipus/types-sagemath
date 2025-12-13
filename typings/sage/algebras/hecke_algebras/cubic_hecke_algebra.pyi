from sage.algebras.hecke_algebras.cubic_hecke_base_ring import CubicHeckeRingOfDefinition as CubicHeckeRingOfDefinition
from sage.algebras.hecke_algebras.cubic_hecke_matrix_rep import AbsIrreducibeRep as AbsIrreducibeRep, CubicHeckeMatrixSpace as CubicHeckeMatrixSpace, RepresentationType as RepresentationType
from sage.algebras.splitting_algebra import solve_with_extension as solve_with_extension
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.groups.cubic_braid import CubicBraidGroup as CubicBraidGroup
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.verbose import verbose as verbose
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ

class CubicHeckeElement(CombinatorialFreeModule.Element):
    """
    An element of a :class:`CubicHeckeAlgebra`.

    For more information see :class:`CubicHeckeAlgebra`.

    EXAMPLES::

        sage: CHA3s = algebras.CubicHecke('s1, s2'); CHA3s.an_element()
        -w*s1*s2^-1 + v*s1 + u*s2 - ((v*w-u)/w)
        sage: CHA3.<c1, c2> = algebras.CubicHecke(3)
        sage: c1**3*~c2
        u*w*c1^-1*c2^-1 + (u^2-v)*c1*c2^-1 - (u*v-w)*c2^-1
    """
    def __invert__(self):
        """
        Return inverse of ``self`` (if possible).

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele1 = CHA3((1,-2,1)); ele1
            c0*c1^-1*c0
            sage: ~ele1                       # indirect doctest
            c0^-1*c1*c0^-1

            sage: CHA2 = algebras.CubicHecke(2)
            sage: x = CHA2.an_element(); x
            v*c - ((v*w-u)/w)
            sage: ~x
            Traceback (most recent call last):
            ...
            ValueError: cannot invert self (= v*c - ((v*w-u)/w))
        """
    def Tietze(self):
        """
        Return the Tietze presentation of ``self`` if ``self`` belongs to the
        basis of its parent and ``None`` otherwise.

        OUTPUT:

        A tuple representing the pre image braid of ``self`` if ``self`` is a
        monomial from the basis ``None`` else-wise

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element(); ele
            -w*c0*c1^-1 + v*c0 + u*c1 - ((v*w-u)/w)
            sage: ele.Tietze() is None
            True
            sage: [CHA3(sp).Tietze() for sp in ele.support()]
            [(), (1,), (1, -2), (2,)]
        """
    def max_len(self):
        """
        Return the maximum of the length of Tietze expressions among the
        support of ``self``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element(); ele
            -w*c0*c1^-1 + v*c0 + u*c1 - ((v*w-u)/w)
            sage: ele.max_len()
            2
        """
    def braid_group_algebra_pre_image(self):
        """
        Return a pre image of ``self`` in the group algebra of the braid group
        (with respect to the basis given by Ivan Marin).

        OUTPUT:

        The pre image of ``self`` as instance of the element class of the group
        algebra of the BraidGroup

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element(); ele
            -w*c0*c1^-1 + v*c0 + u*c1 - ((v*w-u)/w)
            sage: b_ele = ele.braid_group_algebra_pre_image(); b_ele
            -((v*w-u)/w) + v*c0 + u*c1 - w*c0*c1^-1
            sage: ele in CHA3
            True
            sage: b_ele in CHA3
            False
            sage: b_ele in CHA3.braid_group_algebra()
            True
        """
    def cubic_braid_group_algebra_pre_image(self):
        """
        Return a pre image of ``self`` in the group algebra of the cubic braid
        group.

        OUTPUT:

        The pre image of ``self`` as instance of the element class of the group
        algebra of the :class:`CubicBraidGroup`.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element(); ele
            -w*c0*c1^-1 + v*c0 + u*c1 - ((v*w-u)/w)
            sage: cb_ele = ele.cubic_braid_group_algebra_pre_image(); cb_ele
            -w*c0*c1^-1 + v*c0 + u*c1 - ((v*w-u)/w)
            sage: ele in CHA3
            True
            sage: cb_ele in CHA3
            False
            sage: cb_ele in CHA3.cubic_braid_group_algebra()
            True
        """
    @cached_method
    def matrix(self, subdivide: bool = False, representation_type=None, original: bool = False):
        """
        Return certain types of matrix representations of ``self``.

        The absolutely irreducible representations of the cubic Hecke algebra
        are constructed using the ``GAP3`` interface and the ``CHEVIE`` package
        if ``GAP3`` and ``CHEVIE`` are installed on the system. Furthermore,
        the representations given on `Ivan Marin's homepage
        <http://www.lamfa.u-picardie.fr/marin/representationH4-en.html>`__
        are used:

        INPUT:

        - ``subdivide`` -- boolean (default: ``False``); this boolean is passed
          to the block_matrix function
        - ``representation_type`` -- instance of enum :class:`RepresentationType`;
          this can be obtained by the attribute :attr:`CubicHeckeAlgebra.repr_type`
          of ``self``; the following values are possible:

          - ``RegularLeft`` -- (regular left repr. from the above URL)
          - ``RegularRight`` -- (regular right repr. from the above URL)
          - ``SplitIrredChevie`` -- (split irred. repr. via CHEVIE)
          - ``SplitIrredMarin`` -- (split irred. repr. from the above URL)
          - default:  ``SplitIrredChevie`` taken if GAP3 and CHEVIE are installed
            on the system, otherwise the default will be ``SplitIrredMarin``

        - ``original`` -- boolean (default: ``False``); if set to ``True`` the base
          ring of the matrix will be the generic base_ring resp. generic extension
          ring (for the split versions) of the parent of ``self``

        OUTPUT:

        An instance of :class:`~sage.algebras.hecke_algebras.cubic_hecke_matrix_rep.CubicHeckeMatrixRep`,
        which is inherited from :class:`~sage.matrix.matrix_generic_dense.Matrix_generic_dense`.
        In the case of the irreducible representations the matrix is given as a
        block matrix. Each single irreducible can be obtained as item indexed by
        the members of the enum :class:`AbsIrreducibeRep` available via
        :attr:`CubicHeckeAlgebra.irred_repr`.
        For details type: ``CubicHeckeAlgebra.irred_repr?``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: CHA3.inject_variables()
            Defining c0, c1
            sage: c0m = c0.matrix()
            sage: c0m[CHA3.irred_repr.W3_111]
            [                      -b - a + u     0    0]
            [(-2*a + u)*b - 2*a^2 + 2*u*a - v     b    0]
            [                               b     1    a]

        using the ``representation_type`` option::

            sage: CHA3.<c0, c1> = algebras.CubicHecke(3)     #  optional gap3
            sage: chevie = CHA3.repr_type.SplitIrredChevie   #  optional gap3
            sage: c0m_ch = c0.matrix(representation_type=chevie) #  optional gap3
            sage: c0m_ch[CHA3.irred_repr.W3_011]             #  optional gap3
            [         b          0]
            [        -b -b - a + u]
            sage: c0m[CHA3.irred_repr.W3_011]
            [            b             0]
            [a^2 - u*a + v    -b - a + u]

        using the ``original`` option::

            sage: c0mo = c0.matrix(original=True)
            sage: c0mo_ch = c0.matrix(representation_type=chevie, original=True) #  optional gap3
            sage: c0mo[CHA3.irred_repr.W3_011]
            [  b   0]
            [b*c   c]
            sage: c0mo_ch[CHA3.irred_repr.W3_011]            #  optional gap3
            [ b  0]
            [-b  c]

        specialized matrices::

            sage: t = (3,7,11)
            sage: CHA4 = algebras.CubicHecke(4, cubic_equation_roots=t)  # optional database_cubic_hecke
            sage: e = CHA4.an_element(); e                     # optional database_cubic_hecke
            -231*c0*c1^-1 + 131*c0*c2^-1 + 21*c2*c1 - 1440/11
            sage: em = e.matrix()                              # optional database_cubic_hecke
            sage: em.base_ring()                               # optional database_cubic_hecke
            Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
               over Integer Ring localized at (3, 7, 11)
            sage: em.dimensions()                              # optional database_cubic_hecke
            (108, 108)
            sage: em_irr24 = em[23]                            # optional database_cubic_hecke
            sage: em_irr24.dimensions()                        # optional database_cubic_hecke
            (9, 9)
            sage: em_irr24[3,2]                                # optional database_cubic_hecke
            -131*E3 - 393/7
            sage: emg = e.matrix(representation_type=chevie)   # optional gap3 database_cubic_hecke
            sage: emg_irr24 = emg[23]                          # optional gap3 database_cubic_hecke
            sage: emg_irr24[3,2]                               # optional gap3 database_cubic_hecke
            -131*E3 - 393/7
        """
    def revert_garside(self):
        """
        Return the image of ``self`` under the Garside involution.

        .. SEEALSO::

            :meth:`CubicHeckeAlgebra.garside_involution`

        EXAMPLES::

            sage: roots = (E(3), ~E(3), 1)
            sage: CHA3.<c1, c2> = algebras.CubicHecke(3, cubic_equation_roots=roots)
            sage: e = CHA3.an_element(); e
            -c1*c2^-1
            sage: _.revert_garside()
            -c2*c1^-1
            sage: _.revert_garside()
            -c1*c2^-1
        """
    def revert_mirror(self):
        """
        Return the image of ``self`` under the mirror isomorphism.

        .. SEEALSO::

            :meth:`CubicHeckeAlgebra.mirror_isomorphism`

        EXAMPLES::

            sage: CHA3.<c1, c2> = algebras.CubicHecke(3)
            sage: e = CHA3.an_element()
            sage: e.revert_mirror()
            -1/w*c0^-1*c1 + u/w*c0^-1 + v/w*c1^-1 + ((v*w-u)/w)
            sage: _.revert_mirror() == e
            True
        """
    def revert_orientation(self):
        """
        Return the image of ``self`` under the anti involution reverting the
        orientation of braids.

        .. SEEALSO::

            :meth:`CubicHeckeAlgebra.orientation_antiinvolution`

        EXAMPLES::

            sage: CHA3.<c1, c2> = algebras.CubicHecke(3)
            sage: e = CHA3.an_element()
            sage: e.revert_orientation()
            -w*c2^-1*c1 + v*c1 + u*c2 - ((v*w-u)/w)
            sage: _.revert_orientation() == e
            True
        """
    def formal_markov_trace(self, extended: bool = False, field_embedding: bool = False):
        """
        Return a formal expression which can be specialized to Markov traces
        which factor through the cubic Hecke algebra.

        This covers Markov traces corresponding to the

        - HOMFLY-PT polynomial,
        - Kauffman polynomial,
        - Links-Gould polynomial.

        These expressions are elements of a sub-module of the module of linear
        forms on ``self`` the base ring of which is an extension of the
        generic base ring of ``self`` by an additional variable ``s``
        representing the writhe factor. All variables of this base ring
        extension are invertible.

        A Markov trace is a family of class functions `tr_n` on the family
        of braid groups `B_n` into some commutative ring `R` depending on
        a unit `s \\in R` such that for all `b \\in B_n` the following two
        conditions are satisfied (see [Kau1991]_, section 7):

        .. MATH::

            \\begin{array}{lll}
            tr_{n+1}(b g_n)      &  = &  s tr_n(b), \\\\\n            tr_{n+1}(b g^{-1}_n) &  = &  s^{-1} tr_n(b).
            \\end{array}

        The unit `s` is often called the writhe factor and corresponds to the
        additional variable mentioned above.

        .. NOTE::

            Currently it is not known if all linear forms of this sub-module
            belong to a Markov trace, i.e. can be extended to the full tower
            of cubic Hecke algebras. Anyway, at least the four basis elements
            (``U1``, ``U2``, ``U3`` and ``K4``) can be reconstructed form
            the HOMFLY-PT and Kauffman polynomial.

        INPUT:

        - ``extended`` -- boolean (default: ``False``); if set to ``True`` the
          base ring of the Markov trace module is constructed as an extension
          of generic extension ring of ``self``; per default it is constructed
          upon the generic base ring
        - ``field_embedding`` -- boolean (default: ``False``); if set to ``True``
          the base ring of the module is the smallest field containing the
          generic extension ring of ``self``; ignored if ``extended=False``

        EXAMPLES::

            sage: from sage.knots.knotinfo import KnotInfo
            sage: CHA2 = algebras.CubicHecke(2)
            sage: K3_1 = KnotInfo.K3_1
            sage: b3_1 = CHA2(K3_1.braid())
            sage: mt3_1 = b3_1.formal_markov_trace(); mt3_1
            ((u^2*s^2-v*s^2+u*w)/s)*B[U1] - (u*v-w)*B[U2]
            sage: mt3_1.parent()
            Free module generated by {U1, U2}
               over Multivariate Polynomial Ring in u, v, w, s
               over Integer Ring localized at (s, w, v, u)

            sage: f = b3_1.formal_markov_trace(extended=True); f
            (a^2*b*c*s^-1+a*b^2*c*s^-1+a*b*c^2*s^-1+a^2*s+a*b*s+b^2*s+a*c*s+b*c*s+c^2*s)*B[U1]
              + (-a^2*b-a*b^2-a^2*c+(-2)*a*b*c-b^2*c-a*c^2-b*c^2)*B[U2]
            sage: f.parent().base_ring()
            Multivariate Laurent Polynomial Ring in a, b, c, s
              over Splitting Algebra of x^2 + x + 1 with roots [e3, -e3 - 1]
              over Integer Ring

            sage: f = b3_1.formal_markov_trace(extended=True, field_embedding=True); f
            ((a^2*b*c+a*b^2*c+a*b*c^2+a^2*s^2+a*b*s^2+b^2*s^2+a*c*s^2+b*c*s^2+c^2*s^2)/s)*B[U1]
            - (a^2*b+a*b^2+a^2*c+2*a*b*c+b^2*c+a*c^2+b*c^2)*B[U2]
            sage: f.parent().base_ring()
            Fraction Field of Multivariate Polynomial Ring in a, b, c, s
              over Cyclotomic Field of order 3 and degree 2

        Obtaining the well known link invariants from it::

            sage: MT = mt3_1.base_ring()
            sage: sup = mt3_1.support()
            sage: u, v, w, s = mt3_1.base_ring().gens()
            sage: LK3_1 = mt3_1*s**-3 # since the writhe of K3_1 is 3
            sage: f = MT.specialize_homfly()
            sage: g = sum(f(LK3_1.coefficient(b)) * b.regular_homfly_polynomial() for b in sup); g
            L^-2*M^2 - 2*L^-2 - L^-4
            sage: g == K3_1.link().homfly_polynomial()
            True

            sage: f = MT.specialize_kauffman()
            sage: g = sum(f(LK3_1.coefficient(b)) * b.regular_kauffman_polynomial() for b in sup); g
            a^-2*z^2 - 2*a^-2 + a^-3*z + a^-4*z^2 - a^-4 + a^-5*z
            sage: g == K3_1.kauffman_polynomial()
            True

            sage: f = MT.specialize_links_gould()
            sage: g = sum(f(LK3_1.coefficient(b)) * b.links_gould_polynomial() for b in sup); g
            -t0^2*t1 - t0*t1^2 + t0^2 + 2*t0*t1 + t1^2 - t0 - t1 + 1
            sage: g == K3_1.link().links_gould_polynomial()
            True
        """

class CubicHeckeAlgebra(CombinatorialFreeModule):
    """
    Return the Cubic-Hecke algebra with respect to the Artin braid group on
    `n` strands.

    This is a quotient of the group algebra of the Artin braid group, such that
    the images `s_i` (`1 \\leq i < n`) of the braid generators satisfy a cubic
    equation (see :mod:`~sage.algebras.hecke_algebras.cubic_hecke_algebra`
    for more information, in a session type
    ``sage.algebras.hecke_algebras.cubic_hecke_algebra?``):

    .. MATH::

        s_i^3 = u s_i^2 - v s_i + w.

    The base ring of this algebra can be specified by giving optional keywords
    described below. If no keywords are given, the base ring will be a
    :class:`CubicHeckeRingOfDefinition`, which is constructed as the
    polynomial ring in `u, v, w` over the integers localized at `w`.
    This ring will be called the *ring of definition* or sometimes for short
    *generic base ring*. However note, that in this context the word *generic*
    should not remind in a generic point of the corresponding scheme.

    In addition to the base ring, another ring containing the roots (`a`, `b`
    and `c`) of the cubic equation will be needed to handle the split
    irreducible representations. This ring will be called the *extension ring*.
    Generically, the extension ring will be a
    :class:`~sage.algebras.hecke_algebras.cubic_hecke_base_ring.CubicHeckeExtensionRing`,
    which is constructed as the Laurent polynomial ring in `a, b` and `c` over
    the integers adjoined with a primitive third root of unity. A special form
    of this *generic extension ring* is constructed as a
    :class:`~sage.algebras.splitting_algebra.SplittingAlgebra` for the roots of
    the cubic equation and a primitive third root of unity over the ring of
    definition. This ring will be called the *default extension ring*.

    This class uses a static and a dynamic data library. The first one is defined
    as instance of :class:`~sage.databases.cubic_hecke_db.CubicHeckeDataBase`
    and contains the complete basis for the algebras with less than 5 strands
    and various types of representation matrices of the generators. These data
    have been calculated by `Ivan Marin <http://www.lamfa.u-picardie.fr/marin/anglais.html>`__
    and have been imported from his corresponding
    `web page <http://www.lamfa.u-picardie.fr/marin/representationH4-en.html>`__.

    Note that just the data for the cubic Hecke algebras on less than four
    strands is available in Sage by default. To deal with four strands and
    more you need to install the optional package
    `database_cubic_hecke <https://pypi.org/project/database-cubic-hecke/>`__
    by typing

    - ``sage -i database_cubic_hecke`` (first time installation) or
    - ``sage -f database_cubic_hecke`` (reinstallation) respective
    - ``sage -i -c database_cubic_hecke`` (for running all test in concern)
    - ``sage -f -c database_cubic_hecke``

    This will add a `Python wrapper <https://github.com/soehms/database_cubic_hecke#readme>`__
    around Ivan Marin's data to the Sage library. For more installation hints
    see the documentation of this wrapper.

    Furthermore, representation matrices can be obtained from the ``CHEVIE``
    package of ``GAP3`` via the ``GAP3`` interface if ``GAP3`` is installed
    inside Sage. For more information on how to obtain representation matrices
    to elements of this class, see the documentation of the element class
    :class:`~sage.algebras.hecke_algebras.cubic_hecke_algebra.CubicHeckeElement`
    or its method
    :meth:`~sage.algebras.hecke_algebras.cubic_hecke_algebra.CubicHeckeElement.matrix`:

        ``algebras.CubicHecke.Element?`` or ``algebras.CubicHecke.Element.matrix?``

    The second library is created as instance of
    :class:`~sage.databases.cubic_hecke_db.CubicHeckeFileCache` and used while
    working with the class to achieve a better performance. This file cache
    contains images of braids and representation matrices of basis elements
    from former calculations. A refresh of the file cache can be done using
    the :meth:`reset_filecache`.

    INPUT:

    - ``names`` -- string containing the names of the generators as images of
      the braid group generators
    - ``cubic_equation_parameters`` -- tuple ``(u, v, w)`` of three elements
      in an integral domain used as coefficients in the cubic equation. If this
      argument is given the base ring will be set to the common parent of
      ``u, v, w``. In addition a conversion map from the generic base ring is
      supplied. This keyword can also be used to change the variable names of
      the generic base ring (see example 3 below)
    - ``cubic_equation_roots`` -- tuple ``(a, b, c)`` of three elements in an
      integral domain which stand for the roots of the cubic equation. If this
      argument is given the extension ring will be set to the common parent of
      ``a, b, c``. In addition a conversion map from the generic extension ring
      and the generic base ring is supplied. This keyword can also be used to
      change the variable names of the generic extension ring (see example 3
      below)

    EXAMPLES:

    Cubic Hecke algebra over the ring of definition::

        sage: CHA3 = algebras.CubicHecke('s1, s2'); CHA3
        Cubic Hecke algebra on 3 strands over Multivariate Polynomial Ring
          in u, v, w
          over Integer Ring localized at (w,)
          with cubic equation: h^3 - u*h^2 + v*h - w = 0
        sage: CHA3.gens()
        (s1, s2)
        sage: GER = CHA3.extension_ring(generic=True); GER
        Multivariate Laurent Polynomial Ring in a, b, c
          over Splitting Algebra of x^2 + x + 1
            with roots [e3, -e3 - 1] over Integer Ring
        sage: ER = CHA3.extension_ring(); ER
        Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
          over Splitting Algebra of h^3 - u*h^2 + v*h - w
            with roots [a, b, -b - a + u]
          over Multivariate Polynomial Ring in u, v, w
          over Integer Ring localized at (w,)

    Element construction::

        sage: ele = CHA3.an_element(); ele
        -w*s1*s2^-1 + v*s1 + u*s2 - ((v*w-u)/w)
        sage: ele2 = ele**2; ele2
        w^2*(s1^-1*s2)^2 - u*w^2*s1^-1*s2*s1^-1 - v*w*s2*s1^-1*s2
        - v*w^2*s1^-1*s2^-1 + u*w*s1*s2*s1^-1*s2 - u*w*s1^-1*s2*s1
        - (u*v*w-2*v*w+2*u)*s1*s2^-1 + u*v*w*s2*s1^-1 + u*v*s2*s1 + v^2*w*s1^-1
        - u^2*w*s1*s2*s1^-1 + ((u*v^2*w-2*v^2*w-u*w^2+2*u*v)/w)*s1 + u*v*s1*s2
        + (u^2*w+v^2*w)*s2^-1 + ((u^3*w-2*u*v*w+2*u^2)/w)*s2
        - ((u^2*v*w^2+v^3*w^2-v^2*w^2+2*u*v*w-u^2)/w^2)
        sage: B3 = CHA3.braid_group()
        sage: braid = B3((2,-1, 2, 1)); braid
        s2*s1^-1*s2*s1
        sage: ele3 = CHA3(braid); ele3
        s1*s2*s1^-1*s2 + u*s1^-1*s2*s1 - v*s1*s2^-1 + v*s2^-1*s1 - u*s1*s2*s1^-1
        sage: ele3t = CHA3((2,-1, 2, 1))
        sage: ele3 == ele3t
        True
        sage: CHA4 = algebras.CubicHecke(4)     # optional database_cubic_hecke
        sage: ele4 = CHA4(ele3); ele4           # optional database_cubic_hecke
        c0*c1*c0^-1*c1 + u*c0^-1*c1*c0 + (-v)*c0*c1^-1 + v*c1^-1*c0 + (-u)*c0*c1*c0^-1

    Cubic Hecke algebra over the ring of definition using different variable
    names::

        sage: algebras.CubicHecke(3, cubic_equation_parameters='u, v, w', cubic_equation_roots='p, q, r')
        Cubic Hecke algebra on 3 strands over Multivariate Polynomial Ring
          in u, v, w
          over Integer Ring localized at (w,)
            with cubic equation: h^3 - u*h^2 + v*h - w = 0
        sage: _.extension_ring()
        Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
          over Splitting Algebra of h^3 - u*h^2 + v*h - w
            with roots [p, q, -q - p + u]
          over Multivariate Polynomial Ring in u, v, w
          over Integer Ring localized at (w,)

    Cubic Hecke algebra over a special base ring with respect to a special
    cubic equation::

        sage: algebras.CubicHecke('s1, s2', cubic_equation_parameters=(QQ(1),3,1))
        Cubic Hecke algebra on 3 strands over Rational Field
          with cubic equation: h^3 - h^2 + 3*h - 1 = 0
        sage: CHA3 = _
        sage: ER = CHA3.extension_ring(); ER
        Number Field in T with defining polynomial T^12 + 4*T^11 + 51*T^10
        + 154*T^9 + 855*T^8 + 1880*T^7 + 5805*T^6 + 8798*T^5 + 15312*T^4
        + 14212*T^3 + 13224*T^2 + 5776*T + 1444
        sage: CHA3.cubic_equation_roots()[0]
        -4321/1337904*T^11 - 4181/445968*T^10 - 4064/27873*T^9 - 51725/167238*T^8
        - 2693189/1337904*T^7 - 1272907/445968*T^6 - 704251/74328*T^5
        - 591488/83619*T^4 - 642145/83619*T^3 + 252521/111492*T^2 + 45685/5868*T
        + 55187/17604

        sage: F = GF(25,'u')
        sage: algebras.CubicHecke('s1, s2', cubic_equation_parameters=(F(1), F.gen(), F(3)))
        Cubic Hecke algebra on 3 strands over Finite Field in u of size 5^2
          with cubic equation: h^3 + 4*h^2 + u*h + 2 = 0
        sage: CHA3 = _
        sage: ER = CHA3.extension_ring(); ER
        Finite Field in S of size 5^4
        sage: CHA3.cubic_equation_roots()
        [2*S^3 + 2*S^2 + 2*S + 1, 2*S^3 + 3*S^2 + 3*S + 2, S^3 + 3]


    Cubic Hecke algebra over a special extension ring with respect to special
    roots of the cubic equation::

        sage: UCF = UniversalCyclotomicField()
        sage: e3=UCF.gen(3); e5=UCF.gen(5)
        sage: algebras.CubicHecke('s1, s2', cubic_equation_roots=(1, e5, e3))
        Cubic Hecke algebra on 3 strands over Universal Cyclotomic Field
          with cubic equation:
          h^3 + (-E(15) - E(15)^4 - E(15)^7 + E(15)^8)*h^2 + (-E(15)^2 - E(15)^8
          - E(15)^11 - E(15)^13 - E(15)^14)*h - E(15)^8 = 0

    TESTS::

        sage: CHA3 = algebras.CubicHecke(3)
        sage: TestSuite(CHA3).run()

    Note, that the ``TestSuite`` run on the cubic Hecke algebra on four strands
    would take up to half an hour if the file cache is empty. A repetition takes
    less than half a minute.
    """
    Element = CubicHeckeElement
    repr_type = RepresentationType
    irred_repr = AbsIrreducibeRep
    @staticmethod
    def __classcall_private__(cls, n=None, names: str = 'c', cubic_equation_parameters=None, cubic_equation_roots=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2, 'd', cubic_equation_roots=(3,5,7)); CHA2
            Cubic Hecke algebra on 2 strands
              over Integer Ring localized at (3, 5, 7)
                with cubic equation:
                h^3 - 15*h^2 + 71*h - 105 = 0
            sage: CHA2.inject_variables()
            Defining d
            sage: CHA3 = algebras.CubicHecke(3,  cubic_equation_parameters=(3,5,7)); CHA3
            Cubic Hecke algebra on 3 strands
              over Integer Ring localized at (7,)
                with cubic equation:
                h^3 - 3*h^2 + 5*h - 7 = 0
            sage: CHA3.cubic_equation_roots()
            [a, b, -b - a + 3]
        """
    def __init__(self, names, cubic_equation_parameters=None, cubic_equation_roots=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: CHA2 = algebras.CubicHecke(2, 'd', cubic_equation_roots=(3,5,7))
            sage: TestSuite(CHA2).run()
            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_parameters=(3,5,7))
            sage: TestSuite(CHA2).run()
        """
    def get_order(self):
        """
        Return an ordering of the basis of ``self``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: len(CHA3.get_order())
            24
        """
    def ngens(self):
        """
        The number of generators of the algebra.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.ngens()
            1
        """
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.algebra_generators()
            Finite family {c: c}
        """
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.gens()
            (c,)
        """
    def gen(self, i):
        """
        The ``i``-th generator of the algebra.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.gen(0)
            c
        """
    def one_basis(self):
        """
        Return the index of the basis element for the identity element
        in the cubic braid group.

         EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.one_basis()
            1
        """
    @cached_method
    def chevie(self):
        """
        Return the ``GAP3``-``CHEVIE`` realization of the corresponding
        cyclotomic Hecke algebra in the finite-dimensional case.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)  # optional gap3
            sage: CHA3.chevie()                  # optional gap3
            Hecke(G4,[[a,b,c]])
        """
    @cached_method
    def product_on_basis(self, g1, g2):
        """
        Return product on basis elements indexed by ``g1`` and ``g2``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: g = CHA3.basis().keys().an_element(); g
            c0*c1
            sage: CHA3.product_on_basis(g, ~g)
            1
            sage: CHA3.product_on_basis(g, g)
            w*c0^-1*c1*c0 - v*c1*c0 + u*c0*c1*c0
        """
    def filecache_section(self):
        """
        Return the ``enum`` to select a section in the file cache.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: list(CHA2.filecache_section())
            [<section.matrix_representations: 'matrix_representations'>,
             <section.braid_images: 'braid_images'>,
             <section.basis_extensions: 'basis_extensions'>,
             <section.markov_trace: 'markov_trace'>]
        """
    def is_filecache_empty(self, section=None):
        """
        Return ``True`` if the file cache of the given ``section`` is empty.
        If no ``section`` is given the answer is given for the complete
        file cache.

        INPUT:

        - ``section`` -- (default: all sections) an element of enum
          :class:`~sage.databases.cubic_hecke_db.CubicHeckeFileCache.section`
          that can be selected using :meth:`filecache_section`

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.is_filecache_empty()
            False
        """
    def reset_filecache(self, section=None, commit: bool = True) -> None:
        """
        Reset the file cache of the given ``section`` resp. the complete
        file cache if no ``section`` is given.

        INPUT:

        - ``section`` -- (default: all sections) an element of enum
          :class:`~sage.databases.cubic_hecke_db.CubicHeckeFileCache.section`
          that can be selected using :meth:`filecache_section`
        - ``commit`` -- boolean (default: ``True``); if set to ``False`` the
          reset is not written to the filesystem

        EXAMPLES::

            sage: # optional - database_cubic_hecke
            sage: CHA5 = algebras.CubicHecke(5)
            sage: be = CHA5.filecache_section().basis_extensions
            sage: CHA5.is_filecache_empty(be)
            False
            sage: CHA5.reset_filecache(be)
            sage: CHA5.is_filecache_empty(be)
            True
        """
    def strands(self):
        """
        Return the number of strands of the braid group whose group algebra
        image is ``self``.

        EXAMPLES::

            sage: CHA4 = algebras.CubicHecke(2)
            sage: CHA4.strands()
            2
        """
    def garside_involution(self, element):
        """
        Return the image of the given element of ``self`` under the extension of
        the Garside involution of braids to ``self``.

        This method may be invoked by the ``revert_garside`` method of the
        element class of ``self``, alternatively.

        INPUT:

        - ``element`` -- instance of the element class of ``self``

        OUTPUT:

        Instance of the element class of ``self`` representing the image of
        ``element`` under the extension of the Garside involution to ``self``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element()
            sage: ele_gar = CHA3.garside_involution(ele); ele_gar
            -w*c1*c0^-1 + u*c0 + v*c1 - ((v*w-u)/w)
            sage: ele == CHA3.garside_involution(ele_gar)
            True
        """
    def orientation_antiinvolution(self, element):
        """
        Return the image of the given element of ``self`` under the extension of
        the orientation anti involution of braids to ``self``. The orientation
        anti involution of a braid is given by reversing the order of generators
        in the braid word.

        This method may be invoked by the ``revert_orientation`` method of the
        element class of ``self``, alternatively.

        INPUT:

        - ``element`` -- instance of the element class of ``self``

        OUTPUT:

        Instance of the element class of ``self`` representing the image of
        ``element`` under the extension of the orientation reversing braid
        involution to ``self``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element()
            sage: ele_ori = CHA3.orientation_antiinvolution(ele); ele_ori
            -w*c1^-1*c0 + v*c0 + u*c1 - ((v*w-u)/w)
            sage: ele == CHA3.orientation_antiinvolution(ele_ori)
            True
        """
    def mirror_isomorphism(self, element):
        """
        Return the image of the given element of ``self`` under the extension
        of the mirror involution of braids to ``self``. The mirror involution
        of a braid is given by inverting all generators in the braid word. It
        does not factor through ``self`` over the base ring but it factors
        through ``self`` considered as a `\\ZZ`-module relative to the mirror
        automorphism of the generic base ring. Considering ``self`` as algebra
        over its base ring this involution defines an isomorphism of ``self``
        onto a different cubic Hecke algebra with a different cubic equation.
        This is defined over a different base (and extension) ring than
        ``self``. It can be obtained by the method ``mirror_image`` or as
        parent of the output of this method.

        This method may be invoked by the ``CubicHeckeElelemnt.revert_mirror``
        method of the element class of ``self``, alternatively.

        INPUT:

        - ``element`` -- instance of the element class of ``self``

        OUTPUT:

        Instance of the element class of the mirror image of ``self``
        representing the image of element under the extension of the braid
        mirror involution to ``self``.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ele = CHA3.an_element()
            sage: ele_mirr = CHA3.mirror_isomorphism(ele); ele_mirr
            -1/w*c0^-1*c1 + u/w*c0^-1 + v/w*c1^-1 + ((v*w-u)/w)
            sage: ele_mirr2 = ele.revert_mirror()  # indirect doctest
            sage: ele_mirr == ele_mirr2
            True
            sage: par_mirr = ele_mirr.parent()
            sage: par_mirr == CHA3
            False
            sage: par_mirr == CHA3.mirror_image()
            True
            sage: ele == par_mirr.mirror_isomorphism(ele_mirr)
            True
        """
    def cubic_equation(self, var: str = 'h', as_coefficients: bool = False, generic: bool = False):
        """
        Return the cubic equation attached to ``self``.

        INPUT:

        - ``var`` -- string (default: ``'h'``); setting the indeterminate of the
          equation
        - ``as_coefficients`` -- boolean (default: ``False``);  if set to ``True``
          the list of coefficients is returned
        - ``generic`` -- boolean (default: ``False``);  if set to ``True`` the
          cubic equation will be given over the generic base ring

        OUTPUT:

        A polynomial over the base ring (resp. generic base ring if ``generic``
        is set to True). In case ``as_coefficients`` is set to ``True`` a list
        of them is returned.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_roots=(E(3), ~E(3), 1))
            sage: CHA2.cubic_equation()
            h^3 - 1
            sage: CHA2.cubic_equation(generic=True)
            h^3 - u*h^2 + v*h - w
            sage: CHA2.cubic_equation(as_coefficients=True, generic=True)
            [-w, v, -u, 1]
            sage: CHA2.cubic_equation(as_coefficients=True)
            [-1, 0, 0, 1]
        """
    def cubic_equation_roots(self, generic: bool = False):
        """
        Return the roots of the underlying cubic equation.

        INPUT:

        - ``generic`` -- boolean (default: ``False``);  if set to ``True`` the
          roots are returned as elements of the generic extension ring

        OUTPUT: a triple consisting of the roots

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_roots=(3, 4, 5))
            sage: CHA2.cubic_equation()
            h^3 - 12*h^2 + 47*h - 60
            sage: CHA2.cubic_equation_roots()
            [3, 4, 5]
            sage: CHA2.cubic_equation_roots(generic=True)
            [a, b, c]
        """
    def cubic_equation_parameters(self, generic: bool = False):
        """
        Return the coefficients of the underlying cubic equation.

        INPUT:

        - ``generic`` -- boolean (default: ``False``);  if set to ``True`` the
          coefficients are returned as elements of the generic base ring

        OUTPUT: a triple consisting of the coefficients

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_roots=(3, 4, 5))
            sage: CHA2.cubic_equation()
            h^3 - 12*h^2 + 47*h - 60
            sage: CHA2.cubic_equation_parameters()
            [12, 47, 60]
            sage: CHA2.cubic_equation_parameters(generic=True)
            [u, v, w]
        """
    def base_ring(self, generic: bool = False):
        """
        Return the base ring of ``self``.

        INPUT:

        - ``generic`` -- boolean (default: ``False``); if ``True`` the ring
          of definition (here often called the generic base ring) is returned

        EXAMMPLES::

            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_roots=(3, 4, 5))
            sage: CHA2.base_ring()
            Integer Ring localized at (2, 3, 5)
            sage: CHA2.base_ring(generic=True)
            Multivariate Polynomial Ring in u, v, w
              over Integer Ring localized at (w,)
        """
    def extension_ring(self, generic: bool = False):
        """
        Return the extension ring of ``self``.

        This is an extension of its base ring containing the roots
        of the cubic equation.

        INPUT:

        - ``generic`` -- boolean (default: ``False``); if ``True`` the
          extension ring of definition (here often called the generic
          extension ring) is returned

        EXAMMPLES::

            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_roots=(3, 4, 5))
            sage: CHA2.extension_ring()
            Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
            over Integer Ring localized at (2, 3, 5)
            sage: CHA2.extension_ring(generic=True)
            Multivariate Laurent Polynomial Ring in a, b, c
            over Splitting Algebra of x^2 + x + 1
              with roots [e3, -e3 - 1] over Integer Ring
        """
    def cyclotomic_generator(self, generic: bool = False):
        """
        Return the third root of unity as element of the extension ring.

        The only thing where this is needed is in the nine dimensional
        irreducible representations of the cubic Hecke algebra on four strands
        (see the examples of :meth:`CubicHeckeElement.matrix` for instance).

        INPUT:

        - ``generic`` -- boolean (default: ``False``); if ``True`` the
          cyclotomic generator is returned as an element extension ring of
          definition

        EXAMMPLES::

            sage: CHA2 = algebras.CubicHecke(2, cubic_equation_roots=(3, 4, 5))
            sage: CHA2.cyclotomic_generator()
            E3
            sage: CHA2.cyclotomic_generator(generic=True)
            e3
        """
    def braid_group(self):
        """
        Return the braid group attached to ``self``.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.braid_group()
            Braid group on 2 strands
        """
    def cubic_braid_group(self):
        """
        Return the cubic braid group attached to ``self``.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.cubic_braid_group()
            Cubic Braid group on 2 strands
        """
    def braid_group_algebra(self):
        """
        Return the group algebra of braid group attached to ``self`` over the
        base ring of ``self``.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.braid_group_algebra()
            Algebra of Braid group on 2 strands
             over Multivariate Polynomial Ring in u, v, w
             over Integer Ring localized at (w,)
        """
    def cubic_braid_group_algebra(self):
        """
        Return the group algebra of cubic braid group attached to ``self`` over
        the base ring of ``self``.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: CHA2.cubic_braid_group_algebra()
            Algebra of Cubic Braid group on 2 strands
             over Multivariate Polynomial Ring in u, v, w
             over Integer Ring localized at (w,)
        """
    def cubic_hecke_subalgebra(self, nstrands=None):
        """
        Return a :class:`CubicHeckeAlgebra` that realizes a sub-algebra
        of ``self`` on the first ``n_strands`` strands.

        INPUT:

        - ``nstrands`` -- integer at least 1 and at most :meth:`strands` giving
          the number of strands for the subgroup; the default is one strand
          less than ``self`` has

        OUTPUT: an instance of this class realizing the sub-algebra

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3, cubic_equation_roots=(3, 4, 5))
            sage: CHA3.cubic_hecke_subalgebra()
            Cubic Hecke algebra on 2 strands
              over Integer Ring localized at (2, 3, 5)
                with cubic equation: h^3 - 12*h^2 + 47*h - 60 = 0
        """
    def mirror_image(self):
        """
        Return a copy of ``self`` with the mirrored cubic equation, that is:
        the cubic equation has the inverse roots to the roots with respect
        to ``self``.

        This is needed since the mirror involution of the braid group does
        not factor through ``self`` (considered as an algebra over the base
        ring, just considered as `\\ZZ`-algebra). Therefore, the mirror
        involution of an element of ``self`` belongs to ``mirror_image``.

        OUTPUT:

        A cubic Hecke algebra over the same base and extension ring,
        but whose cubic equation is transformed by the mirror involution
        applied to its coefficients and roots.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: ce = CHA2.cubic_equation(); ce
            h^3 - u*h^2 + v*h - w
            sage: CHA2m = CHA2.mirror_image()
            sage: cem =  CHA2m.cubic_equation(); cem
            h^3 + ((-v)/w)*h^2 + u/w*h + (-1)/w
            sage: mi = CHA2.base_ring().mirror_involution(); mi
            Ring endomorphism of Multivariate Polynomial Ring in u, v, w
                                 over Integer Ring localized at (w,)
              Defn: u |--> v/w
                    v |--> u/w
                    w |--> 1/w
            sage: cem == cem.parent()([mi(cf) for cf in ce.coefficients()])
            True

        Note that both cubic Hecke algebras have the same ring of definition
        and identical generic cubic equation::

            sage: cemg = CHA2m.cubic_equation(generic=True)
            sage: CHA2.cubic_equation(generic=True) == cemg
            True
            sage: CHA2.cubic_equation() == cemg
            True
            sage: a, b, c = CHA2.cubic_equation_roots()
            sage: CHA2m.cubic_equation_roots(generic=True) == [a, b, c]
            True
            sage: CHA2m.cubic_equation_roots()
            [((-1)/(-w))*a^2 + (u/(-w))*a + (-v)/(-w),
             ((1/(-w))*a)*b + (1/(-w))*a^2 + ((-u)/(-w))*a,
             (((-1)/(-w))*a)*b]
            sage: ai, bi, ci = _
            sage: ai == ~a, bi == ~b, ci == ~c
            (True, True, True)
            sage: CHA2.extension_ring(generic=True).mirror_involution()
            Ring endomorphism of Multivariate Laurent Polynomial Ring in a, b, c
                                 over Splitting Algebra of x^2 + x + 1
                                   with roots [e3, -e3 - 1] over Integer Ring
              Defn: a |--> a^-1
                    b |--> b^-1
                    c |--> c^-1
                    with map of base ring

        The mirror image can not be obtained for specialized cubic Hecke
        algebras if the specialization does not factor through the mirror
        involution on the ring if definition::

            sage: CHA2s = algebras.CubicHecke(2, cubic_equation_roots=(3, 4, 5))
            sage: CHA2s
            Cubic Hecke algebra on 2 strands
              over Integer Ring localized at (2, 3, 5)
                with cubic equation: h^3 - 12*h^2 + 47*h - 60 = 0

        In the next example it is not clear what the mirror image of ``7``
        should be::

            sage: CHA2s.mirror_image()
            Traceback (most recent call last):
            ...
            RuntimeError: base ring Integer Ring localized at (2, 3, 5)
            does not factor through mirror involution
        """
    def schur_elements(self, generic: bool = False):
        """
        Return the list of Schur elements of ``self`` as elements
        of the extension ring of ``self``.

        .. NOTE::

            This method needs ``GAP3`` installed with package ``CHEVIE``.

        INPUT:

        - ``generic`` -- boolean (default: ``False``); if ``True``,
          the element is returned as element of the generic
          extension ring

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)       # optional gap3
            sage: sch_eles = CHA3.schur_elements()    # optional gap3
            sage: sch_eles[6]                         # optional gap3
            (u^3*w + v^3 - 6*u*v*w + 8*w^2)/w^2
        """
    def schur_element(self, item, generic: bool = False):
        """
        Return a single Schur element of ``self`` as elements
        of the extension ring of ``self``.

        .. NOTE::

            This method needs ``GAP3`` installed with package ``CHEVIE``.

        INPUT:

        - ``item`` -- an element of :class:`AbsIrreducibeRep` to give
          the irreducible representation of ``self`` to which the Schur
          element should be returned
        - ``generic`` -- boolean (default: ``False``); if ``True``,
          the element is returned as element of the generic
          extension ring

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)                 # optional gap3
            sage: CHA3.schur_element(CHA3.irred_repr.W3_111)    # optional gap3
            (u^3*w + v^3 - 6*u*v*w + 8*w^2)/w^2
        """
    def characters(self, irr=None, original: bool = True):
        """
        Return the irreducible characters of ``self``.

        By default the values are given in the generic extension ring.
        Setting the keyword ``original`` to ``False`` you can obtain
        the values in the (non generic) extension ring (compare the
        same keyword for :meth:`CubicHeckeElement.matrix`).

        INPUT:

        - ``irr`` -- (optional) instance of :class:`AbsIrreducibeRep`
          selecting the irreducible representation corresponding to the
          character; if not given a list of all characters is returned
        - ``original`` -- boolean (default: ``True``); see description above

        OUTPUT:

        Function or list of Functions from the element class of ``self`` to
        the (generic or non generic) extension ring depending on the given
        keyword arguments.

        EXAMPLES::

            sage: CHA3 = algebras.CubicHecke(3)
            sage: ch = CHA3.characters()
            sage: e = CHA3.an_element()
            sage: ch[0](e)
            a^2*b + a^2*c + a^2 - b*c + b^-1*c^-1 + a^-1*c^-1 + a^-1*b^-1
            sage: _.parent()
            Multivariate Laurent Polynomial Ring in a, b, c
              over Splitting Algebra of x^2 + x + 1 with roots [e3, -e3 - 1]
              over Integer Ring
            sage: ch_w3_100 = CHA3.characters(irr=CHA3.irred_repr.W3_100)
            sage: ch_w3_100(e) == ch[0](e)
            True
            sage: ch_x = CHA3.characters(original=False)
            sage: ch_x[0](e)
            (u + v)*a + (-v*w - w^2 + u)/w
            sage: _.parent()
            Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
              over Splitting Algebra of h^3 - u*h^2 + v*h - w
                with roots [a, b, -b - a + u]
              over Multivariate Polynomial Ring in u, v, w
              over Integer Ring localized at (w,)
        """
