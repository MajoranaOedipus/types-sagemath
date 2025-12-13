from .all import SL2Z as SL2Z
from .arithgroup_generic import ArithmeticSubgroup as ArithmeticSubgroup
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.functions import lcm as lcm
from sage.arith.misc import CRT_basis as CRT_basis
from sage.groups.perm_gps.permgroup import PermutationGroup as PermutationGroup
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ

Idm: Incomplete
Lm: Incomplete
Rm: Incomplete
S2m: Incomplete
S3m: Incomplete
S2mi: Incomplete
S3mi: Incomplete
Lmi: Incomplete
Rmi: Incomplete

def sl2z_word_problem(A):
    """
    Given an element of `\\SL_2(\\ZZ)`, express it as a word in the generators L =
    [1,1,0,1] and R = [1,0,1,1].

    The return format is a list of pairs ``(a,b)``, where ``a = 0`` or ``1``
    denoting ``L`` or ``R`` respectively, and ``b`` is an integer exponent.

    See also the function :func:`eval_sl2z_word`.

    EXAMPLES::

        sage: from sage.modular.arithgroup.arithgroup_perm import eval_sl2z_word, sl2z_word_problem
        sage: m = SL2Z([1,0,0,1])
        sage: eval_sl2z_word(sl2z_word_problem(m)) == m
        True
        sage: m = SL2Z([0,-1,1,0])
        sage: eval_sl2z_word(sl2z_word_problem(m)) == m
        True
        sage: m = SL2Z([7,8,-50,-57])
        sage: eval_sl2z_word(sl2z_word_problem(m)) == m
        True
    """
def eval_sl2z_word(w):
    """
    Given a word in the format output by :func:`sl2z_word_problem`, convert it back
    into an element of `\\SL_2(\\ZZ)`.

    EXAMPLES::

        sage: from sage.modular.arithgroup.arithgroup_perm import eval_sl2z_word
        sage: eval_sl2z_word([(0, 1), (1, -1), (0, 0), (1, 3), (0, 2), (1, 9), (0, -1)])
        [ 66 -59]
        [ 47 -42]
    """
def word_of_perms(w, p1, p2):
    """
    Given a word `w` as a list of 2-tuples ``(index,power)`` and permutations
    ``p1`` and ``p2`` return the product of ``p1`` and ``p2`` that corresponds
    to ``w``.

    EXAMPLES::

        sage: import sage.modular.arithgroup.arithgroup_perm as ap
        sage: S2 = SymmetricGroup(4)
        sage: p1 = S2('(1,2)(3,4)')
        sage: p2 = S2('(1,2,3,4)')
        sage: ap.word_of_perms([(1,1),(0,1)], p1, p2) ==  p2 * p1
        True
        sage: ap.word_of_perms([(0,1),(1,1)], p1, p2) == p1 * p2
        True
    """
def ArithmeticSubgroup_Permutation(L=None, R=None, S2=None, S3=None, relabel: bool = False, check: bool = True):
    '''
    Construct a subgroup of `\\SL_2(\\ZZ)` from the action of generators on its
    right cosets.

    Return an arithmetic subgroup knowing the action, given by permutations, of
    at least two standard generators on the its cosets. The generators
    considered are the following matrices:

    .. MATH::

        s_2 = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix},\\quad
        s_3 = \\begin{pmatrix} 0 & 1 \\\\ -1 & 1 \\end{pmatrix},\\quad
        l = \\begin{pmatrix} 1 & 1 \\\\ 0 & 1\\end{pmatrix},\\quad
        r = \\begin{pmatrix} 1 & 0 \\\\ 1 & 1 \\end{pmatrix}.

    An error will be raised if only one permutation is given. If no arguments
    are given at all, the full modular group `\\SL(2, \\ZZ)` is returned.

    INPUT:

    - ``S2``, ``S3``, ``L``, ``R`` -- permutations; action of matrices on the
      right cosets (each coset is identified to an element of `\\{1,\\dots,n\\}`
      where `1` is reserved for the identity coset)

    - ``relabel`` -- boolean (default: ``False``); if ``True``, renumber the cosets in a
      canonical way

    - ``check`` -- boolean (default: ``True``); check that the input is valid (it
      may be time efficient but less safe to set it to False)

    EXAMPLES::

        sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)",S3="(1,2,3)")
        sage: G
        Arithmetic subgroup with permutations of right cosets
         S2=(1,2)(3,4)
         S3=(1,2,3)
         L=(1,4,3)
         R=(2,4,3)
        sage: G.index()
        4

        sage: G = ArithmeticSubgroup_Permutation(); G
        Arithmetic subgroup with permutations of right cosets
         S2=()
         S3=()
         L=()
         R=()
        sage: G == SL2Z
        True

    Some invalid inputs::

        sage: ArithmeticSubgroup_Permutation(S2="(1,2)")
        Traceback (most recent call last):
        ...
        ValueError: Need at least two generators
        sage: ArithmeticSubgroup_Permutation(S2="(1,2)",S3="(3,4,5)")
        Traceback (most recent call last):
        ...
        ValueError: Permutations do not generate a transitive group
        sage: ArithmeticSubgroup_Permutation(L="(1,2)",R="(1,2,3)")
        Traceback (most recent call last):
        ...
        ValueError: Wrong relations between generators
        sage: ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="()")
        Traceback (most recent call last):
        ...
        ValueError: S2^2 does not equal to S3^3
        sage: ArithmeticSubgroup_Permutation(S2="(1,4,2,5,3)", S3="(1,3,5,2,4)")
        Traceback (most recent call last):
        ...
        ValueError: S2^2 = S3^3 must have order 1 or 2

    The input checks can be disabled for speed::

        sage: ArithmeticSubgroup_Permutation(S2="(1,2)",S3="(3,4,5)", check=False) # don\'t do this!
        Arithmetic subgroup with permutations of right cosets
         S2=(1,2)
         S3=(3,4,5)
         L=(1,2)(3,5,4)
         R=(1,2)(3,4,5)
    '''

