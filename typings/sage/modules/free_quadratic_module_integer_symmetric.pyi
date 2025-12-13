from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import gcd as gcd
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_quadratic_module import FreeQuadraticModule as FreeQuadraticModule, FreeQuadraticModule_submodule_with_basis_pid as FreeQuadraticModule_submodule_with_basis_pid
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Matrix as Matrix

def IntegralLattice(data, basis=None):
    '''
    Return the integral lattice spanned by ``basis`` in the ambient space.

    A lattice is a finitely generated free abelian group `L \\cong \\ZZ^r`
    equipped with a non-degenerate, symmetric bilinear form
    `L \\times L \\to \\ZZ`. Here, lattices have an
    ambient quadratic space `\\QQ^n` and a distinguished basis.

    INPUT:

    The input is a descriptor of the lattice and a (optional) basis.
    - ``data`` -- can be one of the following:

      * a symmetric matrix over the rationals -- the inner product matrix
      * an integer -- the dimension for a Euclidean lattice
      * a symmetric Cartan type or anything recognized by
        :class:`CartanMatrix` (see also
        :mod:`Cartan types <sage.combinat.root_system.cartan_type>`)
        -- for a root lattice
      * the string ``\'U\'`` or ``\'H\'`` -- for hyperbolic lattices

    - ``basis`` -- (optional) a matrix whose rows form a basis of the
      lattice, or a list of module elements forming a basis

    OUTPUT:

    A lattice in the ambient space defined by the inner_product_matrix.
    Unless specified, the basis of the lattice is the standard basis.

    EXAMPLES::

        sage: H5 = Matrix(ZZ, 2, [2,1,1,-2])
        sage: IntegralLattice(H5)
        Lattice of degree 2 and rank 2 over Integer Ring
        Standard basis
        Inner product matrix:
        [ 2  1]
        [ 1 -2]

    A basis can be specified too::

        sage: IntegralLattice(H5, Matrix([1,1]))
        Lattice of degree 2 and rank 1 over Integer Ring
        Basis matrix:
        [1 1]
        Inner product matrix:
        [ 2  1]
        [ 1 -2]

    We can define a Euclidean lattice just by its dimension::

        sage: IntegralLattice(3)
        Lattice of degree 3 and rank 3 over Integer Ring
        Standard basis
        Standard scalar product


    Here is an example of the `A_2` root lattice in Euclidean space::

        sage: basis = Matrix([[1,-1,0], [0,1,-1]])
        sage: A2 = IntegralLattice(3, basis)
        sage: A2
        Lattice of degree 3 and rank 2 over Integer Ring
        Basis matrix:
        [ 1 -1  0]
        [ 0  1 -1]
        Standard scalar product
        sage: A2.gram_matrix()
        [ 2 -1]
        [-1  2]

    We use ``\'U\'`` or ``\'H\'`` for defining a hyperbolic lattice::

        sage: L1 = IntegralLattice(\'U\')
        sage: L1
        Lattice of degree 2 and rank 2 over Integer Ring
        Standard basis
        Inner product matrix:
        [0 1]
        [1 0]
        sage: L1 == IntegralLattice(\'H\')
        True

    We can construct root lattices by specifying their type
    (see :mod:`Cartan types <sage.combinat.root_system.cartan_type>`
    and :class:`CartanMatrix`)::

        sage: # needs sage.graphs
        sage: IntegralLattice(["E", 7])
        Lattice of degree 7 and rank 7 over Integer Ring
        Standard basis
        Inner product matrix:
        [ 2  0 -1  0  0  0  0]
        [ 0  2  0 -1  0  0  0]
        [-1  0  2 -1  0  0  0]
        [ 0 -1 -1  2 -1  0  0]
        [ 0  0  0 -1  2 -1  0]
        [ 0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0 -1  2]
        sage: IntegralLattice(["A", 2])
        Lattice of degree 2 and rank 2 over Integer Ring
        Standard basis
        Inner product matrix:
        [ 2 -1]
        [-1  2]
        sage: IntegralLattice("D3")
        Lattice of degree 3 and rank 3 over Integer Ring
        Standard basis
        Inner product matrix:
        [ 2 -1 -1]
        [-1  2  0]
        [-1  0  2]
        sage: IntegralLattice(["D", 4])
        Lattice of degree 4 and rank 4 over Integer Ring
        Standard basis
        Inner product matrix:
        [ 2 -1  0  0]
        [-1  2 -1 -1]
        [ 0 -1  2  0]
        [ 0 -1  0  2]

    We can specify a basis as well::

        sage: G = Matrix(ZZ, 2, [0,1,1,0])
        sage: B = [vector([1,1])]
        sage: IntegralLattice(G, basis=B)
        Lattice of degree 2 and rank 1 over Integer Ring
        Basis matrix:
        [1 1]
        Inner product matrix:
        [0 1]
        [1 0]
        sage: IntegralLattice(["A", 3], [[1,1,1]])                                      # needs sage.graphs
        Lattice of degree 3 and rank 1 over Integer Ring
        Basis matrix:
        [1 1 1]
        Inner product matrix:
        [ 2 -1  0]
        [-1  2 -1]
        [ 0 -1  2]
        sage: IntegralLattice(4, [[1,1,1,1]])
        Lattice of degree 4 and rank 1 over Integer Ring
        Basis matrix:
        [1 1 1 1]
        Standard scalar product
        sage: IntegralLattice("A2", [[1,1]])                                            # needs sage.graphs
        Lattice of degree 2 and rank 1 over Integer Ring
        Basis matrix:
        [1 1]
        Inner product matrix:
        [ 2 -1]
        [-1  2]

    TESTS::

        sage: IntegralLattice(["A", 1, 1])                                              # needs sage.graphs
        Traceback (most recent call last):
        ...
        ValueError: lattices must be nondegenerate; use FreeQuadraticModule instead
        sage: IntegralLattice(["D", 3, 1])                                              # needs sage.graphs
        Traceback (most recent call last):
        ...
        ValueError: lattices must be nondegenerate; use FreeQuadraticModule instead
    '''
