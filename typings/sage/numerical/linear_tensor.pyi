from sage.misc.cachefunc import cached_function as cached_function
from sage.numerical.linear_functions import LinearFunction as LinearFunction, LinearFunctionsParent_class as LinearFunctionsParent_class
from sage.numerical.linear_tensor_element import LinearTensor as LinearTensor
from sage.structure.parent import Parent as Parent

def is_LinearTensor(x):
    """
    Test whether ``x`` is a tensor product of linear functions with a
    free module.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: p = MixedIntegerLinearProgram()
        sage: x = p.new_variable(nonnegative=False)
        sage: from sage.numerical.linear_tensor import is_LinearTensor
        sage: is_LinearTensor(x[0] - 2*x[2])
        doctest:warning...
        DeprecationWarning: The function is_LinearTensor is deprecated;
        use 'isinstance(..., LinearTensor)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        False
        sage: is_LinearTensor('a string')
        False
    """
@cached_function
def LinearTensorParent(free_module_parent, linear_functions_parent):
    """
    Return the parent for the tensor product over the common ``base_ring``.

    The output is cached, so only a single parent is ever constructed
    for a given base ring.

    INPUT:

    - ``free_module_parent`` -- a free module, like vector or matrix space

    - ``linear_functions_parent`` -- linear functions; the linear functions
      parent

    OUTPUT:

    The parent of the tensor product of a free module and linear
    functions over a common base ring.

    EXAMPLES::

        sage: from sage.numerical.linear_functions import LinearFunctionsParent
        sage: from sage.numerical.linear_tensor import LinearTensorParent
        sage: LinearTensorParent(QQ^3, LinearFunctionsParent(QQ))
        Tensor product of Vector space of dimension 3 over Rational Field and Linear functions over Rational Field

        sage: LinearTensorParent(ZZ^3, LinearFunctionsParent(QQ))
        Traceback (most recent call last):
        ...
        ValueError: base rings must match
    """

class LinearTensorParent_class(Parent):
    """
    The parent for all linear functions over a fixed base ring.

    .. warning::

        You should use :func:`LinearTensorParent` to construct
        instances of this class.

    INPUT/OUTPUT: see :func:`LinearTensorParent`

    EXAMPLES::

        sage: from sage.numerical.linear_tensor import LinearTensorParent_class
        sage: LinearTensorParent_class
        <class 'sage.numerical.linear_tensor.LinearTensorParent_class'>
    """
    Element = LinearTensor
    def __init__(self, free_module, linear_functions) -> None:
        """
        The Python constructor.

        INPUT/OUTPUT: see :func:`LinearTensorParent`

        TESTS::

            sage: from sage.numerical.linear_functions import LinearFunctionsParent
            sage: LinearFunctionsParent(RDF).tensor(RDF^2)
            Tensor product of Vector space of dimension 2 over Real Double
            Field and Linear functions over Real Double Field
        """
    def free_module(self):
        """
        Return the linear functions.

        See also :meth:`free_module`.

        OUTPUT:

        Parent of the linear functions, one of the factors in the
        tensor product construction.

        EXAMPLES::

            sage: mip.<x> = MixedIntegerLinearProgram()
            sage: lt = x[0] * vector(RDF, [1,2])
            sage: lt.parent().free_module()
            Vector space of dimension 2 over Real Double Field
            sage: lt.parent().free_module() is vector(RDF, [1,2]).parent()
            True
        """
    def is_vector_space(self):
        """
        Return whether the free module is a vector space.

        OUTPUT: boolean; whether the :meth:`free_module` factor in the tensor
        product is a vector space

        EXAMPLES::

            sage: mip = MixedIntegerLinearProgram()
            sage: LF = mip.linear_functions_parent()
            sage: LF.tensor(RDF^2).is_vector_space()
            True
            sage: LF.tensor(RDF^(2,2)).is_vector_space()
            False
        """
    def is_matrix_space(self):
        """
        Return whether the free module is a matrix space.

        OUTPUT: boolean; whether the :meth:`free_module` factor in the tensor
        product is a matrix space

        EXAMPLES::

            sage: mip = MixedIntegerLinearProgram()
            sage: LF = mip.linear_functions_parent()
            sage: LF.tensor(RDF^2).is_matrix_space()
            False
            sage: LF.tensor(RDF^(2,2)).is_matrix_space()
            True
        """
    def linear_functions(self):
        """
        Return the linear functions.

        See also :meth:`free_module`.

        OUTPUT:

        Parent of the linear functions, one of the factors in the
        tensor product construction.

        EXAMPLES::

            sage: mip.<x> = MixedIntegerLinearProgram()
            sage: lt = x[0] * vector([1,2])
            sage: lt.parent().linear_functions()
            Linear functions over Real Double Field
            sage: lt.parent().linear_functions() is mip.linear_functions_parent()
            True
        """
