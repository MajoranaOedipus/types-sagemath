import sage.matroids.basis_exchange_matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matroids.utilities import cmp_elements_key as cmp_elements_key
from sage.misc.decorators import rename_keyword as rename_keyword
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, Callable, ClassVar, overload

__pyx_capi__: dict

class BasisMatroid(sage.matroids.basis_exchange_matroid.BasisExchangeMatroid):
    """BasisMatroid(M=None, groundset=None, bases=None, nonbases=None, rank=None)

    File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 79)

    Create general matroid, stored as a set of bases.

    INPUT:

    - ``M`` -- matroid (optional)
    - ``groundset`` -- any iterable set (optional)
    - ``bases`` -- set of subsets of the ``groundset`` (optional)
    - ``nonbases`` -- set of subsets of the ``groundset`` (optional)
    - ``rank`` -- natural number (optional)

    EXAMPLES:

    The empty matroid::

        sage: from sage.matroids.advanced import *
        sage: M = BasisMatroid()
        sage: M.groundset()
        frozenset()
        sage: M.full_rank()
        0

    Create a BasisMatroid instance out of any other matroid::

        sage: from sage.matroids.advanced import *
        sage: F = matroids.catalog.Fano()
        sage: M = BasisMatroid(F)
        sage: F.groundset() == M.groundset()
        True
        sage: len(set(F.bases()).difference(M.bases()))
        0

    It is possible to provide either bases or nonbases::

        sage: from sage.matroids.advanced import *
        sage: M1 = BasisMatroid(groundset='abc', bases=['ab', 'ac'] )
        sage: M2 = BasisMatroid(groundset='abc', nonbases=['bc'])
        sage: M1 == M2
        True

    Providing only groundset and rank creates a uniform matroid::

        sage: from sage.matroids.advanced import *
        sage: M1 = BasisMatroid(matroids.Uniform(2, 5))
        sage: M2 = BasisMatroid(groundset=range(5), rank=2)
        sage: M1 == M2
        True

    We do not check if the provided input forms an actual matroid::

        sage: from sage.matroids.advanced import *
        sage: M1 = BasisMatroid(groundset='abcd', bases=['ab', 'cd'])
        sage: M1.full_rank()
        2
        sage: M1.is_valid()
        False"""
    relabel: ClassVar[Callable] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, M=..., groundset=..., bases=..., nonbases=..., rank=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def __init__(self, F) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def __init__(self, groundset=..., bases=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def __init__(self, groundset=..., nonbases=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def __init__(self, groundset=..., rank=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def __init__(self, groundset=..., bases=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 137)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: F = matroids.catalog.Fano()
                    sage: M = BasisMatroid(F)
                    sage: F.groundset() == M.groundset()
                    True
                    sage: len(set(F.bases()).difference(M.bases()))
                    0

                TESTS::

                    sage: F = matroids.catalog.Fano()
                    sage: M = Matroid(bases=F.bases())
                    sage: TestSuite(M).run()
        """
    @overload
    def bases(self) -> SetSystem:
        """BasisMatroid.bases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 568)

        Return the bases of the matroid.

        A *basis* is a maximal independent set.

        OUTPUT: iterable containing all bases of the matroid

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: len(M.bases())
            28"""
    @overload
    def bases(self) -> Any:
        """BasisMatroid.bases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 568)

        Return the bases of the matroid.

        A *basis* is a maximal independent set.

        OUTPUT: iterable containing all bases of the matroid

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: len(M.bases())
            28"""
    @overload
    def bases(self) -> Any:
        """BasisMatroid.bases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 568)

        Return the bases of the matroid.

        A *basis* is a maximal independent set.

        OUTPUT: iterable containing all bases of the matroid

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: len(M.bases())
            28"""
    @overload
    def bases_count(self) -> Any:
        """BasisMatroid.bases_count(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 550)

        Return the number of bases of the matroid.

        OUTPUT: integer

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: M.bases_count()
            28"""
    @overload
    def bases_count(self) -> Any:
        """BasisMatroid.bases_count(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 550)

        Return the number of bases of the matroid.

        OUTPUT: integer

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: M.bases_count()
            28"""
    def dual(self) -> Any:
        """BasisMatroid.dual(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 331)

        Return the dual of the matroid.

        Let `M` be a matroid with groundset `E`. If `B` is the set of bases
        of `M`, then the set `\\{E - b : b \\in B\\}` is the set of bases of
        another matroid, the *dual* of `M`.

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Pappus().bases())
            sage: M.dual()
            Matroid of rank 6 on 9 elements with 75 bases

        ALGORITHM:

        A BasisMatroid on `n` elements and of rank `r` is stored as a
        bitvector of length `\\binom{n}{r}`. The `i`-th bit in this vector
        indicates that the `i`-th `r`-set in the lexicographic enumeration of
        `r`-subsets of the groundset is a basis. Reversing this bitvector
        yields a bitvector that indicates whether the complement of an
        `(n - r)`-set is a basis, i.e. gives the bitvector of the bases of the
        dual."""
    @overload
    def is_distinguished(self, e) -> bool:
        """BasisMatroid.is_distinguished(self, e) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 790)

        Return whether ``e`` is a 'distinguished' element of the groundset.

        The set of distinguished elements is an isomorphism invariant. Each
        matroid has at least one distinguished element. The typical
        application of this method is the execution of an orderly algorithm
        for generating all matroids up to isomorphism in a minor-closed class,
        by successively enumerating the single-element extensions and
        coextensions of the matroids generated so far.

        INPUT:

        - ``e`` -- element of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.extensions() <sage.matroids.matroid.Matroid.extensions>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.N1())
            sage: sorted([e for e in M.groundset() if M.is_distinguished(e)])
            ['c', 'g', 'h', 'j']"""
    @overload
    def is_distinguished(self, e) -> Any:
        """BasisMatroid.is_distinguished(self, e) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 790)

        Return whether ``e`` is a 'distinguished' element of the groundset.

        The set of distinguished elements is an isomorphism invariant. Each
        matroid has at least one distinguished element. The typical
        application of this method is the execution of an orderly algorithm
        for generating all matroids up to isomorphism in a minor-closed class,
        by successively enumerating the single-element extensions and
        coextensions of the matroids generated so far.

        INPUT:

        - ``e`` -- element of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.extensions() <sage.matroids.matroid.Matroid.extensions>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.N1())
            sage: sorted([e for e in M.groundset() if M.is_distinguished(e)])
            ['c', 'g', 'h', 'j']"""
    @overload
    def nonbases(self) -> SetSystem:
        """BasisMatroid.nonbases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 597)

        Return the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        OUTPUT: iterable containing the nonbases of the matroid

        .. SEEALSO::

            :meth:`Matroid.basis() <sage.matroids.matroid.Matroid.basis>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: len(M.nonbases())
            7"""
    @overload
    def nonbases(self) -> Any:
        """BasisMatroid.nonbases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 597)

        Return the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        OUTPUT: iterable containing the nonbases of the matroid

        .. SEEALSO::

            :meth:`Matroid.basis() <sage.matroids.matroid.Matroid.basis>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.Fano().bases())
            sage: M
            Matroid of rank 3 on 7 elements with 28 bases
            sage: len(M.nonbases())
            7"""
    @overload
    def truncation(self) -> Any:
        """BasisMatroid.truncation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 401)

        Return a rank-1 truncation of the matroid.

        Let `M` be a matroid of rank `r`. The *truncation* of `M` is the
        matroid obtained by declaring all subsets of size `r` dependent. It
        can be obtained by adding an element freely to the span of the matroid
        and then contracting that element.

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.N2().bases())
            sage: M.truncation()
            Matroid of rank 5 on 12 elements with 702 bases
            sage: M.whitney_numbers2()
            [1, 12, 66, 190, 258, 99, 1]
            sage: M.truncation().whitney_numbers2()
            [1, 12, 66, 190, 258, 1]"""
    @overload
    def truncation(self) -> Any:
        """BasisMatroid.truncation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 401)

        Return a rank-1 truncation of the matroid.

        Let `M` be a matroid of rank `r`. The *truncation* of `M` is the
        matroid obtained by declaring all subsets of size `r` dependent. It
        can be obtained by adding an element freely to the span of the matroid
        and then contracting that element.

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.N2().bases())
            sage: M.truncation()
            Matroid of rank 5 on 12 elements with 702 bases
            sage: M.whitney_numbers2()
            [1, 12, 66, 190, 258, 99, 1]
            sage: M.truncation().whitney_numbers2()
            [1, 12, 66, 190, 258, 1]"""
    @overload
    def truncation(self) -> Any:
        """BasisMatroid.truncation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 401)

        Return a rank-1 truncation of the matroid.

        Let `M` be a matroid of rank `r`. The *truncation* of `M` is the
        matroid obtained by declaring all subsets of size `r` dependent. It
        can be obtained by adding an element freely to the span of the matroid
        and then contracting that element.

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`

        EXAMPLES::

            sage: M = Matroid(bases=matroids.catalog.N2().bases())
            sage: M.truncation()
            Matroid of rank 5 on 12 elements with 702 bases
            sage: M.whitney_numbers2()
            [1, 12, 66, 190, 258, 99, 1]
            sage: M.truncation().whitney_numbers2()
            [1, 12, 66, 190, 258, 1]"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """BasisMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 1079)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.Fano())
            sage: N = BasisMatroid(matroids.catalog.Fano().dual()).dual()
            sage: O = BasisMatroid(matroids.catalog.NonFano())
            sage: hash(M) == hash(N)
            True
            sage: hash(M) == hash(O)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """BasisMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/basis_matroid.pyx (starting at line 1132)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(E, R, name, BB)`` where
        ``E`` is the groundset of the matroid, ``R`` is the rank, ``name`` is a
        custom name, and ``BB`` is the bitpacked list of bases, as pickled by
        Sage's ``bitset_pickle``.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = BasisMatroid(matroids.catalog.Vamos())
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.rename('Vamos')
            sage: loads(dumps(M))
            Vamos"""
