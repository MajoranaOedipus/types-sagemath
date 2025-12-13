from sage.categories.modules import Modules as Modules
from sage.combinat.root_system.weyl_characters import WeylCharacterRing as WeylCharacterRing
from sage.matrix.constructor import Matrix as Matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as RecursivelyEnumeratedSet
from sage.structure.category_object import CategoryObject as CategoryObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IntegrableRepresentation(UniqueRepresentation, CategoryObject):
    '''
    An irreducible integrable highest weight representation of
    an affine Lie algebra.

    INPUT:

    - ``Lam`` -- a dominant weight in an extended weight lattice
      of affine type

    REFERENCES:

    - [Ka1990]_

    .. [KMPS] Kass, Moody, Patera and Slansky, *Affine Lie algebras,
       weight multiplicities, and branching rules*. Vols. 1, 2. University
       of California Press, Berkeley, CA, 1990.

    .. [KacPeterson] Kac and Peterson. *Infinite-dimensional Lie algebras,
       theta functions and modular forms*. Adv. in Math. 53 (1984),
       no. 2, 125-264.

    .. [Carter] Carter, *Lie algebras of finite and affine type*. Cambridge
       University Press, 2005

    If `\\Lambda` is a dominant integral weight for an affine root system,
    there exists a unique integrable representation `V=V_\\Lambda` of highest
    weight `\\Lambda`. If `\\mu` is another weight, let `m(\\mu)` denote the
    multiplicity of the weight `\\mu` in this representation. The set
    `\\operatorname{supp}(V)` of `\\mu` such that `m(\\mu) > 0` is contained in the
    paraboloid

    .. MATH::

         (\\Lambda+\\rho | \\Lambda+\\rho) - (\\mu+\\rho | \\mu+\\rho) \\geq 0

    where `(\\, | \\,)` is the invariant inner product on the weight
    lattice and `\\rho` is the Weyl vector. Moreover if `m(\\mu)>0`
    then `\\mu\\in\\operatorname{supp}(V)` differs from `\\Lambda` by an element
    of the root lattice ([Ka1990]_, Propositions 11.3 and 11.4).

    Let `\\delta` be the nullroot, which is the lowest positive imaginary
    root. Then by [Ka1990]_, Proposition 11.3 or Corollary 11.9, for fixed `\\mu`
    the function `m(\\mu - k\\delta)` is a monotone increasing function of
    `k`. It is useful to take `\\mu` to be such that this function is nonzero
    if and only if `k \\geq 0`. Therefore we make the following definition.  If
    `\\mu` is such that `m(\\mu) \\neq 0` but `m(\\mu + \\delta) = 0` then `\\mu` is
    called *maximal*.

    Since `\\delta` is fixed under the action of the affine Weyl group,
    and since the weight multiplicities are Weyl group invariant, the
    function `k \\mapsto m(\\mu - k \\delta)` is unchanged if `\\mu` is replaced
    by an equivalent weight. Therefore in tabulating these functions, we may
    assume that `\\mu` is dominant. There are only a finite number of dominant
    maximal weights.

    Since every nonzero weight multiplicity appears in the string
    `\\mu - k\\delta` for one of the finite number of dominant maximal
    weights `\\mu`, it is important to be able to compute these. We may
    do this as follows.

    EXAMPLES::

         sage: Lambda = RootSystem([\'A\',3,1]).weight_lattice(extended=true).fundamental_weights()
         sage: IntegrableRepresentation(Lambda[1]+Lambda[2]+Lambda[3]).print_strings()
         2*Lambda[0] + Lambda[2]: 4 31 161 665 2380 7658 22721 63120 166085 417295 1007601 2349655
         Lambda[0] + 2*Lambda[1]: 2 18 99 430 1593 5274 16005 45324 121200 308829 754884 1779570
         Lambda[0] + 2*Lambda[3]: 2 18 99 430 1593 5274 16005 45324 121200 308829 754884 1779570
         Lambda[1] + Lambda[2] + Lambda[3]: 1 10 60 274 1056 3601 11199 32354 88009 227555 563390 1343178
         3*Lambda[2] - delta: 3 21 107 450 1638 5367 16194 45687 121876 310056 757056 1783324
         sage: Lambda = RootSystem([\'D\',4,1]).weight_lattice(extended=true).fundamental_weights()
         sage: IntegrableRepresentation(Lambda[0]+Lambda[1]).print_strings()                        # long time
         Lambda[0] + Lambda[1]: 1 10 62 293 1165 4097 13120 38997 109036 289575 735870 1799620
         Lambda[3] + Lambda[4] - delta: 3 25 136 590 2205 7391 22780 65613 178660 463842 1155717 2777795

    In this example, we construct the extended weight lattice of Cartan
    type `A_3^{(1)}`, then define ``Lambda`` to be the fundamental
    weights `(\\Lambda_i)_{i \\in I}`. We find there are 5 maximal
    dominant weights in irreducible representation of highest weight
    `\\Lambda_1 + \\Lambda_2 + \\Lambda_3`, and we determine their strings.

    It was shown in [KacPeterson]_ that each string is the set of Fourier
    coefficients of a modular form.

    Every weight `\\mu` such that the weight multiplicity `m(\\mu)` is
    nonzero has the form

      .. MATH::

          \\Lambda - n_0 \\alpha_0 - n_1 \\alpha_1 - \\cdots,

    where the `n_i` are nonnegative integers. This is represented internally
    as a tuple `(n_0, n_1, n_2, \\ldots)`. If you want an individual
    multiplicity you use the method :meth:`m` and supply it with this tuple::

        sage: Lambda = RootSystem([\'C\',2,1]).weight_lattice(extended=true).fundamental_weights()
        sage: V = IntegrableRepresentation(2*Lambda[0]); V
        Integrable representation of [\'C\', 2, 1] with highest weight 2*Lambda[0]
        sage: V.m((3,5,3))
        18

    The :class:`IntegrableRepresentation` class has methods :meth:`to_weight`
    and :meth:`from_weight` to convert between this internal representation
    and the weight lattice::

        sage: delta = V.weight_lattice().null_root()
        sage: V.to_weight((4,3,2))
        -3*Lambda[0] + 6*Lambda[1] - Lambda[2] - 4*delta
        sage: V.from_weight(-3*Lambda[0] + 6*Lambda[1] - Lambda[2] - 4*delta)
        (4, 3, 2)

    To get more values, use the depth parameter::

        sage: L0 = RootSystem(["A",1,1]).weight_lattice(extended=true).fundamental_weight(0); L0
        Lambda[0]
        sage: IntegrableRepresentation(4*L0).print_strings(depth=20)
        4*Lambda[0]: 1 1 3 6 13 23 44 75 131 215 354 561 889 1368 2097 3153 4712 6936 10151 14677
        2*Lambda[0] + 2*Lambda[1] - delta: 1 2 5 10 20 36 66 112 190 310 501 788 1230 1880 2850 4256 6303 9222 13396 19262
        4*Lambda[1] - 2*delta: 1 2 6 11 23 41 75 126 215 347 561 878 1368 2082 3153 4690 6936 10121 14677 21055

    An example in type `C_2^{(1)}`::

        sage: Lambda = RootSystem([\'C\',2,1]).weight_lattice(extended=true).fundamental_weights()
        sage: V = IntegrableRepresentation(2*Lambda[0])
        sage: V.print_strings()    # long time
        2*Lambda[0]: 1 2 9 26 77 194 477 1084 2387 5010 10227 20198
        Lambda[0] + Lambda[2] - delta: 1 5 18 55 149 372 872 1941 4141 8523 17005 33019
        2*Lambda[1] - delta: 1 4 15 44 122 304 721 1612 3469 7176 14414 28124
        2*Lambda[2] - 2*delta: 2 7 26 72 194 467 1084 2367 5010 10191 20198 38907

    Examples for twisted affine types::

        sage: Lambda = RootSystem(["A",2,2]).weight_lattice(extended=True).fundamental_weights()
        sage: IntegrableRepresentation(Lambda[0]).strings()
        {Lambda[0]: [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56]}
        sage: Lambda = RootSystem([\'G\',2,1]).dual.weight_lattice(extended=true).fundamental_weights()
        sage: V = IntegrableRepresentation(Lambda[0]+Lambda[1]+Lambda[2])
        sage: V.print_strings() # long time
        6*Lambdacheck[0]: 4 28 100 320 944 2460 6064 14300 31968 69020 144676 293916
        3*Lambdacheck[0] + Lambdacheck[1]: 2 16 58 192 588 1568 3952 9520 21644 47456 100906 207536
        4*Lambdacheck[0] + Lambdacheck[2]: 4 22 84 276 800 2124 5288 12470 28116 61056 128304 261972
        2*Lambdacheck[1] - deltacheck: 2 8 32 120 354 980 2576 6244 14498 32480 69776 145528
        Lambdacheck[0] + Lambdacheck[1] + Lambdacheck[2]: 1 6 26 94 294 832 2184 5388 12634 28390 61488 128976
        2*Lambdacheck[0] + 2*Lambdacheck[2]: 2 12 48 164 492 1344 3428 8256 18960 41844 89208 184512
        3*Lambdacheck[2] - deltacheck: 4 16 60 208 592 1584 4032 9552 21728 47776 101068 207888
        sage: Lambda = RootSystem([\'A\',6,2]).weight_lattice(extended=true).fundamental_weights()
        sage: V = IntegrableRepresentation(Lambda[0]+2*Lambda[1])
        sage: V.print_strings() # long time
        5*Lambda[0]: 3 42 378 2508 13707 64650 272211 1045470 3721815 12425064 39254163 118191378
        3*Lambda[0] + Lambda[2]: 1 23 234 1690 9689 47313 204247 800029 2893198 9786257 31262198 95035357
        Lambda[0] + 2*Lambda[1]: 1 14 154 1160 6920 34756 153523 612354 2248318 7702198 24875351 76341630
        Lambda[0] + Lambda[1] + Lambda[3] - 2*delta: 6 87 751 4779 25060 113971 464842 1736620 6034717 19723537 61152367 181068152
        Lambda[0] + 2*Lambda[2] - 2*delta: 3 54 499 3349 18166 84836 353092 1341250 4725259 15625727 48938396 146190544
        Lambda[0] + 2*Lambda[3] - 4*delta: 15 195 1539 9186 45804 200073 789201 2866560 9723582 31120281 94724550 275919741
    '''
    def __init__(self, Lam) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Lambda = RootSystem(['A',3,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[1]+Lambda[2]+Lambda[3])

        Some methods required by the category are not implemented::

            sage: TestSuite(V).run()  # known bug (#21387)
        """
    def highest_weight(self):
        """
        Return the highest weight of ``self``.

        EXAMPLES::

            sage: Lambda = RootSystem(['D',4,1]).weight_lattice(extended=true).fundamental_weights()
            sage: IntegrableRepresentation(Lambda[0]+2*Lambda[2]).highest_weight()
            Lambda[0] + 2*Lambda[2]
        """
    def weight_lattice(self):
        """
        Return the weight lattice associated to ``self``.

        EXAMPLES::

            sage: V=IntegrableRepresentation(RootSystem(['E',6,1]).weight_lattice(extended=true).fundamental_weight(0))
            sage: V.weight_lattice()
            Extended weight lattice of the Root system of type ['E', 6, 1]
        """
    def root_lattice(self):
        """
        Return the root lattice associated to ``self``.

        EXAMPLES::

            sage: V=IntegrableRepresentation(RootSystem(['F',4,1]).weight_lattice(extended=true).fundamental_weight(0))
            sage: V.root_lattice()
            Root lattice of the Root system of type ['F', 4, 1]
        """
    @cached_method
    def level(self):
        """
        Return the level of ``self``.

        The level of a highest weight representation `V_{\\Lambda}` is
        defined as `(\\Lambda | \\delta)` See [Ka1990]_ section 12.4.

        EXAMPLES::

            sage: Lambda = RootSystem(['G',2,1]).weight_lattice(extended=true).fundamental_weights()
            sage: [IntegrableRepresentation(Lambda[i]).level() for i in [0,1,2]]
            [1, 1, 2]
        """
    @cached_method
    def coxeter_number(self):
        """
        Return the Coxeter number of the Cartan type of ``self``.

        The Coxeter number is defined in [Ka1990]_ Chapter 6, and commonly
        denoted `h`.

        EXAMPLES::

            sage: Lambda = RootSystem(['F',4,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: V.coxeter_number()
            12
        """
    @cached_method
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number of the Cartan type of ``self``.

        The dual Coxeter number is defined in [Ka1990]_ Chapter 6, and commonly
        denoted `h^{\\vee}`.

        EXAMPLES::

            sage: Lambda = RootSystem(['F',4,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: V.dual_coxeter_number()
            9
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: Lambda = RootSystem(['F',4,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: V.cartan_type()
            ['F', 4, 1]
        """
    def to_weight(self, n):
        """
        Return the weight associated to the tuple ``n`` in ``self``.

        If ``n`` is the tuple `(n_1, n_2, \\ldots)`, then the associated
        weight is `\\Lambda - \\sum_i n_i \\alpha_i`, where `\\Lambda`
        is the weight of the representation.

        INPUT:

        - ``n`` -- tuple representing a weight

        EXAMPLES::

            sage: Lambda = RootSystem(['A',2,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(2*Lambda[2])
            sage: V.to_weight((1,0,0))
            -2*Lambda[0] + Lambda[1] + 3*Lambda[2] - delta
        """
    def from_weight(self, mu):
        """
        Return the tuple `(n_0, n_1, ...)`` such that ``mu`` equals
        `\\Lambda - \\sum_{i \\in I} n_i \\alpha_i` in ``self``, where `\\Lambda`
        is the highest weight of ``self``.

        EXAMPLES::

            sage: Lambda = RootSystem(['A',2,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(2*Lambda[2])
            sage: V.to_weight((1,0,0))
            -2*Lambda[0] + Lambda[1] + 3*Lambda[2] - delta
            sage: delta = V.weight_lattice().null_root()
            sage: V.from_weight(-2*Lambda[0] + Lambda[1] + 3*Lambda[2] - delta)
            (1, 0, 0)
        """
    def s(self, n, i):
        """
        Return the action of the ``i``-th simple reflection on the
        internal representation of weights by tuples ``n`` in ``self``.

        EXAMPLES::

            sage: V = IntegrableRepresentation(RootSystem(['A',2,1]).weight_lattice(extended=true).fundamental_weight(0))
            sage: [V.s((0,0,0),i) for i in V._index_set]
            [(1, 0, 0), (0, 0, 0), (0, 0, 0)]
        """
    def to_dominant(self, n):
        """
        Return the dominant weight in ``self`` equivalent to ``n``
        under the affine Weyl group.

        EXAMPLES::

            sage: Lambda = RootSystem(['A',2,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(3*Lambda[0])
            sage: n = V.to_dominant((13,11,7)); n
            (4, 3, 3)
            sage: V.to_weight(n)
            Lambda[0] + Lambda[1] + Lambda[2] - 4*delta
        """
    def m(self, n):
        """
        Return the multiplicity of the weight `\\mu` in ``self``, where
        `\\mu = \\Lambda - \\sum_i n_i \\alpha_i`.

        INPUT:

        - ``n`` -- tuple representing a weight `\\mu`

        EXAMPLES::

            sage: Lambda = RootSystem(['E',6,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: u = V.highest_weight() - V.weight_lattice().null_root()
            sage: V.from_weight(u)
            (1, 1, 2, 2, 3, 2, 1)
            sage: V.m(V.from_weight(u))
            6
        """
    def mult(self, mu):
        '''
        Return the weight multiplicity of ``mu``.

        INPUT:

        - ``mu`` -- an element of the weight lattice

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: L = RootSystem("B3~").weight_lattice(extended=True)
            sage: Lambda = L.fundamental_weights()
            sage: delta = L.null_root()
            sage: W = L.weyl_group(prefix=\'s\')
            sage: [s0,s1,s2,s3] = W.simple_reflections()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: V.mult(Lambda[2] - 2*delta)
            3
            sage: V.mult(Lambda[2] - Lambda[1])
            0
            sage: weights = [w.action(Lambda[1] - 4*delta) for w in [s1,s2,s0*s1*s2*s3]]
            sage: weights
            [-Lambda[1] + Lambda[2] - 4*delta,
             Lambda[1] - 4*delta,
             -Lambda[1] + Lambda[2] - 4*delta]
            sage: [V.mult(mu) for mu in weights]
            [35, 35, 35]

        TESTS::

            sage: L = RootSystem("B3~").weight_lattice(extended=True)
            sage: La = L.fundamental_weights()
            sage: V = IntegrableRepresentation(La[0])
            sage: Q = RootSystem("B3~").root_space()
            sage: al = Q.simple_roots()
            sage: V.mult(1/2*al[1])
            0
        '''
    @cached_method
    def dominant_maximal_weights(self):
        """
        Return the dominant maximal weights of ``self``.

        A weight `\\mu` is *maximal* if it has nonzero multiplicity but
        `\\mu + \\delta`` has multiplicity zero. There are a finite number
        of dominant maximal weights. Indeed, [Ka1990]_ Proposition 12.6
        shows that the dominant maximal weights are in bijection with
        the classical weights in `k \\cdot F` where `F` is the fundamental
        alcove and `k` is the level. The construction used in this
        method is based on that Proposition.

        EXAMPLES::

            sage: Lambda = RootSystem(['C',3,1]).weight_lattice(extended=true).fundamental_weights()
            sage: IntegrableRepresentation(2*Lambda[0]).dominant_maximal_weights()
            (2*Lambda[0],
             Lambda[0] + Lambda[2] - delta,
             2*Lambda[1] - delta,
             Lambda[1] + Lambda[3] - 2*delta,
             2*Lambda[2] - 2*delta,
             2*Lambda[3] - 3*delta)
        """
    def string(self, max_weight, depth: int = 12):
        """
        Return the list of multiplicities `m(\\Lambda - k \\delta)` in
        ``self``, where `\\Lambda` is ``max_weight`` and `k` runs from `0`
        to ``depth``.

        INPUT:

        - ``max_weight`` -- a dominant maximal weight
        - ``depth`` -- (default: 12) the maximum value of `k`

        EXAMPLES::

            sage: Lambda = RootSystem(['A',2,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(2*Lambda[0])
            sage: V.string(2*Lambda[0])
            [1, 2, 8, 20, 52, 116, 256, 522, 1045, 1996, 3736, 6780]
            sage: V.string(Lambda[1] + Lambda[2])
            [0, 1, 4, 12, 32, 77, 172, 365, 740, 1445, 2736, 5041]
        """
    def strings(self, depth: int = 12):
        '''
        Return the set of dominant maximal weights of ``self``, together
        with the string coefficients for each.

        OPTIONAL:

        - ``depth`` -- (default: 12) a parameter indicating how far
          to push computations

        EXAMPLES::

            sage: Lambda = RootSystem([\'A\',1,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(2*Lambda[0])
            sage: S = V.strings(depth=25)
            sage: for k in S:
            ....:     print("{}: {}".format(k, \' \'.join(str(x) for x in S[k])))
            2*Lambda[0]: 1 1 3 5 10 16 28 43 70 105 161 236 350 501 722 1016 1431 1981 2741 3740 5096 6868 9233 12306 16357
            2*Lambda[1] - delta: 1 2 4 7 13 21 35 55 86 130 196 287 420 602 858 1206 1687 2331 3206 4368 5922 7967 10670 14193 18803
        '''
    def print_strings(self, depth: int = 12) -> None:
        """
        Print the strings of ``self``.

        .. SEEALSO::

            :meth:`strings`

        EXAMPLES::

            sage: Lambda = RootSystem(['A',1,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(2*Lambda[0])
            sage: V.print_strings(depth=25)
            2*Lambda[0]: 1 1 3 5 10 16 28 43 70 105 161 236 350 501 722 1016 1431 1981 2741 3740 5096 6868 9233 12306 16357
            2*Lambda[1] - delta: 1 2 4 7 13 21 35 55 86 130 196 287 420 602 858 1206 1687 2331 3206 4368 5922 7967 10670 14193 18803
        """
    def modular_characteristic(self, mu=None):
        """
        Return the modular characteristic of ``self``.

        The modular characteristic is a rational number introduced
        by Kac and Peterson [KacPeterson]_, required to interpret the
        string functions as Fourier coefficients of modular forms. See
        [Ka1990]_ Section 12.7. Let `k` be the level, and let `h^\\vee`
        be the dual Coxeter number. Then

        .. MATH::

            m_\\Lambda = \\frac{|\\Lambda+\\rho|^2}{2(k+h^\\vee)}
            - \\frac{|\\rho|^2}{2h^\\vee}

        If `\\mu` is a weight, then

        .. MATH::

            m_{\\Lambda,\\mu} = m_\\Lambda - \\frac{|\\mu|^2}{2k}.

        OPTIONAL:

        - ``mu`` -- a weight, or alternatively,
        - ``n`` -- tuple representing a weight `\\mu`

        If no optional parameter is specified, this returns `m_\\Lambda`.
        If ``mu`` is specified, it returns `m_{\\Lambda,\\mu}`. You may
        use the tuple ``n`` to specify `\\mu`. If you do this, `\\mu` is
        `\\Lambda - \\sum_i n_i \\alpha_i`.

        EXAMPLES::

            sage: Lambda = RootSystem(['A',1,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(3*Lambda[0]+2*Lambda[1])
            sage: [V.modular_characteristic(x) for x in V.dominant_maximal_weights()]
            [11/56, -1/280, 111/280]
        """
    def branch(self, i=None, weyl_character_ring=None, sequence=None, depth: int = 5):
        '''
        Return the branching rule on ``self``.

        Removing any node from the extended Dynkin diagram of the affine
        Lie algebra results in the Dynkin diagram of a classical Lie
        algebra, which is therefore a Lie subalgebra. For example
        removing the `0` node from the Dynkin diagram of type ``[X, r, 1]``
        produces the classical Dynkin diagram of ``[X, r]``.

        Thus for each `i` in the index set, we may restrict ``self`` to
        the corresponding classical subalgebra. Of course ``self`` is
        an infinite dimensional representation, but each weight `\\mu`
        is assigned a grading by the number of times the simple root
        `\\alpha_i` appears in `\\Lambda-\\mu`. Thus the branched
        representation is graded and we get sequence of finite-dimensional
        representations which this method is able to compute.

        OPTIONAL:

        - ``i`` -- (default: 0) an element of the index set
        - ``weyl_character_ring`` -- a WeylCharacterRing
        - ``sequence`` -- dictionary
        - ``depth`` -- (default: 5) an upper bound for `k` determining
          how many terms to give

        In the default case where `i = 0`, you do not need to specify
        anything else, though you may want to increase the depth if
        you need more terms.

        EXAMPLES::

            sage: Lambda = RootSystem([\'A\',2,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(2*Lambda[0])
            sage: b = V.branch(); b                                                     # needs sage.libs.gap
            [A2(0,0),
             A2(1,1),
             A2(0,0) + 2*A2(1,1) + A2(2,2),
             2*A2(0,0) + 2*A2(0,3) + 4*A2(1,1) + 2*A2(3,0) + 2*A2(2,2),
             4*A2(0,0) + 3*A2(0,3) + 10*A2(1,1) + 3*A2(3,0) + A2(1,4) + 6*A2(2,2) + A2(4,1),
             6*A2(0,0) + 9*A2(0,3) + 20*A2(1,1) + 9*A2(3,0) + 3*A2(1,4) + 12*A2(2,2) + 3*A2(4,1) + A2(3,3)]

        If the parameter ``weyl_character_ring`` is omitted, the ring may be recovered
        as the parent of one of the branched coefficients::

            sage: A2 = b[0].parent(); A2                                                # needs sage.libs.gap
            The Weyl Character Ring of Type A2 with Integer Ring coefficients

        If `i` is not zero then you should specify the :class:`WeylCharacterRing` that you
        are branching to. This is determined by the Dynkin diagram::

            sage: Lambda = RootSystem([\'B\',3,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: V.cartan_type().dynkin_diagram()
                O 0
                |
                |
            O---O=>=O
            1   2   3
            B3~

        In this example, we observe that removing the `i=2` node from the
        Dynkin diagram produces a reducible diagram of type ``A1xA1xA1``.
        Thus we have a branching to
        `\\mathfrak{sl}(2) \\times \\mathfrak{sl}(2) \\times \\mathfrak{sl}(2)`::

            sage: A1xA1xA1 = WeylCharacterRing("A1xA1xA1",style=\'coroots\')              # needs sage.libs.gap
            sage: V.branch(i=2,weyl_character_ring=A1xA1xA1)                            # needs sage.libs.gap
            [A1xA1xA1(1,0,0),
             A1xA1xA1(0,1,2),
             A1xA1xA1(1,0,0) + A1xA1xA1(1,2,0) + A1xA1xA1(1,0,2),
             A1xA1xA1(2,1,2) + A1xA1xA1(0,1,0) + 2*A1xA1xA1(0,1,2),
             3*A1xA1xA1(1,0,0) + 2*A1xA1xA1(1,2,0) + A1xA1xA1(1,2,2) + 2*A1xA1xA1(1,0,2) + A1xA1xA1(1,0,4) + A1xA1xA1(3,0,0),
             A1xA1xA1(2,1,0) + 3*A1xA1xA1(2,1,2) + 2*A1xA1xA1(0,1,0) + 5*A1xA1xA1(0,1,2) + A1xA1xA1(0,1,4) + A1xA1xA1(0,3,2)]

        If the nodes of the two Dynkin diagrams are not in the same order, you
        must specify an additional parameter, ``sequence`` which gives a dictionary
        to the affine Dynkin diagram to the classical one.

        EXAMPLES::

            sage: Lambda = RootSystem([\'F\',4,1]).weight_lattice(extended=true).fundamental_weights()
            sage: V = IntegrableRepresentation(Lambda[0])
            sage: V.cartan_type().dynkin_diagram()
            O---O---O=>=O---O
            0   1   2   3   4
            F4~
            sage: A1xC3=WeylCharacterRing("A1xC3",style=\'coroots\')
            sage: A1xC3.dynkin_diagram()
            O
            1
            O---O=<=O
            2   3   4
            A1xC3

        Observe that removing the `i=1` node from the ``F4~`` Dynkin diagram
        gives the ``A1xC3`` diagram, but the roots are in a different order.
        The nodes `0, 2, 3, 4` of ``F4~`` correspond to ``1, 4, 3, 2``
        of ``A1xC3`` and so we encode this in a dictionary::

            sage: V.branch(i=1, weyl_character_ring=A1xC3, sequence={0:1,2:4,3:3,4:2})  # long time
            [A1xC3(1,0,0,0),
             A1xC3(0,0,0,1),
             A1xC3(1,0,0,0) + A1xC3(1,2,0,0),
             A1xC3(2,0,0,1) + A1xC3(0,0,0,1) + A1xC3(0,1,1,0),
             2*A1xC3(1,0,0,0) + A1xC3(1,0,1,0) + 2*A1xC3(1,2,0,0) + A1xC3(1,0,2,0) + A1xC3(3,0,0,0),
             2*A1xC3(2,0,0,1) + A1xC3(2,1,1,0) + A1xC3(0,1,0,0) + 3*A1xC3(0,0,0,1) + 2*A1xC3(0,1,1,0) + A1xC3(0,2,0,1)]

        The branch method gives a way of computing the graded dimension of the integrable representation::

            sage: Lambda = RootSystem("A1~").weight_lattice(extended=true).fundamental_weights()
            sage: V=IntegrableRepresentation(Lambda[0])
            sage: r = [x.degree() for x in V.branch(depth=15)]; r
            [1, 3, 4, 7, 13, 19, 29, 43, 62, 90, 126, 174, 239, 325, 435, 580]
            sage: oeis(r)                                                        # optional -- internet
            0: A029552: Expansion of phi(x) / f(-x) in powers of x where phi(), f() are Ramanujan theta functions.
        '''
