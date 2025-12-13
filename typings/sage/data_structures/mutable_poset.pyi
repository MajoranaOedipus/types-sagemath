from _typeshed import Incomplete
from collections.abc import Generator
from sage.structure.sage_object import SageObject as SageObject

class MutablePosetShell(SageObject):
    '''
    A shell for an element of a :class:`mutable poset <MutablePoset>`.

    INPUT:

    - ``poset`` -- the poset to which this shell belongs

    - ``element`` -- the element which should be
      contained/encapsulated in this shell

    OUTPUT: a shell for the given element

    .. NOTE::

        If the :meth:`element` of a shell is ``None``, then this
        element is considered as "special" (see :meth:`is_special`).
        There are two special elements, namely

        - a ``\'null\'`` (an element smaller than each other element;
          it has no predecessors) and
        - an ``\'oo\'`` (an element larger than each other element;
          it has no successors).

    EXAMPLES::

        sage: from sage.data_structures.mutable_poset import MutablePoset as MP
        sage: P = MP()
        sage: P.add(66)
        sage: P
        poset(66)
        sage: s = P.shell(66)
        sage: type(s)
        <class \'sage.data_structures.mutable_poset.MutablePosetShell\'>

    .. SEEALSO::

        :class:`MutablePoset`
    '''
    def __init__(self, poset, element) -> None:
        """
        See :class:`MutablePosetShell` for details.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: MutablePosetShell(P, (1, 2))
            (1, 2)
        """
    @property
    def poset(self):
        """
        The poset to which this shell belongs.

        .. SEEALSO::

            :class:`MutablePoset`

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: e = MutablePosetShell(P, (1, 2))
            sage: e.poset is P
            True
        """
    @property
    def element(self):
        """
        The element contained in this shell.

        .. SEEALSO::

            :meth:`key`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: e = MutablePosetShell(P, (1, 2))
            sage: e.element
            (1, 2)
        """
    @property
    def key(self):
        """
        The key of the element contained in this shell.

        The key of an element is determined by the mutable poset (the
        parent) via the ``key``-function (see construction of a
        :class:`MutablePoset`).

        .. SEEALSO::

            :meth:`element`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: P = MP()
            sage: e = MutablePosetShell(P, (1, 2))
            sage: e.key
            (1, 2)
            sage: Q = MP(key=lambda k: k[0])
            sage: f = MutablePosetShell(Q, (1, 2))
            sage: f.key
            1

        Test the caching of the key::

            sage: def k(k):
            ....:     print('key %s' % (k,))
            ....:     return k
            sage: R = MP(key=k)
            sage: h = MutablePosetShell(R, (1, 2))
            key (1, 2)
            sage: h.key; h.key
            (1, 2)
            (1, 2)
        """
    def predecessors(self, reverse: bool = False):
        """
        Return the predecessors of this shell.

        INPUT:

        - ``reverse`` -- boolean (default: ``False``); if set, then return
          successors instead

        OUTPUT: set

        .. SEEALSO::

            :meth:`successors`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: e = MutablePosetShell(P, (1, 2))
            sage: e.predecessors()
            set()
        """
    def successors(self, reverse: bool = False):
        """
        Return the successors of this shell.

        INPUT:

        - ``reverse`` -- boolean (default: ``False``); if set, then return
          predecessors instead

        OUTPUT: set

        .. SEEALSO::

            :meth:`predecessors`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: e = MutablePosetShell(P, (1, 2))
            sage: e.successors()
            set()
        """
    def is_special(self):
        """
        Return whether this shell contains either the null-element, i.e., the
        element smaller than any possible other element or the
        infinity-element, i.e., the element larger than any possible
        other element.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`is_null`,
            :meth:`is_oo`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.null.is_special()
            True
            sage: P.oo.is_special()
            True
        """
    def is_null(self):
        """
        Return whether this shell contains the null-element, i.e., the element
        smaller than any possible other element.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`is_special`,
            :meth:`is_oo`,
            :meth:`MutablePoset.null`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.null.is_null()
            True
            sage: P.oo.is_null()
            False
        """
    def is_oo(self):
        """
        Return whether this shell contains the infinity-element, i.e., the element
        larger than any possible other element.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`is_null`,
            :meth:`is_special`,
            :meth:`MutablePoset.oo`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.null.is_oo()
            False
            sage: P.oo.is_oo()
            True
        """
    def __hash__(self):
        """
        Return the hash of this shell.

        OUTPUT: a hash value

        This returns the hash value of the key of the element
        contained in this shell.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: hash(MutablePosetShell(P, (1, 2))) == hash((1, 2))
            True
        """
    def le(self, other, reverse: bool = False):
        """
        Return whether this shell is less than or equal to ``other``.

        INPUT:

        - ``other`` -- a shell

        - ``reverse`` -- boolean (default: ``False``); if set, then return
          whether this shell is greater than or equal to ``other``

        OUTPUT: boolean

        .. NOTE::

            The comparison of the shells is based on the comparison
            of the keys of the elements contained in the shells,
            except for special shells (see :class:`MutablePosetShell`).

        .. SEEALSO::

            :meth:`eq`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: e = MutablePosetShell(P, (1, 2))
            sage: z = P.null
            sage: oo = P.oo
            sage: z <= e  # indirect doctest
            True
            sage: e <= oo  # indirect doctest
            True
            sage: z <= oo  # indirect doctest
            True
            sage: oo <= z  # indirect doctest
            False
            sage: oo <= e  # indirect doctest
            False
            sage: e <= z  # indirect doctest
            False
            sage: z <= z  # indirect doctest
            True
            sage: oo <= oo  # indirect doctest
            True
            sage: e <= e  # indirect doctest
            True

        ::

            sage: z.le(e, reverse=True)
            False
            sage: e.le(oo, reverse=True)
            False
            sage: z.le(oo, reverse=True)
            False
            sage: oo.le(z, reverse=True)
            True
            sage: oo.le(e, reverse=True)
            True
            sage: e.le(z, reverse=True)
            True
            sage: z.le(z, reverse=True)
            True
            sage: oo.le(oo, reverse=True)
            True
            sage: e.le(e, reverse=True)
            True
        """
    __le__ = le
    def eq(self, other):
        """
        Return whether this shell is equal to ``other``.

        INPUT:

        - ``other`` -- a shell

        OUTPUT: boolean

        .. NOTE::

            This method compares the keys of the elements contained
            in the (non-special) shells. In particular,
            elements/shells with the same key are considered as equal.

        .. SEEALSO::

            :meth:`le`,
            :class:`MutablePoset`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: from sage.data_structures.mutable_poset import MutablePosetShell
            sage: e = MutablePosetShell(P, (1, 2))
            sage: f = MutablePosetShell(P, (2, 1))
            sage: z = P.null
            sage: oo = P.oo
            sage: z == z
            True
            sage: oo == oo
            True
            sage: e == e
            True
            sage: e == f
            False
            sage: z == e
            False
            sage: e == oo
            False
            sage: oo == z
            False

        Comparing elements in different mutable posets is possible; their
        shells are equal if their elements are::

            sage: S = MP([42]); s = S.shell(42)
            sage: T = MP([42]); t = T.shell(42)
            sage: s == t
            True
            sage: S.oo == T.oo
            True
        """
    __eq__ = eq
    def lower_covers(self, shell, reverse: bool = False):
        """
        Return the lower covers of the specified ``shell``;
        the search is started at this (``self``) shell.

        A lower cover of `x` is an element `y` of the poset
        such that `y < x` and there is no element `z` of the poset
        so that `y < z < x`.

        INPUT:

        - ``shell`` -- the shell for which to find the covering shells
          There is no restriction of ``shell`` being contained in the poset
          If ``shell`` is contained in the poset, then use the more efficient
          methods :meth:`predecessors` and :meth:`successors`.

        - ``reverse`` -- boolean (default: ``False``); if set, then find
          the upper covers (see also :meth:`upper_covers`)
          instead of the lower covers

        OUTPUT: a set of :class:`shells <MutablePosetShell>`

        .. NOTE::

            Suppose ``reverse`` is ``False``. This method starts at
            the calling shell (``self``) and searches towards ``'oo'``.
            Thus, only shells which are (not necessarily
            direct) successors of this shell are considered.

            If ``reverse`` is ``True``, then the reverse direction is
            taken.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: e = P.shell(T((2, 2))); e
            (2, 2)
            sage: sorted(P.null.lower_covers(e),
            ....:        key=lambda c: repr(c.element))
            [(1, 2), (2, 1)]
            sage: set(_) == e.predecessors()
            True
            sage: sorted(P.oo.upper_covers(e),
            ....:        key=lambda c: repr(c.element))
            [(4, 4)]
            sage: set(_) == e.successors()
            True

        ::

            sage: Q = MP([T((3, 2))])
            sage: f = next(Q.shells())
            sage: sorted(P.null.lower_covers(f),
            ....:        key=lambda c: repr(c.element))
            [(2, 2)]
            sage: sorted(P.oo.upper_covers(f),
            ....:        key=lambda c: repr(c.element))
            [(4, 4)]

        .. SEEALSO::

            :meth:`upper_covers`,
            :meth:`predecessors`,
            :meth:`successors`,
            :class:`MutablePoset`.
        """
    def upper_covers(self, shell, reverse: bool = False):
        """
        Return the upper covers of the specified ``shell``;
        the search is started at this (``self``) shell.

        An upper cover of `x` is an element `y` of the poset
        such that `x < y` and there is no element `z` of the poset
        so that `x < z < y`.

        INPUT:

        - ``shell`` -- the shell for which to find the covering shells
          There is no restriction of ``shell`` being contained in the poset
          If ``shell`` is contained in the poset, then use the more efficient
          methods :meth:`predecessors` and :meth:`successors`.

        - ``reverse`` -- boolean (default: ``False``); if set, then find
          the lower covers (see also :meth:`lower_covers`)
          instead of the upper covers.

        OUTPUT: a set of :class:`shells <MutablePosetShell>`

        .. NOTE::

            Suppose ``reverse`` is ``False``. This method starts at
            the calling shell (``self``) and searches towards ``'null'``.
            Thus, only shells which are (not necessarily
            direct) predecessors of this shell are considered.

            If ``reverse`` is ``True``, then the reverse direction is
            taken.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: e = P.shell(T((2, 2))); e
            (2, 2)
            sage: sorted(P.null.lower_covers(e),
            ....:        key=lambda c: repr(c.element))
            [(1, 2), (2, 1)]
            sage: set(_) == e.predecessors()
            True
            sage: sorted(P.oo.upper_covers(e),
            ....:        key=lambda c: repr(c.element))
            [(4, 4)]
            sage: set(_) == e.successors()
            True

        ::

            sage: Q = MP([T((3, 2))])
            sage: f = next(Q.shells())
            sage: sorted(P.null.lower_covers(f),
            ....:        key=lambda c: repr(c.element))
            [(2, 2)]
            sage: sorted(P.oo.upper_covers(f),
            ....:        key=lambda c: repr(c.element))
            [(4, 4)]

        .. SEEALSO::

            :meth:`predecessors`,
            :meth:`successors`,
            :class:`MutablePoset`.
        """
    def iter_depth_first(self, reverse: bool = False, key=None, condition=None):
        """
        Iterate over all shells in depth first order.

        INPUT:

        - ``reverse`` -- boolean (default: ``False``); if set, reverses the
          order, i.e., ``False`` searches towards ``'oo'`` and
          ``True`` searches towards ``'null'``

        - ``key`` -- (default: ``None``) a function used for sorting
          the direct successors of a shell (used in case of a
          tie). If this is ``None``, no sorting occurs.

        - ``condition`` -- (default: ``None``) a function mapping a
          shell to ``True`` (include in iteration) or ``False`` (do
          not include). ``None`` is equivalent to a function returning
          always ``True``. Note that the iteration does not go beyond a
          not included shell.

        .. NOTE::

            The depth first search starts at this (``self``) shell. Thus
            only this shell and shells greater than (in case of
            ``reverse=False``) this shell are visited.

        ALGORITHM:

        See :wikipedia:`Depth-first_search`.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: list(P.null.iter_depth_first(reverse=False, key=repr))
            [null, (1, 1), (1, 2), (1, 3), (4, 4), oo, (2, 2), (2, 1)]
            sage: list(P.oo.iter_depth_first(reverse=True, key=repr))
            [oo, (4, 4), (1, 3), (1, 2), (1, 1), null, (2, 2), (2, 1)]
            sage: list(P.null.iter_depth_first(
            ....:     condition=lambda s: s.element[0] == 1))
            [null, (1, 1), (1, 2), (1, 3)]

        .. SEEALSO::

            :meth:`iter_topological`,
            :class:`MutablePoset`.
        """
    def iter_topological(self, reverse: bool = False, key=None, condition=None):
        """
        Iterate over all shells in topological order.

        INPUT:

        - ``reverse`` -- boolean (default: ``False``); if set, reverses the
          order, i.e., ``False`` searches towards ``'oo'`` and
          ``True`` searches towards ``'null'``

        - ``key`` -- (default: ``None``) a function used for sorting
          the direct predecessors of a shell (used in case of a
          tie). If this is ``None``, no sorting occurs.

        - ``condition`` -- (default: ``None``) a function mapping a
          shell to ``True`` (include in iteration) or ``False`` (do
          not include). ``None`` is equivalent to a function returning
          always ``True``. Note that the iteration does not go beyond a
          not included shell.

        OUTPUT: an iterator

        .. NOTE::

            The topological search will only find shells smaller than
            (in case of ``reverse=False``)
            or equal to this (``self``) shell. This is in contrast to
            :meth:`iter_depth_first`.

        ALGORITHM:

        Here a simplified version of the algorithm found in [Tar1976]_
        and [CLRS2001]_ is used. See also
        :wikipedia:`Topological_sorting`.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])

        ::

            sage: for e in P.shells_topological(include_special=True,
            ....:                               reverse=True, key=repr):
            ....:     print(e)
            ....:     print(list(e.iter_topological(reverse=True, key=repr)))
            oo
            [oo]
            (4, 4)
            [oo, (4, 4)]
            (1, 3)
            [oo, (4, 4), (1, 3)]
            (2, 2)
            [oo, (4, 4), (2, 2)]
            (1, 2)
            [oo, (4, 4), (1, 3), (2, 2), (1, 2)]
            (2, 1)
            [oo, (4, 4), (2, 2), (2, 1)]
            (1, 1)
            [oo, (4, 4), (1, 3), (2, 2), (1, 2), (2, 1), (1, 1)]
            null
            [oo, (4, 4), (1, 3), (2, 2), (1, 2), (2, 1), (1, 1), null]

        ::

            sage: for e in P.shells_topological(include_special=True,
            ....:                               reverse=True, key=repr):
            ....:     print(e)
            ....:     print(list(e.iter_topological(reverse=False, key=repr)))
            oo
            [null, (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (4, 4), oo]
            (4, 4)
            [null, (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (4, 4)]
            (1, 3)
            [null, (1, 1), (1, 2), (1, 3)]
            (2, 2)
            [null, (1, 1), (1, 2), (2, 1), (2, 2)]
            (1, 2)
            [null, (1, 1), (1, 2)]
            (2, 1)
            [null, (1, 1), (2, 1)]
            (1, 1)
            [null, (1, 1)]
            null
            [null]

        ::

            sage: list(P.null.iter_topological(
            ....:     reverse=True, condition=lambda s: s.element[0] == 1,
            ....:     key=repr))
            [(1, 3), (1, 2), (1, 1), null]

        .. SEEALSO::

            :meth:`iter_depth_first`,
            :meth:`MutablePoset.shells_topological`,
            :meth:`MutablePoset.elements_topological`,
            :meth:`MutablePoset.keys_topological`,
            :class:`MutablePoset`.
        """
    def merge(self, element, check: bool = True, delete: bool = True) -> None:
        """
        Merge the given element with the element contained in this
        shell.

        INPUT:

        - ``element`` -- an element (of the poset)

        - ``check`` -- boolean (default: ``True``); if set, then the
          ``can_merge``-function of :class:`MutablePoset` determines
          whether the merge is possible. ``can_merge`` is ``None`` means
          that this check is always passed.

        - ``delete`` -- boolean (default: ``True``); if set, then ``element``
          is removed from the poset after the merge

        OUTPUT: nothing

        .. NOTE::

            This operation depends on the parameters ``merge`` and
            ``can_merge`` of the :class:`MutablePoset` this shell is
            contained in. These parameters are defined when the poset
            is constructed.

        .. NOTE::

            If the ``merge`` function returns ``None``, then this shell
            is removed from the poset.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: def add(left, right):
            ....:     return (left[0], ''.join(sorted(left[1] + right[1])))
            sage: def can_add(left, right):
            ....:     return left[0] <= right[0]
            sage: P = MP([(1, 'a'), (3, 'b'), (2, 'c'), (4, 'd')],
            ....:        key=lambda c: c[0], merge=add, can_merge=can_add)
            sage: P
            poset((1, 'a'), (2, 'c'), (3, 'b'), (4, 'd'))
            sage: P.shell(2).merge((3, 'b'))
            sage: P
            poset((1, 'a'), (2, 'bc'), (4, 'd'))

        .. SEEALSO::

            :meth:`MutablePoset.merge`,
            :class:`MutablePoset`.

        TESTS::

            sage: MP([2], merge=operator.add,
            ....:    can_merge=lambda _, __: False).shell(2).merge(1)
            Traceback (most recent call last):
            ...
            RuntimeError: Cannot merge 2 with 1.
        """

