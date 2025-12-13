from sage.categories.fields import Fields as Fields
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class EvenlyDistributedSetsBacktracker:
    '''EvenlyDistributedSetsBacktracker(K, k, up_to_isomorphism=True, check=False)

    File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 30)

    Set of evenly distributed subsets in finite fields.

        **Definition:** Let `K` be a finite field of cardinality `q` and `k` an
        integer so that `k(k-1)` divides `q-1`. Let `H = K^*` be the
        multiplicative group of invertible elements in `K`. A `k`-*evenly
        distributed set* in `K` is a set `B = \\{b_1, b_2, \\ldots, b_k\\}` of `k`
        elements of `K` so that the `k(k-1)` differences `\\Delta B = \\{b_i -
        b_j; i \\not= j\\}` hit each coset modulo `H^{2(q-1)/(k(k-1))}` exactly
        twice.

    Evenly distributed sets were introduced by Wilson [Wi72]_ (see also
    [BJL99-1]_, Chapter VII.6). He proved that for any `k`, and for any prime power
    `q` large enough such that `k(k-1)` divides `k` there exists a `k`-evenly
    distributed set in the field of cardinality `q`. This existence result based
    on a counting argument (using Dirichlet theorem) does not provide a simple
    method to generate them.

    From a `k`-evenly distributed set, it is straightforward to build a
    `(q,k,1)`-difference family (see :meth:`to_difference_family`). Another
    approach to generate a difference family, somehow dual to this one, is via
    radical difference family (see in particular
    :func:`~sage.combinat.designs.difference_family.radical_difference_family`
    from the module :mod:`~sage.combinat.designs.difference_family`).

    By default, this backtracker only considers evenly distributed sets up to
    affine automorphisms, i.e. `B` is considered equivalent to `s B + t` for any
    invertible element `s` and any element `t` in the field `K`. Note that the
    set of differences is just multiplicatively translated by `s` as `\\Delta (s
    B + t) = s (\\Delta B)`, and so that `B` is an evenly distributed set if and
    only if `sB` is one too. This behaviour can be modified via the argument
    ``up_to_isomorphism`` (see the input section and the examples below).

    INPUT:

    - ``K`` -- a finite field of cardinality `q`

    - ``k`` -- positive integer such that `k(k-1)` divides `q-1`

    - ``up_to_isomorphism`` -- boolean (default: ``True``); whether only consider
      evenly distributed sets up to automorphisms of the field of the form
      `x \\mapsto ax + b`. If set to ``False`` then the iteration is over all
      evenly distributed sets that contain ``0`` and ``1``.

    - ``check`` -- boolean (default: ``False``); whether you want to check
      intermediate steps of the iterator. This is mainly intended for debugging
      purpose. Setting it to ``True`` will considerably slow the iteration.

    EXAMPLES:

    The main part of the code is contained in the iterator. To get one evenly
    distributed set just do::

        sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker
        sage: E = EvenlyDistributedSetsBacktracker(Zmod(151),6)
        sage: B = E.an_element()
        sage: B
        [0, 1, 69, 36, 57, 89]

    The class has a method to convert it to a difference family::

        sage: E.to_difference_family(B)
        [[0, 1, 69, 36, 57, 89],
         [0, 132, 48, 71, 125, 121],
         [0, 59, 145, 10, 41, 117],
         [0, 87, 114, 112, 127, 42],
         [0, 8, 99, 137, 3, 108]]

    It is also possible to run over all evenly distributed sets::

        sage: E = EvenlyDistributedSetsBacktracker(Zmod(13), 4, up_to_isomorphism=False)
        sage: for B in E: print(B)
        [0, 1, 11, 5]
        [0, 1, 4, 6]
        [0, 1, 9, 3]
        [0, 1, 8, 10]

        sage: E = EvenlyDistributedSetsBacktracker(Zmod(13), 4, up_to_isomorphism=True)
        sage: for B in E: print(B)
        [0, 1, 11, 5]


    Or only count them::

        sage: for k in range(13, 200, 12):
        ....:     if is_prime_power(k):
        ....:         K = GF(k,\'a\')
        ....:         E1 = EvenlyDistributedSetsBacktracker(K, 4, False)
        ....:         E2 = EvenlyDistributedSetsBacktracker(K, 4, True)
        ....:         print("{:3} {:3} {:3}".format(k, E1.cardinality(), E2.cardinality()))
         13   4   1
         25  40   4
         37  12   1
         49  24   2
         61  12   1
         73  48   4
         97  64   6
        109  72   6
        121 240  20
        157  96   8
        169 240  20
        181 204  17
        193 336  28

    Note that by definition, the number of evenly distributed sets up to
    isomorphisms is at most `k(k-1)` times smaller than without isomorphisms.
    But it might not be exactly `k(k-1)` as some of them might have symmetries::

        sage: B = EvenlyDistributedSetsBacktracker(Zmod(13), 4).an_element()
        sage: B
        [0, 1, 11, 5]
        sage: [9*x + 5 for x in B]
        [5, 1, 0, 11]
        sage: [3*x + 11 for x in B]
        [11, 1, 5, 0]'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, K, k, up_to_isomorphism=..., check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 175)

                TESTS::

                    sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

                    sage: EvenlyDistributedSetsBacktracker(Zmod(4),2)
                    Traceback (most recent call last):
                    ...
                    ValueError: Ring of integers modulo 4 is not a field

                    sage: EvenlyDistributedSetsBacktracker(Zmod(71),7)
                    Traceback (most recent call last):
                    ...
                    ValueError: k(k-1)=42 does not divide q-1=70

                For `q=421` which is congruent to 1 modulo `12`, `20`, `30` and `42` we
                run backtracker with the ``check`` argument set to ``True``::

                    sage: for _ in EvenlyDistributedSetsBacktracker(Zmod(421), 4, check=True):
                    ....:     pass
                    sage: for _ in EvenlyDistributedSetsBacktracker(Zmod(421), 5, check=True):
                    ....:    pass
                    sage: for _ in EvenlyDistributedSetsBacktracker(Zmod(421), 6, check=True):
                    ....:    pass
                    sage: for _ in EvenlyDistributedSetsBacktracker(Zmod(421), 7, check=True):
                    ....:    pass
        """
    @overload
    def an_element(self) -> Any:
        """EvenlyDistributedSetsBacktracker.an_element(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 315)

        Return an evenly distributed set.

        If there is no such subset raise an
        :class:`~sage.categories.sets_cat.EmptySetError`.

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(41),5)
            sage: E.an_element()
            [0, 1, 13, 38, 31]

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(61),6)
            sage: E.an_element()
            Traceback (most recent call last):
            ...
            EmptySetError: no 6-evenly distributed set in Ring of integers modulo 61"""
    @overload
    def an_element(self) -> Any:
        """EvenlyDistributedSetsBacktracker.an_element(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 315)

        Return an evenly distributed set.

        If there is no such subset raise an
        :class:`~sage.categories.sets_cat.EmptySetError`.

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(41),5)
            sage: E.an_element()
            [0, 1, 13, 38, 31]

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(61),6)
            sage: E.an_element()
            Traceback (most recent call last):
            ...
            EmptySetError: no 6-evenly distributed set in Ring of integers modulo 61"""
    @overload
    def an_element(self) -> Any:
        """EvenlyDistributedSetsBacktracker.an_element(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 315)

        Return an evenly distributed set.

        If there is no such subset raise an
        :class:`~sage.categories.sets_cat.EmptySetError`.

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(41),5)
            sage: E.an_element()
            [0, 1, 13, 38, 31]

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(61),6)
            sage: E.an_element()
            Traceback (most recent call last):
            ...
            EmptySetError: no 6-evenly distributed set in Ring of integers modulo 61"""
    @overload
    def cardinality(self) -> Any:
        """EvenlyDistributedSetsBacktracker.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 364)

        Return the number of evenly distributed sets.

        Use with precaution as there can be a lot of such sets and this method
        might be very long to answer!

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(GF(25,'a'), 4); E
            4-evenly distributed sets (up to isomorphism)
             in Finite Field in a of size 5^2
            sage: E.cardinality()
            4

            sage: E = EvenlyDistributedSetsBacktracker(GF(25,'a'), 4,
            ....:                                      up_to_isomorphism=False)
            sage: E.cardinality()
            40"""
    @overload
    def cardinality(self) -> Any:
        """EvenlyDistributedSetsBacktracker.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 364)

        Return the number of evenly distributed sets.

        Use with precaution as there can be a lot of such sets and this method
        might be very long to answer!

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(GF(25,'a'), 4); E
            4-evenly distributed sets (up to isomorphism)
             in Finite Field in a of size 5^2
            sage: E.cardinality()
            4

            sage: E = EvenlyDistributedSetsBacktracker(GF(25,'a'), 4,
            ....:                                      up_to_isomorphism=False)
            sage: E.cardinality()
            40"""
    @overload
    def cardinality(self) -> Any:
        """EvenlyDistributedSetsBacktracker.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 364)

        Return the number of evenly distributed sets.

        Use with precaution as there can be a lot of such sets and this method
        might be very long to answer!

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(GF(25,'a'), 4); E
            4-evenly distributed sets (up to isomorphism)
             in Finite Field in a of size 5^2
            sage: E.cardinality()
            4

            sage: E = EvenlyDistributedSetsBacktracker(GF(25,'a'), 4,
            ....:                                      up_to_isomorphism=False)
            sage: E.cardinality()
            40"""
    def to_difference_family(self, B, check=...) -> Any:
        '''EvenlyDistributedSetsBacktracker.to_difference_family(self, B, check=True)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 265)

        Given an evenly distributed set ``B`` convert it to a difference family.

        As for any `x\\in K^*=H` we have `|\\Delta B \\cap x
        H^{2(q-1)/(k(k-1))}|=2` (see :class:`EvenlyDistributedSetsBacktracker`),
        the difference family is produced as `\\{xB:x\\in H^{2(q-1)/(k(k-1))}\\}`

        This method is useful if you want to obtain the difference family from
        the output of the iterator.

        INPUT:

        - ``B`` -- an evenly distributed set

        - ``check`` -- boolean (default: ``True``); whether to check the result

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker
            sage: E = EvenlyDistributedSetsBacktracker(Zmod(41),5)
            sage: B = E.an_element(); B
            [0, 1, 13, 38, 31]
            sage: D = E.to_difference_family(B); D
            [[0, 1, 13, 38, 31], [0, 32, 6, 27, 8]]

            sage: from sage.combinat.designs.difference_family import is_difference_family
            sage: is_difference_family(Zmod(41),D,41,5,1)
            True

        Setting ``check`` to ``False`` is much faster::

            sage: timeit("df = E.to_difference_family(B, check=True)") # random
            625 loops, best of 3: 117 µs per loop

            sage: timeit("df = E.to_difference_family(B, check=False)")  # random
            625 loops, best of 3: 1.83 µs per loop'''
    def __iter__(self) -> Any:
        """EvenlyDistributedSetsBacktracker.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/evenly_distributed_sets.pyx (starting at line 469)

        Iterator through all evenly distributed sets that start with `[0,1]`.

        EXAMPLES::

            sage: from sage.combinat.designs.evenly_distributed_sets import EvenlyDistributedSetsBacktracker

            sage: E = EvenlyDistributedSetsBacktracker(Zmod(13),4)
            sage: for B in E:
            ....:     print(B)
            [0, 1, 11, 5]"""
