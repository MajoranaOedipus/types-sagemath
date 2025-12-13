from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent

def is_Monoid(x) -> bool:
    """
    Return ``True`` if ``x`` is of type ``Monoid_class``.

    EXAMPLES::

        sage: from sage.monoids.monoid import is_Monoid
        sage: is_Monoid(0)
        doctest:warning...
        DeprecationWarning: the function is_Monoid is deprecated;
        use 'isinstance(..., Monoid_class)' instead
        See https://github.com/sagemath/sage/issues/37897 for details.
        False
        sage: is_Monoid(ZZ)   # The technical math meaning of monoid has
        ....:                 # no bearing whatsoever on the result: it's
        ....:                 # a typecheck which is not satisfied by ZZ
        ....:                 # since it does not inherit from Monoid_class.
        False
        sage: is_Monoid(sage.monoids.monoid.Monoid_class(('a','b')))
        True
        sage: F.<a,b,c,d,e> = FreeMonoid(5)
        sage: is_Monoid(F)
        True
    """

class Monoid_class(Parent):
    def __init__(self, names) -> None:
        """
        EXAMPLES::

            sage: from sage.monoids.monoid import Monoid_class
            sage: Monoid_class(('a','b'))
            <sage.monoids.monoid.Monoid_class_with_category object at ...>

        TESTS::

            sage: F.<a,b,c,d,e> = FreeMonoid(5)
            sage: TestSuite(F).run()
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators for ``self``.

        EXAMPLES::

            sage: F.<a,b,c,d,e> = FreeMonoid(5)
            sage: F.gens()
            (a, b, c, d, e)
        """
    def monoid_generators(self):
        """
        Return the generators for ``self``.

        EXAMPLES::

            sage: F.<a,b,c,d,e> = FreeMonoid(5)
            sage: F.monoid_generators()
            Family (a, b, c, d, e)
        """
