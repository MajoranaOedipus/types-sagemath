from . import hall_littlewood as hall_littlewood, jack as jack, llt as llt, macdonald as macdonald, orthotriang as orthotriang, sfa as sfa
from _typeshed import Incomplete
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

translate: Incomplete
conversion_functions: Incomplete

def init() -> None:
    """
    Set up the conversion functions between the classical bases.

    EXAMPLES::

        sage: from sage.combinat.sf.classical import init
        sage: sage.combinat.sf.classical.conversion_functions = {}
        sage: init()
        sage: sage.combinat.sf.classical.conversion_functions[('Schur', 'powersum')]
        <cyfunction t_SCHUR_POWSYM_symmetrica at ...>

    The following checks if the bug described in :issue:`15312` is fixed. ::

        sage: change = sage.combinat.sf.classical.conversion_functions[('powersum', 'Schur')]
        sage: hideme = change({Partition([1]*47):ZZ(1)}) # long time
        sage: change({Partition([2,2]):QQ(1)})
        s[1, 1, 1, 1] - s[2, 1, 1] + 2*s[2, 2] - s[3, 1] + s[4]
    """

class SymmetricFunctionAlgebra_classical(sfa.SymmetricFunctionAlgebra_generic):
    """
    The class of classical symmetric functions.

    .. TODO:: delete this class once all coercions will be handled by Sage's coercion model

    TESTS::

        sage: TestSuite(SymmetricFunctions(QQ).s()).run()
        sage: TestSuite(SymmetricFunctions(QQ).h()).run()
        sage: TestSuite(SymmetricFunctions(QQ).m()).run()
        sage: TestSuite(SymmetricFunctions(QQ).e()).run()
        sage: TestSuite(SymmetricFunctions(QQ).p()).run()
    """
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element):
        """
        A symmetric function.
        """
