from enum import Enum
from sage.categories.groups import Groups as Groups
from sage.categories.shephard_groups import ShephardGroups as ShephardGroups
from sage.groups.braid import BraidGroup as BraidGroup
from sage.groups.finitely_presented import FinitelyPresentedGroup as FinitelyPresentedGroup, FinitelyPresentedGroupElement as FinitelyPresentedGroupElement
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.libs.gap.element import GapElement as GapElement
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def AssionGroupS(n=None, names: str = 's'):
    """
    Construct cubic braid groups :class:`CubicBraidGroup` which have been
    investigated by J.Assion using the notation S(m). This function is a short hand cut
    for setting the construction arguments ``cbg_type=CubicBraidGroup.type.AssionS``
    and default ``names='s'``.

    INPUT:

    - ``n`` -- integer (optional); the number of strands
    - ``names`` -- (default: ``'s'``) string or list/tuple/iterable of strings

    .. SEEALSO::

        :class:`CubicBraidGroup`

    EXAMPLES::

        sage: S3 = AssionGroupS(3);  S3
        Assion group on 3 strands of type S
        sage: S3x = CubicBraidGroup(3, names='s', cbg_type=CubicBraidGroup.type.AssionS); S3x
        Assion group on 3 strands of type S
        sage: S3 == S3x
        True
    """
def AssionGroupU(n=None, names: str = 'u'):
    """
    Construct cubic braid groups as instance of :class:`CubicBraidGroup` which have been
    investigated by J.Assion using the notation U(m). This function is a short hand cut
    for setting the construction arguments ``cbg_type=CubicBraidGroup.type.AssionU``
    and default ``names='u'``.

    INPUT:

    - ``n`` -- integer (optional); the number of strands
    - ``names`` -- (default: ``'s'``) string or list/tuple/iterable of strings

    .. SEEALSO::

        :class:`CubicBraidGroup`

    EXAMPLES::

        sage: U3 = AssionGroupU(3);  U3
        Assion group on 3 strands of type U
        sage: U3x = CubicBraidGroup(3, names='u', cbg_type=CubicBraidGroup.type.AssionU); U3x
        Assion group on 3 strands of type U
        sage: U3 == U3x
        True
    """

