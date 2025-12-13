from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.matrix.constructor import matrix as matrix
from sage.misc.flatten import flatten as flatten
from sage.misc.functional import is_even as is_even, is_odd as is_odd
from sage.modules.free_module_element import vector as vector
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

def branch_weyl_character(chi, R, S, rule: str = 'default'):
    '''
    A branching rule describes the restriction of representations from
    a Lie group or algebra `G` to a subgroup `H`. See for example, R. C.
    King, Branching rules for classical Lie groups using tensor and
    spinor methods. J. Phys. A 8 (1975), 429-449, Howe, Tan and
    Willenbring, Stable branching rules for classical symmetric pairs,
    Trans. Amer. Math. Soc. 357 (2005), no. 4, 1601-1626, McKay and
    Patera, Tables of Dimensions, Indices and Branching Rules for
    Representations of Simple Lie Algebras (Marcel Dekker, 1981),
    and Fauser, Jarvis, King and Wybourne, New branching rules induced
    by plethysm. J. Phys. A 39 (2006), no. 11, 2611--2655. If `H\\subset G`
    we will write `G\\Rightarrow H` to denote the branching rule, which
    is a homomorphism of WeylCharacterRings.

    INPUT:

    - ``chi`` -- a character of `G`

    - ``R`` -- the Weyl Character Ring of `G`

    - ``S`` -- the Weyl Character Ring of `H`

    - ``rule`` -- an element of the ``BranchingRule`` class
      or one (most usually) a keyword such as:

      * ``\'levi\'``
      * ``\'automorphic\'``
      * ``\'symmetric\'``
      * ``\'extended\'``
      * ``\'orthogonal_sum\'``
      * ``\'tensor\'``
      * ``\'triality\'``
      * ``\'miscellaneous\'``

    The :class:`BranchingRule` class is a wrapper for functions
    from the weight lattice of `G` to the weight lattice of `H`.
    An instance of this class encodes an embedding of `H` into
    `G`. The usual way to specify an embedding is to supply a
    keyword, which tells Sage to use one of the built-in rules.
    We will discuss these first.

    To explain the predefined rules, we survey the most important
    branching rules. These may be classified into several cases, and
    once this is understood, the detailed classification can be read
    off from the Dynkin diagrams. Dynkin classified the maximal
    subgroups of Lie groups in Mat. Sbornik N.S. 30(72):349-462 (1952).

    We will list give predefined rules that cover most cases where the
    branching rule is to a maximal subgroup. For convenience, we
    also give some branching rules to subgroups that are not maximal.
    For example, a Levi subgroup may or may not be maximal.

    For example, there is a "levi" branching rule defined from `SL(5)` (with
    Cartan type `A_4`) to `SL(4)` (with Cartan type `A_3`), so
    we may compute the branching rule as follows:

    EXAMPLES::

        sage: A3=WeylCharacterRing("A3",style=\'coroots\')
        sage: A2=WeylCharacterRing("A2",style=\'coroots\')
        sage: [A3(fw).branch(A2,rule=\'levi\') for fw in A3.fundamental_weights()]
        [A2(0,0) + A2(1,0), A2(0,1) + A2(1,0), A2(0,0) + A2(0,1)]

    In this case the Levi branching rule is the default branching rule
    so we may omit the specification rule="levi".

    If a subgroup is not maximal, you may specify a branching rule
    by finding a chain of intermediate subgroups. For this
    purpose, branching rules may be multiplied as in the following
    example.

    EXAMPLES::

        sage: A4=WeylCharacterRing("A4",style=\'coroots\')
        sage: A2=WeylCharacterRing("A2",style=\'coroots\')
        sage: br=branching_rule("A4","A3")*branching_rule("A3","A2")
        sage: A4(1,0,0,0).branch(A2,rule=br)
        2*A2(0,0) + A2(1,0)

    You may try omitting the rule if it is "obvious". Default
    rules are provided for the following cases:

    .. MATH::

        \\begin{aligned}
        A_{2s} & \\Rightarrow B_s,
        \\\\ A_{2s-1} & \\Rightarrow C_s,
        \\\\ A_{2*s-1} & \\Rightarrow D_s.
        \\end{aligned}

    The above default rules correspond to embedding the group
    `SO(2s+1)`, `Sp(2s)` or `SO(2s)` into the corresponding general
    or special linear group by the standard representation. Default
    rules are also specified for the following cases:

    .. MATH::

        \\begin{aligned}
        B_{s+1} & \\Rightarrow D_s,
        \\\\ D_s & \\Rightarrow B_s.
        \\end{aligned}

    These correspond to the embedding of `O(n)` into `O(n+1)` where
    `n = 2s` or `2s + 1`. Finally, the branching rule for the embedding of
    a Levi subgroup is also implemented as a default rule.

    EXAMPLES::

        sage: A1 = WeylCharacterRing("A1", style=\'coroots\')
        sage: A2 = WeylCharacterRing("A2", style=\'coroots\')
        sage: D4 = WeylCharacterRing("D4", style=\'coroots\')
        sage: B3 = WeylCharacterRing("B3", style=\'coroots\')
        sage: B4 = WeylCharacterRing("B4", style=\'coroots\')
        sage: A6 = WeylCharacterRing("A6", style=\'coroots\')
        sage: A7 = WeylCharacterRing("A7", style=\'coroots\')
        sage: def try_default_rule(R, S): return [R(f).branch(S) for f in R.fundamental_weights()]
        sage: try_default_rule(A2,A1)
        [A1(0) + A1(1), A1(0) + A1(1)]
        sage: try_default_rule(D4,B3)
        [B3(0,0,0) + B3(1,0,0), B3(1,0,0) + B3(0,1,0), B3(0,0,1), B3(0,0,1)]
        sage: try_default_rule(B4,D4)
        [D4(0,0,0,0) + D4(1,0,0,0), D4(1,0,0,0) + D4(0,1,0,0),
        D4(0,1,0,0) + D4(0,0,1,1), D4(0,0,1,0) + D4(0,0,0,1)]
        sage: try_default_rule(A7,D4)
        [D4(1,0,0,0), D4(0,1,0,0), D4(0,0,1,1), D4(0,0,2,0) + D4(0,0,0,2),
        D4(0,0,1,1),
        D4(0,1,0,0),
        D4(1,0,0,0)]
        sage: try_default_rule(A6,B3)
        [B3(1,0,0), B3(0,1,0), B3(0,0,2), B3(0,0,2), B3(0,1,0), B3(1,0,0)]

    If a default rule is not known, you may cue Sage as to what the
    Lie group embedding is by supplying a rule from the list of
    predefined rules. We will treat these next.

    .. RUBRIC:: Levi Type

    These can be read off from the Dynkin diagram. If
    removing a node from the Dynkin diagram produces another Dynkin
    diagram, there is a branching rule. A Levi subgroup may
    or may not be maximal. If it is maximal, there may or may not
    be a built-in branching rule for but you may obtain the
    Levi branching rule by first branching to a suitable
    maximal subgroup. For these rules use the option ``rule="levi"``:

    .. MATH::

        \\begin{aligned}
        A_r & \\Rightarrow A_{r-1}
        \\\\ B_r & \\Rightarrow A_{r-1}
        \\\\ B_r & \\Rightarrow B_{r-1}
        \\\\ C_r & \\Rightarrow A_{r-1}
        \\\\ C_r & \\Rightarrow C_{r-1}
        \\\\ D_r & \\Rightarrow A_{r-1}
        \\\\ D_r & \\Rightarrow D_{r-1}
        \\\\ E_r & \\Rightarrow A_{r-1} \\quad r = 7,8
        \\\\ E_r & \\Rightarrow D_{r-1} \\quad r = 6,7,8
        \\\\ E_r & \\Rightarrow E_{r-1}
        \\\\ F_4 & \\Rightarrow B_3
        \\\\ F_4 & \\Rightarrow C_3
        \\\\ G_2 & \\Rightarrow A_1 \\text{(short root)}
        \\end{aligned}

    Not all Levi subgroups are maximal subgroups. If the Levi is not
    maximal there may or may not be a preprogrammed ``rule="levi"`` for
    it. If there is not, the branching rule may still be obtained by going
    through an intermediate subgroup that is maximal using rule="extended".
    Thus the other Levi branching rule from `G_2 \\Rightarrow A_1` corresponding to the
    long root is available by first branching `G_2 \\Rightarrow A_2` then `A_2 \\Rightarrow A_1`.
    Similarly the branching rules to the Levi subgroup:

    .. MATH::

        E_r \\Rightarrow A_{r-1} \\quad r = 6,7,8

    may be obtained by first branching `E_6 \\Rightarrow A_5 \\times A_1`, `E_7 \\Rightarrow A_7`
    or `E_8 \\Rightarrow A_8`.

    EXAMPLES::

        sage: A1 = WeylCharacterRing("A1")
        sage: A2 = WeylCharacterRing("A2")
        sage: A3 = WeylCharacterRing("A3")
        sage: A4 = WeylCharacterRing("A4")
        sage: A5 = WeylCharacterRing("A5")
        sage: B2 = WeylCharacterRing("B2")
        sage: B3 = WeylCharacterRing("B3")
        sage: B4 = WeylCharacterRing("B4")
        sage: C2 = WeylCharacterRing("C2")
        sage: C3 = WeylCharacterRing("C3")
        sage: D3 = WeylCharacterRing("D3")
        sage: D4 = WeylCharacterRing("D4")
        sage: G2 = WeylCharacterRing("G2")
        sage: F4 = WeylCharacterRing("F4",style=\'coroots\')
        sage: E6=WeylCharacterRing("E6",style=\'coroots\')
        sage: E7=WeylCharacterRing("E7",style=\'coroots\')
        sage: D5=WeylCharacterRing("D5",style=\'coroots\')
        sage: D6=WeylCharacterRing("D6",style=\'coroots\')
        sage: [B3(w).branch(A2,rule=\'levi\') for w in B3.fundamental_weights()]
        [A2(0,0,0) + A2(1,0,0) + A2(0,0,-1),
        A2(0,0,0) + A2(1,0,0) + A2(1,1,0) + A2(1,0,-1) + A2(0,-1,-1) + A2(0,0,-1),
        A2(-1/2,-1/2,-1/2) + A2(1/2,-1/2,-1/2) + A2(1/2,1/2,-1/2) + A2(1/2,1/2,1/2)]

    The last example must be understood as follows. The representation
    of `B_3` being branched is spin, which is not a representation of
    `SO(7)` but of its double cover `\\mathrm{spin}(7)`. The group `A_2` is
    really GL(3) and the double cover of `SO(7)` induces a cover of `GL(3)`
    that is trivial over `SL(3)` but not over the center of `GL(3)`. The weight
    lattice for this `GL(3)` consists of triples `(a,b,c)` of half integers
    such that `a - b` and `b - c` are in `\\ZZ`, and this is reflected in the
    last decomposition.

    ::

        sage: [C3(w).branch(A2,rule=\'levi\') for w in C3.fundamental_weights()]
        [A2(1,0,0) + A2(0,0,-1),
        A2(1,1,0) + A2(1,0,-1) + A2(0,-1,-1),
        A2(-1,-1,-1) + A2(1,-1,-1) + A2(1,1,-1) + A2(1,1,1)]
        sage: [D4(w).branch(A3,rule=\'levi\') for w in D4.fundamental_weights()]
        [A3(1,0,0,0) + A3(0,0,0,-1),
        A3(0,0,0,0) + A3(1,1,0,0) + A3(1,0,0,-1) + A3(0,0,-1,-1),
        A3(1/2,-1/2,-1/2,-1/2) + A3(1/2,1/2,1/2,-1/2),
        A3(-1/2,-1/2,-1/2,-1/2) + A3(1/2,1/2,-1/2,-1/2) + A3(1/2,1/2,1/2,1/2)]
        sage: [B3(w).branch(B2,rule=\'levi\') for w in B3.fundamental_weights()]
        [2*B2(0,0) + B2(1,0), B2(0,0) + 2*B2(1,0) + B2(1,1), 2*B2(1/2,1/2)]
        sage: C3 = WeylCharacterRing([\'C\',3])
        sage: [C3(w).branch(C2,rule=\'levi\') for w in C3.fundamental_weights()]
        [2*C2(0,0) + C2(1,0),
         C2(0,0) + 2*C2(1,0) + C2(1,1),
         C2(1,0) + 2*C2(1,1)]
        sage: [D5(w).branch(D4,rule=\'levi\') for w in D5.fundamental_weights()]
        [2*D4(0,0,0,0) + D4(1,0,0,0),
         D4(0,0,0,0) + 2*D4(1,0,0,0) + D4(1,1,0,0),
         D4(1,0,0,0) + 2*D4(1,1,0,0) + D4(1,1,1,0),
         D4(1/2,1/2,1/2,-1/2) + D4(1/2,1/2,1/2,1/2),
         D4(1/2,1/2,1/2,-1/2) + D4(1/2,1/2,1/2,1/2)]
        sage: G2(1,0,-1).branch(A1,rule=\'levi\')
        A1(1,0) + A1(1,-1) + A1(0,-1)
        sage: E6=WeylCharacterRing("E6",style=\'coroots\')
        sage: D5=WeylCharacterRing("D5",style=\'coroots\')
        sage: fw = E6.fundamental_weights()
        sage: [E6(fw[i]).branch(D5,rule=\'levi\') for i in [1,2,6]]
        [D5(0,0,0,0,0) + D5(0,0,0,0,1) + D5(1,0,0,0,0),
         D5(0,0,0,0,0) + D5(0,0,0,1,0) + D5(0,0,0,0,1) + D5(0,1,0,0,0),
         D5(0,0,0,0,0) + D5(0,0,0,1,0) + D5(1,0,0,0,0)]
         sage: E7=WeylCharacterRing("E7",style=\'coroots\')
         sage: A3xA3xA1=WeylCharacterRing("A3xA3xA1",style=\'coroots\')
         sage: E7(1,0,0,0,0,0,0).branch(A3xA3xA1,rule=\'extended\') # long time (0.7s)
         A3xA3xA1(0,0,1,0,0,1,1) + A3xA3xA1(0,1,0,0,1,0,0) + A3xA3xA1(1,0,0,1,0,0,1) +
          A3xA3xA1(1,0,1,0,0,0,0) + A3xA3xA1(0,0,0,1,0,1,0) + A3xA3xA1(0,0,0,0,0,0,2)
        sage: fw = E7.fundamental_weights()
        sage: [E7(fw[i]).branch(D6,rule=\'levi\') for i in [1,2,7]] # long time (0.3s)
        [3*D6(0,0,0,0,0,0) + 2*D6(0,0,0,0,1,0) + D6(0,1,0,0,0,0),
         3*D6(0,0,0,0,0,1) + 2*D6(1,0,0,0,0,0) + 2*D6(0,0,1,0,0,0) + D6(1,0,0,0,1,0),
         D6(0,0,0,0,0,1) + 2*D6(1,0,0,0,0,0)]
        sage: D7=WeylCharacterRing("D7",style=\'coroots\')
        sage: E8=WeylCharacterRing("E8",style=\'coroots\')
        sage: D7=WeylCharacterRing("D7",style=\'coroots\')
        sage: E8(1,0,0,0,0,0,0,0).branch(D7,rule=\'levi\') # long time (7s)
         3*D7(0,0,0,0,0,0,0) + 2*D7(0,0,0,0,0,1,0) + 2*D7(0,0,0,0,0,0,1) + 2*D7(1,0,0,0,0,0,0)
         + D7(0,1,0,0,0,0,0) + 2*D7(0,0,1,0,0,0,0) + D7(0,0,0,1,0,0,0) + D7(1,0,0,0,0,1,0) + D7(1,0,0,0,0,0,1) + D7(2,0,0,0,0,0,0)
        sage: E8(0,0,0,0,0,0,0,1).branch(D7,rule=\'levi\') # long time (0.6s)
         D7(0,0,0,0,0,0,0) + D7(0,0,0,0,0,1,0) + D7(0,0,0,0,0,0,1) + 2*D7(1,0,0,0,0,0,0) + D7(0,1,0,0,0,0,0)
        sage: [F4(fw).branch(B3,rule=\'levi\') for fw in F4.fundamental_weights()] # long time (1s)
         [B3(0,0,0) + 2*B3(1/2,1/2,1/2) + 2*B3(1,0,0) + B3(1,1,0),
         B3(0,0,0) + 6*B3(1/2,1/2,1/2) + 5*B3(1,0,0) + 7*B3(1,1,0) + 3*B3(1,1,1)
         + 6*B3(3/2,1/2,1/2) + 2*B3(3/2,3/2,1/2) + B3(2,0,0) + 2*B3(2,1,0) + B3(2,1,1),
         3*B3(0,0,0) + 6*B3(1/2,1/2,1/2) + 4*B3(1,0,0) + 3*B3(1,1,0) + B3(1,1,1) + 2*B3(3/2,1/2,1/2),
         3*B3(0,0,0) + 2*B3(1/2,1/2,1/2) + B3(1,0,0)]
        sage: [F4(fw).branch(C3,rule=\'levi\') for fw in F4.fundamental_weights()] # long time (1s)
         [3*C3(0,0,0) + 2*C3(1,1,1) + C3(2,0,0),
         3*C3(0,0,0) + 6*C3(1,1,1) + 4*C3(2,0,0) + 2*C3(2,1,0) + 3*C3(2,2,0) + C3(2,2,2) + C3(3,1,0) + 2*C3(3,1,1),
         2*C3(1,0,0) + 3*C3(1,1,0) + C3(2,0,0) + 2*C3(2,1,0) + C3(2,1,1),
         2*C3(1,0,0) + C3(1,1,0)]
        sage: A1xA1 = WeylCharacterRing("A1xA1")
        sage: [A3(hwv).branch(A1xA1,rule=\'levi\') for hwv in A3.fundamental_weights()]
        [A1xA1(1,0,0,0) + A1xA1(0,0,1,0),
        A1xA1(1,1,0,0) + A1xA1(1,0,1,0) + A1xA1(0,0,1,1),
        A1xA1(1,1,1,0) + A1xA1(1,0,1,1)]
        sage: A1xB1=WeylCharacterRing("A1xB1",style=\'coroots\')
        sage: [B3(x).branch(A1xB1,rule=\'levi\') for x in B3.fundamental_weights()]
        [2*A1xB1(1,0) + A1xB1(0,2),
        3*A1xB1(0,0) + 2*A1xB1(1,2) + A1xB1(2,0) + A1xB1(0,2),
        A1xB1(1,1) + 2*A1xB1(0,1)]

    .. RUBRIC:: Automorphic Type

    If the Dynkin diagram has a symmetry, then there
    is an automorphism that is a special case of a branching rule.
    There is also an exotic "triality" automorphism of `D_4` having order 3.
    Use ``rule="automorphic"`` (or for `D_4` ``rule="triality"``):

    .. MATH::

        \\begin{aligned}
        A_r & \\Rightarrow A_r
        \\\\ D_r & \\Rightarrow D_r
        \\\\ E_6 & \\Rightarrow E_6
        \\end{aligned}

    EXAMPLES::

        sage: [A3(chi).branch(A3,rule=\'automorphic\') for chi in A3.fundamental_weights()]
        [A3(0,0,0,-1), A3(0,0,-1,-1), A3(0,-1,-1,-1)]
        sage: [D4(chi).branch(D4,rule=\'automorphic\') for chi in D4.fundamental_weights()]
        [D4(1,0,0,0), D4(1,1,0,0), D4(1/2,1/2,1/2,1/2), D4(1/2,1/2,1/2,-1/2)]

    Here is an example with `D_4` triality::

        sage: [D4(chi).branch(D4,rule=\'triality\') for chi in D4.fundamental_weights()]
        [D4(1/2,1/2,1/2,-1/2), D4(1,1,0,0), D4(1/2,1/2,1/2,1/2), D4(1,0,0,0)]

    .. RUBRIC:: Symmetric Type

    Related to the automorphic type, when `G` admits
    an outer automorphism (usually of degree 2) we may consider
    the branching rule to the isotropy subgroup `H`. Outer
    automorphisms correspond to symmetries of the Dynkin diagram.
    For such isotropy subgroups use ``rule="symmetric"``.
    We may thus obtain the following branching rules.

    .. MATH::

        A_{2r} & \\Rightarrow B_r
        \\\\ A_{2r-1} & \\Rightarrow C_r
        \\\\ A_{2r-1} & \\Rightarrow D_r
        \\\\ D_r & \\Rightarrow B_{r-1}
        \\\\ E_6 & \\Rightarrow F_4
        \\\\ E_6 & \\Rightarrow C_4
        \\\\ D_4 & \\Rightarrow G_2

    The last branching rule, `D_4 \\Rightarrow G_2` is not to a maximal subgroup
    since `D_4 \\Rightarrow B_3 \\Rightarrow G_2`, but it is included for convenience.

    In some cases, two outer automorphisms that differ by an
    inner automorphism may have different fixed subgroups.
    Thus, while the Dynkin diagram of `E_6` has a single
    involutory automorphism, there are two involutions
    of the group (differing by an inner automorphism) with
    fixed subgroups `F_4` and `C_4`. Similarly
    `SL(2r)`, of Cartan type `A_{2r-1}`, has subgroups
    `SO(2r)` and `Sp(2r)`, both fixed subgroups of outer
    automorphisms that differ from each other by an inner
    automorphism.

    In many cases the Dynkin diagram of `H` can be obtained by
    folding the Dynkin diagram of `G`.

    EXAMPLES::

        sage: [w.branch(B2,rule=\'symmetric\') for w in [A4(1,0,0,0,0),A4(1,1,0,0,0),A4(1,1,1,0,0),A4(2,0,0,0,0)]]
        [B2(1,0), B2(1,1), B2(1,1), B2(0,0) + B2(2,0)]
        sage: [A5(w).branch(C3,rule=\'symmetric\') for w in A5.fundamental_weights()]
        [C3(1,0,0), C3(0,0,0) + C3(1,1,0), C3(1,0,0) + C3(1,1,1), C3(0,0,0) + C3(1,1,0), C3(1,0,0)]
        sage: [A5(w).branch(D3,rule=\'symmetric\') for w in A5.fundamental_weights()]
        [D3(1,0,0), D3(1,1,0), D3(1,1,-1) + D3(1,1,1), D3(1,1,0), D3(1,0,0)]
        sage: [D4(x).branch(B3,rule=\'symmetric\') for x in D4.fundamental_weights()]
        [B3(0,0,0) + B3(1,0,0), B3(1,0,0) + B3(1,1,0), B3(1/2,1/2,1/2), B3(1/2,1/2,1/2)]
        sage: [D4(x).branch(G2,rule=\'symmetric\') for x in D4.fundamental_weights()]
        [G2(0,0,0) + G2(1,0,-1), 2*G2(1,0,-1) + G2(2,-1,-1), G2(0,0,0) + G2(1,0,-1), G2(0,0,0) + G2(1,0,-1)]
        sage: [E6(fw).branch(F4,rule=\'symmetric\') for fw in E6.fundamental_weights()] # long time (4s)
        [F4(0,0,0,0) + F4(0,0,0,1),
         F4(0,0,0,1) + F4(1,0,0,0),
         F4(0,0,0,1) + F4(1,0,0,0) + F4(0,0,1,0),
         F4(1,0,0,0) + 2*F4(0,0,1,0) + F4(1,0,0,1) + F4(0,1,0,0),
         F4(0,0,0,1) + F4(1,0,0,0) + F4(0,0,1,0),
         F4(0,0,0,0) + F4(0,0,0,1)]
        sage: E6=WeylCharacterRing("E6",style=\'coroots\')
        sage: C4=WeylCharacterRing("C4",style=\'coroots\')
        sage: chi = E6(1,0,0,0,0,0); chi.degree()
        27
        sage: chi.branch(C4,rule=\'symmetric\')
        C4(0,1,0,0)

    .. RUBRIC:: Extended Type

    If removing a node from the extended Dynkin diagram
    results in a Dynkin diagram, then there is a branching rule. Use
    ``rule="extended"`` for these. We will also use this classification
    for some rules that are not of this type, mainly involving type `B`,
    such as `D_6 \\Rightarrow B_3 \\times B_3`.

    Here is the extended Dynkin diagram for `D_6`::

            0       6
            O       O
            |       |
            |       |
        O---O---O---O---O
        1   2   3   4   6

    Removing the node 3 results in an embedding `D_3 \\times D_3 \\Rightarrow D_6`.
    This corresponds to the embedding `SO(6) \\times SO(6) \\Rightarrow SO(12)`, and
    is of extended type. On the other hand the embedding `SO(5) \\times SO(7)
    \\Rightarrow SO(12)` (e.g. `B_2 \\times B_3 \\Rightarrow D_6`) cannot be explained this way
    but for uniformity is implemented under ``rule="extended"``.

    The following rules are implemented as special cases
    of ``rule="extended"``:

    .. MATH::

        \\begin{aligned}
        E_6 & \\Rightarrow A_5 \\times A_1, A_2 \\times A_2 \\times A_2
        \\\\ E_7 & \\Rightarrow A_7, D_6 \\times A_1, A_3 \\times A_3 \\times A_1
        \\\\ E_8 & \\Rightarrow A_8, D_8, E_7 \\times A_1, A_4 \\times A_4,
        D_5 \\times A_3, E_6 \\times A_2
        \\\\ F_4 & \\Rightarrow B_4, C_3 \\times A_1, A_2 \\times A_2, A_3 \\times A_1
        \\\\ G_2 & \\Rightarrow A_1 \\times A_1
        \\end{aligned}

    Note that `E_8` has only a limited number of representations of
    reasonably low degree.

    EXAMPLES::

        sage: [B3(x).branch(D3,rule=\'extended\') for x in B3.fundamental_weights()]
        [D3(0,0,0) + D3(1,0,0),
         D3(1,0,0) + D3(1,1,0),
         D3(1/2,1/2,-1/2) + D3(1/2,1/2,1/2)]
        sage: [G2(w).branch(A2, rule=\'extended\') for w in G2.fundamental_weights()]
        [A2(0,0,0) + A2(1/3,1/3,-2/3) + A2(2/3,-1/3,-1/3),
         A2(1/3,1/3,-2/3) + A2(2/3,-1/3,-1/3) + A2(1,0,-1)]
        sage: [F4(fw).branch(B4,rule=\'extended\') for fw in F4.fundamental_weights()] # long time (2s)
        [B4(1/2,1/2,1/2,1/2) + B4(1,1,0,0),
         B4(1,1,0,0) + B4(1,1,1,0) + B4(3/2,1/2,1/2,1/2) + B4(3/2,3/2,1/2,1/2) + B4(2,1,1,0),
         B4(1/2,1/2,1/2,1/2) + B4(1,0,0,0) + B4(1,1,0,0) + B4(1,1,1,0) + B4(3/2,1/2,1/2,1/2),
         B4(0,0,0,0) + B4(1/2,1/2,1/2,1/2) + B4(1,0,0,0)]

        sage: E6 = WeylCharacterRing("E6", style=\'coroots\')
        sage: A2xA2xA2 = WeylCharacterRing("A2xA2xA2",style=\'coroots\')
        sage: A5xA1 = WeylCharacterRing("A5xA1",style=\'coroots\')
        sage: G2 = WeylCharacterRing("G2", style=\'coroots\')
        sage: A1xA1 = WeylCharacterRing("A1xA1", style=\'coroots\')
        sage: F4 = WeylCharacterRing("F4",style=\'coroots\')
        sage: A3xA1 = WeylCharacterRing("A3xA1", style=\'coroots\')
        sage: A2xA2 = WeylCharacterRing("A2xA2", style=\'coroots\')
        sage: A1xC3 = WeylCharacterRing("A1xC3",style=\'coroots\')
        sage: E6(1,0,0,0,0,0).branch(A5xA1,rule=\'extended\') # (0.7s)
         A5xA1(0,0,0,1,0,0) + A5xA1(1,0,0,0,0,1)
        sage: E6(1,0,0,0,0,0).branch(A2xA2xA2, rule=\'extended\') # (0.7s)
        A2xA2xA2(0,1,1,0,0,0) + A2xA2xA2(1,0,0,0,0,1) + A2xA2xA2(0,0,0,1,1,0)
        sage: E7 = WeylCharacterRing("E7",style=\'coroots\')
        sage: A7 = WeylCharacterRing("A7",style=\'coroots\')
        sage: E7(1,0,0,0,0,0,0).branch(A7,rule=\'extended\')
         A7(0,0,0,1,0,0,0) + A7(1,0,0,0,0,0,1)
        sage: D6xA1 = WeylCharacterRing("D6xA1",style=\'coroots\')
        sage: E7(1,0,0,0,0,0,0).branch(D6xA1,rule=\'extended\')
         D6xA1(0,0,0,0,1,0,1) + D6xA1(0,1,0,0,0,0,0) + D6xA1(0,0,0,0,0,0,2)
        sage: A5xA2 = WeylCharacterRing("A5xA2",style=\'coroots\')
        sage: E7(1,0,0,0,0,0,0).branch(A5xA2,rule=\'extended\')
        A5xA2(0,0,0,1,0,1,0) + A5xA2(0,1,0,0,0,0,1) + A5xA2(1,0,0,0,1,0,0) + A5xA2(0,0,0,0,0,1,1)
        sage: E8 = WeylCharacterRing("E8",style=\'coroots\')
        sage: D8 = WeylCharacterRing("D8",style=\'coroots\')
        sage: A8 = WeylCharacterRing("A8",style=\'coroots\')
        sage: E8(0,0,0,0,0,0,0,1).branch(D8,rule=\'extended\') # long time (0.56s)
         D8(0,0,0,0,0,0,1,0) + D8(0,1,0,0,0,0,0,0)
        sage: E8(0,0,0,0,0,0,0,1).branch(A8,rule=\'extended\') # long time (0.73s)
        A8(0,0,0,0,0,1,0,0) + A8(0,0,1,0,0,0,0,0) + A8(1,0,0,0,0,0,0,1)
        sage: F4(1,0,0,0).branch(A1xC3,rule=\'extended\') # (0.05s)
         A1xC3(1,0,0,1) + A1xC3(2,0,0,0) + A1xC3(0,2,0,0)
        sage: G2(0,1).branch(A1xA1, rule=\'extended\')
         A1xA1(2,0) + A1xA1(3,1) + A1xA1(0,2)
        sage: F4(0,0,0,1).branch(A2xA2, rule=\'extended\') # (0.4s)
         A2xA2(0,1,0,1) + A2xA2(1,0,1,0) + A2xA2(0,0,1,1)
        sage: F4(0,0,0,1).branch(A3xA1,rule=\'extended\') # (0.34s)
         A3xA1(0,0,0,0) + A3xA1(0,0,1,1) + A3xA1(0,1,0,0) + A3xA1(1,0,0,1) + A3xA1(0,0,0,2)
        sage: D4=WeylCharacterRing("D4",style=\'coroots\')
        sage: D2xD2=WeylCharacterRing("D2xD2",style=\'coroots\') # We get D4 => A1xA1xA1xA1 by remembering that A1xA1 = D2.
        sage: [D4(fw).branch(D2xD2, rule=\'extended\') for fw in D4.fundamental_weights()]
         [D2xD2(1,1,0,0) + D2xD2(0,0,1,1),
         D2xD2(2,0,0,0) + D2xD2(0,2,0,0) + D2xD2(1,1,1,1) + D2xD2(0,0,2,0) + D2xD2(0,0,0,2),
         D2xD2(1,0,0,1) + D2xD2(0,1,1,0),
         D2xD2(1,0,1,0) + D2xD2(0,1,0,1)]

    .. RUBRIC:: Orthogonal Sum

    Using ``rule="orthogonal_sum"``, for `n = a + b + c + \\cdots`,
    you can get any branching rule

    .. MATH::

        \\begin{aligned}
        SO(n) & \\Rightarrow SO(a) \\times SO(b) \\times SO(c) \\times \\cdots,
        \\\\ Sp(2n) & \\Rightarrow Sp(2a) \\times Sp(2b) \\times Sp(2c) x \\times \\cdots,
        \\end{aligned}

    where `O(a)` is type `D_r` for `a = 2r` or `B_r` for `a = 2r+1`
    and `Sp(2r)` is type `C_r`. In some cases these are also of
    extended type, as in the case `D_3 \\times D_3 \\Rightarrow D_6` discussed above.
    But in other cases, for example `B_3 \\times B_3 \\Rightarrow D_7`, they are not
    of extended type.

    .. RUBRIC:: Tensor

    There are branching rules:

    .. MATH::

        \\begin{aligned}
        A_{rs-1} & \\Rightarrow A_{r-1} \\times A_{s-1},
        \\\\ B_{2rs+r+s} & \\Rightarrow B_r \\times B_s,
        \\\\ D_{2rs+s} & \\Rightarrow B_r \\times D_s,
        \\\\ D_{2rs} & \\Rightarrow D_r \\times D_s,
        \\\\ D_{2rs} & \\Rightarrow C_r \\times C_s,
        \\\\ C_{2rs+s} & \\Rightarrow B_r \\times C_s,
        \\\\ C_{2rs} & \\Rightarrow C_r \\times D_s.
        \\end{aligned}

    corresponding to the tensor product homomorphism. For type
    `A`, the homomorphism is `GL(r) \\times GL(s) \\Rightarrow GL(rs)`. For the
    classical types, the relevant fact is that if `V, W` are
    orthogonal or symplectic spaces, that is, spaces endowed
    with symmetric or skew-symmetric bilinear forms, then `V \\otimes W`
    is also an orthogonal space (if `V` and `W` are both
    orthogonal or both symplectic) or symplectic (if one of
    `V` and `W` is orthogonal and the other symplectic).

    The corresponding branching rules are obtained using ``rule="tensor"``.

    EXAMPLES::

        sage: A5=WeylCharacterRing("A5", style=\'coroots\')
        sage: A2xA1=WeylCharacterRing("A2xA1", style=\'coroots\')
        sage: [A5(hwv).branch(A2xA1, rule=\'tensor\') for hwv in A5.fundamental_weights()]
        [A2xA1(1,0,1),
        A2xA1(0,1,2) + A2xA1(2,0,0),
        A2xA1(1,1,1) + A2xA1(0,0,3),
        A2xA1(1,0,2) + A2xA1(0,2,0),
        A2xA1(0,1,1)]
        sage: B4=WeylCharacterRing("B4",style=\'coroots\')
        sage: B1xB1=WeylCharacterRing("B1xB1",style=\'coroots\')
        sage: [B4(f).branch(B1xB1,rule=\'tensor\') for f in B4.fundamental_weights()]
        [B1xB1(2,2),
        B1xB1(2,0) + B1xB1(2,4) + B1xB1(4,2) + B1xB1(0,2),
        B1xB1(2,0) + B1xB1(2,2) + B1xB1(2,4) + B1xB1(4,2) + B1xB1(4,4) + B1xB1(6,0) + B1xB1(0,2) + B1xB1(0,6),
        B1xB1(1,3) + B1xB1(3,1)]
        sage: D4=WeylCharacterRing("D4",style=\'coroots\')
        sage: C2xC1=WeylCharacterRing("C2xC1",style=\'coroots\')
        sage: [D4(f).branch(C2xC1,rule=\'tensor\') for f in D4.fundamental_weights()]
        [C2xC1(1,0,1),
        C2xC1(0,1,2) + C2xC1(2,0,0) + C2xC1(0,0,2),
        C2xC1(1,0,1),
        C2xC1(0,1,0) + C2xC1(0,0,2)]
        sage: C3=WeylCharacterRing("C3",style=\'coroots\')
        sage: B1xC1=WeylCharacterRing("B1xC1",style=\'coroots\')
        sage: [C3(f).branch(B1xC1,rule=\'tensor\') for f in C3.fundamental_weights()]
        [B1xC1(2,1), B1xC1(2,2) + B1xC1(4,0), B1xC1(4,1) + B1xC1(0,3)]

    .. RUBRIC:: Symmetric Power

    The `k`-th symmetric and exterior power homomorphisms map

    .. MATH::

        GL(n) \\Rightarrow GL\\left(\\binom{n+k-1}{k}\\right)
        \\times GL\\left(\\binom{n}{k}\\right).

    The corresponding branching rules are not implemented but a special
    case is. The `k`-th symmetric power homomorphism `SL(2) \\Rightarrow GL(k+1)`
    has its image inside of `SO(2r+1)` if `k = 2r` and inside of `Sp(2r)` if
    `k = 2r - 1`. Hence there are branching rules:

    .. MATH::

        \\begin{aligned}
        B_r & \\Rightarrow A_1
        \\\\ C_r & \\Rightarrow A_1
        \\end{aligned}

    and these may be obtained using the rule "symmetric_power".

    EXAMPLES::

        sage: A1=WeylCharacterRing("A1",style=\'coroots\')
        sage: B3=WeylCharacterRing("B3",style=\'coroots\')
        sage: C3=WeylCharacterRing("C3",style=\'coroots\')
        sage: [B3(fw).branch(A1,rule=\'symmetric_power\') for fw in B3.fundamental_weights()]
        [A1(6), A1(2) + A1(6) + A1(10), A1(0) + A1(6)]
        sage: [C3(fw).branch(A1,rule=\'symmetric_power\') for fw in C3.fundamental_weights()]
        [A1(5), A1(4) + A1(8), A1(3) + A1(9)]

    .. RUBRIC:: Miscellaneous

    Use ``rule="miscellaneous"`` for the following embeddings of maximal subgroups,
    all involving exceptional groups.

    .. MATH::

        \\begin{aligned}
        B_3 & \\Rightarrow G_2,
        \\\\ E_6 & \\Rightarrow G_2,
        \\\\ E_6 & \\Rightarrow A_2,
        \\\\ F_4 & \\Rightarrow G_2 \\times A_1,
        \\\\ E_6 & \\Rightarrow G_2 \\times A_2,
        \\\\ E_7 & \\Rightarrow G_2 \\times C_3,
        \\\\ E_7 & \\Rightarrow F_4 \\times A_1,
        \\\\ E_7 & \\Rightarrow A_1 \\times A_1,
        \\\\ E_7 & \\Rightarrow G_2 \\times A_1,
        \\\\ E_8 & \\Rightarrow G_2 \\times F_4.
        \\\\ E_8 & \\Rightarrow A2 \\times A_1.
        \\\\ E_8 & \\Rightarrow B2.
        \\end{aligned}

    Except for those embeddings available by ``rule="extended"``, these
    are the only embeddings of these groups as maximal subgroups.
    There may be other embeddings besides these. For example,
    there are other more obvious embeddings of `A_2` and `G_2` into `E_6`.
    However the embeddings in this table are characterized as embeddings
    as maximal subgroups. Regarding the embeddings of `A_2` and `G_2` in
    `E_6`, the embeddings in question may be characterized by the condition that the
    27-dimensional representations of `E_6` restrict irreducibly to `A_2` or
    `G_2`. Since `G_2` has a subgroup isomorphic to `A_2`, it is worth
    mentioning that the composite branching rules::

        branching_rule("E6","G2","miscellaneous")*branching_rule("G2","A2","extended")
        branching_rule("E6","A2","miscellaneous")

    are distinct.

    These embeddings are described more completely (with references
    to the literature) in the thematic tutorial at:

    https://doc.sagemath.org/html/en/thematic_tutorials/lie.html

    EXAMPLES::

        sage: G2 = WeylCharacterRing("G2")
        sage: [fw1, fw2, fw3] = B3.fundamental_weights()
        sage: B3(fw1+fw3).branch(G2, rule=\'miscellaneous\')
        G2(1,0,-1) + G2(2,-1,-1) + G2(2,0,-2)
        sage: E6 = WeylCharacterRing("E6",style=\'coroots\')
        sage: G2 = WeylCharacterRing("G2",style=\'coroots\')
        sage: E6(1,0,0,0,0,0).branch(G2,"miscellaneous")
        G2(2,0)
        sage: A2=WeylCharacterRing("A2",style=\'coroots\')
        sage: E6(1,0,0,0,0,0).branch(A2,rule=\'miscellaneous\')
        A2(2,2)
        sage: E6(0,1,0,0,0,0).branch(A2,rule=\'miscellaneous\')
        A2(1,1) + A2(1,4) + A2(4,1)
        sage: E6(0,0,0,0,0,2).branch(G2,"miscellaneous") # long time (0.59s)
        G2(0,0) + G2(2,0) + G2(1,1) + G2(0,2) + G2(4,0)
        sage: F4=WeylCharacterRing("F4",style=\'coroots\')
        sage: G2xA1=WeylCharacterRing("G2xA1",style=\'coroots\')
        sage: F4(0,0,1,0).branch(G2xA1,rule=\'miscellaneous\')
        G2xA1(1,0,0) + G2xA1(1,0,2) + G2xA1(1,0,4) + G2xA1(1,0,6) + G2xA1(0,1,4) + G2xA1(2,0,2) + G2xA1(0,0,2) + G2xA1(0,0,6)
        sage: E6 = WeylCharacterRing("E6",style=\'coroots\')
        sage: A2xG2 = WeylCharacterRing("A2xG2",style=\'coroots\')
        sage: E6(1,0,0,0,0,0).branch(A2xG2,rule=\'miscellaneous\')
        A2xG2(0,1,1,0) + A2xG2(2,0,0,0)
        sage: E7=WeylCharacterRing("E7",style=\'coroots\')
        sage: G2xC3=WeylCharacterRing("G2xC3",style=\'coroots\')
        sage: E7(0,1,0,0,0,0,0).branch(G2xC3,rule=\'miscellaneous\') # long time (1.84s)
        G2xC3(1,0,1,0,0) + G2xC3(1,0,1,1,0) + G2xC3(0,1,0,0,1) + G2xC3(2,0,1,0,0) + G2xC3(0,0,1,1,0)
        sage: F4xA1=WeylCharacterRing("F4xA1",style=\'coroots\')
        sage: E7(0,0,0,0,0,0,1).branch(F4xA1,"miscellaneous")
        F4xA1(0,0,0,1,1) + F4xA1(0,0,0,0,3)
        sage: A1xA1=WeylCharacterRing("A1xA1",style=\'coroots\')
        sage: E7(0,0,0,0,0,0,1).branch(A1xA1,rule=\'miscellaneous\')
        A1xA1(2,5) + A1xA1(4,1) + A1xA1(6,3)
        sage: A2=WeylCharacterRing("A2",style=\'coroots\')
        sage: E7(0,0,0,0,0,0,1).branch(A2,rule=\'miscellaneous\')
        A2(0,6) + A2(6,0)
        sage: G2xA1=WeylCharacterRing("G2xA1",style=\'coroots\')
        sage: E7(1,0,0,0,0,0,0).branch(G2xA1,rule=\'miscellaneous\')
        G2xA1(1,0,4) + G2xA1(0,1,0) + G2xA1(2,0,2) + G2xA1(0,0,2)
        sage: E8 = WeylCharacterRing("E8",style=\'coroots\')
        sage: G2xF4 = WeylCharacterRing("G2xF4",style=\'coroots\')
        sage: E8(0,0,0,0,0,0,0,1).branch(G2xF4,rule=\'miscellaneous\') # long time (0.76s)
        G2xF4(1,0,0,0,0,1) + G2xF4(0,1,0,0,0,0) + G2xF4(0,0,1,0,0,0)
        sage: E8=WeylCharacterRing("E8",style=\'coroots\')
        sage: A1xA2=WeylCharacterRing("A1xA2",style=\'coroots\')
        sage: E8(0,0,0,0,0,0,0,1).branch(A1xA2,rule=\'miscellaneous\') # long time (0.76s)
        A1xA2(2,0,0) + A1xA2(2,2,2) + A1xA2(4,0,3) + A1xA2(4,3,0) + A1xA2(6,1,1) + A1xA2(0,1,1)
        sage: B2=WeylCharacterRing("B2",style=\'coroots\')
        sage: E8(0,0,0,0,0,0,0,1).branch(B2,rule=\'miscellaneous\') # long time (0.53s)
        B2(0,2) + B2(0,6) + B2(3,2)

    .. RUBRIC:: A1 maximal subgroups of exceptional groups

    There are seven cases where the exceptional group `G_2`, `F_4`,
    `E_7` or `E_8` contains a maximal subgroup of type `A_1`.
    These are tabulated in Theorem 1 of Testerman,
    The construction of the maximal A1\'s in the exceptional algebraic groups,
    Proc. Amer. Math. Soc. 116 (1992), no. 3, 635-644. The
    names of these branching rules are roman numerals referring
    to the seven cases of her Theorem 1. Use these branching
    rules as in the following examples.

    EXAMPLES::

        sage: A1=WeylCharacterRing("A1",style=\'coroots\')
        sage: G2=WeylCharacterRing("G2",style=\'coroots\')
        sage: F4=WeylCharacterRing("F4",style=\'coroots\')
        sage: E7=WeylCharacterRing("E7",style=\'coroots\')
        sage: E8=WeylCharacterRing("E8",style=\'coroots\')
        sage: [G2(f).branch(A1,rule=\'i\') for f in G2.fundamental_weights()]
        [A1(6), A1(2) + A1(10)]
        sage: F4(1,0,0,0).branch(A1,rule=\'ii\')
        A1(2) + A1(10) + A1(14) + A1(22)
        sage: E7(0,0,0,0,0,0,1).branch(A1,rule=\'iii\')
        A1(9) + A1(17) + A1(27)
        sage: E7(0,0,0,0,0,0,1).branch(A1,rule=\'iv\')
        A1(5) + A1(11) + A1(15) + A1(21)
        sage: E8(0,0,0,0,0,0,0,1).branch(A1,rule=\'v\') # long time (0.6s)
        A1(2) + A1(14) + A1(22) + A1(26) + A1(34) + A1(38) + A1(46) + A1(58)
        sage: E8(0,0,0,0,0,0,0,1).branch(A1,rule=\'vi\') # long time (0.6s)
        A1(2) + A1(10) + A1(14) + A1(18) + A1(22) + A1(26) + A1(28) + A1(34) + A1(38) + A1(46)
        sage: E8(0,0,0,0,0,0,0,1).branch(A1,rule=\'vii\') # long time (0.6s)
        A1(2) + A1(6) + A1(10) + A1(14) + A1(16) + A1(18) + 2*A1(22) + A1(26) + A1(28) + A1(34) + A1(38)

    .. RUBRIC:: Branching Rules From Plethysms

    Nearly all branching rules `G \\Rightarrow H` where `G` is of type `A`, `B`, `C`
    or `D` are covered by the preceding rules. The function
    :func:`branching_rule_from_plethysm` covers the remaining cases.

    This is a general rule that includes any branching rule
    from types `A`, `B`, `C`, or `D` as a special case. Thus it could be
    used in place of the above rules and would give the same
    results. However it is most useful when branching from `G`
    to a maximal subgroup `H` such that
    `\\mathrm{rank}(H) < \\mathrm{rank}(G) - 1`.

    We consider a homomorphism `H \\Rightarrow G` where `G` is one of
    `SL(r+1)`, `SO(2r+1)`, `Sp(2r)` or `SO(2r)`. The function
    :func:`branching_rule_from_plethysm` produces the corresponding
    branching rule. The main ingredient is the character
    `\\chi` of the representation of `H` that is the homomorphism
    to `GL(r+1)`, `GL(2r+1)` or `GL(2r)`.

    This rule is so powerful that it contains the other
    rules implemented above as special cases. First let
    us consider the symmetric fifth power representation
    of `SL(2)`.

    ::

        sage: A1=WeylCharacterRing("A1",style=\'coroots\')
        sage: chi=A1([5])
        sage: chi.degree()
         6
        sage: chi.frobenius_schur_indicator()
        -1

    This confirms that the character has degree 6 and
    is symplectic, so it corresponds to a homomorphism
    `SL(2) \\Rightarrow Sp(6)`, and there is a corresponding
    branching rule `C_3 \\Rightarrow A_1`.

    ::

        sage: C3 = WeylCharacterRing("C3",style=\'coroots\')
        sage: sym5rule = branching_rule_from_plethysm(chi,"C3")
        sage: [C3(hwv).branch(A1,rule=sym5rule) for hwv in C3.fundamental_weights()]
        [A1(5), A1(4) + A1(8), A1(3) + A1(9)]

    This is identical to the results we would obtain using
    ``rule="symmetric_power"``. The next example gives a branching
    not available by other standard rules.

    ::

        sage: G2 = WeylCharacterRing("G2",style=\'coroots\')
        sage: D7 = WeylCharacterRing("D7",style=\'coroots\')
        sage: ad=G2(0,1); ad.degree(); ad.frobenius_schur_indicator()
         14
         1
        sage: spin = D7(0,0,0,0,0,1,0); spin.degree()
         64
        sage: spin.branch(G2, rule=branching_rule_from_plethysm(ad, "D7"))
         G2(1,1)

    We have confirmed that the adjoint representation of `G_2`
    gives a homomorphism into `SO(14)`, and that the pullback
    of the one of the two 64 dimensional spin representations
    to `SO(14)` is an irreducible representation of `G_2`.

    We do not actually have to create the character or
    its parent WeylCharacterRing to create the
    branching rule::

        sage: b = branching_rule("C7","C3(0,0,1)","plethysm"); b
        plethysm (along C3(0,0,1)) branching rule C7 => C3

    .. RUBRIC:: Isomorphic Type

    Although not usually referred to as a branching
    rule, the effects of the accidental isomorphisms may be handled
    using ``rule="isomorphic"``:

    .. MATH::

        \\begin{aligned}
        B_2 & \\Rightarrow C_2
        \\\\ C_2 & \\Rightarrow B_2
        \\\\ A_3 & \\Rightarrow D_3
        \\\\ D_3 & \\Rightarrow A_3
        \\\\ D_2 & \\Rightarrow A_1 \\Rightarrow A_1
        \\\\ B_1 & \\Rightarrow A_1
        \\\\ C_1 & \\Rightarrow A_1
        \\end{aligned}

    EXAMPLES::

        sage: B2 = WeylCharacterRing("B2")
        sage: C2 = WeylCharacterRing("C2")
        sage: [B2(x).branch(C2, rule=\'isomorphic\') for x in B2.fundamental_weights()]
        [C2(1,1), C2(1,0)]
        sage: [C2(x).branch(B2, rule=\'isomorphic\') for x in C2.fundamental_weights()]
        [B2(1/2,1/2), B2(1,0)]
        sage: D3 = WeylCharacterRing("D3")
        sage: A3 = WeylCharacterRing("A3")
        sage: [A3(x).branch(D3,rule=\'isomorphic\') for x in A3.fundamental_weights()]
        [D3(1/2,1/2,1/2), D3(1,0,0), D3(1/2,1/2,-1/2)]
        sage: [D3(x).branch(A3,rule=\'isomorphic\') for x in D3.fundamental_weights()]
        [A3(1/2,1/2,-1/2,-1/2), A3(1/4,1/4,1/4,-3/4), A3(3/4,-1/4,-1/4,-1/4)]

    Here `A_3(x,y,z,w)` can be understood as a representation of `SL(4)`.
    The weights `x,y,z,w` and `x+t,y+t,z+t,w+t` represent the same
    representation of `SL(4)` - though not of `GL(4)` - since
    `A_3(x+t,y+t,z+t,w+t)` is the same as `A_3(x,y,z,w)` tensored with
    `\\mathrm{det}^t`. So as a representation of `SL(4)`,
    ``A3(1/4,1/4,1/4,-3/4)`` is the same as ``A3(1,1,1,0)``. The exterior
    square representation `SL(4) \\Rightarrow GL(6)` admits an invariant symmetric
    bilinear form, so is a representation `SL(4) \\Rightarrow SO(6)` that lifts to
    an isomorphism `SL(4) \\Rightarrow \\mathrm{Spin}(6)`. Conversely, there are two
    isomorphisms `SO(6) \\Rightarrow SL(4)`, of which we\'ve selected one.

    In cases like this you might prefer ``style="coroots"``::

        sage: A3 = WeylCharacterRing("A3",style=\'coroots\')
        sage: D3 = WeylCharacterRing("D3",style=\'coroots\')
        sage: [D3(fw) for fw in D3.fundamental_weights()]
        [D3(1,0,0), D3(0,1,0), D3(0,0,1)]
        sage: [D3(fw).branch(A3,rule=\'isomorphic\') for fw in D3.fundamental_weights()]
        [A3(0,1,0), A3(0,0,1), A3(1,0,0)]
        sage: D2 = WeylCharacterRing("D2", style=\'coroots\')
        sage: A1xA1 = WeylCharacterRing("A1xA1", style=\'coroots\')
        sage: [D2(fw).branch(A1xA1,rule=\'isomorphic\') for fw in D2.fundamental_weights()]
        [A1xA1(1,0), A1xA1(0,1)]

    .. RUBRIC:: Branching From a Reducible WeylCharacterRing

    If the Cartan Type of R is reducible, we may project a character onto
    any of the components, or any combination of components. The rule to
    project on the first component is specified by the string ``\'proj1\'``,
    the rule to project on the second component is ``"proj2". To
    project on the first and third components, use ``\'proj13\'`` and so on.

    EXAMPLES::

        sage: A2xG2=WeylCharacterRing("A2xG2",style=\'coroots\')
        sage: A2=WeylCharacterRing("A2",style=\'coroots\')
        sage: G2=WeylCharacterRing("G2",style=\'coroots\')
        sage: A2xG2(1,0,1,0).branch(A2,rule=\'proj1\')
        7*A2(1,0)
        sage: A2xG2(1,0,1,0).branch(G2,rule=\'proj2\')
        3*G2(1,0)
        sage: A2xA2xG2=WeylCharacterRing("A2xA2xG2",style=\'coroots\')
        sage: A2xA2xG2(0,1,1,1,0,1).branch(A2xG2,rule=\'proj13\')
        8*A2xG2(0,1,0,1)

    A more general way of specifying a branching rule from a reducible type is
    to supply a *list* of rules, one *component rule* for each
    component type in the root system. In the following example, we branch the
    fundamental representations of `D_4` down to `A_1\\times A_1\\times A_1
    \\times A_1` through the intermediate group `D_2\\times D_2`. We use
    multiplicative notation to compose the branching rules. There is no need
    to construct the intermediate WeylCharacterRing with type `D_2\\times D_2`.

    EXAMPLES::

        sage: D4 = WeylCharacterRing("D4",style=\'coroots\')
        sage: A1xA1xA1xA1 = WeylCharacterRing("A1xA1xA1xA1",style=\'coroots\')
        sage: b = branching_rule("D2","A1xA1","isomorphic")
        sage: br = branching_rule("D4","D2xD2","extended")*branching_rule("D2xD2","A1xA1xA1xA1",[b,b])
        sage: [D4(fw).branch(A1xA1xA1xA1,rule=br) for fw in D4.fundamental_weights()]
        [A1xA1xA1xA1(1,1,0,0) + A1xA1xA1xA1(0,0,1,1),
        A1xA1xA1xA1(1,1,1,1) + A1xA1xA1xA1(2,0,0,0) + A1xA1xA1xA1(0,2,0,0) + A1xA1xA1xA1(0,0,2,0) + A1xA1xA1xA1(0,0,0,2),
        A1xA1xA1xA1(1,0,0,1) + A1xA1xA1xA1(0,1,1,0),
        A1xA1xA1xA1(1,0,1,0) + A1xA1xA1xA1(0,1,0,1)]

    In the list of rules to be supplied in branching from a reducible root
    system, we may use two key words "omit" and "identity". The term "omit"
    means that we omit one factor, projecting onto the remaining factors.
    The term "identity" is supplied when the irreducible factor Cartan Types
    of both the target and the source are the same, and the component
    branching rule is to be the identity map. For example, we have
    projection maps from `A_3\\times A_2` to `A_3` and `A_2`, and
    the corresponding branching may be accomplished as follows. In
    this example the same could be accomplished using ``rule="proj2"``.

    EXAMPLES::

        sage: A3xA2=WeylCharacterRing("A3xA2",style=\'coroots\')
        sage: A3=WeylCharacterRing("A3",style=\'coroots\')
        sage: chi = A3xA2(0,1,0,1,0)
        sage: chi.branch(A3,rule=["identity","omit"])
        3*A3(0,1,0)
        sage: A2=WeylCharacterRing("A2",style=\'coroots\')
        sage: chi.branch(A2,rule=["omit","identity"])
        6*A2(1,0)

    Yet another way of branching from a reducible root system with
    repeated Cartan types is to embed along the diagonal. The
    branching rule is equivalent to the tensor product, as
    the example shows::

        sage: G2=WeylCharacterRing("G2",style=\'coroots\')
        sage: G2xG2=WeylCharacterRing("G2xG2",style=\'coroots\')
        sage: G2=WeylCharacterRing("G2",style=\'coroots\')
        sage: G2xG2(1,0,0,1).branch(G2,rule=\'diagonal\')
        G2(1,0) + G2(2,0) + G2(1,1)
        sage: G2xG2(1,0,0,1).branch(G2,rule=\'diagonal\') == G2(1,0)*G2(0,1)
        True

    .. RUBRIC:: Writing Your Own (Branching) Rules

    Suppose you want to branch from a group `G` to a subgroup `H`.
    Arrange the embedding so that a Cartan subalgebra `U` of `H` is
    contained in a Cartan subalgebra `T` of `G`. There is thus
    a mapping from the weight spaces `\\mathrm{Lie}(T)^* \\Rightarrow \\mathrm{Lie}(U)^*`.
    Two embeddings will produce identical branching rules if they
    differ by an element of the Weyl group of `H`.

    The *rule* is this map `\\mathrm{Lie}(T)^*`, which is ``G.space()``, to
    `\\mathrm{Lie}(U)^*`, which is ``H.space()``,
    which you may implement as a function. As an example, let
    us consider how to implement the branching rule `A_3 \\Rightarrow C_2`.
    Here `H = C_2 = Sp(4)` embedded as a subgroup in `A_3 = GL(4)`. The
    Cartan subalgebra `U` consists of diagonal matrices with
    eigenvalues `u_1, u_2, -u_2, -u_1`. The ``C2.space()`` is the
    two dimensional vector spaces consisting of the linear
    functionals `u_1` and `u_2` on `U`. On the other hand `\\mathrm{Lie}(T)` is
    `\\RR^4`. A convenient way to see the restriction is to
    think of it as the adjoint of the map `(u_1, u_2) \\mapsto
    (u_1,u_2, -u_2, -u_1)`,
    that is, `(x_0, x_1, x_2, x_3) \\Rightarrow (x_0 - x_3, x_1 - x_2)`. Hence we may
    encode the rule as follows::

       def rule(x):
           return [x[0]-x[3],x[1]-x[2]]

    or simply::

        rule = lambda x: [x[0]-x[3],x[1]-x[2]]

    We may now make and use the branching rule as follows.

    EXAMPLES::

        sage: br = BranchingRule("A3", "C2", lambda x: [x[0]-x[3],x[1]-x[2]], "homemade"); br
        homemade branching rule A3 => C2
        sage: [A3,C2]=[WeylCharacterRing(x,style=\'coroots\') for x in ["A3","C2"]]
        sage: A3(0,1,0).branch(C2,rule=br)
        C2(0,0) + C2(0,1)
    '''

