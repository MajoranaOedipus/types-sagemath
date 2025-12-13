import sage.modules.matrix_morphism
from .finite_subgroup import TorsionPoint as TorsionPoint
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class Morphism_abstract(sage.modules.matrix_morphism.MatrixMorphism_abstract):
    """
    A morphism between modular abelian varieties.

    EXAMPLES::

        sage: t = J0(11).hecke_operator(2)
        sage: from sage.modular.abvar.morphism import Morphism
        sage: isinstance(t, Morphism)
        True
    """
    def complementary_isogeny(self):
        """
        Return the complementary isogeny of ``self``.

        EXAMPLES::

            sage: J = J0(43)
            sage: A = J[1]
            sage: T5 = A.hecke_operator(5)
            sage: T5.is_isogeny()
            True
            sage: T5.complementary_isogeny()
            Abelian variety endomorphism of Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)
            sage: (T5.complementary_isogeny() * T5).matrix()
            [2 0 0 0]
            [0 2 0 0]
            [0 0 2 0]
            [0 0 0 2]
        """
    def is_isogeny(self) -> bool:
        """
        Return ``True`` if this morphism is an isogeny of abelian varieties.

        EXAMPLES::

            sage: J = J0(39)
            sage: Id = J.hecke_operator(1)
            sage: Id.is_isogeny()
            True
            sage: J.hecke_operator(19).is_isogeny()
            False
        """
    def cokernel(self):
        """
        Return the cokernel of ``self``.

        OUTPUT:

        - ``A`` -- an abelian variety (the cokernel)

        - ``phi`` -- a quotient map from ``self.codomain()`` to the
          cokernel of self

        EXAMPLES::

            sage: t = J0(33).hecke_operator(2)
            sage: (t-1).cokernel()
            (Abelian subvariety of dimension 1 of J0(33),
             Abelian variety morphism:
              From: Abelian variety J0(33) of dimension 3
              To:   Abelian subvariety of dimension 1 of J0(33))

        Projection will always have cokernel zero.

        ::

            sage: J0(37).projection(J0(37)[0]).cokernel()
            (Simple abelian subvariety of dimension 0 of J0(37),
             Abelian variety morphism:
              From: Simple abelian subvariety 37a(1,37) of dimension 1 of J0(37)
              To:   Simple abelian subvariety of dimension 0 of J0(37))

        Here we have a nontrivial cokernel of a Hecke operator, as the
        T_2-eigenvalue for the newform 37b is 0.

        ::

            sage: J0(37).hecke_operator(2).cokernel()
            (Abelian subvariety of dimension 1 of J0(37),
             Abelian variety morphism:
              From: Abelian variety J0(37) of dimension 2
              To:   Abelian subvariety of dimension 1 of J0(37))
            sage: AbelianVariety('37b').newform().q_expansion(5)
            q + q^3 - 2*q^4 + O(q^5)
        """
    def kernel(self):
        """
        Return the kernel of this morphism.

        OUTPUT:

        - ``G`` -- a finite group

        - ``A`` -- an abelian variety (identity component of the kernel)

        EXAMPLES: We compute the kernel of a projection map. Notice that
        the kernel has a nontrivial abelian variety part.

        ::

            sage: A, B, C = J0(33)
            sage: pi = J0(33).projection(B)
            sage: pi.kernel()
            (Finite subgroup with invariants [20] over QQbar of Abelian variety J0(33) of dimension 3,
             Abelian subvariety of dimension 2 of J0(33))

        We compute the kernels of some Hecke operators::

            sage: t2 = J0(33).hecke_operator(2)
            sage: t2
            Hecke operator T_2 on Abelian variety J0(33) of dimension 3
            sage: t2.kernel()
            (Finite subgroup with invariants [2, 2, 2, 2] over QQ of Abelian variety J0(33) of dimension 3,
             Abelian subvariety of dimension 0 of J0(33))
            sage: t3 = J0(33).hecke_operator(3)
            sage: t3.kernel()
            (Finite subgroup with invariants [3, 3] over QQ of Abelian variety J0(33) of dimension 3,
             Abelian subvariety of dimension 0 of J0(33))
        """
    def factor_out_component_group(self):
        """
        View ``self`` as a morphism `f:A \\to B`. Then `\\ker(f)`
        is an extension of an abelian variety `C` by a finite
        component group `G`. This function constructs a morphism
        `g` with domain `A` and codomain Q isogenous to
        `C` such that `\\ker(g)` is equal to `C`.

        OUTPUT: a morphism

        EXAMPLES::

            sage: A,B,C = J0(33)
            sage: pi = J0(33).projection(A)
            sage: pi.kernel()
            (Finite subgroup with invariants [5] over QQbar of Abelian variety J0(33) of dimension 3,
             Abelian subvariety of dimension 2 of J0(33))
            sage: psi = pi.factor_out_component_group()
            sage: psi.kernel()
            (Finite subgroup with invariants [] over QQbar of Abelian variety J0(33) of dimension 3,
             Abelian subvariety of dimension 2 of J0(33))

        ALGORITHM: We compute a subgroup `G` of `B` so that
        the composition `h: A\\to B \\to B/G` has kernel that
        contains `A[n]` and component group isomorphic to
        `(\\ZZ/n\\ZZ)^{2d}`, where `d` is the
        dimension of `A`. Then `h` factors through
        multiplication by `n`, so there is a morphism
        `g: A\\to B/G` such that `g \\circ [n] = h`. Then
        `g` is the desired morphism. We give more details below
        about how to transform this into linear algebra.
        """
    def image(self):
        """
        Return the image of this morphism.

        OUTPUT: an abelian variety

        EXAMPLES: We compute the image of projection onto a factor of
        `J_0(33)`::

            sage: A,B,C = J0(33)
            sage: A
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: f = J0(33).projection(A)
            sage: f.image()
            Abelian subvariety of dimension 1 of J0(33)
            sage: f.image() == A
            True

        We compute the image of a Hecke operator::

            sage: t2 = J0(33).hecke_operator(2); t2.fcp()
            (x - 1) * (x + 2)^2
            sage: phi = t2 + 2
            sage: phi.image()
            Abelian subvariety of dimension 1 of J0(33)

        The sum of the image and the kernel is the whole space::

            sage: phi.kernel()[1] + phi.image() == J0(33)
            True
        """
    def __call__(self, X):
        """
        INPUT:

        - ``X`` -- abelian variety, finite group, or torsion element

        OUTPUT: abelian variety, finite group, torsion element

        EXAMPLES: We apply morphisms to elements::

            sage: t2 = J0(33).hecke_operator(2)
            sage: G  = J0(33).torsion_subgroup(2); G
            Finite subgroup with invariants [2, 2, 2, 2, 2, 2] over QQ of Abelian variety J0(33) of dimension 3
            sage: t2(G.0)
            [(-1/2, 0, 1/2, -1/2, 1/2, -1/2)]
            sage: t2(G.0) in G
            True
            sage: t2(G.1)
            [(0, -1, 1/2, 0, 1/2, -1/2)]
            sage: t2(G.2)
            [(0, 0, 0, 0, 0, 0)]
            sage: K = t2.kernel()[0]; K
            Finite subgroup with invariants [2, 2, 2, 2] over QQ of Abelian variety J0(33) of dimension 3
            sage: t2(K.0)
            [(0, 0, 0, 0, 0, 0)]

        We apply morphisms to subgroups::

            sage: t2 = J0(33).hecke_operator(2)
            sage: G  = J0(33).torsion_subgroup(2); G
            Finite subgroup with invariants [2, 2, 2, 2, 2, 2] over QQ of Abelian variety J0(33) of dimension 3
            sage: t2(G)
            Finite subgroup with invariants [2, 2] over QQ of Abelian variety J0(33) of dimension 3
            sage: t2.fcp()
            (x - 1) * (x + 2)^2

        We apply morphisms to abelian subvarieties::

            sage: E11a0, E11a1, B = J0(33)
            sage: t2 = J0(33).hecke_operator(2)
            sage: t3 = J0(33).hecke_operator(3)
            sage: E11a0
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: t3(E11a0)
            Abelian subvariety of dimension 1 of J0(33)
            sage: t3(E11a0).decomposition()
            [Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33)]
            sage: t3(E11a0) == E11a1
            True
            sage: t2(E11a0) == E11a0
            True
            sage: t3(E11a0) == E11a0
            False
            sage: t3(E11a0 + E11a1) == E11a0 + E11a1
            True

        We apply some Hecke operators to the cuspidal subgroup and split it
        up::

            sage: C = J0(33).cuspidal_subgroup(); C
            Finite subgroup with invariants [10, 10] over QQ of Abelian variety J0(33) of dimension 3
            sage: t2 = J0(33).hecke_operator(2); t2.fcp()
            (x - 1) * (x + 2)^2
            sage: (t2 - 1)(C)
            Finite subgroup with invariants [5, 5] over QQ of Abelian variety J0(33) of dimension 3
            sage: (t2 + 2)(C)
            Finite subgroup with invariants [2, 2] over QQ of Abelian variety J0(33) of dimension 3

        Same but on a simple new factor::

            sage: C = J0(33)[2].cuspidal_subgroup(); C
            Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)
            sage: t2 = J0(33)[2].hecke_operator(2); t2.fcp()
            x - 1
            sage: t2(C)
            Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)
        """

