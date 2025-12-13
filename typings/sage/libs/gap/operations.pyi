from _typeshed import Incomplete
from sage.libs.gap.libgap import libgap as libgap
from sage.structure.sage_object import SageObject as SageObject

Length: Incomplete
FlagsType: Incomplete
TypeObj: Incomplete
IS_SUBSET_FLAGS: Incomplete
GET_OPER_FLAGS: Incomplete
OPERATIONS: Incomplete
NameFunction: Incomplete
NAME_RE: Incomplete

class OperationInspector(SageObject):
    flags: Incomplete
    def __init__(self, libgap_element) -> None:
        """
        Information about operations that can act on a given LibGAP element.

        INPUT:

        - ``libgap_element`` -- libgap element

        EXAMPLES::

            sage: from sage.libs.gap.operations import OperationInspector
            sage: OperationInspector(libgap(123))
            Operations on 123
        """
    @property
    def obj(self):
        """
        The first argument for the operations.

        OUTPUT: a Libgap object

        EXAMPLES::

            sage: from sage.libs.gap.operations import OperationInspector
            sage: x = OperationInspector(libgap(123))
            sage: print(x.obj)
            123
        """
    def operations(self):
        """
        Return the GAP operations for :meth:`obj`.

        OUTPUT: list of GAP operations

        EXAMPLES::

            sage: from sage.libs.gap.operations import OperationInspector
            sage: x = OperationInspector(libgap(123))
            sage: Unknown = libgap.function_factory('Unknown')
            sage: Unknown in x.operations()
            True
        """
    def op_names(self):
        """
        Return the names of the operations.

        OUTPUT: list of strings

        EXAMPLES::

            sage: from sage.libs.gap.operations import OperationInspector
            sage: x = OperationInspector(libgap(123))
            sage: 'Sqrt' in x.op_names()
            True
        """