class BranchingRule(SageObject):
    """
    A class for branching rules.
    """
    def __init__(self, R, S, f, name: str = 'default', intermediate_types=[], intermediate_names=[]) -> None:
        """
        INPUT:

        - ``R``, ``S`` -- CartanTypes
        - ``f`` -- a function from the weight lattice of R to the weight lattice of S
        """
    def __call__(self, x):
        '''
        EXAMPLES::

            sage: b=branching_rule("A3","C2","symmetric")
            sage: b([2,1,0,0])
            [2, 1]
        '''
    def __eq__(self, other):
        '''
        Two branching rules with the same source and target Cartan types are
        considered equal if they are the same as mappings from the weight
        lattice of the larger group to the smaller. The last example shows
        that two rules may be different by this criterion yet describe the
        same branching, if they differ by conjugation by an element of the
        Weyl group.

        EXAMPLES::

            sage: b = branching_rule("E6","F4","symmetric")*branching_rule("F4","B3","levi")*branching_rule("B3","G2","miscellaneous"); b
            composite branching rule E6 => (symmetric) F4 => (levi) B3 => (miscellaneous) G2
            sage: c = branching_rule("E6", "G2xA2", "miscellaneous")*branching_rule("G2xA2", "G2", "proj1"); c
            composite branching rule E6 => (miscellaneous) G2xA2 => (proj1) G2
            sage: b == c
            True
            sage: d = branching_rule("A3","A2","levi")*branching_rule("A2","A1","levi"); d
            composite branching rule A3 => (levi) A2 => (levi) A1
            sage: e = branching_rule("A3","D3","isomorphic")*branching_rule("D3","B2","symmetric")*branching_rule("B2","A1","levi"); e
            composite branching rule A3 => (isomorphic) D3 => (symmetric) B2 => (levi) A1
            sage: d == e
            False
            sage: b1 = BranchingRule("A2","A2",lambda x: [x[2], x[1], x[0]], "long Weyl element conjugation")
            sage: b2 = BranchingRule("A2","A2",lambda x: x, "identity map")
            sage: b1 == b2
            False
            sage: A2 = WeylCharacterRing("A2",style=\'coroots\')
            sage: [A2(f).branch(A2,rule=b1) == A2(f).branch(A2,rule=b2) for f in A2.fundamental_weights()]
            [True, True]
        '''
    def __ne__(self, other):
        '''
        Test inequality.

        EXAMPLES::

            sage: b1 = BranchingRule("A2","A2",lambda x: [x[2], x[1], x[0]], "long Weyl element conjugation")
            sage: b2 = BranchingRule("A2","A2",lambda x: x, "identity map")
            sage: b1 != b2
            True
        '''
    def __mul__(self, other):
        '''
        EXAMPLES::

            sage: E6 = WeylCharacterRing("E6",style=\'coroots\')
            sage: A5 = WeylCharacterRing("A5",style=\'coroots\')
            sage: br = branching_rule("E6","A5xA1",rule=\'extended\')*branching_rule("A5xA1","A5",rule=\'proj1\'); br
            composite branching rule E6 => (extended) A5xA1 => (proj1) A5
            sage: E6(1,0,0,0,0,0).branch(A5,rule=br)
            A5(0,0,0,1,0) + 2*A5(1,0,0,0,0)
        '''
    def Rtype(self):
        '''
        In a branching rule R => S, returns the Cartan Type of the ambient group R.

        EXAMPLES::

            sage: branching_rule("A3","A2","levi").Rtype()
            [\'A\', 3]
        '''
    def Stype(self):
        '''
        In a branching rule R => S, returns the Cartan Type of the subgroup S.

        EXAMPLES::

            sage: branching_rule("A3","A2","levi").Stype()
            [\'A\', 2]
        '''
    def describe(self, verbose: bool = False, debug: bool = False, no_r: bool = False) -> None:
        '''
        Describe how extended roots restrict under ``self``.

        EXAMPLES::

            sage: branching_rule("G2","A2","extended").describe()
            <BLANKLINE>
            3
            O=<=O---O
            1   2   0
            G2~
            <BLANKLINE>
            root restrictions G2 => A2:
            <BLANKLINE>
            O---O
            1   2
            A2
            <BLANKLINE>
            0 => 2
            2 => 1
            <BLANKLINE>
            For more detailed information use verbose=True

        In this example, `0` is the affine root, that is, the negative
        of the highest root, for `"G2"`. If `i \\geq j` is printed, this
        means that the `i`-th simple (or affine) root of the ambient
        group restricts to the `j`-th simple root of the subgroup.
        For reference the Dynkin diagrams are also printed. The
        extended Dynkin diagram of the ambient group is printed if
        the affine root restricts to a simple root. More information
        is printed if the parameter `verbose` is true.
        '''
    def branch(self, chi, style=None):
        '''
        INPUT:

        - ``chi`` -- a character of the WeylCharacterRing with Cartan type self.Rtype()

        Returns the branched character.

        EXAMPLES::

            sage: G2=WeylCharacterRing("G2",style=\'coroots\')
            sage: chi=G2(1,1); chi.degree()
            64
            sage: b=G2.maximal_subgroup("A2"); b
            extended branching rule G2 => A2
            sage: b.branch(chi)
            A2(0,1) + A2(1,0) + A2(0,2) + 2*A2(1,1) + A2(2,0) + A2(1,2) + A2(2,1)
            sage: A2=WeylCharacterRing("A2",style=\'coroots\'); A2
            The Weyl Character Ring of Type A2 with Integer Ring coefficients
            sage: chi.branch(A2,rule=b)
            A2(0,1) + A2(1,0) + A2(0,2) + 2*A2(1,1) + A2(2,0) + A2(1,2) + A2(2,1)
        '''

