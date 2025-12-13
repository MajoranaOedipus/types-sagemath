from sage.categories.modules import Modules as Modules
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.family import AbstractFamily as AbstractFamily, Family as Family

class Representation_abstract:
    """
    Mixin class for (left) representations of Lie algebras.

    INPUT:

    - ``lie_algebra`` -- a Lie algebra
    """
    def __init__(self, lie_algebra) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sp(QQ, 6)
            sage: R = L.trivial_representation()
            sage: TestSuite(R).run()
        """
    def lie_algebra(self):
        """
        Return the Lie algebra whose representation ``self`` is.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 4)
            sage: R = L.trivial_representation()
            sage: R.lie_algebra() is L
            True
        """
    def side(self):
        """
        Return that ``self`` is a left representation.

        OUTPUT: the string ``'left'``

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 4)
            sage: R = L.trivial_representation()
            sage: R.side()
            'left'
        """
    def representation_matrix(self, elt):
        """
        Return the matrix for the action of ``elt`` on ``self``.

        EXAMPLES::

            sage: H1 = lie_algebras.Heisenberg(QQ, 1)
            sage: F = H1.faithful_representation(algorithm='minimal')
            sage: P1 = F.representation_matrix(H1.gen(0)); P1
            [0 0 0]
            [0 0 0]
            [1 0 0]
            sage: Q1 = F.representation_matrix(H1.gen(1)); Q1
            [ 0  0  0]
            [ 0  0 -1]
            [ 0  0  0]
            sage: Z = P1.commutator(Q1); Z
            [0 0 0]
            [1 0 0]
            [0 0 0]
            sage: P1.commutator(Z) == Q1.commutator(Z) == 0
            True
            sage: (H1.gen(0) * F.an_element()).to_vector()
            (0, 0, 2)
            sage: P1 * F.an_element().to_vector()
            (0, 0, 2)
            sage: (H1.gen(1) * F.an_element()).to_vector()
            (0, -3, 0)
            sage: Q1 * F.an_element().to_vector()
            (0, -3, 0)
            sage: (H1.basis()['z'] * F.an_element()).to_vector()
            (0, 2, 0)
            sage: Z * F.an_element().to_vector()
            (0, 2, 0)
        """

class RepresentationByMorphism(CombinatorialFreeModule, Representation_abstract):
    '''
    Representation of a Lie algebra defined by a Lie algebra morphism.

    INPUT:

    - ``lie_algebra`` -- a Lie algebra
    - ``f`` -- the Lie algebra morphism defining the action of the basis
      elements of ``lie_algebra``
    - ``index_set`` -- (optional) the index set of the module basis
    - ``on_basis`` -- boolean (default: ``False``); the function `f` defines a
      map from the basis elements or from a generic element of ``lie_algebra``

    If `f` is encoded as a ``dict`` or ``Family``, then the keys must
    be indices of the basis of ``lie_algebra`` and the values being the
    corresponding matrix defining the action. This sets ``on_basis=True``.

    EXAMPLES::

        sage: L.<x,y> = LieAlgebra(QQ, {(\'x\',\'y\'): {\'y\':1}})
        sage: f = {x: Matrix([[1,0],[0,0]]), y: Matrix([[0,1],[0,0]])}
        sage: L.representation(f)
        Representation of Lie algebra on 2 generators (x, y) over Rational Field defined by:
               [1 0]
        x |--> [0 0]
               [0 1]
        y |--> [0 0]

    We construct the direct sum of two copies of the trivial representation
    for an infinite dimensional Lie algebra::

        sage: L = lie_algebras.Affine(QQ, [\'E\',6,1])
        sage: R = L.representation(lambda b: matrix.zero(QQ, 2), index_set=[\'a\',\'b\'])
        sage: x = L.an_element()
        sage: v = R.an_element(); v
        2*R[\'a\'] + 2*R[\'b\']
        sage: x * v
        0

    We construct a finite dimensional representation of the affline Lie algebra
    of type `A_2^{(1)}`::

        sage: L = lie_algebras.Affine(QQ, [\'A\',2,1]).derived_subalgebra()
        sage: Phi_plus = list(RootSystem([\'A\',2]).root_lattice().positive_roots())
        sage: def aff_action(key):
        ....:     mat = matrix.zero(QQ, 3)
        ....:     if key == \'c\':  # central element
        ....:         return mat
        ....:     b, ell = key
        ....:     if b in Phi_plus:  # positive root
        ....:         ind = tuple(sorted(b.to_ambient().support()))
        ....:         mat[ind] = 1
        ....:         if ind[0] + 1 != ind[1]:
        ....:             mat[ind] = -1
        ....:     elif -b in Phi_plus:  # negative root
        ....:         ind = tuple(sorted(b.to_ambient().support(), reverse=True))
        ....:         mat[ind] = 1
        ....:         if ind[0] - 1 != ind[1]:
        ....:             mat[ind] = -1
        ....:     else:  # must be in the Cartan
        ....:         i = b.leading_support()
        ....:         mat[i,i] = -1
        ....:         mat[i-1,i-1] = 1
        ....:     return mat
        sage: F = Family(L.basis(), aff_action, name="lifted natural repr")
        sage: R = L.representation(index_set=range(1,4), on_basis=F)
        sage: x = L.an_element(); x
        (E[alpha[2]] + E[alpha[1]] + h1 + h2 + E[-alpha[2]] + E[-alpha[1]])#t^0
         + (E[-alpha[1] - alpha[2]])#t^1 + (E[alpha[1] + alpha[2]])#t^-1 + c
        sage: v = R.an_element(); v
        2*R[1] + 2*R[2] + 3*R[3]
        sage: x * v
        R[1] + 5*R[2] - 3*R[3]
        sage: R._test_representation()  # verify that it is a representation
    '''
    @staticmethod
    def __classcall_private__(cls, lie_algebra, f=None, index_set=None, on_basis: bool = False, **kwargs):
        """
        Normalize inpute to ensure a unique representation.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'y':1}})
            sage: f1 = {'x': Matrix([[1,0],[0,0]]), 'y': Matrix([[0,1],[0,0]])}
            sage: R1 = L.representation(f1)
            sage: f2 = Family({x: Matrix([[1,0],[0,0]]), y: Matrix(QQ, [[0,1],[0,0]])})
            sage: R2 = L.representation(f2)
            sage: R1 is R2
            True

        TESTS::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'y':1}})
            sage: f = {'x': Matrix([[1,0]]), 'y': Matrix([[0,1]])}
            sage: L.representation(f)
            Traceback (most recent call last):
            ...
            ValueError: all matrices must be square

            sage: f = {'x': Matrix([[1,0],[0,0]]), 'y': Matrix([[0]])}
            sage: L.representation(f)
            Traceback (most recent call last):
            ...
            ValueError: all matrices must be square of size 2

            sage: L.representation(index_set=[1,2,3])
            Traceback (most recent call last):
            ...
            ValueError: either 'f' or 'on_basis' must be specified
            sage: L.representation(on_basis=lambda x: QQ.zero())
            Traceback (most recent call last):
            ...
            ValueError: the index set needs to be specified
        """
    def __init__(self, lie_algebra, f, index_set, on_basis, category, **kwargs) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'y':1}})
            sage: f = {'x': Matrix([[1,0],[0,0]]), 'y': Matrix([[0,1],[0,0]])}
            sage: R = L.representation(f)
            sage: TestSuite(R).run()
        """
    class Element(CombinatorialFreeModule.Element): ...