def is_MutablePoset(P):
    """
    Test whether ``P`` inherits from :class:`MutablePoset`.

    .. SEEALSO::

        :class:`MutablePoset`

    TESTS::

        sage: from sage.data_structures.mutable_poset import MutablePoset as MP
        sage: from sage.data_structures.mutable_poset import is_MutablePoset
        sage: P = MP()
        sage: is_MutablePoset(P)
        doctest:warning...
        DeprecationWarning: The function is_MutablePoset is deprecated; use 'isinstance(..., MutablePoset)' instead.
        See https://github.com/sagemath/sage/issues/38125 for details.
        True
    """

class MutablePoset(SageObject):
    """
    A data structure that models a mutable poset (partially ordered
    set).

    INPUT:

    - ``data`` -- data from which to construct the poset. It can be
      any of the following:

      #. ``None`` (default), in which case an empty poset is created,

      #. a :class:`MutablePoset`, which will be copied during creation,

      #. an iterable, whose elements will be in the poset.

    - ``key`` -- a function which maps elements to keys. If ``None``
      (default), this is the identity, i.e., keys are equal to their
      elements.

      Two elements with the same keys are considered as equal; so only
      one of these two elements can be in the poset.

      This ``key`` is not used for sorting (in contrast to
      sorting-functions, e.g. ``sorted``).

    - ``merge`` -- a function which merges its second argument (an
      element) to its first (again an element) and returns the result
      (as an element). If the return value is ``None``, the element is
      removed from the poset.

      This hook is called by :meth:`merge`. Moreover it is used during
      :meth:`add` when an element (more precisely its key) is already
      in this poset.

      ``merge`` is ``None`` (default) is equivalent to ``merge``
      returning its first argument. Note that it is not allowed that the
      key of the returning element differs from the key of the first
      input parameter. This means ``merge`` must not change the
      position of the element in the poset.

    - ``can_merge`` -- a function which checks whether its second argument
      can be merged to its first

      This hook is called by :meth:`merge`. Moreover it is used during
      :meth:`add` when an element (more precisely its key) is already
      in this poset.

      ``can_merge`` is ``None`` (default) is equivalent to ``can_merge``
      returning ``True`` in all cases.

    OUTPUT: a mutable poset

    You can find a short introduction and examples
    :mod:`here <sage.data_structures.mutable_poset>`.

    EXAMPLES::

        sage: from sage.data_structures.mutable_poset import MutablePoset as MP

    We illustrate the different input formats

    #. No input::

        sage: A = MP(); A
        poset()

    #. A :class:`MutablePoset`::

        sage: B = MP(A); B
        poset()
        sage: B.add(42)
        sage: C = MP(B); C
        poset(42)

    #. An iterable::

        sage: C = MP([5, 3, 11]); C
        poset(3, 5, 11)

    .. SEEALSO::

        :class:`MutablePosetShell`.
    """
    def __init__(self, data=None, key=None, merge=None, can_merge=None) -> None:
        """
        See :class:`MutablePoset` for details.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: MP()
            poset()

        ::

            sage: P = MP()
            sage: P.add(42)
            sage: MP(P)
            poset(42)

        ::

            sage: MP([3, 5, 7])
            poset(3, 5, 7)

        ::

            sage: MP(33)
            Traceback (most recent call last):
            ...
            TypeError: 33 is not iterable; do not know what to do with it.
        """
    def clear(self) -> None:
        """
        Remove all elements from this poset.

        OUTPUT: nothing

        .. SEEALSO::

            :meth:`discard`,
            :meth:`pop`,
            :meth:`remove`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.add(42); P
            poset(42)
            sage: P.clear()
            sage: print(P.repr_full())
            poset()
            +-- null
            |   +-- no predecessors
            |   +-- successors:   oo
            +-- oo
            |   +-- predecessors:   null
            |   +-- no successors
        """
    def __len__(self) -> int:
        """
        Return the number of elements contained in this poset.

        OUTPUT: integer

        .. NOTE::

            The special elements ``'null'`` and ``'oo'`` are not counted.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: len(P)  # indirect doctest
            0
            sage: bool(P)
            False
            sage: P.add(42)
            sage: len(P)
            1
            sage: bool(P)
            True
        """
    @property
    def null(self):
        """
        The shell `\\emptyset` whose element is smaller than any
        other element.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: z = P.null; z
            null
            sage: z.is_null()
            True

        .. SEEALSO::

            :meth:`oo`,
            :meth:`MutablePosetShell.is_null`,
            :meth:`MutablePosetShell.is_special`.
        """
    @property
    def oo(self):
        """
        The shell `\\infty` whose element is larger than any other
        element.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: oo = P.oo; oo
            oo
            sage: oo.is_oo()
            True

        .. SEEALSO::

            :meth:`null`,
            :meth:`MutablePosetShell.is_oo`,
            :meth:`MutablePosetShell.is_special`.
        """
    def shell(self, key):
        """
        Return the shell of the element corresponding to ``key``.

        INPUT:

        - ``key`` -- the key of an object

        OUTPUT: an instance of :class:`MutablePosetShell`

        .. NOTE::

            Each element is contained/encapsulated in a shell inside
            the poset.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.add(42)
            sage: e = P.shell(42); e
            42
            sage: type(e)
            <class 'sage.data_structures.mutable_poset.MutablePosetShell'>

        .. SEEALSO::

            :meth:`element`,
            :meth:`get_key`.
        """
    def element(self, key):
        """
        Return the element corresponding to ``key``.

        INPUT:

        - ``key`` -- the key of an object

        OUTPUT: an object

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.add(42)
            sage: e = P.element(42); e
            42
            sage: type(e)
            <class 'sage.rings.integer.Integer'>

        .. SEEALSO::

            :meth:`shell`,
            :meth:`get_key`.
        """
    def get_key(self, element):
        """
        Return the key corresponding to the given element.

        INPUT:

        - ``element`` -- an object

        OUTPUT: an object (the key of ``element``)

        .. SEEALSO::

            :meth:`element`,
            :meth:`shell`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.get_key(None) is None
            True
            sage: P.get_key((1, 2))
            (1, 2)
            sage: Q = MP(key=lambda k: k[0])
            sage: Q.get_key((1, 2))
            1
        """
    def copy(self, mapping=None):
        """
        Create a shallow copy.

        INPUT:

        - ``mapping`` -- a function which is applied on each of the elements

        OUTPUT: a poset with the same content as ``self``

        .. SEEALSO::

            :meth:`map`,
            :meth:`mapped`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2))])
            sage: Q = copy(P)  # indirect doctest
            sage: P.repr_full() == Q.repr_full()
            True
        """
    __copy__ = copy
    def shells(self, include_special: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over all shells.

        INPUT:

        - ``include_special`` -- boolean (default: ``False``); if set, then
          including shells containing a smallest element (`\\emptyset`)
          and a largest element (`\\infty`)

        OUTPUT: an iterator

        .. NOTE::

            Each element is contained/encapsulated in a shell inside
            the poset.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: tuple(P.shells())
            ()
            sage: tuple(P.shells(include_special=True))
            (null, oo)

        .. SEEALSO::

            :meth:`shells_topological`,
            :meth:`elements`,
            :meth:`elements_topological`,
            :meth:`keys`,
            :meth:`keys_topological`,
            :meth:`MutablePosetShell.iter_depth_first`,
            :meth:`MutablePosetShell.iter_topological`.
        """
    def shells_topological(self, include_special: bool = False, reverse: bool = False, key=None):
        """
        Return an iterator over all shells in topological order.

        INPUT:

        - ``include_special`` -- boolean (default: ``False``); if set, then
          including shells containing a smallest element (`\\emptyset`)
          and a largest element (`\\infty`).

        - ``reverse`` -- boolean (default: ``False``); if set, reverses the
          order, i.e., ``False`` gives smallest elements first,
          ``True`` gives largest first.

        - ``key`` -- (default: ``None``) a function used for sorting
          the direct successors of a shell (used in case of a tie).
          If this is ``None``, no sorting occurs.

        OUTPUT: an iterator

        .. NOTE::

            Each element is contained/encapsulated in a shell inside
            the poset.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: list(P.shells_topological(key=repr))
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (4, 4)]
            sage: list(P.shells_topological(reverse=True, key=repr))
            [(4, 4), (1, 3), (2, 2), (1, 2), (2, 1), (1, 1)]
            sage: list(P.shells_topological(include_special=True, key=repr))
            [null, (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (4, 4), oo]
            sage: list(P.shells_topological(
            ....:     include_special=True, reverse=True, key=repr))
            [oo, (4, 4), (1, 3), (2, 2), (1, 2), (2, 1), (1, 1), null]

        .. SEEALSO::

            :meth:`shells`,
            :meth:`elements`,
            :meth:`elements_topological`,
            :meth:`keys`,
            :meth:`keys_topological`,
            :meth:`MutablePosetShell.iter_depth_first`,
            :meth:`MutablePosetShell.iter_topological`.
        """
    def elements(self, **kwargs) -> Generator[Incomplete]:
        """
        Return an iterator over all elements.

        INPUT:

        - ``kwargs`` -- arguments are passed to :meth:`shells`

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7])
            sage: [(v, type(v)) for v in sorted(P.elements())]
            [(3, <class 'sage.rings.integer.Integer'>),
             (7, <class 'sage.rings.integer.Integer'>),
             (42, <class 'sage.rings.integer.Integer'>)]

        Note that

        ::

            sage: it = iter(P)
            sage: sorted(it)
            [3, 7, 42]

        returns all elements as well.

        .. SEEALSO::

            :meth:`shells`,
            :meth:`shells_topological`,
            :meth:`elements_topological`,
            :meth:`keys`,
            :meth:`keys_topological`,
            :meth:`MutablePosetShell.iter_depth_first`,
            :meth:`MutablePosetShell.iter_topological`.
        """
    __iter__ = elements
    def elements_topological(self, **kwargs) -> Generator[Incomplete]:
        """
        Return an iterator over all elements in topological order.

        INPUT:

        - ``kwargs`` -- arguments are passed to :meth:`shells_topological`

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: [(v, type(v)) for v in P.elements_topological(key=repr)]
            [((1, 1), <class '__main__.T'>),
             ((1, 2), <class '__main__.T'>),
             ((1, 3), <class '__main__.T'>),
             ((2, 1), <class '__main__.T'>),
             ((2, 2), <class '__main__.T'>),
             ((4, 4), <class '__main__.T'>)]

        .. SEEALSO::

            :meth:`shells`,
            :meth:`shells_topological`,
            :meth:`elements`,
            :meth:`keys`,
            :meth:`keys_topological`,
            :meth:`MutablePosetShell.iter_depth_first`,
            :meth:`MutablePosetShell.iter_topological`.
        """
    def keys(self, **kwargs) -> Generator[Incomplete]:
        """
        Return an iterator over all keys of the elements.

        INPUT:

        - ``kwargs`` -- arguments are passed to :meth:`shells`

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7], key=lambda c: -c)
            sage: [(v, type(v)) for v in sorted(P.keys())]
            [(-42, <class 'sage.rings.integer.Integer'>),
             (-7, <class 'sage.rings.integer.Integer'>),
             (-3, <class 'sage.rings.integer.Integer'>)]

            sage: [(v, type(v)) for v in sorted(P.elements())]
            [(3, <class 'sage.rings.integer.Integer'>),
             (7, <class 'sage.rings.integer.Integer'>),
             (42, <class 'sage.rings.integer.Integer'>)]

            sage: [(v, type(v)) for v in sorted(P.shells(),
            ....:                               key=lambda c: c.element)]
            [(3, <class 'sage.data_structures.mutable_poset.MutablePosetShell'>),
             (7, <class 'sage.data_structures.mutable_poset.MutablePosetShell'>),
             (42, <class 'sage.data_structures.mutable_poset.MutablePosetShell'>)]

        .. SEEALSO::

            :meth:`shells`,
            :meth:`shells_topological`,
            :meth:`elements`,
            :meth:`elements_topological`,
            :meth:`keys_topological`,
            :meth:`MutablePosetShell.iter_depth_first`,
            :meth:`MutablePosetShell.iter_topological`.
        """
    def keys_topological(self, **kwargs) -> Generator[Incomplete]:
        """
        Return an iterator over all keys of the elements in
        topological order.

        INPUT:

        - ``kwargs`` -- arguments are passed to :meth:`shells_topological`

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([(1, 1), (2, 1), (4, 4)],
            ....:        key=lambda c: c[0])
            sage: [(v, type(v)) for v in P.keys_topological(key=repr)]
            [(1, <class 'sage.rings.integer.Integer'>),
             (2, <class 'sage.rings.integer.Integer'>),
             (4, <class 'sage.rings.integer.Integer'>)]
            sage: [(v, type(v)) for v in P.elements_topological(key=repr)]
            [((1, 1), <... 'tuple'>),
             ((2, 1), <... 'tuple'>),
             ((4, 4), <... 'tuple'>)]
            sage: [(v, type(v)) for v in P.shells_topological(key=repr)]
            [((1, 1), <class 'sage.data_structures.mutable_poset.MutablePosetShell'>),
             ((2, 1), <class 'sage.data_structures.mutable_poset.MutablePosetShell'>),
             ((4, 4), <class 'sage.data_structures.mutable_poset.MutablePosetShell'>)]

        .. SEEALSO::

            :meth:`shells`,
            :meth:`shells_topological`,
            :meth:`elements`,
            :meth:`elements_topological`,
            :meth:`keys`,
            :meth:`MutablePosetShell.iter_depth_first`,
            :meth:`MutablePosetShell.iter_topological`.
        """
    def repr(self, include_special: bool = False, reverse: bool = False):
        """
        Return a representation of the poset.

        INPUT:

        - ``include_special`` -- boolean (default: ``False``); whether to
          include the special elements ``'null'`` and ``'oo'`` or not

        - ``reverse`` -- boolean (default: ``False``); if set, then
          largest elements are displayed first

        OUTPUT: string

        .. SEEALSO::

            :meth:`repr_full`

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: print(MP().repr())
            poset()
        """
    def repr_full(self, reverse: bool = False):
        """
        Return a representation with ordering details of the poset.

        INPUT:

        - ``reverse`` -- boolean (default: ``False``); if set, then
          largest elements are displayed first

        OUTPUT: string

        .. SEEALSO::

            :meth:`repr`

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: print(MP().repr_full(reverse=True))
            poset()
            +-- oo
            |   +-- no successors
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   oo
            |   +-- no predecessors
        """
    def contains(self, key):
        """
        Test whether ``key`` is encapsulated by one of the poset's elements.

        INPUT:

        - ``key`` -- an object

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`shells`,
            :meth:`elements`,
            :meth:`keys`.

        TESTS::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP()
            sage: P.add(T((1, 1)))
            sage: T((1, 1)) in P  # indirect doctest
            True
            sage: T((1, 2)) in P  # indirect doctest
            False
        """
    __contains__ = contains
    def add(self, element) -> None:
        """
        Add the given object as element to the poset.

        INPUT:

        - ``element`` -- an object (hashable and supporting comparison
          with the operator ``<=``)

        OUTPUT: nothing

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2))])
            sage: print(P.repr_full(reverse=True))
            poset((4, 4), (1, 3), (1, 2), (2, 1), (1, 1))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (4, 4)
            +-- (4, 4)
            |   +-- successors:   oo
            |   +-- predecessors: (1, 3), (2, 1)
            +-- (1, 3)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 2)
            +-- (1, 2)
            |   +-- successors:   (1, 3)
            |   +-- predecessors: (1, 1)
            +-- (2, 1)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 1)
            +-- (1, 1)
            |   +-- successors:   (1, 2), (2, 1)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (1, 1)
            |   +-- no predecessors
            sage: P.add(T((2, 2)))
            sage: reprP = P.repr_full(reverse=True); print(reprP)
            poset((4, 4), (1, 3), (2, 2), (1, 2), (2, 1), (1, 1))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (4, 4)
            +-- (4, 4)
            |   +-- successors:   oo
            |   +-- predecessors: (1, 3), (2, 2)
            +-- (1, 3)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 2)
            +-- (2, 2)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 2), (2, 1)
            +-- (1, 2)
            |   +-- successors:   (1, 3), (2, 2)
            |   +-- predecessors: (1, 1)
            +-- (2, 1)
            |   +-- successors:   (2, 2)
            |   +-- predecessors: (1, 1)
            +-- (1, 1)
            |   +-- successors:   (1, 2), (2, 1)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (1, 1)
            |   +-- no predecessors

        When adding an element which is already in the poset, nothing happens::

            sage: e = T((2, 2))
            sage: P.add(e)
            sage: P.repr_full(reverse=True) == reprP
            True

        We can influence the behavior when an element with existing key
        is to be inserted in the poset. For example, we can perform an
        addition on some argument of the elements::

            sage: def add(left, right):
            ....:     return (left[0], ''.join(sorted(left[1] + right[1])))
            sage: A = MP(key=lambda k: k[0], merge=add)
            sage: A.add((3, 'a'))
            sage: A
            poset((3, 'a'))
            sage: A.add((3, 'b'))
            sage: A
            poset((3, 'ab'))

        We can also deal with cancellations. If the return value of
        our hook-function is ``None``, then the element is removed out of
        the poset::

            sage: def add_None(left, right):
            ....:     s = left[1] + right[1]
            ....:     if s == 0:
            ....:         return None
            ....:     return (left[0], s)
            sage: B = MP(key=lambda k: k[0],
            ....:        merge=add_None)
            sage: B.add((7, 42))
            sage: B.add((7, -42))
            sage: B
            poset()

        .. SEEALSO::

            :meth:`discard`,
            :meth:`pop`,
            :meth:`remove`.

        TESTS::

            sage: R = MP([(1, 1, 42), (1, 3, 42), (2, 1, 7),
            ....:         (4, 4, 42), (1, 2, 7), (2, 2, 7)],
            ....:        key=lambda k: T(k[2:3]))
            sage: print(R.repr_full(reverse=True))
            poset((1, 1, 42), (2, 1, 7))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (1, 1, 42)
            +-- (1, 1, 42)
            |   +-- successors:   oo
            |   +-- predecessors: (2, 1, 7)
            +-- (2, 1, 7)
            |   +-- successors:   (1, 1, 42)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (2, 1, 7)
            |   +-- no predecessors

        ::

            sage: P = MP()
            sage: P.add(None)
            Traceback (most recent call last):
            ...
            ValueError: None is not an allowed element.
        """
    def remove(self, key, raise_key_error: bool = True) -> None:
        """
        Remove the given object from the poset.

        INPUT:

        - ``key`` -- the key of an object

        - ``raise_key_error`` -- boolean (default: ``True``); switch raising
          :exc:`KeyError` on and off

        OUTPUT: nothing

        If the element is not a member and ``raise_key_error`` is set
        (default), raise a :exc:`KeyError`.

        .. NOTE::

            As with Python's ``set``, the methods :meth:`remove`
            and :meth:`discard` only differ in their behavior when an
            element is not contained in the poset: :meth:`remove`
            raises a :exc:`KeyError` whereas :meth:`discard` does not
            raise any exception.

            This default behavior can be overridden with the
            ``raise_key_error`` parameter.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: print(P.repr_full(reverse=True))
            poset((4, 4), (1, 3), (2, 2), (1, 2), (2, 1), (1, 1))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (4, 4)
            +-- (4, 4)
            |   +-- successors:   oo
            |   +-- predecessors: (1, 3), (2, 2)
            +-- (1, 3)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 2)
            +-- (2, 2)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 2), (2, 1)
            +-- (1, 2)
            |   +-- successors:   (1, 3), (2, 2)
            |   +-- predecessors: (1, 1)
            +-- (2, 1)
            |   +-- successors:   (2, 2)
            |   +-- predecessors: (1, 1)
            +-- (1, 1)
            |   +-- successors:   (1, 2), (2, 1)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (1, 1)
            |   +-- no predecessors
            sage: P.remove(T((1, 2)))
            sage: print(P.repr_full(reverse=True))
            poset((4, 4), (1, 3), (2, 2), (2, 1), (1, 1))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (4, 4)
            +-- (4, 4)
            |   +-- successors:   oo
            |   +-- predecessors: (1, 3), (2, 2)
            +-- (1, 3)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (1, 1)
            +-- (2, 2)
            |   +-- successors:   (4, 4)
            |   +-- predecessors: (2, 1)
            +-- (2, 1)
            |   +-- successors:   (2, 2)
            |   +-- predecessors: (1, 1)
            +-- (1, 1)
            |   +-- successors:   (1, 3), (2, 1)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (1, 1)
            |   +-- no predecessors

        .. SEEALSO::

            :meth:`add`,
            :meth:`clear`,
            :meth:`discard`,
            :meth:`pop`.

        TESTS::

            sage: Q = MP([(1, 1, 42), (1, 3, 42), (2, 1, 7),
            ....:         (4, 4, 42), (1, 2, 7), (2, 2, 7)],
            ....:        key=lambda k: T(k[0:2]))
            sage: print(Q.repr_full(reverse=True))
            poset((4, 4, 42), (1, 3, 42), (2, 2, 7),
                  (1, 2, 7), (2, 1, 7), (1, 1, 42))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (4, 4, 42)
            +-- (4, 4, 42)
            |   +-- successors:   oo
            |   +-- predecessors: (1, 3, 42), (2, 2, 7)
            +-- (1, 3, 42)
            |   +-- successors:   (4, 4, 42)
            |   +-- predecessors: (1, 2, 7)
            +-- (2, 2, 7)
            |   +-- successors:   (4, 4, 42)
            |   +-- predecessors: (1, 2, 7), (2, 1, 7)
            +-- (1, 2, 7)
            |   +-- successors:   (1, 3, 42), (2, 2, 7)
            |   +-- predecessors: (1, 1, 42)
            +-- (2, 1, 7)
            |   +-- successors:   (2, 2, 7)
            |   +-- predecessors: (1, 1, 42)
            +-- (1, 1, 42)
            |   +-- successors:   (1, 2, 7), (2, 1, 7)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (1, 1, 42)
            |   +-- no predecessors
            sage: Q.remove((1,1))
            sage: print(Q.repr_full(reverse=True))
            poset((4, 4, 42), (1, 3, 42), (2, 2, 7), (1, 2, 7), (2, 1, 7))
            +-- oo
            |   +-- no successors
            |   +-- predecessors: (4, 4, 42)
            +-- (4, 4, 42)
            |   +-- successors:   oo
            |   +-- predecessors: (1, 3, 42), (2, 2, 7)
            +-- (1, 3, 42)
            |   +-- successors:   (4, 4, 42)
            |   +-- predecessors: (1, 2, 7)
            +-- (2, 2, 7)
            |   +-- successors:   (4, 4, 42)
            |   +-- predecessors: (1, 2, 7), (2, 1, 7)
            +-- (1, 2, 7)
            |   +-- successors:   (1, 3, 42), (2, 2, 7)
            |   +-- predecessors: null
            +-- (2, 1, 7)
            |   +-- successors:   (2, 2, 7)
            |   +-- predecessors: null
            +-- null
            |   +-- successors:   (1, 2, 7), (2, 1, 7)
            |   +-- no predecessors

        ::

            sage: P = MP()
            sage: P.remove(None)
            Traceback (most recent call last):
            ...
            ValueError: None is not an allowed key.
        """
    def discard(self, key, raise_key_error: bool = False):
        """
        Remove the given object from the poset.

        INPUT:

        - ``key`` -- the key of an object

        - ``raise_key_error`` -- boolean (default: ``False``); switch raising
          :exc:`KeyError` on and off

        OUTPUT: nothing

        If the element is not a member and ``raise_key_error`` is set
        (not default), raise a :exc:`KeyError`.

        .. NOTE::

            As with Python's ``set``, the methods :meth:`remove`
            and :meth:`discard` only differ in their behavior when an
            element is not contained in the poset: :meth:`remove`
            raises a :exc:`KeyError` whereas :meth:`discard` does not
            raise any exception.

            This default behavior can be overridden with the
            ``raise_key_error`` parameter.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: P.discard(T((1, 2)))
            sage: P.remove(T((1, 2)))
            Traceback (most recent call last):
            ...
            KeyError: 'Key (1, 2) is not contained in this poset.'
            sage: P.discard(T((1, 2)))

        .. SEEALSO::

            :meth:`add`,
            :meth:`clear`,
            :meth:`remove`,
            :meth:`pop`.
        """
    def pop(self, **kwargs):
        """
        Remove and return an arbitrary poset element.

        INPUT:

        - ``kwargs`` -- arguments are passed to :meth:`shells_topological`

        OUTPUT: an object

        .. NOTE::

            The special elements ``'null'`` and ``'oo'`` cannot be popped.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP()
            sage: P.add(3)
            sage: P
            poset(3)
            sage: P.pop()
            3
            sage: P
            poset()
            sage: P.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty poset'

        .. SEEALSO::

            :meth:`add`,
            :meth:`clear`,
            :meth:`discard`,
            :meth:`remove`.
        """
    def union(self, *other):
        """
        Return the union of the given posets as a new poset.

        INPUT:

        - ``other`` -- a poset or an iterable. In the latter case the
          iterated objects are seen as elements of a poset.
          It is possible to specify more than one ``other`` as
          variadic arguments (arbitrary argument lists).

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal.

            Due to keys and a ``merge`` function (see :class:`MutablePoset`)
            this operation might not be commutative.

        .. TODO::

            Use the already existing information in the other poset to speed
            up this function. (At the moment each element of the other poset
            is inserted one by one and without using this information.)

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.union(Q)
            poset(3, 4, 7, 8, 42)

        .. SEEALSO::

            :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.

        TESTS::

            sage: P.union(P, Q, Q, P)
            poset(3, 4, 7, 8, 42)
        """
    def union_update(self, *other) -> None:
        """
        Update this poset with the union of itself and another poset.

        INPUT:

        - ``other`` -- a poset or an iterable. In the latter case the
          iterated objects are seen as elements of a poset.
          It is possible to specify more than one ``other`` as
          variadic arguments (arbitrary argument lists).

        OUTPUT: nothing

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal;
            ``A.union_update(B)`` and ``B.union_update(A)`` might
            result in different posets.

        .. TODO::

            Use the already existing information in the other poset to speed
            up this function. (At the moment each element of the other poset
            is inserted one by one and without using this information.)

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.union_update(Q)
            sage: P
            poset(3, 4, 7, 8, 42)

        .. SEEALSO::

            :meth:`union`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.

        TESTS::

            sage: Q.update(P)
            sage: Q
            poset(3, 4, 7, 8, 42)
        """
    update = union_update
    def difference(self, *other):
        """
        Return a new poset where all elements of this poset, which are
        contained in one of the other given posets, are removed.

        INPUT:

        - ``other`` -- a poset or an iterable. In the latter case the
          iterated objects are seen as elements of a poset.
          It is possible to specify more than one ``other`` as
          variadic arguments (arbitrary argument lists).

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.difference(Q)
            poset(3, 7)

        .. SEEALSO::

            :meth:`union`, :meth:`union_update`,
            :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.

        TESTS::

            sage: P.difference(Q, Q)
            poset(3, 7)
            sage: P.difference(P)
            poset()
            sage: P.difference(Q, P)
            poset()
        """
    def difference_update(self, *other) -> None:
        """
        Remove all elements of another poset from this poset.

        INPUT:

        - ``other`` -- a poset or an iterable. In the latter case the
          iterated objects are seen as elements of a poset.
          It is possible to specify more than one ``other`` as
          variadic arguments (arbitrary argument lists).

        OUTPUT: nothing

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.difference_update(Q)
            sage: P
            poset(3, 7)

        .. SEEALSO::

            :meth:`union`, :meth:`union_update`,
            :meth:`difference`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.
        """
    def intersection(self, *other):
        """
        Return the intersection of the given posets as a new poset.

        INPUT:

        - ``other`` -- a poset or an iterable. In the latter case the
          iterated objects are seen as elements of a poset.
          It is possible to specify more than one ``other`` as
          variadic arguments (arbitrary argument lists).

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.intersection(Q)
            poset(42)

        .. SEEALSO::

            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.

        TESTS::

            sage: P.intersection(P, Q, Q, P)
            poset(42)
        """
    def intersection_update(self, *other) -> None:
        """
        Update this poset with the intersection of itself and another poset.

        INPUT:

        - ``other`` -- a poset or an iterable. In the latter case the
          iterated objects are seen as elements of a poset.
          It is possible to specify more than one ``other`` as
          variadic arguments (arbitrary argument lists).

        OUTPUT: nothing

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal;
            ``A.intersection_update(B)`` and ``B.intersection_update(A)`` might
            result in different posets.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.intersection_update(Q)
            sage: P
            poset(42)

        .. SEEALSO::

            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.
        """
    def symmetric_difference(self, other):
        """
        Return the symmetric difference of two posets as a new poset.

        INPUT:

        - ``other`` -- a poset

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.symmetric_difference(Q)
            poset(3, 4, 7, 8)

        .. SEEALSO::

            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference_update`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.
        """
    def symmetric_difference_update(self, other) -> None:
        """
        Update this poset with the symmetric difference of itself and
        another poset.

        INPUT:

        - ``other`` -- a poset

        OUTPUT: nothing

        .. NOTE::

            The key of an element is used for comparison. Thus elements with
            the same key are considered as equal;
            ``A.symmetric_difference_update(B)`` and
            ``B.symmetric_difference_update(A)`` might
            result in different posets.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.symmetric_difference_update(Q)
            sage: P
            poset(3, 4, 7, 8)

        .. SEEALSO::

            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`,
            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`is_superset`.
        """
    def is_disjoint(self, other):
        """
        Return whether another poset is disjoint to this poset.

        INPUT:

        - ``other`` -- a poset or an iterable; in the latter case the
          iterated objects are seen as elements of a poset

        OUTPUT: nothing

        .. NOTE::

            If this poset uses a ``key``-function, then all
            comparisons are performed on the keys of the elements (and
            not on the elements themselves).

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.is_disjoint(Q)
            False
            sage: P.is_disjoint(Q.difference(P))
            True

        .. SEEALSO::

            :meth:`is_subset`,
            :meth:`is_superset`,
            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`.
        """
    isdisjoint = is_disjoint
    def is_subset(self, other):
        """
        Return whether another poset contains this poset, i.e., whether this poset
        is a subset of the other poset.

        INPUT:

        - ``other`` -- a poset or an iterable; in the latter case the
          iterated objects are seen as elements of a poset

        OUTPUT: nothing

        .. NOTE::

            If this poset uses a ``key``-function, then all
            comparisons are performed on the keys of the elements (and
            not on the elements themselves).

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.is_subset(Q)
            False
            sage: Q.is_subset(P)
            False
            sage: P.is_subset(P)
            True
            sage: P.is_subset(P.union(Q))
            True

        .. SEEALSO::

            :meth:`is_disjoint`,
            :meth:`is_superset`,
            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`.
        """
    issubset = is_subset
    def is_superset(self, other):
        """
        Return whether this poset contains another poset, i.e., whether this poset
        is a superset of the other poset.

        INPUT:

        - ``other`` -- a poset or an iterable; in the latter case the
          iterated objects are seen as elements of a poset

        OUTPUT: nothing

        .. NOTE::

            If this poset uses a ``key``-function, then all
            comparisons are performed on the keys of the elements (and
            not on the elements themselves).

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: P = MP([3, 42, 7]); P
            poset(3, 7, 42)
            sage: Q = MP([4, 8, 42]); Q
            poset(4, 8, 42)
            sage: P.is_superset(Q)
            False
            sage: Q.is_superset(P)
            False
            sage: P.is_superset(P)
            True
            sage: P.union(Q).is_superset(P)
            True

        .. SEEALSO::

            :meth:`is_disjoint`,
            :meth:`is_subset`,
            :meth:`union`, :meth:`union_update`,
            :meth:`difference`, :meth:`difference_update`,
            :meth:`intersection`, :meth:`intersection_update`,
            :meth:`symmetric_difference`, :meth:`symmetric_difference_update`.
        """
    issuperset = is_superset
    def merge(self, key=None, reverse: bool = False):
        """
        Merge the given element with its successors/predecessors.

        INPUT:

        - ``key`` -- the key specifying an element or ``None``
          (default), in which case this method is called on each
          element in this poset

        - ``reverse`` -- boolean (default: ``False``); specifies which
          direction to go first:
          ``False`` searches towards ``'oo'`` and
          ``True`` searches towards ``'null'``.
          When ``key=None``, then this also
          specifies which elements are merged first.

        OUTPUT: nothing

        This method tests all (not necessarily direct) successors and
        predecessors of the given element whether they can be merged with
        the element itself. This is done by the ``can_merge``-function
        of :class:`MutablePoset`. If this merge is possible, then it
        is performed by calling :class:`MutablePoset`'s
        ``merge``-function and the corresponding successor/predecessor
        is removed from the poset.

        .. NOTE::

            ``can_merge`` is applied in the sense of the condition of
            depth first iteration, i.e., once ``can_merge`` fails,
            the successors/predecessors are no longer tested.

        .. NOTE::

            The motivation for such a merge behavior comes from
            asymptotic expansions: `O(n^3)` merges with, for
            example, `3n^2` or `O(n)` to `O(n^3)` (as `n` tends to
            `\\infty`; see :wikipedia:`Big_O_notation`).

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: key = lambda t: T(t[0:2])
            sage: def add(left, right):
            ....:     return (left[0], left[1],
            ....:             ''.join(sorted(left[2] + right[2])))
            sage: def can_add(left, right):
            ....:     return key(left) >= key(right)
            sage: P = MP([(1, 1, 'a'), (1, 3, 'b'), (2, 1, 'c'),
            ....:         (4, 4, 'd'), (1, 2, 'e'), (2, 2, 'f')],
            ....:        key=key, merge=add, can_merge=can_add)
            sage: Q = copy(P)
            sage: Q.merge(T((1, 3)))
            sage: print(Q.repr_full(reverse=True))
            poset((4, 4, 'd'), (1, 3, 'abe'), (2, 2, 'f'), (2, 1, 'c'))
            +-- oo
            |   +-- no successors
            |   +-- predecessors:   (4, 4, 'd')
            +-- (4, 4, 'd')
            |   +-- successors:   oo
            |   +-- predecessors:   (1, 3, 'abe'), (2, 2, 'f')
            +-- (1, 3, 'abe')
            |   +-- successors:   (4, 4, 'd')
            |   +-- predecessors:   null
            +-- (2, 2, 'f')
            |   +-- successors:   (4, 4, 'd')
            |   +-- predecessors:   (2, 1, 'c')
            +-- (2, 1, 'c')
            |   +-- successors:   (2, 2, 'f')
            |   +-- predecessors:   null
            +-- null
            |   +-- successors:   (1, 3, 'abe'), (2, 1, 'c')
            |   +-- no predecessors
            sage: for k in sorted(P.keys()):
            ....:     Q = copy(P)
            ....:     Q.merge(k)
            ....:     print('merging %s: %s' % (k, Q))
            merging (1, 1): poset((1, 1, 'a'), (1, 2, 'e'), (1, 3, 'b'),
                                  (2, 1, 'c'), (2, 2, 'f'), (4, 4, 'd'))
            merging (1, 2): poset((1, 2, 'ae'), (1, 3, 'b'), (2, 1, 'c'),
                                  (2, 2, 'f'), (4, 4, 'd'))
            merging (1, 3): poset((1, 3, 'abe'), (2, 1, 'c'), (2, 2, 'f'),
                                  (4, 4, 'd'))
            merging (2, 1): poset((1, 2, 'e'), (1, 3, 'b'), (2, 1, 'ac'),
                                  (2, 2, 'f'), (4, 4, 'd'))
            merging (2, 2): poset((1, 3, 'b'), (2, 2, 'acef'), (4, 4, 'd'))
            merging (4, 4): poset((4, 4, 'abcdef'))

            sage: Q = copy(P)
            sage: Q.merge(); Q
            poset((4, 4, 'abcdef'))

        .. SEEALSO::

            :meth:`MutablePosetShell.merge`

        TESTS::

            sage: copy(P).merge(reverse=False) == copy(P).merge(reverse=True)
            True

        ::

            sage: P = MP(srange(4),
            ....:        merge=lambda l, r: l, can_merge=lambda l, r: l >= r); P
            poset(0, 1, 2, 3)
            sage: Q = P.copy()
            sage: Q.merge(reverse=True); Q
            poset(3)
            sage: R = P.mapped(lambda x: x+1)
            sage: R.merge(reverse=True); R
            poset(4)

        ::

            sage: P = MP(srange(4),
            ....:        merge=lambda l, r: r, can_merge=lambda l, r: l < r)
            sage: P.merge()
            Traceback (most recent call last):
            ...
            RuntimeError: Stopping merge before started;
            the can_merge-function is not reflexive.
        """
    def maximal_elements(self):
        """
        Return an iterator over the maximal elements of this poset.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 1)), T((1, 3)), T((2, 1)),
            ....:         T((1, 2)), T((2, 2))])
            sage: sorted(P.maximal_elements())
            [(1, 3), (2, 2)]

        .. SEEALSO::

            :meth:`minimal_elements`
        """
    def minimal_elements(self):
        """
        Return an iterator over the minimal elements of this poset.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: sorted(P.minimal_elements())
            [(1, 2), (2, 1)]

        .. SEEALSO::

            :meth:`maximal_elements`
        """
    def map(self, function, topological: bool = False, reverse: bool = False) -> None:
        """
        Apply the given ``function`` to each element of this poset.

        INPUT:

        - ``function`` -- a function mapping an existing element to
          a new element

        - ``topological`` -- boolean (default: ``False``); if set, then the
          mapping is done in topological order, otherwise unordered

        - ``reverse`` -- is passed on to topological ordering

        OUTPUT: nothing

        .. NOTE::

            Since this method works inplace, it is not allowed that
            ``function`` alters the key of an element.

        .. NOTE::

            If ``function`` returns ``None``, then the element is
            removed.

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))],
            ....:        key=lambda e: e[:2])
            sage: P.map(lambda e: e + (sum(e),))
            sage: P
            poset((1, 2, 3), (1, 3, 4), (2, 1, 3), (2, 2, 4), (4, 4, 8))

        TESTS::

            sage: P.map(lambda e: e if e[2] != 4 else None); P
            poset((1, 2, 3), (2, 1, 3), (4, 4, 8))

        .. SEEALSO::

            :meth:`copy`,
            :meth:`mapped`.
        """
    def mapped(self, function):
        """
        Return a poset where on each element the given ``function``
        was applied.

        INPUT:

        - ``function`` -- a function mapping an existing element to
          a new element

        - ``topological`` -- boolean (default: ``False``); if set, then the
          mapping is done in topological order, otherwise unordered

        - ``reverse`` -- is passed on to topological ordering

        OUTPUT: a :class:`MutablePoset`

        .. NOTE::

            ``function`` is not allowed to change the order of the keys,
            but changing the keys themselves is allowed (in contrast
            to :meth:`map`).

        EXAMPLES::

            sage: from sage.data_structures.mutable_poset import MutablePoset as MP
            sage: class T(tuple):
            ....:     def __le__(left, right):
            ....:         return all(l <= r for l, r in zip(left, right))
            sage: P = MP([T((1, 3)), T((2, 1)),
            ....:         T((4, 4)), T((1, 2)), T((2, 2))])
            sage: P.mapped(lambda e: str(e))
            poset('(1, 2)', '(1, 3)', '(2, 1)', '(2, 2)', '(4, 4)')

        .. SEEALSO::

            :meth:`copy`,
            :meth:`map`.
        """
