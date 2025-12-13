from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.sage_object import SageObject as SageObject

def repr_short_to_parent(s):
    """
    Helper method for the growth group factory, which converts a short
    representation string to a parent.

    INPUT:

    - ``s`` -- string; short representation of a parent

    OUTPUT: a parent

    The possible short representations are shown in the examples below.

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import repr_short_to_parent
        sage: repr_short_to_parent('ZZ')
        Integer Ring
        sage: repr_short_to_parent('QQ')
        Rational Field
        sage: repr_short_to_parent('SR')
        Symbolic Ring
        sage: repr_short_to_parent('NN')
        Non negative integer semiring
        sage: repr_short_to_parent('UU')
        Group of Roots of Unity

    TESTS::

        sage: repr_short_to_parent('abcdef')
        Traceback (most recent call last):
        ...
        ValueError: Cannot create a parent out of 'abcdef'.
        > *previous* ValueError: unknown specification abcdef
        > *and* NameError: name 'abcdef' is not defined
    """
def parent_to_repr_short(P):
    """
    Helper method which generates a short(er) representation string
    out of a parent.

    INPUT:

    - ``P`` -- a parent

    OUTPUT: string

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import parent_to_repr_short
        sage: parent_to_repr_short(ZZ)
        'ZZ'
        sage: parent_to_repr_short(QQ)
        'QQ'
        sage: parent_to_repr_short(SR)
        'SR'
        sage: parent_to_repr_short(RR)
        'RR'
        sage: parent_to_repr_short(CC)
        'CC'
        sage: parent_to_repr_short(ZZ['x'])
        'ZZ[x]'
        sage: parent_to_repr_short(QQ['d, k'])
        'QQ[d, k]'
        sage: parent_to_repr_short(QQ['e'])
        'QQ[e]'
        sage: parent_to_repr_short(SR[['a, r']])
        'SR[[a, r]]'
        sage: parent_to_repr_short(Zmod(3))
        'Ring of integers modulo 3'
        sage: parent_to_repr_short(Zmod(3)['g'])
        'Univariate Polynomial Ring in g over Ring of integers modulo 3'
    """
def split_str_by_op(string, op, strip_parentheses: bool = True):
    """
    Split the given string into a tuple of substrings arising by
    splitting by ``op`` and taking care of parentheses.

    INPUT:

    - ``string`` -- string

    - ``op`` -- string; this is used by
      :python:`str.split <library/stdtypes.html#str.split>`.
      Thus, if this is ``None``, then any whitespace string is a
      separator and empty strings are removed from the result.

    - ``strip_parentheses`` -- boolean (default: ``True``)

    OUTPUT: a tuple of strings

    TESTS::

        sage: from sage.rings.asymptotic.misc import split_str_by_op
        sage: split_str_by_op('x^ZZ', '*')
        ('x^ZZ',)
        sage: split_str_by_op('log(x)^ZZ * y^QQ', '*')
        ('log(x)^ZZ', 'y^QQ')
        sage: split_str_by_op('log(x)**ZZ * y**QQ', '*')
        ('log(x)**ZZ', 'y**QQ')
        sage: split_str_by_op('a^b * * c^d', '*')
        Traceback (most recent call last):
        ...
        ValueError: 'a^b * * c^d' is invalid since a '*' follows a '*'.
        sage: split_str_by_op('a^b * (c*d^e)', '*')
        ('a^b', 'c*d^e')

    ::

        sage: split_str_by_op('(a^b)^c', '^')
        ('a^b', 'c')
        sage: split_str_by_op('a^(b^c)', '^')
        ('a', 'b^c')

    ::

        sage: split_str_by_op('(a) + (b)', op='+', strip_parentheses=True)
        ('a', 'b')
        sage: split_str_by_op('(a) + (b)', op='+', strip_parentheses=False)
        ('(a)', '(b)')
        sage: split_str_by_op(' ( t  ) ', op='+', strip_parentheses=False)
        ('( t  )',)

    ::

        sage: split_str_by_op(' ( t  ) ', op=None)
        ('t',)
        sage: split_str_by_op(' ( t  )s', op=None)
        ('(t)s',)
        sage: split_str_by_op(' ( t  ) s', op=None)
        ('t', 's')

    ::

        sage: split_str_by_op('(e^(n*log(n)))^SR.subring(no_variables=True)', '*')
        ('(e^(n*log(n)))^SR.subring(no_variables=True)',)
    """
