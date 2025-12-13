import _cython_3_2_1
from typing import Any

__pyx_capi__: dict
canonicalize_axioms: _cython_3_2_1.cython_function_or_method
category_sort_key: _cython_3_2_1.cython_function_or_method
get_axiom_index: _cython_3_2_1.cython_function_or_method
join_as_tuple: _cython_3_2_1.cython_function_or_method

class AxiomContainer(dict):
    '''File: /build/sagemath/src/sage/src/sage/categories/category_cy_helper.pyx (starting at line 217)

        A fast container for axioms.

        This is derived from :class:`dict`. A key is the name of an axiom. The
        corresponding value is the "rank" of this axiom, that is used to order the
        axioms in :func:`canonicalize_axioms`.

        EXAMPLES::

            sage: all_axioms = sage.categories.category_with_axiom.all_axioms
            sage: isinstance(all_axioms, sage.categories.category_with_axiom.AxiomContainer)
            True
    '''
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add(self, axiom) -> Any:
        """AxiomContainer.add(self, axiom)

        File: /build/sagemath/src/sage/src/sage/categories/category_cy_helper.pyx (starting at line 231)

        Add a new axiom name, of the next rank.

        EXAMPLES::

            sage: all_axioms = sage.categories.category_with_axiom.all_axioms
            sage: m = max(all_axioms.values())
            sage: all_axioms.add('Awesome')
            sage: all_axioms['Awesome'] == m + 1
            True

        To avoid side effects, we remove the added axiom::

            sage: del all_axioms['Awesome']"""
    def __iadd__(self, L) -> Any:
        """AxiomContainer.__iadd__(self, L)

        File: /build/sagemath/src/sage/src/sage/categories/category_cy_helper.pyx (starting at line 249)

        Inline addition, which means to add a list of axioms to the container.

        EXAMPLES::

            sage: all_axioms = sage.categories.category_with_axiom.all_axioms
            sage: m = max(all_axioms.values())
            sage: all_axioms += ('Fancy', 'Awesome')
            sage: all_axioms['Awesome'] == m + 2
            True

        To avoid side effects, we delete the axioms that we just added::

            sage: del all_axioms['Awesome'], all_axioms['Fancy']"""
