from sage.arith.misc import factorial as factorial
from sage.coding.codecan.codecan import PartitionRefinementLinearCode as PartitionRefinementLinearCode
from sage.combinat.permutation import Permutation as Permutation
from typing import Any, overload

class LinearCodeAutGroupCanLabel:
    """File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 135)

        Canonical representatives and automorphism group computation for linear
        codes over finite fields.

        There are several notions of equivalence for linear codes:
        Let `C`, `D` be linear codes of length `n` and dimension `k`.
        The codes `C` and `D` are said to be

        - permutational equivalent, if there is some permutation `\\pi \\in S_n`
          such that `(c_{\\pi(0)}, \\ldots, c_{\\pi(n-1)}) \\in D` for all `c \\in C`.

        - linear equivalent, if there is some permutation `\\pi \\in S_n` and a
          vector `\\phi \\in {\\GF{q}^*}^n` of units of length `n` such that
          `(c_{\\pi(0)} \\phi_0^{-1}, \\ldots, c_{\\pi(n-1)} \\phi_{n-1}^{-1}) \\in D`
          for all `c \\in C`.

        - semilinear equivalent, if there is some permutation `\\pi \\in S_n`, a
          vector `\\phi` of units of length `n` and a field automorphism `\\alpha`
          such that
          `(\\alpha(c_{\\pi(0)}) \\phi_0^{-1}, \\ldots, \\alpha( c_{\\pi(n-1)}) \\phi_{n-1}^{-1} ) \\in D`
          for all `c \\in C`.

        These are group actions. This class provides an algorithm that will compute
        a unique representative `D` in the orbit of the given linear code `C`.
        Furthermore, the group element `g` with `g * C = D` and the automorphism
        group of `C` will be computed as well.

        There is also the possibility to restrict the permutational part of this
        action to a Young subgroup of `S_n`. This could be achieved by passing a
        partition `P` (as a list of lists) of the set `\\{0, \\ldots, n-1\\}`. This is
        an option which is also available in the computation of a canonical form of
        a graph, see :meth:`sage.graphs.generic_graph.GenericGraph.canonical_label`.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(3), 3).dual_code()
            sage: P = LinearCodeAutGroupCanLabel(C)
            sage: P.get_canonical_form().generator_matrix()
            [1 0 0 0 0 1 1 1 1 1 1 1 1]
            [0 1 0 1 1 0 0 1 1 2 2 1 2]
            [0 0 1 1 2 1 2 1 2 1 2 0 0]
            sage: LinearCode(P.get_transporter()*C.generator_matrix()) == P.get_canonical_form()
            True
            sage: a = P.get_autom_gens()[0]
            sage: (a*C.generator_matrix()).echelon_form() == C.generator_matrix().echelon_form()
            True
            sage: P.get_autom_order() == GL(3, GF(3)).order()
            True
    """
    def __init__(self, C, P=..., algorithm_type=...) -> Any:
        """LinearCodeAutGroupCanLabel.__init__(self, C, P=None, algorithm_type='semilinear')

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 187)

        See :class:`LinearCodeAutGroupCanLabel`.

        INPUT:

        - ``C`` -- a linear code

        - ``P`` -- (optional) a coloring of the coordinates i.e. a partition
          (list of disjoint lists) of [0 , ..., C.length()-1 ]

        - ``algorithm_type`` -- (optional) defines the acting group, either

            * ``permutational``

            * ``linear``

            * ``semilinear``

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: P = LinearCodeAutGroupCanLabel(C)
            sage: P.get_canonical_form().generator_matrix()
            [1 0 0 0 1 1 1]
            [0 1 0 1 0 1 1]
            [0 0 1 1 1 1 0]
            sage: P2 = LinearCodeAutGroupCanLabel(C, P=[[0,3,5],[1,2,4,6]],
            ....:      algorithm_type='permutational')
            sage: P2.get_canonical_form().generator_matrix()
            [1 1 1 0 0 0 1]
            [0 1 0 1 1 0 1]
            [0 0 1 0 1 1 1]"""
    def get_PGammaL_gens(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_PGammaL_gens(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 595)

        Return the set of generators translated to the group `P\\Gamma L(k,q)`.

        There is a geometric point of view of code equivalence. A linear
        code is identified with the multiset of points in the finite projective
        geometry `PG(k-1, q)`. The equivalence of codes translates to the
        natural action of `P\\Gamma L(k,q)`. Therefore, we may interpret the
        group as a subgroup of `P\\Gamma L(k,q)` as well.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(4, 'a'), 3).dual_code()
            sage: A = LinearCodeAutGroupCanLabel(C).get_PGammaL_gens()
            sage: Gamma = C.generator_matrix()
            sage: N = [ x.monic() for x in Gamma.columns() ]
            sage: all((g[0]*n.apply_map(g[1])).monic() in N for n in N for g in A)
            True"""
    def get_PGammaL_order(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_PGammaL_order(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 623)

        Return the size of the automorphism group as a subgroup of
        `P\\Gamma L(k,q)`.

        There is a geometric point of view of code equivalence. A linear
        code is identified with the multiset of points in the finite projective
        geometry `PG(k-1, q)`. The equivalence of codes translates to the
        natural action of `P\\Gamma L(k,q)`. Therefore, we may interpret the
        group as a subgroup of `P\\Gamma L(k,q)` as well.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(4, 'a'), 3).dual_code()
            sage: LinearCodeAutGroupCanLabel(C).get_PGammaL_order() == GL(3, GF(4, 'a')).order()*2/3
            True"""
    @overload
    def get_autom_gens(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_autom_gens(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 567)

        Return a generating set for the automorphism group of the code.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: A = LinearCodeAutGroupCanLabel(C).get_autom_gens()
            sage: Gamma = C.generator_matrix().echelon_form()
            sage: all((g*Gamma).echelon_form() == Gamma for g in A)
            True"""
    @overload
    def get_autom_gens(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_autom_gens(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 567)

        Return a generating set for the automorphism group of the code.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: A = LinearCodeAutGroupCanLabel(C).get_autom_gens()
            sage: Gamma = C.generator_matrix().echelon_form()
            sage: all((g*Gamma).echelon_form() == Gamma for g in A)
            True"""
    @overload
    def get_autom_order(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_autom_order(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 582)

        Return the size of the automorphism group of the code.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: LinearCodeAutGroupCanLabel(C).get_autom_order()
            168"""
    @overload
    def get_autom_order(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_autom_order(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 582)

        Return the size of the automorphism group of the code.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: LinearCodeAutGroupCanLabel(C).get_autom_order()
            168"""
    @overload
    def get_canonical_form(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 534)

        Return the canonical orbit representative we computed.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(3), 3).dual_code()
            sage: CF1 = LinearCodeAutGroupCanLabel(C).get_canonical_form()
            sage: s = SemimonomialTransformationGroup(GF(3), C.length()).an_element()
            sage: C2 = LinearCode(s*C.generator_matrix())
            sage: CF2 = LinearCodeAutGroupCanLabel(C2).get_canonical_form()
            sage: CF1 == CF2
            True"""
    @overload
    def get_canonical_form(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 534)

        Return the canonical orbit representative we computed.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(3), 3).dual_code()
            sage: CF1 = LinearCodeAutGroupCanLabel(C).get_canonical_form()
            sage: s = SemimonomialTransformationGroup(GF(3), C.length()).an_element()
            sage: C2 = LinearCode(s*C.generator_matrix())
            sage: CF2 = LinearCodeAutGroupCanLabel(C2).get_canonical_form()
            sage: CF1 == CF2
            True"""
    @overload
    def get_canonical_form(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 534)

        Return the canonical orbit representative we computed.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(3), 3).dual_code()
            sage: CF1 = LinearCodeAutGroupCanLabel(C).get_canonical_form()
            sage: s = SemimonomialTransformationGroup(GF(3), C.length()).an_element()
            sage: C2 = LinearCode(s*C.generator_matrix())
            sage: CF2 = LinearCodeAutGroupCanLabel(C2).get_canonical_form()
            sage: CF1 == CF2
            True"""
    @overload
    def get_transporter(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_transporter(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 551)

        Return the element which maps the code to its canonical form.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: P = LinearCodeAutGroupCanLabel(C)
            sage: g = P.get_transporter()
            sage: D = P.get_canonical_form()
            sage: (g*C.generator_matrix()).echelon_form() == D.generator_matrix().echelon_form()
            True"""
    @overload
    def get_transporter(self) -> Any:
        """LinearCodeAutGroupCanLabel.get_transporter(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/autgroup_can_label.pyx (starting at line 551)

        Return the element which maps the code to its canonical form.

        EXAMPLES::

            sage: from sage.coding.codecan.autgroup_can_label import LinearCodeAutGroupCanLabel
            sage: C = codes.HammingCode(GF(2), 3).dual_code()
            sage: P = LinearCodeAutGroupCanLabel(C)
            sage: g = P.get_transporter()
            sage: D = P.get_canonical_form()
            sage: (g*C.generator_matrix()).echelon_form() == D.generator_matrix().echelon_form()
            True"""
