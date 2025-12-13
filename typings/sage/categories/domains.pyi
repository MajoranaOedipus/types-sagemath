from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.rings import Rings as Rings
from sage.misc.lazy_import import LazyImport as LazyImport

class Domains(CategoryWithAxiom):
    """
    The category of domains.

    A domain (or non-commutative integral domain), is a ring, not
    necessarily commutative, with no nonzero zero divisors.

    EXAMPLES::

        sage: C = Domains(); C
        Category of domains
        sage: C.super_categories()
        [Category of rings]
        sage: C is Rings().NoZeroDivisors()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Domains().super_categories()
            [Category of rings]
        """
    Commutative: Incomplete
    class ParentMethods: ...
    class ElementMethods: ...
