from sage.algebras.lie_algebras.lie_algebra import FinitelyGeneratedLieAlgebra as FinitelyGeneratedLieAlgebra
from sage.algebras.lie_algebras.lie_algebra_element import StructureCoefficientsElement as StructureCoefficientsElement
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import FreeModule as FreeModule
from sage.sets.family import Family as Family
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators, standardize_names_index_set as standardize_names_index_set

class LieAlgebraWithStructureCoefficients(FinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    A Lie algebra with a set of specified structure coefficients.

    The structure coefficients are specified as a dictionary `d` whose
    keys are pairs of basis indices, and whose values are
    dictionaries which in turn are indexed by basis indices. The value
    of `d` at a pair `(u, v)` of basis indices is the dictionary whose
    `w`-th entry (for `w` a basis index) is the coefficient of `b_w`
    in the Lie bracket `[b_u, b_v]` (where `b_x` means the basis
    element with index `x`).

    INPUT:

    - ``R`` -- a ring, to be used as the base ring

    - ``s_coeff`` -- dictionary, indexed by pairs of basis indices
      (see below), and whose values are dictionaries which are
      indexed by (single) basis indices and whose values are elements
      of `R`

    - ``names`` -- list or tuple of strings

    - ``index_set`` -- (default: ``names``) list or tuple of hashable
      and comparable elements

    OUTPUT:

    A Lie algebra over ``R`` which (as an `R`-module) is free with
    a basis indexed by the elements of ``index_set``. The `i`-th
    basis element is displayed using the name ``names[i]``.
    If we let `b_i` denote this `i`-th basis element, then the Lie
    bracket is given by the requirement that the `b_k`-coefficient
    of `[b_i, b_j]` is ``s_coeff[(i, j)][k]`` if
    ``s_coeff[(i, j)]`` exists, otherwise ``-s_coeff[(j, i)][k]``
    if ``s_coeff[(j, i)]`` exists, otherwise `0`.

    EXAMPLES:

    We create the Lie algebra of `\\QQ^3` under the Lie bracket defined
    by `\\times` (cross-product)::

        sage: L = LieAlgebra(QQ, 'x,y,z', {('x','y'): {'z':1}, ('y','z'): {'x':1}, ('z','x'): {'y':1}})
        sage: (x,y,z) = L.gens()
        sage: L.bracket(x, y)
        z
        sage: L.bracket(y, x)
        -z

    TESTS:

    We can input structure coefficients that fail the Jacobi
    identity, but the test suite will call us out on it::

        sage: Fake = LieAlgebra(QQ, 'x,y,z', {('x','y'):{'z':3}, ('y','z'):{'z':1}, ('z','x'):{'y':1}})
        sage: TestSuite(Fake).run()
        Failure in _test_jacobi_identity:
        ...

    Old tests !!!!!placeholder for now!!!!!::

        sage: L = LieAlgebra(QQ, 'x,y', {('x','y'):{'x':1}})
        sage: L.basis()
        Finite family {'x': x, 'y': y}
    """
    @staticmethod
    def __classcall_private__(cls, R, s_coeff, names=None, index_set=None, **kwds):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: L1 = LieAlgebra(QQ, 'x,y', {('x','y'): {'x':1}})
            sage: L2 = LieAlgebra(QQ, 'x,y', {('y','x'): {'x':-1}})
            sage: L1 is L2
            True

        Check that we convert names to the indexing set::

            sage: L = LieAlgebra(QQ, 'x,y,z', {('x','y'): {'z':1}, ('y','z'): {'x':1}, ('z','x'): {'y':1}}, index_set=list(range(3)))
            sage: (x,y,z) = L.gens()
            sage: L[x,y]
            L[2]
        """
    def __init__(self, R, s_coeff, names, index_set, category=None, prefix=None, bracket=None, latex_bracket=None, string_quotes=None, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y', {('x','y'): {'x':1}})
            sage: TestSuite(L).run()
        """
    def structure_coefficients(self, include_zeros: bool = False):
        """
        Return the dictionary of structure coefficients of ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z', {('x','y'): {'x':1}})
            sage: L.structure_coefficients()
            Finite family {('x', 'y'): x}
            sage: S = L.structure_coefficients(True); S
            Finite family {('x', 'y'): x, ('x', 'z'): 0, ('y', 'z'): 0}
            sage: S['x','z'].parent() is L
            True

        TESTS:

        Check that :issue:`23373` is fixed::

            sage: L = lie_algebras.sl(QQ, 2)
            sage: sorted(L.structure_coefficients(True), key=str)
            [-2*E[-alpha[1]], -2*E[alpha[1]], h1]
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y', {('x','y'):{'x':1}})
            sage: L.dimension()
            2
        """
    def module(self, sparse: bool = True):
        """
        Return ``self`` as a free module.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'):{'z':1}})
            sage: L.module()
            Sparse vector space of dimension 3 over Rational Field
        """
    @cached_method
    def zero(self):
        """
        Return the element `0` in ``self``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: L.zero()
            0
        """
    def monomial(self, k):
        """
        Return the monomial indexed by ``k``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: L.monomial('x')
            x
        """
    def term(self, k, c=None):
        """
        Return the term indexed by ``i`` with coefficient ``c``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: L.term('x', 4)
            4*x
        """
    def from_vector(self, v, order=None, coerce: bool = True):
        """
        Return an element of ``self`` from the vector ``v``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: L.from_vector([1, 2, -2])
            x + 2*y - 2*z
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.three_dimensional(QQ, 4, 1, -1, 2)
            sage: L.some_elements()
            [X, Y, Z, X + Y + Z]
        """
    def change_ring(self, R):
        """
        Return a Lie algebra with identical structure coefficients over ``R``.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(ZZ, {('x','y'): {'z':1}})
            sage: L.structure_coefficients()
            Finite family {('x', 'y'): z}
            sage: LQQ = L.change_ring(QQ)
            sage: LQQ.structure_coefficients()
            Finite family {('x', 'y'): z}
            sage: LSR = LQQ.change_ring(SR)                                             # needs sage.symbolic
            sage: LSR.structure_coefficients()                                          # needs sage.symbolic
            Finite family {('x', 'y'): z}
        """
    class Element(StructureCoefficientsElement): ...