class ArithmeticSubgroup_Permutation_class(ArithmeticSubgroup):
    """
    A subgroup of `\\SL_2(\\ZZ)` defined by the action of generators on its
    coset graph.

    The class stores the action of generators `s_2, s_3, l, r` on right cosets
    `Hg` of a finite index subgroup `H < \\SL_2(\\ZZ)`. In particular the action of
    `\\SL_2(\\ZZ)` on the cosets is on right.

    .. MATH::

        s_2 = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix},\\quad
        s_3 = \\begin{pmatrix} 0 & 1 \\\\ -1 & 1 \\end{pmatrix},\\quad
        l = \\begin{pmatrix} 1 & 1 \\\\ 0 & 1\\end{pmatrix},\\quad
        r = \\begin{pmatrix} 1 & 0 \\\\ 1 & 1 \\end{pmatrix}.

    TESTS::

        sage: s2 = PermutationGroupElement('(1,2)(3,4)(5,6)')
        sage: s3 = PermutationGroupElement('(1,3,5)(2,4,6)')
        sage: G = ArithmeticSubgroup_Permutation(S2=s2, S3=s3)
        sage: G.S2() == s2
        True
        sage: G.S3() == s3
        True
        sage: G == ArithmeticSubgroup_Permutation(L=G.L(), R=G.R())
        True
        sage: G == ArithmeticSubgroup_Permutation(L=G.L(), S2=G.S2())
        True
        sage: G == ArithmeticSubgroup_Permutation(L=G.L(), S3=G.S3())
        True
        sage: G == ArithmeticSubgroup_Permutation(R=G.R(), S2=G.S2())
        True
        sage: G == ArithmeticSubgroup_Permutation(R=G.R(), S3=G.S3())
        True
        sage: G == ArithmeticSubgroup_Permutation(S2=G.S2(), S3=G.S3())
        True

        sage: G = ArithmeticSubgroup_Permutation(S2='',S3='')
        sage: TestSuite(G).run()

        sage: S2 = '(1,2)(3,4)(5,6)'
        sage: S3 = '(1,2,3)(4,5,6)'
        sage: G = ArithmeticSubgroup_Permutation(S2=S2, S3=S3)
        sage: TestSuite(G).run()
    """
    def __eq__(self, other):
        '''
        Equality test.

        TESTS::

            sage: G2 = Gamma(2)
            sage: G3 = Gamma(3)
            sage: H = ArithmeticSubgroup_Permutation(S2="(1,4)(2,6)(3,5)",S3="(1,2,3)(4,5,6)")
            sage: (G2 == H) and (H == G2)
            True
            sage: (G3 == H) or (H == G3)
            False

            sage: G2 = Gamma1(2)
            sage: G3 = Gamma1(3)
            sage: H = ArithmeticSubgroup_Permutation(S2="(1,6,4,3)(2,7,5,8)",S3="(1,2,3,4,5,6)(7,8)")
            sage: (G2 == H) or (H == G2)
            False
            sage: (G3 == H) and (H == G3)
            True
        '''
    def __ne__(self, other):
        '''
        Check that ``self`` is not equal to ``other``.

        TESTS::

            sage: G2 = Gamma(2)
            sage: G3 = Gamma(3)
            sage: H = ArithmeticSubgroup_Permutation(S2="(1,4)(2,6)(3,5)",S3="(1,2,3)(4,5,6)")
            sage: (G2 != H) or (H != G2)
            False
            sage: (G3 != H) and (H != G3)
            True

            sage: G2 = Gamma1(2)
            sage: G3 = Gamma1(3)
            sage: H = ArithmeticSubgroup_Permutation(S2="(1,6,4,3)(2,7,5,8)",S3="(1,2,3,4,5,6)(7,8)")
            sage: (G2 != H) and (H != G2)
            True
            sage: (G3 != H) or (H != G3)
            False
        '''
    def __hash__(self):
        """
        Return a hash value.

        TESTS::

            sage: G1 = ArithmeticSubgroup_Permutation(S2='(1,2)(3,4)(5,6)',S3='(1,2,3)(4,5,6)')
            sage: G2 = ArithmeticSubgroup_Permutation(S2='(1,2)(3,4)(5,6)',S3='(1,5,6)(4,2,3)')
            sage: hash(G1) == hash(G2)
            False
        """
    def S2(self):
        '''
        Return the action of the matrix `s_2` as a permutation of cosets.

        .. MATH::

            s_2 = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)",S3="(1,2,3)")
            sage: G.S2()
            (1,2)
        '''
    def S3(self):
        '''
        Return the action of the matrix `s_3` as a permutation of cosets.

        .. MATH::

           s_3 = \\begin{pmatrix} 0 & 1 \\\\ -1 & 1 \\end{pmatrix},\\quad

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)",S3="(1,2,3)")
            sage: G.S3()
            (1,2,3)
        '''
    def L(self):
        '''
        Return the action of the matrix `l` as a permutation of cosets.

        .. MATH::

            l = \\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)",S3="(1,2,3)")
            sage: G.L()
            (1,3)
        '''
    def R(self):
        '''
        Return the action of the matrix `r` as a permutation of cosets.

        .. MATH::

            r = \\begin{pmatrix}1&0\\\\1&1\\end{pmatrix}

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)",S3="(1,2,3)")
            sage: G.R()
            (2,3)
        '''
    def perm_group(self):
        """
        Return the underlying permutation group.

        The permutation group returned is isomorphic to the action of the
        generators `s_2` (element of order two), `s_3` (element of order 3), `l`
        (parabolic element) and `r` (parabolic element) on right cosets (the
        action is on the right).

        EXAMPLES::

            sage: import sage.modular.arithgroup.arithgroup_perm as ap
            sage: ap.HsuExample10().perm_group()
            Permutation Group with generators [(1,2)(3,4)(5,6)(7,8)(9,10), (1,8,3)(2,4,6)(5,7,10), (1,4)(2,5,9,10,8)(3,7,6), (1,7,9,10,6)(2,3)(4,5,8)]
        """
    def index(self):
        """
        Return the index of this modular subgroup in the full modular group.

        EXAMPLES::

            sage: G = Gamma(2)
            sage: P = G.as_permutation_group()
            sage: P.index()
            6
            sage: G.index() == P.index()
            True

            sage: G = Gamma0(8)
            sage: P = G.as_permutation_group()
            sage: P.index()
            12
            sage: G.index() == P.index()
            True

            sage: G = Gamma1(6)
            sage: P = G.as_permutation_group()
            sage: P.index()
            24
            sage: G.index() == P.index()
            True
        """
    __dict__: Incomplete
    def relabel(self, inplace: bool = True):
        '''
        Relabel the cosets of this modular subgroup in a canonical way.

        The implementation of modular subgroup by action of generators on cosets
        depends on the choice of a numbering. This function provides
        canonical labels in the sense that two equal subgroups with different
        labels are relabeled the same way. The default implementation relabels
        the group itself. If you want to get a relabeled copy of your modular
        subgroup, put to ``False`` the option ``inplace``.

        ALGORITHM:

        We give an overview of how the canonical labels for the modular subgroup
        are built. The procedure only uses the permutations `S3` and `S2` that
        define the modular subgroup and can be used to renumber any
        transitive action of the symmetric group. In other words, the algorithm
        construct a canonical representative of a transitive subgroup in its
        conjugacy class in the full symmetric group.

        1. The identity is still numbered `0` and set the current vertex to be
        the identity.

        2. Number the cycle of `S3` the current vertex belongs to: if the
        current vertex is labeled `n` then the numbering in such way that the
        cycle becomes `(n, n+1, \\ldots, n+k)`).

        3. Find a new current vertex using the permutation `S2`.
        If all vertices are relabeled then it\'s done, otherwise go to step 2.

        EXAMPLES::

            sage: S2 = "(1,2)(3,4)(5,6)"; S3 = "(1,2,3)(4,5,6)"
            sage: G1 = ArithmeticSubgroup_Permutation(S2=S2,S3=S3); G1
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,4)(5,6)
             S3=(1,2,3)(4,5,6)
             L=(1,4,5,3)
             R=(2,4,6,3)
            sage: G1.relabel(); G1
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,4)(5,6)
             S3=(1,2,3)(4,5,6)
             L=(1,4,5,3)
             R=(2,4,6,3)

            sage: S2 = "(1,2)(3,5)(4,6)"; S3 = "(1,2,3)(4,5,6)"
            sage: G2 = ArithmeticSubgroup_Permutation(S2=S2,S3=S3); G2
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,5)(4,6)
             S3=(1,2,3)(4,5,6)
             L=(1,5,6,3)
             R=(2,5,4,3)
            sage: G2.relabel(); G2
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,4)(5,6)
             S3=(1,2,3)(4,5,6)
             L=(1,4,5,3)
             R=(2,4,6,3)

            sage: S2 = "(1,2)(3,6)(4,5)"; S3 = "(1,2,3)(4,5,6)"
            sage: G3 = ArithmeticSubgroup_Permutation(S2=S2,S3=S3); G3
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,6)(4,5)
             S3=(1,2,3)(4,5,6)
             L=(1,6,4,3)
             R=(2,6,5,3)
            sage: G4 = G3.relabel(inplace=False)
            sage: G4
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,4)(5,6)
             S3=(1,2,3)(4,5,6)
             L=(1,4,5,3)
             R=(2,4,6,3)
            sage: G3 is G4
            False

        TESTS::

            sage: S2 = "(1,2)(3,6)(4,5)"
            sage: S3 = "(1,2,3)(4,5,6)"
            sage: G = ArithmeticSubgroup_Permutation(S2=S2,S3=S3)
            sage: H = G.relabel(inplace=False)
            sage: G is H
            False
            sage: G._S2 is H._S2 or G._S3 is H._S3 or G._L is H._L or G._R is H._R
            False
            sage: G.relabel(inplace=False) is H
            True
            sage: H.relabel(inplace=False) is H
            True
            sage: G.relabel(); G
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)(3,4)(5,6)
             S3=(1,2,3)(4,5,6)
             L=(1,4,5,3)
             R=(2,4,6,3)
            sage: G.relabel(inplace=False) is G
            True
        '''
    def random_element(self, initial_steps: int = 30):
        """
        Return a random element in this subgroup.

        The algorithm uses a random walk on the Cayley graph of `\\SL_2(\\ZZ)` stopped
        at the first time it reaches the subgroup after at least
        ``initial_steps`` steps.

        INPUT:

        - ``initial_steps`` -- positive integer (default: 30)

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2='(1,3)(4,5)',S3='(1,2,5)(3,4,6)')
            sage: all(G.random_element() in G for _ in range(10))
            True
        """
    def permutation_action(self, x):
        """
        Given an element ``x`` of `\\SL_2(\\ZZ)`, compute the permutation of the
        cosets of ``self`` given by right multiplication by ``x``.

        EXAMPLES::

            sage: import sage.modular.arithgroup.arithgroup_perm as ap
            sage: ap.HsuExample10().permutation_action(SL2Z([32, -21, -67, 44]))
            (1,4,6,2,10,5,3,7,8,9)
        """
    def is_normal(self) -> bool:
        """
        Test whether the group is normal.

        EXAMPLES::

            sage: G = Gamma(2).as_permutation_group()
            sage: G.is_normal()
            True

            sage: G = Gamma1(2).as_permutation_group()
            sage: G.is_normal()
            False
        """
    def coset_graph(self, right_cosets: bool = False, s2_edges: bool = True, s3_edges: bool = True, l_edges: bool = False, r_edges: bool = False, s2_label: str = 's2', s3_label: str = 's3', l_label: str = 'l', r_label: str = 'r'):
        '''
        Return the right (or left) coset graph.

        INPUT:

        - ``right_cosets`` -- boolean (default: ``False``); right or left coset graph

        - ``s2_edges`` -- boolean (default: ``True``); put edges associated to s2

        - ``s3_edges`` -- boolean (default: ``True``); put edges associated to s3

        - ``l_edges`` -- boolean (default: ``False``); put edges associated to l

        - ``r_edges`` -- boolean (default: ``False``); put edges associated to r

        - ``s2_label``, ``s3_label``, ``l_label``, ``r_label`` -- the labels to
          put on the edges corresponding to the generators action. Use ``None``
          for no label.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)",S3="()")
            sage: G
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2)
             S3=()
             L=(1,2)
             R=(1,2)
            sage: G.index()
            2
            sage: G.coset_graph()
            Looped multi-digraph on 2 vertices
        '''
    def generalised_level(self):
        """
        Return the generalised level of this subgroup.

        The *generalised level* of a subgroup of the modular group is the least
        common multiple of the widths of the cusps. It was proven by Wohlfart
        that for even congruence subgroups, the (conventional) level coincides
        with the generalised level. For odd congruence subgroups the level is
        either the generalised level, or twice the generalised level [KSV2011]_.

        EXAMPLES::

            sage: G = Gamma(2).as_permutation_group()
            sage: G.generalised_level()
            2
            sage: G = Gamma0(3).as_permutation_group()
            sage: G.generalised_level()
            3
        """
    def congruence_closure(self):
        """
        Return the smallest congruence subgroup containing ``self``. If ``self`` is
        congruence, this is just self, but represented as a congruence subgroup
        data type. If ``self`` is not congruence, then it may be larger.

        In practice, we use the following criterion: let `m` be the generalised
        level of ``self``. If this subgroup is even, let `n = m`, else let `n =
        2m`. Then any congruence subgroup containing ``self`` contains `\\Gamma(n)`
        (a generalisation of Wohlfahrt's theorem due to Kiming, Verrill and
        Schuett). So we compute the image of ``self`` modulo `n` and return the
        preimage of that.

        .. NOTE::

            If you just want to know if the subgroup is congruence or not, it
            is *much* faster to use :meth:`~is_congruence`.

        EXAMPLES::

            sage: Gamma1(3).as_permutation_group().congruence_closure()
            Congruence subgroup of SL(2,Z) of level 3, preimage of:
             Matrix group over Ring of integers modulo 3 with 2 generators (
            [1 1]  [1 2]
            [0 1], [0 1]
            )
            sage: sage.modular.arithgroup.arithgroup_perm.HsuExample10().congruence_closure()  # long time (11s on sage.math, 2012)
            Modular Group SL(2,Z)
        """
    def is_congruence(self) -> bool:
        '''
        Return ``True`` if this is a congruence subgroup, and ``False``
        otherwise.

        ALGORITHM:

        Uses Hsu\'s algorithm [Hsu1996]_. Adapted from Chris Kurth\'s
        implementation in KFarey [Kur2008]_.

        For *odd* subgroups, Hsu\'s algorithm still works with minor
        modifications, using the extension of Wohlfarht\'s theorem due to
        Kiming, Schuett and Verrill [KSV2011]_. See [HL2014]_ for details.

        The algorithm is as follows. Let `G` be a finite-index subgroup of
        `\\SL(2, \\ZZ)`, and let `L` and `R` be the permutations of the
        cosets of `G` given by the elements `\\begin{pmatrix} 1 & 1 \\\\ 0 & 1
        \\end{pmatrix}` and `\\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix}`. Let
        `N` be the generalized level of `G` (if `G` is even) or twice the
        generalized level (if `G` is odd). Then:

        - if `N` is odd, `G` is congruence if and only if the relation

          .. MATH::

            (L R^{-1} L)^2 = (R^2 L^{1/2})^3

          holds, where `1/2` is understood as the multiplicative inverse of 2
          modulo N.

        - if `N` is a power of 2, then `G` is congruence if and only
          if the relations

          .. MATH::

            \\begin{array}{cc}
             (L R^{-1} L)^{-1} S (L R^{-1} L) S = 1 & (A1)\\\\\n             S^{-1} R S = R^{25} & (A2)\\\\\n             (L R^{-1} L)^2 = (S R^5 L R^{-1} L)^3 & (A3) \\\\\n            \\end{array}

          hold, where `S = L^{20} R^{1/5} L^{-4} R^{-1}`, `1/5` being the inverse
          of 5 modulo N.

        - if `N` is neither odd nor a power of 2, seven relations (B1-7) hold,
          for which see [HL2014]_, or the source code of this function.

        If the Sage verbosity flag is set (using ``set_verbose()``), then extra
        output will be produced indicating which of the relations (A1-3) or
        (B1-7) is not satisfied.

        EXAMPLES:

        Test if `\\SL_2(\\ZZ)` is congruence::

            sage: a = ArithmeticSubgroup_Permutation(L=\'\',R=\'\')
            sage: a.index()
            1
            sage: a.is_congruence()
            True

        This example is congruence -- it is `\\Gamma_0(3)` in disguise::

            sage: S2 = SymmetricGroup(4)
            sage: l = S2((2,3,4))
            sage: r = S2((1,3,4))
            sage: G = ArithmeticSubgroup_Permutation(L=l,R=r)
            sage: G
            Arithmetic subgroup with permutations of right cosets
            S2=(1,2)(3,4)
            S3=(1,4,2)
            L=(2,3,4)
            R=(1,3,4)
            sage: G.is_congruence()
            True

        This one is noncongruence::

            sage: import sage.modular.arithgroup.arithgroup_perm as ap
            sage: ap.HsuExample10().is_congruence()
            False

        The following example (taken from [KSV2011]_) shows that a lifting of a
        congruence subgroup of `\\PSL(2,\\ZZ)` to a subgroup of `\\SL(2,
        \\ZZ)` need not necessarily be congruence::

            sage: S2 = "(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23)"
            sage: S3 = "(1,14,15,13,2,3)(4,5,6,16,17,18)(7,8,9,19,20,21)(10,11,12,22,23,24)"
            sage: G = ArithmeticSubgroup_Permutation(S2=S2,S3=S3)
            sage: G.is_congruence()
            False
            sage: G.to_even_subgroup().is_congruence()
            True

        In fact `G` is a lifting to `\\SL(2,\\ZZ)` of the group
        `\\bar{\\Gamma}_0(6)`::

            sage: G.to_even_subgroup() == Gamma0(6)
            True
        '''
    def surgroups(self) -> Generator[Incomplete]:
        '''
        Return an iterator through the non-trivial intermediate groups between
        `SL(2,\\ZZ)` and this finite index group.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)(5,6)", S3="(1,2,3)(4,5,6)")
            sage: H = next(G.surgroups())
            sage: H
             Arithmetic subgroup with permutations of right cosets
             S2=(1,2)
             S3=(1,2,3)
             L=(1,3)
             R=(2,3)
            sage: G.is_subgroup(H)
            True

        The principal congruence group `\\Gamma(3)` has thirteen surgroups::

            sage: G = Gamma(3).as_permutation_group()
            sage: G.index()
            24
            sage: l = []
            sage: for H in G.surgroups():
            ....:     l.append(H.index())
            ....:     assert G.is_subgroup(H) and H.is_congruence()
            sage: l
            [6, 3, 4, 8, 4, 8, 4, 12, 4, 6, 6, 8, 8]
        '''

