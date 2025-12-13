from sage.algebras.free_algebra_element import FreeAlgebraElement as FreeAlgebraElement
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.modules.free_module_element import FreeModuleElement as FreeModuleElement
from sage.monoids.free_monoid_element import FreeMonoidElement as FreeMonoidElement
from sage.rings.integer import Integer as Integer
from sage.structure.element import AlgebraElement as AlgebraElement, RingElement as RingElement
from sage.structure.parent_gens import localvars as localvars
from sage.structure.richcmp import richcmp as richcmp

def is_FreeAlgebraQuotientElement(x):
    """
    EXAMPLES::

        sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)
        sage: sage.algebras.free_algebra_quotient_element.is_FreeAlgebraQuotientElement(i)
        doctest:warning...
        DeprecationWarning: The function is_FreeAlgebraQuotientElement is deprecated;
        use 'isinstance(..., FreeAlgebraQuotientElement)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        True

    Of course this is testing the data type::

        sage: sage.algebras.free_algebra_quotient_element.is_FreeAlgebraQuotientElement(1)
        False
        sage: sage.algebras.free_algebra_quotient_element.is_FreeAlgebraQuotientElement(H(1))
        True
    """

class FreeAlgebraQuotientElement(AlgebraElement):
    def __init__(self, A, x) -> None:
        """
        Create the element x of the FreeAlgebraQuotient A.

        EXAMPLES::

            sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(ZZ)
            sage: sage.algebras.free_algebra_quotient.FreeAlgebraQuotientElement(H, i)
            i
            sage: a = sage.algebras.free_algebra_quotient.FreeAlgebraQuotientElement(H, 1); a
            1
            sage: a in H
            True

        TESTS::

            sage: TestSuite(i).run()
        """
    def vector(self):
        """
        Return underlying vector representation of this element.

        EXAMPLES::

            sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)
            sage: ((2/3)*i - j).vector()
            (0, 2/3, -1, 0)
        """
    def __neg__(self):
        """
        Return negative of ``self``.

        EXAMPLES::

            sage: H, (i,j,k) = sage.algebras.free_algebra_quotient.hamilton_quatalg(QQ)
            sage: -i
            -i
            sage: -(2/3*i - 3/7*j + k)
            -2/3*i + 3/7*j - k
        """