class Morphism(Morphism_abstract, sage.modules.matrix_morphism.MatrixMorphism):
    def restrict_domain(self, sub):
        """
        Restrict ``self`` to the subvariety sub of ``self.domain()``.

        EXAMPLES::

            sage: J = J0(37) ; A, B = J.decomposition()
            sage: A.lattice().matrix()
            [ 1 -1  1  0]
            [ 0  0  2 -1]
            sage: B.lattice().matrix()
            [1 1 1 0]
            [0 0 0 1]
            sage: T = J.hecke_operator(2) ; T.matrix()
            [-1  1  1 -1]
            [ 1 -1  1  0]
            [ 0  0 -2  1]
            [ 0  0  0  0]
            sage: T.restrict_domain(A)
            Abelian variety morphism:
              From: Simple abelian subvariety 37a(1,37) of dimension 1 of J0(37)
              To:   Abelian variety J0(37) of dimension 2
            sage: T.restrict_domain(A).matrix()
            [-2  2 -2  0]
            [ 0  0 -4  2]
            sage: T.restrict_domain(B)
            Abelian variety morphism:
              From: Simple abelian subvariety 37b(1,37) of dimension 1 of J0(37)
              To:   Abelian variety J0(37) of dimension 2
            sage: T.restrict_domain(B).matrix()
            [0 0 0 0]
            [0 0 0 0]
        """

