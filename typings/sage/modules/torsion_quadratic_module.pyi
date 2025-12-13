from _typeshed import Incomplete
from sage.arith.misc import gcd as gcd, legendre_symbol as legendre_symbol
from sage.groups.additive_abelian.qmodnz import QmodnZ as QmodnZ
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import diagonal_matrix as diagonal_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.fg_pid.fgp_element import FGP_Element as FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class as FGP_Module_class
from sage.modules.free_quadratic_module import FreeQuadraticModule as FreeQuadraticModule
from sage.rings.finite_rings.integer_mod import mod as mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation

def TorsionQuadraticForm(q):
    """
    Create a torsion quadratic form module from a rational matrix.

    The resulting quadratic form takes values in `\\QQ / \\ZZ`
    or `\\QQ / 2 \\ZZ` (depending on ``q``).
    If it takes values modulo `2`, then it is non-degenerate.
    In any case the bilinear form is non-degenerate.

    INPUT:

    - ``q`` -- a symmetric rational matrix

    EXAMPLES::

        sage: q1 = Matrix(QQ, 2, [1,1/2,1/2,1])
        sage: TorsionQuadraticForm(q1)
        Finite quadratic module over Integer Ring with invariants (2, 2)
        Gram matrix of the quadratic form with values in Q/2Z:
        [  1 1/2]
        [1/2   1]

    In the following example the quadratic form is degenerate.
    But the bilinear form is still non-degenerate::

        sage: q2 = diagonal_matrix(QQ, [1/4,1/3])
        sage: TorsionQuadraticForm(q2)
        Finite quadratic module over Integer Ring with invariants (12,)
        Gram matrix of the quadratic form with values in Q/Z:
        [7/12]

    TESTS::

        sage: TorsionQuadraticForm(matrix.diagonal([3/4,3/8,3/8]))
        Finite quadratic module over Integer Ring with invariants (4, 8, 8)
        Gram matrix of the quadratic form with values in Q/2Z:
        [3/4   0   0]
        [  0 3/8   0]
        [  0   0 3/8]
    """

class TorsionQuadraticModuleElement(FGP_Element):
    """
    An element of a torsion quadratic module.

    INPUT:

    - ``parent`` -- parent

    - ``x`` -- element of ``parent.V()``

    - ``check`` -- boolean (default: ``True``)

    TESTS::

        sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
        sage: T = TorsionQuadraticModule(ZZ^3, 6*ZZ^3)
        sage: loads(dumps(T)) == T
        True
        sage: t = T.gen(0)
        sage: loads(dumps(t)) == t
        True

        sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
        sage: V = span([[1/2,1,1], [3/2,2,1], [0,0,1]], ZZ)
        sage: b = V.basis()
        sage: W = V.span([2*b[0] + 4*b[1], 9*b[0] + 12*b[1], 4*b[2]])
        sage: Q = TorsionQuadraticModule(V, W)
        sage: x = Q(b[0] - b[1])
        sage: TestSuite(x).run()
    """
    inner_product: Incomplete
    b: Incomplete
    def quadratic_product(self):
        """
        Compute the quadratic product of ``self``.

        OUTPUT:

        - an element of `\\QQ / n\\ZZ` where `n\\ZZ = 2(V,W) +
          \\ZZ \\{ (w,w) | w \\in W \\}`

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: W = FreeQuadraticModule(ZZ, 2, 2*matrix.identity(2))
            sage: V = (1/2) * W
            sage: T = TorsionQuadraticModule(V, W)
            sage: x = T.gen(0)
            sage: x
            (1, 0)
            sage: x.quadratic_product()
            1/2
            sage: x.quadratic_product().parent()
            Q/2Z
            sage: x*x
            1/2
            sage: (x*x).parent()
            Q/Z
        """
    q = quadratic_product

