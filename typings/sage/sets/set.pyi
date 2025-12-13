from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.misc.latex import latex as latex
from sage.misc.prandom import choice as choice
from sage.structure.category_object import CategoryObject as CategoryObject
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent, Set_generic as Set_generic
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method

def has_finite_length(obj) -> bool:
    """
    Return ``True`` if ``obj`` is known to have finite length.

    This is mainly meant for pure Python types, so we do not call any
    Sage-specific methods.

    EXAMPLES::

        sage: from sage.sets.set import has_finite_length
        sage: has_finite_length(tuple(range(10)))
        True
        sage: has_finite_length(list(range(10)))
        True
        sage: has_finite_length(set(range(10)))
        True
        sage: has_finite_length(iter(range(10)))
        False
        sage: has_finite_length(GF(17^127))                                             # needs sage.rings.finite_rings
        True
        sage: has_finite_length(ZZ)
        False
    """
def Set(X=None, category=None):
    """
    Create the underlying set of ``X``.

    If ``X`` is a list, tuple, Python set, or ``X.is_finite()`` is
    ``True``, this returns a wrapper around Python's enumerated immutable
    ``frozenset`` type with extra functionality.  Otherwise it returns a
    more formal wrapper.

    If you need the functionality of mutable sets, use Python's
    builtin set type.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: X = Set(GF(9, 'a'))
        sage: X
        {0, 1, 2, a, a + 1, a + 2, 2*a, 2*a + 1, 2*a + 2}
        sage: type(X)
        <class 'sage.sets.set.Set_object_enumerated_with_category'>
        sage: Y = X.union(Set(QQ))
        sage: Y
        Set-theoretic union of
         {0, 1, 2, a, a + 1, a + 2, 2*a, 2*a + 1, 2*a + 2} and
         Set of elements of Rational Field
        sage: type(Y)
        <class 'sage.sets.set.Set_object_union_with_category'>

    Usually sets can be used as dictionary keys.

    ::

        sage: # needs sage.symbolic
        sage: d = {Set([2*I, 1 + I]): 10}
        sage: d                  # key is randomly ordered
        {{I + 1, 2*I}: 10}
        sage: d[Set([1+I,2*I])]
        10
        sage: d[Set((1+I,2*I))]
        10

    The original object is often forgotten.

    ::

        sage: v = [1,2,3]
        sage: X = Set(v)
        sage: X
        {1, 2, 3}
        sage: v.append(5)
        sage: X
        {1, 2, 3}
        sage: 5 in X
        False

    Set also accepts iterators, but be careful to only give *finite*
    sets::

        sage: sorted(Set(range(1,6)))
        [1, 2, 3, 4, 5]
        sage: sorted(Set(list(range(1,6))))
        [1, 2, 3, 4, 5]
        sage: sorted(Set(iter(range(1,6))))
        [1, 2, 3, 4, 5]

    We can also create sets from different types::

        sage: sorted(Set([Sequence([3,1], immutable=True), 5, QQ, Partition([3,1,1])]), key=str)    # needs sage.combinat
        [5, Rational Field, [3, 1, 1], [3, 1]]

    Sets with unhashable objects work, but with less functionality::

        sage: A = Set([QQ, (3, 1), 5])  # hashable
        sage: sorted(A.list(), key=repr)
        [(3, 1), 5, Rational Field]
        sage: type(A)
        <class 'sage.sets.set.Set_object_enumerated_with_category'>
        sage: B = Set([QQ, [3, 1], 5])  # unhashable
        sage: sorted(B.list(), key=repr)
        Traceback (most recent call last):
        ...
        AttributeError: 'Set_object_with_category' object has no attribute 'list'...
        sage: type(B)
        <class 'sage.sets.set.Set_object_with_category'>

    TESTS::

        sage: Set(Primes())
        Set of all prime numbers: 2, 3, 5, 7, ...
        sage: Set(Subsets([1,2,3])).cardinality()
        8
        sage: S = Set(iter([1,2,3])); S
        {1, 2, 3}
        sage: type(S)
        <class 'sage.sets.set.Set_object_enumerated_with_category'>
        sage: S = Set([])
        sage: TestSuite(S).run()

    Check that :issue:`16090` is fixed::

        sage: Set()
        {}
    """