def repr_op(left, op, right=None, latex: bool = False):
    """
    Create a string ``left op right`` with
    taking care of parentheses in its operands.

    INPUT:

    - ``left`` -- an element

    - ``op`` -- string

    - ``right`` -- an element

    - ``latex`` -- boolean (default: ``False``); if set, then
      LaTeX-output is returned

    OUTPUT: string

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import repr_op
        sage: repr_op('a^b', '^', 'c')
        '(a^b)^c'

    TESTS::

        sage: repr_op('a-b', '^', 'c')
        '(a-b)^c'
        sage: repr_op('a+b', '^', 'c')
        '(a+b)^c'

    ::

        sage: print(repr_op(r'\\frac{1}{2}', '^', 'c', latex=True))
        \\left(\\frac{1}{2}\\right)^c

    ::

        sage: repr_op('Arg', '_', 'Symbolic Ring')
        'Arg_(Symbolic Ring)'
    """
def combine_exceptions(e, *f):
    """
    Helper function which combines the messages of the given exceptions.

    INPUT:

    - ``e`` -- an exception

    - ``*f`` -- exceptions

    OUTPUT: an exception

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import combine_exceptions
        sage: raise combine_exceptions(ValueError('Outer.'), TypeError('Inner.'))
        Traceback (most recent call last):
        ...
        ValueError: Outer.
        > *previous* TypeError: Inner.
        sage: raise combine_exceptions(ValueError('Outer.'),
        ....:                          TypeError('Inner1.'), TypeError('Inner2.'))
        Traceback (most recent call last):
        ...
        ValueError: Outer.
        > *previous* TypeError: Inner1.
        > *and* TypeError: Inner2.
        sage: raise combine_exceptions(ValueError('Outer.'),
        ....:                          combine_exceptions(TypeError('Middle.'),
        ....:                                             TypeError('Inner.')))
        Traceback (most recent call last):
        ...
        ValueError: Outer.
        > *previous* TypeError: Middle.
        >> *previous* TypeError: Inner.
    """
def substitute_raise_exception(element, e) -> None:
    """
    Raise an error describing what went wrong with the substitution.

    INPUT:

    - ``element`` -- an element

    - ``e`` -- an exception which is included in the raised error message

    OUTPUT: raise an exception of the same type as ``e``

    TESTS::

        sage: from sage.rings.asymptotic.misc import substitute_raise_exception
        sage: substitute_raise_exception(x, Exception('blub'))
        Traceback (most recent call last):
        ...
        Exception: Cannot substitute in x in Symbolic Ring.
        > *previous* Exception: blub
    """