class CubicBraidElement(FinitelyPresentedGroupElement):
    """
    Elements of cubic factor groups of the braid group.

    For more information see :class:`CubicBraidGroup`.

    EXAMPLES::

        sage: C4.<c1, c2, c3> = CubicBraidGroup(4); C4
        Cubic Braid group on 4 strands
        sage: ele1 = c1*c2*c3^-1*c2^-1
        sage: ele2 = C4((1, 2, -3, -2))
        sage: ele1 == ele2
        True
    """
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C6 = CubicBraidGroup(6)
            sage: C6.inject_variables()
            Defining c0, c1, c2, c3, c4
            sage: c1**2*~c2*c4*c0**2*c4   # indirect doctest
            c1^-1*c2^-1*c4^-1*c0^-1
        """
    def __hash__(self):
        """
        Return a hash value for ``self``.

        EXAMPLES::

            sage: C3.<c1, c2> = CubicBraidGroup(3)
            sage: hash(~c1) == hash(c1**2)
            True
        """
    def braid(self):
        """
        Return the canonical braid preimage of ``self`` as a :class:`Braid`.

        EXAMPLES::

            sage: C3.<c1, c2> = CubicBraidGroup(3)
            sage: c1.parent()
            Cubic Braid group on 3 strands
            sage: c1.braid().parent()
            Braid group on 3 strands
        """
    @cached_method
    def burau_matrix(self, root_bur=None, domain=None, characteristic=None, var: str = 't', reduced: bool = False):
        """
        Return the Burau matrix of the cubic braid coset.

        This method uses the same method belonging to :class:`Braid`, but
        reduces the indeterminate to a primitive sixth (resp. twelfth in case
        ``reduced='unitary'``) root of unity.

        INPUT (all arguments are optional keywords):

        - ``root_bur`` -- six (resp. twelfth) root of unity in some field
          (default: root of unity over `\\QQ`)
        - ``domain`` -- (default: cyclotomic field of order 3 and degree 2, resp.
          the domain of ``root_bur`` if given) base ring for the Burau matrix
        - ``characteristic`` -- integer giving the characteristic of the
          domain (default: 0 or the characteristic of ``domain`` if given)
        - ``var`` -- string used for the indeterminate name in case ``root_bur``
          must be constructed in a splitting field
        - ``reduced`` -- boolean or string (default: ``False``); for more
          information see the documentation of :meth:`burau_matrix` of
          :class:`Braid`

        OUTPUT:

        The Burau matrix of the cubic braid coset with entries in the
        domain given by the options. In case the option ``reduced='unitary'``
        is given a triple consisting of the Burau matrix, its adjoined and
        the Hermitian form is returned.

        EXAMPLES::

            sage: C3.<c1, c2> = CubicBraidGroup(3)
            sage: ele = c1*c2*c1

            sage: # needs sage.rings.number_field
            sage: BuMa = ele.burau_matrix(); BuMa
            [  -zeta3         1     zeta3]
            [  -zeta3 zeta3 + 1         0]
            [       1         0         0]
            sage: BuMa.base_ring()
            Cyclotomic Field of order 3 and degree 2
            sage: BuMa == ele.burau_matrix(characteristic=0)
            True
            sage: BuMa = ele.burau_matrix(domain=QQ); BuMa
            [-t + 1      1  t - 1]
            [-t + 1      t      0]
            [     1      0      0]
            sage: BuMa.base_ring()
            Number Field in t with defining polynomial t^2 - t + 1
            sage: BuMa = ele.burau_matrix(domain = QQ[I, sqrt(3)]); BuMa                # needs sage.symbolic
            [ 1/2*sqrt3*I + 1/2                  1 -1/2*sqrt3*I - 1/2]
            [ 1/2*sqrt3*I + 1/2 -1/2*sqrt3*I + 1/2                  0]
            [                 1                  0                  0]
            sage: BuMa.base_ring()                                                      # needs sage.symbolic
            Number Field in I with defining polynomial x^2 + 1 over its base field

            sage: BuMa = ele.burau_matrix(characteristic=7); BuMa
            [3 1 4]
            [3 5 0]
            [1 0 0]
            sage: BuMa.base_ring()
            Finite Field of size 7

            sage: # needs sage.rings.finite_rings
            sage: BuMa = ele.burau_matrix(characteristic=2); BuMa
            [t + 1     1 t + 1]
            [t + 1     t     0]
            [    1     0     0]
            sage: BuMa.base_ring()
            Finite Field in t of size 2^2
            sage: F4.<r64> = GF(4)
            sage: BuMa = ele.burau_matrix(root_bur=r64); BuMa
            [r64 + 1       1 r64 + 1]
            [r64 + 1     r64       0]
            [      1       0       0]
            sage: BuMa.base_ring()
            Finite Field in r64 of size 2^2
            sage: BuMa = ele.burau_matrix(domain=GF(5)); BuMa
            [2*t + 2       1 3*t + 3]
            [2*t + 2 3*t + 4       0]
            [      1       0       0]
            sage: BuMa.base_ring()
            Finite Field in t of size 5^2

            sage: # needs sage.rings.number_field
            sage: BuMa, BuMaAd, H = ele.burau_matrix(reduced='unitary'); BuMa
            [       0 zeta12^3]
            [zeta12^3        0]
            sage: BuMa * H * BuMaAd == H
            True
            sage: BuMa.base_ring()
            Cyclotomic Field of order 12 and degree 4
            sage: BuMa, BuMaAd, H = ele.burau_matrix(domain=QQ[I, sqrt(3)],             # needs sage.symbolic
            ....:                                    reduced='unitary'); BuMa
            [0 I]
            [I 0]
            sage: BuMa.base_ring()                                                      # needs sage.symbolic
            Number Field in I with defining polynomial x^2 + 1 over its base field
        """

class CubicBraidGroup(UniqueRepresentation, FinitelyPresentedGroup):
    """
    Factor groups of the Artin braid group mapping their generators to elements
    of order 3.

    These groups are implemented as a particular case of finitely presented
    groups similar to the :class:`BraidGroup_class`.

    A cubic braid group can be created by giving the number of strands, and
    the name of the generators in a similar way as it works for the
    :class:`BraidGroup_class`.

    INPUT:

    - ``names`` -- see the corresponding documentation of :class:`BraidGroup_class`
    - ``cbg_type`` -- (default: ``CubicBraidGroup.type.Coxeter``;
      see explanation below) enum type :class:`CubicBraidGroup.type`

    Setting the keyword ``cbg_type`` to one on the values
    ``CubicBraidGroup.type.AssionS`` or ``CubicBraidGroup.type.AssionU``,
    the additional relations due to Assion are added:

    .. MATH::

        \\begin{array}{lll}
        \\mbox{S:} & s_3 s_1 t_2 s_1 t_2^{-1} t_3 t_2 s_1 t_2^{-1} t_3^{-1} = 1
                  & \\mbox{ for } m >= 5 \\mbox{ in case } S(m), \\\\\n        \\mbox{U:} & t_1 t_3 = 1
                  & \\mbox{ for } m >= 5 \\mbox{ in case } U(m),
        \\end{array}

    where `t_i = (s_i s_{i+1})^3`. If ``cbg_type == CubicBraidGroup.type.Coxeter``
    (default) only the cubic relation on the generators is active (Coxeter's
    case of investigation). Note that for `n = 2, 3, 4`, the groups do not
    differ between the three possible values of ``cbg_type`` (as finitely
    presented groups). However, the ``CubicBraidGroup.type.Coxeter``,
    ``CubicBraidGroup.type.AssionS`` and ``CubicBraidGroup.type.AssionU``
    are different, so they have different classical realizations implemented.

    .. SEEALSO::

        Instances can also be constructed more easily by using
        :func:`CubicBraidGroup`, :func:`AssionGroupS` and :func:`AssionGroupU`.

    EXAMPLES::

        sage: U3 = CubicBraidGroup(3, cbg_type=CubicBraidGroup.type.AssionU); U3
        Assion group on 3 strands of type U
        sage: U3.gens()
        (c0, c1)

    Alternative possibilities defining ``U3``::

        sage: U3 = AssionGroupU(3); U3
        Assion group on 3 strands of type U
        sage: U3.gens()
        (u0, u1)
        sage: U3.<u1,u2> = AssionGroupU(3); U3
        Assion group on 3 strands of type U
        sage: U3.gens()
        (u1, u2)

    Alternates naming the generators::

        sage: U3 = AssionGroupU(3, 'a, b'); U3
        Assion group on 3 strands of type U
        sage: U3.gens()
        (a, b)
        sage: C3 = CubicBraidGroup(3, 't'); C3
        Cubic Braid group on 3 strands
        sage: C3.gens()
        (t0, t1)
        sage: U3.is_isomorphic(C3)
        True
        sage: U3.as_classical_group()
        Subgroup generated by [(1,7,6)(3,19,14)(4,15,10)(5,11,18)(12,16,20),
                               (1,12,13)(2,15,19)(4,9,14)(5,18,8)(6,21,16)]
         of (The projective general unitary group of degree 3 over Finite Field of size 2)
        sage: C3.as_classical_group()
        Subgroup with 2 generators (
        [  E(3)^2        0]  [       1 -E(12)^7]
        [-E(12)^7        1], [       0   E(3)^2]
        ) of General Unitary Group of degree 2 over Universal Cyclotomic Field
        with respect to positive definite hermitian form
        [-E(12)^7 + E(12)^11                  -1]
        [                 -1 -E(12)^7 + E(12)^11]

    REFERENCES:

    - [Cox1957]_
    - [Ass1978]_
    """
    Element = CubicBraidElement
    class type(Enum):
        """
        Enum class to select the type of the group:

        - ``Coxeter`` -- ``'C'`` the full cubic braid group
        - ``AssionS`` -- ``'S'`` finite factor group of type S considered by Assion
        - ``AssionU`` -- ``'U'`` finite factor group of type U considered by Assion

        EXAMPLES::

            sage: S2 = CubicBraidGroup(2, cbg_type=CubicBraidGroup.type.AssionS); S2
            Assion group on 2 strands of type S
            sage: U3 = CubicBraidGroup(2, cbg_type='U')
            Traceback (most recent call last):
            ...
            TypeError: the cbg_type must be an instance of <enum 'CubicBraidGroup.type'>
        """
        Coxeter = 'C'
        AssionS = 'S'
        AssionU = 'U'
    @staticmethod
    def __classcall_private__(cls, n=None, names: str = 'c', cbg_type=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: C3 = CubicBraidGroup(3); C3.generators()
            (c0, c1)
            sage: CubicBraidGroup(3, 'g').generators()
            (g0, g1)
            sage: U3.<u1,u2>=CubicBraidGroup(3, cbg_type=CubicBraidGroup.type.AssionU); U3.generators()
            (u1, u2)
        """
    def __init__(self, names, cbg_type=None) -> None:
        """
        Python constructor.

        TESTS::

            sage: C3 = CubicBraidGroup(3)    # indirect doctest
            sage: TestSuite(C3).run()
            sage: C4 = CubicBraidGroup(4)    # indirect doctest
            sage: TestSuite(C4).run()        # long time
            sage: C6 = CubicBraidGroup(6)    # indirect doctest
            sage: TestSuite(C6).run()        # long time
            sage: S3 = AssionGroupS(3)       # indirect doctest
            sage: TestSuite(S3).run()
            sage: S5 = AssionGroupS(5)       # indirect doctest
            sage: TestSuite(S5).run()        # long time
            sage: U3 = AssionGroupU(3)       # indirect doctest
            sage: TestSuite(U3).run()
            sage: U4 = AssionGroupU(4)       # indirect doctest
            sage: TestSuite(U4).run()        # long time
            sage: U5 = AssionGroupU(5)       # indirect doctest
            sage: TestSuite(U5).run()        # long time
        """
    def index_set(self):
        """
        Return the index set of ``self``.

        This is the set of integers `0,\\dots,n-2` where `n` is
        the number of strands.

        This is only used when ``self`` is a finite reflection group.

        EXAMPLES::

            sage: CubicBraidGroup(3).index_set()
            [0, 1]
        """
    def simple_reflections(self):
        """
        Return the generators of ``self``.

        This is only used when ``self`` is a finite reflection group.

        EXAMPLES::

            sage: CubicBraidGroup(3).simple_reflections()
            (c0, c1)
        """
    def degrees(self):
        """
        Return the degrees of ``self``.

        This only makes sense when ``self`` is a finite reflection group.

        EXAMPLES::

            sage: CubicBraidGroup(4).degrees()
            (6, 9, 12)
        """
    def codegrees(self):
        """
        Return the codegrees of ``self``.

        This only makes sense when ``self`` is a finite reflection group.

        EXAMPLES::

            sage: CubicBraidGroup(5).codegrees()
            (0, 6, 12, 18)
        """
    def strands(self):
        """
        Return the number of strands of the braid group whose image is ``self``.

        OUTPUT: :class:`Integer`

        EXAMPLES::

            sage: C4 = CubicBraidGroup(4)
            sage: C4.strands()
            4
        """
    def braid_group(self):
        """
        Return a :class:`BraidGroup` with identical generators, such that
        there exists an epimorphism to ``self``.

        OUTPUT: a :class:`BraidGroup` having conversion maps to and from
        ``self`` (which is just a section in the latter case)

        EXAMPLES::

            sage: U5 = AssionGroupU(5); U5
            Assion group on 5 strands of type U
            sage: B5 = U5.braid_group(); B5
            Braid group on 5 strands
            sage: b = B5([4,3,2,-4,1])
            sage: u = U5([4,3,2,-4,1])
            sage: u == b
            False
            sage: b.burau_matrix()
            [ 1 - t      t      0      0      0]
            [ 1 - t      0      t      0      0]
            [ 1 - t      0      0      0      t]
            [ 1 - t      0      0      1 -1 + t]
            [     1      0      0      0      0]
            sage: u.burau_matrix()
            [t + 1     t     0     0     0]
            [t + 1     0     t     0     0]
            [t + 1     0     0     0     t]
            [t + 1     0     0     1 t + 1]
            [    1     0     0     0     0]
            sage: bU = U5(b)
            sage: uB = B5(u)
            sage: bU == u
            True
            sage: uB == b
            True
        """
    @cached_method
    def as_matrix_group(self, root_bur=None, domain=None, characteristic=None, var: str = 't', reduced: bool = False):
        """
        Create an epimorphic image of ``self`` as a matrix group by use of
        the burau representation.

        INPUT:

        - ``root_bur`` -- (default: root of unity over `\\QQ`) six (resp. twelfth)
          root of unity in some field
        - ``domain`` -- (default: cyclotomic field of order 3 and degree 2, resp.
          the domain of ``root_bur`` if given) base ring for the Burau matrix
        - ``characteristic`` -- integer (optional); the characteristic of the
          domain; if none of the keywords ``root_bur``, ``domain`` and
          ``characteristic`` are given, the default characteristic is 3
          (resp. 2) if ``self`` is of ``cbg_type``
          ``CubicBraidGroup.type.AssionS`` (resp. ``CubicBraidGroup.type.AssionU``)
        - ``var`` -- string used for the indeterminate name in case ``root_bur``
          must be constructed in a splitting field
        - ``reduced`` -- boolean (default: ``False``); for more information
          see the documentation of :meth:`Braid.burau_matrix`

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: C5 = CubicBraidGroup(5)
            sage: C5Mch5 = C5.as_matrix_group(characteristic=5); C5Mch5
            Matrix group over Finite Field in t of size 5^2 with 4 generators (
            [2*t + 2 3*t + 4       0       0       0]
            [     1       0       0       0       0]
            [     0       0       1       0       0]
            [     0       0       0       1       0]
            [     0       0       0       0       1],
            <BLANKLINE>
            [     1       0       0       0       0]
            [     0 2*t + 2 3*t + 4       0       0]
            [     0       1       0       0       0]
            [     0       0       0       1       0]
            [     0       0       0       0       1],
            <BLANKLINE>
            [     1       0       0       0       0]
            [     0       1       0       0       0]
            [     0       0 2*t + 2 3*t + 4       0]
            [     0       0       1       0       0]
            [     0       0       0       0       1],
            <BLANKLINE>
            [     1       0       0       0       0]
            [     0       1       0       0       0]
            [     0       0       1       0       0]
            [     0       0       0 2*t + 2 3*t + 4]
            [     0       0       0       1       0]
            )
            sage: c = C5([3,4,-2,-3,1]); c
            c2*c3*c1^-1*c2^-1*c0
            sage: m = C5Mch5(c); m
            [2*t + 2 3*t + 4       0       0       0]
            [     0       0       0       1       0]
            [2*t + 1       0 2*t + 2     3*t 3*t + 3]
            [2*t + 2       0       0 3*t + 4       0]
            [     0       0 2*t + 2 3*t + 4       0]
            sage: m_back = C5(m)
            sage: m_back == c
            True
            sage: U5 = AssionGroupU(5); U5
            Assion group on 5 strands of type U
            sage: U5Mch3 = U5.as_matrix_group(characteristic=3)
            Traceback (most recent call last):
            ...
            ValueError: Burau representation does not factor through the relations
        """
    @cached_method
    def as_permutation_group(self, use_classical: bool = True):
        """
        Return a permutation group isomorphic to ``self`` that has a
        group isomorphism from ``self`` as a conversion.

        INPUT:

        - ``use_classical`` -- boolean (default: ``True``); the permutation
          group is calculated via the attached classical matrix group as this
          results in a smaller degree; if ``False``, the permutation group will
          be calculated using ``self`` (as finitely presented group)

        EXAMPLES::

            sage: C3 = CubicBraidGroup(3)
            sage: PC3 = C3.as_permutation_group()
            sage: assert C3.is_isomorphic(PC3)  # random (with respect to the occurrence of the info message)
            sage: PC3.degree()
            8
            sage: c = C3([2,1-2])
            sage: C3(PC3(c)) == c
            True
        """
    def as_classical_group(self, embedded: bool = False):
        """
        Create an isomorphic image of ``self`` as a classical group according
        to the construction given by Coxeter resp. Assion.

        INPUT:

        - ``embedded`` -- boolean (default: ``False``); this boolean effects the
          cases of Assion groups when they are realized as projective groups only.
          More precisely: if ``self`` is of ``cbg_type CubicBraidGroup.type.AssionS``
          (for example) and the number of strands ``n`` is even, than its classical
          group is a subgroup of ``PSp(n,3)`` (being centralized by the element
          ``self.centralizing_element(projective=True))``. By default this group
          will be given. Setting ``embedded = True`` the classical realization
          is given as subgroup of its classical enlargement with one more strand
          (in this case as subgroup of ``Sp(n,3))``.

        OUTPUT:

        Depending on the type of ``self`` and the number of strands an
        instance of ``Sp(n-1,3)``, ``GU(n-1,2)``, subgroup of ``PSp(n,3)``,
        ``PGU(n,2)``, or a subgroup of ``GU(n-1, UCF)``
        (``cbg_type == CubicBraidGroup.type.Coxeter``) with respect to a
        certain Hermitian form attached to the Burau representation
        (used by Coxeter and Squier). Here ``UCF`` stands for the universal
        cyclotomic field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: U3 = AssionGroupU(3)
            sage: U3Cl = U3.as_classical_group(); U3Cl
            Subgroup generated by [(1,7,6)(3,19,14)(4,15,10)(5,11,18)(12,16,20),
                                   (1,12,13)(2,15,19)(4,9,14)(5,18,8)(6,21,16)] of
             (The projective general unitary group of degree 3 over Finite Field of size 2)
            sage: U3Clemb = U3.as_classical_group(embedded=True); U3Clemb
            Subgroup with 2 generators (
            [0 0 a]  [a + 1     a     a]
            [0 1 0]  [    a a + 1     a]
            [a 0 a], [    a     a a + 1]
            ) of General Unitary Group of degree 3 over Finite Field in a of size 2^2
            sage: u = U3([-2,1,-2,1]); u
            (u1^-1*u0)^2
            sage: uCl = U3Cl(u); uCl
            (1,16)(2,9)(3,10)(4,19)(6,12)(7,20)(13,21)(14,15)
            sage: uCle = U3Clemb(u); uCle
            [a + 1 a + 1     1]
            [a + 1     0     a]
            [   1     a     a]
            sage: U3(uCl) == u
            True
            sage: U3(uCle) == u
            True
            sage: U4 = AssionGroupU(4)
            sage: U4Cl = U4.as_classical_group(); U4Cl
            General Unitary Group of degree 3 over Finite Field in a of size 2^2
            sage: U3Clemb.ambient() == U4Cl
            True

            sage: # needs sage.rings.number_field
            sage: C4 = CubicBraidGroup(4)
            sage: C4Cl = C4.as_classical_group(); C4Cl
            Subgroup with 3 generators (
            [  E(3)^2        0        0]  [       1 -E(12)^7        0]
            [-E(12)^7        1        0]  [       0   E(3)^2        0]
            [       0        0        1], [       0 -E(12)^7        1],
            <BLANKLINE>
            [       1        0        0]
            [       0        1 -E(12)^7]
            [       0        0   E(3)^2]
            ) of General Unitary Group of degree 3 over Universal Cyclotomic Field
            with respect to positive definite hermitian form
            [-E(12)^7 + E(12)^11                  -1                   0]
            [                 -1 -E(12)^7 + E(12)^11                  -1]
            [                  0                  -1 -E(12)^7 + E(12)^11]
        """
    def as_reflection_group(self):
        """
        Return an isomorphic image of ``self`` as irreducible complex
        reflection group.

        This is possible only for the finite cubic braid groups of ``cbg_type``
        ``CubicBraidGroup.type.Coxeter``.

        .. NOTE::

            This method uses the sage implementation of reflection group via
            the ``gap3`` ``CHEVIE`` package. These must be installed in order
            to use this method.

        EXAMPLES::

           sage: # optional - gap3
           sage: C3.<c1,c2> = CubicBraidGroup(3)
           sage: R3 = C3.as_reflection_group(); R3
           Irreducible complex reflection group of rank 2 and type ST4
           sage: R3.cartan_matrix()
           [-2*E(3) - E(3)^2           E(3)^2]
           [        -E(3)^2 -2*E(3) - E(3)^2]
           sage: R3.simple_roots()
           Finite family {1: (0, -2*E(3) - E(3)^2), 2: (2*E(3)^2, E(3)^2)}
           sage: R3.simple_coroots()
           Finite family {1: (0, 1), 2: (1/3*E(3) - 1/3*E(3)^2, 1/3*E(3) - 1/3*E(3)^2)}

        Conversion maps::

           sage: # optional - gap3
           sage: r = R3.an_element()
           sage: cr = C3(r); cr
           c1*c2
           sage: mr = r.matrix(); mr
           [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
           [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
           sage: C3Cl = C3.as_classical_group()
           sage: C3Cl(cr)
           [ E(3)^2    -E(4)]
           [-E(12)^7        0]

        The reflection groups can also be viewed as subgroups of unitary groups
        over the universal cyclotomic field. Note that the unitary group
        corresponding to the reflection group is isomorphic but different from
        the classical group due to different hermitian forms for the unitary
        groups they live in::

           sage: # optional - gap3
           sage: C4 = CubicBraidGroup(4)
           sage: R4 = C4.as_reflection_group()
           sage: R4.invariant_form()
           [1 0 0]
           [0 1 0]
           [0 0 1]
           sage: _ == C4.classical_invariant_form()
           False
        """
    def classical_invariant_form(self):
        """
        Return the invariant form of the classical realization of ``self``.

        OUTPUT:

        A square matrix of dimension according to the space the classical
        realization is operating on. In the case of the full cubic braid groups
        and of the Assion groups of ``cbg_type CubicBraidGroup.type.AssionU``
        the matrix is Hermitian. In the case of the Assion groups of
        ``cbg_type CubicBraidGroup.type.AssionS`` it is alternating.
        Note that the invariant form of the full cubic braid group on more
        than 5 strands is degenerated (causing the group to be infinite).

        In the case of Assion groups having projective classical groups,
        the invariant form corresponds to the ambient group of its
        classical embedding.

        EXAMPLES::

            sage: S3 = AssionGroupS(3)
            sage: S3.classical_invariant_form()
            [0 1]
            [2 0]
            sage: S4 = AssionGroupS(4)
            sage: S4.classical_invariant_form()
            [0 0 0 1]
            [0 0 1 0]
            [0 2 0 0]
            [2 0 0 0]
            sage: S5 = AssionGroupS(5)
            sage: S4.classical_invariant_form() == S5.classical_invariant_form()
            True
            sage: U4 = AssionGroupU(4)
            sage: U4.classical_invariant_form()
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: C5 = CubicBraidGroup(5)
            sage: C5.classical_invariant_form()
            [-E(12)^7 + E(12)^11                  -1                   0                   0]
            [                -1 -E(12)^7 + E(12)^11                  -1                   0]
            [                 0                  -1 -E(12)^7 + E(12)^11                  -1]
            [                 0                   0                  -1 -E(12)^7 + E(12)^11]
            sage: _.is_singular()
            False
            sage: C6 = CubicBraidGroup(6)
            sage: C6.classical_invariant_form().is_singular()
            True
        """
    def centralizing_element(self, embedded: bool = False):
        """
        Return the centralizing element defined by the work of Assion
        (Hilfssatz 1.1.3 and 1.2.3).

        INPUT:

        - ``embedded`` -- boolean (default; ``False``); this boolean only effects
          the cases of Assion groups when they are realized as projective groups.
          More precisely: if ``self`` is of ``cbg_type CubicBraidGroup.type.AssionS``
          (for example) and the number of strands ``n`` is even, than its
          classical group is a subgroup of ``PSp(n,3)`` being centralized
          by the element return for option ``embedded=False``. Otherwise the
          image of this element inside the embedded classical group will be
          returned (see option embedded of :meth:`classical_group`).

        OUTPUT:

        Depending on the optional keyword a permutation as an element
        of ``PSp(n,3)`` (type S) or ``PGU(n,2)`` (type U) for ``n = 0 mod 2``
        (type S) resp. ``n = 0 mod 3`` (type U) is returned. Otherwise, the
        centralizing element is a matrix belonging to ``Sp(n,3)``
        resp. ``GU(n,2)``.

        EXAMPLES::

            sage: U3 = AssionGroupU(3);  U3
            Assion group on 3 strands of type U
            sage: U3Cl = U3.as_classical_group(); U3Cl
            Subgroup generated by [(1,7,6)(3,19,14)(4,15,10)(5,11,18)(12,16,20),
                                   (1,12,13)(2,15,19)(4,9,14)(5,18,8)(6,21,16)]
             of (The projective general unitary group of degree 3 over Finite Field of size 2)
            sage: c = U3.centralizing_element(); c
            (1,16)(2,9)(3,10)(4,19)(6,12)(7,20)(13,21)(14,15)
            sage: c in U3Cl
            True
            sage: P = U3Cl.ambient_group()
            sage: P.centralizer(c) == U3Cl
            True

        Embedded version::

            sage: cm = U3.centralizing_element(embedded=True); cm
            [a + 1 a + 1     1]
            [a + 1     0     a]
            [   1     a     a]
            sage: U4 = AssionGroupU(4)
            sage: U4Cl = U4.as_classical_group()
            sage: cm in U4Cl
            True
            sage: [cm * U4Cl(g) == U4Cl(g) * cm for g in U4.gens()]
            [True, True, False]
        """
    def order(self):
        """
        To avoid long wait-time on calculations the order will be obtained
        using the classical realization.

        OUTPUT: cardinality of the group as integer or infinity

        EXAMPLES::

            sage: S15 = AssionGroupS(15)
            sage: S15.order()
            109777561863482259035023554842176139436811616256000
            sage: C6 = CubicBraidGroup(6)
            sage: C6.order()
            +Infinity
        """
    cardinality = order
    def is_finite(self):
        """
        Return if ``self`` is a finite group or not.

        EXAMPLES::

            sage: CubicBraidGroup(6).is_finite()
            False
            sage: AssionGroupS(6).is_finite()
            True
        """
    def cubic_braid_subgroup(self, nstrands=None):
        """
        Return a cubic braid group as subgroup of ``self`` on the first
        ``nstrands`` strands.

        INPUT:

        - ``nstrands`` -- (default: ``self.strands() - 1``) integer at least 1
          and at most  ``self.strands()`` giving the number of strands of
          the subgroup

        .. WARNING::

            Since ``self`` is inherited from :class:`UniqueRepresentation`, the
            obtained instance is identical to other instances created with the
            same arguments (see example below). The ambient group corresponds
            to the last call of this method.

        EXAMPLES::

            sage: U5 = AssionGroupU(5)
            sage: U3s = U5.cubic_braid_subgroup(3)
            sage: u1, u2 = U3s.gens()
            sage: u1 in U5
            False
            sage: U5(u1) in U5.gens()
            True
            sage: U3s is AssionGroupU(3)
            True
            sage: U3s.ambient() == U5
            True
        """