class OddArithmeticSubgroup_Permutation(ArithmeticSubgroup_Permutation_class):
    '''
    An arithmetic subgroup of `\\SL(2, \\ZZ)` not containing `-1`,
    represented in terms of the right action of `\\SL(2, \\ZZ)` on its
    cosets.

    EXAMPLES::

        sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)")
        sage: G
        Arithmetic subgroup with permutations of right cosets
        S2=(1,2,3,4)
        S3=(1,3)(2,4)
        L=(1,2,3,4)
        R=(1,4,3,2)
        sage: type(G)
        <class \'sage.modular.arithgroup.arithgroup_perm.OddArithmeticSubgroup_Permutation_with_category\'>
    '''
    def __init__(self, S2, S3, L, R, canonical_labels: bool = False) -> None:
        '''
        TESTS::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)")
            sage: G
            Arithmetic subgroup with permutations of right cosets
             S2=(1,2,3,4)
             S3=(1,3)(2,4)
             L=(1,2,3,4)
             R=(1,4,3,2)
            sage: TestSuite(G).run()
        '''
    def __reduce__(self):
        '''
        Return the data used to construct ``self``. Used in pickling.

        TESTS::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)")
            sage: G == loads(dumps(G))  #indirect doctest
            True
            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)",relabel=True)
            sage: GG = loads(dumps(G))
            sage: GG == G #indirect doctest
            True
            sage: GG.relabel(inplace=False) is GG
            True
        '''
    def is_odd(self) -> bool:
        '''
        Test whether the group is odd.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,6,4,3)(2,7,5,8)",S3="(1,2,3,4,5,6)(7,8)")
            sage: G.is_odd()
            True
        '''
    def is_even(self) -> bool:
        '''
        Test whether the group is even.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,6,4,3)(2,7,5,8)",S3="(1,2,3,4,5,6)(7,8)")
            sage: G.is_even()
            False
        '''
    def to_even_subgroup(self, relabel: bool = True):
        """
        Return the group with `-Id` added in it.

        EXAMPLES::

            sage: G = Gamma1(3).as_permutation_group()
            sage: G.to_even_subgroup()
            Arithmetic subgroup with permutations of right cosets
             S2=(1,3)(2,4)
             S3=(1,2,3)
             L=(2,3,4)
             R=(1,4,2)

            sage: H = ArithmeticSubgroup_Permutation(S2 = '(1,4,11,14)(2,7,12,17)(3,5,13,15)(6,9,16,19)(8,10,18,20)', S3 = '(1,2,3,11,12,13)(4,5,6,14,15,16)(7,8,9,17,18,19)(10,20)')
            sage: G = H.to_even_subgroup(relabel=False); G
            Arithmetic subgroup with permutations of right cosets
             S2=(1,4)(2,7)(3,5)(6,9)(8,10)
             S3=(1,2,3)(4,5,6)(7,8,9)
             L=(1,5)(2,4,9,10,8)(3,7,6)
             R=(1,7,10,8,6)(2,5,9)(3,4)
            sage: H.is_subgroup(G)
            True
        """
    def nu2(self):
        '''
        Return the number of elliptic points of order 2.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)")
            sage: G.nu2()
            0

            sage: G = Gamma1(2).as_permutation_group()
            sage: G.nu2()
            1
        '''
    def nu3(self):
        '''
        Return the number of elliptic points of order 3.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)")
            sage: G.nu3()
            2

            sage: G = Gamma1(3).as_permutation_group()
            sage: G.nu3()
            1
        '''
    def nirregcusps(self):
        '''
        Return the number of irregular cusps.

        The cusps are associated to cycles of the permutations `L` or `R`.
        The irregular cusps are the one which are stabilised by `-Id`.

        EXAMPLES::

            sage: S2 = "(1,3,2,4)(5,7,6,8)(9,11,10,12)"
            sage: S3 = "(1,3,5,2,4,6)(7,9,11,8,10,12)"
            sage: G = ArithmeticSubgroup_Permutation(S2=S2,S3=S3)
            sage: G.nirregcusps()
            3
        '''
    def nregcusps(self):
        """
        Return the number of regular cusps of the group.

        The cusps are associated to cycles of `L` or `R`. The irregular cusps
        correspond to the ones which are not stabilised by `-Id`.

        EXAMPLES::

            sage: G = Gamma1(3).as_permutation_group()
            sage: G.nregcusps()
            2
        """
    def cusp_widths(self, exp: bool = False):
        """
        Return the list of cusp widths.

        INPUT:

        - ``exp`` -- boolean (default: ``False``); if ``True``, return a
          dictionary with keys the possible widths and with values the number
          of cusp with that width

        EXAMPLES::

            sage: G = Gamma1(5).as_permutation_group()
            sage: G.cusp_widths()
            [1, 1, 5, 5]
            sage: G.cusp_widths(exp=True)
            {1: 2, 5: 2}
        """
    def ncusps(self):
        '''
        Return the number of cusps.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2,3,4)",S3="(1,3)(2,4)")
            sage: G.ncusps()
            1

            sage: G = Gamma1(3).as_permutation_group()
            sage: G.ncusps()
            2
        '''