class Set_base:
    """
    Abstract base class for sets, not necessarily parents.
    """
    def union(self, X):
        """
        Return the union of ``self`` and ``X``.

        EXAMPLES::

            sage: Set(QQ).union(Set(ZZ))
            Set-theoretic union of
             Set of elements of Rational Field and
             Set of elements of Integer Ring
            sage: Set(QQ) + Set(ZZ)
            Set-theoretic union of
             Set of elements of Rational Field and
             Set of elements of Integer Ring
            sage: X = Set(QQ).union(Set(GF(3))); X
            Set-theoretic union of
             Set of elements of Rational Field and
             {0, 1, 2}
            sage: 2/3 in X
            True
            sage: GF(3)(2) in X                                                         # needs sage.libs.pari
            True
            sage: GF(5)(2) in X
            False
            sage: sorted(Set(GF(7)) + Set(GF(3)), key=int)
            [0, 0, 1, 1, 2, 2, 3, 4, 5, 6]
        """
    def intersection(self, X):
        """
        Return the intersection of ``self`` and ``X``.

        EXAMPLES::

            sage: X = Set(ZZ).intersection(Primes())
            sage: 4 in X
            False
            sage: 3 in X
            True

            sage: 2/1 in X
            True

            sage: X = Set(GF(9,'b')).intersection(Set(GF(27,'c'))); X                   # needs sage.rings.finite_rings
            {}

            sage: X = Set(GF(9,'b')).intersection(Set(GF(27,'b'))); X                   # needs sage.rings.finite_rings
            {}
        """
    def difference(self, X):
        """
        Return the set difference ``self - X``.

        EXAMPLES::

            sage: X = Set(ZZ).difference(Primes())
            sage: 4 in X
            True
            sage: 3 in X
            False

            sage: 4/1 in X
            True

            sage: X = Set(GF(9,'b')).difference(Set(GF(27,'c'))); X                     # needs sage.rings.finite_rings
            {0, 1, 2, b, b + 1, b + 2, 2*b, 2*b + 1, 2*b + 2}

            sage: X = Set(GF(9,'b')).difference(Set(GF(27,'b'))); X                     # needs sage.rings.finite_rings
            {0, 1, 2, b, b + 1, b + 2, 2*b, 2*b + 1, 2*b + 2}
        """
    def symmetric_difference(self, X):
        """
        Return the symmetric difference of ``self`` and ``X``.

        EXAMPLES::

            sage: X = Set([1,2,3]).symmetric_difference(Set([3,4]))
            sage: X
            {1, 2, 4}
        """

class Set_boolean_operators:
    """
    Mix-in class providing the Boolean operators ``__or__``, ``__and__``, ``__xor__``.

    The operators delegate to the methods ``union``, ``intersection``, and
    ``symmetric_difference``, which need to be implemented by the class.
    """
    def __or__(self, X):
        """
        Return the union of ``self`` and ``X``.

        EXAMPLES::

            sage: Set([2,3]) | Set([3,4])
            {2, 3, 4}
            sage: Set(ZZ) | Set(QQ)
            Set-theoretic union of Set of elements of Integer Ring and Set of elements of Rational Field
        """
    def __and__(self, X):
        """
        Return the intersection of ``self`` and ``X``.

        EXAMPLES::

            sage: Set([2,3]) & Set([3,4])
            {3}
            sage: Set(ZZ) & Set(QQ)
            Set-theoretic intersection of Set of elements of Integer Ring and Set of elements of Rational Field
        """
    def __xor__(self, X):
        """
        Return the symmetric difference of ``self`` and ``X``.

        EXAMPLES::

            sage: X = Set([1,2,3,4])
            sage: Y = Set([1,2])
            sage: X.symmetric_difference(Y)
            {3, 4}
            sage: X.__xor__(Y)
            {3, 4}
        """

class Set_add_sub_operators:
    """
    Mix-in class providing the operators ``__add__`` and ``__sub__``.

    The operators delegate to the methods ``union`` and ``intersection``,
    which need to be implemented by the class.
    """
    def __add__(self, X):
        """
        Return the union of ``self`` and ``X``.

        EXAMPLES::

            sage: Set(RealField()) + Set(QQ^5)                                          # needs sage.modules
             Set-theoretic union of
              Set of elements of Real Field with 53 bits of precision and
              Set of elements of Vector space of dimension 5 over Rational Field
            sage: Set(GF(3)) + Set(GF(2))
            {0, 1, 2, 0, 1}
            sage: Set(GF(2)) + Set(GF(4,'a'))                                           # needs sage.rings.finite_rings
            {0, 1, a, a + 1}
            sage: sorted(Set(GF(8,'b')) + Set(GF(4,'a')), key=str)                      # needs sage.rings.finite_rings
            [0, 0, 1, 1, a, a + 1, b, b + 1, b^2, b^2 + 1, b^2 + b, b^2 + b + 1]
        """
    def __sub__(self, X):
        """
        Return the difference of ``self`` and ``X``.

        EXAMPLES::

            sage: X = Set(ZZ).difference(Primes())
            sage: Y = Set(ZZ) - Primes()
            sage: X == Y
            True
        """

