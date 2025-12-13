from .free_abelian_monoid_element import FreeAbelianMonoidElement as FreeAbelianMonoidElement
from _typeshed import Incomplete
from sage.categories.monoids import Monoids as Monoids
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent

class FreeAbelianMonoidFactory(UniqueFactory):
    '''
    Create the free abelian monoid in `n` generators.

    INPUT:

    - ``n`` -- integer

    - ``names`` -- names of generators

    OUTPUT: free abelian monoid

    EXAMPLES::

        sage: FreeAbelianMonoid(0, \'\')
        Free abelian monoid on 0 generators ()
        sage: F = FreeAbelianMonoid(5,names = list("abcde"))
        sage: F
        Free abelian monoid on 5 generators (a, b, c, d, e)
        sage: F(1)
        1
        sage: (a, b, c, d, e) = F.gens()
        sage: mul([ a, b, a, c, b, d, c, d ], F(1))
        a^2*b^2*c^2*d^2
        sage: a**2 * b**3 * a**2 * b**4
        a^4*b^7

    ::

        sage: loads(dumps(F)) is F
        True
    '''
    def create_key(self, n, names): ...
    def create_object(self, version, key): ...

FreeAbelianMonoid_factory: Incomplete

def FreeAbelianMonoid(index_set=None, names=None, **kwds):
    """
    Return a free abelian monoid on `n` generators or with the generators
    indexed by a set `I`.

    We construct free abelian monoids by specifying either:

    - the number of generators and/or the names of the generators
    - the indexing set for the generators (this ignores the other two inputs)

    INPUT:

    - ``index_set`` -- an indexing set for the generators; if an integer,
      then this becomes `\\{0, 1, \\ldots, n-1\\}`

    - ``names`` -- names of generators

    OUTPUT: a free abelian monoid

    EXAMPLES::

        sage: F.<a,b,c,d,e> = FreeAbelianMonoid(); F
        Free abelian monoid on 5 generators (a, b, c, d, e)
        sage: FreeAbelianMonoid(index_set=ZZ)
        Free abelian monoid indexed by Integer Ring
        sage: FreeAbelianMonoid(names='x,y')
        Free abelian monoid on 2 generators (x, y)
    """
def is_FreeAbelianMonoid(x):
    """
    Return ``True`` if `x` is a free abelian monoid.

    EXAMPLES::

        sage: from sage.monoids.free_abelian_monoid import is_FreeAbelianMonoid
        sage: is_FreeAbelianMonoid(5)
        doctest:warning...
        DeprecationWarning: the function is_FreeAbelianMonoid is deprecated;
        use 'isinstance(..., FreeAbelianMonoid_class)' instead
        See https://github.com/sagemath/sage/issues/37897 for details.
        False
        sage: is_FreeAbelianMonoid(FreeAbelianMonoid(7,'a'))
        True
        sage: is_FreeAbelianMonoid(FreeMonoid(7,'a'))
        False
        sage: is_FreeAbelianMonoid(FreeMonoid(0,''))
        False
    """

class FreeAbelianMonoid_class(Parent):
    """
    Free abelian monoid on `n` generators.
    """
    Element = FreeAbelianMonoidElement
    def __init__(self, n, names) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(6,'b')
            sage: TestSuite(F).run()
        """
    def __call__(self, x):
        """
        Create an element of this abelian monoid from `x`.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(10,'x')
            sage: F(F.gen(2))
            x2
            sage: F(1)
            1
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if `x` is an element of this abelian monoid.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(10,'b')
            sage: F.gen(2)*F.gen(3) in F
            True

        Note that a monoid on `9` generators is not considered a
        submonoid of one on `10` generators.

        ::

            sage: FreeAbelianMonoid(9,'c').gen(2) in F
            False

        However, multiple calls to the monoid constructor do *not* return
        multiple distinct monoids.

        ::

            sage: FreeAbelianMonoid(10,'b').gen(2) in F
            True
        """
    def gen(self, i: int = 0):
        """
        The `i`-th generator of the abelian monoid.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5,'a')
            sage: F.gen(0)
            a0
            sage: F.gen(2)
            a2
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5,'a')
            sage: F.gens()
            (a0, a1, a2, a3, a4)
        """
    def ngens(self):
        """
        The number of free generators of the abelian monoid.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(3000, 'a')
            sage: F.ngens()
            3000
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is `\\infty`.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(3000, 'a')
            sage: F.cardinality()
            +Infinity
        """
