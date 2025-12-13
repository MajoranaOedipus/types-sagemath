from sage.categories.graded_hopf_algebras_with_basis import GradedHopfAlgebrasWithBasis as GradedHopfAlgebrasWithBasis
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.words.alphabet import Alphabet as Alphabet
from sage.combinat.words.finite_word import FiniteWord_class as FiniteWord_class
from sage.combinat.words.words import Words as Words
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family

class ShuffleAlgebra(CombinatorialFreeModule):
    """
    The shuffle algebra on some generators over a base ring.

    Shuffle algebras are commutative and associative algebras, with a
    basis indexed by words. The product of two words `w_1 \\cdot w_2` is given
    by the sum over the shuffle product of `w_1` and `w_2`.

    .. SEEALSO::

        For more on shuffle products, see
        :mod:`~sage.combinat.words.shuffle_product` and
        :meth:`~sage.combinat.words.finite_word.FiniteWord_class.shuffle()`.

    REFERENCES:

    - :wikipedia:`Shuffle algebra`

    INPUT:

    - ``R`` -- ring

    - ``names`` -- generator names (string or an alphabet)

    EXAMPLES::

        sage: F = ShuffleAlgebra(QQ, 'xyz'); F
        Shuffle Algebra on 3 generators ['x', 'y', 'z'] over Rational Field

        sage: mul(F.gens())
        B[xyz] + B[xzy] + B[yxz] + B[yzx] + B[zxy] + B[zyx]

        sage: mul([ F.gen(i) for i in range(2) ]) + mul([ F.gen(i+1) for i in range(2) ])
        B[xy] + B[yx] + B[yz] + B[zy]

        sage: S = ShuffleAlgebra(ZZ, 'abcabc'); S
        Shuffle Algebra on 3 generators ['a', 'b', 'c'] over Integer Ring
        sage: S.base_ring()
        Integer Ring

        sage: G = ShuffleAlgebra(S, 'mn'); G
        Shuffle Algebra on 2 generators ['m', 'n'] over Shuffle Algebra on 3 generators ['a', 'b', 'c'] over Integer Ring
        sage: G.base_ring()
        Shuffle Algebra on 3 generators ['a', 'b', 'c'] over Integer Ring

    Shuffle algebras commute with their base ring::

        sage: K = ShuffleAlgebra(QQ,'ab')
        sage: a,b = K.gens()
        sage: K.is_commutative()
        True
        sage: L = ShuffleAlgebra(K,'cd')
        sage: c,d = L.gens()
        sage: L.is_commutative()
        True
        sage: s = a*b^2 * c^3; s
        (12*B[abb]+12*B[bab]+12*B[bba])*B[ccc]
        sage: parent(s)
        Shuffle Algebra on 2 generators ['c', 'd'] over Shuffle Algebra on 2 generators ['a', 'b'] over Rational Field
        sage: c^3 * a * b^2
        (12*B[abb]+12*B[bab]+12*B[bba])*B[ccc]

    Shuffle algebras are commutative::

        sage: c^3 * b * a * b == c * a * c * b^2 * c
        True

    We can also manipulate elements in the basis and coerce elements from our
    base field::

        sage: F = ShuffleAlgebra(QQ, 'abc')
        sage: B = F.basis()
        sage: B[Word('bb')] * B[Word('ca')]
        B[bbca] + B[bcab] + B[bcba] + B[cabb]
         + B[cbab] + B[cbba]
        sage: 1 - B[Word('bb')] * B[Word('ca')] / 2
        B[] - 1/2*B[bbca] - 1/2*B[bcab] - 1/2*B[bcba]
         - 1/2*B[cabb] - 1/2*B[cbab] - 1/2*B[cbba]

    TESTS::

        sage: R = ShuffleAlgebra(QQ,'x')
        sage: R.is_commutative()
        True
        sage: R = ShuffleAlgebra(QQ,'xy')
        sage: R.is_commutative()
        True

    Check for a fix when using numbers as generators::

        sage: A = algebras.Shuffle(QQ,[0,1])
        sage: A_d = A.dual_pbw_basis()
        sage: W = A.basis().keys()
        sage: x = A(W([0,1,0]))
        sage: A_d(x)
        -2*S[001] + S[010]
    """
    @staticmethod
    def __classcall_private__(cls, R, names, prefix=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: F1 = ShuffleAlgebra(QQ, 'xyz')
            sage: F2 = ShuffleAlgebra(QQ, ['x','y','z'])
            sage: F3 = ShuffleAlgebra(QQ, Alphabet('xyz'))
            sage: F1 is F2 and F1 is F3
            True
        """
    def __init__(self, R, names, prefix) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: F = ShuffleAlgebra(QQ, 'xyz'); F
            Shuffle Algebra on 3 generators ['x', 'y', 'z'] over Rational Field
            sage: TestSuite(F).run()  # long time

        TESTS::

            sage: ShuffleAlgebra(24, 'toto')
            Traceback (most recent call last):
            ...
            TypeError: argument R must be a ring

            sage: F = ShuffleAlgebra(QQ, 'xyz', prefix='f'); F
            Shuffle Algebra on 3 generators ['x', 'y', 'z'] over Rational Field
            sage: F.gens()
            Family (f[x], f[y], f[z])
        """
    def variable_names(self):
        """
        Return the names of the variables.

        EXAMPLES::

            sage: R = ShuffleAlgebra(QQ,'xy')
            sage: R.variable_names()
            {'x', 'y'}
        """
    @cached_method
    def one_basis(self):
        """
        Return the empty word, which index of `1` of this algebra,
        as per :meth:`AlgebrasWithBasis.ParentMethods.one_basis`.

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ,'a')
            sage: A.one_basis()
            word:
            sage: A.one()
            B[]
        """
    def product_on_basis(self, w1, w2):
        '''
        Return the product of basis elements ``w1`` and ``w2``, as per
        :meth:`AlgebrasWithBasis.ParentMethods.product_on_basis()`.

        INPUT:

        - ``w1``, ``w2`` -- basis elements

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ,\'abc\')
            sage: W = A.basis().keys()
            sage: A.product_on_basis(W("acb"), W("cba"))
            B[acbacb] + B[acbcab] + 2*B[acbcba]
             + 2*B[accbab] + 4*B[accbba] + B[cabacb]
             + B[cabcab] + B[cabcba] + B[cacbab]
             + 2*B[cacbba] + 2*B[cbaacb] + B[cbacab]
             + B[cbacba]

            sage: (a,b,c) = A.algebra_generators()
            sage: a * (1-b)^2 * c
            2*B[abbc] - 2*B[abc] + 2*B[abcb] + B[ac]
             - 2*B[acb] + 2*B[acbb] + 2*B[babc]
             - 2*B[bac] + 2*B[bacb] + 2*B[bbac]
             + 2*B[bbca] - 2*B[bca] + 2*B[bcab]
             + 2*B[bcba] + B[ca] - 2*B[cab] + 2*B[cabb]
             - 2*B[cba] + 2*B[cbab] + 2*B[cbba]
        '''
    def antipode_on_basis(self, w):
        '''
        Return the antipode on the basis element ``w``.

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ,\'abc\')
            sage: W = A.basis().keys()
            sage: A.antipode_on_basis(W("acb"))
            -B[bca]
        '''
    def gen(self, i):
        """
        Return the ``i``-th generator of the algebra.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: F = ShuffleAlgebra(ZZ,'xyz')
            sage: F.gen(0)
            B[x]

            sage: F.gen(4)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 4) must be between 0 and 2
        """
    def some_elements(self):
        """
        Return some typical elements.

        EXAMPLES::

            sage: F = ShuffleAlgebra(ZZ,'xyz')
            sage: F.some_elements()
            [0, B[], B[x], B[y], B[z], B[xz] + B[zx]]
        """
    def coproduct_on_basis(self, w):
        """
        Return the coproduct of the element of the basis indexed by
        the word ``w``.

        The coproduct is given by deconcatenation.

        INPUT:

        - ``w`` -- a word

        EXAMPLES::

            sage: F = ShuffleAlgebra(QQ,'ab')
            sage: F.coproduct_on_basis(Word('a'))
            B[] # B[a] + B[a] # B[]
            sage: F.coproduct_on_basis(Word('aba'))
            B[] # B[aba] + B[a] # B[ba]
             + B[ab] # B[a] + B[aba] # B[]
            sage: F.coproduct_on_basis(Word())
            B[] # B[]

        TESTS::

            sage: F = ShuffleAlgebra(QQ,'ab')
            sage: S = F.an_element(); S
            B[] + 2*B[a] + 3*B[b] + B[bab]
            sage: F.coproduct(S)
            B[] # B[] + 2*B[] # B[a]
             + 3*B[] # B[b] + B[] # B[bab]
             + 2*B[a] # B[] + 3*B[b] # B[]
             + B[b] # B[ab] + B[ba] # B[b]
             + B[bab] # B[]
            sage: F.coproduct(F.one())
            B[] # B[]
        """
    def counit(self, S):
        """
        Return the counit of ``S``.

        EXAMPLES::

            sage: F = ShuffleAlgebra(QQ,'ab')
            sage: S = F.an_element(); S
            B[] + 2*B[a] + 3*B[b] + B[bab]
            sage: F.counit(S)
            1
        """
    def degree_on_basis(self, w):
        """
        Return the degree of the element ``w``.

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ, 'ab')
            sage: [A.degree_on_basis(x.leading_support()) for x in A.some_elements() if x != 0]
            [0, 1, 1, 2]
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the generators of this algebra.

        EXAMPLES::

            sage: A = ShuffleAlgebra(ZZ,'fgh'); A
            Shuffle Algebra on 3 generators ['f', 'g', 'h'] over Integer Ring
            sage: A.algebra_generators()
            Family (B[f], B[g], B[h])

            sage: A = ShuffleAlgebra(QQ, ['x1','x2'])
            sage: A.algebra_generators()
            Family (B[x1], B[x2])

        TESTS::

            sage: A = ShuffleAlgebra(ZZ,[0,1])
            sage: A.algebra_generators()
            Family (B[0], B[1])
        """
    gens = algebra_generators
    def dual_pbw_basis(self):
        """
        Return the dual PBW of ``self``.

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ, 'ab')
            sage: A.dual_pbw_basis()
            The dual Poincare-Birkhoff-Witt basis of Shuffle Algebra on 2 generators ['a', 'b'] over Rational Field
        """
    def to_dual_pbw_element(self, w):
        """
        Return the element `w` of ``self`` expressed in the dual PBW basis.

        INPUT:

        - ``w`` -- an element of the shuffle algebra

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ, 'ab')
            sage: f = 2 * A(Word()) + A(Word('ab')); f
            2*B[] + B[ab]
            sage: A.to_dual_pbw_element(f)
            2*S[] + S[ab]
            sage: A.to_dual_pbw_element(A.one())
            S[]
            sage: S = A.dual_pbw_basis()
            sage: elt = S.expansion_on_basis(Word('abba')); elt
            2*B[aabb] + B[abab] + B[abba]
            sage: A.to_dual_pbw_element(elt)
            S[abba]
            sage: A.to_dual_pbw_element(2*A(Word('aabb')) + A(Word('abab')))
            S[abab]
            sage: S.expansion(S('abab'))
            2*B[aabb] + B[abab]
        """

class DualPBWBasis(CombinatorialFreeModule):
    """
    The basis dual to the Poincaré-Birkhoff-Witt basis of the free algebra.

    We recursively define the dual PBW basis as the basis of the
    shuffle algebra given by

    .. MATH::

        S_w = \\begin{cases}
        w & |w| = 1, \\\\\n        x S_u & w = xu \\text{ and } w \\in \\mathrm{Lyn}(X), \\\\\n        \\displaystyle \\frac{S_{\\ell_{i_1}}^{\\ast \\alpha_1} \\ast \\cdots
        \\ast S_{\\ell_{i_k}}^{\\ast \\alpha_k}}{\\alpha_1! \\cdots \\alpha_k!} &
        w = \\ell_{i_1}^{\\alpha_1} \\cdots \\ell_{i_k}^{\\alpha_k} \\text{ with }
        \\ell_1 > \\cdots > \\ell_k \\in \\mathrm{Lyn}(X).
        \\end{cases}

    where `S \\ast T` denotes the shuffle product of `S` and `T` and
    `\\mathrm{Lyn}(X)` is the set of Lyndon words in the alphabet `X`.

    The definition may be found in Theorem 5.3 of [Reu1993]_.

    INPUT:

    - ``R`` -- ring

    - ``names`` -- names of the generators (string or an alphabet)

    EXAMPLES::

        sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
        sage: S
        The dual Poincare-Birkhoff-Witt basis of Shuffle Algebra on 2 generators ['a', 'b'] over Rational Field
        sage: S.one()
        S[]
        sage: S.one_basis()
        word:
        sage: T = ShuffleAlgebra(QQ, 'abcd').dual_pbw_basis(); T
        The dual Poincare-Birkhoff-Witt basis of Shuffle Algebra on 4 generators ['a', 'b', 'c', 'd'] over Rational Field
        sage: T.algebra_generators()
        (S[a], S[b], S[c], S[d])

    TESTS:

    We check conversion between the bases::

        sage: A = ShuffleAlgebra(QQ, 'ab')
        sage: S = A.dual_pbw_basis()
        sage: W = Words('ab', 5)
        sage: all(S(A(S(w))) == S(w) for w in W)
        True
        sage: all(A(S(A(w))) == A(w) for w in W)
        True
    """
    @staticmethod
    def __classcall_private__(cls, R, names):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.algebras.shuffle_algebra import DualPBWBasis
            sage: D1 = DualPBWBasis(QQ, 'ab')
            sage: D2 = DualPBWBasis(QQ, Alphabet('ab'))
            sage: D1 is D2
            True
        """
    def __init__(self, R, names) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: D = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: TestSuite(D).run()  # long time
        """
    def one_basis(self):
        """
        Return the indexing element of the basis element `1`.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: S.one_basis()
            word:
        """
    def counit(self, S):
        """
        Return the counit of ``S``.

        EXAMPLES::

            sage: F = ShuffleAlgebra(QQ,'ab').dual_pbw_basis()
            sage: (3*F.gen(0)+5*F.gen(1)**2).counit()
            0
            sage: (4*F.one()).counit()
            4
        """
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: S.algebra_generators()
            (S[a], S[b])
        """
    gens = algebra_generators
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: S.gen(0)
            S[a]
            sage: S.gen(1)
            S[b]
        """
    def some_elements(self):
        """
        Return some typical elements.

        EXAMPLES::

            sage: F = ShuffleAlgebra(QQ,'xyz').dual_pbw_basis()
            sage: F.some_elements()
            [0, S[], S[x], S[y], S[z], S[zx]]
        """
    def shuffle_algebra(self):
        """
        Return the associated shuffle algebra of ``self``.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: S.shuffle_algebra()
            Shuffle Algebra on 2 generators ['a', 'b'] over Rational Field
        """
    def product(self, u, v):
        """
        Return the product of two elements ``u`` and ``v``.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: a,b = S.gens()
            sage: S.product(a, b)
            S[ba]
            sage: S.product(b, a)
            S[ba]
            sage: S.product(b^2*a, a*b*a)
            36*S[bbbaaa]

        TESTS:

        Check that multiplication agrees with the multiplication in the
        shuffle algebra::

            sage: A = ShuffleAlgebra(QQ, 'ab')
            sage: S = A.dual_pbw_basis()
            sage: a,b = S.gens()
            sage: A(a*b)
            B[ab] + B[ba]
            sage: A(a*b*a)
            2*B[aab] + 2*B[aba] + 2*B[baa]
            sage: S(A(a)*A(b)*A(a)) == a*b*a
            True
        """
    def antipode(self, elt):
        """
        Return the antipode of the element ``elt``.

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ, 'ab')
            sage: S = A.dual_pbw_basis()
            sage: w = S('abaab').antipode(); w
            S[abaab] - 2*S[ababa] - S[baaba]
             + 3*S[babaa] - 6*S[bbaaa]
            sage: w.antipode()
            S[abaab]
        """
    def coproduct(self, elt):
        """
        Return the coproduct of the element ``elt``.

        EXAMPLES::

            sage: A = ShuffleAlgebra(QQ, 'ab')
            sage: S = A.dual_pbw_basis()
            sage: S('ab').coproduct()
            S[] # S[ab] + S[a] # S[b]
             + S[ab] # S[]
            sage: S('ba').coproduct()
            S[] # S[ba] + S[a] # S[b]
             + S[b] # S[a] + S[ba] # S[]

        TESTS::

            sage: all(A.tensor_square()(S(x).coproduct()) == x.coproduct()
            ....:     for x in A.some_elements())
            True
            sage: all(S.tensor_square()(A(x).coproduct()) == x.coproduct()
            ....:     for x in S.some_elements())
            True
        """
    def degree_on_basis(self, w):
        """
        Return the degree of the element ``w``.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: [S.degree_on_basis(x.leading_support()) for x in S.some_elements() if x != 0]
            [0, 1, 1, 2]
        """
    @lazy_attribute
    def expansion(self):
        """
        Return the morphism corresponding to the expansion into words of
        the shuffle algebra.

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: f = S('ab') + S('aba')
            sage: S.expansion(f)
            2*B[aab] + B[ab] + B[aba]
        """
    @cached_method
    def expansion_on_basis(self, w):
        """
        Return the expansion of `S_w` in words of the shuffle algebra.

        INPUT:

        - ``w`` -- a word

        EXAMPLES::

            sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
            sage: S.expansion_on_basis(Word())
            B[]
            sage: S.expansion_on_basis(Word()).parent()
            Shuffle Algebra on 2 generators ['a', 'b'] over Rational Field
            sage: S.expansion_on_basis(Word('abba'))
            2*B[aabb] + B[abab] + B[abba]
            sage: S.expansion_on_basis(Word())
            B[]
            sage: S.expansion_on_basis(Word('abab'))
            2*B[aabb] + B[abab]
        """
    class Element(CombinatorialFreeModule.Element):
        """
        An element in the dual PBW basis.
        """
        def expand(self):
            """
            Expand ``self`` in words of the shuffle algebra.

            EXAMPLES::

                sage: S = ShuffleAlgebra(QQ, 'ab').dual_pbw_basis()
                sage: f = S('ab') + S('bab')
                sage: f.expand()
                B[ab] + 2*B[abb] + B[bab]
            """
