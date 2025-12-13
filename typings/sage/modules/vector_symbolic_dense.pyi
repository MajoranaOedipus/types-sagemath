from sage.modules import free_module_element as free_module_element
from sage.symbolic.expression import Expression as Expression

def apply_map(phi):
    """
    Return a function that applies ``phi`` to its argument.

    EXAMPLES::

        sage: from sage.modules.vector_symbolic_dense import apply_map
        sage: v = vector([1,2,3])
        sage: f = apply_map(lambda x: x+1)
        sage: f(v)
        (2, 3, 4)
    """

class Vector_symbolic_dense(free_module_element.FreeModuleElement_generic_dense): ...