def bidirectional_merge_overlapping(A, B, key=None):
    """
    Merge the two overlapping tuples/lists.

    INPUT:

    - ``A`` -- list or tuple (type has to coincide with type of ``B``)

    - ``B`` -- list or tuple (type has to coincide with type of ``A``)

    - ``key`` -- (default: ``None``) a function. If ``None``, then the
      identity is used.  This ``key``-function applied on an element
      of the list/tuple is used for comparison. Thus elements with the
      same key are considered as equal.

    OUTPUT:

    A pair of lists or tuples (depending on the type of ``A`` and ``B``).

    .. NOTE::

        Suppose we can decompose the list `A=ac` and `B=cb` with
        lists `a`, `b`, `c`, where `c` is nonempty. Then
        :func:`bidirectional_merge_overlapping` returns the pair `(acb, acb)`.

        Suppose a ``key``-function is specified and `A=ac_A` and
        `B=c_Bb`, where the list of keys of the elements of `c_A`
        equals the list of keys of the elements of `c_B`. Then
        :func:`bidirectional_merge_overlapping` returns the pair `(ac_Ab, ac_Bb)`.

        After unsuccessfully merging `A=ac` and `B=cb`,
        a merge of `A=ca` and `B=bc` is tried.

    TESTS::

        sage: from sage.rings.asymptotic.misc import bidirectional_merge_overlapping
        sage: def f(L, s):
        ....:     return list((ell, s) for ell in L)
        sage: key = lambda k: k[0]
        sage: bidirectional_merge_overlapping(f([0..3], 'a'), f([5..7], 'b'), key)
        Traceback (most recent call last):
        ...
        ValueError: Input does not have an overlap.
        sage: bidirectional_merge_overlapping(f([0..2], 'a'), f([4..7], 'b'), key)
        Traceback (most recent call last):
        ...
        ValueError: Input does not have an overlap.
        sage: bidirectional_merge_overlapping(f([4..7], 'a'), f([0..2], 'b'), key)
        Traceback (most recent call last):
        ...
        ValueError: Input does not have an overlap.
        sage: bidirectional_merge_overlapping(f([0..3], 'a'), f([3..4], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a'), (4, 'b')],
         [(0, 'a'), (1, 'a'), (2, 'a'), (3, 'b'), (4, 'b')])
        sage: bidirectional_merge_overlapping(f([3..4], 'a'), f([0..3], 'b'), key)
        ([(0, 'b'), (1, 'b'), (2, 'b'), (3, 'a'), (4, 'a')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b'), (4, 'a')])
        sage: bidirectional_merge_overlapping(f([0..1], 'a'), f([0..4], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'b'), (3, 'b'), (4, 'b')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b'), (4, 'b')])
        sage: bidirectional_merge_overlapping(f([0..3], 'a'), f([0..1], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'b'), (1, 'b'), (2, 'a'), (3, 'a')])
        sage: bidirectional_merge_overlapping(f([0..3], 'a'), f([1..3], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'a'), (1, 'b'), (2, 'b'), (3, 'b')])
        sage: bidirectional_merge_overlapping(f([1..3], 'a'), f([0..3], 'b'), key)
        ([(0, 'b'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b')])
        sage: bidirectional_merge_overlapping(f([0..6], 'a'), f([3..4], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a'), (4, 'a'), (5, 'a'), (6, 'a')],
         [(0, 'a'), (1, 'a'), (2, 'a'), (3, 'b'), (4, 'b'), (5, 'a'), (6, 'a')])
        sage: bidirectional_merge_overlapping(f([0..3], 'a'), f([1..2], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'a'), (1, 'b'), (2, 'b'), (3, 'a')])
        sage: bidirectional_merge_overlapping(f([1..2], 'a'), f([0..3], 'b'), key)
        ([(0, 'b'), (1, 'a'), (2, 'a'), (3, 'b')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b')])
        sage: bidirectional_merge_overlapping(f([1..3], 'a'), f([1..3], 'b'), key)
        ([(1, 'a'), (2, 'a'), (3, 'a')],
         [(1, 'b'), (2, 'b'), (3, 'b')])
    """
