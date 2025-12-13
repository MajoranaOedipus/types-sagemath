from sage.arith.misc import random_prime as random_prime
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

MAX_MODULUS: int

class MultiModularBasis(MultiModularBasis_base):
    """File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 851)

        Class used for storing a MultiModular bases of a fixed length.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class MultiModularBasis_base:
    """MultiModularBasis_base(val, unsigned long l_bound=0x400, unsigned long u_bound=0x8000)

    File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 37)

    This class stores a list of machine-sized prime numbers,
    and can do reduction and Chinese Remainder Theorem lifting
    modulo these primes.

    Lifting implemented via Garner's algorithm, which has the advantage
    that all reductions are word-sized. For each `i`, precompute
    `\\prod_j=1^{i-1} m_j` and `\\prod_j=1^{i-1} m_j^{-1} (mod m_i)`.

    This class can be initialized in two ways, either with a list of prime
    moduli or an upper bound for the product of the prime moduli. The prime
    moduli are generated automatically in the second case.

    EXAMPLES::

        sage: from sage.arith.multi_modular import MultiModularBasis_base
        sage: mm = MultiModularBasis_base([3, 5, 7]); mm
        MultiModularBasis with moduli [3, 5, 7]

        sage: height = 52348798724
        sage: mm = MultiModularBasis_base(height); mm
        MultiModularBasis with moduli [...]
        sage: mm.prod() >= 2*height
        True

    TESTS::

        sage: mm = MultiModularBasis_base((3,5,7)); mm
        MultiModularBasis with moduli [3, 5, 7]
        sage: mm = MultiModularBasis_base(primes(10,20)); mm
        MultiModularBasis with moduli [11, 13, 17, 19]

    There is no overflow if the modulus is below ``MAX_MODULUS``::

        sage: from sage.arith.multi_modular import MAX_MODULUS
        sage: p0 = previous_prime(MAX_MODULUS)
        sage: p1 = previous_prime(p0)
        sage: MultiModularBasis_base([p0, p1]).crt([p0-1, p1-1])
        -1

    If we add another bit to the prime length then there is an
    overflow, as expected::

        sage: p0 = previous_prime(2*MAX_MODULUS)
        sage: p1 = previous_prime(p0)
        sage: MultiModularBasis_base([p0, p1]).crt([p0-1, p1-1])
        Traceback (most recent call last):
        ...
        OverflowError: given modulus 6074000981 is larger than 3037000498"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, val, unsignedlongl_bound=..., unsignedlongu_bound=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 126)

                Initialize a multi-modular basis and perform precomputations.

                INPUT:

                - ``val`` -- as integer
                                determines how many primes are computed
                                (their product will be at least 2*val)
                            as list, tuple or generator
                                a list of prime moduli to start with
                - ``l_bound`` -- integer (default: 2^10); lower bound for the random primes
                - ``u_bound`` -- integer (default: 2^15); upper bound for the random primes

                EXAMPLES::

                    sage: from sage.arith.multi_modular import MultiModularBasis_base
                    sage: mm = MultiModularBasis_base([1009, 10007]); mm
                    MultiModularBasis with moduli [1009, 10007]
                    sage: mm.prod()
                    10097063

                    sage: height = 10097063
                    sage: mm = MultiModularBasis_base(height); mm
                    MultiModularBasis with moduli [...]

                    sage: mm.prod()//height >= 2
                    True

                    sage: mm = MultiModularBasis_base([1000000000000000000000000000057])
                    Traceback (most recent call last):
                    ...
                    OverflowError: given modulus 1000000000000000000000000000057 is larger than 3037000498

                    sage: mm = MultiModularBasis_base(0); mm
                    MultiModularBasis with moduli [...]

                    sage: mm = MultiModularBasis_base([6, 10])
                    Traceback (most recent call last):
                    ...
                    ArithmeticError: The inverse of 6 modulo 10 is not defined.
        """
    def crt(self, b) -> Any:
        """MultiModularBasis_base.crt(self, b)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 638)

        Calculate lift mod `\\prod_{i=0}^{len(b)-1} m_i`.

        In the case that offset > 0,
        z[j] remains unchanged mod `\\prod_{i=0}^{offset-1} m_i`

        INPUT:

        - ``b`` -- list of length at most self.n

        OUTPUT:

            Integer z where `z = b[i] mod m_i` for 0 <= i < len(b)

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([10007, 10009, 10037, 10039, 17351])
            sage: res = mm.crt([3,5,7,9]); res
            8474803647063985
            sage: res % 10007
            3
            sage: res % 10009
            5
            sage: res % 10037
            7
            sage: res % 10039
            9"""
    def extend_with_primes(self, plist, partial_products=..., check=...) -> Any:
        """MultiModularBasis_base.extend_with_primes(self, plist, partial_products=None, check=True)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 203)

        Extend the stored list of moduli with the given primes in ``plist``.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([1009, 10007]); mm
            MultiModularBasis with moduli [1009, 10007]
            sage: mm.extend_with_primes([10037, 10039])
            4
            sage: mm
            MultiModularBasis with moduli [1009, 10007, 10037, 10039]"""
    @overload
    def list(self) -> Any:
        """MultiModularBasis_base.list(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 764)

        Return a list with the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307, 10007])
            sage: mm.list()
            [46307, 10007]"""
    @overload
    def list(self) -> Any:
        """MultiModularBasis_base.list(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 764)

        Return a list with the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307, 10007])
            sage: mm.list()
            [46307, 10007]"""
    def partial_product(self, n) -> Any:
        """MultiModularBasis_base.partial_product(self, n)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 698)

        Return a list containing precomputed partial products.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307, 10007]); mm
            MultiModularBasis with moduli [46307, 10007]
            sage: mm.partial_product(0)
            46307
            sage: mm.partial_product(1)
            463394149

        TESTS::

            sage: mm.partial_product(2)
            Traceback (most recent call last):
            ...
            IndexError: beyond bound for multi-modular prime list
            sage: mm.partial_product(-2)
            Traceback (most recent call last):
            ...
            IndexError: negative index not valid"""
    def precomputation_list(self) -> Any:
        """MultiModularBasis_base.precomputation_list(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 682)

        Return a list of the precomputed coefficients
        `\\prod_j=1^{i-1} m_j^{-1} (mod m_i)`
        where `m_i` are the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307, 10007]); mm
            MultiModularBasis with moduli [46307, 10007]
            sage: mm.precomputation_list()
            [1, 4013]"""
    @overload
    def prod(self) -> Any:
        """MultiModularBasis_base.prod(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 732)

        Return the product of the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307]); mm
            MultiModularBasis with moduli [46307]
            sage: mm.prod()
            46307
            sage: mm = MultiModularBasis_base([46307, 10007]); mm
            MultiModularBasis with moduli [46307, 10007]
            sage: mm.prod()
            463394149

        TESTS::

            sage: mm = MultiModularBasis_base([]); mm
            MultiModularBasis with moduli []
            sage: len(mm)
            0
            sage: mm.prod()
            1"""
    @overload
    def prod(self) -> Any:
        """MultiModularBasis_base.prod(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 732)

        Return the product of the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307]); mm
            MultiModularBasis with moduli [46307]
            sage: mm.prod()
            46307
            sage: mm = MultiModularBasis_base([46307, 10007]); mm
            MultiModularBasis with moduli [46307, 10007]
            sage: mm.prod()
            463394149

        TESTS::

            sage: mm = MultiModularBasis_base([]); mm
            MultiModularBasis with moduli []
            sage: len(mm)
            0
            sage: mm.prod()
            1"""
    @overload
    def prod(self) -> Any:
        """MultiModularBasis_base.prod(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 732)

        Return the product of the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307]); mm
            MultiModularBasis with moduli [46307]
            sage: mm.prod()
            46307
            sage: mm = MultiModularBasis_base([46307, 10007]); mm
            MultiModularBasis with moduli [46307, 10007]
            sage: mm.prod()
            463394149

        TESTS::

            sage: mm = MultiModularBasis_base([]); mm
            MultiModularBasis with moduli []
            sage: len(mm)
            0
            sage: mm.prod()
            1"""
    @overload
    def prod(self) -> Any:
        """MultiModularBasis_base.prod(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 732)

        Return the product of the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([46307]); mm
            MultiModularBasis with moduli [46307]
            sage: mm.prod()
            46307
            sage: mm = MultiModularBasis_base([46307, 10007]); mm
            MultiModularBasis with moduli [46307, 10007]
            sage: mm.prod()
            463394149

        TESTS::

            sage: mm = MultiModularBasis_base([]); mm
            MultiModularBasis with moduli []
            sage: len(mm)
            0
            sage: mm.prod()
            1"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, ix) -> Any:
        """MultiModularBasis_base.__getitem__(self, ix)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 809)

        Return the moduli stored at index `ix` as a Python long.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([10007, 10009])
            sage: mm[1]
            10009
            sage: mm[-1]
            Traceback (most recent call last):
            ...
            IndexError: index out of range

            sage: mm[:1]
            MultiModularBasis with moduli [10007]"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __iter__(self) -> Any:
        """MultiModularBasis_base.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 794)

        Return an iterator over the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([10007, 10009])
            sage: t = iter(mm); t
            <list...iterator object at ...>
            sage: list(mm.__iter__())
            [10007, 10009]"""
    @overload
    def __iter__(self) -> Any:
        """MultiModularBasis_base.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 794)

        Return an iterator over the prime moduli.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([10007, 10009])
            sage: t = iter(mm); t
            <list...iterator object at ...>
            sage: list(mm.__iter__())
            [10007, 10009]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """MultiModularBasis_base.__len__(self)

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 777)

        Return the number of moduli stored.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MultiModularBasis_base
            sage: mm = MultiModularBasis_base([10007])
            sage: len(mm)
            1
            sage: mm._extend_moduli_to_count(2)
            2
            sage: len(mm)
            2"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class MutableMultiModularBasis(MultiModularBasis):
    """File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 917)

        Class used for performing multi-modular methods,
        with the possibility of removing bad primes.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def next_prime(self) -> mod_int:
        """MutableMultiModularBasis.next_prime(self) -> mod_int

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 922)

        Pick a new random prime between the bounds given during the
        initialization of this object, update the precomputed data,
        and return the new prime modulus.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MutableMultiModularBasis
            sage: mm = MutableMultiModularBasis([10007])
            sage: p = mm.next_prime()
            sage: 1024 < p < 32768
            True
            sage: p != 10007
            True
            sage: mm.list() == [10007, p]
            True"""
    @overload
    def next_prime(self) -> Any:
        """MutableMultiModularBasis.next_prime(self) -> mod_int

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 922)

        Pick a new random prime between the bounds given during the
        initialization of this object, update the precomputed data,
        and return the new prime modulus.

        EXAMPLES::

            sage: from sage.arith.multi_modular import MutableMultiModularBasis
            sage: mm = MutableMultiModularBasis([10007])
            sage: p = mm.next_prime()
            sage: 1024 < p < 32768
            True
            sage: p != 10007
            True
            sage: mm.list() == [10007, p]
            True"""
    def replace_prime(self, intix) -> mod_int:
        """MutableMultiModularBasis.replace_prime(self, int ix) -> mod_int

        File: /build/sagemath/src/sage/src/sage/arith/multi_modular.pyx (starting at line 943)

        Replace the prime moduli at the given index with a different one,
        update the precomputed data accordingly, and return the new prime.

        INPUT:

        - ``ix`` -- index into list of moduli

        OUTPUT: the new prime modulus

        EXAMPLES::

            sage: from sage.arith.multi_modular import MutableMultiModularBasis
            sage: mm = MutableMultiModularBasis([10007, 10009, 10037, 10039])
            sage: mm
            MultiModularBasis with moduli [10007, 10009, 10037, 10039]
            sage: prev_prod = mm.prod(); prev_prod
            10092272478850909
            sage: mm.precomputation_list()
            [1, 5004, 6536, 6060]
            sage: mm.partial_product(2)
            1005306552331
            sage: p = mm.replace_prime(1)
            sage: mm.list() == [10007, p, 10037, 10039]
            True
            sage: mm.prod()*10009 == prev_prod*p
            True
            sage: precomputed = mm.precomputation_list()
            sage: precomputed == [prod(Integers(mm[i])(1 / mm[j])
            ....:                      for j in range(i))
            ....:                 for i in range(4)]
            True
            sage: mm.partial_product(2) == prod(mm.list()[:3])
            True"""
