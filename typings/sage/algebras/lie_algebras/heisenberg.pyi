from sage.algebras.lie_algebras.lie_algebra import LieAlgebraFromAssociative as LieAlgebraFromAssociative, LieAlgebraWithGenerators as LieAlgebraWithGenerators
from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElement as LieAlgebraElement, LieAlgebraMatrixWrapper as LieAlgebraMatrixWrapper
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers
from sage.sets.set import Set as Set
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators

class HeisenbergAlgebra_abstract(IndexedGenerators):
    """
    The common methods for the (non-matrix) Heisenberg algebras.
    """
    def __init__(self, I) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo) # indirect doctest
        """
    def p(self, i):
        """
        The generator `p_i` of the Heisenberg algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.p(2)
            p2
        """
    def q(self, i):
        """
        The generator `q_i` of the Heisenberg algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.q(2)
            q2
        """
    def z(self):
        """
        Return the basis element `z` of the Heisenberg algebra.

        The element `z` spans the center of the Heisenberg algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.z()
            z
        """
    def bracket_on_basis(self, x, y):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``
        where ``x < y``.

        The basis of a Heisenberg algebra is ordered in such a way that
        the `p_i` come first, the `q_i` come next, and the `z` comes last.

        EXAMPLES::

            sage: H = lie_algebras.Heisenberg(QQ, 3)
            sage: p1 = ('p', 1)
            sage: q1 = ('q', 1)
            sage: H.bracket_on_basis(p1, q1)
            z
        """
    def step(self):
        """
        Return the nilpotency step of ``self``.

        EXAMPLES::

            sage: h = lie_algebras.Heisenberg(ZZ, 10)
            sage: h.step()
            2

            sage: h = lie_algebras.Heisenberg(ZZ, oo)
            sage: h.step()
            2
        """
    class Element(LieAlgebraElement): ...

class HeisenbergAlgebra_fd:
    """
    Common methods for finite-dimensional Heisenberg algebras.
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``n`` -- the rank

        TESTS::

            sage: H = lie_algebras.Heisenberg(QQ, 3) # indirect doctest
        """
    def n(self):
        """
        Return the rank of the Heisenberg algebra ``self``.

        This is the ``n`` such that ``self`` is the `n`-th Heisenberg
        algebra. The dimension of this Heisenberg algebra is then
        `2n + 1`.

        EXAMPLES::

            sage: H = lie_algebras.Heisenberg(QQ, 3)
            sage: H.n()
            3
            sage: H = lie_algebras.Heisenberg(QQ, 3, representation='matrix')
            sage: H.n()
            3
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the Lie algebra generators of ``self``.

        EXAMPLES::

            sage: H = lie_algebras.Heisenberg(QQ, 2)
            sage: H.gens()
            (p1, p2, q1, q2)
            sage: H = lie_algebras.Heisenberg(QQ, 0)
            sage: H.gens()
            (z,)
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        EXAMPLES::

            sage: H = lie_algebras.Heisenberg(QQ, 2)
            sage: H.gen(0)
            p1
            sage: H.gen(3)
            q2
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the Lie algebra generators of ``self``.

        EXAMPLES::

            sage: H = lie_algebras.Heisenberg(QQ, 1)
            sage: H.lie_algebra_generators()
            Finite family {'p1': p1, 'q1': q1}
            sage: H = lie_algebras.Heisenberg(QQ, 0)
            sage: H.lie_algebra_generators()
            Finite family {'z': z}
        """
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: H = lie_algebras.Heisenberg(QQ, 1)
            sage: H.basis()
            Finite family {'p1': p1, 'q1': q1, 'z': z}
        """

class HeisenbergAlgebra(HeisenbergAlgebra_fd, HeisenbergAlgebra_abstract, LieAlgebraWithGenerators):
    '''
    A Heisenberg algebra defined using structure coefficients.

    The `n`-th Heisenberg algebra (where `n` is a nonnegative
    integer or infinity) is the Lie algebra with basis
    `\\{p_i\\}_{1 \\leq i \\leq n} \\cup \\{q_i\\}_{1 \\leq i \\leq n} \\cup \\{z\\}`
    with the following relations:

    .. MATH::

        [p_i, q_j] = \\delta_{ij} z, \\quad [p_i, z] = [q_i, z] = [p_i, p_j]
        = [q_i, q_j] = 0.

    This Lie algebra is also known as the Heisenberg algebra of rank `n`.

    .. NOTE::

        The relations `[p_i, q_j] = \\delta_{ij} z`, `[p_i, z] = 0`, and
        `[q_i, z] = 0` are known as canonical commutation relations. See
        :wikipedia:`Canonical_commutation_relations`.

    .. WARNING::

        The `n` in the above definition is called the "rank" of the
        Heisenberg algebra; it is not, however, a rank in any of the usual
        meanings that this word has in the theory of Lie algebras.

    INPUT:

    - ``R`` -- the base ring
    - ``n`` -- the rank of the Heisenberg algebra

    REFERENCES:

    - :wikipedia:`Heisenberg_algebra`

    EXAMPLES::

        sage: L = lie_algebras.Heisenberg(QQ, 2)
    '''
    def __init__(self, R, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 2)
            sage: TestSuite(L).run()
            sage: L = lie_algebras.Heisenberg(QQ, 0)  # not tested -- :issue:`18224`
            sage: TestSuite(L).run()
        """

