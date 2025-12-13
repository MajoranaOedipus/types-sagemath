from sage.misc.cachefunc import cached_function as cached_function
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent

def is_LinearTensorConstraint(x):
    """
    Test whether ``x`` is a constraint on module-valued linear functions.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: mip.<x> = MixedIntegerLinearProgram()
        sage: vector_ieq = (x[0] * vector([1,2]) <= x[1] * vector([2,3]))
        sage: from sage.numerical.linear_tensor_constraints import is_LinearTensorConstraint
        sage: is_LinearTensorConstraint(vector_ieq)
        doctest:warning...
        DeprecationWarning: The function is_LinearTensorConstraint is deprecated;
        use 'isinstance(..., LinearTensorConstraint)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        True
        sage: is_LinearTensorConstraint('a string')
        False
    """
@cached_function
def LinearTensorConstraintsParent(linear_functions_parent):
    """
    Return the parent for linear functions over ``base_ring``.

    The output is cached, so only a single parent is ever constructed
    for a given base ring.

    INPUT:

    - ``linear_functions_parent`` -- a
      :class:`~sage.numerical.linear_functions.LinearFunctionsParent_class`. The
      type of linear functions that the constraints are made out of.

    OUTPUT: the parent of the linear constraints with the given linear functions

    EXAMPLES::

        sage: from sage.numerical.linear_functions import LinearFunctionsParent
        sage: from sage.numerical.linear_tensor import LinearTensorParent
        sage: from sage.numerical.linear_tensor_constraints import         ....:     LinearTensorConstraintsParent, LinearTensorConstraintsParent
        sage: LF = LinearFunctionsParent(QQ)
        sage: LT = LinearTensorParent(QQ^2, LF)
        sage: LinearTensorConstraintsParent(LT)
        Linear constraints in the tensor product of Vector space of dimension 2
        over Rational Field and Linear functions over Rational Field
    """

class LinearTensorConstraint(Element):
    '''
    Formal constraint involving two module-valued linear functions.

    .. NOTE::

        In the code, we use "linear tensor" as abbreviation for the
        tensor product (over the common base ring) of a :mod:`linear
        function <sage.numerical.linear_functions>` and a free module
        like a vector/matrix space.

    .. warning::

        This class has no reason to be instantiated by the user, and
        is meant to be used by instances of
        :class:`MixedIntegerLinearProgram`.

    INPUT:

    - ``parent`` -- the parent, a
      :class:`LinearTensorConstraintsParent_class`

    - ``lhs``, ``rhs`` -- two
      :class:`sage.numerical.linear_tensor_element.LinearTensor`. The
      left and right hand side of the constraint (in)equality.

    - ``equality`` -- boolean (default: ``False``); whether the
      constraint is an equality.  If ``False``, it is a ``<=``
      inequality.

    EXAMPLES::

        sage: mip.<b> = MixedIntegerLinearProgram()
        sage: (b[2]+2*b[3]) * vector([1,2]) <= b[8] * vector([2,3]) - 5
        (1.0, 2.0)*x_0 + (2.0, 4.0)*x_1 <= (-5.0, -5.0) + (2.0, 3.0)*x_2
    '''
    def __init__(self, parent, lhs, rhs, equality) -> None:
        """
        Constructor for ``LinearTensorConstraint``.

        INPUT:

        See :class:`LinearTensorConstraint`.

        EXAMPLES::

            sage: mip.<b> = MixedIntegerLinearProgram()
            sage: b[2] * vector([1,2]) + 2*b[3] <= 0
            (1.0, 2.0)*x_0 + (2.0, 2.0)*x_1 <= (0.0, 0.0)
        """
    def is_equation(self):
        """
        Whether the constraint is a chained equation.

        OUTPUT: boolean

        EXAMPLES::

            sage: mip.<b> = MixedIntegerLinearProgram()
            sage: (b[0] * vector([1,2]) == 0).is_equation()
            True
            sage: (b[0] * vector([1,2]) >= 0).is_equation()
            False
        """
    def is_less_or_equal(self):
        """
        Whether the constraint is a chained less-or_equal inequality.

        OUTPUT: boolean

        EXAMPLES::

            sage: mip.<b> = MixedIntegerLinearProgram()
            sage: (b[0] * vector([1,2]) == 0).is_less_or_equal()
            False
            sage: (b[0] * vector([1,2]) >= 0).is_less_or_equal()
            True
        """
    def lhs(self):
        """
        Return the left side of the (in)equality.

        OUTPUT:

        Instance of
        :class:`sage.numerical.linear_tensor_element.LinearTensor`. A
        linear function valued in a free module.

        EXAMPLES::

            sage: mip.<x> = MixedIntegerLinearProgram()
            sage: (x[0] * vector([1,2]) == 0).lhs()
            (1.0, 2.0)*x_0
        """
    def rhs(self):
        """
        Return the right side of the (in)equality.

        OUTPUT:

        Instance of
        :class:`sage.numerical.linear_tensor_element.LinearTensor`. A
        linear function valued in a free module.

        EXAMPLES::

            sage: mip.<x> = MixedIntegerLinearProgram()
            sage: (x[0] * vector([1,2]) == 0).rhs()
            (0.0, 0.0)
        """