def branching_rule(Rtype, Stype, rule: str = 'default'):
    '''
    Create a branching rule.

    INPUT:

    - ``R`` -- the Weyl Character Ring of `G`

    - ``S`` -- the Weyl Character Ring of `H`

    - ``rule`` -- string describing the branching rule as a map from
      the weight space of `S` to the weight space of `R`

    If the rule parameter is omitted, in some cases, a default rule is supplied. See
    :func:`~sage.combinat.root_system.branching_rules.branch_weyl_character`.

    EXAMPLES::

       sage: rule = branching_rule(CartanType("A3"),CartanType("C2"),"symmetric")
       sage: [rule(x) for x in WeylCharacterRing("A3").fundamental_weights()]
       [[1, 0], [1, 1], [1, 0]]
    '''
get_branching_rule = branching_rule

def branching_rule_from_plethysm(chi, cartan_type, return_matrix: bool = False):
    '''
    Create the branching rule of a plethysm.

    INPUT:

    - ``chi`` -- the character of an irreducible representation `\\pi` of
      a group `G`
    - ``cartan_type`` -- a classical Cartan type (`A`,`B`,`C` or `D`)

    It is assumed that the image of the irreducible representation pi
    naturally has its image in the group `G`.

    Returns a branching rule for this plethysm.

    EXAMPLES:

    The adjoint representation `SL(3) \\to GL(8)` factors
    through `SO(8)`. The branching rule in question will
    describe how representations of `SO(8)` composed with
    this homomorphism decompose into irreducible characters
    of `SL(3)`::

        sage: A2 = WeylCharacterRing("A2")
        sage: A2 = WeylCharacterRing("A2", style=\'coroots\')
        sage: ad = A2.adjoint_representation(); ad
        A2(1,1)
        sage: ad.degree()
        8
        sage: ad.frobenius_schur_indicator()
        1

    This confirms that `ad` has degree 8 and is orthogonal,
    hence factors through `SO(8)` which is type `D_4`::

        sage: br = branching_rule_from_plethysm(ad,"D4")
        sage: D4 = WeylCharacterRing("D4")
        sage: [D4(f).branch(A2,rule = br) for f in D4.fundamental_weights()]
        [A2(1,1), A2(0,3) + A2(1,1) + A2(3,0), A2(1,1), A2(1,1)]
    '''