class DegeneracyMap(Morphism):
    def __init__(self, parent, A, t, side: str = 'left') -> None:
        """
        Create the degeneracy map of index t in parent defined by the
        matrix A.

        INPUT:

        - ``parent`` -- a space of homomorphisms of abelian varieties

        - ``A`` -- a matrix defining self

        - ``t`` -- list of indices defining the degeneracy map

        EXAMPLES::

            sage: J0(44).degeneracy_map(11,2)
            Degeneracy map from Abelian variety J0(44) of dimension 4 to Abelian variety J0(11) of dimension 1 defined by [2]
            sage: J0(44)[0].degeneracy_map(88,2)
            Degeneracy map from Simple abelian subvariety 11a(1,44) of dimension 1 of J0(44) to Abelian variety J0(88) of dimension 9 defined by [2]
        """
    def t(self):
        """
        Return the list of indices defining ``self``.

        EXAMPLES::

            sage: J0(22).degeneracy_map(44).t()
            [1]
            sage: J = J0(22) * J0(11)
            sage: J.degeneracy_map([44,44], [2,1])
            Degeneracy map from Abelian variety J0(22) x J0(11) of dimension 3 to Abelian variety J0(44) x J0(44) of dimension 8 defined by [2, 1]
            sage: J.degeneracy_map([44,44], [2,1]).t()
            [2, 1]
        """

