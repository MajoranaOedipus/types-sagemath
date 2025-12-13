from .free_monoid_element import FreeMonoidElement as FreeMonoidElement
from .monoid import Monoid_class as Monoid_class
from sage.combinat.words.finite_word import FiniteWord_class as FiniteWord_class
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_FreeMonoid(x):
    """
    Return ``True`` if `x` is a free monoid.

    EXAMPLES::

        sage: from sage.monoids.free_monoid import is_FreeMonoid
        sage: is_FreeMonoid(5)
        doctest:warning...
        DeprecationWarning: the function is_FreeMonoid is deprecated;
        use 'isinstance(..., (FreeMonoid, IndexedFreeMonoid))' instead
        See https://github.com/sagemath/sage/issues/37897 for details.
        False
        sage: is_FreeMonoid(FreeMonoid(7,'a'))
        True
        sage: is_FreeMonoid(FreeAbelianMonoid(7,'a'))
        False
        sage: is_FreeMonoid(FreeAbelianMonoid(0,''))
        False
        sage: is_FreeMonoid(FreeMonoid(index_set=ZZ))
        True
        sage: is_FreeMonoid(FreeAbelianMonoid(index_set=ZZ))
        False
    """

class FreeMonoid(Monoid_class, UniqueRepresentation):
    """
    Return a free monoid on `n` generators or with the generators
    indexed by a set `I`.

    We construct free monoids by specifying either:

    - the number of generators and/or the names of the generators
    - the indexing set for the generators

    INPUT:

    - ``index_set`` -- an indexing set for the generators; if an
      integer `n`, than this becomes `\\{0, 1, \\ldots, n-1\\}`

    - ``names`` -- names of generators

    - ``commutative`` -- boolean (default: ``False``); whether the free
      monoid is commutative or not

    OUTPUT: a free monoid

    EXAMPLES::

        sage: F = FreeMonoid(3,'x'); F
        Free monoid on 3 generators (x0, x1, x2)
        sage: x = F.gens()
        sage: x[0]*x[1]**5 * (x[0]*x[2])
        x0*x1^5*x0*x2
        sage: F = FreeMonoid(3, 'a')
        sage: F
        Free monoid on 3 generators (a0, a1, a2)

        sage: F.<a,b,c,d,e> = FreeMonoid(); F
        Free monoid on 5 generators (a, b, c, d, e)
        sage: FreeMonoid(index_set=ZZ)
        Free monoid indexed by Integer Ring

        sage: F.<x,y,z> = FreeMonoid(abelian=True); F
        Free abelian monoid on 3 generators (x, y, z)
        sage: FreeMonoid(index_set=ZZ, commutative=True)
        Free abelian monoid indexed by Integer Ring
    """
    @staticmethod
    def __classcall_private__(cls, index_set=None, names=None, commutative: bool = False, **kwds):
        """
        Construct a free monoid or a free abelian monoid, depending on the
        input. Also, normalize the input.

        EXAMPLES::

            sage: F.<a,b,c,d,e> = FreeMonoid(); F
            Free monoid on 5 generators (a, b, c, d, e)
            sage: FreeMonoid(index_set=ZZ)
            Free monoid indexed by Integer Ring
            sage: F.<x,y,z> = FreeMonoid(abelian=True); F
            Free abelian monoid on 3 generators (x, y, z)
            sage: FreeMonoid(index_set=ZZ, commutative=True)
            Free abelian monoid indexed by Integer Ring
            sage: F = FreeMonoid(index_set=ZZ, names='x,y,z')
            sage: G = FreeMonoid(index_set=ZZ, names=['x', 'y', 'z'])
            sage: F == G
            True
            sage: F is G
            True

            sage: FreeMonoid(2, names='a,b') is FreeMonoid(names=['a','b'])
            True

        Fix a bug when ``index_set`` is ``None`` and ``names`` is a
        string (:issue:`26221`)::

            sage: FreeMonoid(2, names=['a','b']) is FreeMonoid(names='a,b')
            True
        """
    Element = FreeMonoidElement
    def __init__(self, n, names=None) -> None:
        """
        Return a free monoid on `n` generators or with the generators
        indexed by a set `I`.

        INPUT:

        - ``n`` -- number of generators

        - ``names`` -- names of generators

        TESTS::

            sage: M = FreeMonoid(3, names=['a','b','c'])
            sage: TestSuite(M).run()
            sage: F.<x,y> = FreeMonoid()
            sage: TestSuite(F).run()
        """
    def __contains__(self, x) -> bool: ...
    def gen(self, i: int = 0):
        """
        The `i`-th generator of the monoid.

        INPUT:

        - ``i`` -- integer (default: 0)

        EXAMPLES::

            sage: F = FreeMonoid(3, 'a')
            sage: F.gen(1)
            a1
            sage: F.gen(2)
            a2
            sage: F.gen(5)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 5) must be between 0 and 2
        """
    def ngens(self):
        """
        The number of free generators of the monoid.

        EXAMPLES::

            sage: F = FreeMonoid(2005, 'a')
            sage: F.ngens()
            2005
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        This is `\\infty` if there is at least one generator.

        EXAMPLES::

            sage: F = FreeMonoid(2005, 'a')
            sage: F.cardinality()
            +Infinity

            sage: F = FreeMonoid(0, [])
            sage: F.cardinality()
            1
        """