class TrivialRepresentation(CombinatorialFreeModule, Representation_abstract):
    """
    The trivial representation of a Lie algebra.

    The trivial representation of a Lie algebra `L` over a commutative ring
    `R` is the `1`-dimensional `R`-module on which every element of `L`
    acts by zero.

    INPUT:

    - ``lie_algebra`` -- a Lie algebra

    REFERENCES:

    - :wikipedia:`Trivial_representation`
    """
    def __init__(self, lie_algebra, **kwargs) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: R = L.trivial_representation()
            sage: TestSuite(R).run()
        """
    class Element(CombinatorialFreeModule.Element): ...

class FaithfulRepresentationNilpotentPBW(CombinatorialFreeModule, Representation_abstract):
    """
    Return a faithful representation of a nilpotent Lie algebra
    constructed using the PBW basis.

    Let `L` be a `k`-step nilpotent Lie algebra. Define a weight function
    on elements in `L` by the lower central series of `L`. Then a faithful
    representation of `L` is `U(L) / U(L)^{k+1}`, where `U(L)^{k+1}`
    is the (twosided) ideal of `U(L)` generated by all monomials
    of weight at least `k + 1`.

    We can also expand the ideal keeping the property that `I \\cap Z(L) = 0`.
    The resulting quotient `U(L) / I` remains faithful and is a minimal
    faithful representation of `L` in the sense that it has no faithful
    submodules or quotients. (Note: this is not necessarily the smallest
    dimensional faithful representation of `L`.)

    We consider an example of the rank 2 Heisenberg Lie algebra,
    but with a non-standard basis given by `a = p_1 + z`, `b = q_1`,
    and `c = q_1 + z`::

        sage: scoeffs = {('a','b'): {'b':-1, 'c':1}, ('a','c'): {'b':-1, 'c':1}}
        sage: L.<a,b,c> = LieAlgebra(QQ, scoeffs)
        sage: TestSuite(L).run(elements=list(L.basis()))
        sage: L.is_nilpotent()
        True
        sage: L.derived_series()
        (Lie algebra on 3 generators (a, b, c) over Rational Field,
         Ideal (b - c) of Lie algebra on 3 generators (a, b, c) over Rational Field,
         Ideal () of Lie algebra on 3 generators (a, b, c) over Rational Field)
        sage: F = L.faithful_representation()
        sage: L.an_element() * F.an_element()
        2*F[1, 0, 0] + 8*F[1, 1, 0] + 3*F[2, 0, 0] + 4*F[0, 1, 0]
         + 4*F[0, 2, 0] + 4*F[0, 0, 1]

        sage: MF = L.faithful_representation(algorithm='minimal')
        sage: MF.dimension()
        3
        sage: [MF.representation_matrix(be) for be in L.basis()]
        [
        [0 0 0]  [ 0  0  0]  [ 0  0  0]
        [0 0 0]  [ 0  0 -1]  [ 1  0 -1]
        [1 0 0], [ 0  0  0], [ 0  0  0]
        ]

    An example with ``minimal=True`` for `H_2 \\oplus A_1`, where `A_1` is
    a `1`-dimensional Abelian Lie algebra::

        sage: scoeffs = {('a','b'): {'b':-1, 'c':1}, ('a','c'): {'b':-1, 'c':1}}
        sage: L.<a,b,c,d> = LieAlgebra(QQ, scoeffs)
        sage: F = L.faithful_representation(); F
        Faithful 11 dimensional representation of Lie algebra on 4
         generators (a, b, c, d) over Rational Field
        sage: MF = L.faithful_representation(algorithm='minimal'); MF
        Minimal faithful representation of Lie algebra on 4
         generators (a, b, c, d) over Rational Field
        sage: MF.dimension()
        4

    INPUT:

    - ``minimal`` -- boolean (default: ``False``); whether to construct
      the minimal basis or not

    REFERENCES:

    - [BEdG2009]_
    """
    def __init__(self, L, minimal: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: H2 = lie_algebras.Heisenberg(QQ, 2)
            sage: F = H2.faithful_representation()
            sage: TestSuite(F).run(elements=list(F.basis()))
            sage: MF = H2.faithful_representation(algorithm='minimal')
            sage: TestSuite(MF).run(elements=list(MF.basis()))

            sage: sc = {('a','b'): {'b':-1, 'c':1}, ('a','c'): {'b':-1, 'c':1}}
            sage: L.<a,b,c> = LieAlgebra(QQ, sc)
            sage: F = L.faithful_representation()
            sage: TestSuite(F).run(elements=list(F.basis()))
            sage: MF = L.faithful_representation(algorithm='minimal')
            sage: TestSuite(MF).run(elements=list(MF.basis()))
        """
    class Element(CombinatorialFreeModule.Element): ...