class HeckeOperator(Morphism):
    """
    A Hecke operator acting on a modular abelian variety.
    """
    def __init__(self, abvar, n, side: str = 'left') -> None:
        """
        Create the Hecke operator of index `n` acting on the
        abelian variety abvar.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        - ``n`` -- positive integer

        EXAMPLES::

            sage: J = J0(37)
            sage: T2 = J.hecke_operator(2); T2
            Hecke operator T_2 on Abelian variety J0(37) of dimension 2
            sage: T2.parent()
            Endomorphism ring of Abelian variety J0(37) of dimension 2
        """
    def index(self):
        """
        Return the index of this Hecke operator. (For example, if this is
        the operator `T_n`, then the index is the integer `n`.)

        OUTPUT:

        - ``n`` -- a (Sage) Integer

        EXAMPLES::

            sage: J = J0(15)
            sage: t = J.hecke_operator(53)
            sage: t
            Hecke operator T_53 on Abelian variety J0(15) of dimension 1
            sage: t.index()
            53
            sage: t = J.hecke_operator(54)
            sage: t
            Hecke operator T_54 on Abelian variety J0(15) of dimension 1
            sage: t.index()
            54

        ::

            sage: J = J1(12345)
            sage: t = J.hecke_operator(997) ; t
            Hecke operator T_997 on Abelian variety J1(12345) of dimension 5405473
            sage: t.index()
            997
            sage: type(t.index())
            <class 'sage.rings.integer.Integer'>
        """
    def n(self):
        """
        Alias for ``self.index()``.

        EXAMPLES::

            sage: J = J0(17)
            sage: J.hecke_operator(5).n()
            5
        """
    def characteristic_polynomial(self, var: str = 'x'):
        """
        Return the characteristic polynomial of this Hecke operator in the
        given variable.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        OUTPUT: a polynomial in var over the rational numbers

        EXAMPLES::

            sage: A = J0(43)[1]; A
            Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)
            sage: t2 = A.hecke_operator(2); t2
            Hecke operator T_2 on Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)
            sage: f = t2.characteristic_polynomial(); f
            x^2 - 2
            sage: f.parent()
            Univariate Polynomial Ring in x over Integer Ring
            sage: f.factor()
            x^2 - 2
            sage: t2.characteristic_polynomial('y')
            y^2 - 2
        """
    def charpoly(self, var: str = 'x'):
        """
        Synonym for ``self.characteristic_polynomial(var)``.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        EXAMPLES::

            sage: A = J1(13)
            sage: t2 = A.hecke_operator(2); t2
            Hecke operator T_2 on Abelian variety J1(13) of dimension 2
            sage: f = t2.charpoly(); f
            x^2 + 3*x + 3
            sage: f.factor()
            x^2 + 3*x + 3
            sage: t2.charpoly('y')
            y^2 + 3*y + 3
        """
    def fcp(self, var: str = 'x'):
        """
        Return the factorization of the characteristic polynomial.

        EXAMPLES::

            sage: t2 = J0(33).hecke_operator(2)
            sage: t2.charpoly()
            x^3 + 3*x^2 - 4
            sage: t2.fcp()
            (x - 1) * (x + 2)^2
        """
    def action_on_homology(self, R=...):
        """
        Return the action of this Hecke operator on the homology
        `H_1(A; R)` of this abelian variety with coefficients in
        `R`.

        EXAMPLES::

            sage: A = J0(43)
            sage: t2 = A.hecke_operator(2); t2
            Hecke operator T_2 on Abelian variety J0(43) of dimension 3
            sage: h2 = t2.action_on_homology(); h2
            Hecke operator T_2 on Integral Homology of Abelian variety J0(43) of dimension 3
            sage: h2.matrix()
            [-2  1  0  0  0  0]
            [-1  1  1  0 -1  0]
            [-1  0 -1  2 -1  1]
            [-1  0  1  1 -1  1]
            [ 0 -2  0  2 -2  1]
            [ 0 -1  0  1  0 -1]
            sage: h2 = t2.action_on_homology(GF(2)); h2
            Hecke operator T_2 on Homology with coefficients in Finite Field of size 2 of Abelian variety J0(43) of dimension 3
            sage: h2.matrix()
            [0 1 0 0 0 0]
            [1 1 1 0 1 0]
            [1 0 1 0 1 1]
            [1 0 1 1 1 1]
            [0 0 0 0 0 1]
            [0 1 0 1 0 1]
        """
    def matrix(self):
        """
        Return the matrix of ``self`` acting on the homology
        `H_1(A, ZZ)` of this abelian variety with coefficients in `\\ZZ`.

        EXAMPLES::

            sage: J0(47).hecke_operator(3).matrix()
            [ 0  0  1 -2  1  0 -1  0]
            [ 0  0  1  0 -1  0  0  0]
            [-1  2  0  0  2 -2  1 -1]
            [-2  1  1 -1  3 -1 -1  0]
            [-1 -1  1  0  1  0 -1  1]
            [-1  0  0 -1  2  0 -1  0]
            [-1 -1  2 -2  2  0 -1  0]
            [ 0 -1  0  0  1  0 -1  1]

        ::

            sage: J0(11).hecke_operator(7).matrix()
            [-2  0]
            [ 0 -2]
            sage: (J0(11) * J0(33)).hecke_operator(7).matrix()
            [-2  0  0  0  0  0  0  0]
            [ 0 -2  0  0  0  0  0  0]
            [ 0  0  0  0  2 -2  2 -2]
            [ 0  0  0 -2  2  0  2 -2]
            [ 0  0  0  0  2  0  4 -4]
            [ 0  0 -4  0  2  2  2 -2]
            [ 0  0 -2  0  2  2  0 -2]
            [ 0  0 -2  0  0  2  0 -2]

        ::

            sage: J0(23).hecke_operator(2).matrix()
            [ 0  1 -1  0]
            [ 0  1 -1  1]
            [-1  2 -2  1]
            [-1  1  0 -1]
        """