class EvenArithmeticSubgroup_Permutation(ArithmeticSubgroup_Permutation_class):
    """
    An arithmetic subgroup of `\\SL(2, \\ZZ)` containing `-1`, represented
    in terms of the right action of `\\SL(2, \\ZZ)` on its cosets.

    EXAMPLES:

    Construct a noncongruence subgroup of index 7 (the smallest possible)::

        sage: a2 = SymmetricGroup(7)([(1,2),(3,4),(6,7)]); a3 = SymmetricGroup(7)([(1,2,3),(4,5,6)])
        sage: G = ArithmeticSubgroup_Permutation(S2=a2, S3=a3); G
        Arithmetic subgroup with permutations of right cosets
        S2=(1,2)(3,4)(6,7)
        S3=(1,2,3)(4,5,6)
        L=(1,4,7,6,5,3)
        R=(2,4,5,7,6,3)
        sage: G.index()
        7
        sage: G.dimension_cusp_forms(4)
        1
        sage: G.is_congruence()
        False

    Convert some standard congruence subgroups into permutation form::

        sage: G = Gamma0(8).as_permutation_group()
        sage: G.index()
        12
        sage: G.is_congruence()
        True

        sage: G = Gamma0(12).as_permutation_group()
        sage: G
        Arithmetic subgroup of index 24
        sage: G.is_congruence()
        True

    The following is the unique index 2 even subgroup of `\\SL_2(\\ZZ)`::

        sage: w = SymmetricGroup(2)([2,1])
        sage: G = ArithmeticSubgroup_Permutation(L=w, R=w)
        sage: G.dimension_cusp_forms(6)
        1
        sage: G.genus()
        0
    """
    def __init__(self, S2, S3, L, R, canonical_labels: bool = False) -> None:
        '''
        TESTS::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)(5,6)",S3="(1,2,3)(4,5,6)")
            sage: G == loads(dumps(G))
            True
            sage: G is loads(dumps(G))
            False
        '''
    def __reduce__(self):
        '''
        Data for pickling.

        TESTS::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)",S3="(1,2,4)")
            sage: G == loads(dumps(G)) #indirect doctest
            True
            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)",S3="(1,2,4)",relabel=True)
            sage: GG = loads(dumps(G))
            sage: G == GG #indirect doctest
            True
            sage: GG.relabel(inplace=False) is GG
            True
        '''
    def is_odd(self) -> bool:
        """
        Return ``True`` if this subgroup does not contain the matrix `-Id`.

        EXAMPLES::

            sage: G = Gamma(2).as_permutation_group()
            sage: G.is_odd()
            False
        """
    def is_even(self) -> bool:
        """
        Return ``True`` if this subgroup contains the matrix `-Id`.

        EXAMPLES::

            sage: G = Gamma(2).as_permutation_group()
            sage: G.is_even()
            True
        """
    def nu2(self):
        '''
        Return the number of orbits of elliptic points of order 2 for this
        arithmetic subgroup.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,4)(2)(3)",S3="(1,2,3)(4)")
            sage: G.nu2()
            2
        '''
    def nu3(self):
        '''
        Return the number of orbits of elliptic points of order 3 for this
        arithmetic subgroup.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,4)(2)(3)",S3="(1,2,3)(4)")
            sage: G.nu3()
            1
        '''
    def ncusps(self):
        '''
        Return the number of cusps of this arithmetic subgroup.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)(5,6)",S3="(1,2,3)(4,5,6)")
            sage: G.ncusps()
            3
        '''
    def todd_coxeter_s2_s3(self):
        """
        Return a 4-tuple ``(coset_reps, gens, s2, s3)`` where ``coset_reps``
        are coset representatives of the subgroup, ``gens`` is a list of
        generators, ``s2`` and ``s3`` are the action of the matrices `S2` and
        `S3` on the list of cosets.

        The so called *Todd-Coxeter algorithm* is a general method for coset
        enumeration for a subgroup of a group given by generators and relations.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2='(1,2)(3,4)',S3='(1,2,3)')
            sage: G.genus()
            0
            sage: reps,gens,s2,s3=G.todd_coxeter_s2_s3()
            sage: g1,g2 = gens
            sage: g1 in G and g2 in G
            True
            sage: Matrix(2, 2, [-1, 3, -1, 2]) in gens
            True
            sage: Matrix(2, 2, [-1, 0, 1, -1]) in gens or Matrix(2, 2, [1, 0, 1, 1]) in gens
            True
            sage: S2 = SL2Z([0,-1,1,0])
            sage: S3 = SL2Z([0,1,-1,1])
            sage: reps[0] == SL2Z([1,0,0,1])
            True
            sage: all(reps[i]*S2*~reps[s2[i]] in G for i in range(4))
            True
            sage: all(reps[i]*S3*~reps[s3[i]] in G for i in range(4))
            True
        """
    def todd_coxeter_l_s2(self):
        """
        Return a 4-tuple ``(coset_reps, gens, l, s2)`` where ``coset_reps`` is
        a list of coset representatives of the subgroup, ``gens`` a list of
        generators, ``l`` and ``s2`` are list that corresponds to the action of
        the matrix `S2` and `L` on the cosets.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2='(1,2)(3,4)',S3='(1,2,3)')
            sage: reps,gens,l,s=G.todd_coxeter_l_s2()
            sage: reps
            [
            [1 0]  [ 0 -1]  [1 2]  [1 1]
            [0 1], [ 1  0], [0 1], [0 1]
            ]
            sage: len(gens)
            3
            sage: Matrix(2, 2, [1, 3, 0, 1]) in gens
            True
            sage: Matrix(2, 2, [1, 0, -1, 1]) in gens
            True
            sage: Matrix(2, 2, [1, -3, 1, -2]) in gens or Matrix(2, 2, [2, -3, 1, -1]) in gens
            True
            sage: l
            [3, 1, 0, 2]
            sage: s
            [1, 0, 3, 2]
            sage: S2 = SL2Z([0,-1,1,0])
            sage: L = SL2Z([1,1,0,1])
            sage: reps[0] == SL2Z([1,0,0,1])
            True
            sage: all(reps[i]*S2*~reps[s[i]] in G for i in range(4))
            True
            sage: all(reps[i]*L*~reps[l[i]] in G for i in range(4))
            True
        """
    todd_coxeter = todd_coxeter_l_s2
    def coset_reps(self):
        '''
        Return coset representatives.

        EXAMPLES::

            sage: G = ArithmeticSubgroup_Permutation(S2="(1,2)(3,4)",S3="(1,2,3)")
            sage: c = G.coset_reps()
            sage: len(c)
            4
            sage: [g in G for g in c]
            [True, False, False, False]
        '''
    def cusp_widths(self, exp: bool = False):
        '''
        Return the list of cusp widths of the group.

        EXAMPLES::

            sage: G = Gamma(2).as_permutation_group()
            sage: G.cusp_widths()
            [2, 2, 2]
            sage: G.cusp_widths(exp=True)
            {2: 3}

            sage: S2 = "(1,2)(3,4)(5,6)"
            sage: S3 = "(1,2,3)(4,5,6)"
            sage: G = ArithmeticSubgroup_Permutation(S2=S2,S3=S3)
            sage: G.cusp_widths()
            [1, 1, 4]
            sage: G.cusp_widths(exp=True)
            {1: 2, 4: 1}

            sage: S2 = "(1,2)(3,4)(5,6)"
            sage: S3 = "(1,3,5)(2,4,6)"
            sage: G = ArithmeticSubgroup_Permutation(S2=S2,S3=S3)
            sage: G.cusp_widths()
            [6]
            sage: G.cusp_widths(exp=True)
            {6: 1}
        '''
    def to_even_subgroup(self, relabel: bool = True):
        """
        Return the subgroup generated by ``self`` and ``-Id``. Since ``self`` is even,
        this is just ``self``. Provided for compatibility.

        EXAMPLES::

            sage: G = Gamma0(4).as_permutation_group()
            sage: H = G.to_even_subgroup()
            sage: H == G
            True
        """
    def one_odd_subgroup(self, random: bool = False):
        """
        Return an odd subgroup of index 2 in `\\Gamma`, where `\\Gamma` is this
        subgroup. If the optional argument ``random`` is False (the default),
        this returns an arbitrary but consistent choice from the set of index 2
        odd subgroups. If ``random`` is True, then it will choose one of these
        at random.

        For details of the algorithm used, see the docstring for the related
        function :meth:`odd_subgroups`, which returns a list of all the
        index 2 odd subgroups.

        EXAMPLES:

        Starting from `\\Gamma(4)` we get back `\\Gamma(4)`::

            sage: G = Gamma(4).as_permutation_group()
            sage: G.is_odd(), G.index()
            (True, 48)
            sage: Ge = G.to_even_subgroup()
            sage: Go = Ge.one_odd_subgroup()
            sage: Go.is_odd(), Go.index()
            (True, 48)
            sage: Go == G
            True

        Starting from `\\Gamma(6)` we get a different group::

            sage: G = Gamma(6).as_permutation_group()
            sage: G.is_odd(), G.index()
            (True, 144)
            sage: Ge = G.to_even_subgroup()
            sage: Go = Ge.one_odd_subgroup()
            sage: Go.is_odd(), Go.index()
            (True, 144)
            sage: Go == G
            False

        An error will be raised if there are no such subgroups, which occurs if
        and only if the group contains an element of order 4::

            sage: Gamma0(10).as_permutation_group().one_odd_subgroup()
            Traceback (most recent call last):
            ...
            ValueError: Group contains an element of order 4, hence no index 2 odd subgroups

        Testing randomness::

            sage: G = Gamma(6).as_permutation_group().to_even_subgroup()
            sage: G1 = G.one_odd_subgroup(random=True) # random
            sage: G1.is_subgroup(G)
            True
        """
    def odd_subgroups(self):
        """
        Return a list of the odd subgroups of index 2 in `\\Gamma`, where
        `\\Gamma` is this subgroup. (Equivalently, return the liftings of
        `\\bar{\\Gamma} \\le \\PSL(2, \\ZZ)` to `\\SL(2, \\ZZ)`.) This can
        take rather a long time if the index of this subgroup is large.

        .. SEEALSO:: :meth:`one_odd_subgroup`, which returns just one of the
           odd subgroups (which is much quicker than enumerating them all).

        ALGORITHM:

        - If `\\Gamma` has an element of order 4, then there are no index 2 odd
          subgroups, so return the empty set.

        - If `\\Gamma` has no elements of order 4, then the permutation `S_2` is
          a combination of 2-cycles with no fixed points on `\\{1, \\dots, N\\}`.
          We construct the permutation `\\tilde{S}_2` of `\\{1, \\dots, 2N\\}`
          which has a 4-cycle `(a, b, a+N, b+N)` for each 2-cycle `(a,b)` in
          ``S2``. Similarly, we construct a permutation `\\tilde{S}_3` which has
          a 6-cycle `(a,b,c,a+N,b+N,c+N)` for each 3-cycle `(a,b,c)` in `S_3`,
          and a 2-cycle `(a,a+N)` for each fixed point `a` of `S_3`.

          Then the permutations `\\tilde{S}_2` and `\\tilde{S}_3` satisfy
          `\\tilde{S}_2^2 = \\tilde{S}_3^3 = \\iota` where `\\iota` is the order 2
          permutation interchanging `a` and `a+N` for each `a`. So the subgroup
          corresponding to these permutations is an index 2 odd subgroup of
          `\\Gamma`.

        - The other index 2 odd subgroups of `\\Gamma` are obtained from the
          pairs `\\tilde{S}_2, \\tilde{S}_3^\\sigma` where `\\sigma` is an element
          of the group generated by the 2-cycles `(a, a+N)`.

        Studying the permutations in the first example below gives a good
        illustration of the algorithm.

        EXAMPLES::

            sage: G = sage.modular.arithgroup.arithgroup_perm.HsuExample10()
            sage: [G.S2(), G.S3()]
            [(1,2)(3,4)(5,6)(7,8)(9,10), (1,8,3)(2,4,6)(5,7,10)]
            sage: X = G.odd_subgroups()
            sage: for u in X: print([u.S2(), u.S3()])
            [(1,2,11,12)(3,4,13,14)(5,6,15,16)(7,8,17,18)(9,10,19,20), (1,8,3,11,18,13)(2,4,6,12,14,16)(5,7,10,15,17,20)(9,19)]
            [(1,2,11,12)(3,4,13,14)(5,6,15,16)(7,8,17,18)(9,10,19,20), (1,18,13,11,8,3)(2,4,6,12,14,16)(5,7,10,15,17,20)(9,19)]
            [(1,2,11,12)(3,4,13,14)(5,6,15,16)(7,8,17,18)(9,10,19,20), (1,8,13,11,18,3)(2,4,6,12,14,16)(5,7,10,15,17,20)(9,19)]
            [(1,2,11,12)(3,4,13,14)(5,6,15,16)(7,8,17,18)(9,10,19,20), (1,18,3,11,8,13)(2,4,6,12,14,16)(5,7,10,15,17,20)(9,19)]

        A projective congruence subgroup may have noncongruence liftings, as the example of `\\bar{\\Gamma}_0(6)` illustrates (see [KSV2011]_)::

            sage: X = Gamma0(6).as_permutation_group().odd_subgroups(); Sequence([[u.S2(), u.S3()] for u in X],cr=True)
            [[(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,2,3,13,14,15)(4,5,6,16,17,18)(7,8,9,19,20,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,14,15,13,2,3)(4,5,6,16,17,18)(7,8,9,19,20,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,2,3,13,14,15)(4,17,6,16,5,18)(7,8,9,19,20,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,14,15,13,2,3)(4,17,6,16,5,18)(7,8,9,19,20,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,2,3,13,14,15)(4,5,6,16,17,18)(7,20,9,19,8,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,14,15,13,2,3)(4,5,6,16,17,18)(7,20,9,19,8,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,2,3,13,14,15)(4,17,6,16,5,18)(7,20,9,19,8,21)(10,11,12,22,23,24)],
             [(1,3,13,15)(2,4,14,16)(5,7,17,19)(6,10,18,22)(8,12,20,24)(9,11,21,23),
              (1,14,15,13,2,3)(4,17,6,16,5,18)(7,20,9,19,8,21)(10,11,12,22,23,24)]]
            sage: [u.is_congruence() for u in X]
            [True, False, False, True, True, False, False, True]
        """