class Set_object(Set_generic, Set_base, Set_boolean_operators, Set_add_sub_operators):
    """
    A set attached to an almost arbitrary object.

    EXAMPLES::

        sage: K = GF(19)
        sage: Set(K)
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}
        sage: S = Set(K)

        sage: latex(S)
        \\left\\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\\right\\}
        sage: TestSuite(S).run()

        sage: latex(Set(ZZ))
        \\Bold{Z}

    TESTS:

    See :issue:`14486`::

        sage: 0 == Set([1]), Set([1]) == 0
        (False, False)
        sage: 1 == Set([0]), Set([0]) == 1
        (False, False)
    """
    def __init__(self, X, category=None) -> None:
        """
        Create a Set_object.

        This function is called by the Set function; users
        shouldn't call this directly.

        EXAMPLES::

            sage: type(Set(QQ))
            <class 'sage.sets.set.Set_object_with_category'>
            sage: Set(QQ).category()
            Category of infinite sets

        TESTS::

            sage: _a, _b = get_coercion_model().canonical_coercion(Set([0]), 0)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            '<class 'sage.sets.set.Set_object_enumerated_with_category'>'
            and 'Integer Ring'
        """
    def __hash__(self):
        """
        Return the hash value of ``self``.

        EXAMPLES::

            sage: hash(Set(QQ)) == hash(QQ)
            True
        """
    def __iter__(self):
        """
        Iterate over the elements of this set.

        EXAMPLES::

            sage: X = Set(ZZ)
            sage: I = X.__iter__()
            sage: next(I)
            0
            sage: next(I)
            1
            sage: next(I)
            -1
            sage: next(I)
            2
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if `x` is in ``self``.

        EXAMPLES::

            sage: X = Set(ZZ)
            sage: 5 in X
            True
            sage: GF(7)(3) in X                                                         # needs sage.libs.pari
            True
            sage: 2/1 in X
            True
            sage: 2/1 in ZZ
            True
            sage: 2/3 in X
            False

        Finite fields better illustrate the difference between
        ``__contains__`` for objects and their underlying sets::

            sage: X = Set(GF(7))
            sage: X
            {0, 1, 2, 3, 4, 5, 6}
            sage: 5/3 in X
            False
            sage: 5/3 in GF(7)
            False
            sage: sorted(Set(GF(7)).union(Set(GF(5))), key=int)
            [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6]
            sage: Set(GF(7)).intersection(Set(GF(5)))
            {}
        """
    def __richcmp__(self, right, op):
        """
        Compare ``self`` and ``right``.

        If ``right`` is not a :class:`Set_object`, return ``NotImplemented``.
        If ``right`` is also a :class:`Set_object`, returns comparison
        on the underlying objects.

        .. NOTE::

           If `X < Y` is true this does *not* necessarily mean
           that `X` is a subset of `Y`.  Also, any two sets can be
           compared still, but the result need not be meaningful
           if they are not equal.

        EXAMPLES::

            sage: Set(ZZ) == Set(QQ)
            False
            sage: Set(ZZ) < Set(QQ)
            True
            sage: Primes() == Set(QQ)
            False
        """
    def cardinality(self):
        """
        Return the cardinality of this set, which is either an integer or
        ``Infinity``.

        EXAMPLES::

            sage: Set(ZZ).cardinality()
            +Infinity
            sage: Primes().cardinality()
            +Infinity
            sage: Set(GF(5)).cardinality()
            5
            sage: Set(GF(5^2,'a')).cardinality()                                        # needs sage.rings.finite_rings
            25
        """
    def is_empty(self):
        """
        Return boolean representing emptiness of the set.

        OUTPUT: ``True`` if the set is empty, ``False`` otherwise

        EXAMPLES::

            sage: Set([]).is_empty()
            True
            sage: Set([0]).is_empty()
            False
            sage: Set([1..100]).is_empty()
            False
            sage: Set(SymmetricGroup(2).list()).is_empty()                              # needs sage.groups
            False
            sage: Set(ZZ).is_empty()
            False

        TESTS::

            sage: Set([]).is_empty()
            True
            sage: Set([1,2,3]).is_empty()
            False
            sage: Set([1..100]).is_empty()
            False
            sage: Set(DihedralGroup(4).list()).is_empty()                               # needs sage.groups
            False
            sage: Set(QQ).is_empty()
            False
        """
    def is_finite(self):
        """
        Return ``True`` if ``self`` is finite.

        EXAMPLES::

            sage: Set(QQ).is_finite()
            False
            sage: Set(GF(250037)).is_finite()                                           # needs sage.rings.finite_rings
            True
            sage: Set(Integers(2^1000000)).is_finite()
            True
            sage: Set([1,'a',ZZ]).is_finite()
            True
        """
    def object(self):
        """
        Return underlying object.

        EXAMPLES::

            sage: X = Set(QQ)
            sage: X.object()
            Rational Field
            sage: X = Primes()
            sage: X.object()
            Set of all prime numbers: 2, 3, 5, 7, ...
        """
    def subsets(self, size=None):
        """
        Return the :class:`Subsets` object representing the subsets of a set.
        If size is specified, return the subsets of that size.

        EXAMPLES::

            sage: X = Set([1, 2, 3])
            sage: list(X.subsets())
            [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
            sage: list(X.subsets(2))
            [{1, 2}, {1, 3}, {2, 3}]
        """
    def subsets_lattice(self):
        """
        Return the lattice of subsets ordered by containment.

        EXAMPLES::

            sage: X = Set([1,2,3])
            sage: X.subsets_lattice()                                                   # needs sage.graphs
            Finite lattice containing 8 elements
            sage: Y = Set()
            sage: Y.subsets_lattice()                                                   # needs sage.graphs
            Finite lattice containing 1 elements
        """

