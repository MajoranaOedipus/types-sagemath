from sage.combinat.combinat import CombinatorialElement as CombinatorialElement

class SJT(CombinatorialElement):
    """
    A representation of a list permuted using the Steinhaus-Johnson-Trotter
    algorithm.

    Each element of the list has a direction (initialized at -1) that
    changes at each permutation and that is used to determine which
    elements to transpose.  The directions have three possible values:

    - ``-1``: element transposes to the left

    - ``1``: element transposes to the right

    - ``0``: element does not move

    Thus in addition to the permutation itself, the direction of each
    element is also stored.

    Note that the permutations are not generated in lexicographic order.

    .. WARNING::

        An ``SJT`` object should always be created with identity
        permutation for the algorithm to behave properly. If the
        identity permutation is not provided, it expects a coherent
        list of directions according to the provided input. This list
        is not checked.

    .. TODO::

        Implement the previous permutation for the Steinhaus-Johnson-Trotter
        algorithm.

    EXAMPLES::

        sage: from sage.combinat.SJT import SJT
        sage: s = SJT([1, 2, 3, 4]); s
        [1, 2, 3, 4]
        sage: s = s.next(); s
        [1, 2, 4, 3]
        sage: p = Permutation(s._list, algorithm='sjt', sjt=s)
        sage: p
        [1, 2, 4, 3]
        sage: p.next()
        [1, 4, 2, 3]

    TESTS::

        sage: from sage.combinat.SJT import SJT
        sage: s = SJT([1, 2, 3, 4]); s
        [1, 2, 3, 4]
        sage: s = SJT([1]); s
        [1]
        sage: s = s.next(); s
        False
        sage: s = SJT([]); s
        []
        sage: s = s.next(); s
        False
    """
    def __init__(self, l, directions=None) -> None:
        """
        Transpose two elements at positions ``a`` and ``b`` in ``perm`` and
        their corresponding directions as well following the
        Steinhaus-Johnson-Trotter algorithm.

        Each permutation is obtained by transposing two adjacent elements from
        the previous permutation.

        INPUT:

        - ``l`` -- list; a list of ordered ``int``.

        - ``directions`` -- list (default: ``None``); a list of
          directions for each element in the permuted list. Used when
          constructing permutations from a pre-defined internal state.

        EXAMPLES::

            sage: from sage.combinat.SJT import SJT
            sage: s = SJT([1, 2, 3, 4]); s
            [1, 2, 3, 4]
            sage: s = s.next(); s
            [1, 2, 4, 3]
            sage: p = Permutation(s._list, algorithm='sjt', sjt=s)
            sage: p
            [1, 2, 4, 3]
            sage: p.next()
            [1, 4, 2, 3]

        TESTS::

            sage: from sage.combinat.SJT import SJT
            sage: s = SJT([1, 3, 2, 4])
            Traceback (most recent call last):
            ...
            ValueError: no internal state directions were given
            for non-identity starting permutation
            for Steinhaus-Johnson-Trotter algorithm
            sage: s = SJT([]); s
            []
            sage: s = s.next(); s
            False
        """
    def next(self):
        """
        Produce the next permutation of ``self`` following the
        Steinhaus-Johnson-Trotter algorithm.

        OUTPUT: the list of the next permutation

        EXAMPLES::

            sage: from sage.combinat.SJT import SJT
            sage: s = SJT([1, 2, 3, 4])
            sage: s = s.next(); s
            [1, 2, 4, 3]
            sage: s = s.next(); s
            [1, 4, 2, 3]

        TESTS::

            sage: from sage.combinat.SJT import SJT
            sage: s = SJT([1, 2, 3])
            sage: s.next()
            [1, 3, 2]

            sage: s = SJT([1])
            sage: s.next()
            False
        """
    __next__ = next