class InfiniteHeisenbergAlgebra(HeisenbergAlgebra_abstract, LieAlgebraWithGenerators):
    """
    The infinite Heisenberg algebra.

    This is the Heisenberg algebra on an infinite number of generators. In
    other words, this is the Heisenberg algebra of rank `\\infty`. See
    :class:`HeisenbergAlgebra` for more information.
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: TestSuite(L).run()
            sage: L.p(1).bracket(L.q(1)) == L.z()
            True
            sage: L.q(1).bracket(L.p(1)) == -L.z()
            True
        """
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.lie_algebra_generators()
            Lazy family (generator map(i))_{i in The Cartesian product of
                                            (Positive integers, {'p', 'q'})}
        """
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.basis()
            Lazy family (basis map(i))_{i in Disjoint union of Family ({'z'},
             The Cartesian product of (Positive integers, {'p', 'q'}))}
            sage: L.basis()['z']
            z
            sage: L.basis()[(12, 'p')]
            p12
        """

class HeisenbergAlgebra_matrix(HeisenbergAlgebra_fd, LieAlgebraFromAssociative):
    """
    A Heisenberg algebra represented using matrices.

    The `n`-th Heisenberg algebra over `R` is a Lie algebra which is
    defined as the Lie algebra of the `(n+2) \\times (n+2)`-matrices:

    .. MATH::

        \\begin{bmatrix}
        0 & p^T & k \\\\\n        0 & 0_n & q \\\\\n        0 & 0 & 0
        \\end{bmatrix}

    where `p, q \\in R^n` and `0_n` in the `n \\times n` zero matrix. It has
    a basis consisting of

    .. MATH::

        \\begin{aligned}
        p_i & = \\begin{bmatrix}
        0 & e_i^T & 0 \\\\\n        0 & 0_n & 0 \\\\\n        0 & 0 & 0
        \\end{bmatrix} \\qquad \\text{for } 1 \\leq i \\leq n ,
        \\\\ q_i & = \\begin{bmatrix}
        0 & 0 & 0 \\\\\n        0 & 0_n & e_i \\\\\n        0 & 0 & 0
        \\end{bmatrix} \\qquad \\text{for } 1 \\leq i \\leq n ,
        \\\\ z & = \\begin{bmatrix}
        0 & 0 & 1 \\\\\n        0 & 0_n & 0 \\\\\n        0 & 0 & 0
        \\end{bmatrix},
        \\end{aligned}

    where `\\{e_i\\}` is the standard basis of `R^n`. In other words, it has
    the basis `(p_1, p_2, \\ldots, p_n, q_1, q_2, \\ldots, q_n, z)`, where
    `p_i = E_{1, i+1}`, `q_i = E_{i+1, n+2}` and `z = E_{1, n+2}` are
    elementary matrices.

    This Lie algebra is isomorphic to the `n`-th Heisenberg algebra
    constructed in :class:`HeisenbergAlgebra`; the bases correspond to
    each other.

    INPUT:

    - ``R`` -- the base ring
    - ``n`` -- the nonnegative integer `n`

    EXAMPLES::

        sage: L = lie_algebras.Heisenberg(QQ, 1, representation='matrix')
        sage: p = L.p(1)
        sage: q = L.q(1)
        sage: z = L.bracket(p, q); z
        [0 0 1]
        [0 0 0]
        [0 0 0]
        sage: z == L.z()
        True
        sage: L.dimension()
        3

        sage: L = lie_algebras.Heisenberg(QQ, 2, representation='matrix')
        sage: sorted(dict(L.basis()).items())
        [(
              [0 1 0 0]
              [0 0 0 0]
              [0 0 0 0]
        'p1', [0 0 0 0]
        ),
         (
              [0 0 1 0]
              [0 0 0 0]
              [0 0 0 0]
        'p2', [0 0 0 0]
        ),
         (
              [0 0 0 0]
              [0 0 0 1]
              [0 0 0 0]
        'q1', [0 0 0 0]
        ),
         (
              [0 0 0 0]
              [0 0 0 0]
              [0 0 0 1]
        'q2', [0 0 0 0]
        ),
         (
             [0 0 0 1]
             [0 0 0 0]
             [0 0 0 0]
        'z', [0 0 0 0]
        )]

        sage: L = lie_algebras.Heisenberg(QQ, 0, representation='matrix')
        sage: sorted(dict(L.basis()).items())
        [(
             [0 1]
        'z', [0 0]
        )]
        sage: L.gens()
        (
        [0 1]
        [0 0]
        )
        sage: L.lie_algebra_generators()
        Finite family {'z': [0 1]
        [0 0]}
    """
    def __init__(self, R, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 2, representation='matrix')
            sage: TestSuite(L).run()
        """
    def p(self, i):
        """
        Return the generator `p_i` of the Heisenberg algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 1, representation='matrix')
            sage: L.p(1)
            [0 1 0]
            [0 0 0]
            [0 0 0]
        """
    def q(self, i):
        """
        Return the generator `q_i` of the Heisenberg algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 1, representation='matrix')
            sage: L.q(1)
            [0 0 0]
            [0 0 1]
            [0 0 0]
        """
    def z(self):
        """
        Return the basis element `z` of the Heisenberg algebra.

        The element `z` spans the center of the Heisenberg algebra.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 1, representation='matrix')
            sage: L.z()
            [0 0 1]
            [0 0 0]
            [0 0 0]
        """
    def step(self):
        """
        Return the nilpotency step of ``self``.

        EXAMPLES::

            sage: h = lie_algebras.Heisenberg(ZZ, 2, representation='matrix')
            sage: h.step()
            2
        """
    class Element(LieAlgebraMatrixWrapper, LieAlgebraFromAssociative.Element):
        def monomial_coefficients(self, copy: bool = True):
            """
            Return a dictionary whose keys are indices of basis elements in
            the support of ``self`` and whose values are the corresponding
            coefficients.

            INPUT:

            - ``copy`` -- ignored

            EXAMPLES::

                sage: L = lie_algebras.Heisenberg(QQ, 3, representation='matrix')
                sage: elt = L(Matrix(QQ, [[0, 1, 3, 0, 3], [0, 0, 0, 0, 0], [0, 0, 0, 0, -3],
                ....:                     [0, 0, 0, 0, 7], [0, 0, 0, 0, 0]]))
                sage: elt
                [ 0  1  3  0  3]
                [ 0  0  0  0  0]
                [ 0  0  0  0 -3]
                [ 0  0  0  0  7]
                [ 0  0  0  0  0]
                sage: sorted(elt.monomial_coefficients().items())
                [('p1', 1), ('p2', 3), ('q2', -3), ('q3', 7), ('z', 3)]
            """