class TorsionQuadraticModule(FGP_Module_class, CachedRepresentation):
    """
    Finite quotients with a bilinear and a quadratic form.

    Let `V` be a symmetric :class:`FreeQuadraticModule` and `W \\subseteq V` a
    submodule of the same rank as `V`. The quotient `V / W` is a torsion
    quadratic module. It inherits a bilinear form `b` and a quadratic
    form `q`.

    `b: V \\times V \\to \\QQ / m\\ZZ`, where  `m\\ZZ = (V,W)`
    and `b(x,y) = (x,y) + m\\ZZ`

    `q: V \\to \\QQ / n\\ZZ`, where `n\\ZZ = 2(V,W) + \\ZZ \\{ (w,w) | w \\in W \\}`

    INPUT:

    - ``V`` -- a :class:`FreeModule` with a symmetric inner product matrix

    - ``W`` -- a submodule of ``V`` of the same rank as ``V``

    - ``check`` -- boolean (default: ``True``)

    - ``modulus`` -- a rational number dividing `m` (default: `m`);
      the inner product `b` is defined in `\\QQ /` ``modulus`` `\\ZZ`

    - ``modulus_qf`` -- a rational number dividing `n` (default: `n`);
      the quadratic form `q` is defined in `\\QQ /` ``modulus_qf`` `\\ZZ`

    EXAMPLES::

        sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
        sage: V = FreeModule(ZZ, 3)
        sage: T = TorsionQuadraticModule(V, 5*V); T
        Finite quadratic module over Integer Ring with invariants (5, 5, 5)
        Gram matrix of the quadratic form with values in Q/5Z:
        [1 0 0]
        [0 1 0]
        [0 0 1]
    """
    Element = TorsionQuadraticModuleElement
    @staticmethod
    def __classcall__(cls, V, W, gens=None, modulus=None, modulus_qf=None, check: bool = True):
        """
        Return a :class:`TorsionQuadraticModule`.

        This method does the preprocessing for :meth:`sage.structure.CachedRepresentation`.

        TESTS::

            sage: q = matrix([1/2])
            sage: D1 = TorsionQuadraticForm(q)
            sage: D2 = TorsionQuadraticForm(q)
            sage: D1 is D2
            True
        """
    def __init__(self, V, W, gens, modulus, modulus_qf) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: T = TorsionQuadraticModule(ZZ^3, 6*ZZ^3)
            sage: TestSuite(T).run()
        """
    def all_submodules(self):
        '''
        Return a list of all submodules of ``self``.

        .. WARNING::

            This method creates all submodules in memory. The number of submodules
            grows rapidly with the number of generators. For example consider a
            vector space of dimension `n` over a finite field of prime order `p`.
            The number of subspaces is (very) roughly `p^{(n^2-n)/2}`.

        EXAMPLES::

            sage: D = IntegralLattice("D4").discriminant_group()                        # needs sage.combinat
            sage: D.all_submodules()                                                    # needs sage.combinat
            [Finite quadratic module over Integer Ring with invariants ()
              Gram matrix of the quadratic form with values in Q/2Z:
              [],
             Finite quadratic module over Integer Ring with invariants (2,)
              Gram matrix of the quadratic form with values in Q/2Z:
              [1],
             Finite quadratic module over Integer Ring with invariants (2,)
              Gram matrix of the quadratic form with values in Q/2Z:
              [1],
             Finite quadratic module over Integer Ring with invariants (2,)
              Gram matrix of the quadratic form with values in Q/2Z:
              [1],
             Finite quadratic module over Integer Ring with invariants (2, 2)
              Gram matrix of the quadratic form with values in Q/2Z:
              [  1 1/2]
              [1/2   1]]
        '''
    @cached_method
    def brown_invariant(self):
        '''
        Return the Brown invariant of this torsion quadratic form.

        Let `(D,q)` be a torsion quadratic module with values in `\\QQ / 2 \\ZZ`.
        The Brown invariant `Br(D,q) \\in \\Zmod{8}` is defined by the equation

        .. MATH::

            \\exp \\left( \\frac{2 \\pi i }{8} Br(q)\\right) =
            \\frac{1}{\\sqrt{D}} \\sum_{x \\in D} \\exp(i \\pi q(x)).

        The Brown invariant is additive with respect to direct sums of
        torsion quadratic modules.

        OUTPUT: an element of `\\Zmod{8}`

        EXAMPLES::

            sage: L = IntegralLattice("D4")                                             # needs sage.combinat
            sage: D = L.discriminant_group()                                            # needs sage.combinat
            sage: D.brown_invariant()                                                   # needs sage.combinat
            4

        We require the quadratic form to be defined modulo `2 \\ZZ`::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: V = FreeQuadraticModule(ZZ, 3, matrix.identity(3))
            sage: T = TorsionQuadraticModule((1/10)*V, V)
            sage: T.brown_invariant()
            Traceback (most recent call last):
            ...
            ValueError: the torsion quadratic form must have values in QQ / 2 ZZ
        '''
    @cached_method
    def gram_matrix_bilinear(self):
        """
        Return the Gram matrix with respect to the generators.

        OUTPUT:

        A rational matrix ``G`` with ``G[i,j]`` given by the inner product
        of the `i`-th and `j`-th generator. Its entries are only well
        defined `\\mod (V, W)`.

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: V = FreeQuadraticModule(ZZ, 3, matrix.identity(3)*5)
            sage: T = TorsionQuadraticModule((1/5)*V, V)
            sage: T.gram_matrix_bilinear()
            [1/5   0   0]
            [  0 1/5   0]
            [  0   0 1/5]
        """
    @cached_method
    def gram_matrix_quadratic(self):
        """
        The Gram matrix of the quadratic form with respect to the generators.

        OUTPUT:

        - a rational matrix ``Gq`` with ``Gq[i,j] = gens[i]*gens[j]``
          and ``G[i,i] = gens[i].q()``

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: D4_gram = Matrix(ZZ, [[2,0,0,-1],[0,2,0,-1],[0,0,2,-1],[-1,-1,-1,2]])
            sage: D4 = FreeQuadraticModule(ZZ, 4, D4_gram)
            sage: D4dual = D4.span(D4_gram.inverse())
            sage: discrForm = TorsionQuadraticModule(D4dual, D4)
            sage: discrForm.gram_matrix_quadratic()
            [  1 1/2]
            [1/2   1]
            sage: discrForm.gram_matrix_bilinear()
            [  0 1/2]
            [1/2   0]
        """
    def gens(self) -> tuple:
        """
        Return generators of ``self``.

        There is no assumption on the generators except that they
        generate the module.

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: V = FreeModule(ZZ, 3)
            sage: T = TorsionQuadraticModule(V, 5*V)
            sage: T.gens()
            ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        """
    def genus(self, signature_pair):
        '''
        Return the genus defined by ``self`` and the ``signature_pair``.

        If no such genus exists, raise a :exc:`ValueError`.

        REFERENCES:

        [Nik1977]_ Corollary 1.9.4 and 1.16.3.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: L = IntegralLattice("D4").direct_sum(IntegralLattice("A2"))
            sage: D = L.discriminant_group()
            sage: genus = D.genus(L.signature_pair())                                   # needs sage.libs.pari
            sage: genus                                                                 # needs sage.libs.pari
            Genus of
            None
            Signature:  (6, 0)
            Genus symbol at 2:    1^4:2^-2
            Genus symbol at 3:     1^-5 3^-1
            sage: genus == L.genus()                                                    # needs sage.libs.pari
            True

        Let `H` be an even unimodular lattice of signature `(9, 1)`.
        Then `L = D_4 + A_2` is primitively embedded in `H`. We compute the discriminant
        form of the orthogonal complement of `L` in `H`::

            sage: DK = D.twist(-1)                                                      # needs sage.combinat sage.libs.pari
            sage: DK                                                                    # needs sage.combinat sage.libs.pari
            Finite quadratic module over Integer Ring with invariants (2, 6)
            Gram matrix of the quadratic form with values in Q/2Z:
            [  1 1/2]
            [1/2 1/3]

        We know that  `K` has signature `(5, 1)` and thus we can compute
        the genus of `K` as::

            sage: DK.genus((3,1))                                                       # needs sage.combinat sage.libs.pari
            Genus of
            None
            Signature:  (3, 1)
            Genus symbol at 2:    1^2:2^-2
            Genus symbol at 3:     1^-3 3^1

        We can also compute the genus of an odd lattice
        from its discriminant form::

            sage: L = IntegralLattice(matrix.diagonal(range(1, 5)))
            sage: D = L.discriminant_group()
            sage: D.genus((4,0))                                                        # needs sage.libs.pari
            Genus of
            None
            Signature:  (4, 0)
            Genus symbol at 2:    [1^-2 2^1 4^1]_6
            Genus symbol at 3:     1^-3 3^1

        TESTS::

            sage: L.genus() == D.genus((4,0))                                           # needs sage.libs.pari
            True
            sage: D.genus((1,0))                                                        # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: this discriminant form and signature do not define a genus

        A systematic test of lattices of small ranks and determinants::

            sage: # needs sage.libs.pari
            sage: from sage.quadratic_forms.genera.genus import genera
            sage: signatures = [(1,0), (1,1), (1,2), (3,0), (0,4)]
            sage: dets = range(1, 33)
            sage: genera = flatten([genera(s, d, even=False) for d in dets for s in signatures])  # long time
            sage: all(g == g.discriminant_form().genus(g.signature_pair()) for g in genera)  # long time
            True
        '''
    def is_genus(self, signature_pair, even: bool = True) -> bool:
        '''
        Return ``True`` if there is a lattice with this signature and discriminant form.

        .. TODO::

            implement the same for odd lattices

        INPUT:

        - ``signature_pair`` -- tuple of nonnegative integers ``(s_plus, s_minus)``
        - ``even`` -- boolean (default: ``True``)

        EXAMPLES::

            sage: L3 = IntegralLattice(3 * Matrix(ZZ, 2, [2,1,1,2]))
            sage: L = IntegralLattice("D4").direct_sum(L3)                              # needs sage.combinat
            sage: D = L.discriminant_group()                                            # needs sage.combinat
            sage: D.is_genus((6,0))                                                     # needs sage.combinat
            True

        Let us see if there is a lattice in the genus defined by the same discriminant form
        but with a different signature::

            sage: D.is_genus((4,2))                                                     # needs sage.combinat
            False
            sage: D.is_genus((16,2))                                                    # needs sage.combinat
            True
        '''
    def orthogonal_group(self, gens=None, check: bool = False):
        """
        Orthogonal group of the associated torsion quadratic form.

        .. WARNING::

            This is can be smaller than the orthogonal group of the bilinear form.

        INPUT:

        - ``gens`` -- a list of generators, for instance square matrices,
          something that acts on ``self``, or an automorphism
          of the underlying abelian group
        - ``check`` -- perform additional checks on the generators

        EXAMPLES:

        You can provide generators to obtain a subgroup of the full orthogonal group::

            sage: D = TorsionQuadraticForm(matrix.identity(2)/2)
            sage: f = matrix(2, [0,1,1,0])
            sage: D.orthogonal_group(gens=[f]).order()                                  # needs sage.groups
            2

        If no generators are given a slow brute force approach is used to calculate the full orthogonal group::

            sage: D = TorsionQuadraticForm(matrix.identity(3)/2)
            sage: OD = D.orthogonal_group()                                             # needs sage.groups
            sage: OD.order()                                                            # needs sage.groups
            6
            sage: fd = D.hom([D.1, D.0, D.2])                                           # needs sage.symbolic
            sage: OD(fd)                                                                # needs sage.groups sage.symbolic
            [0 1 0]
            [1 0 0]
            [0 0 1]

        We compute the kernel of the action of the orthogonal group of `L` on the discriminant group::

            sage: # needs sage.combinat sage.groups
            sage: L = IntegralLattice('A4')
            sage: O = L.orthogonal_group()
            sage: D = L.discriminant_group()
            sage: Obar = D.orthogonal_group(O.gens())
            sage: O.order()
            240
            sage: Obar.order()
            2
            sage: phi = O.hom(Obar.gens())
            sage: phi.kernel().order()
            120
        """
    def orthogonal_submodule_to(self, S):
        """
        Return the submodule orthogonal to ``S``.

        INPUT:

        - ``S`` -- a submodule, list, or tuple of generators

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: V = FreeModule(ZZ, 10)
            sage: T = TorsionQuadraticModule(V, 3*V)
            sage: S = T.submodule(T.gens()[:5])
            sage: O = T.orthogonal_submodule_to(S)
            sage: O
            Finite quadratic module over Integer Ring with invariants (3, 3, 3, 3, 3)
            Gram matrix of the quadratic form with values in Q/3Z:
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            sage: O.V() + S.V() == T.V()
            True
        """
    @cached_method
    def normal_form(self, partial: bool = False):
        """
        Return the normal form of this torsion quadratic module.

        Two torsion quadratic modules are isomorphic if and only if they have
        the same value modules and the same normal form.

        A torsion quadratic module `(T,q)` with values in `\\QQ/n\\ZZ` is
        in normal form if the rescaled quadratic module `(T, q/n)`
        with values in `\\QQ/\\ZZ` is in normal form.

        For the definition of normal form see [MirMor2009]_ IV Definition 4.6.
        Below are some of its properties.
        Let `p` be odd and `u` be the smallest non-square modulo `p`.
        The normal form is a diagonal matrix with diagonal entries either `p^n`
        or `u p^n`.

        If `p = 2` is even, then the normal form consists of
        `1 \\times 1` blocks of the form

        .. MATH::

            (0), \\quad 2^n(1),\\quad 2^n(3),\\quad 2^n(5) ,\\quad 2^n(7)

        or of `2 \\times 2` blocks of the form

        .. MATH::

            2^n
            \\left(\\begin{matrix}
                2 & 1\\\\\n                1 & 2
            \\end{matrix}\\right), \\quad
            2^n
            \\left(\\begin{matrix}
                0 & 1\\\\\n                1 & 0
            \\end{matrix}\\right).

        The blocks are ordered by their valuation.

        INPUT:

        - ``partial`` -- boolean (default: ``False``); return only a partial
          normal form. It is not unique but still useful to extract invariants.

        OUTPUT: a torsion quadratic module

        EXAMPLES::

            sage: L1 = IntegralLattice(matrix([[-2,0,0], [0,1,0], [0,0,4]]))
            sage: L1.discriminant_group().normal_form()                                 # needs sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (2, 4)
            Gram matrix of the quadratic form with values in Q/Z:
            [1/2   0]
            [  0 1/4]
            sage: L2 = IntegralLattice(matrix([[-2,0,0], [0,1,0], [0,0,-4]]))
            sage: L2.discriminant_group().normal_form()                                 # needs sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (2, 4)
            Gram matrix of the quadratic form with values in Q/Z:
            [1/2   0]
            [  0 1/4]

        We check that :issue:`24864` is fixed::

            sage: L1 = IntegralLattice(matrix([[-4,0,0], [0,4,0], [0,0,-2]]))
            sage: AL1 = L1.discriminant_group()
            sage: L2 = IntegralLattice(matrix([[-4,0,0], [0,-4,0], [0,0,2]]))
            sage: AL2 = L2.discriminant_group()
            sage: AL1.normal_form()                                                     # needs sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (2, 4, 4)
            Gram matrix of the quadratic form with values in Q/2Z:
            [1/2   0   0]
            [  0 1/4   0]
            [  0   0 5/4]
            sage: AL2.normal_form()                                                     # needs sage.libs.pari sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (2, 4, 4)
            Gram matrix of the quadratic form with values in Q/2Z:
            [1/2   0   0]
            [  0 1/4   0]
            [  0   0 5/4]

        Some exotic cases::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: D4_gram = Matrix(ZZ, 4, 4,[2,0,0,-1, 0,2,0,-1, 0,0,2,-1, -1,-1,-1,2])
            sage: D4 = FreeQuadraticModule(ZZ, 4, D4_gram)
            sage: D4dual = D4.span(D4_gram.inverse())
            sage: T = TorsionQuadraticModule((1/6)*D4dual, D4); T
            Finite quadratic module over Integer Ring with invariants (6, 6, 12, 12)
            Gram matrix of the quadratic form with values in Q/(1/3)Z:
            [ 1/18  1/12  5/36  1/36]
            [ 1/12   1/6  1/36   1/9]
            [ 5/36  1/36  1/36 11/72]
            [ 1/36   1/9 11/72  1/36]
            sage: T.normal_form()                                                       # needs sage.libs.pari sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (6, 6, 12, 12)
            Gram matrix of the quadratic form with values in Q/(1/3)Z:
            [ 1/6 1/12    0    0    0    0    0    0]
            [1/12  1/6    0    0    0    0    0    0]
            [   0    0 1/12 1/24    0    0    0    0]
            [   0    0 1/24 1/12    0    0    0    0]
            [   0    0    0    0  1/9    0    0    0]
            [   0    0    0    0    0  1/9    0    0]
            [   0    0    0    0    0    0  1/9    0]
            [   0    0    0    0    0    0    0  1/9]

        TESTS:

        A degenerate case::

            sage: T = TorsionQuadraticModule((1/6)*D4dual, D4, modulus=1/36)
            sage: T.normal_form()                                                       # needs sage.libs.pari sage.rings.padics
            Finite quadratic module over Integer Ring with invariants (6, 6, 12, 12)
            Gram matrix of the quadratic form with values in Q/(1/18)Z:
            [1/36 1/72    0    0    0    0    0    0]
            [1/72 1/36    0    0    0    0    0    0]
            [   0    0    0    0    0    0    0    0]
            [   0    0    0    0    0    0    0    0]
            [   0    0    0    0    0    0    0    0]
            [   0    0    0    0    0    0    0    0]
            [   0    0    0    0    0    0    0    0]
            [   0    0    0    0    0    0    0    0]
        """
    def primary_part(self, m):
        """
        Return the ``m``-primary part of this torsion quadratic module
        as a submodule.

        INPUT:

        - ``m`` -- integer

        OUTPUT: a submodule

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: T = TorsionQuadraticModule((1/6)*ZZ^3, ZZ^3); T
            Finite quadratic module over Integer Ring with invariants (6, 6, 6)
            Gram matrix of the quadratic form with values in Q/(1/3)Z:
            [1/36    0    0]
            [   0 1/36    0]
            [   0    0 1/36]
            sage: T.primary_part(2)
            Finite quadratic module over Integer Ring with invariants (2, 2, 2)
            Gram matrix of the quadratic form with values in Q/(1/3)Z:
            [1/4   0   0]
            [  0 1/4   0]
            [  0   0 1/4]

        TESTS::

            sage: T == T.primary_part(T.annihilator().gen())
            True
        """
    def submodule_with_gens(self, gens):
        """
        Return a submodule with generators given by ``gens``.

        INPUT:

        - ``gens`` -- list of generators that convert into ``self``

        OUTPUT: a submodule with the specified generators

        EXAMPLES::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: V = FreeQuadraticModule(ZZ, 3, matrix.identity(3)*10)
            sage: T = TorsionQuadraticModule((1/10)*V, V)
            sage: g = T.gens()
            sage: new_gens = [2*g[0], 5*g[0]]
            sage: T.submodule_with_gens(new_gens)
            Finite quadratic module over Integer Ring with invariants (10,)
            Gram matrix of the quadratic form with values in Q/2Z:
            [2/5   0]
            [  0 1/2]

        The generators do not need to be independent::

            sage: new_gens = [g[0], 2*g[1], g[0], g[1]]
            sage: T.submodule_with_gens(new_gens)
            Finite quadratic module over Integer Ring with invariants (10, 10)
            Gram matrix of the quadratic form with values in Q/2Z:
            [1/10    0 1/10    0]
            [   0  2/5    0  1/5]
            [1/10    0 1/10    0]
            [   0  1/5    0 1/10]

        TESTS:

        Test that things work without specified gens too::

            sage: from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
            sage: V = FreeQuadraticModule(ZZ, 3, matrix.identity(3)*5)
            sage: T = TorsionQuadraticModule((1/5)*V, V); T
            Finite quadratic module over Integer Ring with invariants (5, 5, 5)
            Gram matrix of the quadratic form with values in Q/Z:
            [1/5   0   0]
            [  0 1/5   0]
            [  0   0 1/5]
            sage: T.submodule(T.gens()[:2])
            Finite quadratic module over Integer Ring with invariants (5, 5)
            Gram matrix of the quadratic form with values in Q/Z:
            [1/5   0]
            [  0 1/5]
        """
    def twist(self, s):
        """
        Return the torsion quadratic module with quadratic form scaled by ``s``.

        If the old form was defined modulo `n`, then the new form is defined
        modulo `n s`.

        INPUT:

        - ``s`` -- a rational number

        EXAMPLES::

            sage: q = TorsionQuadraticForm(matrix.diagonal([3/9, 1/9]))
            sage: q.twist(-1)
            Finite quadratic module over Integer Ring with invariants (3, 9)
            Gram matrix of the quadratic form with values in Q/Z:
            [2/3   0]
            [  0 8/9]

        This form is defined modulo `3`::

            sage: q.twist(3)
            Finite quadratic module over Integer Ring with invariants (3, 9)
            Gram matrix of the quadratic form with values in Q/3Z:
            [  1   0]
            [  0 1/3]

        The next form is defined modulo `4`::

            sage: q.twist(4)
            Finite quadratic module over Integer Ring with invariants (3, 9)
            Gram matrix of the quadratic form with values in Q/4Z:
            [4/3   0]
            [  0 4/9]
        """
    def value_module(self):
        """
        Return `\\QQ / m\\ZZ` with `m = (V, W)`.

        This is where the inner product takes values.

        EXAMPLES::

            sage: A2 = Matrix(ZZ, 2, 2, [2,-1,-1,2])
            sage: L = IntegralLattice(2*A2)
            sage: D = L.discriminant_group(); D
            Finite quadratic module over Integer Ring with invariants (2, 6)
            Gram matrix of the quadratic form with values in Q/2Z:
            [  1 1/2]
            [1/2 1/3]
            sage: D.value_module()
            Q/Z
        """
    def value_module_qf(self):
        """
        Return `\\QQ / n\\ZZ` with `n\\ZZ = (V,W) + \\ZZ \\{ (w,w) | w \\in W \\}`.

        This is where the torsion quadratic form takes values.

        EXAMPLES::

            sage: A2 = Matrix(ZZ, 2, 2, [2,-1,-1,2])
            sage: L = IntegralLattice(2 * A2)
            sage: D = L.discriminant_group(); D
            Finite quadratic module over Integer Ring with invariants (2, 6)
            Gram matrix of the quadratic form with values in Q/2Z:
            [  1 1/2]
            [1/2 1/3]
            sage: D.value_module_qf()
            Q/2Z
        """
