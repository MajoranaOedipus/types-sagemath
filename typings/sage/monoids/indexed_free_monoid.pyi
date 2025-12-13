from sage.categories.monoids import Monoids as Monoids
from sage.categories.poor_man_map import PoorManMap as PoorManMap
from sage.categories.sets_cat import Sets as Sets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.element import MonoidElement as MonoidElement
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators, parse_indices_names as parse_indices_names
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, rich_to_bool as rich_to_bool, richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IndexedMonoidElement(MonoidElement):
    """
    An element of an indexed monoid.

    This is an abstract class which uses the (abstract) method
    :meth:`_sorted_items` for all of its functions. So to implement an
    element of an indexed monoid, one just needs to implement
    :meth:`_sorted_items`, which returns a list of pairs ``(i, p)`` where
    ``i`` is the index and ``p`` is the corresponding power, sorted in some
    order. For example, in the free monoid there is no such choice, but for
    the free abelian monoid, one could want lex order or have the highest
    powers first.

    Indexed monoid elements are ordered lexicographically with respect to
    the result of :meth:`_sorted_items` (which for abelian free monoids is
    influenced by the order on the indexing set).
    """
    def __init__(self, F, x) -> None:
        """
        Create the element ``x`` of an indexed free abelian monoid ``F``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: F.gen(1)
            F[1]
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: x = a^2 * b^3 * a^2 * b^4; x
            F[0]^4*F[1]^7
            sage: TestSuite(x).run()

            sage: F = FreeMonoid(index_set=tuple('abcde'))
            sage: a,b,c,d,e = F.gens()
            sage: a in F
            True
            sage: a*b in F
            True
            sage: TestSuite(a*d^2*e*c*a).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: list(b*a*c^3*b)
            [(F[1], 1), (F[0], 1), (F[2], 3), (F[1], 1)]

        ::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: list(b*c^3*a)
            [(F[0], 1), (F[1], 1), (F[2], 3)]
        """
    def support(self):
        """
        Return a list of the objects indexing ``self`` with
        nonzero exponents.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*a*c^3*b).support()
            [0, 1, 2]

        ::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (a*c^3).support()
            [0, 2]
        """
    def leading_support(self):
        """
        Return the support of the leading generator of ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*a*c^3*a).leading_support()
            1

        ::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*c^3*a).leading_support()
            0
        """
    def trailing_support(self):
        """
        Return the support of the trailing generator of ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*a*c^3*a).trailing_support()
            0

        ::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*c^3*a).trailing_support()
            2
        """
    def to_word_list(self):
        """
        Return ``self`` as a word represented as a list whose entries
        are indices of ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*a*c^3*a).to_word_list()
            [1, 0, 2, 2, 2, 0]

        ::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*c^3*a).to_word_list()
            [0, 1, 2, 2, 2]
        """
    def is_one(self) -> bool:
        """
        Return if ``self`` is the identity element.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*a*c^3*a).is_one()
            False
            sage: F.one().is_one()
            True

        ::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (b*c^3*a).is_one()
            False
            sage: F.one().is_one()
            True
        """

class IndexedFreeMonoidElement(IndexedMonoidElement):
    """
    An element of an indexed free abelian monoid.
    """
    def __init__(self, F, x) -> None:
        """
        Create the element ``x`` of an indexed free abelian monoid ``F``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=tuple('abcde'))
            sage: x = F( [(1, 2), (0, 1), (3, 2), (0, 1)] )
            sage: y = F( ((1, 2), (0, 1), [3, 2], [0, 1]) )
            sage: z = F( reversed([(0, 1), (3, 2), (0, 1), (1, 2)]) )
            sage: x == y and y == z
            True
            sage: TestSuite(x).run()
        """
    def __hash__(self):
        """
        TESTS::

            sage: F = FreeMonoid(index_set=tuple('abcde'))
            sage: hash(F ([(1,2),(0,1)]) ) == hash(((1, 2), (0, 1)))
            True
            sage: hash(F ([(0,2),(1,1)]) ) == hash(((0, 2), (1, 1)))
            True
        """
    def __len__(self) -> int:
        """
        Return the length of ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: elt = a*c^3*b^2*a
            sage: elt.length()
            7
            sage: len(elt)
            7
        """
    length = __len__

