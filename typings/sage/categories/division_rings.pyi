from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.rings import Rings as Rings
from sage.misc.lazy_import import LazyImport as LazyImport

class DivisionRings(CategoryWithAxiom):
    """
    The category of division rings.

    A division ring (or skew field) is a not necessarily commutative
    ring where all nonzero elements have multiplicative inverses

    EXAMPLES::

      sage: DivisionRings()
      Category of division rings
      sage: DivisionRings().super_categories()
      [Category of domains]

    TESTS::

        sage: TestSuite(DivisionRings()).run()
    """
    def extra_super_categories(self):
        '''
        Return the :class:`Domains` category.

        This method specifies that a division ring has no zero
        divisors, i.e. is a domain.

        .. SEEALSO::

            The :ref:`axioms-deduction-rules` section in the
            documentation of axioms

        EXAMPLES::

            sage: DivisionRings().extra_super_categories()
            (Category of domains,)
            sage: "NoZeroDivisors" in DivisionRings().axioms()
            True
        '''
    Commutative: Incomplete
    def Finite_extra_super_categories(self):
        """
        Return extraneous super categories for ``DivisionRings().Finite()``.

        EXAMPLES:

        Any field is a division ring::

            sage: Fields().is_subcategory(DivisionRings())
            True

        This methods specifies that, by Weddeburn theorem, the
        reciprocal holds in the finite case: a finite division ring is
        commutative and thus a field::

            sage: DivisionRings().Finite_extra_super_categories()
            (Category of commutative magmas,)
            sage: DivisionRings().Finite()
            Category of finite enumerated fields

        .. WARNING::

            This is not implemented in
            ``DivisionRings.Finite.extra_super_categories`` because
            the categories of finite division rings and of finite
            fields coincide. See the section
            :ref:`axioms-deduction-rules` in the documentation of
            axioms.

        TESTS::

            sage: DivisionRings().Finite() is Fields().Finite()
            True

        This works also for subcategories::

            sage: class Foo(Category):
            ....:     def super_categories(self): return [DivisionRings()]
            sage: Foo().Finite().is_subcategory(Fields())
            True
        """
    class ParentMethods: ...
    class ElementMethods: ...
