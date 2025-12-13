from _typeshed import Incomplete
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc import inject_variable as inject_variable
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field import CyclotomicField as CyclotomicField
from sage.sets.set import Set as Set

class FusionDouble(CombinatorialFreeModule):
    '''
    The fusion ring corresponding to the Drinfeld double of a finite group.

    This is the fusion ring of the modular tensor category of modules
    over the Drinfeld double of a finite group. Usage is similar
    to :class:`FusionRing`; we refer the reader to that class for more
    information.

    INPUT:

    - ``G`` -- a finite group
    - ``prefix`` -- (default: ``\'s\'``) a prefix for the names of simple objects
    - ``inject_varables`` -- (optional) set to ``True`` to create variables
      for the simple objects

    REFERENCES:

    - [BaKi2001]_ Chapter 3
    - [Mas1995]_
    - [CHW2015]_
    - [Goff1999]_

    EXAMPLES::

        sage: G = DihedralGroup(5)
        sage: H = FusionDouble(G, inject_variables=True)
        sage: H.basis()
        Finite family {0: s0, 1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 7: s7, 8: s8,
                       9: s9, 10: s10, 11: s11, 12: s12, 13: s13, 14: s14, 15: s15}
        sage: for x in H.basis():
        ....:     print ("%s : %s"%(x,x^2))
        ....:
        s0 : s0
        s1 : s0
        s2 : s0 + s1 + s3
        s3 : s0 + s1 + s2
        s4 : s0 + s2 + s3 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15
        s5 : s0 + s2 + s3 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15
        s6 : s0 + s1 + s11
        s7 : s0 + s1 + s13
        s8 : s0 + s1 + s15
        s9 : s0 + s1 + s12
        s10 : s0 + s1 + s14
        s11 : s0 + s1 + s6
        s12 : s0 + s1 + s9
        s13 : s0 + s1 + s7
        s14 : s0 + s1 + s10
        s15 : s0 + s1 + s8
        sage: s4*s5
        s1 + s2 + s3 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15
        sage: s4.ribbon()
        1
        sage: s5.ribbon()
        -1
        sage: s8.ribbon()
        zeta5^3

    If the fusion double is multiplicity-free, meaning that the fusion
    coefficients `N_k^{ij}` are bounded by `1`, then the F-matrix may be
    computed, by solving the pentagon and hexagon relations as described
    in [Bond2007]_ and [Ab2022]_, just as for :class:`FusionRing`.
    There is a caveat here, since even if the fusion rules are multiplicity-free,
    if there are too many F-matrix values to compute, even if many of them are
    zero, in the current implementation singular cannot create enough variables.
    At least, this code can compute the F-matrix for the Fusion Double of the
    symmetric group `S_3`, duplicating the result of [CHW2015]_.

    ::

        sage: G1 = SymmetricGroup(3)
        sage: H1 = FusionDouble(G1, prefix=\'u\', inject_variables=True)
        sage: F = H1.get_fmatrix()

    The above commands create the F-matrix. You can compute all of the
    F-matrices with the command::

        sage: H1.find_orthogonal_solution()  # not tested (10-15 minutes)

    Individual F-matrices may be computed thus::

        sage: F.fmatrix(u3, u3, u3, u4)  # not tested

    See :class:`FMatrix` for more information.

    Unfortunately beyond `S_3` the number of simple objects is seemingly
    impractical. Although the :class:`FusionDouble` class and its methods
    work well for groups of moderate size, the :class:`FMatrix` may not be
    computable. For the dihedral group of order 8, there are already 22
    simple objects, and the F-matrix seems out of reach. The actual limitation
    is that singular will not create a polynomial ring in more than
    `2^{15}-1 = 32767` symbols, and there are more than this many F-matrix
    values to be computed for the dihedral group of order 8, so in the
    current implementation, this FusionRing is out of reach.

    It is an open problem to classify the finite groups whose fusion doubles
    are multiplicity-free. Abelian groups, dihedral groups, dicyclic groups,
    and all groups of order 16 are multiplicity-free.  On the other hand, for
    groups of order 32, some are multiplicity-free and others are not.
    These can all be constructed using :class:`SmallPermutationGroup`.

    EXAMPLES::

        sage: G = SmallPermutationGroup(16,9)
        sage: F = FusionDouble(G, prefix=\'b\', inject_variables=True)
        sage: b13^2 # long time (4s)
        b0 + b3 + b4
    '''
    @staticmethod
    def __classcall_private__(cls, G, prefix: str = 's', inject_variables: bool = False):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: H1 = FusionDouble(DihedralGroup(6), inject_variables=True)
            sage: H2 = FusionDouble(DihedralGroup(6), prefix='s')
            sage: H1 is H2
            True
        """
    def __init__(self, G, prefix: str = 's') -> None:
        """
        EXAMPLES::

            sage: H = FusionDouble(DihedralGroup(6))
            sage: TestSuite(H).run()
            sage: H = FusionDouble(DihedralGroup(7))
            sage: TestSuite(H).run()  # long time

            sage: F = FusionDouble(CyclicPermutationGroup(2))
            sage: [F._repr_term(t) for t in F._names]
            ['s0', 's1', 's2', 's3']
            sage: F = FusionDouble(CyclicPermutationGroup(2))
            sage: [F._latex_term(t) for t in F._names]
            ['s_{0}', 's_{1}', 's_{2}', 's_{3}']

            sage: FusionDouble(SymmetricGroup(4)).get_order()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        """
    def inject_variables(self) -> None:
        """
        Create variables for the simple objects in the global name space.

        EXAMPLES::

            sage: F = FusionDouble(DiCyclicGroup(3), prefix='d')
            sage: F.inject_variables()
            sage: d0 + d1 + d5
            d0 + d1 + d5
        """
    @cached_method
    def s_ij(self, i, j, unitary: bool = False, base_coercion: bool = True):
        """
        Return the element of the `S`-matrix of this fusion ring
        corresponding to the given elements.

        Without the unitary option set true, this is the unnormalized `S`-matrix
        entry, denoted `\\tilde{s}_{ij}`, in [BaKi2001]_ Chapter 3. The
        normalized `S`-matrix entries are denoted `s_{ij}`.

        INPUT:

        - ``i``, ``j``, -- a pair of basis elements
        - ``unitary`` -- boolean (default: ``False``); set to ``True`` to
          obtain the unitary `S`-matrix

        EXAMPLES::

            sage: D = FusionDouble(SymmetricGroup(3), prefix='t', inject_variables=True)
            sage: [D.s_ij(t2, x) for x in D.basis()]
            [2, 2, 4, 0, 0, -2, -2, -2]
            sage: [D.s_ij(t2, x, unitary=True) for x in D.basis()]
            [1/3, 1/3, 2/3, 0, 0, -1/3, -1/3, -1/3]
        """
    def s_ijconj(self, i, j, unitary: bool = False, base_coercion: bool = True):
        """
        Return the conjugate of the element of the `S`-matrix given by
        ``self.s_ij(elt_i, elt_j, base_coercion=base_coercion)``.

        .. SEEALSO::

            :meth:`s_ij`

        EXAMPLES::

            sage: P = FusionDouble(CyclicPermutationGroup(3),prefix='p',inject_variables=True)
            sage: P.s_ij(p1,p3)
            zeta3
            sage: P.s_ijconj(p1,p3)
            -zeta3 - 1
        """
    def s_matrix(self, unitary: bool = False, base_coercion: bool = True):
        """
        Return the `S`-matrix of this fusion ring.

        OPTIONAL:

        - ``unitary`` -- boolean (default: ``False``); set to ``True`` to
          obtain the unitary `S`-matrix

        Without the ``unitary`` parameter, this is the matrix denoted
        `\\widetilde{s}` in [BaKi2001]_.

        EXAMPLES::

            sage: FusionDouble(SymmetricGroup(3)).s_matrix()
            [ 1  1  2  3  3  2  2  2]
            [ 1  1  2 -3 -3  2  2  2]
            [ 2  2  4  0  0 -2 -2 -2]
            [ 3 -3  0  3 -3  0  0  0]
            [ 3 -3  0 -3  3  0  0  0]
            [ 2  2 -2  0  0  4 -2 -2]
            [ 2  2 -2  0  0 -2 -2  4]
            [ 2  2 -2  0  0 -2  4 -2]
            sage: FusionDouble(SymmetricGroup(3)).s_matrix(unitary=True)
            [ 1/6  1/6  1/3  1/2  1/2  1/3  1/3  1/3]
            [ 1/6  1/6  1/3 -1/2 -1/2  1/3  1/3  1/3]
            [ 1/3  1/3  2/3    0    0 -1/3 -1/3 -1/3]
            [ 1/2 -1/2    0  1/2 -1/2    0    0    0]
            [ 1/2 -1/2    0 -1/2  1/2    0    0    0]
            [ 1/3  1/3 -1/3    0    0  2/3 -1/3 -1/3]
            [ 1/3  1/3 -1/3    0    0 -1/3 -1/3  2/3]
            [ 1/3  1/3 -1/3    0    0 -1/3  2/3 -1/3]
        """
    @cached_method
    def N_ijk(self, i, j, k):
        """
        The symmetric invariant of three simple objects.

        This is the dimension of

        .. MATH::

           Hom(i \\otimes j \\otimes k, s_0),

        where `s_0` is the unit element (assuming ``prefix='s'``).
        Method of computation is through the Verlinde formula,
        deducing the values from the known values of the `S`-matrix.

        EXAMPLES::

            sage: A = FusionDouble(AlternatingGroup(4),prefix='a',inject_variables=True)
            sage: [A.N_ijk(a10,a11,x) for x in A.basis()]
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

        TESTS::

            sage: F = FusionDouble(SymmetricGroup(4))
            sage: from itertools import product
            sage: B = list(F.basis())
            sage: all(F.N_ijk(i,j,k).parent() is ZZ
            ....:     for i, j, k in product(B[::6], repeat=3))
            True
        """
    @cached_method
    def Nk_ij(self, i, j, k, use_characters: bool = False):
        """
        Return the fusion coefficient `N^k_{ij}`.

        INPUT:

        - ``i``, ``j``, ``k`` -- basis elements
        - ``use_characters`` -- boolean (default: ``False``); see the algorithm
          description below

        ALGORITHM:

        If ``use_characters=False``, then this is computed using
        the Verlinde formula:

        .. MATH::

            N^k_{ij} = \\sum_l \\frac{s(i, \\ell)\\, s(j, \\ell)\\,
            \\overline{s(k, \\ell)}}{s(I, \\ell)}.

        Otherwise we use a character theoretic method to compute the fusion
        coefficient `N_{ij}^k` as follows. Each simple object, for example
        `i` corresponds to a conjugacy class `\\mathcal{C}_i` of the underlying
        group `G`, and an irreducible character `\\chi_i` of the centralizer
        `C(g_i)` of a fixed representative `g_i` of `\\mathcal{C}_i`. In addition
        to the fixed representative `g_k` of the class `\\mathcal{C}_i`
        and `\\mathcal{C}_j`, the formula will make use of variable elements
        `h_i` and `h_j` that are subject to the condition `h_i h_j = g_k`.
        See [GoMa2010]_ equation (7).

        .. MATH::

            \\frac{|\\mathcal{C}_k|}{|G|}
            \\sum_{\\substack{h_i\\in\\mathcal{C}_i \\\\ h_j\\in\\mathcal{C}_j \\\\ h_ih_j=g_k}}
            \\lvert C(h_i)\\cap C(h_j) \\rvert \\,
            \\langle \\chi_i^{(h_i)} \\chi_j^{(h_j)}, \\chi_k \\rangle_{C(h_i)\\cap C(h_j)},

        where `\\chi_i^{(h_i)}` is the character `\\chi_i` of `C(g_i)`
        conjugated to a character of `C(h_i)`, when `h_i` is a conjugate
        of the fixed representative `g_i`. More exactly, there exists `r_i`
        such that `r_i g_i r_i^{-1} = h_i`, and then `\\chi_i^{(h_i)}(x) =
        \\chi_i(r_i^{-1}xr_i)`, and this definition does not depend on the
        choice of `r_i`.

        .. NOTE::

            This should be functionally equivalent, and testing shows
            that it is, but it is slower.

        EXAMPLES::

            sage: A = FusionDouble(AlternatingGroup(4),prefix='aa',inject_variables=True)
            sage: [A.Nk_ij(aa8,aa10,x) for x in A.basis()]
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1]

            sage: B = FusionDouble(CyclicPermutationGroup(2))
            sage: all(B.Nk_ij(x,y,z,use_characters=True) == B.Nk_ij(x,y,z)
            ....:     for x in B.basis() for y in B.basis() for z in B.basis())
            True
        """
    @cached_method
    def field(self):
        """
        Return a cyclotomic field large enough to contain the values
        of R-matrices and twists that can arise for this fusion ring.

        EXAMPLES::

            sage: FusionDouble(SymmetricGroup(3)).field()
            Cyclotomic Field of order 24 and degree 8
        """
    def fvars_field(self):
        """
        Return a field containing the ``CyclotomicField`` computed by
        :meth:`field` as well as all the F-symbols of the associated
        ``FMatrix`` factory object.

        This method is only available if ``self`` is multiplicity-free.

        EXAMPLES::

            sage: FusionDouble(SymmetricGroup(3)).fvars_field()
            Cyclotomic Field of order 24 and degree 8
        """
    def root_of_unity(self, r, base_coercion: bool = True):
        """
        Return `e^{i\\pi r}` as an element of ``self.field()`` if possible.

        INPUT:

        - ``r`` -- a rational number

        EXAMPLES::

            sage: H = FusionDouble(DihedralGroup(6))
            sage: H.field()
            Cyclotomic Field of order 24 and degree 8
            sage: for n in [1..7]:
            ....:     try:
            ....:         print (n,H.root_of_unity(2/n))
            ....:     except ValueError as err:
            ....:         print (n,err)
            ....:
            1 1
            2 -1
            3 zeta24^4 - 1
            4 zeta24^6
            5 not a root of unity in the field
            6 zeta24^4
            7 not a root of unity in the field
        """
    @cached_method
    def r_matrix(self, i, j, k, base_coercion: bool = True):
        """
        Return the R-matrix entry corresponding to the subobject ``k``
        in the tensor product of ``i`` with ``j``. This method is only
        correct if the fusion coefficient ``N_{ij}^k\\leq 1``. See the
        :class:`FusionRing` method for more information, including
        the reason for this caveat, and the algorithm.

        EXAMPLES::

            sage: C = FusionDouble(SymmetricGroup(3),prefix='c',inject_variables=True)
            sage: c4*c5
            c3 + c4
            sage: [C.r_matrix(c4,c5,k) for k in [c3,c4]]
            [-zeta24^6, 1]
            sage: c6^2
            c0 + c1 + c6
            sage: [C.r_matrix(c6,c6,k) for k in [c0,c1,c6]]
            [zeta3, -zeta3, -zeta3 - 1]
        """
    def global_q_dimension(self, base_coercion: bool = True):
        """
        Return the global quantum dimension, which is the sum of the squares of the
        quantum dimensions of the simple objects.

        For the Drinfeld double, it is the square of the order of the underlying quantum group.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: H = FusionDouble(G)
            sage: H.global_q_dimension()
            576
            sage: sum(x.q_dimension()^2 for x in H.basis())
            576
        """
    def total_q_order(self, base_coercion: bool = True):
        """
        Return the positive square root of :meth:`self.global_q_dimension()
        <global_q_dimension>` as an element of :meth:`self.field() <field>`.

        For the Drinfeld double of a finite group `G`, this equals the
        cardinality of `G`. This is also equal to `\\sum d_i^2 \\theta_i^{\\pm 1}`,
        where `i` runs through the simple objects, `d_i` is the quantum
        dimension, and `\\theta_i` is the twist. This sum with `\\theta_i` is
        denoted `p_-` in [BaKi2001]_ Chapter 3.

        EXAMPLES::

            sage: FusionDouble(DihedralGroup(7)).total_q_order()
            14
        """
    D_minus = total_q_order
    D_plus = total_q_order
    def is_multiplicity_free(self, verbose: bool = False) -> bool:
        """
        Return ``True`` if all fusion coefficients are at most 1.

        EXAMPLES::

            sage: FusionDouble(SymmetricGroup(3)).is_multiplicity_free()
            True
            sage: FusionDouble(SymmetricGroup(4)).is_multiplicity_free()
            False

            sage: FusionDouble(SymmetricGroup(3)).is_multiplicity_free(True)
            Checking multiplicity freeness
            True
            sage: FusionDouble(SymmetricGroup(4)).is_multiplicity_free(True)
            Checking multiplicity freeness
            N(s2,s13,s13) = 2
            False
        """
    @cached_method
    def one_basis(self):
        """
        The unit element of the ring, which is the first basis element.

        EXAMPLES::

            sage: FusionDouble(CyclicPermutationGroup(2), prefix='h').one()
            h1
        """
    @cached_method
    def dual(self, i):
        """
        Return the dual object ``i^\\ast`` to ``i``.

        The dual is also available as an element method of ``i``.

        EXAMPLES::

            sage: K = FusionDouble(CyclicPermutationGroup(3),prefix='k')
            sage: [(x,K.dual(x)) for x in K.basis()]
            [(k0, k0),
            (k1, k2),
            (k2, k1),
            (k3, k6),
            (k4, k8),
            (k5, k7),
            (k6, k3),
            (k7, k5),
            (k8, k4)]
            sage: all(K.dual(x)==x.dual() for x in K.basis())
            True
        """
    def product_on_basis(self, a, b):
        """
        Return the product of two basis elements corresponding to keys `a` and `b`.

        INPUT:

        - ``a``, ``b`` -- keys for the dictionary ``self._names`` representing
          simple objects

        EXAMPLES::

            sage: Q = FusionDouble(SymmetricGroup(3),prefix='q',inject_variables=True)
            sage: q3*q4
            q1 + q2 + q5 + q6 + q7
            sage: Q._names
            {0: 'q0', 1: 'q1', 2: 'q2', 3: 'q3', 4: 'q4', 5: 'q5', 6: 'q6', 7: 'q7'}
            sage: Q.product_on_basis(3,4)
            q1 + q2 + q5 + q6 + q7
        """
    def group(self):
        """
        Return the underlying group.

        EXAMPLES::

            sage: FusionDouble(DiCyclicGroup(4)).group()
            Dicyclic group of order 16 as a permutation group
        """
    fmats: Incomplete
    def get_fmatrix(self, *args, **kwargs):
        """
        Construct an :class:`FMatrix` factory to solve the pentagon and
        hexagon relations and organize the resulting F-symbols.

        EXAMPLES::

            sage: f = FusionDouble(SymmetricGroup(3)).get_fmatrix(); f
            F-Matrix factory for The Fusion Ring of the Drinfeld Double of
                Symmetric group of order 3! as a permutation group
        """
    class Element(CombinatorialFreeModule.Element):
        def is_simple_object(self) -> bool:
            """
            Determine whether ``self`` is a simple object (basis element) of the fusion ring.

            EXAMPLES::

                sage: H = FusionDouble(CyclicPermutationGroup(2), prefix='g', inject_variables=True)
                sage: [x.is_simple_object() for x in [g0, g1, g0+g1]]
                [True, True, False]
            """
        def g(self):
            """
            The data determining a simple object consists of a conjugacy
            class representative `g` and an irreducible character `\\chi` of
            the centralizer of `g`.

            This returns the conjugacy class representative of the underlying
            group corresponding to a simple object. See also :meth:`char`.

            EXAMPLES::

                sage: G = QuaternionGroup()
                sage: H = FusionDouble(G, prefix='e', inject_variables=True)
                sage: e10.g()
                (1,3)(2,4)(5,7)(6,8)
                sage: e10.char()
                Character of Subgroup generated by [(1,2,3,4)(5,6,7,8), (1,5,3,7)(2,8,4,6)]
                    of (Quaternion group of order 8 as a permutation group)
            """
        def char(self):
            """
            Return the character `\\chi` corresponding to ``self``.

            The data determining a simple object consists of a conjugacy
            class representative `g` and an irreducible character `\\chi` of
            the centralizer of `g`.

            .. SEEALSO:: :meth:`g`

            EXAMPLES::

                sage: G = DihedralGroup(5)
                sage: H = FusionDouble(G, prefix='f', inject_variables=True)
                sage: f10.g()
                (1,2,3,4,5)
                sage: f10.char()
                Character of Subgroup generated by [(1,2,3,4,5)] of
                    (Dihedral group of order 10 as a permutation group)
            """
        def ribbon(self, base_coercion: bool = True):
            """
            Return the twist or ribbon of the simple object.

            EXAMPLES::

                sage: H = FusionDouble(CyclicPermutationGroup(3))
                sage: [i.ribbon() for i in H.basis()]
                [1, 1, 1, 1, zeta3, -zeta3 - 1, 1, -zeta3 - 1, zeta3]
            """
        def twist(self, reduced: bool = True):
            """
            Return a rational number `h` such that `\\theta = e^{i \\pi h}`
            is the twist of ``self``.

            The quantity `e^{i \\pi h}` is also available using :meth:`ribbon`.

            This method is only available for simple objects.

            EXAMPLES::

                sage: Q = FusionDouble(CyclicPermutationGroup(3))
                sage: [x.twist() for x in Q.basis()]
                [0, 0, 0, 0, 2/3, 4/3, 0, 4/3, 2/3]
                sage: [x.ribbon() for x in Q.basis()]
                [1, 1, 1, 1, zeta3, -zeta3 - 1, 1, -zeta3 - 1, zeta3]

            TESTS::

                sage: H = FusionDouble(AlternatingGroup(4))
                sage: sum(H.basis()).twist()
                Traceback (most recent call last):
                ...
                ValueError: quantum twist is only available for simple objects
            """
        def dual(self):
            """
            Return the dual of ``self``.

            This method is only available for simple objects.

            EXAMPLES::

                sage: G = CyclicPermutationGroup(4)
                sage: H = FusionDouble(G, prefix='j')
                sage: [x for x in H.basis() if x == x.dual()]
                [j0, j1, j8, j9]

            TESTS::

                sage: H = FusionDouble(AlternatingGroup(4))
                sage: sum(H.basis()).dual()
                Traceback (most recent call last):
                ...
                ValueError: dual is only available for simple objects
            """
        @cached_method
        def q_dimension(self, base_coercion: bool = True):
            """
            Return the q-dimension of ``self``.

            This method is only available for simple objects.

            EXAMPLES::

                sage: G = AlternatingGroup(4)
                sage: H = FusionDouble(G)
                sage: [x.q_dimension() for x in H.basis()]
                [1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]
                sage: sum(x.q_dimension()^2 for x in H.basis()) == G.order()^2
                True

            TESTS::

                sage: H = FusionDouble(AlternatingGroup(4))
                sage: sum(H.basis()).q_dimension()
                Traceback (most recent call last):
                ...
                ValueError: quantum dimension is only available for simple objects
            """