class LinearTensorConstraintsParent_class(Parent):
    """
    Parent for :class:`LinearTensorConstraint`.

    .. warning::

        This class has no reason to be instantiated by the user, and
        is meant to be used by instances of
        :class:`MixedIntegerLinearProgram`. Also, use the
        :func:`LinearTensorConstraintsParent` factory function.

    INPUT/OUTPUT: see :func:`LinearTensorConstraintsParent`

    EXAMPLES::

        sage: p = MixedIntegerLinearProgram()
        sage: LT = p.linear_functions_parent().tensor(RDF^2);  LT
        Tensor product of Vector space of dimension 2 over Real Double
        Field and Linear functions over Real Double Field
        sage: from sage.numerical.linear_tensor_constraints import LinearTensorConstraintsParent
        sage: LTC = LinearTensorConstraintsParent(LT);  LTC
        Linear constraints in the tensor product of Vector space of
        dimension 2 over Real Double Field and Linear functions over
        Real Double Field
        sage: type(LTC)
        <class 'sage.numerical.linear_tensor_constraints.LinearTensorConstraintsParent_class'>
    """
    Element = LinearTensorConstraint
    def __init__(self, linear_tensor_parent) -> None:
        """
        The Python constructor.

        INPUT:

        - ``linear_tensor_parent`` -- instance of
          :class:`LinearTensorParent_class`

        TESTS::

            sage: from sage.numerical.linear_functions import LinearFunctionsParent
            sage: LF = LinearFunctionsParent(RDF)
            sage: from sage.numerical.linear_tensor import LinearTensorParent
            sage: LT = LinearTensorParent(RDF^2, LF)
            sage: from sage.numerical.linear_tensor_constraints import LinearTensorConstraintsParent
            sage: LinearTensorConstraintsParent(LT)
            Linear constraints in the tensor product of Vector space of
            dimension 2 over Real Double Field and Linear functions over
            Real Double Field
        """
    def linear_tensors(self):
        """
        Return the parent for the linear functions.

        OUTPUT: instance of :class:`sage.numerical.linear_tensor.LinearTensorParent_class`

        EXAMPLES::

            sage: mip.<x> = MixedIntegerLinearProgram()
            sage: ieq = (x[0] * vector([1,2]) >= 0)
            sage: ieq.parent().linear_tensors()
            Tensor product of Vector space of dimension 2 over Real Double
            Field and Linear functions over Real Double Field
        """
    def linear_functions(self):
        """
        Return the parent for the linear functions.

        OUTPUT: instance of :class:`sage.numerical.linear_functions.LinearFunctionsParent_class`

        EXAMPLES::

            sage: mip.<x> = MixedIntegerLinearProgram()
            sage: ieq = (x[0] * vector([1,2]) >= 0)
            sage: ieq.parent().linear_functions()
            Linear functions over Real Double Field
        """
