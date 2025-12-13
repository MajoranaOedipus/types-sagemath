from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.homset import RingHomset_generic as RingHomset_generic
from sage.rings.morphism import RingHomomorphism_im_gens as RingHomomorphism_im_gens
from sage.structure.element import Matrix as Matrix

class FiniteDimensionalAlgebraMorphism(RingHomomorphism_im_gens):
    """
    Create a morphism between two :class:`finite-dimensional algebras <FiniteDimensionalAlgebra>`.

    INPUT:

    - ``parent`` -- the parent homset

    - ``f`` -- matrix of the underlying `k`-linear map

    - ``unitary`` -- boolean (default: ``True``); if ``True`` and ``check``
      is also ``True``, raise a :exc:`ValueError` unless ``A`` and ``B`` are
      unitary and ``f`` respects unit elements

    - ``check`` -- boolean (default: ``True``); check whether the given
      `k`-linear map really defines a (not necessarily unitary)
      `k`-algebra homomorphism

    The algebras ``A`` and ``B`` must be defined over the same base field.

    EXAMPLES::

        sage: from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_morphism import FiniteDimensionalAlgebraMorphism
        sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
        ....:                                   Matrix([[0, 1], [0, 0]])])
        sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
        sage: H = Hom(A, B)
        sage: f = H(Matrix([[1], [0]]))
        sage: f.domain() is A
        True
        sage: f.codomain() is B
        True
        sage: f(A.basis()[0])
        e
        sage: f(A.basis()[1])
        0

    .. TODO:: An example illustrating unitary flag.
    """
    def __init__(self, parent, f, check: bool = True, unitary: bool = True) -> None:
        """
        TESTS::

            sage: from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_morphism import FiniteDimensionalAlgebraMorphism
            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])])
            sage: H = Hom(A, B)
            sage: phi = FiniteDimensionalAlgebraMorphism(H, Matrix([[1, 0]]))
            sage: TestSuite(phi).run(skip='_test_category')
        """
    def __call__(self, x):
        """
        TESTS::

            sage: cat = CommutativeAlgebras(QQ).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: I = A.maximal_ideal()                                                 # needs sage.libs.pari
            sage: q = A.quotient_map(I)                                                 # needs sage.libs.pari
            sage: q(0) == 0 and q(1) == 1                                               # needs sage.libs.pari
            True
        """
    def __eq__(self, other):
        """
        Check equality.

        TESTS::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])])
            sage: H = Hom(A, B)
            sage: phi = H(Matrix([[1, 0]]))
            sage: psi = H(Matrix([[1, 0]]))
            sage: phi == psi
            True
            sage: phi == H.zero()
            False
        """
    def __ne__(self, other):
        """
        Check not equals.

        TESTS::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])])
            sage: H = Hom(A, B)
            sage: phi = H(Matrix([[1, 0]]))
            sage: psi = H(Matrix([[1, 0]]))
            sage: phi != psi
            False
            sage: phi != H.zero()
            True
        """
    def matrix(self):
        """
        Return the matrix of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])])
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
            sage: M = Matrix([[1], [0]])
            sage: H = Hom(A, B)
            sage: f = H(M)
            sage: f.matrix() == M
            True
        """
    def inverse_image(self, I):
        """
        Return the inverse image of ``I`` under ``self``.

        INPUT:

        - ``I`` -- ``FiniteDimensionalAlgebraIdeal``, an ideal of ``self.codomain()``

        OUTPUT: :class:`FiniteDimensionalAlgebraIdeal`, the inverse image of `I` under ``self``

        EXAMPLES::

            sage: cat = CommutativeAlgebras(QQ).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: I = A.maximal_ideal()                                                 # needs sage.libs.pari
            sage: q = A.quotient_map(I)                                                 # needs sage.libs.pari
            sage: B = q.codomain()                                                      # needs sage.libs.pari
            sage: q.inverse_image(B.zero_ideal()) == I                                  # needs sage.libs.pari
            True
        """

class FiniteDimensionalAlgebraHomset(RingHomset_generic):
    """
    Set of morphisms between two finite-dimensional algebras.
    """
    @cached_method
    def zero(self):
        """
        Construct the zero morphism of ``self``.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])])
            sage: H = Hom(A, B)
            sage: H.zero()
            Morphism from Finite-dimensional algebra of degree 1 over Rational Field to
             Finite-dimensional algebra of degree 2 over Rational Field given by matrix
            [0 0]
        """
    def __call__(self, f, check: bool = True, unitary: bool = True):
        """
        Construct a homomorphism.

        .. TODO::

            Implement taking generator images and converting them to a matrix.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebra(QQ, [Matrix([1])])
            sage: B = FiniteDimensionalAlgebra(QQ, [Matrix([[1, 0], [0, 1]]),
            ....:                                   Matrix([[0, 1], [0, 0]])])
            sage: H = Hom(A, B)
            sage: H(Matrix([[1, 0]]))
            Morphism from Finite-dimensional algebra of degree 1 over Rational Field to
             Finite-dimensional algebra of degree 2 over Rational Field given by matrix
            [1 0]
        """
