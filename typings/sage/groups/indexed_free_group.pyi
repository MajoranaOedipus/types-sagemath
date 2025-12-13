from sage.categories.groups import Groups as Groups
from sage.categories.poor_man_map import PoorManMap as PoorManMap
from sage.groups.group import AbelianGroup as AbelianGroup, Group as Group
from sage.misc.cachefunc import cached_method as cached_method
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoidElement as IndexedFreeAbelianMonoidElement, IndexedFreeMonoidElement as IndexedFreeMonoidElement, IndexedMonoid as IndexedMonoid
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.sets.family import Family as Family

class IndexedGroup(IndexedMonoid):
    """
    Base class for free (abelian) groups whose generators are indexed
    by a set.

    TESTS:

    We check finite properties::

        sage: G = Groups().free(index_set=ZZ)
        sage: G.is_finite()
        False
        sage: G = Groups().free(index_set='abc')
        sage: G.is_finite()
        False
        sage: G = Groups().free(index_set=[])
        sage: G.is_finite()
        True

    ::

        sage: G = Groups().Commutative().free(index_set=ZZ)
        sage: G.is_finite()
        False
        sage: G = Groups().Commutative().free(index_set='abc')
        sage: G.is_finite()
        False
        sage: G = Groups().Commutative().free(index_set=[])
        sage: G.is_finite()
        True
    """
    def order(self):
        """
        Return the number of elements of ``self``, which is `\\infty` unless
        this is the trivial group.

        EXAMPLES::

            sage: G = Groups().free(index_set=ZZ)
            sage: G.order()
            +Infinity
            sage: G = Groups().Commutative().free(index_set='abc')
            sage: G.order()
            +Infinity
            sage: G = Groups().Commutative().free(index_set=[])
            sage: G.order()
            1
        """
    def rank(self):
        """
        Return the rank of ``self``.

        This is the number of generators of ``self``.

        EXAMPLES::

            sage: G = Groups().free(index_set=ZZ)
            sage: G.rank()
            +Infinity
            sage: G = Groups().free(index_set='abc')
            sage: G.rank()
            3
            sage: G = Groups().free(index_set=[])
            sage: G.rank()
            0

        ::

            sage: G = Groups().Commutative().free(index_set=ZZ)
            sage: G.rank()
            +Infinity
            sage: G = Groups().Commutative().free(index_set='abc')
            sage: G.rank()
            3
            sage: G = Groups().Commutative().free(index_set=[])
            sage: G.rank()
            0
        """
    @cached_method
    def group_generators(self):
        """
        Return the group generators of ``self``.

        EXAMPLES::

            sage: G = Groups.free(index_set=ZZ)
            sage: G.group_generators()
            Lazy family (Generator map from Integer Ring to
             Free group indexed by Integer Ring(i))_{i in Integer Ring}
            sage: G = Groups().free(index_set='abcde')
            sage: sorted(G.group_generators())
            [F['a'], F['b'], F['c'], F['d'], F['e']]
        """
    gens = group_generators

