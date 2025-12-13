from .finite_dimensional_algebra_element import FiniteDimensionalAlgebraElement as FiniteDimensionalAlgebraElement
from .finite_dimensional_algebra_ideal import FiniteDimensionalAlgebraIdeal as FiniteDimensionalAlgebraIdeal
from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.magmatic_algebras import MagmaticAlgebras as MagmaticAlgebras
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import Matrix as Matrix
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FiniteDimensionalAlgebra(UniqueRepresentation, Parent):
    """
    Create a finite-dimensional `k`-algebra from a multiplication table.

    This is a magmatic `k`-algebra, i.e., not necessarily
    associative or unital.

    INPUT:

    - ``k`` -- a field

    - ``table`` -- list of matrices

    - ``names`` -- string (default: ``'e'``); names for the basis
      elements

    - ``assume_associative`` -- boolean (default: ``False``); if
      ``True``, then the category is set to ``category.Associative()``
      and methods requiring associativity assume this

    - ``assume_unital`` -- boolean (default: ``False``); if
      ``True``, then the category is set to ``category.Unital()``
      and methods requiring unitality assume this

    - ``category`` -- (default:
      ``MagmaticAlgebras(k).FiniteDimensional().WithBasis()``)
      the category to which this algebra belongs

    The list ``table`` must have the following form: there exists a
    finite-dimensional `k`-algebra of degree `n` with basis
    `(e_1, \\ldots, e_n)` such that the `i`-th element of ``table`` is the
    matrix of right multiplication by `e_i` with respect to the basis
    `(e_1, \\ldots, e_n)`.

    EXAMPLES::

        sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
        ....:                                      Matrix([[0, 1], [0, 0]])]); A
        Finite-dimensional algebra of degree 2 over Finite Field of size 3
        sage: TestSuite(A).run()

        sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
        ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
        ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
        sage: B
        Finite-dimensional algebra of degree 3 over Rational Field
        sage: B.one()
        e0 + e2
        sage: B.is_associative()
        True

    A more complicated example (the descent algebra of `S_3` in
    a slightly rescaled I-basis, see :class:`DescentAlgebra`)::

        sage: Ma = Matrix([[6,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
        sage: Mb = Matrix([[0,0,0,0], [0,1,0,0], [0,1,0,0], [0,0,0,0]])
        sage: Mc = Matrix([[0,0,0,0], [0,0,1,0], [0,0,1,0], [0,0,0,0]])
        sage: Md = Matrix([[0,0,0,0], [0,1,-1,0], [0,-1,1,0], [0,0,0,2]])
        sage: C = FiniteDimensionalAlgebra(QQ, [Ma, Mb, Mc, Md])
        sage: C.one()
        1/6*e0 + 1/2*e1 + 1/2*e2 + 1/2*e3
        sage: C.is_associative()
        True
        sage: C.is_commutative()
        False

    If we set both ``is_associative`` and ``is_unital`` to
    ``True``, then this is an associative unital algebra and
    belongs to the category of
    :class:`sage.categories.finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis`::

        sage: C = FiniteDimensionalAlgebra(QQ, [Ma, Mb, Mc, Md],
        ....:                              assume_associative=True,
        ....:                              assume_unital=True)
        sage: C.radical_basis()
        (e1 - e2,)
        sage: C.radical()
        Radical of Finite-dimensional algebra of degree 4 over Rational Field
        sage: C.center_basis()
        (e0, e1 + e2 + e3)
        sage: C.center()
        Center of Finite-dimensional algebra of degree 4 over Rational Field
        sage: C.center().is_commutative()
        True
        sage: e = C.basis()
        sage: C.annihilator_basis([e[1]])
        (e0, e1 - e2, e3)
        sage: C.annihilator_basis([e[1]], side='left')
        (e0, e1 - e2 - e3)

    TESTS::

        sage: A.category()
        Category of finite dimensional magmatic algebras with basis
         over Finite Field of size 3
        sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
        ....:                                      Matrix([[0, 1], [0, 0]])],
        ....:                              assume_associative=True)
        sage: A.category()
        Category of finite dimensional associative algebras with basis
         over Finite Field of size 3
    """
    @staticmethod
    def __classcall_private__(cls, k, table, names: str = 'e', assume_associative: bool = False, assume_unital: bool = False, category=None):
        """
        Normalize input.

        TESTS::

            sage: table = [Matrix([[1, 0], [0, 1]]), Matrix([[0, 1], [0, 0]])]
            sage: A1 = FiniteDimensionalAlgebra(GF(3), table)
            sage: A2 = FiniteDimensionalAlgebra(GF(3), table, names='e')
            sage: A3 = FiniteDimensionalAlgebra(GF(3), table, names=['e0', 'e1'])
            sage: A1 is A2 and A2 is A3
            True

        The ``assume_associative`` keyword is built into the category::

            sage: from sage.categories.magmatic_algebras import MagmaticAlgebras
            sage: cat = MagmaticAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A1 = FiniteDimensionalAlgebra(GF(3), table,
            ....:                               category=cat.Associative())
            sage: A2 = FiniteDimensionalAlgebra(GF(3), table, assume_associative=True)
            sage: A1 is A2
            True

        Likewise for the ``assume_associative`` keyword::

            sage: A3 = FiniteDimensionalAlgebra(GF(3), table,
            ....:                               category=cat.Unital())
            sage: A4 = FiniteDimensionalAlgebra(GF(3), table, assume_unital=True)
            sage: A3 is A4
            True

        With both keywords on, the
        :class:`sage.categories.algebras.Algebras` category
        is used::

            sage: cat_a = Algebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A5 = FiniteDimensionalAlgebra(GF(3), table,
            ....:                               category=cat_a)
            sage: A6 = FiniteDimensionalAlgebra(GF(3), table, assume_associative=True,
            ....:                               assume_unital=True)
            sage: A5 is A6
            True

        Uniqueness depends on the category::

            sage: cat = Algebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A1 = FiniteDimensionalAlgebra(GF(3), table)
            sage: A2 = FiniteDimensionalAlgebra(GF(3), table, category=cat)
            sage: A1 == A2
            False
            sage: A1 is A2
            False

        Checking that equality is still as expected::

            sage: A = FiniteDimensionalAlgebra(GF(3), table)
            sage: B = FiniteDimensionalAlgebra(GF(5), [Matrix([0])])
            sage: A == A
            True
            sage: B == B
            True
            sage: A == B
            False
            sage: A != A
            False
            sage: B != B
            False
            sage: A != B
            True
        """
    def __init__(self, k, table, names: str = 'e', category=None) -> None:
        """
        TESTS::

            sage: A = FiniteDimensionalAlgebra(QQ, [])
            sage: A
            Finite-dimensional algebra of degree 0 over Rational Field
            sage: type(A)
            <class 'sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra.FiniteDimensionalAlgebra_with_category'>
            sage: TestSuite(A).run()

            sage: B = FiniteDimensionalAlgebra(GF(7), [Matrix([1])])
            sage: B
            Finite-dimensional algebra of degree 1 over Finite Field of size 7
            sage: TestSuite(B).run()

            sage: C = FiniteDimensionalAlgebra(CC, [Matrix([[1, 0], [0, 1]]), Matrix([[0, 1], [0, 0]])])
            sage: C
            Finite-dimensional algebra of degree 2 over Complex Field with 53 bits of precision
            sage: TestSuite(C).run()

            sage: FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]])])
            Traceback (most recent call last):
            ...
            ValueError: input is not a multiplication table

            sage: D.<a,b> = FiniteDimensionalAlgebra(RR, [Matrix([[1, 0], [0, 1]]), Matrix([[0, 1], [-1, 0]])])
            sage: D.gens()
            (a, b)

            sage: E = FiniteDimensionalAlgebra(QQ, [Matrix([0])])
            sage: E.gens()
            (e,)
        """
    Element = FiniteDimensionalAlgebraElement
    from_base_ring: Incomplete
    def ngens(self):
        """
        Return the number of generators of ``self``, i.e., the degree
        of ``self`` over its base field.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])])
            sage: A.ngens()
            2
        """
    degree = ngens
    @cached_method
    def gen(self, i):
        """
        Return the `i`-th basis element of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])])
            sage: A.gen(0)
            e0
        """
    @cached_method
    def basis(self):
        """
        Return a list of the basis elements of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])])
            sage: A.basis()
            Finite family {0: e0, 1: e1}
        """
    def __iter__(self):
        """
        Iterate over the elements of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])])
            sage: list(A)
            [0, e0, 2*e0, e1, e0 + e1, 2*e0 + e1, 2*e1, e0 + 2*e1, 2*e0 + 2*e1]

        This is used in the :class:`Testsuite`'s when ``self`` is
        finite.
        """
    def table(self):
        """
        Return the multiplication table of ``self``, as a list of
        matrices for right multiplication by the basis elements.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])])
            sage: A.table()
            (
            [1 0]  [0 1]
            [0 1], [0 0]
            )
        """
    @cached_method
    def left_table(self):
        '''
        Return the list of matrices for left multiplication by the
        basis elements.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: T = B.left_table(); T
            (
            [1 0]  [ 0  1]
            [0 1], [-1  0]
            )

        We check immutability::

            sage: T[0] = "vandalized by h4xx0r"
            Traceback (most recent call last):
            ...
            TypeError: \'tuple\' object does not support item assignment
            sage: T[1][0] = [13, 37]
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead
             (i.e., use copy(M) to change a copy of M).
        '''
    def base_extend(self, F):
        """
        Return ``self`` base changed to the field ``F``.

        EXAMPLES::

            sage: C = FiniteDimensionalAlgebra(GF(2), [Matrix([1])])
            sage: k.<y> = GF(4)                                                         # needs sage.rings.finite_rings
            sage: C.base_extend(k)                                                      # needs sage.rings.finite_rings
            Finite-dimensional algebra of degree 1 over Finite Field in y of size 2^2
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(7), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [2, 3]])])
            sage: A.cardinality()
            49

            sage: B = FiniteDimensionalAlgebra(RR, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [2, 3]])])
            sage: B.cardinality()
            +Infinity

            sage: C = FiniteDimensionalAlgebra(RR, [])
            sage: C.cardinality()
            1
        """
    def ideal(self, gens=None, given_by_matrix: bool = False, side=None):
        """
        Return the right ideal of ``self`` generated by ``gens``.

        INPUT:

        - ``A`` -- a :class:`FiniteDimensionalAlgebra`

        - ``gens`` -- (default: ``None``) either an element of `A` or a
          list of elements of `A`, given as vectors, matrices, or
          FiniteDimensionalAlgebraElements.  If ``given_by_matrix`` is
          ``True``, then ``gens`` should instead be a matrix whose rows
          form a basis of an ideal of `A`.

        - ``given_by_matrix`` -- boolean (default: ``False``); if
          ``True``, no checking is done

        - ``side`` -- ignored but necessary for coercions

        The algebra ``A`` has to be in the category of associative algebras.

        EXAMPLES::

            sage: cat = Algebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: A.ideal(A([1,1]))
            Ideal (e0 + e1) of
             Finite-dimensional algebra of degree 2 over Finite Field of size 3
        """
    @cached_method
    def is_associative(self):
        """
        Return ``True`` if ``self`` is associative.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: A.is_associative()
            True

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,1]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,1], [0,0,0], [1,0,0]])])
            sage: B.is_associative()
            False

            sage: e = B.basis()
            sage: (e[1]*e[2])*e[2]==e[1]*(e[2]*e[2])
            False
        """
    @cached_method
    def is_commutative(self) -> bool:
        """
        Return ``True`` if ``self`` is commutative.

        EXAMPLES::

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B.is_commutative()
            True

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,1,0], [0,0,1]])])
            sage: C.is_commutative()
            False
        """
    def is_finite(self):
        """
        Return ``True`` if the cardinality of ``self`` is finite.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(7), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [2, 3]])])
            sage: A.is_finite()
            True

            sage: B = FiniteDimensionalAlgebra(RR, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [2, 3]])])
            sage: B.is_finite()
            False

            sage: C = FiniteDimensionalAlgebra(RR, [])
            sage: C.is_finite()
            True
        """
    @cached_method
    def is_unitary(self):
        """
        Return ``True`` if ``self`` has a two-sided multiplicative
        identity element.

        .. WARNING::

            This uses linear algebra; thus expect wrong results when
            the base ring is not a field.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [])
            sage: A.is_unitary()
            True

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: B.is_unitary()
            True

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[0,0], [0,0]]),
            ....:                                   Matrix([[0,0], [0,0]])])
            sage: C.is_unitary()
            False

            sage: D = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[1,0], [0,1]])])
            sage: D.is_unitary()
            False

            sage: E = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0],[1,0]]),
            ....:                                   Matrix([[0,1],[0,1]])])
            sage: E.is_unitary()
            False

            sage: F = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,1]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,1], [0,0,0], [1,0,0]])])
            sage: F.is_unitary()
            True

            sage: G = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,1]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [1,0,0]])])
            sage: G.is_unitary()  # Unique right identity, but no left identity.
            False
        """
    def is_zero(self):
        """
        Return ``True`` if ``self`` is the zero ring.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [])
            sage: A.is_zero()
            True

            sage: B = FiniteDimensionalAlgebra(GF(7), [Matrix([0])])
            sage: B.is_zero()
            False
        """
    def one(self):
        """
        Return the multiplicative identity element of ``self``, if it
        exists.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [])
            sage: A.one()
            0

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0], [0,1]]),
            ....:                                   Matrix([[0,1], [-1,0]])])
            sage: B.one()
            e0

            sage: C = FiniteDimensionalAlgebra(QQ, [Matrix([[0,0], [0,0]]),
            ....:                                   Matrix([[0,0], [0,0]])])
            sage: C.one()
            Traceback (most recent call last):
            ...
            TypeError: algebra is not unitary

            sage: D = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,1]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,1], [0,0,0], [1,0,0]])])
            sage: D.one()
            e0

            sage: E = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,1]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [1,0,0]])])
            sage: E.one()
            Traceback (most recent call last):
            ...
            TypeError: algebra is not unitary
        """
    def random_element(self, *args, **kwargs):
        """
        Return a random element of ``self``.

        Optional input parameters are propagated to the ``random_element``
        method of the underlying :class:`VectorSpace`.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])])
            sage: A.random_element()  # random
            e0 + 2*e1

            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])])
            sage: B.random_element(num_bound=1000)  # random
            215/981*e0 + 709/953*e1 + 931/264*e2
        """
    def quotient_map(self, ideal):
        """
        Return the quotient of ``self`` by ``ideal``.

        ``self`` has to be in the category of associative and unital algebras.

        INPUT:

        - ``ideal`` -- a :class:`FiniteDimensionalAlgebraIdeal`

        OUTPUT:

        - :class:`~sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_morphism.FiniteDimensionalAlgebraMorphism`;
          the quotient homomorphism

        EXAMPLES::

            sage: cat = Algebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: q0 = A.quotient_map(A.zero_ideal()); q0
            Morphism
             from Finite-dimensional algebra of degree 2 over Finite Field of size 3
               to Finite-dimensional algebra of degree 2 over Finite Field of size 3
             given by matrix
             [1 0]
             [0 1]
            sage: q1 = A.quotient_map(A.ideal(A.gen(1))); q1
            Morphism
             from Finite-dimensional algebra of degree 2 over Finite Field of size 3
               to Finite-dimensional algebra of degree 1 over Finite Field of size 3
             given by matrix
             [1]
             [0]
        """
    def maximal_ideal(self):
        """
        Compute the maximal ideal of the local algebra ``self``.

        .. NOTE::

            ``self`` has to be in the category of unitary, commutative
             and associative algebras as in the examples below. It must
             moreover be local (have a unique maximal ideal).

        OUTPUT:

        - :class:`~sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_ideal.FiniteDimensionalAlgebraIdeal`;
          the unique maximal ideal of ``self``.  If ``self`` is not a local
          algebra, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: A.maximal_ideal()                                                     # needs sage.rings.finite_rings
            Ideal (0, e1) of
             Finite-dimensional algebra of degree 2 over Finite Field of size 3

            sage: cat = CommutativeAlgebras(QQ).FiniteDimensional().WithBasis()
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])],
            ....:                              category=cat)
            sage: B.maximal_ideal()                                                     # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: algebra is not local
        """
    def primary_decomposition(self):
        """
        Return the primary decomposition of ``self``.

        .. NOTE::

            ``self`` has to be in the category of unitary, commutative
             and associative algebras as in the examples below.

        OUTPUT:

        - a list consisting of the quotient maps ``self`` -> `A`,
          with `A` running through the primary factors of ``self``

        EXAMPLES::

            sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])], category=cat)
            sage: A.primary_decomposition()                                             # needs sage.rings.finite_rings
            [Morphism
              from Finite-dimensional algebra of degree 2 over Finite Field of size 3
                to Finite-dimensional algebra of degree 2 over Finite Field of size 3
              given by matrix [1 0]
                              [0 1]]

            sage: cat = CommutativeAlgebras(QQ).FiniteDimensional().WithBasis()
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1,0,0], [0,1,0], [0,0,0]]),
            ....:                                   Matrix([[0,1,0], [0,0,0], [0,0,0]]),
            ....:                                   Matrix([[0,0,0], [0,0,0], [0,0,1]])], category=cat)
            sage: B.primary_decomposition()                                             # needs sage.libs.pari
            [Morphism
              from Finite-dimensional algebra of degree 3 over Rational Field
                to Finite-dimensional algebra of degree 1 over Rational Field
              given by matrix [0]
                              [0]
                              [1],
             Morphism
              from Finite-dimensional algebra of degree 3 over Rational Field
                to Finite-dimensional algebra of degree 2 over Rational Field
              given by matrix [1 0]
                              [0 1]
                              [0 0]]
        """
    def maximal_ideals(self):
        """
        Return a list consisting of all maximal ideals of ``self``.

        The algebra ``self`` has to be in the category of
        commutative, associative algebras.

        EXAMPLES::

            sage: cat = Algebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])], category=cat)
            sage: A.maximal_ideals()                                                    # needs sage.rings.finite_rings
            [Ideal (e1) of Finite-dimensional algebra of degree 2 over Finite Field of size 3]

            sage: cat = Algebras(QQ).FiniteDimensional().WithBasis()
            sage: B = FiniteDimensionalAlgebra(QQ, [], category=cat)
            sage: B.maximal_ideals()
            []
        """
