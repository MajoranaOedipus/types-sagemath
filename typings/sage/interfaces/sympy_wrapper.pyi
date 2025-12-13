from sympy.sets.sets import Set

class SageSet(Set):
    """
    Wrapper for a Sage set providing the SymPy Set API.

    Parents in the category :class:`sage.categories.sets_cat.Sets`, unless
    a more specific method is implemented, convert to SymPy by creating
    an instance of this class.

    EXAMPLES::

        sage: F = Family([2, 3, 5, 7]); F
        Family (2, 3, 5, 7)
        sage: sF = F._sympy_(); sF            # indirect doctest
        SageSet(Family (2, 3, 5, 7))
        sage: sF._sage_() is F
        True
        sage: bool(sF)
        True
        sage: len(sF)
        4
        sage: list(sF)
        [2, 3, 5, 7]
        sage: sF.is_finite_set
        True
    """
    def __new__(cls, sage_set):
        """
        Construct a wrapper for a Sage set.

        TESTS::

            sage: from sage.interfaces.sympy_wrapper import SageSet
            sage: F = Set([1, 2]); F
            {1, 2}
            sage: sF = SageSet(F); sF
            SageSet({1, 2})
        """
    @property
    def is_empty(self):
        """
        Return whether the set ``self`` is empty.

        EXAMPLES::

            sage: Empty = Family([])
            sage: sEmpty = Empty._sympy_()
            sage: sEmpty.is_empty
            True
        """
    @property
    def is_finite_set(self):
        '''
        Return whether the set ``self`` is finite.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = WeylGroup(["A",1,1])
            sage: sW = W._sympy_(); sW
            SageSet(Weyl Group of type [\'A\', 1, 1] (as a matrix group acting on the root space))
            sage: sW.is_finite_set
            False
        '''
    @property
    def is_iterable(self):
        '''
        Return whether the set ``self`` is iterable.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = WeylGroup(["A",1,1])
            sage: sW = W._sympy_(); sW
            SageSet(Weyl Group of type [\'A\', 1, 1] (as a matrix group acting on the root space))
            sage: sW.is_iterable
            True
        '''
    def __iter__(self):
        """
        Iterator for the set ``self``.

        EXAMPLES::

            sage: sPrimes = Primes()._sympy_(); sPrimes
            SageSet(Set of all prime numbers: 2, 3, 5, 7, ...)
            sage: iter_sPrimes = iter(sPrimes)
            sage: next(iter_sPrimes), next(iter_sPrimes), next(iter_sPrimes)
            (2, 3, 5)
        """
    def __len__(self) -> int:
        '''
        Return the cardinality of the finite set ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: sB3 = WeylGroup(["B", 3])._sympy_(); sB3
            SageSet(Weyl Group of type [\'B\', 3] (as a matrix group acting on the ambient space))
            sage: len(sB3)
            48
        '''
