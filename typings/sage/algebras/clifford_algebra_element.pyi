"""File: /build/sagemath/src/sage/src/sage/algebras/clifford_algebra_element.pyx (starting at line 1)

Clifford algebra elements

AUTHORS:

- Travis Scrimshaw (2013-09-06): Initial version
- Trevor Karn (2022-07-10): Rewrite multiplication using bitsets

"""

from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class CliffordAlgebraElement(IndexedFreeModuleElement): 
    r"""File: /build/sagemath/src/sage/src/sage/algebras/clifford_algebra_element.pyx (starting at line 28)

    An element in a Clifford algebra.

    TESTS::

        sage: Q = QuadraticForm(ZZ, 3, [1, 2, 3, 4, 5, 6])
        sage: Cl.<x,y,z> = CliffordAlgebra(Q)
        sage: elt = ((x^3-z)*x + y)^2
        sage: TestSuite(elt).run()
    
"""
    ...

class ExteriorAlgebraElement(CliffordAlgebraElement):
    r"""File: /build/sagemath/src/sage/src/sage/algebras/clifford_algebra_element.pyx (starting at line 401)

    An element of an exterior algebra.
"""
    ...

class CohomologyRAAGElement(CliffordAlgebraElement):
    r"""File: /build/sagemath/src/sage/src/sage/algebras/clifford_algebra_element.pyx (starting at line 936)

    An element in the cohomology of a right-angled Artin group.

    .. SEEALSO::

        :class:`~sage.groups.raag.CohomologyRAAG`"""
    ...