def maximal_subgroups(ct, mode: str = 'print_rules'):
    '''
    Given a classical Cartan type (of rank less than or equal to 8)
    this prints the Cartan types of maximal subgroups, with a method
    of obtaining the branching rule. The string to the right of the
    colon in the output is a command to create a branching rule.

    INPUT:

    - ``ct`` -- a classical irreducible Cartan type

    Returns a list of maximal subgroups of ct.

    EXAMPLES::

        sage: from sage.combinat.root_system.branching_rules import maximal_subgroups
        sage: maximal_subgroups("D4")
        B3:branching_rule("D4","B3","symmetric")
        A2:branching_rule("D4","A2(1,1)","plethysm")
        A1xC2:branching_rule("D4","C1xC2","tensor")*branching_rule("C1xC2","A1xC2",[branching_rule("C1","A1","isomorphic"),"identity"])
        A1xA1xA1xA1:branching_rule("D4","D2xD2","orthogonal_sum")*branching_rule("D2xD2","A1xA1xA1xA1",[branching_rule("D2","A1xA1","isomorphic"),branching_rule("D2","A1xA1","isomorphic")])

    .. SEEALSO:: :meth:`~sage.combinat.root_system.weyl_characters.WeylCharacterRing.ParentMethods.maximal_subgroups`
    '''
