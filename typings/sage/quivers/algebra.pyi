from .algebra_elements import PathAlgebraElement as PathAlgebraElement
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method

class PathAlgebra(CombinatorialFreeModule):
    """
    Create the path algebra of a :class:`quiver <DiGraph>` over a given field.

    Given a quiver `Q` and a field `k`, the path algebra `kQ` is defined as
    follows.  As a vector space it has basis the set of all paths in `Q`.
    Multiplication is defined on this basis and extended bilinearly.  If `p`
    is a path with terminal vertex `t` and `q` is a path with initial vertex
    `i` then the product `p*q` is defined to be the composition of the
    paths `p` and `q` if `t = i` and `0` otherwise.

    INPUT:

    - ``k`` -- field (or commutative ring), the base field of the path algebra

    - ``P`` -- the path semigroup of a quiver `Q`

    - ``order`` -- string; one of ``'negdegrevlex'`` (default),
      ``'degrevlex'``, ``'negdeglex'`` or ``'deglex'``, defining the monomial
      order to be used

    OUTPUT: the path algebra `kP` with the given monomial order

    .. NOTE::

        Monomial orders that are not degree orders are not supported.

    EXAMPLES::

        sage: P = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
        sage: A = P.algebra(GF(7))
        sage: A
        Path algebra of Multi-digraph on 3 vertices over Finite Field of size 7
        sage: A.variable_names()
        ('e_1', 'e_2', 'e_3', 'a', 'b')

    Note that path algebras are uniquely defined by their quiver, field and
    monomial order::

        sage: A is P.algebra(GF(7))
        True
        sage: A is P.algebra(GF(7), order='degrevlex')
        False
        sage: A is P.algebra(RR)
        False
        sage: A is DiGraph({1:{2:['a']}}).path_semigroup().algebra(GF(7))
        False

    The path algebra of an acyclic quiver has a finite basis::

        sage: A.dimension()
        6
        sage: list(A.basis())
        [e_1, e_2, e_3, a, b, a*b]

    The path algebra can create elements from paths or from elements of the
    base ring::

        sage: A(5)
        5*e_1 + 5*e_2 + 5*e_3
        sage: S = A.semigroup()
        sage: S
        Partial semigroup formed by the directed paths of Multi-digraph on 3 vertices
        sage: p = S([(1, 2, 'a')])
        sage: r = S([(2, 3, 'b')])
        sage: e2 = S([(2, 2)])
        sage: x = A(p) + A(e2)
        sage: x
        a + e_2
        sage: y = A(p) + A(r)
        sage: y
        a + b

    Path algebras are graded algebras.  The grading is given by assigning
    to each basis element the length of the path corresponding to that
    basis element::

        sage: x.is_homogeneous()
        False
        sage: x.degree()
        Traceback (most recent call last):
        ...
        ValueError: element is not homogeneous
        sage: y.is_homogeneous()
        True
        sage: y.degree()
        1
        sage: A[1]
        Free module spanned by [a, b] over Finite Field of size 7
        sage: A[2]
        Free module spanned by [a*b] over Finite Field of size 7

    TESTS::

        sage: TestSuite(A).run()
    """
    Element = PathAlgebraElement
    def __init__(self, k, P, order: str = 'negdegrevlex') -> None:
        """
        Create a :class:`PathAlgebra` object.

        Type ``PathAlgebra?`` for more information.

        INPUT:

        - ``k`` -- a commutative ring
        - ``P`` -- the partial semigroup formed by the paths of a quiver

        TESTS::

            sage: P = DiGraph({1:{2:['a']}, 2:{3:['b', 'c']}, 4:{}}).path_semigroup()
            sage: P.algebra(GF(5))
            Path algebra of Multi-digraph on 4 vertices over Finite Field of size 5
        """
    def order_string(self) -> str:
        """
        Return the string that defines the monomial order of this algebra.

        EXAMPLES::

            sage: P1 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P2 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P3 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='negdeglex')
            sage: P4 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='deglex')
            sage: P1.order_string()
            'negdegrevlex'
            sage: P2.order_string()
            'degrevlex'
            sage: P3.order_string()
            'negdeglex'
            sage: P4.order_string()
            'deglex'
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of this algebra (idempotents and arrows).

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a']}, 2:{3:['b', 'c']}, 4:{}}).path_semigroup()
            sage: A = P.algebra(GF(5))
            sage: A.variable_names()
            ('e_1', 'e_2', 'e_3', 'e_4', 'a', 'b', 'c')
            sage: A.gens()
            (e_1, e_2, e_3, e_4, a, b, c)
        """
    @cached_method
    def arrows(self):
        """
        Return the arrows of this algebra (corresponding to edges of the
        underlying quiver).

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a']}, 2:{3:['b', 'c']}, 4:{}}).path_semigroup()
            sage: A = P.algebra(GF(5))
            sage: A.arrows()
            (a, b, c)
        """
    @cached_method
    def idempotents(self):
        """
        Return the idempotents of this algebra (corresponding to vertices
        of the underlying quiver).

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a']}, 2:{3:['b', 'c']}, 4:{}}).path_semigroup()
            sage: A = P.algebra(GF(5))
            sage: A.idempotents()
            (e_1, e_2, e_3, e_4)
        """
    @cached_method
    def gen(self, i):
        """
        Return the `i`-th generator of this algebra.

        This is an idempotent (corresponding to a trivial path at a
        vertex) if `i < n` (where `n` is the number of vertices of the
        quiver), and a single-edge path otherwise.

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a']}, 2:{3:['b', 'c']}, 4:{}}).path_semigroup()
            sage: A = P.algebra(GF(5))
            sage: A.gens()
            (e_1, e_2, e_3, e_4, a, b, c)
            sage: A.gen(2)
            e_3
            sage: A.gen(5)
            b
        """
    def ngens(self):
        """
        Number of generators of this algebra.

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a']}, 2:{3:['b', 'c']}, 4:{}}).path_semigroup()
            sage: A = P.algebra(GF(5))
            sage: A.ngens()
            7
        """
    @cached_method
    def one(self):
        """
        Return the multiplicative identity element.

        The multiplicative identity of a path algebra is the sum of the basis
        elements corresponding to the trivial paths at each vertex.

        EXAMPLES::

            sage: A = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup().algebra(QQ)
            sage: A.one()
            e_1 + e_2 + e_3
        """
    def quiver(self):
        """
        Return the quiver from which the algebra ``self`` was formed.

        OUTPUT: :class:`DiGraph`; the quiver of the algebra

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: A = P.algebra(GF(3))
            sage: A.quiver() is P.quiver()
            True
        """
    def semigroup(self):
        """
        Return the (partial) semigroup from which the algebra ``self`` was
        constructed.

        .. NOTE::

            The partial semigroup is formed by the paths of a quiver,
            multiplied by concatenation. If the quiver has more than a single
            vertex, then multiplication in the path semigroup is not always
            defined.

        OUTPUT:

        - the path semigroup from which ``self`` was formed (a partial
          semigroup)

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a', 'b']}}).path_semigroup()
            sage: A = P.algebra(GF(3))
            sage: A.semigroup() is P
            True
        """
    def degree_on_basis(self, x):
        """
        Return ``x.degree()``.

        This function is here to make some methods work that are inherited
        from :class:`~sage.combinat.free_module.CombinatorialFreeModule`.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: X = a+2*b+3*c*e-a*d+5*e_0+3*e_2
            sage: X
            5*e_0 + a - a*d + 2*b + 3*e_2
            sage: X.homogeneous_component(0)   # indirect doctest
            5*e_0 + 3*e_2
            sage: X.homogeneous_component(1)
            a + 2*b
            sage: X.homogeneous_component(2)
            -a*d
            sage: X.homogeneous_component(3)
            0
        """
    def sum(self, iter_of_elements):
        """
        Return the sum of all elements in ``iter_of_elements``.

        INPUT:

        - ``iter_of_elements`` -- iterator of elements of ``self``

        .. NOTE::

            It overrides a method inherited from
            :class:`~sage.combinat.free_module.CombinatorialFreeModule`,
            which relies on a private attribute of elements---an
            implementation detail that is simply not available for
            :class:`~sage.quivers.algebra_elements.PathAlgebraElement`.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: A.sum((a, 2*b, 3*c*e, -a*d, 5*e_0, 3*e_2))
            5*e_0 + a - a*d + 2*b + 3*e_2
        """
    def linear_combination(self, iter_of_elements_coeff, factor_on_left: bool = True):
        """
        Return the linear combination `\\lambda_1 v_1 + \\cdots +
        \\lambda_k v_k` (resp.  the linear combination `v_1 \\lambda_1 +
        \\cdots + v_k \\lambda_k`) where ``iter_of_elements_coeff`` iterates
        through the sequence `((v_1, \\lambda_1), ..., (v_k, \\lambda_k))`.

        INPUT:

        - ``iter_of_elements_coeff`` -- iterator of pairs ``(element, coeff)``
          with ``element`` in ``self`` and ``coeff`` in ``self.base_ring()``

        - ``factor_on_left`` -- (optional) if ``True``, the coefficients are
          multiplied from the left if ``False``, the coefficients are
          multiplied from the right

        .. NOTE::

            It overrides a method inherited from
            :class:`~sage.combinat.free_module.CombinatorialFreeModule`,
            which relies on a private attribute of elements---an
            implementation detail that is simply not available for
            :class:`~sage.quivers.algebra_elements.PathAlgebraElement`.

        EXAMPLES::

            sage: A = DiGraph({0: {1: ['a'], 2: ['b']},
            ....:              1: {0: ['c'], 1: ['d']},
            ....:              2: {0: ['e'], 2: ['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: A.linear_combination([(a, 1), (b, 2), (c*e, 3),
            ....:                       (a*d, -1), (e_0, 5), (e_2, 3)])
            5*e_0 + a - a*d + 2*b + 3*e_2
        """
    def homogeneous_component(self, n):
        """
        Return the `n`-th homogeneous piece of the path algebra.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        - :class:`CombinatorialFreeModule`, module spanned by the paths
          of length `n` in the quiver

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a'], 3:['b']}, 2:{4:['c']}, 3:{4:['d']}}).path_semigroup()
            sage: A = P.algebra(GF(7))
            sage: A.homogeneous_component(2)
            Free module spanned by [a*c, b*d] over Finite Field of size 7

            sage: D = DiGraph({1: {2: 'a'}, 2: {3: 'b'}, 3: {1: 'c'}})
            sage: P = D.path_semigroup()
            sage: A = P.algebra(ZZ)
            sage: A.homogeneous_component(3)
            Free module spanned by [a*b*c, b*c*a, c*a*b] over Integer Ring
        """
    __getitem__ = homogeneous_component
    def homogeneous_components(self):
        """
        Return the nonzero homogeneous components of ``self``.

        EXAMPLES::

            sage: Q = DiGraph([[1,2,'a'],[2,3,'b'],[3,4,'c']])
            sage: PQ = Q.path_semigroup()
            sage: A = PQ.algebra(GF(7))
            sage: A.homogeneous_components()
            [Free module spanned by [e_1, e_2, e_3, e_4] over Finite Field of size 7,
             Free module spanned by [a, b, c] over Finite Field of size 7,
             Free module spanned by [a*b, b*c] over Finite Field of size 7,
             Free module spanned by [a*b*c] over Finite Field of size 7]

        .. WARNING::

             Backward incompatible change: since :issue:`12630` and
             until :issue:`8678`, this feature was implemented under
             the syntax ``list(A)`` by means of ``A.__iter__``. This
             was incorrect since ``A.__iter__``, when defined for a
             parent, should iterate through the elements of `A`.
        """
