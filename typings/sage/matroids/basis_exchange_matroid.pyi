import sage.matroids.matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class BasisExchangeMatroid(sage.matroids.matroid.Matroid):
    """BasisExchangeMatroid(groundset, basis=None, rank=None)

    File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 32)

    Class BasisExchangeMatroid is a virtual class that derives from Matroid.
    It implements each of the elementary matroid methods
    (:meth:`rank() <sage.matroids.matroid.Matroid.rank>`,
    :meth:`max_independent() <sage.matroids.matroid.Matroid.max_independent>`,
    :meth:`circuit() <sage.matroids.matroid.Matroid.circuit>`,
    :meth:`closure() <sage.matroids.matroid.Matroid.closure>` etc.),
    essentially by crawling the base exchange graph of the matroid. This is
    the graph whose vertices are the bases of the matroid, two bases being
    adjacent in the graph if their symmetric difference has 2 members.

    This base exchange graph is not stored as such, but should be provided
    implicitly by the child class in the form of two methods
    ``_is_exchange_pair(x, y)`` and ``_exchange(x, y)``, as well as an
    initial basis. At any moment, BasisExchangeMatroid keeps a current basis
    `B`. The method ``_is_exchange_pair(x, y)`` should return a boolean
    indicating whether `B - x + y` is a basis. The method ``_exchange(x, y)``
    is called when the current basis `B` is replaced by said `B-x + y`. It is
    up to the child class to update its internal data structure to make
    information relative to the new basis more accessible. For instance, a
    linear matroid would perform a row reduction to make the column labeled by
    `y` a standard basis vector (and therefore the columns indexed by `B-x+y`
    would form an identity matrix).

    Each of the elementary matroid methods has a straightforward greedy-type
    implementation in terms of these two methods. For example, given a subset
    `F` of the groundset, one can step to a basis `B` over the edges of the
    base exchange graph which has maximal intersection with `F`, in each step
    increasing the intersection of the current `B` with `F`. Then one computes
    the rank of `F` as the cardinality of the intersection of `F` and `B`.

    The following matroid classes can/will implement their oracle efficiently
    by deriving from ``BasisExchangeMatroid``:

    - :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`: keeps
      a list of all bases.

        - ``_is_exchange_pair(x, y)`` reduces to a query whether `B - x + y`
          is a basis.
        - ``_exchange(x, y)`` has no work to do.

    - :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`:
      keeps a matrix representation `A` of the matroid so that `A[B] = I`.

        - ``_is_exchange_pair(x, y)`` reduces to testing whether `A[r, y]`
          is nonzero, where `A[r, x]=1`.
        - ``_exchange(x, y)`` should modify the matrix so that `A[B - x + y]`
          becomes `I`, which means pivoting on `A[r, y]`.

    - ``TransversalMatroid`` (not yet implemented): If `A` is a set of subsets
      of `E`, then `I` is independent if it is a system of distinct
      representatives of `A`, i.e. if `I` is covered by a matching of an
      appropriate bipartite graph `G`, with color classes `A` and `E` and an
      edge `(A_i,e)` if `e` is in the subset `A_i`. At any time you keep a
      maximum matching `M` of `G` covering the current basis `B`.

        - ``_is_exchange_pair(x, y)`` checks for the existence of an
          `M`-alternating path `P` from `y` to `x`.
        - ``_exchange(x, y)`` replaces `M` by the symmetric difference of
          `M` and `E(P)`.

    - ``AlgebraicMatroid`` (not yet implemented): keeps a list of polynomials
      in variables `E - B + e` for each variable `e` in `B`.

        - ``_is_exchange_pair(x, y)`` checks whether the polynomial that
          relates `y` to `E-B` uses `x`.
        - ``_exchange(x, y)`` make new list of polynomials by computing
          resultants.

    All but the first of the above matroids are algebraic, and all
    implementations specializations of the algebraic one.

    BasisExchangeMatroid internally renders subsets of the groundset as
    bitsets. It provides optimized methods for enumerating bases, nonbases,
    flats, circuits, etc."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, groundset, basis=..., rank=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 110)

                Construct a BasisExchangeMatroid.

                A BasisExchangeMatroid is a virtual class. It is unlikely that you
                want to create a BasisExchangeMatroid from the command line. See the
                class docstring for
                :class:`BasisExchangeMatroid <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid>`.

                INPUT:

                - ``groundset`` -- set
                - ``basis`` -- subset of groundset (default: ``None``)
                - ``rank`` -- integer (default: ``None``)

                This initializer sets up a correspondence between elements of
                ``groundset`` and ``range(len(groundset))``. ``BasisExchangeMatroid``
                uses this correspondence for encoding of subsets of the groundset as
                bitpacked sets of integers --- see ``_pack()`` and ``__unpack()``. In
                general, methods of ``BasisExchangeMatroid`` having a name starting
                with two underscores deal with such encoded subsets.

                A second task of this initializer is to store the rank and initialize
                the 'current' basis.

                EXAMPLES::

                    sage: from sage.matroids.basis_exchange_matroid import BasisExchangeMatroid
                    sage: M = BasisExchangeMatroid(groundset='abcdef', basis='abc')
                    sage: sorted(M.groundset())
                    ['a', 'b', 'c', 'd', 'e', 'f']
                    sage: sorted(M.basis())
                    ['a', 'b', 'c']


                TESTS::

                    sage: from sage.matroids.advanced import *
                    sage: M = BasisExchangeMatroid(groundset=[1, 2, 3], rank=2)
                    sage: TestSuite(M).run(skip='_test_pickling')

                .. NOTE::

                    This is an abstract base class, without a data structure, so no
                    pickling mechanism was implemented.
        """
    @overload
    def bases_count(self) -> Any:
        """BasisExchangeMatroid.bases_count(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1466)

        Return the number of bases of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: M.bases_count()
            184"""
    @overload
    def bases_count(self) -> Any:
        """BasisExchangeMatroid.bases_count(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1466)

        Return the number of bases of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: M.bases_count()
            184"""
    @overload
    def basis(self) -> Any:
        """BasisExchangeMatroid.basis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 573)

        Return an arbitrary basis of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. NOTE::

            The output of this method can change in between calls. It reflects
            the internal state of the matroid. This state is updated by lots
            of methods, including the method ``M._move_current_basis()``.

        OUTPUT: set of elements

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.basis())
            ['a', 'b', 'c']
            sage: M.rank('cd')
            2
            sage: sorted(M.basis())
            ['a', 'c', 'd']"""
    @overload
    def basis(self) -> Any:
        """BasisExchangeMatroid.basis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 573)

        Return an arbitrary basis of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. NOTE::

            The output of this method can change in between calls. It reflects
            the internal state of the matroid. This state is updated by lots
            of methods, including the method ``M._move_current_basis()``.

        OUTPUT: set of elements

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.basis())
            ['a', 'b', 'c']
            sage: M.rank('cd')
            2
            sage: sorted(M.basis())
            ['a', 'c', 'd']"""
    @overload
    def basis(self) -> Any:
        """BasisExchangeMatroid.basis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 573)

        Return an arbitrary basis of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. NOTE::

            The output of this method can change in between calls. It reflects
            the internal state of the matroid. This state is updated by lots
            of methods, including the method ``M._move_current_basis()``.

        OUTPUT: set of elements

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.basis())
            ['a', 'b', 'c']
            sage: M.rank('cd')
            2
            sage: sorted(M.basis())
            ['a', 'c', 'd']"""
    @overload
    def circuits(self, k=...) -> SetSystem:
        """BasisExchangeMatroid.circuits(self, k=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1764)

        Return the circuits of the matroid.

        OUTPUT: iterable containing all circuits

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`

        EXAMPLES::

            sage: M = Matroid(matroids.catalog.NonFano().bases())
            sage: sorted([sorted(C) for C in M.circuits()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'],
             ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'e', 'f'],
             ['a', 'd', 'g'], ['a', 'e', 'f', 'g'], ['b', 'c', 'd'],
             ['b', 'c', 'e', 'f'], ['b', 'd', 'e', 'f'], ['b', 'd', 'f', 'g'],
             ['b', 'e', 'g'], ['c', 'd', 'e', 'f'], ['c', 'd', 'e', 'g'],
             ['c', 'f', 'g'], ['d', 'e', 'f', 'g']]"""
    @overload
    def circuits(self) -> Any:
        """BasisExchangeMatroid.circuits(self, k=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1764)

        Return the circuits of the matroid.

        OUTPUT: iterable containing all circuits

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`

        EXAMPLES::

            sage: M = Matroid(matroids.catalog.NonFano().bases())
            sage: sorted([sorted(C) for C in M.circuits()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'],
             ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'e', 'f'],
             ['a', 'd', 'g'], ['a', 'e', 'f', 'g'], ['b', 'c', 'd'],
             ['b', 'c', 'e', 'f'], ['b', 'd', 'e', 'f'], ['b', 'd', 'f', 'g'],
             ['b', 'e', 'g'], ['c', 'd', 'e', 'f'], ['c', 'd', 'e', 'g'],
             ['c', 'f', 'g'], ['d', 'e', 'f', 'g']]"""
    @overload
    def cocircuits(self) -> SetSystem:
        """BasisExchangeMatroid.cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1718)

        Return the cocircuits of the matroid.

        OUTPUT: iterable containing all cocircuits

        .. SEEALSO::

            :meth:`Matroid.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.NonFano().bases())
            sage: sorted([sorted(C) for C in M.cocircuits()])
            [['a', 'b', 'c', 'd', 'g'], ['a', 'b', 'c', 'e', 'g'],
             ['a', 'b', 'c', 'f', 'g'], ['a', 'b', 'd', 'e'],
             ['a', 'c', 'd', 'f'], ['a', 'e', 'f', 'g'], ['b', 'c', 'e', 'f'],
             ['b', 'd', 'f', 'g'], ['c', 'd', 'e', 'g']]"""
    @overload
    def cocircuits(self) -> Any:
        """BasisExchangeMatroid.cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1718)

        Return the cocircuits of the matroid.

        OUTPUT: iterable containing all cocircuits

        .. SEEALSO::

            :meth:`Matroid.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.NonFano().bases())
            sage: sorted([sorted(C) for C in M.cocircuits()])
            [['a', 'b', 'c', 'd', 'g'], ['a', 'b', 'c', 'e', 'g'],
             ['a', 'b', 'c', 'f', 'g'], ['a', 'b', 'd', 'e'],
             ['a', 'c', 'd', 'f'], ['a', 'e', 'f', 'g'], ['b', 'c', 'e', 'f'],
             ['b', 'd', 'f', 'g'], ['c', 'd', 'e', 'g']]"""
    def coflats(self, longk) -> SetSystem:
        """BasisExchangeMatroid.coflats(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1331)

        Return the collection of coflats of the matroid of specified corank.

        A *coflat* is a coclosed set.

        INPUT:

        - ``k`` -- integer

        OUTPUT: iterable containing all coflats of corank `k`

        .. SEEALSO::

            :meth:`Matroid.coclosure() <sage.matroids.matroid.Matroid.coclosure>`

        EXAMPLES::

            sage: M = matroids.catalog.S8().dual()
            sage: M.whitney_numbers2()
            [1, 8, 22, 14, 1]
            sage: len(M.coflats(2))
            22
            sage: len(M.coflats(8))
            0
            sage: len(M.coflats(4))
            1"""
    @overload
    def components(self) -> Any:
        """BasisExchangeMatroid.components(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 974)

        Return an iterable containing the components of the matroid.

        A *component* is an inclusionwise maximal connected subset of the
        matroid. A subset is *connected* if the matroid resulting from
        deleting the complement of that subset is
        :meth:`connected <sage.matroids.matroid.Matroid.is_connected>`.

        OUTPUT: list of subsets

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: setprint(M.components())
            [{0, 1, 3, 4}, {2, 5}]"""
    @overload
    def components(self) -> Any:
        """BasisExchangeMatroid.components(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 974)

        Return an iterable containing the components of the matroid.

        A *component* is an inclusionwise maximal connected subset of the
        matroid. A subset is *connected* if the matroid resulting from
        deleting the complement of that subset is
        :meth:`connected <sage.matroids.matroid.Matroid.is_connected>`.

        OUTPUT: list of subsets

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: setprint(M.components())
            [{0, 1, 3, 4}, {2, 5}]"""
    @overload
    def dependent_sets(self, longk) -> SetSystem:
        """BasisExchangeMatroid.dependent_sets(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1579)

        Return the dependent sets of fixed size.

        INPUT:

        - ``k`` -- integer

        OUTPUT: iterable containing all dependent sets of size ``k``

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: len(M.nonbases())
            68
            sage: [len(M.dependent_sets(k)) for k in range(M.full_rank() + 1)]
            [0, 0, 0, 0, 9, 68]

        TESTS::

            sage: binomial(M.size(), M.full_rank())-M.bases_count()                     # needs sage.symbolic
            68
            sage: len([B for B in M.nonbases()])
            68"""
    @overload
    def dependent_sets(self, k) -> Any:
        """BasisExchangeMatroid.dependent_sets(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1579)

        Return the dependent sets of fixed size.

        INPUT:

        - ``k`` -- integer

        OUTPUT: iterable containing all dependent sets of size ``k``

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: len(M.nonbases())
            68
            sage: [len(M.dependent_sets(k)) for k in range(M.full_rank() + 1)]
            [0, 0, 0, 0, 9, 68]

        TESTS::

            sage: binomial(M.size(), M.full_rank())-M.bases_count()                     # needs sage.symbolic
            68
            sage: len([B for B in M.nonbases()])
            68"""
    def flats(self, longk) -> SetSystem:
        """BasisExchangeMatroid.flats(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1258)

        Return the collection of flats of the matroid of specified rank.

        A *flat* is a closed set.

        INPUT:

        - ``k`` -- integer

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`Matroid.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.S8()
            sage: M.whitney_numbers2()
            [1, 8, 22, 14, 1]
            sage: len(M.flats(2))
            22
            sage: len(M.flats(8))
            0
            sage: len(M.flats(4))
            1"""
    @overload
    def full_corank(self) -> Any:
        """BasisExchangeMatroid.full_corank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 547)

        Return the corank of the matroid.

        The *corank* of the matroid equals the rank of the dual matroid. It is
        given by ``M.size() - M.full_rank()``.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.full_corank()
            4
            sage: M.dual().full_corank()
            3"""
    @overload
    def full_corank(self) -> Any:
        """BasisExchangeMatroid.full_corank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 547)

        Return the corank of the matroid.

        The *corank* of the matroid equals the rank of the dual matroid. It is
        given by ``M.size() - M.full_rank()``.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.full_corank()
            4
            sage: M.dual().full_corank()
            3"""
    @overload
    def full_corank(self) -> Any:
        """BasisExchangeMatroid.full_corank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 547)

        Return the corank of the matroid.

        The *corank* of the matroid equals the rank of the dual matroid. It is
        given by ``M.size() - M.full_rank()``.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.full_corank()
            4
            sage: M.dual().full_corank()
            3"""
    @overload
    def full_rank(self) -> Any:
        """BasisExchangeMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 528)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.full_rank()
            3
            sage: M.dual().full_rank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """BasisExchangeMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 528)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.full_rank()
            3
            sage: M.dual().full_rank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """BasisExchangeMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 528)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.full_rank()
            3
            sage: M.dual().full_rank()
            4"""
    @overload
    def groundset(self) -> frozenset:
        """BasisExchangeMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 469)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def groundset(self) -> Any:
        """BasisExchangeMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 469)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def groundset_list(self) -> list:
        """BasisExchangeMatroid.groundset_list(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 485)

        Return a list of elements of the groundset of the matroid.

        The order of the list does not change between calls.

        OUTPUT: list

        .. SEEALSO::

            :meth:`M.groundset() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.groundset>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: type(M.groundset())
            <... 'frozenset'>
            sage: type(M.groundset_list())
            <... 'list'>
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']

            sage: E = M.groundset_list()
            sage: E.remove('a')
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def groundset_list(self) -> Any:
        """BasisExchangeMatroid.groundset_list(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 485)

        Return a list of elements of the groundset of the matroid.

        The order of the list does not change between calls.

        OUTPUT: list

        .. SEEALSO::

            :meth:`M.groundset() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.groundset>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: type(M.groundset())
            <... 'frozenset'>
            sage: type(M.groundset_list())
            <... 'list'>
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']

            sage: E = M.groundset_list()
            sage: E.remove('a')
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def groundset_list(self) -> Any:
        """BasisExchangeMatroid.groundset_list(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 485)

        Return a list of elements of the groundset of the matroid.

        The order of the list does not change between calls.

        OUTPUT: list

        .. SEEALSO::

            :meth:`M.groundset() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.groundset>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: type(M.groundset())
            <... 'frozenset'>
            sage: type(M.groundset_list())
            <... 'list'>
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']

            sage: E = M.groundset_list()
            sage: E.remove('a')
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def groundset_list(self) -> Any:
        """BasisExchangeMatroid.groundset_list(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 485)

        Return a list of elements of the groundset of the matroid.

        The order of the list does not change between calls.

        OUTPUT: list

        .. SEEALSO::

            :meth:`M.groundset() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.groundset>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: type(M.groundset())
            <... 'frozenset'>
            sage: type(M.groundset_list())
            <... 'list'>
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']

            sage: E = M.groundset_list()
            sage: E.remove('a')
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def groundset_list(self) -> Any:
        """BasisExchangeMatroid.groundset_list(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 485)

        Return a list of elements of the groundset of the matroid.

        The order of the list does not change between calls.

        OUTPUT: list

        .. SEEALSO::

            :meth:`M.groundset() <sage.matroids.basis_exchange_matroid.BasisExchangeMatroid.groundset>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: type(M.groundset())
            <... 'frozenset'>
            sage: type(M.groundset_list())
            <... 'list'>
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']

            sage: E = M.groundset_list()
            sage: E.remove('a')
            sage: sorted(M.groundset_list())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""
    @overload
    def independent_sets(self, longk=...) -> SetSystem:
        """BasisExchangeMatroid.independent_sets(self, long k=-1) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1497)

        Return the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return the size-`k`
          independent sets of the matroid

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: I = M.independent_sets()
            sage: len(I)
            57
            sage: M = matroids.catalog.N1()
            sage: M.bases_count()
            184
            sage: [len(M.independent_sets(k)) for k in range(M.full_rank() + 1)]
            [1, 10, 45, 120, 201, 184]

        TESTS::

            sage: len([B for B in M.bases()])
            184"""
    @overload
    def independent_sets(self) -> Any:
        """BasisExchangeMatroid.independent_sets(self, long k=-1) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1497)

        Return the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return the size-`k`
          independent sets of the matroid

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: I = M.independent_sets()
            sage: len(I)
            57
            sage: M = matroids.catalog.N1()
            sage: M.bases_count()
            184
            sage: [len(M.independent_sets(k)) for k in range(M.full_rank() + 1)]
            [1, 10, 45, 120, 201, 184]

        TESTS::

            sage: len([B for B in M.bases()])
            184"""
    @overload
    def independent_sets(self, k) -> Any:
        """BasisExchangeMatroid.independent_sets(self, long k=-1) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1497)

        Return the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return the size-`k`
          independent sets of the matroid

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: I = M.independent_sets()
            sage: len(I)
            57
            sage: M = matroids.catalog.N1()
            sage: M.bases_count()
            184
            sage: [len(M.independent_sets(k)) for k in range(M.full_rank() + 1)]
            [1, 10, 45, 120, 201, 184]

        TESTS::

            sage: len([B for B in M.bases()])
            184"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """BasisExchangeMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 2234)

        Test if the data obey the matroid axioms.

        This method checks the basis axioms for the class. If `B` is the set
        of bases of a matroid `M`, then

        * `B` is nonempty
        * if `X` and `Y` are in `B`, and `x` is in `X - Y`, then there is a
          `y` in `Y - X` such that `(X - x) + y` is again a member of `B`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.Fano())
            sage: M.is_valid()
            True
            sage: M = Matroid(groundset='abcd', bases=['ab', 'cd'])
            sage: M.is_valid(certificate=True)
            (False, {'error': 'exchange axiom failed'})

        TESTS:

        Verify that :issue:`20172` was fixed::

            sage: M = Matroid(groundset='1234', bases=['12','13','23','34'])
            sage: M.is_valid()
            False"""
    @overload
    def is_valid(self) -> Any:
        """BasisExchangeMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 2234)

        Test if the data obey the matroid axioms.

        This method checks the basis axioms for the class. If `B` is the set
        of bases of a matroid `M`, then

        * `B` is nonempty
        * if `X` and `Y` are in `B`, and `x` is in `X - Y`, then there is a
          `y` in `Y - X` such that `(X - x) + y` is again a member of `B`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.Fano())
            sage: M.is_valid()
            True
            sage: M = Matroid(groundset='abcd', bases=['ab', 'cd'])
            sage: M.is_valid(certificate=True)
            (False, {'error': 'exchange axiom failed'})

        TESTS:

        Verify that :issue:`20172` was fixed::

            sage: M = Matroid(groundset='1234', bases=['12','13','23','34'])
            sage: M.is_valid()
            False"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """BasisExchangeMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 2234)

        Test if the data obey the matroid axioms.

        This method checks the basis axioms for the class. If `B` is the set
        of bases of a matroid `M`, then

        * `B` is nonempty
        * if `X` and `Y` are in `B`, and `x` is in `X - Y`, then there is a
          `y` in `Y - X` such that `(X - x) + y` is again a member of `B`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.Fano())
            sage: M.is_valid()
            True
            sage: M = Matroid(groundset='abcd', bases=['ab', 'cd'])
            sage: M.is_valid(certificate=True)
            (False, {'error': 'exchange axiom failed'})

        TESTS:

        Verify that :issue:`20172` was fixed::

            sage: M = Matroid(groundset='1234', bases=['12','13','23','34'])
            sage: M.is_valid()
            False"""
    @overload
    def is_valid(self) -> Any:
        """BasisExchangeMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 2234)

        Test if the data obey the matroid axioms.

        This method checks the basis axioms for the class. If `B` is the set
        of bases of a matroid `M`, then

        * `B` is nonempty
        * if `X` and `Y` are in `B`, and `x` is in `X - Y`, then there is a
          `y` in `Y - X` such that `(X - x) + y` is again a member of `B`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.Fano())
            sage: M.is_valid()
            True
            sage: M = Matroid(groundset='abcd', bases=['ab', 'cd'])
            sage: M.is_valid(certificate=True)
            (False, {'error': 'exchange axiom failed'})

        TESTS:

        Verify that :issue:`20172` was fixed::

            sage: M = Matroid(groundset='1234', bases=['12','13','23','34'])
            sage: M.is_valid()
            False"""
    @overload
    def noncospanning_cocircuits(self) -> SetSystem:
        """BasisExchangeMatroid.noncospanning_cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1670)

        Return the noncospanning cocircuits of the matroid.

        A *noncospanning cocircuit* is a cocircuit whose corank is strictly
        smaller than the corank of the matroid.

        OUTPUT: iterable containing all nonspanning circuits

        .. SEEALSO::

            :meth:`Matroid.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`Matroid.corank() <sage.matroids.matroid.Matroid.corank>`

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: len(M.noncospanning_cocircuits())
            23"""
    @overload
    def noncospanning_cocircuits(self) -> Any:
        """BasisExchangeMatroid.noncospanning_cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1670)

        Return the noncospanning cocircuits of the matroid.

        A *noncospanning cocircuit* is a cocircuit whose corank is strictly
        smaller than the corank of the matroid.

        OUTPUT: iterable containing all nonspanning circuits

        .. SEEALSO::

            :meth:`Matroid.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`Matroid.corank() <sage.matroids.matroid.Matroid.corank>`

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: len(M.noncospanning_cocircuits())
            23"""
    @overload
    def nonspanning_circuits(self) -> SetSystem:
        """BasisExchangeMatroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1623)

        Return the nonspanning circuits of the matroid.

        A *nonspanning circuit* is a circuit whose rank is strictly smaller
        than the rank of the matroid.

        OUTPUT: iterable containing all nonspanning circuits

        .. SEEALSO::

            :meth:`Matroid.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`Matroid.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: len(M.nonspanning_circuits())
            23"""
    @overload
    def nonspanning_circuits(self) -> Any:
        """BasisExchangeMatroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1623)

        Return the nonspanning circuits of the matroid.

        A *nonspanning circuit* is a circuit whose rank is strictly smaller
        than the rank of the matroid.

        OUTPUT: iterable containing all nonspanning circuits

        .. SEEALSO::

            :meth:`Matroid.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`Matroid.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: len(M.nonspanning_circuits())
            23"""
    def whitney_numbers2(self) -> list:
        """BasisExchangeMatroid.whitney_numbers2(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 1201)

        Return the Whitney numbers of the second kind of the matroid.

        The Whitney numbers of the second kind are here encoded as a vector
        `(W_0, \\ldots, W_r)`, where `W_i` is the number of flats of rank `i`,
        and `r` is the rank of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: M = matroids.catalog.S8()
            sage: M.whitney_numbers2()
            [1, 8, 22, 14, 1]"""
    def __len__(self) -> Any:
        """BasisExchangeMatroid.__len__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_exchange_matroid.pyx (starting at line 514)

        Return the size of the groundset.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: len(M)
            7
            sage: len(M.groundset())
            7"""