class IndexedFreeGroup(IndexedGroup, Group):
    """
    An indexed free group.

    EXAMPLES::

        sage: G = Groups().free(index_set=ZZ)
        sage: G
        Free group indexed by Integer Ring
        sage: G = Groups().free(index_set='abcde')
        sage: G
        Free group indexed by {'a', 'b', 'c', 'd', 'e'}
    """
    def __init__(self, indices, prefix, category=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: G = Groups().free(index_set=ZZ)
            sage: TestSuite(G).run()
            sage: G = Groups().free(index_set='abc')
            sage: TestSuite(G).run()
        """
    @cached_method
    def one(self):
        """
        Return the identity element of ``self``.

        EXAMPLES::

            sage: G = Groups().free(ZZ)
            sage: G.one()
            1
        """
    def gen(self, x):
        """
        The generator indexed by ``x`` of ``self``.

        EXAMPLES::

            sage: G = Groups().free(index_set=ZZ)
            sage: G.gen(0)
            F[0]
            sage: G.gen(2)
            F[2]
        """
    class Element(IndexedFreeMonoidElement):
        def __len__(self) -> int:
            """
            Return the length of ``self``.

            EXAMPLES::

                sage: G = Groups().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: elt = a*c^-3*b^-2*a
                sage: elt.length()
                7
                sage: len(elt)
                7

                sage: G = Groups().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: elt = a*c^-3*b^-2*a
                sage: elt.length()
                7
                sage: len(elt)
                7
            """
        length = __len__
        def __invert__(self):
            """
            Return the inverse of ``self``.

            EXAMPLES::

                sage: G = Groups().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: x = a*b^2*e^-1*d; ~x
                F[3]^-1*F[4]*F[1]^-2*F[0]^-1
                sage: x * ~x
                1
            """
        def to_word_list(self):
            """
            Return ``self`` as a word represented as a list whose entries
            are the pairs ``(i, s)`` where ``i`` is the index and ``s`` is
            the sign.

            EXAMPLES::

                sage: G = Groups().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: x = a*b^2*e*a^-1
                sage: x.to_word_list()
                [(0, 1), (1, 1), (1, 1), (4, 1), (0, -1)]
            """

class IndexedFreeAbelianGroup(IndexedGroup, AbelianGroup):
    """
    An indexed free abelian group.

    EXAMPLES::

        sage: G = Groups().Commutative().free(index_set=ZZ)
        sage: G
        Free abelian group indexed by Integer Ring
        sage: G = Groups().Commutative().free(index_set='abcde')
        sage: G
        Free abelian group indexed by {'a', 'b', 'c', 'd', 'e'}
    """
    def __init__(self, indices, prefix, category=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: G = Groups().Commutative().free(index_set=ZZ)
            sage: TestSuite(G).run()
            sage: G = Groups().Commutative().free(index_set='abc')
            sage: TestSuite(G).run()
        """
    @cached_method
    def one(self):
        """
        Return the identity element of ``self``.

        EXAMPLES::

            sage: G = Groups().Commutative().free(index_set=ZZ)
            sage: G.one()
            1
        """
    def gen(self, x):
        """
        The generator indexed by ``x`` of ``self``.

        EXAMPLES::

            sage: G = Groups().Commutative().free(index_set=ZZ)
            sage: G.gen(0)
            F[0]
            sage: G.gen(2)
            F[2]
        """
    class Element(IndexedFreeAbelianMonoidElement, IndexedFreeGroup.Element):
        def __invert__(self):
            """
            Return the inverse of ``self``.

            EXAMPLES::

                sage: G = Groups().Commutative().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: x = a*b^2*e^-1*d; ~x
                F[0]^-1*F[1]^-2*F[3]^-1*F[4]
                sage: x * ~x
                1
            """
        def __floordiv__(self, a):
            """
            Return the division of ``self`` by ``a``.

            EXAMPLES::

                sage: G = Groups().Commutative().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: elt = a*b*c^3*d^2; elt
                F[0]*F[1]*F[2]^3*F[3]^2
                sage: elt // a
                F[1]*F[2]^3*F[3]^2
                sage: elt // c
                F[0]*F[1]*F[2]^2*F[3]^2
                sage: elt // (a*b*d^2)
                F[2]^3
                sage: elt // a^4
                F[0]^-3*F[1]*F[2]^3*F[3]^2
            """
        def __pow__(self, n):
            """
            Raise ``self`` to the power of ``n``.

            EXAMPLES::

                sage: G = Groups().Commutative().free(index_set=ZZ)
                sage: a,b,c,d,e = [G.gen(i) for i in range(5)]
                sage: x = a*b^2*e^-1*d; x
                F[0]*F[1]^2*F[3]*F[4]^-1
                sage: x^3
                F[0]^3*F[1]^6*F[3]^3*F[4]^-3
                sage: x^0
                1
                sage: x^-3
                F[0]^-3*F[1]^-6*F[3]^-3*F[4]^3
            """