class FaithfulRepresentationPBWPosChar(CombinatorialFreeModule, Representation_abstract):
    """
    A faithful representation of a finite dimensional Lie algebra
    in positive characteristic.

    .. WARNING::

        This is often a very large dimensional representation relative
        to the dimension of the Lie algebra.

    ALGORITHM:

    We implement the algorithm given in [deG2000] Section 6.6. Let `L`
    be a finite dimensional Lie algebra over a ring of characteristic `p`
    with basis `(b_1, \\ldots, b_n)`. We compute (monic) `p`-polynomials
    `f_i` such that `A = \\mathrm{ad}(b_i)` (the adjoint action of `b_i`)
    solves `f_i(A) = 0` by using minimal polynomial of `A`. The
    `(f_1, \\ldots, f_n)` is a Gröbner basis for an ideal `I` of the
    universal enveloping algebra `U(L)` such that the quotient `U(L) / I`
    is a faithful representation of `L`.

    EXAMPLES::

        sage: sl2 = LieAlgebra(GF(3), cartan_type=['A',1])
        sage: F = sl2.faithful_representation()
        sage: F
        Faithful representation with p-multiplicities (1, 3, 1) of Lie algebra
         of ['A', 1] in the Chevalley basis
        sage: F.dimension()
        243
    """
    def __init__(self, L) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: sl2 = LieAlgebra(GF(3), cartan_type=['A',1])
            sage: F = sl2.faithful_representation()
            sage: TestSuite(F).run()
        """
    @cached_method
    def p_exponents(self):
        """
        Return the `p`-exponents of ``self``.

        Let `p` be the characteristic of the base ring of ``self``.
        The `p`-*exponents* are the exponents `m_i` such that the `i`-th
        `p`-polynomial `f_i` is of degree `p^{m_i}`.

        EXAMPLES::

            sage: sp4 = LieAlgebra(GF(3), cartan_type=['C',2])
            sage: F = sp4.faithful_representation()
            sage: F.p_exponents()
            (1, 1, 1, 1, 3, 3, 1, 1, 1, 1)
        """
    def groebner_basis(self):
        """
        Return the defining Gröbner basis of ``self``.

        EXAMPLES::

            sage: sp4 = LieAlgebra(GF(3), cartan_type=['C',2])
            sage: F = sp4.faithful_representation()
            sage: F.groebner_basis()
            [PBW[alpha[2]]^3,
             PBW[alpha[1]]^3,
             PBW[alpha[1] + alpha[2]]^3,
             PBW[2*alpha[1] + alpha[2]]^3,
             2*PBW[alphacheck[1]]^27 + PBW[alphacheck[1]],
             2*PBW[alphacheck[2]]^27 + PBW[alphacheck[2]],
             PBW[-alpha[2]]^3,
             PBW[-alpha[1]]^3,
             PBW[-alpha[1] - alpha[2]]^3,
             PBW[-2*alpha[1] - alpha[2]]^3]
        """
    class Element(CombinatorialFreeModule.Element): ...