def bidirectional_merge_sorted(A, B, key=None):
    """
    Merge the two tuples/lists, keeping the orders provided by them.

    INPUT:

    - ``A`` -- list or tuple (type has to coincide with type of ``B``)

    - ``B`` -- list or tuple (type has to coincide with type of ``A``)

    - ``key`` -- (default: ``None``) a function. If ``None``, then the
      identity is used.  This ``key``-function applied on an element
      of the list/tuple is used for comparison. Thus elements with the
      same key are considered as equal.

    .. NOTE::

        The two tuples/list need to overlap, i.e. need at least
        one key in common.

    OUTPUT:

    A pair of lists containing all elements totally ordered. (The first
    component uses ``A`` as a merge base, the second component ``B``.)

    If merging fails, then a
    :python:`RuntimeError<library/exceptions.html#exceptions.RuntimeError>`
    is raised.

    TESTS::

        sage: from sage.rings.asymptotic.misc import bidirectional_merge_sorted
        sage: def f(L, s):
        ....:     return list((ell, s) for ell in L)
        sage: key = lambda k: k[0]
        sage: bidirectional_merge_sorted(f([0..3], 'a'), f([5..7], 'b'), key)
        Traceback (most recent call last):
        ...
        RuntimeError: no common elements
        sage: bidirectional_merge_sorted(f([0..2], 'a'), f([4..7], 'b'), key)
        Traceback (most recent call last):
        ...
        RuntimeError: no common elements
        sage: bidirectional_merge_sorted(f([4..7], 'a'), f([0..2], 'b'), key)
        Traceback (most recent call last):
        ...
        RuntimeError: no common elements
        sage: bidirectional_merge_sorted(f([0..3], 'a'), f([3..4], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a'), (4, 'b')],
         [(0, 'a'), (1, 'a'), (2, 'a'), (3, 'b'), (4, 'b')])
        sage: bidirectional_merge_sorted(f([3..4], 'a'), f([0..3], 'b'), key)
        ([(0, 'b'), (1, 'b'), (2, 'b'), (3, 'a'), (4, 'a')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b'), (4, 'a')])
        sage: bidirectional_merge_sorted(f([0..1], 'a'), f([0..4], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'b'), (3, 'b'), (4, 'b')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b'), (4, 'b')])
        sage: bidirectional_merge_sorted(f([0..3], 'a'), f([0..1], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'b'), (1, 'b'), (2, 'a'), (3, 'a')])
        sage: bidirectional_merge_sorted(f([0..3], 'a'), f([1..3], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'a'), (1, 'b'), (2, 'b'), (3, 'b')])
        sage: bidirectional_merge_sorted(f([1..3], 'a'), f([0..3], 'b'), key)
        ([(0, 'b'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b')])
        sage: bidirectional_merge_sorted(f([0..6], 'a'), f([3..4], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a'), (4, 'a'), (5, 'a'), (6, 'a')],
         [(0, 'a'), (1, 'a'), (2, 'a'), (3, 'b'), (4, 'b'), (5, 'a'), (6, 'a')])
        sage: bidirectional_merge_sorted(f([0..3], 'a'), f([1..2], 'b'), key)
        ([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')],
         [(0, 'a'), (1, 'b'), (2, 'b'), (3, 'a')])
        sage: bidirectional_merge_sorted(f([1..2], 'a'), f([0..3], 'b'), key)
        ([(0, 'b'), (1, 'a'), (2, 'a'), (3, 'b')],
         [(0, 'b'), (1, 'b'), (2, 'b'), (3, 'b')])
        sage: bidirectional_merge_sorted(f([1..3], 'a'), f([1..3], 'b'), key)
        ([(1, 'a'), (2, 'a'), (3, 'a')],
         [(1, 'b'), (2, 'b'), (3, 'b')])

    ::

        sage: bidirectional_merge_sorted(f([1, 2, 3], 'a'), f([1, 3], 'b'), key)
        ([(1, 'a'), (2, 'a'), (3, 'a')],
         [(1, 'b'), (2, 'a'), (3, 'b')])
        sage: bidirectional_merge_sorted(f([1, 4, 5, 6], 'a'), f([1, 2, 3, 4, 6], 'b'), key)
        ([(1, 'a'), (2, 'b'), (3, 'b'), (4, 'a'), (5, 'a'), (6, 'a')],
         [(1, 'b'), (2, 'b'), (3, 'b'), (4, 'b'), (5, 'a'), (6, 'b')])
        sage: bidirectional_merge_sorted(f([1, 2, 3, 4], 'a'), f([1, 3, 5], 'b'), key)
        Traceback (most recent call last):
        ...
        RuntimeError: sorting not unique
        sage: bidirectional_merge_sorted(f([1, 2], 'a'), f([2, 1], 'b'), key)
        Traceback (most recent call last):
        ...
        RuntimeError: sorting in lists not compatible
        sage: bidirectional_merge_sorted(f([1, 2, 4], 'a'), f([1, 3, 4], 'b'), key)
        Traceback (most recent call last):
        ...
        RuntimeError: sorting not unique
    """
def log_string(element, base=None):
    """
    Return a representation of the log of the given element to the
    given base.

    INPUT:

    - ``element`` -- an object

    - ``base`` -- an object or ``None``

    OUTPUT: string

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import log_string
        sage: log_string(3)
        'log(3)'
        sage: log_string(3, base=42)
        'log(3, base=42)'
    """
def strip_symbolic(expression):
    """
    Return, if possible, the underlying (numeric) object of
    the symbolic expression.

    If ``expression`` is not symbolic, then ``expression`` is returned.

    INPUT:

    - ``expression`` -- an object

    OUTPUT: an object

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import strip_symbolic
        sage: strip_symbolic(SR(2)); _.parent()
        2
        Integer Ring
        sage: strip_symbolic(SR(2/3)); _.parent()
        2/3
        Rational Field
        sage: strip_symbolic(SR('x')); _.parent()
        x
        Symbolic Ring
        sage: strip_symbolic(pi); _.parent()
        pi
        Symbolic Ring
    """

class NotImplementedOZero(NotImplementedError):
    """
    A special :python:`NotImplementedError<library/exceptions.html#exceptions.NotImplementedError>`
    which is raised when the result is O(0) which means 0
    for sufficiently large values of the variable.
    """
    exact_part: Incomplete
    def __init__(self, asymptotic_ring=None, var=None, exact_part: int = 0) -> None:
        """
        INPUT:

        - ``asymptotic_ring`` -- (default: ``None``) an :class:`AsymptoticRing`
          or ``None``

        - ``var`` -- (default: ``None``) a string

        Either ``asymptotic_ring`` or ``var`` has to be specified.

        - ``exact_part`` -- (default: ``0``) asymptotic expansion

        EXAMPLES::

            sage: A = AsymptoticRing('n^ZZ', ZZ)
            sage: from sage.rings.asymptotic.misc import NotImplementedOZero

            sage: raise NotImplementedOZero(A)
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got O(0)
            The error term O(0) means 0 for sufficiently large n.

            sage: raise NotImplementedOZero(var='m')
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got O(0)
            The error term O(0) means 0 for sufficiently large m.

        TESTS::

            sage: raise NotImplementedOZero(A, var='m')
            Traceback (most recent call last):
            ...
            ValueError: specify either 'asymptotic_ring' or 'var'
            sage: raise NotImplementedOZero()
            Traceback (most recent call last):
            ...
            ValueError: specify either 'asymptotic_ring' or 'var'
        """