def IntegralLatticeDirectSum(Lattices, return_embeddings: bool = False):
    '''
    Return the direct sum of the lattices contained in the list ``Lattices``.

    INPUT:

    - ``Lattices`` -- list of lattices ``[L_1,...,L_n]``
    - ``return_embeddings`` -- boolean (default: ``False``)

    OUTPUT:

    The direct sum of the `L_i` if ``return_embeddings`` is ``False`` or
    the tuple ``[L, phi]`` where `L` is the direct sum of `L_i` and ``phi``
    is the list of embeddings from `L_i` to `L`.

    EXAMPLES::

        sage: # needs sage.graphs
        sage: from sage.modules.free_quadratic_module_integer_symmetric import IntegralLatticeDirectSum
        sage: L1 = IntegralLattice("D4")
        sage: L2 = IntegralLattice("A3", [[1, 1, 2]])
        sage: L3 = IntegralLattice("A4", [[0, 1, 1, 2], [1, 2, 3, 1]])
        sage: Lattices = [L1, L2, L3]
        sage: IntegralLatticeDirectSum([L1, L2, L3])
        Lattice of degree 11 and rank 7 over Integer Ring
        Basis matrix:
        [1 0 0 0 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0 0 0 0]
        [0 0 0 1 0 0 0 0 0 0 0]
        [0 0 0 0 1 1 2 0 0 0 0]
        [0 0 0 0 0 0 0 0 1 1 2]
        [0 0 0 0 0 0 0 1 2 3 1]
        Inner product matrix:
        [ 2 -1  0  0  0  0  0  0  0  0  0]
        [-1  2 -1 -1  0  0  0  0  0  0  0]
        [ 0 -1  2  0  0  0  0  0  0  0  0]
        [ 0 -1  0  2  0  0  0  0  0  0  0]
        [ 0  0  0  0  2 -1  0  0  0  0  0]
        [ 0  0  0  0 -1  2 -1  0  0  0  0]
        [ 0  0  0  0  0 -1  2  0  0  0  0]
        [ 0  0  0  0  0  0  0  2 -1  0  0]
        [ 0  0  0  0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0  0  0  0  0 -1  2]
        sage: L, phi = IntegralLatticeDirectSum([L1, L2, L3], True)
        sage: LL3 = L.sublattice(phi[2].image().basis_matrix())
        sage: L3.discriminant() == LL3.discriminant()
        True
        sage: x = L3([1, 2, 3, 1])
        sage: phi[2](x).inner_product(phi[2](x)) == x.inner_product(x)
        True

    TESTS::

        sage: IntegralLatticeDirectSum([IntegralLattice("D4")])                         # needs sage.graphs
        Lattice of degree 4 and rank 4 over Integer Ring
        Standard basis
        Inner product matrix:
        [ 2 -1  0  0]
        [-1  2 -1 -1]
        [ 0 -1  2  0]
        [ 0 -1  0  2]

        sage: L1 = IntegralLattice(2 * matrix.identity(2), [[1/2, 1/2]])
        sage: L2 = IntegralLattice("A3", [[1, 1, 2]])                                   # needs sage.graphs
        sage: L, phi = IntegralLatticeDirectSum([L1, L2], True)                         # needs sage.graphs
        sage: L                                                                         # needs sage.graphs
        Lattice of degree 5 and rank 2 over Integer Ring
        Basis matrix:
        [1/2 1/2   0   0   0]
        [  0   0   1   1   2]
        Inner product matrix:
        [ 2  0  0  0  0]
        [ 0  2  0  0  0]
        [ 0  0  2 -1  0]
        [ 0  0 -1  2 -1]
        [ 0  0  0 -1  2]
    '''
