from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap as FinitelyGeneratedMatrixGroup_gap
from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap as NamedMatrixGroup_gap
from sage.groups.matrix_gps.unitary import UnitaryMatrixGroup_generic as UnitaryMatrixGroup_generic
from sage.misc.cachefunc import cached_method as cached_method

class UnitaryMatrixGroup_gap(UnitaryMatrixGroup_generic, NamedMatrixGroup_gap, FinitelyGeneratedMatrixGroup_gap):
    """
    The general or special unitary group in GAP.

    TESTS:

    Check that :issue:`20867` is fixed::

        sage: from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap
        sage: G = GU(3,3)
        sage: isinstance(G, FinitelyGeneratedMatrixGroup_gap)
        True
    """
    @cached_method
    def invariant_form(self):
        """
        Return the hermitian form preserved by the unitary group.

        OUTPUT: a square matrix describing the bilinear form

        EXAMPLES::

            sage: G32 = GU(3,2)
            sage: G32.invariant_form()
            [0 0 1]
            [0 1 0]
            [1 0 0]
        """