class Set_object_enumerated(Set_object):
    """
    A finite enumerated set.
    """
    def __init__(self, X, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = Set(GF(19)); S
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}
            sage: S.category()
            Category of finite enumerated sets
            sage: print(latex(S))
            \\left\\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\\right\\}
            sage: TestSuite(S).run()
        """
    def random_element(self):
        """
        Return a random element in this set.

        EXAMPLES::

            sage: Set([1,2,3]).random_element() # random
            2
        """
    def is_finite(self):
        """
        Return ``True`` as this is a finite set.

        EXAMPLES::

            sage: Set(GF(19)).is_finite()
            True
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: Set([1,1]).cardinality()
            1
        """
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: len(Set([1,1]))
            1
        """
    def __iter__(self):
        """
        Iterating through the elements of ``self``.

        EXAMPLES::

            sage: S = Set(GF(19))
            sage: I = iter(S)
            sage: next(I)
            0
            sage: next(I)
            1
            sage: next(I)
            2
            sage: next(I)
            3
        """
    def list(self):
        """
        Return the elements of ``self``, as a list.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: X = Set(GF(8,'c'))
            sage: X
            {0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1}
            sage: X.list()
            [0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1]
            sage: type(X.list())
            <... 'list'>

        .. TODO::

            FIXME: What should be the order of the result?
            That of ``self.object()``? Or the order given by
            ``set(self.object())``? Note that :meth:`__getitem__` is
            currently implemented in term of this list method, which
            is really inefficient ...
        """
    def set(self):
        """
        Return the Python set object associated to this set.

        Python has a notion of finite set, and often Sage sets
        have an associated Python set.  This function returns
        that set.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: X = Set(GF(8,'c'))
            sage: X
            {0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1}
            sage: X.set()
            {0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1}
            sage: type(X.set())
            <... 'set'>
            sage: type(X)
            <class 'sage.sets.set.Set_object_enumerated_with_category'>
        """
    def frozenset(self):
        """
        Return the Python frozenset object associated to this set,
        which is an immutable set (hence hashable).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: X = Set(GF(8,'c'))
            sage: X
            {0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1}
            sage: s = X.set(); s
            {0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1}
            sage: hash(s)
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'set'
            sage: s = X.frozenset(); s
            frozenset({0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1})

            sage: hash(s) != hash(tuple(X.set()))                                       # needs sage.rings.finite_rings
            True

            sage: type(s)                                                               # needs sage.rings.finite_rings
            <... 'frozenset'>
        """
    def __hash__(self):
        """
        Return the hash of ``self`` (as a ``frozenset``).

        EXAMPLES::

            sage: s = Set(GF(8,'c'))                                                    # needs sage.rings.finite_rings
            sage: hash(s) == hash(s)                                                    # needs sage.rings.finite_rings
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare the sets ``self`` and ``other``.

        EXAMPLES::

            sage: X = Set(GF(8,'c'))                                                    # needs sage.rings.finite_rings
            sage: X == Set(GF(8,'c'))                                                   # needs sage.rings.finite_rings
            True
            sage: X == Set(GF(4,'a'))                                                   # needs sage.rings.finite_rings
            False
            sage: Set(QQ) == Set(ZZ)
            False
            sage: Set([1]) == set([1])
            True

        Test set equality and inequality::

            sage: L = {0}
            sage: S = Set(L)
            sage: S == L
            True
            sage: S != L
            False
        """
    def issubset(self, other):
        """
        Return whether ``self`` is a subset of ``other``.

        INPUT:

        - ``other`` -- a finite Set

        EXAMPLES::

            sage: X = Set([1,3,5])
            sage: Y = Set([0,1,2,3,5,7])
            sage: X.issubset(Y)
            True
            sage: Y.issubset(X)
            False
            sage: X.issubset(X)
            True

        TESTS::

            sage: len([Z for Z in Y.subsets() if Z.issubset(X)])
            8
        """
    def issuperset(self, other):
        """
        Return whether ``self`` is a superset of ``other``.

        INPUT:

        - ``other`` -- a finite Set

        EXAMPLES::

            sage: X = Set([1,3,5])
            sage: Y = Set([0,1,2,3,5])
            sage: X.issuperset(Y)
            False
            sage: Y.issuperset(X)
            True
            sage: X.issuperset(X)
            True

        TESTS::

            sage: len([Z for Z in Y.subsets() if Z.issuperset(X)])
            4
        """
    def union(self, other):
        """
        Return the union of ``self`` and ``other``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: X = Set(GF(8,'c'))
            sage: Y = Set([GF(8,'c').0, 1, 2, 3])
            sage: X
            {0, 1, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1}
            sage: sorted(Y)
            [1, 2, 3, c]
            sage: sorted(X.union(Y), key=str)
            [0, 1, 2, 3, c, c + 1, c^2, c^2 + 1, c^2 + c, c^2 + c + 1]
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: X = Set(GF(8,'c'))                                                    # needs sage.rings.finite_rings
            sage: Y = Set([GF(8,'c').0, 1, 2, 3])                                       # needs sage.rings.finite_rings
            sage: sorted(X.intersection(Y), key=str)                                    # needs sage.rings.finite_rings
            [1, c]
        """
    def difference(self, other):
        """
        Return the set difference ``self - other``.

        EXAMPLES::

            sage: X = Set([1,2,3,4])
            sage: Y = Set([1,2])
            sage: X.difference(Y)
            {3, 4}
            sage: Z = Set(ZZ)
            sage: W = Set([2.5, 4, 5, 6])
            sage: W.difference(Z)                                                       # needs sage.rings.real_mpfr
            {2.50000000000000}
        """
    def symmetric_difference(self, other):
        """
        Return the symmetric difference of ``self`` and ``other``.

        EXAMPLES::

            sage: X = Set([1,2,3,4])
            sage: Y = Set([1,2])
            sage: X.symmetric_difference(Y)
            {3, 4}
            sage: Z = Set(ZZ)
            sage: W = Set([2.5, 4, 5, 6])
            sage: U = W.symmetric_difference(Z)
            sage: 2.5 in U
            True
            sage: 4 in U
            False
            sage: V = Z.symmetric_difference(W)
            sage: V == U
            True
            sage: 2.5 in V
            True
            sage: 6 in V
            False
        """