def IntegralLatticeGluing(Lattices, glue, return_embeddings: bool = False):
    '''
    Return an overlattice of the direct sum as defined by ``glue``.

    INPUT:

    - ``Lattices`` -- list of lattices `[L_1,...,L_n]`
    - ``glue`` -- list where the elements are lists in the form `[g_1,...,g_n]`;
      here `g_i` is an element of the discriminant group of `L_i`and
      the overlattice is spanned by the additional ``[sum(g) for g in glue]``
    - ``return_embeddings`` -- boolean (default: ``False``)

    OUTPUT:

    The glued lattice given by `L_i` and ``glue`` if ``return_embeddings``
    is ``False`` or the tuple ``[L, phi]`` where `L` is the glued lattice and
    ``phi`` the list of embeddings from `L_i` to `L`

    EXAMPLES:

    A single lattice can be glued. This is the same as taking an overlattice::

        sage: from sage.modules.free_quadratic_module_integer_symmetric import IntegralLatticeGluing
        sage: L1 = IntegralLattice(matrix([[4]]))
        sage: g1 = L1.discriminant_group().gens()[0]
        sage: glue = [[2 * g1]]
        sage: L = IntegralLatticeGluing([L1], glue)
        sage: L
        Lattice of degree 1 and rank 1 over Integer Ring
        Basis matrix:
        [1/2]
        Inner product matrix:
        [4]
        sage: L.gram_matrix()
        [1]
        sage: IntegralLatticeGluing([L1], glue, return_embeddings=True)
        [Lattice of degree 1 and rank 1 over Integer Ring
         Basis matrix:
         [1/2]
         Inner product matrix:
         [4], [Free module morphism defined by the matrix
          [2]
          Domain: Lattice of degree 1 and rank 1 over Integer Ring
          Standard basis
          Inner product matrix:
          [4]
          Codomain: Lattice of degree 1 and rank 1 over Integer Ring
          Basis matrix:
          [1/2]
          Inner product matrix:
          [4]]]

        sage: # needs sage.graphs
        sage: L1 = IntegralLattice([[2]])
        sage: L2 = IntegralLattice([[2]])
        sage: AL1 = L1.discriminant_group()
        sage: AL2 = L2.discriminant_group()
        sage: AL1
        Finite quadratic module over Integer Ring with invariants (2,)
        Gram matrix of the quadratic form with values in Q/2Z:
        [1/2]
        sage: g1 = L1.discriminant_group().gens()[0]
        sage: g2 = L2.discriminant_group().gens()[0]
        sage: glue = [[g1, g2]]
        sage: IntegralLatticeGluing([L1, L2], glue)
        Lattice of degree 2 and rank 2 over Integer Ring
        Basis matrix:
        [1/2 1/2]
        [  0   1]
        Inner product matrix:
        [2 0]
        [0 2]

        sage: # needs sage.graphs
        sage: L1 = IntegralLattice("A4")
        sage: L2 = IntegralLattice("A4")
        sage: g1 = L1.discriminant_group().gens()[0]
        sage: g2 = L2.discriminant_group().gens()[0]
        sage: glue = [[g1, 2 * g2]]
        sage: V, phi = IntegralLatticeGluing([L1, L2], glue, True)
        sage: V
        Lattice of degree 8 and rank 8 over Integer Ring
        Basis matrix:
        [1/5 2/5 3/5 4/5 2/5 4/5 1/5 3/5]
        [  0   1   0   0   0   0   0   0]
        [  0   0   1   0   0   0   0   0]
        [  0   0   0   1   0   0   0   0]
        [  0   0   0   0   1   0   0   0]
        [  0   0   0   0   0   1   0   0]
        [  0   0   0   0   0   0   1   0]
        [  0   0   0   0   0   0   0   1]
        Inner product matrix:
        [ 2 -1  0  0  0  0  0  0]
        [-1  2 -1  0  0  0  0  0]
        [ 0 -1  2 -1  0  0  0  0]
        [ 0  0 -1  2  0  0  0  0]
        [ 0  0  0  0  2 -1  0  0]
        [ 0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0  0 -1  2]
        sage: V.sublattice(phi[0].image().basis_matrix())
        Lattice of degree 8 and rank 4 over Integer Ring
        Basis matrix:
        [1 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0]
        [0 0 0 1 0 0 0 0]
        Inner product matrix:
        [ 2 -1  0  0  0  0  0  0]
        [-1  2 -1  0  0  0  0  0]
        [ 0 -1  2 -1  0  0  0  0]
        [ 0  0 -1  2  0  0  0  0]
        [ 0  0  0  0  2 -1  0  0]
        [ 0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0  0 -1  2]

    Different gluings can be composed::

        sage: # needs sage.graphs
        sage: D4 = IntegralLattice("D4")
        sage: D4.discriminant_group()
        Finite quadratic module over Integer Ring with invariants (2, 2)
        Gram matrix of the quadratic form with values in Q/2Z:
        [  1 1/2]
        [1/2   1]
        sage: L2 = IntegralLattice(2 * matrix.identity(2))
        sage: L2.discriminant_group()
        Finite quadratic module over Integer Ring with invariants (2, 2)
        Gram matrix of the quadratic form with values in Q/2Z:
        [1/2   0]
        [  0 1/2]
        sage: g1 = D4.discriminant_group().gens()[0]
        sage: g2 = L2.discriminant_group().gens()[0] + L2.discriminant_group().gens()[1]
        sage: D6, phi = IntegralLatticeGluing([D4, L2], [[g1, g2]], True)
        sage: AD6 = D6.discriminant_group()
        sage: AD6.normal_form()
        Finite quadratic module over Integer Ring with invariants (2, 2)
        Gram matrix of the quadratic form with values in Q/2Z:
        [3/2   0]
        [  0 3/2]
        sage: f1, g1 = AD6.normal_form().gens()
        sage: f2, g2 = L2.discriminant_group().gens()
        sage: E8, psi = IntegralLatticeGluing([D6, L2], [[f1, f2], [g1, g2]], True)
        sage: D4embed = E8.sublattice(psi[0](phi[0].image()).basis_matrix())
        sage: x = D4([1, 0, 0, 0])
        sage: psi[0](phi[0](x)).inner_product(psi[0](phi[0](x))) == x.inner_product(x)
        True
        sage: D4embed
        Lattice of degree 8 and rank 4 over Integer Ring
        Basis matrix:
        [1 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0]
        [0 0 0 1 0 0 0 0]
        Inner product matrix:
        [ 2 -1  0  0  0  0  0  0]
        [-1  2 -1 -1  0  0  0  0]
        [ 0 -1  2  0  0  0  0  0]
        [ 0 -1  0  2  0  0  0  0]
        [ 0  0  0  0  2  0  0  0]
        [ 0  0  0  0  0  2  0  0]
        [ 0  0  0  0  0  0  2  0]
        [ 0  0  0  0  0  0  0  2]

    The input may be a list of three or more lattices::

        sage: # needs sage.graphs
        sage: A7 = IntegralLattice("A7")
        sage: D5 = IntegralLattice("D5")
        sage: gA7 = A7.discriminant_group().gens()[0]
        sage: gD5 = D5.discriminant_group().gens()[0]
        sage: L, phi = IntegralLatticeGluing([A7, A7, D5, D5],
        ....:                          [[gA7, gA7, gD5, 2 * gD5],
        ....:                          [gA7, 7 * gA7, 2 * gD5, gD5]], True)
        sage: L.determinant()
        1
        sage: B = phi[0].matrix()
        sage: B*L.gram_matrix()*B.transpose() == A7.gram_matrix()
        True

    The gluing takes place in the direct sum of the respective ambient spaces::

        sage: # needs sage.graphs
        sage: L1 = IntegralLattice("D4", [[1, 1, 0, 0], [0, 1, 1, 0]])
        sage: L2 = IntegralLattice("E6", [[0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]])
        sage: f1, f2 = L1.discriminant_group().gens()
        sage: g1, g2 = L2.discriminant_group().gens()
        sage: L, phi = IntegralLatticeGluing([L1, L2],
        ....:                                  [[f1, g1], [f2, 2 * g2]], True)
        sage: phi[0]
        Free module morphism defined by the matrix
        [ 2  2 -2 -1]
        [ 0  2 -1  0]
        Domain: Lattice of degree 4 and rank 2 over Integer Ring
        Basis matrix:
        [1 1 0 0]
        [0 1 1 0]
        Inner product matrix:
        [ 2 -1  0  0]
        [-1  2 -1 -1]
        [ 0 -1  2  0]
        [ 0 -1  0  2]
        Codomain: Lattice of degree 10 and rank 4 over Integer Ring
        Basis matrix:
        [ 1/2    0 -1/2    0    0  1/2    0    0  1/2  1/2]
        [   0  1/2  1/2    0    0  1/2    0    0    0    0]
        [   0    0    0    0    0    1    0    0    0    0]
        [   0    0    0    0    0    0    0    0    1    1]
        Inner product matrix:
        [ 2 -1  0  0  0  0  0  0  0  0]
        [-1  2 -1 -1  0  0  0  0  0  0]
        [ 0 -1  2  0  0  0  0  0  0  0]
        [ 0 -1  0  2  0  0  0  0  0  0]
        [ 0  0  0  0  2  0 -1  0  0  0]
        [ 0  0  0  0  0  2  0 -1  0  0]
        [ 0  0  0  0 -1  0  2 -1  0  0]
        [ 0  0  0  0  0 -1 -1  2 -1  0]
        [ 0  0  0  0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0  0  0  0 -1  2]
        sage: B = phi[0].matrix()
        sage: B * L.gram_matrix() * B.transpose() == L1.gram_matrix()
        True
    '''