class IndexedFreeAbelianMonoidElement(IndexedMonoidElement):
    """
    An element of an indexed free abelian monoid.
    """
    def __init__(self, F, x) -> None:
        """
        Create the element ``x`` of an indexed free abelian monoid ``F``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: x = F([(0, 1), (2, 2), (-1, 2)])
            sage: y = F({0:1, 2:2, -1:2})
            sage: z = F(reversed([(0, 1), (2, 2), (-1, 2)]))
            sage: x == y and y == z
            True
            sage: TestSuite(x).run()
        """
    def __hash__(self):
        """
        TESTS::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: H1 = hash( F([(0,1), (2,2)]) )
            sage: H2 = hash( F([(2,1)]) )
            sage: H1 == H2
            False
        """
    def __pow__(self, n):
        """
        Raise ``self`` to the power of ``n``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: x = a*b^2*e*d; x
            F[0]*F[1]^2*F[3]*F[4]
            sage: x^3
            F[0]^3*F[1]^6*F[3]^3*F[4]^3
            sage: x^0
            1
        """
    def __floordiv__(self, elt):
        """
        Cancel the element ``elt`` out of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: elt = a*b*c^3*d^2; elt
            F[0]*F[1]*F[2]^3*F[3]^2
            sage: elt // a
            F[1]*F[2]^3*F[3]^2
            sage: elt // c
            F[0]*F[1]*F[2]^2*F[3]^2
            sage: elt // (a*b*d^2)
            F[2]^3
            sage: elt // a^4
            Traceback (most recent call last):
            ...
            ValueError: invalid cancellation
            sage: elt // e^4
            Traceback (most recent call last):
            ...
            ValueError: invalid cancellation
        """
    def divides(self, m) -> bool:
        """
        Return whether ``self`` divides ``m``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: elt = a*b*c^3*d^2
            sage: a.divides(elt)
            True
            sage: c.divides(elt)
            True
            sage: (a*b*d^2).divides(elt)
            True
            sage: (a^4).divides(elt)
            False
            sage: e.divides(elt)
            False
        """
    def __len__(self) -> int:
        """
        Return the length of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: elt = a*c^3*b^2*a
            sage: elt.length()
            7
            sage: len(elt)
            7
        """
    length = __len__
    def dict(self):
        """
        Return ``self`` as a dictionary.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: a,b,c,d,e = [F.gen(i) for i in range(5)]
            sage: (a*c^3).dict()
            {0: 1, 2: 3}
        """