class Set_object_binary(Set_object, metaclass=ClasscallMetaclass):
    '''
    An abstract common base class for sets defined by a binary operation (ex.
    :class:`Set_object_union`, :class:`Set_object_intersection`,
    :class:`Set_object_difference`, and
    :class:`Set_object_symmetric_difference`).

    INPUT:

    - ``X``, ``Y`` -- sets, the operands to ``op``

    - ``op`` -- string describing the binary operation

    - ``latex_op`` -- string used for rendering this object in LaTeX

    EXAMPLES::

        sage: X = Set(QQ^2)                                                             # needs sage.modules
        sage: Y = Set(ZZ)
        sage: from sage.sets.set import Set_object_binary
        sage: S = Set_object_binary(X, Y, "union", "\\\\cup"); S                          # needs sage.modules
        Set-theoretic union of
         Set of elements of Vector space of dimension 2 over Rational Field and
         Set of elements of Integer Ring
    '''
    @staticmethod
    def __classcall__(cls, X, Y, *args, **kwds):
        '''
        Convert the operands to instances of :class:`Set_object` if necessary.

        TESTS::

            sage: from sage.sets.set import Set_object_binary
            sage: X = QQ^2                                                              # needs sage.modules
            sage: Y = ZZ
            sage: Set_object_binary(X, Y, "union", "\\\\cup")                             # needs sage.modules
            Set-theoretic union of
             Set of elements of Vector space of dimension 2 over Rational Field and
             Set of elements of Integer Ring
        '''
    def __init__(self, X, Y, op, latex_op, category=None) -> None:
        '''
        Initialization.

        TESTS::

            sage: from sage.sets.set import Set_object_binary
            sage: X = Set(QQ^2)                                                         # needs sage.modules
            sage: Y = Set(ZZ)
            sage: S = Set_object_binary(X, Y, "union", "\\\\cup")                         # needs sage.modules
            sage: type(S)                                                               # needs sage.modules
            <class \'sage.sets.set.Set_object_binary_with_category\'>
        '''
    def __hash__(self):
        """
        The hash value of this set.

        EXAMPLES:

        The hash values of equal sets are in general not equal since it is not
        decidable whether two sets are equal::

            sage: X = Set(GF(13)).intersection(Set(ZZ))
            sage: Y = Set(ZZ).intersection(Set(GF(13)))
            sage: hash(X) == hash(Y)
            False

        TESTS:

        Test that :issue:`14432` has been resolved::

            sage: S = Set(ZZ).union(Set([infinity]))
            sage: T = Set(ZZ).union(Set([infinity]))
            sage: hash(S) == hash(T)
            True
        """