class NotImplementedBZero(NotImplementedError):
    """
    A special :python:`NotImplementedError<library/exceptions.html#exceptions.NotImplementedError>`
    which is raised when the result is B(0) which means 0
    for sufficiently large values of the variable.
    """
    exact_part: Incomplete
    def __init__(self, asymptotic_ring=None, var=None, exact_part: int = 0) -> None:
        """
        INPUT:

        - ``asymptotic_ring`` -- (default: ``None``) an :class:`AsymptoticRing`
          or ``None``

        - ``var`` -- (default: ``None``) string

        Either ``asymptotic_ring`` or ``var`` has to be specified.

        - ``exact_part`` -- (default: ``0``) asymptotic expansion

        EXAMPLES::

            sage: A = AsymptoticRing('n^ZZ', ZZ)
            sage: from sage.rings.asymptotic.misc import NotImplementedBZero

            sage: raise NotImplementedBZero(A)
            Traceback (most recent call last):
            ...
            NotImplementedBZero: got B(0)
            The error term B(0) means 0 for sufficiently large n.

            sage: raise NotImplementedBZero(var='m')
            Traceback (most recent call last):
            ...
            NotImplementedBZero: got B(0)
            The error term B(0) means 0 for sufficiently large m.

            sage: AR.<n> = AsymptoticRing('n^QQ', QQ)
            sage: AR(0).B(42)
            Traceback (most recent call last):
            ...
            NotImplementedBZero: got B(0)
            The error term B(0) means 0 for sufficiently large n.

        TESTS::

            sage: raise NotImplementedBZero(A, var='m')
            Traceback (most recent call last):
            ...
            ValueError: specify either 'asymptotic_ring' or 'var'
            sage: raise NotImplementedBZero()
            Traceback (most recent call last):
            ...
            ValueError: specify either 'asymptotic_ring' or 'var'
        """

def transform_category(category, subcategory_mapping, axiom_mapping, initial_category=None):
    """
    Transform ``category`` to a new category according to the given
    mappings.

    INPUT:

    - ``category`` -- a category

    - ``subcategory_mapping`` -- list (or other iterable) of triples
      ``(from, to, mandatory)``, where

      - ``from`` and ``to`` are categories and
      - ``mandatory`` is a boolean.

    - ``axiom_mapping`` -- list (or other iterable) of triples
      ``(from, to, mandatory)``, where

      - ``from`` and ``to`` are strings describing axioms and
      - ``mandatory`` is a boolean.

    - ``initial_category`` -- (default: ``None``) a category. When
      transforming the given category, this ``initial_category`` is
      used as a starting point of the result. This means the resulting
      category will be a subcategory of ``initial_category``.
      If ``initial_category`` is ``None``, then the
      :class:`category of objects <sage.categories.objects.Objects>`
      is used.

    OUTPUT: a category

    .. NOTE::

        Consider a subcategory mapping ``(from, to, mandatory)``. If
        ``category`` is a subcategory of ``from``, then the
        returned category will be a subcategory of ``to``. Otherwise and
        if ``mandatory`` is set, then an error is raised.

        Consider an axiom mapping ``(from, to, mandatory)``. If
        ``category`` is has axiom ``from``, then the
        returned category will have axiom ``to``. Otherwise and
        if ``mandatory`` is set, then an error is raised.

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import transform_category
        sage: from sage.categories.additive_semigroups import AdditiveSemigroups
        sage: from sage.categories.additive_monoids import AdditiveMonoids
        sage: from sage.categories.additive_groups import AdditiveGroups
        sage: S = [
        ....:     (Sets(), Sets(), True),
        ....:     (Posets(), Posets(), False),
        ....:     (AdditiveMagmas(), Magmas(), False)]
        sage: A = [
        ....:     ('AdditiveAssociative', 'Associative', False),
        ....:     ('AdditiveUnital', 'Unital', False),
        ....:     ('AdditiveInverse', 'Inverse', False),
        ....:     ('AdditiveCommutative', 'Commutative', False)]
        sage: transform_category(Objects(), S, A)
        Traceback (most recent call last):
        ...
        ValueError: Category of objects is not
        a subcategory of Category of sets.
        sage: transform_category(Sets(), S, A)
        Category of sets
        sage: transform_category(Posets(), S, A)
        Category of posets
        sage: transform_category(AdditiveSemigroups(), S, A)
        Category of semigroups
        sage: transform_category(AdditiveMonoids(), S, A)
        Category of monoids
        sage: transform_category(AdditiveGroups(), S, A)
        Category of groups
        sage: transform_category(AdditiveGroups().AdditiveCommutative(), S, A)
        Category of commutative groups

    ::

        sage: transform_category(AdditiveGroups().AdditiveCommutative(), S, A,
        ....:     initial_category=Posets())
        Join of Category of commutative groups
            and Category of posets

    ::

        sage: transform_category(ZZ.category(), S, A)
        Category of commutative groups
        sage: transform_category(QQ.category(), S, A)
        Category of commutative groups
        sage: transform_category(SR.category(), S, A)
        Category of commutative groups
        sage: transform_category(Fields(), S, A)
        Category of commutative groups
        sage: transform_category(ZZ['t'].category(), S, A)
        Category of commutative groups

    ::

        sage: A[-1] = ('Commutative', 'AdditiveCommutative', True)
        sage: transform_category(Groups(), S, A)
        Traceback (most recent call last):
        ...
        ValueError: Category of groups does not have
        axiom Commutative.
    """

