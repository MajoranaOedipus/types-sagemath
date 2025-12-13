from sage.arith.functions import lcm as lcm
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modular.abvar.torsion_point import TorsionPoint as TorsionPoint
from sage.modules.free_module import FreeModule_generic as FreeModule_generic
from sage.modules.module import Module as Module
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import coercion_model as coercion_model
from sage.structure.gens_py import abelian_iterator as abelian_iterator
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sequence import Sequence as Sequence

class FiniteSubgroup(Module):
    """
    A finite subgroup of a modular abelian variety.

    INPUT:

    - ``abvar`` -- a modular abelian variety

    - ``field_of_definition`` -- a field over which this group is defined

    EXAMPLES:

    This is an abstract base class, so there are no instances of
    this class itself::

        sage: A = J0(37)
        sage: G = A.torsion_subgroup(3); G
        Finite subgroup with invariants [3, 3, 3, 3] over QQ of Abelian variety J0(37) of dimension 2
        sage: type(G)
        <class 'sage.modular.abvar.finite_subgroup.FiniteSubgroup_lattice_with_category'>
        sage: from sage.modular.abvar.finite_subgroup import FiniteSubgroup
        sage: isinstance(G, FiniteSubgroup)
        True
    """
    Element = TorsionPoint
    def __init__(self, abvar, field_of_definition=...) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = J0(11)
            sage: G = A.torsion_subgroup(2)
            sage: TestSuite(G).run() # long time
        """
    def lattice(self) -> None:
        """
        Return the lattice corresponding to this subgroup in the rational
        homology of the modular Jacobian product. The elements of the
        subgroup are represented by vectors in the ambient vector space
        (the rational homology), and this returns the lattice they span.
        EXAMPLES::

            sage: J = J0(33); C = J[0].cuspidal_subgroup(); C
            Finite subgroup with invariants [5] over QQ of
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: C.lattice()
            Free module of degree 6 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1/5 13/5   -2 -4/5    2 -1/5]
            [   0    3   -2   -1    2    0]
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        If ``other`` is not a :class:`FiniteSubgroup`, then
        ``NotImplemented`` is returned. If ``other`` is a
        :class:`FiniteSubgroup` and the ambient abelian varieties are
        not equal, then the ambient abelian varieties are compared.
        If ``other`` is a :class:`FiniteSubgroup` and the ambient
        abelian varieties are equal, then the subgroups are compared
        via their corresponding lattices.

        EXAMPLES:

        We first compare two subgroups of `J_0(37)`::

            sage: A = J0(37)
            sage: G = A.torsion_subgroup(3); G.order()
            81
            sage: H = A.cuspidal_subgroup(); H.order()
            3
            sage: H < G
            True
            sage: H.is_subgroup(G)
            True

        The ambient varieties are compared::

            sage: A[0].cuspidal_subgroup() > J0(11).cuspidal_subgroup()
            True

        Comparing subgroups sitting in different abelian varieties::

            sage: A[0].cuspidal_subgroup() < A[1].cuspidal_subgroup()
            True
        """
    def is_subgroup(self, other) -> bool:
        """
        Return ``True`` exactly if ``self`` is a subgroup of ``other``,
        and both are defined as subgroups of the same ambient abelian variety.

        EXAMPLES::

            sage: C = J0(22).cuspidal_subgroup()
            sage: H = C.subgroup([C.0])
            sage: K = C.subgroup([C.1])
            sage: H.is_subgroup(K)
            False
            sage: K.is_subgroup(H)
            False
            sage: K.is_subgroup(C)
            True
            sage: H.is_subgroup(C)
            True
        """
    def __add__(self, other):
        """
        Return the sum of two subgroups.

        EXAMPLES::

            sage: C = J0(22).cuspidal_subgroup()
            sage: C.gens()
            ([(1/5, 1/5, 4/5, 0)], [(0, 0, 0, 1/5)])
            sage: A = C.subgroup([C.0]); B = C.subgroup([C.1])
            sage: A + B == C
            True

        An example where the parent abelian varieties are different::

            sage: A = J0(48); A[0].cuspidal_subgroup() + A[1].cuspidal_subgroup()
            Finite subgroup with invariants [2, 4, 4] over QQ of
             Abelian subvariety of dimension 2 of J0(48)
        """
    def exponent(self):
        """
        Return the exponent of this finite abelian group.

        OUTPUT: integer

        EXAMPLES::

            sage: t = J0(33).hecke_operator(7)
            sage: G = t.kernel()[0]; G
            Finite subgroup with invariants [2, 2, 2, 2, 4, 4] over QQ of
             Abelian variety J0(33) of dimension 3
            sage: G.exponent()
            4
        """
    def intersection(self, other):
        """
        Return the intersection of the finite subgroups ``self`` and ``other``.

        INPUT:

        - ``other`` -- a finite group

        OUTPUT: a finite group

        EXAMPLES::

            sage: E11a0, E11a1, B = J0(33)
            sage: G = E11a0.torsion_subgroup(6); H = E11a0.torsion_subgroup(9)
            sage: G.intersection(H)
            Finite subgroup with invariants [3, 3] over QQ of
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: W = E11a1.torsion_subgroup(15)
            sage: G.intersection(W)
            Finite subgroup with invariants [] over QQ of
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: E11a0.intersection(E11a1)[0]
            Finite subgroup with invariants [5] over QQ of
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)

        We intersect subgroups of different abelian varieties.

        ::

            sage: E11a0, E11a1, B = J0(33)
            sage: G = E11a0.torsion_subgroup(5); H = E11a1.torsion_subgroup(5)
            sage: G.intersection(H)
            Finite subgroup with invariants [5] over QQ of
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: E11a0.intersection(E11a1)[0]
            Finite subgroup with invariants [5] over QQ of
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)

        We intersect abelian varieties with subgroups::

            sage: t = J0(33).hecke_operator(7)
            sage: G = t.kernel()[0]; G
            Finite subgroup with invariants [2, 2, 2, 2, 4, 4] over QQ of
             Abelian variety J0(33) of dimension 3
            sage: A = J0(33).old_subvariety()
            sage: A.intersection(G)
            Finite subgroup with invariants [2, 2, 2, 2] over QQ of
             Abelian subvariety of dimension 2 of J0(33)
            sage: A.hecke_operator(7).kernel()[0]
            Finite subgroup with invariants [2, 2, 2, 2] over QQ of
             Abelian subvariety of dimension 2 of J0(33)
            sage: B = J0(33).new_subvariety()
            sage: B.intersection(G)
            Finite subgroup with invariants [4, 4] over QQ of
             Abelian subvariety of dimension 1 of J0(33)
            sage: B.hecke_operator(7).kernel()[0]
            Finite subgroup with invariants [4, 4] over QQ of
             Abelian subvariety of dimension 1 of J0(33)
            sage: A.intersection(B)[0]
            Finite subgroup with invariants [3, 3] over QQ of
             Abelian subvariety of dimension 2 of J0(33)
        """
    def __mul__(self, right):
        """
        Multiply this subgroup by the rational number ``right``.

        If ``right`` is an integer the result is a subgroup of ``self``. If
        ``right`` is a rational number `n/m`, then this group is first
        divided by `m` then multiplied by `n`.

        INPUT:

        - ``right`` -- a rational number

        OUTPUT: a subgroup

        EXAMPLES::

            sage: J = J0(37)
            sage: H = J.cuspidal_subgroup(); H.order()
            3
            sage: G = H * 3; G.order()
            1
            sage: G = H * (1/2); G.order()
            48
            sage: J.torsion_subgroup(2) + H == G
            True
            sage: G = H*(3/2); G.order()
            16
            sage: J = J0(42)
            sage: G = J.cuspidal_subgroup(); factor(G.order())
            2^8 * 3^2
            sage: (G * 3).order()
            256
            sage: (G * 0).order()
            1
            sage: (G * (1/5)).order()
            22500000000
        """
    def __rmul__(self, left):
        """
        Multiply this finite subgroup on the left by an integer.

        EXAMPLES::

            sage: J = J0(42)
            sage: G = J.cuspidal_subgroup(); factor(G.order())
            2^8 * 3^2
            sage: H = G.__rmul__(2)
            sage: H.order().factor()
            2^4 * 3^2
            sage: 2*G
            Finite subgroup with invariants [6, 24] over QQ of Abelian variety J0(42) of dimension 5
        """
    def abelian_variety(self):
        """
        Return the abelian variety that this is a finite subgroup of.

        EXAMPLES::

            sage: J = J0(42)
            sage: G = J.rational_torsion_subgroup(); G
            Torsion subgroup of Abelian variety J0(42) of dimension 5
            sage: G.abelian_variety()
            Abelian variety J0(42) of dimension 5
        """
    def field_of_definition(self):
        """
        Return the field over which this finite modular abelian variety
        subgroup is defined. This is a field over which this subgroup is
        defined.

        EXAMPLES::

            sage: J = J0(42)
            sage: G = J.rational_torsion_subgroup(); G
            Torsion subgroup of Abelian variety J0(42) of dimension 5
            sage: G.field_of_definition()
            Rational Field
        """
    def order(self):
        """
        Return the order (number of elements) of this finite subgroup.

        EXAMPLES::

            sage: J = J0(42)
            sage: C = J.cuspidal_subgroup()
            sage: C.order()
            2304
        """
    def gens(self) -> tuple:
        """
        Return a tuple of the generators for this finite subgroup.

        EXAMPLES:

        We list generators for several cuspidal subgroups::

            sage: J0(11).cuspidal_subgroup().gens()
            ([(0, 1/5)],)
            sage: J0(37).cuspidal_subgroup().gens()
            ([(0, 0, 0, 1/3)],)
            sage: J0(43).cuspidal_subgroup().gens()
            ([(0, 1/7, 0, 6/7, 0, 5/7)],)
            sage: J1(13).cuspidal_subgroup().gens()
            ([(1/19, 0, 9/19, 9/19)], [(0, 1/19, 0, 9/19)])
            sage: J0(22).torsion_subgroup(6).gens()
            ([(1/6, 0, 0, 0)], [(0, 1/6, 0, 0)], [(0, 0, 1/6, 0)], [(0, 0, 0, 1/6)])
        """
    def gen(self, n):
        """
        Return `n`-th generator of ``self``.

        EXAMPLES::

            sage: J = J0(23)
            sage: C = J.torsion_subgroup(3)
            sage: C.gens()
            ([(1/3, 0, 0, 0)], [(0, 1/3, 0, 0)], [(0, 0, 1/3, 0)], [(0, 0, 0, 1/3)])
            sage: C.gen(0)
            [(1/3, 0, 0, 0)]
            sage: C.gen(3)
            [(0, 0, 0, 1/3)]
            sage: C.gen(4)
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range

        Negative indices wrap around::

            sage: C.gen(-1)
            [(0, 0, 0, 1/3)]
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is contained in this finite subgroup.

        EXAMPLES:

        We define two distinct finite subgroups of `J_0(27)`::

            sage: G1 = J0(27).rational_cusp_subgroup(); G1
            Finite subgroup with invariants [3] over QQ of Abelian variety J0(27) of dimension 1
            sage: G1.0
            [(1/3, 0)]
            sage: G2 = J0(27).cuspidal_subgroup(); G2
            Finite subgroup with invariants [3, 3] over QQ of Abelian variety J0(27) of dimension 1
            sage: G2.gens()
            ([(1/3, 0)], [(0, 1/3)])

        Now we check whether various elements are in `G_1` and `G_2`::

            sage: G2.0 in G1
            True
            sage: G2.1 in G1
            False
            sage: G1.0 in G1
            True
            sage: G1.0 in G2
            True

        The integer `0` is in `G_1`::

            sage: 0 in G1
            True

        Elements that have a completely different ambient product Jacobian
        are never in `G`::

            sage: J0(23).cuspidal_subgroup().0 in G1
            False
            sage: J0(23).cuspidal_subgroup()(0) in G1
            False
        """
    def subgroup(self, gens):
        """
        Return the subgroup of ``self`` spanned by the given
        generators, which must all be elements of ``self``.

        EXAMPLES::

            sage: J = J0(23)
            sage: G = J.torsion_subgroup(11); G
            Finite subgroup with invariants [11, 11, 11, 11] over QQ of
             Abelian variety J0(23) of dimension 2

        We create the subgroup of the 11-torsion subgroup of `J_0(23)`
        generated by the first `11`-torsion point::

            sage: H = G.subgroup([G.0]); H
            Finite subgroup with invariants [11] over QQbar of
             Abelian variety J0(23) of dimension 2
            sage: H.invariants()
            [11]

        We can also create a subgroup from a list of objects that can
        be converted into the ambient rational homology::

            sage: H == G.subgroup([[1/11,0,0,0]])
            True
        """
    def invariants(self):
        """
        Return elementary invariants of this abelian group, by which we
        mean a nondecreasing (immutable) sequence of integers
        `n_i`, `1 \\leq i \\leq k`, with `n_i`
        dividing `n_{i+1}`, and such that this group is abstractly
        isomorphic to
        `\\ZZ/n_1\\ZZ \\times\\cdots\\times \\ZZ/n_k\\ZZ.`

        EXAMPLES::

            sage: J = J0(38)
            sage: C = J.cuspidal_subgroup(); C
            Finite subgroup with invariants [3, 45] over QQ of
             Abelian variety J0(38) of dimension 4
            sage: v = C.invariants(); v
            [3, 45]
            sage: v[0] = 5
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: type(v[0])
            <class 'sage.rings.integer.Integer'>

        ::

            sage: C * 3
            Finite subgroup with invariants [15] over QQ of
             Abelian variety J0(38) of dimension 4

        An example involving another cuspidal subgroup::

            sage: C = J0(22).cuspidal_subgroup(); C
            Finite subgroup with invariants [5, 5] over QQ of
             Abelian variety J0(22) of dimension 2
            sage: C.lattice()
            Free module of degree 4 and rank 4 over Integer Ring
            Echelon basis matrix:
            [1/5 1/5 4/5   0]
            [  0   1   0   0]
            [  0   0   1   0]
            [  0   0   0 1/5]
            sage: C.invariants()
            [5, 5]
        """
    __iter__ = abelian_iterator

class FiniteSubgroup_lattice(FiniteSubgroup):
    def __init__(self, abvar, lattice, field_of_definition=None, check: bool = True) -> None:
        """
        A finite subgroup of a modular abelian variety that is defined by a
        given lattice.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        - ``lattice`` -- a lattice that contains the lattice of abvar

        - ``field_of_definition`` -- the field of definition
          of this finite group scheme

        - ``check`` -- boolean (default: ``True``); whether or not to
          check that lattice contains the abvar lattice

        EXAMPLES::

            sage: J = J0(11)
            sage: G = J.finite_subgroup([[1/3,0], [0,1/5]]); G
            Finite subgroup with invariants [15] over QQbar of
             Abelian variety J0(11) of dimension 1
        """
    def lattice(self):
        """
        Return lattice that defines this finite subgroup.

        EXAMPLES::

            sage: J = J0(11)
            sage: G = J.finite_subgroup([[1/3,0], [0,1/5]]); G
            Finite subgroup with invariants [15] over QQbar of
             Abelian variety J0(11) of dimension 1
            sage: G.lattice()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1/3   0]
            [  0 1/5]
        """
