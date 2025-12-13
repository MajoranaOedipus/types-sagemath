from sage.categories.basic import Fields as Fields
from sage.categories.category import Category as Category
from sage.misc.cachefunc import cached_method as cached_method

class FunctionFields(Category):
    """
    The category of function fields.

    EXAMPLES:

    We create the category of function fields::

        sage: C = FunctionFields()
        sage: C
        Category of function fields

    TESTS::

        sage: TestSuite(FunctionFields()).run()
    """
    @cached_method
    def super_categories(self):
        """
        Return the Category of which this is a direct sub-Category
        For a list off all super categories see all_super_categories

        EXAMPLES::

            sage: FunctionFields().super_categories()
            [Category of fields]
        """
    class ParentMethods: ...
    class ElementMethods: ...
