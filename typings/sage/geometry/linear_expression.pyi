from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LinearExpression(ModuleElement):
    """
    A linear expression.

    A linear expression is just a linear polynomial in some (fixed)
    variables.

    EXAMPLES::

        sage: from sage.geometry.linear_expression import LinearExpressionModule
        sage: L.<x,y,z> = LinearExpressionModule(QQ)
        sage: m = L([1, 2, 3], 4); m
        x + 2*y + 3*z + 4
        sage: m2 = L([(1, 2, 3), 4]); m2
        x + 2*y + 3*z + 4
        sage: m3 = L([4, 1, 2, 3]); m3   # note: constant is first in single-tuple notation
        x + 2*y + 3*z + 4
        sage: m == m2
        True
        sage: m2 == m3
        True
        sage: L.zero()
        0*x + 0*y + 0*z + 0
        sage: a = L([12, 2/3, -1], -2)
        sage: a - m
        11*x - 4/3*y - 4*z - 6
        sage: LZ.<x,y,z> = LinearExpressionModule(ZZ)
        sage: a - LZ([2, -1, 3], 1)
        10*x + 5/3*y - 4*z - 3
    """
    def __init__(self, parent, coefficients, constant, check: bool = True) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: linear = L([1, 2, 3], 4)   # indirect doctest
            sage: linear.parent() is L
            True

            sage: TestSuite(linear).run()
        """
    def A(self):
        """
        Return the coefficient vector.

        OUTPUT: the coefficient vector of the linear expression

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: linear = L([1, 2, 3], 4);  linear
            x + 2*y + 3*z + 4
            sage: linear.A()
            (1, 2, 3)
            sage: linear.b()
            4
        """
    def b(self):
        """
        Return the constant term.

        OUTPUT: the constant term of the linear expression

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: linear = L([1, 2, 3], 4);  linear
            x + 2*y + 3*z + 4
            sage: linear.A()
            (1, 2, 3)
            sage: linear.b()
            4
        """
    constant_term = b
    def coefficients(self):
        """
        Return all coefficients.

        OUTPUT:

        The constant (as first entry) and coefficients of the linear
        terms (as subsequent entries) in a list.

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: linear = L([1, 2, 3], 4);  linear
            x + 2*y + 3*z + 4
            sage: linear.coefficients()
            [4, 1, 2, 3]
        """
    dense_coefficient_list = coefficients
    def monomial_coefficients(self, copy: bool = True):
        """
        Return a dictionary whose keys are indices of basis elements in
        the support of ``self`` and whose values are the corresponding
        coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: linear = L([1, 2, 3], 4)
            sage: sorted(linear.monomial_coefficients().items(), key=lambda x: str(x[0]))
            [(0, 1), (1, 2), (2, 3), ('b', 4)]
        """
    def change_ring(self, base_ring):
        """
        Change the base ring of this linear expression.

        INPUT:

        - ``base_ring`` -- a ring; the new base ring

        OUTPUT: a new linear expression over the new base ring

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: a = x + 2*y + 3*z + 4;  a
            x + 2*y + 3*z + 4
            sage: a.change_ring(RDF)
            1.0*x + 2.0*y + 3.0*z + 4.0
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x> = LinearExpressionModule(QQ)
            sage: hash(L([0,1])) == hash((1,))
            True
        """
    def evaluate(self, point):
        """
        Evaluate the linear expression.

        INPUT:

        - ``point`` -- list/tuple/iterable of coordinates; the
          coordinates of a point

        OUTPUT: the linear expression `Ax + b` evaluated at the point `x`

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y> = LinearExpressionModule(QQ)
            sage: ex = 2*x + 3* y + 4
            sage: ex.evaluate([1,1])
            9
            sage: ex([1,1])    # syntactic sugar
            9
            sage: ex([pi, e])                                                           # needs sage.symbolic
            2*pi + 3*e + 4
        """
    __call__ = evaluate

class LinearExpressionModule(Parent, UniqueRepresentation):
    """
    The module of linear expressions.

    This is the module of linear polynomials which is the parent for
    linear expressions.

    EXAMPLES::

        sage: from sage.geometry.linear_expression import LinearExpressionModule
        sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
        sage: L
        Module of linear expressions in variables x, y, z over Rational Field
        sage: L.an_element()
        x + 0*y + 0*z + 0
    """
    Element = LinearExpression
    def __init__(self, base_ring, names=...) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: type(L)
            <class 'sage.geometry.linear_expression.LinearExpressionModule_with_category'>
            sage: L.base_ring()
            Rational Field

            sage: TestSuite(L).run()

            sage: L = LinearExpressionModule(QQ)
            sage: TestSuite(L).run()
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: list(L.basis())
            [x + 0*y + 0*z + 0,
             0*x + y + 0*z + 0,
             0*x + 0*y + z + 0,
             0*x + 0*y + 0*z + 1]
        """
    @cached_method
    def ngens(self):
        """
        Return the number of linear variables.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: L.ngens()
            3
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        OUTPUT: a tuple of linear expressions, one for each linear variable

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: L.gens()
            (x + 0*y + 0*z + 0, 0*x + y + 0*z + 0, 0*x + 0*y + z + 0)
        """
    def gen(self, i):
        """
        Return the `i`-th generator.

        INPUT:

        - ``i`` -- integer

        OUTPUT: a linear expression

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: L.gen(0)
            x + 0*y + 0*z + 0
        """
    def random_element(self):
        """
        Return a random element.

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L.<x,y,z> = LinearExpressionModule(QQ)
            sage: L.random_element() in L
            True
        """
    @cached_method
    def ambient_module(self):
        """
        Return the ambient module.

        .. SEEALSO::

            :meth:`ambient_vector_space`

        OUTPUT:

        The domain of the linear expressions as a free module over the
        base ring.

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: L.ambient_module()
            Vector space of dimension 3 over Rational Field
            sage: M = LinearExpressionModule(ZZ, ('r', 's'))
            sage: M.ambient_module()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: M.ambient_vector_space()
            Vector space of dimension 2 over Rational Field
        """
    @cached_method
    def ambient_vector_space(self):
        """
        Return the ambient vector space.

        .. SEEALSO::

            :meth:`ambient_module`

        OUTPUT:

        The vector space (over the fraction field of the base ring)
        where the linear expressions live.

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: L = LinearExpressionModule(QQ, ('x', 'y', 'z'))
            sage: L.ambient_vector_space()
            Vector space of dimension 3 over Rational Field
            sage: M = LinearExpressionModule(ZZ, ('r', 's'))
            sage: M.ambient_module()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: M.ambient_vector_space()
            Vector space of dimension 2 over Rational Field
        """
    def change_ring(self, base_ring):
        """
        Return a new module with a changed base ring.

        INPUT:

        - ``base_ring`` -- a ring; the new base ring

        OUTPUT: a new linear expression over the new base ring

        EXAMPLES::

            sage: from sage.geometry.linear_expression import LinearExpressionModule
            sage: M.<y> = LinearExpressionModule(ZZ)
            sage: L = M.change_ring(QQ);  L
            Module of linear expressions in variable y over Rational Field

        TESTS::

            sage: L.change_ring(QQ) is L
            True
        """
