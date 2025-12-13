from typing import Any, ClassVar

class CompiledPolynomialFunction:
    """CompiledPolynomialFunction(coeffs, algorithm='binary')

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 21)

    Build a reasonably optimized directed acyclic graph representation
    for a given polynomial.  A ``CompiledPolynomialFunction`` is callable from
    python, though it is a little faster to call the eval function from
    pyrex.

    This class is not intended to be called by a user, rather, it is
    intended to improve the performance of immutable polynomial objects.

    .. TODO::

        - Recursive calling
        - Faster casting of coefficients / argument
        - Multivariate polynomials
        - Cython implementation of Pippenger's Algorithm that doesn't
          depend heavily upon dicts.
        - Computation of parameter sequence suggested by Pippenger
        - Univariate exponentiation can use Brauer's method to improve
          extremely sparse polynomials of very high degree"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, coeffs, algorithm=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 43)

                Compiles a polynomial into an evaluation DAG representation which
                is at least as optimal as using Horner\'s Rule.  For polynomials
                which have a relatively large number of zero coefficients, the
                improvement over Horner\'s Rule grows significantly.

                Here is a rough description of the algorithm.  Actual
                implementation differs slightly, for sake of speed.  Specifically,
                steps 1 and 3 are done at the same time.

                Step 1: Collect Coefficient Gaps.
                        Scan through coefficient list, and record the lengths of
                        sequences of zero coefficients.  This corresponds to
                        collapsing Horner\'s Form into a reduced representation.
                        For example, ::

                          x^8 + x^4 + x^2 + 1
                           = ((((((((1)*x + 0)*x+0)*x+0)*x+1)*x+0)*x+0)*x+1)*x+0)*x+1
                           = ((((1)*x^4 + 1)*x^2 + 1)*x^2 + 1

                        gives a list of "gaps": [2,4]

                Step 2: Fill in Gap Structure.
                        Given the list of gaps, find a reasonable sequence of
                        of multiplications / squarings of x that will result in
                        the computation of all desired exponents.  Record this
                        sequence of steps as an evaluation DAG, and retain
                        references to the nodes representing the desired
                        exponents.  For the example above, we would have::

                          x^2 = x*x
                          x^4 = (x^2) * (x^2)

                Step 3: Construct Evaluation Dag.
                        Rescan the coefficient list, and build an evaluation DAG
                        representation for the reduced Horner Form as above.
                        Whenever a sequence of zeros is encountered, multiply by
                        the appropriate "gap" node.  Retain a reference to the
                        result node.

                Implementation considerations:

                * By combining steps 1 and 3, we greatly improve the speed of
                  this construction, but some complexity is introduced.  The
                  solution to this is that "dummy" nodes are created to represent
                  the desired gaps.  As the structure of the gaps is filled in,
                  these dummies get references to usable DAG nodes.  After all gaps
                  are filled in, we strip out dummy nodes, and are left with a
                  complete representation of our polynomial.

                * The "binary" algorithm (currently the only algorithm; others are
                  forthcoming) requires the gaps to considered in order, and adds
                  additional dummies as it goes.  Hence, the gaps are put into a
                  binary tree.
        '''
    def __call__(self, x) -> Any:
        """CompiledPolynomialFunction.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 118)"""

class abc_pd(binary_pd):
    """abc_pd(generic_pd left, generic_pd right, int index)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, generic_pdleft, generic_pdright, intindex) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 496)"""

class add_pd(binary_pd):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class binary_pd(generic_pd):
    """binary_pd(generic_pd left, generic_pd right)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, generic_pdleft, generic_pdright) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 456)"""

class coeff_pd(generic_pd):
    """coeff_pd(int index)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intindex) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 405)"""

class dummy_pd(generic_pd):
    """dummy_pd(int label)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intlabel) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 372)"""

class generic_pd:
    """generic_pd()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 355)"""

class mul_pd(binary_pd):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class pow_pd(unary_pd):
    """pow_pd(generic_pd base, exponent)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, generic_pdbase, exponent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 442)"""

class sqr_pd(unary_pd):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class unary_pd(generic_pd):
    """unary_pd(generic_pd operand)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, generic_pdoperand) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 418)"""

class univar_pd(generic_pd):
    """univar_pd()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 395)"""

class var_pd(generic_pd):
    """var_pd(int index)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intindex) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_compiled.pyx (starting at line 384)"""
