from .finite_dimensional_algebra_element import FiniteDimensionalAlgebraElement as FiniteDimensionalAlgebraElement
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.structure.element import Matrix as Matrix, parent as parent
from sage.structure.richcmp import op_EQ as op_EQ, op_GE as op_GE, op_GT as op_GT, op_LE as op_LE, op_LT as op_LT, op_NE as op_NE

class FiniteDimensionalAlgebraIdeal(Ideal_generic):
    """
    An ideal of a :class:`FiniteDimensionalAlgebra`.

    INPUT:

    - ``A`` -- a finite-dimensional algebra
    - ``gens`` -- the generators of this ideal
    - ``given_by_matrix`` -- boolean (default: ``False``); whether the basis
      matrix is given by ``gens``

    EXAMPLES::

        sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
        sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
        ....:                                      Matrix([[0, 1], [0, 0]])],
        ....:                              category=cat)
        sage: A.ideal(A([0,1]))
        Ideal (e1) of Finite-dimensional algebra of degree 2 over Finite Field of size 3
    """
    def __init__(self, A, gens=None, given_by_matrix: bool = False) -> None:
        """
        EXAMPLES::

            sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: I = A.ideal(A([0,1]))
            sage: TestSuite(I).run(skip='_test_category')  # Currently ideals are not using the category framework
        """
    def __contains__(self, elt) -> bool:
        """
        EXAMPLES::

            sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: J = A.ideal(A([0,1]))
            sage: A([0,1]) in J
            True
            sage: A([1,0]) in J
            False
        """
    def basis_matrix(self):
        """
        Return the echelonized matrix whose rows form a basis of ``self``.

        EXAMPLES::

            sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: I = A.ideal(A([1,1]))
            sage: I.basis_matrix()
            [1 0]
            [0 1]
        """
    @cached_method
    def vector_space(self):
        """
        Return ``self`` as a vector space.

        EXAMPLES::

            sage: cat = CommutativeAlgebras(GF(3)).FiniteDimensional().WithBasis()
            sage: A = FiniteDimensionalAlgebra(GF(3), [Matrix([[1, 0], [0, 1]]),
            ....:                                      Matrix([[0, 1], [0, 0]])],
            ....:                              category=cat)
            sage: I = A.ideal(A([1,1]))
            sage: I.vector_space()
            Vector space of degree 2 and dimension 2 over Finite Field of size 3
            Basis matrix:
            [1 0]
            [0 1]
        """
