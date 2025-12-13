from _typeshed import Incomplete
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.set_partition_ordered import OrderedSetPartitions as OrderedSetPartitions
from sage.combinat.shuffle import ShuffleProduct as ShuffleProduct, ShuffleProduct_overlapping as ShuffleProduct_overlapping
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class WQSymBasis_abstract(CombinatorialFreeModule, BindableClass):
    """
    Abstract base class for bases of `WQSym`.

    This must define two attributes:

    - ``_prefix`` -- the basis prefix
    - ``_basis_name`` -- the name of the basis (must match one
      of the names that the basis can be constructed from `WQSym`)
    """
    def __init__(self, alg, graded: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: M = algebras.WQSym(QQ).M()
            sage: TestSuite(M).run()  # long time
        """
    def some_elements(self):
        """
        Return some elements of the word quasi-symmetric functions.

        EXAMPLES::

            sage: M = algebras.WQSym(QQ).M()
            sage: M.some_elements()
            [M[], M[{1}], M[{1, 2}],
             M[{1}] + M[{1}, {2}],
             M[] + 1/2*M[{1}]]
        """

class WordQuasiSymmetricFunctions(UniqueRepresentation, Parent):
    '''
    The word quasi-symmetric functions.

    The ring of word quasi-symmetric functions can be defined as a
    subring of the ring of all bounded-degree noncommutative power
    series in countably many indeterminates (i.e., elements in
    `R \\langle \\langle x_1, x_2, x_3, \\ldots \\rangle \\rangle` of bounded
    degree). Namely, consider words over the alphabet `\\{1, 2, 3, \\ldots\\}`;
    every noncommutative power series is an infinite `R`-linear
    combination of these words.
    For each such word `w`, we define the *packing* of `w` to be the
    word `\\operatorname{pack}(w)` that is obtained from `w` by replacing
    the smallest letter that appears in `w` by `1`, the second-smallest
    letter that appears in `w` by `2`, etc. (for example,
    `\\operatorname{pack}(4112774) = 3112443`).
    A word `w` is said to be *packed* if `\\operatorname{pack}(w) = w`.
    For each packed word `u`, we define the noncommutative power series
    `\\mathbf{M}_u = \\sum w`, where the sum ranges over all words `w`
    satisfying `\\operatorname{pack}(w) = u`.
    The span of these power series `\\mathbf{M}_u` is a subring of the
    ring of all noncommutative power series; it is called the ring of
    word quasi-symmetric functions, and is denoted by `WQSym`.

    For each nonnegative integer `n`, there is a bijection between
    packed words of length `n` and ordered set partitions of
    `\\{1, 2, \\ldots, n\\}`. Under this bijection, a packed word
    `u = (u_1, u_2, \\ldots, u_n)` of length `n` corresponds to the
    ordered set partition `P = (P_1, P_2, \\ldots, P_k)` of
    `\\{1, 2, \\ldots, n\\}` whose `i`-th part `P_i` (for each `i`) is the
    set of all `j \\in \\{1, 2, \\ldots, n\\}` such that `u_j = i`.

    The basis element `\\mathbf{M}_u` is also denoted as `\\mathbf{M}_P`
    in this situation. The basis `(\\mathbf{M}_P)_P` is called the
    *Monomial basis* and is implemented as
    :class:`~sage.combinat.chas.wqsym.WordQuasiSymmetricFunctions.Monomial`.

    Other bases are the cone basis (aka C basis), the characteristic
    basis (aka X basis), the Q basis and the Phi basis.

    Bases of `WQSym` are implemented (internally) using ordered set
    partitions. However, the user may access specific basis vectors using
    either packed words or ordered set partitions. See the examples below,
    noting especially the section on ambiguities.

    `WQSym` is endowed with a connected graded Hopf algebra structure (see
    Section 2.2 of [NoThWi08]_, Section 1.1 of [FoiMal14]_ and
    Section 4.3.2 of [MeNoTh11]_) given by

    .. MATH::

        \\Delta(\\mathbf{M}_{(P_1,\\ldots,P_{\\ell})}) = \\sum_{i=0}^{\\ell}
            \\mathbf{M}_{\\operatorname{st}(P_1, \\ldots, P_i)} \\otimes
            \\mathbf{M}_{\\operatorname{st}(P_{i+1}, \\ldots, P_{\\ell})}.

    Here, for any ordered set partition `(Q_1, \\ldots, Q_k)` of a
    finite set `Z` of integers, we let `\\operatorname{st}(Q_1, \\ldots, Q_k)`
    denote the set partition obtained from `Z` by replacing the smallest
    element appearing in it by `1`, the second-smallest element by `2`,
    and so on.

    A rule for multiplying elements of the monomial basis relies on the
    *quasi-shuffle product* of two ordered set partitions.
    The quasi-shuffle product `\\Box` is given by
    :class:`~sage.combinat.shuffle.ShuffleProduct_overlapping` with the
    ``+`` operation in the overlapping of the shuffles being the
    union of the sets.  The product `\\mathbf{M}_P \\mathbf{M}_Q`
    for two ordered set partitions `P` and `Q` of `[n]` and `[m]`
    is then given by

    .. MATH::

        \\mathbf{M}_P \\mathbf{M}_Q
        = \\sum_{R \\in P \\Box Q^+} \\mathbf{M}_R ,

    where `Q^+` means `Q` with all numbers shifted upwards by `n`.

    Sometimes, `WQSym` is also denoted as `NCQSym`.

    REFERENCES:

    - [FoiMal14]_
    - [MeNoTh11]_
    - [NoThWi08]_
    - [BerZab05]_

    EXAMPLES:

    Constructing the algebra and its Monomial basis::

        sage: WQSym = algebras.WQSym(ZZ)
        sage: WQSym
        Word Quasi-symmetric functions over Integer Ring
        sage: M = WQSym.M()
        sage: M
        Word Quasi-symmetric functions over Integer Ring in the Monomial basis
        sage: M[[]]
        M[]

    Calling basis elements using packed words::

        sage: x = M[1,2,1]; x
        M[{1, 3}, {2}]
        sage: x == M[[1,2,1]] == M[Word([1,2,1])]
        True
        sage: y = M[1,1,2] - M[1,2,2]; y
        -M[{1}, {2, 3}] + M[{1, 2}, {3}]

    Calling basis elements using ordered set partitions::

        sage: z = M[[1,2,3],]; z
        M[{1, 2, 3}]
        sage: z == M[[[1,2,3]]] == M[OrderedSetPartition([[1,2,3]])]
        True
        sage: M[[1,2],[3]]
        M[{1, 2}, {3}]

    Note that expressions above are output in terms of ordered set partitions,
    even when input as packed words. Output as packed words can be achieved
    by modifying the global options. (See :meth:`OrderedSetPartitions.options`
    for further details.)::

        sage: M.options.objects = "words"
        sage: y
        -M[1, 2, 2] + M[1, 1, 2]
        sage: M.options.display = "compact"
        sage: y
        -M[122] + M[112]
        sage: z
        M[111]

    The options should be reset to display as ordered set partitions::

        sage: M.options._reset()
        sage: z
        M[{1, 2, 3}]

    Illustration of the Hopf algebra structure::

        sage: M[[2, 3], [5], [6], [4], [1]].coproduct()
        M[] # M[{2, 3}, {5}, {6}, {4}, {1}] + M[{1, 2}] # M[{3}, {4}, {2}, {1}]
         + M[{1, 2}, {3}] # M[{3}, {2}, {1}] + M[{1, 2}, {3}, {4}] # M[{2}, {1}]
         + M[{1, 2}, {4}, {5}, {3}] # M[{1}] + M[{2, 3}, {5}, {6}, {4}, {1}] # M[]
        sage: _ == M[5,1,1,4,2,3].coproduct()
        True
        sage: M[[1,1,1]] * M[[1,1,2]]   # packed words
        M[{1, 2, 3}, {4, 5}, {6}] + M[{1, 2, 3, 4, 5}, {6}]
         + M[{4, 5}, {1, 2, 3}, {6}] + M[{4, 5}, {1, 2, 3, 6}]
         + M[{4, 5}, {6}, {1, 2, 3}]
        sage: M[[1,2,3],].antipode()  # ordered set partition
        -M[{1, 2, 3}]
        sage: M[[1], [2], [3]].antipode()
        -M[{1, 2, 3}] - M[{2, 3}, {1}] - M[{3}, {1, 2}] - M[{3}, {2}, {1}]
        sage: x = M[[1],[2],[3]] + 3*M[[2],[1]]
        sage: x.counit()
        0
        sage: x.antipode()
        3*M[{1}, {2}] + 3*M[{1, 2}] - M[{1, 2, 3}] - M[{2, 3}, {1}]
         - M[{3}, {1, 2}] - M[{3}, {2}, {1}]

    .. rubric:: Ambiguities

    Some ambiguity arises when accessing basis vectors with the dictionary syntax,
    i.e., ``M[...]``. A common example is when referencing an ordered set partition
    with one part. For example, in the expression ``M[[1,2]]``, does ``[[1,2]]``
    refer to an ordered set partition or does ``[1,2]`` refer to a packed word?
    We choose the latter: if the received arguments do not behave like a tuple of
    iterables, then view them as describing a packed word. (In the running example,
    one argument is received, which behaves as a tuple of integers.) Here are a
    variety of ways to get the same basis vector::

        sage: x = M[1,1]; x
        M[{1, 2}]
        sage: x == M[[1,1]]  # treated as word
        True
        sage: x == M[[1,2],] == M[[[1,2]]]  # treated as ordered set partitions
        True

        sage: M[[1,3],[2]]  # treat as ordered set partition
        M[{1, 3}, {2}]
        sage: M[[1,3],[2]] == M[1,2,1]  # treat as word
        True

    TESTS::

        sage: M = WordQuasiSymmetricFunctions(QQ).M()
        sage: a = M[OrderedSetPartition([[1]])]
        sage: b = M[OrderedSetPartitions(1)([[1]])]
        sage: c = M[[1]]
        sage: a == b == c
        True

    .. TODO::

        - Dendriform structure.
    '''
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = algebras.WQSym(QQ)
            sage: TestSuite(A).run()  # long time

            sage: M = algebras.WQSym(ZZ).M()
            sage: M.is_commutative()
            False
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the `M`-basis).

        EXAMPLES::

            sage: WQSym = algebras.WQSym(QQ)
            sage: WQSym.a_realization()
            Word Quasi-symmetric functions over Rational Field in the Monomial basis
        """
    class options(GlobalOptions):
        '''
        Set and display the global options for bases of WordQuasiSymmetricFunctions.
        If no parameters are set, then the function returns a copy of the options
        dictionary.

        The ``options`` can be accessed as the method
        :obj:`WordQuasiSymmetricFunctions.options` of
        :class:`WordQuasiSymmetricFunctions` or of any associated basis.

        @OPTIONS@

        The ``\'words\'`` representation of a basis element of
        :class:`WordQuasiSymmetricFunctions`, indexed by an ordered
        set partition `A`, is the packed word associated to `A`.
        See :meth:`OrderedSetPartition.to_packed_word` for details.)

        EXAMPLES::

            sage: WQ = WordQuasiSymmetricFunctions(QQ)
            sage: M = WQ.M()
            sage: elt = M[[[1,2]]]*M[[[1]]]; elt
            M[{1, 2}, {3}] + M[{1, 2, 3}] + M[{3}, {1, 2}]
            sage: M.options.display = "tight"
            sage: elt
            M[{1,2},{3}] + M[{1,2,3}] + M[{3},{1,2}]
            sage: M.options.display = "compact"
            sage: elt
            M[12.3] + M[123] + M[3.12]
            sage: WQ.options._reset()
            sage: M.options.objects = "words"
            sage: elt
            M[1, 1, 2] + M[1, 1, 1] + M[2, 2, 1]
            sage: M.options.display = "tight"
            sage: elt
            M[1,1,2] + M[1,1,1] + M[2,2,1]
            sage: WQ.options.display = "compact"
            sage: elt
            M[112] + M[111] + M[221]
            sage: M.options._reset()
            sage: elt
            M[{1, 2}, {3}] + M[{1, 2, 3}] + M[{3}, {1, 2}]
        '''
        NAME: str
        module: str
        option_class: str
        objects: Incomplete
        display: Incomplete
    class Monomial(WQSymBasis_abstract):
        """
        The Monomial basis of `WQSym`.

        The family `(\\mathbf{M}_u)`, as defined in
        :class:`~sage.combinat.chas.wqsym.WordQuasiSymmetricFunctions`
        with `u` ranging over all packed words, is a basis for the
        free `R`-module `WQSym` and called the *Monomial basis*.
        Here it is labelled using ordered set partitions.

        EXAMPLES::

            sage: WQSym = algebras.WQSym(QQ)
            sage: M = WQSym.M(); M
            Word Quasi-symmetric functions over Rational Field in the Monomial basis
            sage: sorted(M.basis(2))
            [M[{1}, {2}], M[{2}, {1}], M[{1, 2}]]
        """
        def product_on_basis(self, x, y):
            """
            Return the (associative) `*` product of the basis elements
            of ``self`` indexed by the ordered set partitions `x` and
            `y`.

            This is the shifted quasi-shuffle product of `x` and `y`.

            EXAMPLES::

                sage: A = algebras.WQSym(QQ).M()
                sage: x = OrderedSetPartition([[1],[2,3]])
                sage: y = OrderedSetPartition([[1,2]])
                sage: z = OrderedSetPartition([[1,2],[3]])
                sage: A.product_on_basis(x, y)
                M[{1}, {2, 3}, {4, 5}] + M[{1}, {2, 3, 4, 5}]
                 + M[{1}, {4, 5}, {2, 3}] + M[{1, 4, 5}, {2, 3}]
                 + M[{4, 5}, {1}, {2, 3}]
                sage: A.product_on_basis(x, z)
                M[{1}, {2, 3}, {4, 5}, {6}] + M[{1}, {2, 3, 4, 5}, {6}]
                 + M[{1}, {4, 5}, {2, 3}, {6}] + M[{1}, {4, 5}, {2, 3, 6}]
                 + M[{1}, {4, 5}, {6}, {2, 3}] + M[{1, 4, 5}, {2, 3}, {6}]
                 + M[{1, 4, 5}, {2, 3, 6}] + M[{1, 4, 5}, {6}, {2, 3}]
                 + M[{4, 5}, {1}, {2, 3}, {6}] + M[{4, 5}, {1}, {2, 3, 6}]
                 + M[{4, 5}, {1}, {6}, {2, 3}] + M[{4, 5}, {1, 6}, {2, 3}]
                 + M[{4, 5}, {6}, {1}, {2, 3}]
                sage: A.product_on_basis(y, y)
                M[{1, 2}, {3, 4}] + M[{1, 2, 3, 4}] + M[{3, 4}, {1, 2}]

            TESTS::

                sage: one = OrderedSetPartition([])
                sage: all(A.product_on_basis(one, z) == A(z) == A.basis()[z] for z in OrderedSetPartitions(3))
                True
                sage: all(A.product_on_basis(z, one) == A(z) == A.basis()[z] for z in OrderedSetPartitions(3))
                True
            """
        def coproduct_on_basis(self, x):
            """
            Return the coproduct of ``self`` on the basis element
            indexed by the ordered set partition ``x``.

            EXAMPLES::

                sage: M = algebras.WQSym(QQ).M()

                sage: M.coproduct(M.one())  # indirect doctest
                M[] # M[]
                sage: M.coproduct( M([[1]]) )  # indirect doctest
                M[] # M[{1}] + M[{1}] # M[]
                sage: M.coproduct( M([[1,2]]) )
                M[] # M[{1, 2}] + M[{1, 2}] # M[]
                sage: M.coproduct( M([[1], [2]]) )
                M[] # M[{1}, {2}] + M[{1}] # M[{1}] + M[{1}, {2}] # M[]
            """
    M = Monomial
    class Characteristic(WQSymBasis_abstract):
        """
        The Characteristic basis of `WQSym`.

        The *Characteristic basis* is a graded basis `(X_P)` of `WQSym`,
        indexed by ordered set partitions `P`. It is defined by

        .. MATH::

            X_P = (-1)^{\\ell(P)} \\mathbf{M}_P ,

        where `(\\mathbf{M}_P)_P` denotes the Monomial basis,
        and where `\\ell(P)` denotes the number of blocks in an ordered
        set partition `P`.

        EXAMPLES::

            sage: WQSym = algebras.WQSym(QQ)
            sage: X = WQSym.X(); X
            Word Quasi-symmetric functions over Rational Field in the Characteristic basis

            sage: X[[[1,2,3]]] * X[[1,2],[3]]
            X[{1, 2, 3}, {4, 5}, {6}] - X[{1, 2, 3, 4, 5}, {6}]
             + X[{4, 5}, {1, 2, 3}, {6}] - X[{4, 5}, {1, 2, 3, 6}]
             + X[{4, 5}, {6}, {1, 2, 3}]

            sage: X[[1, 4], [3], [2]].coproduct()
            X[] # X[{1, 4}, {3}, {2}] + X[{1, 2}] # X[{2}, {1}]
             + X[{1, 3}, {2}] # X[{1}] + X[{1, 4}, {3}, {2}] # X[]

            sage: M = WQSym.M()
            sage: M(X[[1, 2, 3],])
            -M[{1, 2, 3}]
            sage: M(X[[1, 3], [2]])
            M[{1, 3}, {2}]
            sage: X(M[[1, 2, 3],])
            -X[{1, 2, 3}]
            sage: X(M[[1, 3], [2]])
            X[{1, 3}, {2}]
        """
        def __init__(self, alg) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: X = algebras.WQSym(QQ).X()
                sage: TestSuite(X).run()  # long time
            """
        class Element(WQSymBasis_abstract.Element):
            def algebraic_complement(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the algebraic complement involution.

                See
                :meth:`WQSymBases.ElementMethods.algebraic_complement`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`coalgebraic_complement`, :meth:`star_involution`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: X = WQSym.X()
                    sage: X[[1,2],[5,6],[3,4]].algebraic_complement()
                    X[{3, 4}, {5, 6}, {1, 2}]
                    sage: X[[3], [1, 2], [4]].algebraic_complement()
                    X[{4}, {1, 2}, {3}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(X[A]).algebraic_complement() == M(X[A].algebraic_complement())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
            def coalgebraic_complement(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the coalgebraic complement involution.

                See
                :meth:`WQSymBases.ElementMethods.coalgebraic_complement`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`algebraic_complement`, :meth:`star_involution`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: X = WQSym.X()
                    sage: X[[1,2],[5,6],[3,4]].coalgebraic_complement()
                    X[{5, 6}, {1, 2}, {3, 4}]
                    sage: X[[3], [1, 2], [4]].coalgebraic_complement()
                    X[{2}, {3, 4}, {1}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(X[A]).coalgebraic_complement()
                    ....:     == M(X[A].coalgebraic_complement())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
            def star_involution(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the star involution.

                See
                :meth:`WQSymBases.ElementMethods.star_involution`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`algebraic_complement`, :meth:`coalgebraic_complement`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: X = WQSym.X()
                    sage: X[[1,2],[5,6],[3,4]].star_involution()
                    X[{3, 4}, {1, 2}, {5, 6}]
                    sage: X[[3], [1, 2], [4]].star_involution()
                    X[{1}, {3, 4}, {2}]

                TESTS:

                    sage: M = WQSym.M()
                    sage: all(M(X[A]).star_involution() == M(X[A].star_involution())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
    X = Characteristic
    class Cone(WQSymBasis_abstract):
        """
        The Cone basis of `WQSym`.

        Let `(X_P)_P` denote the Characteristic basis of `WQSym`.
        Denote the quasi-shuffle of two ordered set partitions `A` and
        `B` by `A \\Box B`. For an ordered set partition
        `P = (P_1, \\ldots, P_{\\ell})`, we form a list of ordered set
        partitions `[P] := (P'_1, \\ldots, P'_k)` as follows.
        Define a strictly decreasing sequence of integers
        `\\ell + 1 = i_0 > i_1 > \\cdots > i_k = 1` recursively by
        requiring that `\\min P_{i_j} \\leq \\min P_a` for all `a < i_{j-1}`.
        Set `P'_j = (P_{i_j}, \\ldots, P_{i_{j-1}-1})`.

        The *Cone basis* `(C_P)_P` is defined by

        .. MATH::

            C_P = \\sum_Q X_Q,

        where the sum is over all elements `Q` of the quasi-shuffle
        product `P'_1 \\Box P'_2 \\Box \\cdots \\Box P'_k` with
        `[P] = (P'_1, \\ldots, P'_k)`.

        EXAMPLES::

            sage: WQSym = algebras.WQSym(QQ)
            sage: C = WQSym.C()
            sage: C
            Word Quasi-symmetric functions over Rational Field in the Cone basis

            sage: X = WQSym.X()
            sage: X(C[[2,3],[1,4]])
            X[{1, 2, 3, 4}] + X[{1, 4}, {2, 3}] + X[{2, 3}, {1, 4}]
            sage: X(C[[1,4],[2,3]])
            X[{1, 4}, {2, 3}]
            sage: X(C[[2,3],[1],[4]])
            X[{1}, {2, 3}, {4}] + X[{1}, {2, 3, 4}] + X[{1}, {4}, {2, 3}]
             + X[{1, 2, 3}, {4}] + X[{2, 3}, {1}, {4}]
            sage: X(C[[3], [2, 5], [1, 4]])
            X[{1, 2, 3, 4, 5}] + X[{1, 2, 4, 5}, {3}] + X[{1, 3, 4}, {2, 5}]
             + X[{1, 4}, {2, 3, 5}] + X[{1, 4}, {2, 5}, {3}]
             + X[{1, 4}, {3}, {2, 5}] + X[{2, 3, 5}, {1, 4}]
             + X[{2, 5}, {1, 3, 4}] + X[{2, 5}, {1, 4}, {3}]
             + X[{2, 5}, {3}, {1, 4}] + X[{3}, {1, 2, 4, 5}]
             + X[{3}, {1, 4}, {2, 5}] + X[{3}, {2, 5}, {1, 4}]
            sage: C(X[[2,3],[1,4]])
            -C[{1, 2, 3, 4}] - C[{1, 4}, {2, 3}] + C[{2, 3}, {1, 4}]

        REFERENCES:

        - Section 4 of [Early2017]_

        .. TODO::

            Experiments suggest that :meth:`algebraic_complement`,
            :meth:`coalgebraic_complement`, and :meth:`star_involution`
            should have reasonable formulas on the C basis; at least
            the coefficients of the outputs on any element of the C
            basis seem to be always `0, 1, -1`.
            Is this true? What is the formula?
        """
        def __init__(self, alg) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: C = algebras.WQSym(QQ).C()
                sage: TestSuite(C).run()  # long time
            """
        def some_elements(self):
            """
            Return some elements of the word quasi-symmetric functions
            in the Cone basis.

            EXAMPLES::

                sage: C = algebras.WQSym(QQ).C()
                sage: C.some_elements()
                [C[], C[{1}], C[{1, 2}], C[] + 1/2*C[{1}]]
            """
    C = Cone
    class StronglyCoarser(WQSymBasis_abstract):
        """
        The Q basis of `WQSym`.

        We define a partial order `\\leq` on the set of all ordered
        set partitions as follows: `A \\leq B` if and only if
        `A` is strongly finer than `B` (see
        :meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.is_strongly_finer`
        for a definition of this).

        The *Q basis* `(Q_P)_P` is a basis of `WQSym` indexed by ordered
        set partitions, and is defined by

        .. MATH::

            Q_P = \\sum \\mathbf{M}_W,

        where the sum is over ordered set partitions `W` satisfying
        `P \\leq W`.

        EXAMPLES::

            sage: WQSym = algebras.WQSym(QQ)
            sage: M = WQSym.M(); Q = WQSym.Q()
            sage: Q
            Word Quasi-symmetric functions over Rational Field in the Q basis

            sage: Q(M[[2,3],[1,4]])
            Q[{2, 3}, {1, 4}]
            sage: Q(M[[1,2],[3,4]])
            Q[{1, 2}, {3, 4}] - Q[{1, 2, 3, 4}]
            sage: M(Q[[1,2],[3,4]])
            M[{1, 2}, {3, 4}] + M[{1, 2, 3, 4}]
            sage: M(Q[[2,3],[1],[4]])
            M[{2, 3}, {1}, {4}] + M[{2, 3}, {1, 4}]
            sage: M(Q[[3], [2, 5], [1, 4]])
            M[{3}, {2, 5}, {1, 4}]
            sage: M(Q[[1, 4], [2, 3], [5], [6]])
            M[{1, 4}, {2, 3}, {5}, {6}] + M[{1, 4}, {2, 3}, {5, 6}]
             + M[{1, 4}, {2, 3, 5}, {6}] + M[{1, 4}, {2, 3, 5, 6}]

            sage: Q[[1, 3], [2]] * Q[[1], [2]]
            Q[{1, 3}, {2}, {4}, {5}] + Q[{1, 3}, {4}, {2}, {5}]
             + Q[{1, 3}, {4}, {5}, {2}] + Q[{4}, {1, 3}, {2}, {5}]
             + Q[{4}, {1, 3}, {5}, {2}] + Q[{4}, {5}, {1, 3}, {2}]

            sage: Q[[1, 3], [2]].coproduct()
            Q[] # Q[{1, 3}, {2}] + Q[{1, 2}] # Q[{1}] + Q[{1, 3}, {2}] # Q[]

        REFERENCES:

        - Section 6 of [BerZab05]_
        """
        def __init__(self, alg) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: Q = algebras.WQSym(QQ).Q()
                sage: TestSuite(Q).run()  # long time
            """
        def some_elements(self):
            """
            Return some elements of the word quasi-symmetric functions
            in the Q basis.

            EXAMPLES::

                sage: Q = algebras.WQSym(QQ).Q()
                sage: Q.some_elements()
                [Q[], Q[{1}], Q[{1, 2}], Q[] + 1/2*Q[{1}]]
            """
        def product_on_basis(self, x, y):
            """
            Return the (associative) `*` product of the basis elements
            of the Q basis ``self`` indexed by the ordered set partitions
            `x` and `y`.

            This is the shifted shuffle product of `x` and `y`.

            EXAMPLES::

                sage: A = algebras.WQSym(QQ).Q()
                sage: x = OrderedSetPartition([[1],[2,3]])
                sage: y = OrderedSetPartition([[1,2]])
                sage: z = OrderedSetPartition([[1,2],[3]])
                sage: A.product_on_basis(x, y)
                Q[{1}, {2, 3}, {4, 5}] + Q[{1}, {4, 5}, {2, 3}]
                 + Q[{4, 5}, {1}, {2, 3}]
                sage: A.product_on_basis(x, z)
                Q[{1}, {2, 3}, {4, 5}, {6}] + Q[{1}, {4, 5}, {2, 3}, {6}]
                 + Q[{1}, {4, 5}, {6}, {2, 3}] + Q[{4, 5}, {1}, {2, 3}, {6}]
                 + Q[{4, 5}, {1}, {6}, {2, 3}] + Q[{4, 5}, {6}, {1}, {2, 3}]
                sage: A.product_on_basis(y, y)
                Q[{1, 2}, {3, 4}] + Q[{3, 4}, {1, 2}]

            TESTS::

                sage: one = OrderedSetPartition([])
                sage: all(A.product_on_basis(one, z) == A(z) == A.basis()[z] for z in OrderedSetPartitions(3))
                True
                sage: all(A.product_on_basis(z, one) == A(z) == A.basis()[z] for z in OrderedSetPartitions(3))
                True
            """
        def coproduct_on_basis(self, x):
            """
            Return the coproduct of ``self`` on the basis element
            indexed by the ordered set partition ``x``.

            EXAMPLES::

                sage: Q = algebras.WQSym(QQ).Q()

                sage: Q.coproduct(Q.one())  # indirect doctest
                Q[] # Q[]
                sage: Q.coproduct( Q([[1]]) )  # indirect doctest
                Q[] # Q[{1}] + Q[{1}] # Q[]
                sage: Q.coproduct( Q([[1,2]]) )
                Q[] # Q[{1, 2}] + Q[{1, 2}] # Q[]
                sage: Q.coproduct( Q([[1], [2]]) )
                Q[] # Q[{1}, {2}] + Q[{1}] # Q[{1}] + Q[{1}, {2}] # Q[]
                sage: Q[[1,2],[3],[4]].coproduct()
                Q[] # Q[{1, 2}, {3}, {4}] + Q[{1, 2}] # Q[{1}, {2}]
                 + Q[{1, 2}, {3}] # Q[{1}] + Q[{1, 2}, {3}, {4}] # Q[]
            """
        class Element(WQSymBasis_abstract.Element):
            def algebraic_complement(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the algebraic complement involution.

                See
                :meth:`WQSymBases.ElementMethods.algebraic_complement`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`coalgebraic_complement`, :meth:`star_involution`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: Q = WQSym.Q()
                    sage: Q[[1,2],[5,6],[3,4]].algebraic_complement()
                    Q[{3, 4}, {1, 2, 5, 6}] + Q[{3, 4}, {5, 6}, {1, 2}]
                     - Q[{3, 4, 5, 6}, {1, 2}]
                    sage: Q[[3], [1, 2], [4]].algebraic_complement()
                    Q[{1, 2, 4}, {3}] + Q[{4}, {1, 2}, {3}] - Q[{4}, {1, 2, 3}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(Q[A]).algebraic_complement()  # long time
                    ....:     == M(Q[A].algebraic_complement())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
            def coalgebraic_complement(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the coalgebraic complement involution.

                See
                :meth:`WQSymBases.ElementMethods.coalgebraic_complement`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`algebraic_complement`, :meth:`star_involution`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: Q = WQSym.Q()
                    sage: Q[[1,2],[5,6],[3,4]].coalgebraic_complement()
                    Q[{1, 2, 5, 6}, {3, 4}] + Q[{5, 6}, {1, 2}, {3, 4}] - Q[{5, 6}, {1, 2, 3, 4}]
                    sage: Q[[3], [1, 2], [4]].coalgebraic_complement()
                    Q[{2}, {1, 3, 4}] + Q[{2}, {3, 4}, {1}] - Q[{2, 3, 4}, {1}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(Q[A]).coalgebraic_complement()  # long time
                    ....:     == M(Q[A].coalgebraic_complement())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
            def star_involution(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the star involution.

                See
                :meth:`WQSymBases.ElementMethods.star_involution`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`algebraic_complement`, :meth:`coalgebraic_complement`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: Q = WQSym.Q()
                    sage: Q[[1,2],[5,6],[3,4]].star_involution()
                    Q[{3, 4}, {1, 2}, {5, 6}]
                    sage: Q[[3], [1, 2], [4]].star_involution()
                    Q[{1}, {3, 4}, {2}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(Q[A]).star_involution() == M(Q[A].star_involution())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
    Q = StronglyCoarser
    class StronglyFiner(WQSymBasis_abstract):
        """
        The Phi basis of `WQSym`.

        We define a partial order `\\leq` on the set of all ordered
        set partitions as follows: `A \\leq B` if and only if
        `A` is strongly finer than `B` (see
        :meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.is_strongly_finer`
        for a definition of this).

        The *Phi basis* `(\\Phi_P)_P` is a basis of `WQSym` indexed by ordered
        set partitions, and is defined by

        .. MATH::

            \\Phi_P = \\sum \\mathbf{M}_W,

        where the sum is over ordered set partitions `W` satisfying
        `W \\leq P`.

        Novelli and Thibon introduced this basis in [NovThi06]_
        Section 2.7.2, and called it the quasi-ribbon basis.
        It later reappeared in [MeNoTh11]_ Section 4.3.2.

        EXAMPLES::

            sage: WQSym = algebras.WQSym(QQ)
            sage: M = WQSym.M(); Phi = WQSym.Phi()
            sage: Phi
            Word Quasi-symmetric functions over Rational Field in the Phi basis

            sage: Phi(M[[2,3],[1,4]])
            Phi[{2}, {3}, {1}, {4}] - Phi[{2}, {3}, {1, 4}]
             - Phi[{2, 3}, {1}, {4}] + Phi[{2, 3}, {1, 4}]
            sage: Phi(M[[1,2],[3,4]])
            Phi[{1}, {2}, {3}, {4}] - Phi[{1}, {2}, {3, 4}]
             - Phi[{1, 2}, {3}, {4}] + Phi[{1, 2}, {3, 4}]
            sage: M(Phi[[1,2],[3,4]])
            M[{1}, {2}, {3}, {4}] + M[{1}, {2}, {3, 4}]
             + M[{1, 2}, {3}, {4}] + M[{1, 2}, {3, 4}]
            sage: M(Phi[[2,3],[1],[4]])
            M[{2}, {3}, {1}, {4}] + M[{2, 3}, {1}, {4}]
            sage: M(Phi[[3], [2, 5], [1, 4]])
            M[{3}, {2}, {5}, {1}, {4}] + M[{3}, {2}, {5}, {1, 4}]
             + M[{3}, {2, 5}, {1}, {4}] + M[{3}, {2, 5}, {1, 4}]
            sage: M(Phi[[1, 4], [2, 3], [5], [6]])
            M[{1}, {4}, {2}, {3}, {5}, {6}] + M[{1}, {4}, {2, 3}, {5}, {6}]
             + M[{1, 4}, {2}, {3}, {5}, {6}] + M[{1, 4}, {2, 3}, {5}, {6}]

            sage: Phi[[1],] * Phi[[1, 3], [2]]
            Phi[{1, 2, 4}, {3}] + Phi[{2}, {1, 4}, {3}]
             + Phi[{2, 4}, {1, 3}] + Phi[{2, 4}, {3}, {1}]
            sage: Phi[[3, 5], [1, 4], [2]].coproduct()
            Phi[] # Phi[{3, 5}, {1, 4}, {2}]
             + Phi[{1}] # Phi[{4}, {1, 3}, {2}]
             + Phi[{1, 2}] # Phi[{1, 3}, {2}]
             + Phi[{2, 3}, {1}] # Phi[{2}, {1}]
             + Phi[{2, 4}, {1, 3}] # Phi[{1}]
             + Phi[{3, 5}, {1, 4}, {2}] # Phi[]

        REFERENCES:

        - Section 2.7.2 of [NovThi06]_
        """
        def __init__(self, alg) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: Phi = algebras.WQSym(QQ).Phi()
                sage: TestSuite(Phi).run()  # long time
            """
        def some_elements(self):
            """
            Return some elements of the word quasi-symmetric functions
            in the Phi basis.

            EXAMPLES::

                sage: Phi = algebras.WQSym(QQ).Phi()
                sage: Phi.some_elements()
                [Phi[], Phi[{1}], Phi[{1, 2}], Phi[] + 1/2*Phi[{1}]]
            """
        def product_on_basis(self, x, y):
            """
            Return the (associative) `*` product of the basis elements
            of the Phi basis ``self`` indexed by the ordered set partitions
            `x` and `y`.

            This is obtained by the following algorithm (going back to
            [NovThi06]_):

            Let `x` be an ordered set partition of `[m]`, and `y` an
            ordered set partition of `[n]`.
            Transform `x` into a list `u` of all the `m` elements of `[m]`
            by writing out each block of `x` (in increasing order) and
            putting bars between each two consecutive blocks; this is
            called a barred permutation.
            Do the same for `y`, but also shift each entry of the
            resulting barred permutation by `m`. Let `v` be the barred
            permutation of `[m+n] \\setminus [m]` thus obtained.
            Now, shuffle the two barred permutations `u` and `v`
            (ignoring the bars) in all the `\\binom{n+m}{n}` possible ways.
            For each shuffle obtained, place bars between some entries
            of the shuffle, according to the following rule:

            * If two consecutive entries of the shuffle both come from
              `u`, then place a bar between them if the corresponding
              entries of `u` had a bar between them.

            * If the first of two consecutive entries of the shuffle
              comes from `v` and the second from `u`, then place a bar
              between them.

            This results in a barred permutation of `[m+n]`.
            Transform it into an ordered set partition of `[m+n]`,
            by treating the bars as dividers separating consecutive
            blocks.

            The product `\\Phi_x \\Phi_y` is the sum of `\\Phi_p` with
            `p` ranging over all ordered set partitions obtained this
            way.

            EXAMPLES::

                sage: A = algebras.WQSym(QQ).Phi()
                sage: x = OrderedSetPartition([[1],[2,3]])
                sage: y = OrderedSetPartition([[1,2]])
                sage: z = OrderedSetPartition([[1,2],[3]])
                sage: A.product_on_basis(x, y)
                Phi[{1}, {2, 3, 4, 5}] + Phi[{1}, {2, 4}, {3, 5}]
                 + Phi[{1}, {2, 4, 5}, {3}] + Phi[{1, 4}, {2, 3, 5}]
                 + Phi[{1, 4}, {2, 5}, {3}] + Phi[{1, 4, 5}, {2, 3}]
                 + Phi[{4}, {1}, {2, 3, 5}] + Phi[{4}, {1}, {2, 5}, {3}]
                 + Phi[{4}, {1, 5}, {2, 3}] + Phi[{4, 5}, {1}, {2, 3}]
                sage: A.product_on_basis(x, z)
                Phi[{1}, {2, 3, 4, 5}, {6}] + Phi[{1}, {2, 4}, {3, 5}, {6}]
                 + Phi[{1}, {2, 4, 5}, {3, 6}] + Phi[{1}, {2, 4, 5}, {6}, {3}]
                 + Phi[{1, 4}, {2, 3, 5}, {6}] + Phi[{1, 4}, {2, 5}, {3, 6}]
                 + Phi[{1, 4}, {2, 5}, {6}, {3}] + Phi[{1, 4, 5}, {2, 3, 6}]
                 + Phi[{1, 4, 5}, {2, 6}, {3}] + Phi[{1, 4, 5}, {6}, {2, 3}]
                 + Phi[{4}, {1}, {2, 3, 5}, {6}]
                 + Phi[{4}, {1}, {2, 5}, {3, 6}]
                 + Phi[{4}, {1}, {2, 5}, {6}, {3}]
                 + Phi[{4}, {1, 5}, {2, 3, 6}] + Phi[{4}, {1, 5}, {2, 6}, {3}]
                 + Phi[{4}, {1, 5}, {6}, {2, 3}] + Phi[{4, 5}, {1}, {2, 3, 6}]
                 + Phi[{4, 5}, {1}, {2, 6}, {3}] + Phi[{4, 5}, {1, 6}, {2, 3}]
                 + Phi[{4, 5}, {6}, {1}, {2, 3}]
                sage: A.product_on_basis(y, y)
                Phi[{1, 2, 3, 4}] + Phi[{1, 3}, {2, 4}] + Phi[{1, 3, 4}, {2}]
                 + Phi[{3}, {1, 2, 4}] + Phi[{3}, {1, 4}, {2}]
                 + Phi[{3, 4}, {1, 2}]

            TESTS::

                sage: one = OrderedSetPartition([])
                sage: all(A.product_on_basis(one, z) == A(z) == A.basis()[z] for z in OrderedSetPartitions(3))
                True
                sage: all(A.product_on_basis(z, one) == A(z) == A.basis()[z] for z in OrderedSetPartitions(3))
                True
                sage: M = algebras.WQSym(QQ).M()
                sage: x = A[[2, 4], [1, 3]]
                sage: y = A[[1, 3], [2]]
                sage: A(M(x) * M(y)) == x * y  # long time
                True
                sage: A(M(x) ** 2) == x**2 # long time
                True
                sage: A(M(y) ** 2) == y**2
                True
            """
        def coproduct_on_basis(self, x):
            '''
            Return the coproduct of ``self`` on the basis element
            indexed by the ordered set partition ``x``.

            The coproduct of the basis element `\\Phi_x` indexed by
            an ordered set partition `x` of `[n]` can be computed by the
            following formula ([NovThi06]_):

            .. MATH::

                \\Delta \\Phi_x
                = \\sum \\Phi_y \\otimes \\Phi_z ,

            where the sum ranges over all pairs `(y, z)` of ordered set
            partitions `y` and `z` such that:

            * `y` and `z` are ordered set partitions of two complementary
              subsets of `[n]`;

            * `x` is obtained either by concatenating `y` and `z`, or by
              first concatenating `y` and `z` and then merging the two
              "middle blocks" (i.e., the last block of `y` and the first
              block of `z`); in the latter case, the maximum of the last
              block of `y` has to be smaller than the minimum of the first
              block of `z` (so that when merging these blocks, their
              entries don\'t need to be sorted).

            EXAMPLES::

                sage: Phi = algebras.WQSym(QQ).Phi()

                sage: Phi.coproduct(Phi.one())  # indirect doctest
                Phi[] # Phi[]
                sage: Phi.coproduct( Phi([[1]]) )  # indirect doctest
                Phi[] # Phi[{1}] + Phi[{1}] # Phi[]
                sage: Phi.coproduct( Phi([[1,2]]) )
                Phi[] # Phi[{1, 2}] + Phi[{1}] # Phi[{1}] + Phi[{1, 2}] # Phi[]
                sage: Phi.coproduct( Phi([[1], [2]]) )
                Phi[] # Phi[{1}, {2}] + Phi[{1}] # Phi[{1}] + Phi[{1}, {2}] # Phi[]
                sage: Phi[[1,2],[3],[4]].coproduct()
                Phi[] # Phi[{1, 2}, {3}, {4}] + Phi[{1}] # Phi[{1}, {2}, {3}]
                 + Phi[{1, 2}] # Phi[{1}, {2}] + Phi[{1, 2}, {3}] # Phi[{1}]
                 + Phi[{1, 2}, {3}, {4}] # Phi[]

            TESTS::

                sage: M = algebras.WQSym(QQ).M()
                sage: x = Phi[[2, 4], [6], [1, 3], [5, 7]]
                sage: MM = M.tensor(M); AA = Phi.tensor(Phi)
                sage: AA(M(x).coproduct()) == x.coproduct()
                True
            '''
        class Element(WQSymBasis_abstract.Element):
            def algebraic_complement(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the algebraic complement involution.

                See
                :meth:`WQSymBases.ElementMethods.algebraic_complement`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`coalgebraic_complement`, :meth:`star_involution`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: Phi = WQSym.Phi()
                    sage: Phi[[1],[2,4],[3]].algebraic_complement()
                    -Phi[{3}, {2}, {4}, {1}] + Phi[{3}, {2, 4}, {1}] + Phi[{3}, {4}, {2}, {1}]
                    sage: Phi[[1],[2,3],[4]].algebraic_complement()
                    -Phi[{4}, {2}, {3}, {1}] + Phi[{4}, {2, 3}, {1}] + Phi[{4}, {3}, {2}, {1}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(Phi[A]).algebraic_complement()
                    ....:     == M(Phi[A].algebraic_complement())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
            def coalgebraic_complement(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the coalgebraic complement involution.

                See
                :meth:`WQSymBases.ElementMethods.coalgebraic_complement`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`algebraic_complement`, :meth:`star_involution`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: Phi = WQSym.Phi()
                    sage: Phi[[1],[2],[3,4]].coalgebraic_complement()
                    -Phi[{4}, {3}, {1}, {2}] + Phi[{4}, {3}, {1, 2}] + Phi[{4}, {3}, {2}, {1}]
                    sage: Phi[[2],[1,4],[3]].coalgebraic_complement()
                    -Phi[{3}, {1}, {4}, {2}] + Phi[{3}, {1, 4}, {2}] + Phi[{3}, {4}, {1}, {2}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(Phi[A]).coalgebraic_complement()
                    ....:     == M(Phi[A].coalgebraic_complement())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
            def star_involution(self):
                """
                Return the image of the element ``self`` of `WQSym`
                under the star involution.

                See
                :meth:`WQSymBases.ElementMethods.star_involution`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`algebraic_complement`, :meth:`coalgebraic_complement`

                EXAMPLES::

                    sage: WQSym = algebras.WQSym(ZZ)
                    sage: Phi = WQSym.Phi()
                    sage: Phi[[1,2],[5,6],[3,4]].star_involution()
                    Phi[{3, 4}, {1, 2}, {5, 6}]
                    sage: Phi[[3], [1, 2], [4]].star_involution()
                    Phi[{1}, {3, 4}, {2}]

                TESTS::

                    sage: M = WQSym.M()
                    sage: all(M(Phi[A]).star_involution() == M(Phi[A].star_involution())
                    ....:     for A in OrderedSetPartitions(4))
                    True
                """
    Phi = StronglyFiner

class WQSymBases(Category_realization_of_parent):
    """
    The category of bases of `WQSym`.
    """
    def __init__(self, base, graded) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``base`` -- an instance of `WQSym`
        - ``graded`` -- boolean; if the basis is graded or filtered

        TESTS::

            sage: from sage.combinat.chas.wqsym import WQSymBases
            sage: WQSym = algebras.WQSym(ZZ)
            sage: bases = WQSymBases(WQSym, True)
            sage: WQSym.M() in bases
            True
        """
    def super_categories(self):
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.chas.wqsym import WQSymBases
            sage: WQSym = algebras.WQSym(ZZ)
            sage: bases = WQSymBases(WQSym, True)
            sage: bases.super_categories()
            [Category of realizations of Word Quasi-symmetric functions over Integer Ring,
             Join of Category of realizations of Hopf algebras over Integer Ring
                 and Category of graded algebras over Integer Ring
                 and Category of graded coalgebras over Integer Ring,
             Category of graded connected Hopf algebras with basis over Integer Ring]

            sage: bases = WQSymBases(WQSym, False)
            sage: bases.super_categories()
            [Category of realizations of Word Quasi-symmetric functions over Integer Ring,
             Join of Category of realizations of Hopf algebras over Integer Ring
                 and Category of graded algebras over Integer Ring
                 and Category of graded coalgebras over Integer Ring,
             Join of Category of filtered connected Hopf algebras with basis over Integer Ring
                 and Category of graded algebras over Integer Ring
                 and Category of graded coalgebras over Integer Ring]
        """
    class ParentMethods:
        def __getitem__(self, p):
            """
            Return the basis element indexed by ``p``.

            INPUT:

            - ``p`` -- an ordered set partition

            EXAMPLES::

                sage: M = algebras.WQSym(QQ).M()
                sage: M[1, 2, 1]  # pass a word
                M[{1, 3}, {2}]
                sage: _ == M[[1, 2, 1]] == M[Word([1,2,1])]
                True
                sage: M[[1, 2, 3]]
                M[{1}, {2}, {3}]

                sage: M[[[1, 2, 3]]]  # pass an ordered set partition
                M[{1, 2, 3}]
                sage: _ == M[[1,2,3],] == M[OrderedSetPartition([[1,2,3]])]
                True
                sage: M[[1,3],[2]]
                M[{1, 3}, {2}]

            TESTS::

                sage: M[[]]
                M[]
                sage: M[1, 2, 1] == M[Word([2,3,2])] == M[Word('aca')]
                True
                sage: M[[[1,2]]] == M[1,1] == M[1/1,2/2] == M[2/1,2/1] == M['aa']
                True
                sage: M[1] == M[1,] == M[Word([1])] == M[OrderedSetPartition([[1]])] == M[[1],]
                True
            """
        def is_field(self, proof: bool = True):
            """
            Return whether ``self`` is a field.

            EXAMPLES::

                sage: M = algebras.WQSym(QQ).M()
                sage: M.is_field()
                False
            """
        def one_basis(self):
            """
            Return the index of the unit.

            EXAMPLES::

                sage: A = algebras.WQSym(QQ).M()
                sage: A.one_basis()
                []
            """
        def degree_on_basis(self, t):
            """
            Return the degree of an ordered set partition in
            the algebra of word quasi-symmetric functions.

            This is the sum of the sizes of the blocks of the
            ordered set partition.

            EXAMPLES::

                sage: A = algebras.WQSym(QQ).M()
                sage: u = OrderedSetPartition([[2,1],])
                sage: A.degree_on_basis(u)
                2
                sage: u = OrderedSetPartition([[2], [1]])
                sage: A.degree_on_basis(u)
                2
            """
    class ElementMethods:
        def algebraic_complement(self):
            """
            Return the image of the element ``self`` of `WQSym`
            under the algebraic complement involution.

            If `u = (u_1, u_2, \\ldots, u_n)` is a packed word
            that contains the letters `1, 2, \\ldots, k` and no
            others, then the *complement* of `u` is defined to
            be the packed word
            `\\overline{u} := (k+1 - u_1, k+1 - u_2, \\ldots, k+1 - u_n)`.

            The algebraic complement involution is defined as the
            linear map `WQSym \\to WQSym` that sends each basis
            element `\\mathbf{M}_u` of the monomial basis of `WQSym`
            to the basis element `\\mathbf{M}_{\\overline{u}}`.
            This is a graded algebra automorphism and a coalgebra
            anti-automorphism of `WQSym`.
            Denoting by `\\overline{f}` the image of an element
            `f \\in WQSym` under the algebraic complement involution,
            it can be shown that every packed word `u` satisfies

            .. MATH::

                \\overline{\\mathbf{M}_u} = \\mathbf{M}_{\\overline{u}},
                \\qquad \\overline{X_u} = X_{\\overline{u}},

            where standard notations for classical bases of `WQSym`
            are being used (that is, `\\mathbf{M}` for the monomial
            basis, and `X` for the characteristic basis).

            This can be restated in terms of ordered set partitions:
            For any ordered set partition `R = (R_1, R_2, \\ldots, R_k)`,
            let `R^r` denote the ordered set partition
            `(R_k, R_{k-1}, \\ldots, R_1)`; this is known as
            the *reversal* of `R`. Then,

            .. MATH::

                \\overline{\\mathbf{M}_A} = \\mathbf{M}_{A^r}, \\qquad
                \\overline{X_A} = X_{A^r}

            for any ordered set partition `A`.

            The formula describing algebraic complements on the Q basis
            (:class:`WordQuasiSymmetricFunctions.StronglyCoarser`)
            is more complicated, and requires some definitions.
            We define a partial order `\\leq` on the set of all ordered
            set partitions as follows: `A \\leq B` if and only if
            `A` is strongly finer than `B` (see
            :meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.is_strongly_finer`
            for a definition of this).
            The *length* `\\ell(R)` of an ordered set partition `R` shall
            be defined as the number of parts of `R`.
            Use the notation `Q` for the Q basis.
            For any ordered set partition `A` of `[n]`, we have

            .. MATH::

                \\overline{Q_A} = \\sum_P c_{A, P} Q_P,

            where the sum is over all ordered set partitions `P` of
            `[n]`, and where the coefficient `c_{A, P}` is defined
            as follows:

            * If there exists an ordered set partition `R` satisfying
              `R \\leq P` and `A \\leq R^r`, then this `R` is unique,
              and `c_{A, P} = \\left(-1\\right)^{\\ell(R) - \\ell(P)}`.

            * If there exists no such `R`, then `c_{A, P} = 0`.

            The formula describing algebraic complements on the `\\Phi`
            basis (:class:`WordQuasiSymmetricFunctions.StronglyFiner`)
            is identical to the above formula for the Q basis, except
            that the `\\leq` sign has to be replaced by `\\geq` in the
            definition of the coefficients `c_{A, P}`. In fact, both
            formulas are particular cases of a general formula for
            involutions:
            Assume that `V` is an (additive) abelian group, and that
            `I` is a poset. For each `i \\in I`, let `M_i` be an element
            of `V`. Also, let `\\omega` be an involution of the set `I`
            (not necessarily order-preserving or order-reversing),
            and let `\\omega'` be an involutive group endomorphism of
            `V` such that each `i \\in I` satisfies
            `\\omega'(M_i) = M_{\\omega(i)}`.
            For each `i \\in I`, let `F_i = \\sum_{j \\geq i} M_j`,
            where we assume that the sum is finite.
            Then, each `i \\in I` satisfies

            .. MATH::

                \\omega'(F_i)
                = \\sum_j \\sum_{\\substack{k \\leq j; \\\\ \\omega(k) \\geq i}}
                  \\mu(k, j) F_j,

            where `\\mu` denotes the Möbius function. This formula becomes
            particularly useful when the `k` satisfying `k \\leq j`
            and `\\omega(k) \\geq i` is unique (if it exists).
            In our situation, `V` is `WQSym`, and `I` is the set of
            ordered set partitions equipped either with the `\\leq` partial
            order defined above or with its opposite order.
            The `M_i` is the `\\mathbf{M}_A`, whereas the `F_i` is either
            `Q_i` or `\\Phi_i`.

            If we denote the star involution
            (:meth:`~sage.combinat.ncsf_qsym.qsym.QuasiSymmetricFunctions.Bases.ElementMethods.star_involution`)
            of the quasisymmetric functions by `f \\mapsto f^{\\ast}`,
            and if we let `\\pi` be the canonical projection
            `WQSym \\to QSym`, then each `f \\in WQSym` satisfies
            `\\pi(\\overline{f}) = (\\pi(f))^{\\ast}`.

            .. SEEALSO::

                :meth:`coalgebraic_complement`, :meth:`star_involution`

            EXAMPLES:

            Recall that the index set for the bases of `WQSym` is
            given by ordered set partitions, not packed words.
            Translated into the language of ordered set partitions,
            the algebraic complement involution acts on the
            Monomial basis by reversing the ordered set partition.
            In other words, we have

            .. MATH::

                \\overline{\\mathbf{M}_{(P_1, P_2, \\ldots, P_k)}}
                = \\mathbf{M}_{(P_k, P_{k-1}, \\ldots, P_1)}

            for any standard ordered set partition
            `(P_1, P_2, \\ldots, P_k)`. Let us check this in practice::

                sage: WQSym = algebras.WQSym(ZZ)
                sage: M = WQSym.M()
                sage: M[[1,3],[2]].algebraic_complement()
                M[{2}, {1, 3}]
                sage: M[[1,4],[2,5],[3,6]].algebraic_complement()
                M[{3, 6}, {2, 5}, {1, 4}]
                sage: (3*M[[1]] - 4*M[[]] + 5*M[[1],[2]]).algebraic_complement()
                -4*M[] + 3*M[{1}] + 5*M[{2}, {1}]
                sage: X = WQSym.X()
                sage: X[[1,3],[2]].algebraic_complement()
                X[{2}, {1, 3}]
                sage: C = WQSym.C()
                sage: C[[1,3],[2]].algebraic_complement()
                -C[{1, 2, 3}] - C[{1, 3}, {2}] + C[{2}, {1, 3}]
                sage: Q = WQSym.Q()
                sage: Q[[1,2],[5,6],[3,4]].algebraic_complement()
                Q[{3, 4}, {1, 2, 5, 6}] + Q[{3, 4}, {5, 6}, {1, 2}] - Q[{3, 4, 5, 6}, {1, 2}]
                sage: Phi = WQSym.Phi()
                sage: Phi[[2], [1,3]].algebraic_complement()
                -Phi[{1}, {3}, {2}] + Phi[{1, 3}, {2}] + Phi[{3}, {1}, {2}]

            The algebraic complement involution intertwines the antipode
            and the inverse of the antipode::

                sage: all( M(I).antipode().algebraic_complement().antipode()  # long time
                ....:      == M(I).algebraic_complement()
                ....:      for I in OrderedSetPartitions(4) )
                True

            Testing the `\\pi(\\overline{f}) = (\\pi(f))^{\\ast}` relation::

                sage: all( M[I].algebraic_complement().to_quasisymmetric_function()
                ....:      == M[I].to_quasisymmetric_function().star_involution()
                ....:      for I in OrderedSetPartitions(4) )
                True

            .. TODO::

                Check further commutative squares.
            """
        def coalgebraic_complement(self):
            """
            Return the image of the element ``self`` of `WQSym`
            under the coalgebraic complement involution.

            If `u = (u_1, u_2, \\ldots, u_n)` is a packed word,
            then the *reversal* of `u` is defined to be the
            packed word `(u_n, u_{n-1}, \\ldots, u_1)`.
            This reversal is denoted by `u^r`.

            The coalgebraic complement involution is defined as the
            linear map `WQSym \\to WQSym` that sends each basis
            element `\\mathbf{M}_u` of the monomial basis of `WQSym`
            to the basis element `\\mathbf{M}_{u^r}`.
            This is a graded coalgebra automorphism and an algebra
            anti-automorphism of `WQSym`.
            Denoting by `f^r` the image of an element `f \\in WQSym`
            under the coalgebraic complement involution,
            it can be shown that every packed word `u` satisfies

            .. MATH::

                (\\mathbf{M}_u)^r = \\mathbf{M}_{u^r}, \\qquad
                (X_u)^r = X_{u^r},

            where standard notations for classical bases of `WQSym`
            are being used (that is, `\\mathbf{M}` for the monomial
            basis, and `X` for the characteristic basis).

            This can be restated in terms of ordered set partitions:
            For any ordered set partition `R` of `[n]`, let
            `\\overline{R}` denote the complement of `R` (defined in
            :meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.complement`).
            Then,

            .. MATH::

                (\\mathbf{M}_A)^r = \\mathbf{M}_{\\overline{A}}, \\qquad
                (X_A)^r = X_{\\overline{A}}

            for any ordered set partition `A`.

            Recall that `WQSym` is a subring of the ring of all
            bounded-degree noncommutative power series in countably many
            indeterminates. The latter ring has an obvious continuous
            algebra anti-endomorphism which sends each letter `x_i` to
            `x_i` (and thus sends each monomial
            `x_{i_1} x_{i_2} \\cdots x_{i_n}` to
            `x_{i_n} x_{i_{n-1}} \\cdots x_{i_1}`).
            This anti-endomorphism is actually an involution.
            The coalgebraic complement involution is simply the
            restriction of this involution to the subring `WQSym`.

            The formula describing coalgebraic complements on the Q basis
            (:class:`WordQuasiSymmetricFunctions.StronglyCoarser`)
            is more complicated, and requires some definitions.
            We define a partial order `\\leq` on the set of all ordered
            set partitions as follows: `A \\leq B` if and only if
            `A` is strongly finer than `B` (see
            :meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.is_strongly_finer`
            for a definition of this).
            The *length* `\\ell(R)` of an ordered set partition `R` shall
            be defined as the number of parts of `R`.
            Use the notation `Q` for the Q basis.
            For any ordered set partition `A` of `[n]`, we have

            .. MATH::

                (Q_A)^r = \\sum_P c_{A, P} Q_P ,

            where the sum is over all ordered set partitions `P` of
            `[n]`, and where the coefficient `c_{A, P}` is defined
            as follows:

            * If there exists an ordered set partition `R` satisfying
              `R \\leq P` and `A \\leq \\overline{R}`, then this `R` is
              unique,
              and `c_{A, P} = \\left(-1\\right)^{\\ell(R) - \\ell(P)}`.

            * If there exists no such `R`, then `c_{A, P} = 0`.

            The formula describing coalgebraic complements on the `\\Phi`
            basis (:class:`WordQuasiSymmetricFunctions.StronglyFiner`)
            is identical to the above formula for the Q basis, except
            that the `\\leq` sign has to be replaced by `\\geq` in the
            definition of the coefficients `c_{A, P}`. In fact, both
            formulas are particular cases of the general formula for
            involutions described in the documentation of
            :meth:`algebraic_complement`.

            If we let `\\pi` be the canonical projection
            `WQSym \\to QSym`, then each `f \\in WQSym` satisfies
            `\\pi(f^r) = \\pi(f)`.

            .. SEEALSO::

                :meth:`algebraic_complement`, :meth:`star_involution`

            EXAMPLES:

            Recall that the index set for the bases of `WQSym` is
            given by ordered set partitions, not packed words.
            Translated into the language of ordered set partitions,
            the coalgebraic complement involution acts on the
            Monomial basis by complementing the ordered set partition.
            In other words, we have

            .. MATH::

                (\\mathbf{M}_A)^r = \\mathbf{M}_{\\overline{A}}

            for any standard ordered set partition `P`.
            Let us check this in practice::

                sage: WQSym = algebras.WQSym(ZZ)
                sage: M = WQSym.M()
                sage: M[[1,3],[2]].coalgebraic_complement()
                M[{1, 3}, {2}]
                sage: M[[1,2],[3]].coalgebraic_complement()
                M[{2, 3}, {1}]
                sage: M[[1], [4], [2,3]].coalgebraic_complement()
                M[{4}, {1}, {2, 3}]
                sage: M[[1,4],[2,5],[3,6]].coalgebraic_complement()
                M[{3, 6}, {2, 5}, {1, 4}]
                sage: (3*M[[1]] - 4*M[[]] + 5*M[[1],[2]]).coalgebraic_complement()
                -4*M[] + 3*M[{1}] + 5*M[{2}, {1}]
                sage: X = WQSym.X()
                sage: X[[1,3],[2]].coalgebraic_complement()
                X[{1, 3}, {2}]
                sage: C = WQSym.C()
                sage: C[[1,3],[2]].coalgebraic_complement()
                C[{1, 3}, {2}]
                sage: Q = WQSym.Q()
                sage: Q[[1,2],[5,6],[3,4]].coalgebraic_complement()
                Q[{1, 2, 5, 6}, {3, 4}] + Q[{5, 6}, {1, 2}, {3, 4}] - Q[{5, 6}, {1, 2, 3, 4}]
                sage: Phi = WQSym.Phi()
                sage: Phi[[2], [1,3]].coalgebraic_complement()
                -Phi[{2}, {1}, {3}] + Phi[{2}, {1, 3}] + Phi[{2}, {3}, {1}]

            The coalgebraic complement involution intertwines the antipode
            and the inverse of the antipode::

                sage: all( M(I).antipode().coalgebraic_complement().antipode()  # long time
                ....:      == M(I).coalgebraic_complement()
                ....:      for I in OrderedSetPartitions(4) )
                True

            Testing the `\\pi(f^r) = \\pi(f)` relation above::

                sage: all( M[I].coalgebraic_complement().to_quasisymmetric_function()
                ....:      == M[I].to_quasisymmetric_function()
                ....:      for I in OrderedSetPartitions(4) )
                True

            .. TODO::

                Check further commutative squares.
            """
        def star_involution(self):
            """
            Return the image of the element ``self`` of `WQSym`
            under the star involution.

            The star involution is the composition of the
            algebraic complement involution
            (:meth:`algebraic_complement`) with the coalgebraic
            complement involution (:meth:`coalgebraic_complement`).
            The composition can be performed in either order, as the
            involutions commute.

            The star involution is a graded Hopf algebra
            anti-automorphism of `WQSym`.
            Let `f^{\\ast}` denote the image of an element
            `f \\in WQSym` under the star involution.
            Let `\\mathbf{M}`, `X`, `Q` and `\\Phi` stand for the
            monomial, characteristic, Q and Phi bases of `WQSym`.
            For any ordered set partition `A` of `[n]`, we let
            `A^{\\ast}` denote the complement
            (:meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.complement`)
            of the reversal
            (:meth:`~sage.combinat.set_partition_ordered.OrderedSetPartition.reversed`)
            of `A`. Then, for any ordered set partition `A` of `[n]`,
            we have

            .. MATH::

                (\\mathbf{M}_A)^{\\ast} = \\mathbf{M}_{A^{\\ast}}, \\qquad
                (X_A)^{\\ast} = X_{A^{\\ast}}, \\qquad
                (Q_A)^{\\ast} = Q_{A^{\\ast}}, \\qquad
                (\\Phi_A)^{\\ast} = \\Phi_{A^{\\ast}} .

            The star involution
            (:meth:`~sage.combinat.ncsf_qsym.ncsf.NonCommutativeSymmetricFunctions.Bases.ElementMethods.star_involution`)
            on the ring of noncommutative symmetric functions is a
            restriction of the star involution on `WQSym`.

            If we denote the star involution
            (:meth:`~sage.combinat.ncsf_qsym.qsym.QuasiSymmetricFunctions.Bases.ElementMethods.star_involution`)
            of the quasisymmetric functions by `f \\mapsto f^{\\ast}`,
            and if we let `\\pi` be the canonical projection
            `WQSym \\to QSym`, then each `f \\in WQSym` satisfies
            `\\pi(f^{\\ast}) = (\\pi(f))^{\\ast}`.

            .. TODO::

                More commutative diagrams?
                FQSym and FSym need their own star_involution
                methods defined first.

            .. SEEALSO::

                :meth:`algebraic_complement`, :meth:`coalgebraic_complement`

            EXAMPLES:

            Keep in mind that the default input method for basis keys
            of `WQSym` is by entering an ordered set partition, not a
            packed word. Let us check the basis formulas for the
            star involution::

                sage: WQSym = algebras.WQSym(ZZ)
                sage: M = WQSym.M()
                sage: M[[1,3], [2,4,5]].star_involution()
                M[{1, 2, 4}, {3, 5}]
                sage: M[[1,3],[2]].star_involution()
                M[{2}, {1, 3}]
                sage: M[[1,4],[2,5],[3,6]].star_involution()
                M[{1, 4}, {2, 5}, {3, 6}]
                sage: (3*M[[1]] - 4*M[[]] + 5*M[[1],[2]]).star_involution()
                -4*M[] + 3*M[{1}] + 5*M[{1}, {2}]
                sage: X = WQSym.X()
                sage: X[[1,3],[2]].star_involution()
                X[{2}, {1, 3}]
                sage: C = WQSym.C()
                sage: C[[1,3],[2]].star_involution()
                -C[{1, 2, 3}] - C[{1, 3}, {2}] + C[{2}, {1, 3}]
                sage: Q = WQSym.Q()
                sage: Q[[1,3], [2,4,5]].star_involution()
                Q[{1, 2, 4}, {3, 5}]
                sage: Phi = WQSym.Phi()
                sage: Phi[[1,3], [2,4,5]].star_involution()
                Phi[{1, 2, 4}, {3, 5}]

            Testing the formulas for `(Q_A)^{\\ast}` and `(\\Phi_A)^{\\ast}`::

                sage: all(Q[A].star_involution() == Q[A.complement().reversed()] for A in OrderedSetPartitions(4))
                True
                sage: all(Phi[A].star_involution() == Phi[A.complement().reversed()] for A in OrderedSetPartitions(4))
                True

            The star involution commutes with the antipode::

                sage: all( M(I).antipode().star_involution()  # long time
                ....:      == M(I).star_involution().antipode()
                ....:      for I in OrderedSetPartitions(4) )
                True

            Testing the `\\pi(f^{\\ast}) = (\\pi(f))^{\\ast}` relation::

                sage: all( M[I].star_involution().to_quasisymmetric_function()
                ....:      == M[I].to_quasisymmetric_function().star_involution()
                ....:      for I in OrderedSetPartitions(4) )
                True

            Testing the fact that the star involution on the
            noncommutative symmetric functions is a restriction of
            the star involution on `WQSym`::

                sage: NCSF = NonCommutativeSymmetricFunctions(QQ)
                sage: R = NCSF.R()
                sage: all(R[I].star_involution().to_fqsym().to_wqsym()
                ....:     == R[I].to_fqsym().to_wqsym().star_involution()
                ....:     for I in Compositions(4))
                True

            .. TODO::

                Check further commutative squares.
            """
        def to_quasisymmetric_function(self):
            """
            The projection of ``self`` to the ring `QSym` of
            quasisymmetric functions.

            There is a canonical projection `\\pi : WQSym \\to QSym`
            that sends every element `\\mathbf{M}_P` of the monomial
            basis of `WQSym` to the monomial quasisymmetric function
            `M_c`, where `c` is the composition whose parts are the
            sizes of the blocks of `P`.
            This `\\pi` is a ring homomorphism.

            OUTPUT: an element of the quasisymmetric functions in the monomial basis

            EXAMPLES::

                sage: M = algebras.WQSym(QQ).M()
                sage: M[[1,3],[2]].to_quasisymmetric_function()
                M[2, 1]
                sage: (M[[1,3],[2]] + 3*M[[2,3],[1]] - M[[1,2,3],]).to_quasisymmetric_function()
                4*M[2, 1] - M[3]
                sage: X, Y = M[[1,3],[2]], M[[1,2,3],]
                sage: X.to_quasisymmetric_function() * Y.to_quasisymmetric_function() == (X*Y).to_quasisymmetric_function()
                True

                sage: C = algebras.WQSym(QQ).C()
                sage: C[[2,3],[1,4]].to_quasisymmetric_function() == M(C[[2,3],[1,4]]).to_quasisymmetric_function()
                True

                sage: C2 = algebras.WQSym(GF(2)).C()
                sage: C2[[1,2],[3,4]].to_quasisymmetric_function()
                M[2, 2]
                sage: C2[[2,3],[1,4]].to_quasisymmetric_function()
                M[4]
            """