class IndexedMonoid(Parent, IndexedGenerators, UniqueRepresentation):
    """
    Base class for monoids with an indexed set of generators.

    INPUT:

    - ``indices`` -- the indices for the generators

    For the optional arguments that control the printing, see
    :class:`~sage.structure.indexed_generators.IndexedGenerators`.
    """
    @staticmethod
    def __classcall__(cls, indices, prefix=None, names=None, **kwds):
        """
        TESTS::

            sage: F = FreeAbelianMonoid(index_set=['a','b','c'])
            sage: G = FreeAbelianMonoid(index_set=('a','b','c'))
            sage: H = FreeAbelianMonoid(index_set=tuple('abc'))
            sage: F is G and F is H
            True

            sage: F = FreeAbelianMonoid(index_set=['a','b','c'], latex_bracket=['LEFT', 'RIGHT'])
            sage: F.print_options()['latex_bracket']
            ('LEFT', 'RIGHT')
            sage: F is G
            False
            sage: Groups.Commutative.free()
            Traceback (most recent call last):
            ...
            ValueError: either the indices or names must be given
        """
    def __init__(self, indices, prefix, category=None, names=None, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: TestSuite(F).run()
            sage: F = FreeMonoid(index_set=tuple('abcde'))
            sage: TestSuite(F).run()

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: TestSuite(F).run()
            sage: F = FreeAbelianMonoid(index_set=tuple('abcde'))
            sage: TestSuite(F).run()
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is `\\infty` unless this is
        the trivial monoid.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: F.cardinality()
            +Infinity
            sage: F = FreeMonoid(index_set=())
            sage: F.cardinality()
            1

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: F.cardinality()
            +Infinity
            sage: F = FreeAbelianMonoid(index_set=())
            sage: F.cardinality()
            1
        """
    @cached_method
    def monoid_generators(self):
        """
        Return the monoid generators of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: F.monoid_generators()
            Lazy family (Generator map from Integer Ring to
             Free abelian monoid indexed by Integer Ring(i))_{i in Integer Ring}
            sage: F = FreeAbelianMonoid(index_set=tuple('abcde'))
            sage: sorted(F.monoid_generators())
            [F['a'], F['b'], F['c'], F['d'], F['e']]
        """
    gens = monoid_generators

class IndexedFreeMonoid(IndexedMonoid):
    """
    Free monoid with an indexed set of generators.

    INPUT:

    - ``indices`` -- the indices for the generators

    For the optional arguments that control the printing, see
    :class:`~sage.structure.indexed_generators.IndexedGenerators`.

    EXAMPLES::

        sage: F = FreeMonoid(index_set=ZZ)
        sage: F.gen(15)^3 * F.gen(2) * F.gen(15)
        F[15]^3*F[2]*F[15]
        sage: F.gen(1)
        F[1]

    Now we examine some of the printing options::

        sage: F = FreeMonoid(index_set=ZZ, prefix='X', bracket=['|','>'])
        sage: F.gen(2) * F.gen(12)
        X|2>*X|12>
    """
    Element = IndexedFreeMonoidElement
    @cached_method
    def one(self):
        """
        Return the identity element of ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: F.one()
            1
        """
    def gen(self, x):
        """
        The generator indexed by ``x`` of ``self``.

        EXAMPLES::

            sage: F = FreeMonoid(index_set=ZZ)
            sage: F.gen(0)
            F[0]
            sage: F.gen(2)
            F[2]

        TESTS::

            sage: F = FreeMonoid(index_set=[1,2])
            sage: F.gen(2)
            F[2]
            sage: F.gen(0)
            Traceback (most recent call last):
            ...
            IndexError: 0 is not in the index set
        """

class IndexedFreeAbelianMonoid(IndexedMonoid):
    """
    Free abelian monoid with an indexed set of generators.

    INPUT:

    - ``indices`` -- the indices for the generators

    For the optional arguments that control the printing, see
    :class:`~sage.structure.indexed_generators.IndexedGenerators`.

    EXAMPLES::

        sage: F = FreeAbelianMonoid(index_set=ZZ)
        sage: F.gen(15)^3 * F.gen(2) * F.gen(15)
        F[2]*F[15]^4
        sage: F.gen(1)
        F[1]

    Now we examine some of the printing options::

        sage: F = FreeAbelianMonoid(index_set=Partitions(), prefix='A', bracket=False, scalar_mult='%')
        sage: F.gen([3,1,1]) * F.gen([2,2])
        A[2, 2]%A[3, 1, 1]

    .. TODO::

        Implement a subclass when the index sets is finite that utilizes
        vectors or the polydict monomials with the index order fixed.
    """
    Element = IndexedFreeAbelianMonoidElement
    @cached_method
    def one(self):
        """
        Return the identity element of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: F.one()
            1
        """
    def gen(self, x):
        """
        The generator indexed by ``x`` of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(index_set=ZZ)
            sage: F.gen(0)
            F[0]
            sage: F.gen(2)
            F[2]

        TESTS::

            sage: F = FreeAbelianMonoid(index_set=[1,2])
            sage: F.gen(2)
            F[2]
            sage: F.gen(0)
            Traceback (most recent call last):
            ...
            IndexError: 0 is not in the index set

            sage: F = lie_algebras.VirasoroAlgebra(QQ).pbw_basis().indices(); F
            Free abelian monoid indexed by Disjoint union of Family ({'c'}, Integer Ring)
            sage: F.gen('c')
            PBW['c']
        """