class FreeQuadraticModule_integer_symmetric(FreeQuadraticModule_submodule_with_basis_pid):
    '''
    This class represents non-degenerate, integral,
    symmetric free quadratic `\\ZZ`-modules.

    INPUT:

    - ``ambient`` -- an ambient free quadratic module
    - ``basis`` -- list of elements of ambient or a matrix
    - ``inner_product_matrix`` -- a symmetric matrix over the rationals

    EXAMPLES::

        sage: IntegralLattice("U", basis=[vector([1,1])])
        Lattice of degree 2 and rank 1 over Integer Ring
        Basis matrix:
        [1 1]
        Inner product matrix:
        [0 1]
        [1 0]
    '''
    def __init__(self, ambient, basis, inner_product_matrix, check: bool = True, already_echelonized: bool = False) -> None:
        '''
        Create the integral lattice spanned by ``basis`` in the ambient space.

        TESTS::

            sage: L = IntegralLattice("U")
            sage: TestSuite(L).run()
        '''
    @cached_method
    def is_even(self) -> bool:
        '''
        Return whether the diagonal entries of the Gram matrix are even.

        EXAMPLES::

            sage: G = Matrix(ZZ, 2, 2, [-1,1,1,2])
            sage: L = IntegralLattice(G)
            sage: L.is_even()
            False
            sage: L = IntegralLattice("A2")                                             # needs sage.graphs
            sage: L.is_even()                                                           # needs sage.graphs
            True
        '''
    @cached_method
    def dual_lattice(self):
        '''
        Return the dual lattice as a :class:`FreeQuadraticModule`.

        Let `L` be a lattice. Its dual lattice is

        .. MATH::

            L^\\vee = \\{x \\in L \\otimes \\QQ :  (x, l) \\in \\ZZ \\; \\forall l \\in L \\}.

        EXAMPLES::

            sage: L = IntegralLattice("A2")                                             # needs sage.graphs
            sage: Ldual = L.dual_lattice(); Ldual                                       # needs sage.graphs
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1/3 2/3]
            [  0   1]

        Since our lattices are always integral, a lattice is contained in its dual::

            sage: L.is_submodule(Ldual)                                                 # needs sage.graphs
            True
        '''
    def discriminant_group(self, s: int = 0):
        '''
        Return the discriminant group `L^\\vee / L` of this lattice.

        INPUT:

        - ``s`` -- integer (default: 0)

        OUTPUT:

        The `s` primary part of the discriminant group.
        If `s=0`, returns the whole discriminant group.

        EXAMPLES::

            sage: L = IntegralLattice(Matrix(ZZ, 2, 2, [2,1,1,-2]) * 2)
            sage: L.discriminant_group()
            Finite quadratic module over Integer Ring with invariants (2, 10)
            Gram matrix of the quadratic form with values in Q/2Z:
            [  1 1/2]
            [1/2 1/5]
            sage: L.discriminant_group(2)
            Finite quadratic module over Integer Ring with invariants (2, 2)
            Gram matrix of the quadratic form with values in Q/2Z:
            [  1 1/2]
            [1/2   1]
            sage: L.discriminant_group(5)
            Finite quadratic module over Integer Ring with invariants (5,)
            Gram matrix of the quadratic form with values in Q/2Z:
            [4/5]

        TESTS::

            sage: L = IntegralLattice("H")
            sage: L.discriminant_group()
            Finite quadratic module over Integer Ring with invariants ()
            Gram matrix of the quadratic form with values in Q/2Z:
            []

        Test that the memory leak in :issue:`31625` is fixed::

            sage: import gc
            sage: gc.freeze()
            sage: L = IntegralLattice("A2")                                             # needs sage.graphs
            sage: for k in range(1,500):  # long time
            ....:     G = L.twist(k)
            ....:     D = G.discriminant_group()
            sage: tmp = gc.collect()
            sage: tmp = gc.collect()
            sage: len([a for a in gc.get_objects() if type(a) == type(L)]) <= 300
            True
            sage: gc.unfreeze()
        '''
    def signature(self):
        '''
        Return the signature of this lattice, which is defined as
        the difference between the number of positive eigenvalues and
        the number of negative eigenvalues in the Gram matrix.

        EXAMPLES::

            sage: U = IntegralLattice("U")
            sage: U.signature()
            0
        '''
    @cached_method
    def signature_pair(self):
        '''
        Return the signature tuple `(n_+,n_-)` of this lattice.

        Here `n_+` (resp. `n_-`) is the number of positive (resp. negative)
        eigenvalues of the Gram matrix.

        EXAMPLES::

            sage: A2 = IntegralLattice("A2")                                            # needs sage.graphs
            sage: A2.signature_pair()                                                   # needs sage.graphs
            (2, 0)
        '''
    def direct_sum(self, M):
        """
        Return the direct sum of this lattice with ``M``.

        INPUT:

        - ``M`` -- a module over `\\ZZ`

        EXAMPLES::

            sage: A = IntegralLattice(1)
            sage: A.direct_sum(A)
            Lattice of degree 2 and rank 2 over Integer Ring
            Standard basis
            Standard scalar product
        """
    def is_primitive(self, M) -> bool:
        '''
        Return whether ``M`` is a primitive submodule of this lattice.

        A `\\ZZ`-submodule ``M`` of a `\\ZZ`-module ``L`` is called primitive if
        the quotient ``L/M`` is torsion free.

        INPUT:

        - ``M`` -- a submodule of this lattice

        EXAMPLES::

            sage: U = IntegralLattice("U")
            sage: L1 = U.span([vector([1,1])])
            sage: L2 = U.span([vector([1,-1])])
            sage: U.is_primitive(L1)
            True
            sage: U.is_primitive(L2)
            True
            sage: U.is_primitive(L1 + L2)
            False

        We can also compute the index::

            sage: (L1 + L2).index_in(U)
            2
        '''
    def orthogonal_complement(self, M):
        """
        Return the orthogonal complement of ``M`` in this lattice.

        INPUT:

        - ``M`` -- a module in the same ambient space or
          a list of elements of the ambient space

        EXAMPLES::

            sage: H5 = Matrix(ZZ, 2, [2,1,1,-2])
            sage: L = IntegralLattice(H5)
            sage: S = L.span([vector([1,1])])
            sage: L.orthogonal_complement(S)
            Lattice of degree 2 and rank 1 over Integer Ring
            Basis matrix:
            [1 3]
            Inner product matrix:
            [ 2  1]
            [ 1 -2]

            sage: L = IntegralLattice(2)
            sage: L.orthogonal_complement([vector(ZZ, [1,0])])
            Lattice of degree 2 and rank 1 over Integer Ring
            Basis matrix:
            [0 1]
            Standard scalar product
        """
    def sublattice(self, basis):
        '''
        Return the sublattice spanned by ``basis``.

        INPUT:

        - ``basis`` -- list of elements of this lattice

        EXAMPLES::

            sage: U = IntegralLattice("U")
            sage: S = U.sublattice([vector([1,1])]); S
            Lattice of degree 2 and rank 1 over Integer Ring
            Basis matrix:
            [1 1]
            Inner product matrix:
            [0 1]
            [1 0]
            sage: U.sublattice([vector([1,-1])/2])
            Traceback (most recent call last):
            ...
            ValueError: lattices must be integral; use FreeQuadraticModule instead
            sage: S.sublattice([vector([1,-1])])
            Traceback (most recent call last):
            ...
            ValueError: the basis (= [(1, -1)]) does not span a submodule
        '''
    def overlattice(self, gens):
        """
        Return the lattice spanned by this lattice and ``gens``.

        INPUT:

        - ``gens`` -- list of elements or a rational matrix

        EXAMPLES::

            sage: L = IntegralLattice(Matrix(ZZ, 2, 2, [2,0,0,2]))
            sage: M = L.overlattice([vector([1,1])/2])
            sage: M.gram_matrix()
            [1 1]
            [1 2]
        """
    def maximal_overlattice(self, p=None):
        '''
        Return a maximal even integral overlattice of this lattice.

        INPUT:

        - ``p`` -- (default: ``None``) if given return an overlattice
          `M` of this lattice `L` that is maximal at `p` and the
          completions `M_q = L_q` are equal for all primes `q \\neq p`

        If `p` is `2` or ``None``, then the lattice must be even.

        EXAMPLES::

            sage: # needs sage.graphs sage.libs.pari
            sage: L = IntegralLattice("A4").twist(25*89)
            sage: L.maximal_overlattice().determinant()
            5
            sage: L.maximal_overlattice(89).determinant().factor()
            5^9
            sage: L.maximal_overlattice(5).determinant().factor()
            5 * 89^4

        TESTS::

            sage: # needs sage.libs.flint (otherwise timeout) sage.libs.pari
            sage: L = IntegralLattice(matrix.diagonal([2,4,4,8]))
            sage: L.maximal_overlattice().is_even()
            True
        '''
    def orthogonal_group(self, gens=None, is_finite=None):
        '''
        Return the orthogonal group of this lattice as a matrix group.

        The elements are isometries of the ambient vector space
        which preserve this lattice. They are represented by
        matrices with respect to the standard basis.

        INPUT:

        - ``gens`` -- list of matrices (default: ``None``)
        - ``is_finite`` -- boolean (default: ``None``); if set to ``True``,
          then the group is placed in the category of finite groups. Sage does
          not check this.

        OUTPUT:

        The matrix group generated by ``gens``.
        If ``gens`` is not specified, then generators of the full
        orthogonal group of this lattice are computed. They are
        continued as the identity on the orthogonal complement of
        the lattice in its ambient space. Currently, we can only
        compute the orthogonal group for positive definite lattices.

        EXAMPLES::

            sage: A4 = IntegralLattice("A4")                                            # needs sage.graphs
            sage: Aut = A4.orthogonal_group(); Aut                                      # needs sage.graphs sage.libs.gap
            Group of isometries with 4 generators (
            [0 0 0 1]  [-1 -1 -1  0]  [ 1  0  0  0]  [ 1  0  0  0]
            [0 0 1 0]  [ 0  0  0 -1]  [-1 -1 -1 -1]  [ 0  1  0  0]
            [0 1 0 0]  [ 0  0  1  1]  [ 0  0  0  1]  [ 0  0  1  1]
            [1 0 0 0], [ 0  1  0  0], [ 0  0  1  0], [ 0  0  0 -1]
            )

        The group acts from the right on the lattice and its discriminant group::

            sage: # needs sage.graphs sage.libs.gap
            sage: x = A4.an_element()
            sage: g = Aut.an_element(); g
            [-1 -1 -1  0]
            [ 0  0  1  0]
            [ 0  0 -1 -1]
            [ 0  1  1  1]
            sage: x*g
            (-1, -1, -1, 0)
            sage: (x*g).parent() == A4
            True
            sage: (g*x).parent()
            Vector space of dimension 4 over Rational Field
            sage: y = A4.discriminant_group().an_element()
            sage: y*g
            (4)

        If the group is finite we can compute the usual things::

            sage: # needs sage.graphs sage.libs.gap
            sage: Aut.order()
            240
            sage: conj = Aut.conjugacy_classes_representatives()
            sage: len(conj)
            14
            sage: Aut.structure_description()
            \'C2 x S5\'

        The lattice can live in a larger ambient space::

            sage: A2 = IntegralLattice(matrix.identity(3),
            ....:                      Matrix(ZZ, 2, 3, [1,-1,0,0,1,-1]))
            sage: A2.orthogonal_group()                                                 # needs sage.libs.gap
            Group of isometries with 2 generators (
            [ 2/3  2/3 -1/3]  [1 0 0]
            [ 2/3 -1/3  2/3]  [0 0 1]
            [-1/3  2/3  2/3], [0 1 0]
            )

        It can be negative definite as well::

            sage: A2m = IntegralLattice(-Matrix(ZZ, 2, [2,1,1,2]))
            sage: G = A2m.orthogonal_group()                                            # needs sage.libs.gap
            sage: G.order()                                                             # needs sage.libs.gap
            12

        If the lattice is indefinite, sage does not know how to compute generators.
        Can you teach it?::

            sage: U = IntegralLattice(Matrix(ZZ, 2, [0,1,1,0]))
            sage: U.orthogonal_group()                                                  # needs sage.libs.gap
            Traceback (most recent call last):
            ...
            NotImplementedError: currently, we can only compute generators
            for orthogonal groups over definite lattices.

        But we can define subgroups::

            sage: S = IntegralLattice(Matrix(ZZ, 2, [2, 3, 3, 2]))
            sage: f = Matrix(ZZ, 2, [0,1,-1,3])
            sage: S.orthogonal_group([f])                                               # needs sage.libs.gap
            Group of isometries with 1 generator (
            [ 0  1]
            [-1  3]
            )

        TESTS:

        We can handle the trivial group::

            sage: S = IntegralLattice(Matrix(ZZ, 2, [2, 3, 3, 2]))
            sage: S.orthogonal_group([])                                                # needs sage.libs.gap
            Group of isometries with 1 generator (
            [1 0]
            [0 1]
            )
        '''
    automorphisms = orthogonal_group
    def genus(self):
        '''
        Return the genus of this lattice.

        EXAMPLES::

            sage: L = IntegralLattice("U")
            sage: L.genus()                                                             # needs sage.padics
            Genus of
            [0 1]
            [1 0]
            Signature:  (1, 1)
            Genus symbol at 2:    1^2
        '''
    def tensor_product(self, other, discard_basis: bool = False):
        '''
        Return the tensor product of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an integral lattice
        - ``discard_basis`` -- boolean (default: ``False``); if ``True``, then
          the lattice returned is equipped with the standard basis

        EXAMPLES::

            sage: # needs sage.graphs
            sage: L = IntegralLattice("D3", [[1,-1,0], [0,1,-1]])
            sage: L1 = L.tensor_product(L); L1
            Lattice of degree 9 and rank 4 over Integer Ring
            Basis matrix:
            [ 1 -1  0 -1  1  0  0  0  0]
            [ 0  1 -1  0 -1  1  0  0  0]
            [ 0  0  0  1 -1  0 -1  1  0]
            [ 0  0  0  0  1 -1  0 -1  1]
            Inner product matrix:
            [ 4 -2 -2 -2  1  1 -2  1  1]
            [-2  4  0  1 -2  0  1 -2  0]
            [-2  0  4  1  0 -2  1  0 -2]
            [-2  1  1  4 -2 -2  0  0  0]
            [ 1 -2  0 -2  4  0  0  0  0]
            [ 1  0 -2 -2  0  4  0  0  0]
            [-2  1  1  0  0  0  4 -2 -2]
            [ 1 -2  0  0  0  0 -2  4  0]
            [ 1  0 -2  0  0  0 -2  0  4]
            sage: L1.gram_matrix()
            [ 36 -12 -12   4]
            [-12  24   4  -8]
            [-12   4  24  -8]
            [  4  -8  -8  16]
            sage: L2 = L.tensor_product(L, True); L2
            Lattice of degree 4 and rank 4 over Integer Ring
            Standard basis
            Inner product matrix:
            [ 36 -12 -12   4]
            [-12  24   4  -8]
            [-12   4  24  -8]
            [  4  -8  -8  16]
        '''
    @cached_method
    def quadratic_form(self):
        '''
        Return the quadratic form given by `q(x)=(x,x)`.

        EXAMPLES::

            sage: L = IntegralLattice("A2")                                             # needs sage.graphs
            sage: q = L.quadratic_form(); q                                             # needs sage.graphs
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 2 -2 ]
            [ * 2 ]
        '''
    @cached_method
    def minimum(self):
        """
        Return the minimum of this lattice.

        .. MATH::

            \\min\\{x^2 | x \\in L\\setminus \\{0\\}\\}

        EXAMPLES::

            sage: L = IntegralLattice('A2')                                             # needs sage.graphs
            sage: L.minimum()                                                           # needs sage.graphs
            2
            sage: L.twist(-1).minimum()                                                 # needs sage.graphs
            -Infinity
        """
    @cached_method
    def maximum(self):
        """
        Return the maximum of this lattice.

        .. MATH::

            \\max\\{x^2 | x \\in L\\setminus \\{0\\}\\}

        EXAMPLES::

            sage: L = IntegralLattice('A2')                                             # needs sage.graphs
            sage: L.maximum()                                                           # needs sage.graphs
            +Infinity
            sage: L.twist(-1).maximum()                                                 # needs sage.graphs sage.libs.pari
            -2
        """
    min = minimum
    max = maximum
    def LLL(self):
        """
        Return this lattice with an LLL reduced basis.

        EXAMPLES::

            sage: L = IntegralLattice('A2')                                             # needs sage.graphs
            sage: L.lll() == L                                                          # needs sage.graphs sage.libs.pari
            True

            sage: G = matrix(ZZ, 3, [0,1,0, 1,0,0, 0,0,7])
            sage: V = matrix(ZZ, 3, [-14,-15,-15, -4,1,16, -5,-5,-4])
            sage: L = IntegralLattice(V * G * V.T)
            sage: L.lll().gram_matrix()                                                 # needs sage.libs.gap
            [0 0 1]
            [0 7 0]
            [1 0 0]
        """
    lll = LLL
    def short_vectors(self, n, **kwargs):
        """
        Return the short vectors of length `< n`.

        INPUT:

        - ``n`` -- integer
        - further keyword arguments are passed on to
          :meth:`sage.quadratic_forms.short_vector_list_up_to_length`

        OUTPUT: list `L` where ``L[k]`` is the list of vectors of lengths `k`

        EXAMPLES::

            sage: A2 = IntegralLattice('A2')                                            # needs sage.graphs
            sage: A2.short_vectors(3)                                                   # needs sage.graphs sage.libs.pari
            [[(0, 0)], [], [(1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]]
            sage: A2.short_vectors(3, up_to_sign_flag=True)                             # needs sage.graphs sage.libs.pari
            [[(0, 0)], [], [(1, 1), (0, 1), (1, 0)]]

        TESTS:

        Check that keyword arguments are passed to :meth:`sage.quadratic_forms.short_vector_list_up_to_length`
        (:issue:`39848`)::

            sage: A2 = IntegralLattice('A2')                                            # needs sage.graphs
            sage: A2.short_vectors(3, up_to_sign_flag=False)                            # needs sage.graphs sage.libs.pari
            [[(0, 0)], [], [(1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]]
        """
    def enumerate_short_vectors(self) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over all the vectors in this lattice (modulo sign),
        starting from shorter vectors.

        .. WARNING::

            The returned vectors are not necessarily ordered strictly
            by length.

        EXAMPLES::

            sage: L = IntegralLattice(4, [[1,2,3,4], [7,7,8,8], [1,-1,1,0]])
            sage: short = L.enumerate_short_vectors()
            sage: vecs = [next(short) for _ in range(20)]
            sage: sorted(vecs, key=lambda v: (L(v).inner_product(L(v)), v))
            [(1, -1, 1, 0), (2, -2, 2, 0), (3, -3, 3, 0), (0, 3, 2, 4), (1, 2, 3, 4),
             (3, 2, -2, -4), (4, 4, 1, 0), (-1, 4, 1, 4), (3, 5, 0, 0), (4, 1, -1, -4),
             (2, 1, 4, 4), (2, 3, -3, -4), (5, 3, 2, 0), (2, 6, -1, 0), (5, 0, 0, -4),
             (-2, 5, 0, 4), (4, -4, 4, 0), (1, 4, -4, -4), (6, 2, 3, 0), (3, 0, 5, 4)]

        This example demonstrates that the lattice inner product is used for the norm::

            sage: Q = Matrix(QQ, [[1000, 0], [0, 1]])
            sage: B = [[1, 1], [1, -1]]
            sage: L = IntegralLattice(Q, basis=B)
            sage: short = L.enumerate_short_vectors()
            sage: vecs = [next(short) for _ in range(20)]
            sage: sorted(vecs, key=lambda v: (L(v).inner_product(L(v)), v))
            [(0, -2), (0, -4), (0, -6), (0, -8), (0, -10), (0, -12), (0, -14), (0, -16),
            (0, -18), (0, -20), (0, -22), (0, -24), (0, -26), (0, -28), (0, -30), (-1, -1),
            (-1, 1), (-1, -3), (-1, 3), (0, -32)]
        """
    def enumerate_close_vectors(self, target) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over all the vectors in this lattice, starting
        from vectors relatively close to the given ``target`` vector.

        .. WARNING::

            The returned vectors are not necessarily ordered strictly
            by their distance to the target.

        EXAMPLES::

            sage: L = IntegralLattice(4, [[1,2,3,4], [7,7,8,8], [1,-1,1,0]])
            sage: t = vector([1/2, -133/7, 123.44, -11])
            sage: close = L.enumerate_close_vectors(t)
            sage: vecs = [next(close) for _ in range(10)]
            sage: sorted(vecs, key=lambda v: (L(v).inner_product(L(v)), v))
            [(-1, -16, 121, 148), (0, -17, 122, 148), (-3, -22, 122, 148), (1, -18, 123, 148), (-2, -23, 123, 148),
             (2, -19, 124, 148), (3, -20, 125, 148), (4, -21, 126, 148), (-3, -19, 124, 152), (-2, -20, 125, 152)]
        """
    def twist(self, s, discard_basis: bool = False):
        '''
        Return the lattice with inner product matrix scaled by ``s``.

        INPUT:

        - ``s`` -- nonzero integer
        - ``discard_basis`` -- boolean (default: ``False``); if ``True``, then
          the lattice returned is equipped with the standard basis

        EXAMPLES::

            sage: L = IntegralLattice("A4")                                             # needs sage.graphs
            sage: L.twist(3)                                                            # needs sage.graphs
            Lattice of degree 4 and rank 4 over Integer Ring
            Standard basis
            Inner product matrix:
            [ 6 -3  0  0]
            [-3  6 -3  0]
            [ 0 -3  6 -3]
            [ 0  0 -3  6]
            sage: L = IntegralLattice(3, [[2,1,0], [0,1,1]]); L
            Lattice of degree 3 and rank 2 over Integer Ring
            Basis matrix:
            [2 1 0]
            [0 1 1]
            Standard scalar product
            sage: L.twist(1)
            Lattice of degree 3 and rank 2 over Integer Ring
            Basis matrix:
            [2 1 0]
            [0 1 1]
            Standard scalar product
            sage: L.twist(1, True)
            Lattice of degree 2 and rank 2 over Integer Ring
            Standard basis
            Inner product matrix:
            [5 1]
            [1 2]
        '''