class Set_object_union(Set_object_binary):
    """
    A formal union of two sets.
    """
    def __init__(self, X, Y, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: S = Set(QQ^2)
            sage: T = Set(ZZ)
            sage: X = S.union(T); X
            Set-theoretic union of
             Set of elements of Vector space of dimension 2 over Rational Field and
             Set of elements of Integer Ring
            sage: X.category()
            Category of infinite sets
            sage: latex(X)
            \\Bold{Q}^{2} \\cup \\Bold{Z}
            sage: TestSuite(X).run()
        """
    def is_finite(self):
        """
        Return whether this set is finite.

        EXAMPLES::

            sage: X = Set(range(10))
            sage: Y = Set(range(-10,0))
            sage: Z = Set(Primes())
            sage: X.union(Y).is_finite()
            True
            sage: X.union(Z).is_finite()
            False
        """
    def __richcmp__(self, right, op):
        """
        Try to compare ``self`` and ``right``.

        .. NOTE::

           Comparison is basically not implemented, or rather it could
           say sets are not equal even though they are.  I don't know
           how one could implement this for a generic union of sets in
           a meaningful manner.  So be careful when using this.

        EXAMPLES::

            sage: # needs sage.modules
            sage: Y = Set(ZZ^2).union(Set(ZZ^3))
            sage: X = Set(ZZ^3).union(Set(ZZ^2))
            sage: X == Y
            True
            sage: Y == X
            True

        This illustrates that equality testing for formal unions
        can be misleading in general.

        ::

            sage: Set(ZZ).union(Set(QQ)) == Set(QQ)
            False
        """
    def __iter__(self):
        """
        Return iterator over the elements of ``self``.

        EXAMPLES::

            sage: [x for x in Set(GF(3)).union(Set(GF(2)))]
            [0, 1, 2, 0, 1]
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is an element of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: X = Set(GF(3)).union(Set(GF(2)))
            sage: GF(5)(1) in X
            False
            sage: GF(3)(2) in X
            True
            sage: GF(2)(0) in X
            True
            sage: GF(5)(0) in X
            False
        """
    def cardinality(self):
        """
        Return the cardinality of this set.

        EXAMPLES::

            sage: X = Set(GF(3)).union(Set(GF(2)))
            sage: X
            {0, 1, 2, 0, 1}
            sage: X.cardinality()
            5

            sage: X = Set(GF(3)).union(Set(ZZ))
            sage: X.cardinality()
            +Infinity
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if this set is not empty.

        EXAMPLES::

            sage: bool(Set(GF(3)).union(Set(GF(2))))
            True
            sage: bool(Set(GF(3)).intersection(Set(GF(2))))
            False

        TESTS:

        This should still work in the case the first set is nonempty
        and the second set has :meth:`is_empty` unimplemented::

            sage: C = ConditionSet(QQ, lambda x: x > 0)
            sage: C.is_empty()
            Traceback (most recent call last):
            ...
            AttributeError...
            sage: C.is_finite()
            Traceback (most recent call last):
            ...
            AttributeError...
            sage: bool(Set([1]) + C)
            True
            sage: (Set([1]) + C).is_empty()
            False
        """

class Set_object_intersection(Set_object_binary):
    """
    Formal intersection of two sets.
    """
    def __init__(self, X, Y, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: S = Set(QQ^2)
            sage: T = Set(ZZ)
            sage: X = S.intersection(T); X
            Set-theoretic intersection of
             Set of elements of Vector space of dimension 2 over Rational Field and
             Set of elements of Integer Ring
            sage: X.category()
            Category of enumerated sets
            sage: latex(X)
            \\Bold{Q}^{2} \\cap \\Bold{Z}

            sage: X = Set(IntegerRange(100)).intersection(Primes())
            sage: X.is_finite()
            True
            sage: X.cardinality()
            25
            sage: X.category()
            Category of finite enumerated sets
            sage: TestSuite(X).run()

            sage: X = Set(Primes(), category=Sets()).intersection(Set(IntegerRange(200)))
            sage: X.cardinality()
            46
            sage: TestSuite(X).run()
        """
    def is_finite(self):
        """
        Return whether this set is finite.

        EXAMPLES::

            sage: X = Set(IntegerRange(100))
            sage: Y = Set(ZZ)
            sage: X.intersection(Y).is_finite()
            True
            sage: Y.intersection(X).is_finite()
            True
            sage: Y.intersection(Set(QQ)).is_finite()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __richcmp__(self, right, op):
        """
        Try to compare ``self`` and ``right``.

        .. NOTE::

           Comparison is basically not implemented, or rather it could
           say sets are not equal even though they are.  I don't know
           how one could implement this for a generic intersection of
           sets in a meaningful manner.  So be careful when using this.

        EXAMPLES::

            sage: Y = Set(ZZ).intersection(Set(QQ))
            sage: X = Set(QQ).intersection(Set(ZZ))
            sage: X == Y
            True
            sage: Y == X
            True

        This illustrates that equality testing for formal unions
        can be misleading in general.

        ::

            sage: Set(ZZ).intersection(Set(QQ)) == Set(QQ)
            False
        """
    def __iter__(self):
        """
        Return iterator through elements of ``self``.

        ``self`` is a formal intersection of `X` and `Y` and this function is
        implemented by iterating through the elements of `X` and for
        each checking if it is in `Y`, and if yielding it.

        EXAMPLES::

            sage: X = Set(ZZ).intersection(Primes())
            sage: I = X.__iter__()
            sage: next(I)
            2

        Check that known finite intersections have finite iterators (see
        :issue:`18159`)::

            sage: P = Set(ZZ).intersection(Set(range(10,20)))
            sage: list(P)
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``self`` contains ``x``.

        Since ``self`` is a formal intersection of `X` and `Y` this function
        returns ``True`` if both `X` and `Y` contains ``x``.

        EXAMPLES::

            sage: X = Set(QQ).intersection(Set(RR))
            sage: 5 in X
            True
            sage: ComplexField().0 in X                                                 # needs sage.rings.real_mpfr
            False

        Any specific floating-point number in Sage is to finite precision,
        hence it is rational::

            sage: RR(sqrt(2)) in X                                                      # needs sage.rings.real_mpfr sage.symbolic
            True

        Real constants are not rational::

            sage: pi in X                                                               # needs sage.symbolic
            False
        """

class Set_object_difference(Set_object_binary):
    """
    Formal difference of two sets.
    """
    def __init__(self, X, Y, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = Set(QQ)
            sage: T = Set(ZZ)
            sage: X = S.difference(T); X
            Set-theoretic difference of
             Set of elements of Rational Field and
             Set of elements of Integer Ring
            sage: X.category()
            Category of sets
            sage: latex(X)
            \\Bold{Q} - \\Bold{Z}

            sage: TestSuite(X).run()
        """
    def is_finite(self):
        """
        Return whether this set is finite.

        EXAMPLES::

            sage: X = Set(range(10))
            sage: Y = Set(range(-10,5))
            sage: Z = Set(QQ)
            sage: X.difference(Y).is_finite()
            True
            sage: X.difference(Z).is_finite()
            True
            sage: Z.difference(X).is_finite()
            False
            sage: Z.difference(Set(ZZ)).is_finite()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __richcmp__(self, right, op):
        """
        Try to compare ``self`` and ``right``.

        .. NOTE::

           Comparison is basically not implemented, or rather it could
           say sets are not equal even though they are.  I don't know
           how one could implement this for a generic intersection of
           sets in a meaningful manner.  So be careful when using
           this.

        EXAMPLES::

            sage: Y = Set(ZZ).difference(Set(QQ))
            sage: Y == Set([])
            False
            sage: X = Set(QQ).difference(Set(ZZ))
            sage: Y == X
            False
            sage: Z = X.difference(Set(ZZ))
            sage: Z == X
            False

        This illustrates that equality testing for formal unions
        can be misleading in general.

        ::

            sage: X == Set(QQ).difference(Set(ZZ))
            True
        """
    def __iter__(self):
        """
        Return iterator through elements of ``self``.

        ``self`` is a formal difference of `X` and `Y` and this function
        is implemented by iterating through the elements of `X` and for
        each checking if it is not in `Y`, and if yielding it.

        EXAMPLES::

            sage: X = Set(ZZ).difference(Primes())
            sage: I = X.__iter__()
            sage: next(I)
            0
            sage: next(I)
            1
            sage: next(I)
            -1
            sage: next(I)
            -2
            sage: next(I)
            -3
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``self`` contains ``x``.

        Since ``self`` is a formal intersection of `X` and `Y` this function
        returns ``True`` if both `X` and `Y` contains ``x``.

        EXAMPLES::

            sage: X = Set(QQ).difference(Set(ZZ))
            sage: 5 in X
            False
            sage: ComplexField().0 in X                                                 # needs sage.rings.real_mpfr
            False
            sage: sqrt(2) in X     # since sqrt(2) is not a numerical approx            # needs sage.symbolic
            False
            sage: sqrt(RR(2)) in X  # since sqrt(RR(2)) is a numerical approx           # needs sage.rings.real_interval_field
            True
            sage: 5/2 in X
            True
        """

class Set_object_symmetric_difference(Set_object_binary):
    """
    Formal symmetric difference of two sets.
    """
    def __init__(self, X, Y, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = Set(QQ)
            sage: T = Set(ZZ)
            sage: X = S.symmetric_difference(T); X
            Set-theoretic symmetric difference of Set of elements of Rational Field and Set of elements of Integer Ring
            sage: X.category()
            Category of sets
            sage: latex(X)
            \\Bold{Q} \\bigtriangleup \\Bold{Z}

            sage: TestSuite(X).run()
        """
    def is_finite(self):
        """
        Return whether this set is finite.

        EXAMPLES::

            sage: X = Set(range(10))
            sage: Y = Set(range(-10,5))
            sage: Z = Set(QQ)
            sage: X.symmetric_difference(Y).is_finite()
            True
            sage: X.symmetric_difference(Z).is_finite()
            False
            sage: Z.symmetric_difference(X).is_finite()
            False
            sage: Z.symmetric_difference(Set(ZZ)).is_finite()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __richcmp__(self, right, op):
        """
        Try to compare ``self`` and ``right``.

        .. NOTE::

           Comparison is basically not implemented, or rather it could
           say sets are not equal even though they are.  I don't know
           how one could implement this for a generic symmetric
           difference of sets in a meaningful manner.  So be careful
           when using this.

        EXAMPLES::

            sage: Y = Set(ZZ).symmetric_difference(Set(QQ))
            sage: X = Set(QQ).symmetric_difference(Set(ZZ))
            sage: X == Y
            True
            sage: Y == X
            True
        """
    def __iter__(self):
        """
        Return iterator through elements of ``self``.

        This function is implemented by first iterating through the elements
        of `X` and  yielding it if it is not in `Y`.
        Then it will iterate throw all the elements of `Y` and yielding it if
        it is not in `X`.

        EXAMPLES::

            sage: X = Set(ZZ).symmetric_difference(Primes())
            sage: I = X.__iter__()
            sage: next(I)
            0
            sage: next(I)
            1
            sage: next(I)
            -1
            sage: next(I)
            -2
            sage: next(I)
            -3
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``self`` contains ``x``.

        Since ``self`` is the formal symmetric difference of `X` and `Y`
        this function returns ``True`` if either `X` or `Y` (but not both)
        contains ``x``.

        EXAMPLES::

            sage: X = Set(QQ).symmetric_difference(Primes())
            sage: 4 in X
            True
            sage: ComplexField().0 in X                                                 # needs sage.rings.real_mpfr
            False
            sage: sqrt(2) in X      # since sqrt(2) is currently symbolic               # needs sage.symbolic
            False
            sage: sqrt(RR(2)) in X  # since sqrt(RR(2)) is currently approximated       # needs sage.rings.real_interval_field
            True
            sage: pi in X                                                               # needs sage.symbolic
            False
            sage: 5/2 in X
            True
            sage: 3 in X
            False
        """
