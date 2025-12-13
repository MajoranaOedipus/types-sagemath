from _typeshed import Incomplete
from sage.libs.singular.function import lib as lib, list_of_functions as list_of_functions, singular_function as singular_function

class SingularFunctionFactory:
    """
    A convenient interface to libsingular functions.
    """
    def __getattr__(self, name):
        """
        EXAMPLES::

            sage: import sage.libs.singular.function_factory
            sage: groebner = sage.libs.singular.function_factory.ff.groebner
            sage: groebner
            groebner (singular function)

            sage: import sage.libs.singular.function_factory
            sage: primdecSY = sage.libs.singular.function_factory.ff.primdec__lib.primdecSY
            sage: primdecSY
            primdecSY (singular function)
        """
    def __dir__(self):
        '''
        EXAMPLES::

            sage: import sage.libs.singular.function_factory
            sage: "groebner" in sage.libs.singular.function_factory.ff.__dir__()
            True
        '''

ff: Incomplete