def local_modification(M, G, p, check: bool = True):
    '''
    Return a local modification of `M` that matches `G` at `p`.

    INPUT:

    - ``M`` -- a `\\ZZ_p`-maximal lattice

    - ``G`` -- the gram matrix of a lattice isomorphic to `M` over `\\QQ_p`

    - ``p`` -- a prime number

    OUTPUT:

    an integral lattice `M\'` in the ambient space of `M` such that `M` and `M\'` are locally equal at all
    completions except at `p` where `M\'` is locally equivalent to the lattice with gram matrix `G`

    EXAMPLES::

        sage: # needs sage.graphs sage.libs.pari
        sage: from sage.modules.free_quadratic_module_integer_symmetric import local_modification
        sage: L = IntegralLattice("A3").twist(15)
        sage: M = L.maximal_overlattice()
        sage: for p in prime_divisors(L.determinant()):
        ....:     M = local_modification(M, L.gram_matrix(), p)
        sage: M.genus() == L.genus()
        True
        sage: L = IntegralLattice("D4").twist(3*4)
        sage: M = L.maximal_overlattice()
        sage: local_modification(M, L.gram_matrix(), 2)
        Lattice of degree 4 and rank 4 over Integer Ring
        Basis matrix:
        [1/3   0 2/3 2/3]
        [  0 1/3   0 2/3]
        [  0   0   1   0]
        [  0   0   0   1]
        Inner product matrix:
        [ 24 -12   0   0]
        [-12  24 -12 -12]
        [  0 -12  24   0]
        [  0 -12   0  24]
    '''