class Locals(dict):
    """
    A frozen dictionary-like class for storing locals
    of an :class:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticRing`.

    EXAMPLES::

        sage: from sage.rings.asymptotic.misc import Locals
        sage: locals = Locals({'a': 42})
        sage: locals['a']
        42

    The object contains default values (see :meth:`default_locals`)
    for some keys::

        sage: locals['log']
        <function log at 0x...>
    """
    def __getitem__(self, key):
        """
        Return an item.

        TESTS::

            sage: from sage.rings.asymptotic.misc import Locals
            sage: locals = Locals()
            sage: locals
            {}
            sage: locals['log']  # indirect doctest
            <function log at 0x...>
        """
    def __setitem__(self, key, value) -> None:
        """
        Set an item.

        This raises an error as the object is immutable.

        TESTS::

            sage: from sage.rings.asymptotic.misc import Locals
            sage: locals = Locals()
            sage: locals['a'] = 4  # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: locals dictionary is frozen,
            therefore does not support item assignment
        """
    def __hash__(self):
        """
        Return a hash value.

        TESTS::

            sage: from sage.rings.asymptotic.misc import Locals
            sage: locals = Locals({'a': 2, 'b': 1})
            sage: hash(locals)  # random
            -42
        """
    @cached_method
    def default_locals(self):
        """
        Return the default locals used in
        the :class:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticRing`.

        OUTPUT: a dictionary

        EXAMPLES::

            sage: from sage.rings.asymptotic.misc import Locals
            sage: locals = Locals({'a': 2, 'b': 1})
            sage: locals
            {'a': 2, 'b': 1}
            sage: locals.default_locals()
            {'log': <function log at 0x...>}
            sage: locals['log']
            <function log at 0x...>
        """

class WithLocals(SageObject):
    """
    A class extensions for handling local values; see also
    :class:`Locals`.

    This is used in the
    :class:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticRing`.

    EXAMPLES::

        sage: A.<n> = AsymptoticRing('n^ZZ', QQ, locals={'a': 42})
        sage: A.locals()
        {'a': 42}
    """
    def locals(self, locals=None):
        """
        Return the actual :class:`Locals` object to be used.

        INPUT:

        - ``locals`` -- an object

          If ``locals`` is not ``None``, then a :class:`Locals` object
          is created and returned.
          If ``locals`` is ``None``, then a stored :class:`Locals` object,
          if any, is returned. Otherwise, an empty (i.e. no values except
          the default values)
          :class:`Locals` object is created and returned.

        OUTPUT: a :class:`Locals` object

        TESTS::

            sage: A.<n> = AsymptoticRing('n^ZZ', QQ, locals={'a': 42})
            sage: A.locals()
            {'a': 42}
            sage: A.locals({'a': 41})
            {'a': 41}
            sage: A.locals({'b': -3})
            {'b': -3}
        """