def HsuExample10():
    """
    An example of an index 10 arithmetic subgroup studied by Tim Hsu.

    EXAMPLES::

        sage: import sage.modular.arithgroup.arithgroup_perm as ap
        sage: ap.HsuExample10()
        Arithmetic subgroup with permutations of right cosets
         S2=(1,2)(3,4)(5,6)(7,8)(9,10)
         S3=(1,8,3)(2,4,6)(5,7,10)
         L=(1,4)(2,5,9,10,8)(3,7,6)
         R=(1,7,9,10,6)(2,3)(4,5,8)
    """
def HsuExample18():
    """
    An example of an index 18 arithmetic subgroup studied by Tim Hsu.

    EXAMPLES::

        sage: import sage.modular.arithgroup.arithgroup_perm as ap
        sage: ap.HsuExample18()
        Arithmetic subgroup with permutations of right cosets
         S2=(1,5)(2,11)(3,10)(4,15)(6,18)(7,12)(8,14)(9,16)(13,17)
         S3=(1,7,11)(2,18,5)(3,9,15)(4,14,10)(6,17,12)(8,13,16)
         L=(1,2)(3,4)(5,6,7)(8,9,10)(11,12,13,14,15,16,17,18)
         R=(1,12,18)(2,6,13,9,4,8,17,7)(3,16,14)(5,11)(10,15)
    """
