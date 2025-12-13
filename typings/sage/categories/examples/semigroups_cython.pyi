import sage.categories.category
import sage.categories.examples.semigroups
import sage.structure.element
from sage.categories.category import Category as Category
from sage.categories.examples.semigroups import LeftZeroSemigroupPython as LeftZeroSemigroupPython
from sage.categories.semigroups import Semigroups as Semigroups
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class IdempotentSemigroups(sage.categories.category.Category):
    class ElementMethods:
        @overload
        def is_idempotent(self) -> Any:
            """ElementMethods.is_idempotent(self)

            File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 38)

            EXAMPLES::

                sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                sage: S = LeftZeroSemigroup()
                sage: S(2).is_idempotent()
                True"""
        @overload
        def is_idempotent(self) -> Any:
            """ElementMethods.is_idempotent(self)

            File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 38)

            EXAMPLES::

                sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                sage: S = LeftZeroSemigroup()
                sage: S(2).is_idempotent()
                True"""
    @overload
    def super_categories(self) -> Any:
        """IdempotentSemigroups.super_categories(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 15)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import IdempotentSemigroups
            sage: IdempotentSemigroups().super_categories()
            [Category of semigroups]"""
    @overload
    def super_categories(self) -> Any:
        """IdempotentSemigroups.super_categories(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 15)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import IdempotentSemigroups
            sage: IdempotentSemigroups().super_categories()
            [Category of semigroups]"""

class IdempotentSemigroups.ElementMethods:
    @overload
    def is_idempotent(self) -> Any:
        """ElementMethods.is_idempotent(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 38)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup()
            sage: S(2).is_idempotent()
            True"""
    @overload
    def is_idempotent(self) -> Any:
        """ElementMethods.is_idempotent(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 38)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup()
            sage: S(2).is_idempotent()
            True"""

class LeftZeroSemigroup(sage.categories.examples.semigroups.LeftZeroSemigroup):
    """File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 129)

        An example of semigroup.

        This class illustrates a minimal implementation of a semi-group
        where the element class is an extension type, and still gets code
        from the category. The category itself must be a Python class
        though.

        This is purely a proof of concept. The code obviously needs refactorisation!

        Comments:

        - one cannot play ugly class surgery tricks (as with _mul_parent).
          available operations should really be declared to the coercion model!

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup(); S
            An example of a semigroup: the left zero semigroup

        This is the semigroup which contains all sort of objects::

            sage: S.some_elements()
            [3, 42, 'a', 3.4, 'raton laveur']

        with product rule given by `a \\times b = a` for all `a,b`. ::

            sage: S('hello') * S('world')
            'hello'

            sage: S(3)*S(1)*S(2)
            3

            sage: S(3)^12312321312321
            3

            sage: TestSuite(S).run(verbose = True)
            running ._test_an_element() . . . pass
            running ._test_associativity() . . . pass
            running ._test_cardinality() . . . pass
            running ._test_category() . . . pass
            running ._test_construction() . . . pass
            running ._test_elements() . . .
              Running the test suite of self.an_element()
              running ._test_category() . . . pass
              running ._test_eq() . . . pass
              running ._test_new() . . . pass
              running ._test_not_implemented_methods() . . . pass
              running ._test_pickling() . . . pass
              pass
            running ._test_elements_eq_reflexive() . . . pass
            running ._test_elements_eq_symmetric() . . . pass
            running ._test_elements_eq_transitive() . . . pass
            running ._test_elements_neq() . . . pass
            running ._test_eq() . . . pass
            running ._test_new() . . . pass
            running ._test_not_implemented_methods() . . . pass
            running ._test_pickling() . . . pass
            running ._test_some_elements() . . . pass

        That's really the only method which is obtained from the category ... ::

            sage: S(42).is_idempotent
            <bound method IdempotentSemigroups.ElementMethods.is_idempotent of 42>
            sage: S(42).is_idempotent()
            True

            sage: S(42)._pow_int
            <bound method IdempotentSemigroups.ElementMethods._pow_int of 42>
            sage: S(42)^10
            42

            sage: S(42).is_idempotent
            <bound method IdempotentSemigroups.ElementMethods.is_idempotent of 42>
            sage: S(42).is_idempotent()
            True
    """

    class Element(sage.structure.element.Element):
        """LeftZeroSemigroupElement(parent, value)"""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 53)

                    EXAMPLES::

                        sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                        sage: S = LeftZeroSemigroup()
                        sage: x = S(3)
                        sage: TestSuite(x).run()
        """
        def __pow__(self, i, dummy) -> Any:
            """LeftZeroSemigroupElement.__pow__(self, i, dummy)

            File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 117)

            EXAMPLES::

                sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                sage: S = LeftZeroSemigroup()
                sage: S(2)^3
                2"""
        @overload
        def __reduce__(self) -> Any:
            """LeftZeroSemigroupElement.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 76)

            EXAMPLES::

                sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                sage: S = LeftZeroSemigroup()
                sage: x = S(3)
                sage: x.__reduce__()
                (<class 'sage.categories.examples.semigroups_cython.LeftZeroSemigroupElement'>,
                 (An example of a semigroup: the left zero semigroup, 3))"""
        @overload
        def __reduce__(self) -> Any:
            """LeftZeroSemigroupElement.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 76)

            EXAMPLES::

                sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                sage: S = LeftZeroSemigroup()
                sage: x = S(3)
                sage: x.__reduce__()
                (<class 'sage.categories.examples.semigroups_cython.LeftZeroSemigroupElement'>,
                 (An example of a semigroup: the left zero semigroup, 3))"""
        def __rpow__(self, other):
            """Return pow(value, self, mod)."""
    def __init__(self) -> Any:
        """LeftZeroSemigroup.__init__(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 209)

        TESTS::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup()
            sage: S.category()
            Category of idempotent semigroups
            sage: TestSuite(S).run()"""

class LeftZeroSemigroupElement(sage.structure.element.Element):
    """LeftZeroSemigroupElement(parent, value)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, value) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 53)

                EXAMPLES::

                    sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
                    sage: S = LeftZeroSemigroup()
                    sage: x = S(3)
                    sage: TestSuite(x).run()
        """
    def __pow__(self, i, dummy) -> Any:
        """LeftZeroSemigroupElement.__pow__(self, i, dummy)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 117)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup()
            sage: S(2)^3
            2"""
    @overload
    def __reduce__(self) -> Any:
        """LeftZeroSemigroupElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 76)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup()
            sage: x = S(3)
            sage: x.__reduce__()
            (<class 'sage.categories.examples.semigroups_cython.LeftZeroSemigroupElement'>,
             (An example of a semigroup: the left zero semigroup, 3))"""
    @overload
    def __reduce__(self) -> Any:
        """LeftZeroSemigroupElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/examples/semigroups_cython.pyx (starting at line 76)

        EXAMPLES::

            sage: from sage.categories.examples.semigroups_cython import LeftZeroSemigroup
            sage: S = LeftZeroSemigroup()
            sage: x = S(3)
            sage: x.__reduce__()
            (<class 'sage.categories.examples.semigroups_cython.LeftZeroSemigroupElement'>,
             (An example of a semigroup: the left zero semigroup, 3))"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
