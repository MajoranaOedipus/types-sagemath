import sage.structure.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class LinearTensor(sage.structure.element.ModuleElement):
    """LinearTensor(parent, f)

    File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 35)

    A linear function tensored with a free module.

    .. warning::

        You should never instantiate :class:`LinearTensor`
        manually. Use the element constructor in the parent
        instead.

    EXAMPLES::

        sage: parent = MixedIntegerLinearProgram().linear_functions_parent().tensor(RDF^2)
        sage: parent({0: [1,2], 3: [-7,-8]})
        (1.0, 2.0)*x_0 + (-7.0, -8.0)*x_3"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 52)

                Constructor taking a dictionary as its argument.

                INPUT:

                - ``parent`` -- the parent
                  :class:`~sage.numerical.linear_tensor.LinearTensorParent_class`

                - ``f`` -- a linear function tensored by a free module is
                  represented as a dictionary. The values are the coefficient
                  (free module elements) of the variable represented by the
                  keys. The key ``-1`` corresponds to the constant term.

                EXAMPLES:

                With a dictionary::

                    sage: LT = MixedIntegerLinearProgram().linear_functions_parent().tensor(RDF^2)
                    sage: LT({0: [1,2], 3: [-7,-8]})
                    (1.0, 2.0)*x_0 + (-7.0, -8.0)*x_3

                    sage: TestSuite(LT).run(skip=['_test_an_element', '_test_elements_eq_reflexive',
                    ....:     '_test_elements_eq_symmetric', '_test_elements_eq_transitive',
                    ....:     '_test_elements_neq', '_test_additive_associativity',
                    ....:     '_test_elements', '_test_pickling', '_test_zero'])
        """
    def coefficient(self, x) -> Any:
        """LinearTensor.coefficient(self, x)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 127)

        Return one of the coefficients.

        INPUT:

        - ``x`` -- a linear variable or an integer. If an integer `i`
          is passed, then `x_i` is used as linear variable. Pass
          ``-1`` for the constant term.

        OUTPUT:

        A constant, that is, an element of the free module factor. The
        coefficient of ``x`` in the linear function.

        EXAMPLES::

            sage: mip.<b> = MixedIntegerLinearProgram()
            sage: lt = vector([1,2]) * b[3] + vector([4,5]) * b[0] - 5;  lt
            (-5.0, -5.0) + (1.0, 2.0)*x_0 + (4.0, 5.0)*x_1
            sage: lt.coefficient(b[3])
            (1.0, 2.0)
            sage: lt.coefficient(0)      # x_0 is b[3]
            (1.0, 2.0)
            sage: lt.coefficient(4)
            (0.0, 0.0)
            sage: lt.coefficient(-1)
            (-5.0, -5.0)

        TESTS::

            sage: lt.coefficient(b[3] + b[4])
            Traceback (most recent call last):
            ...
            ValueError: x is a sum, must be a single variable
            sage: lt.coefficient(2*b[3])
            Traceback (most recent call last):
            ...
            ValueError: x must have a unit coefficient
            sage: mip.<q> = MixedIntegerLinearProgram(solver='ppl')
            sage: lt.coefficient(q[0])
            Traceback (most recent call last):
            ...
            ValueError: x is from a different linear functions module"""
    @overload
    def dict(self) -> Any:
        """LinearTensor.dict(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 107)

        Return the dictionary corresponding to the tensor product.

        OUTPUT:

        The linear function tensor product is represented as a
        dictionary. The value are the coefficient (free module
        elements) of the variable represented by the keys (which are
        integers). The key ``-1`` corresponds to the constant term.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram().linear_functions_parent().tensor(RDF^2)
            sage: lt = p({0:[1,2], 3:[4,5]})
            sage: lt.dict()
            {0: (1.0, 2.0), 3: (4.0, 5.0)}"""
    @overload
    def dict(self) -> Any:
        """LinearTensor.dict(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 107)

        Return the dictionary corresponding to the tensor product.

        OUTPUT:

        The linear function tensor product is represented as a
        dictionary. The value are the coefficient (free module
        elements) of the variable represented by the keys (which are
        integers). The key ``-1`` corresponds to the constant term.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram().linear_functions_parent().tensor(RDF^2)
            sage: lt = p({0:[1,2], 3:[4,5]})
            sage: lt.dict()
            {0: (1.0, 2.0), 3: (4.0, 5.0)}"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, indices) -> Any:
        """LinearTensor.__getitem__(self, indices)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 83)

        Return the linear function component with given tensor indices.

        INPUT:

        - ``indices`` -- one or more integers. The basis indices of
          the free module. E.g. a single integer for vectors, two for
          matrices.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram().linear_functions_parent().tensor(RDF^2)
            sage: lt = p({0:[1,2], 3:[4,5]});  lt
            (1.0, 2.0)*x_0 + (4.0, 5.0)*x_3
            sage: lt[0]
            x_0 + 4*x_3
            sage: lt[1]
            2*x_0 + 5*x_3"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LinearTensor.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_tensor_element.pyx (starting at line 426)

        Return a hash.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: lt0 = p[0] * vector([1,2])
            sage: hash(lt0)   # random output
            103987752
            sage: d = {}
            sage: d[lt0] = 3

        Since we hash by ``id()``, linear functions and constraints are
        only considered equal for sets and dicts if they are the same
        object::

            sage: f = p[0] * vector([1])
            sage: g = p[0] * vector([1])
            sage: set([f, f])
            {((1.0))*x_0}
            sage: set([f, g])
            {((1.0))*x_0, ((1.0))*x_0}
            sage: len(set([f, f+1]))
            2

            sage: d = {}
            sage: d[f] = 123
            sage: d[g] = 456
            sage: len(list(d))
            2"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
