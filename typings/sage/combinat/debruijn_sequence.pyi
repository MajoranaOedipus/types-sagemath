import _cython_3_2_1
import sage.structure.parent
import sage.structure.unique_representation
from sage.categories.category import ZZ as ZZ
from sage.categories.finite_sets import FiniteSets as FiniteSets
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any

debruijn_sequence: _cython_3_2_1.cython_function_or_method
is_debruijn_sequence: _cython_3_2_1.cython_function_or_method

class DeBruijnSequences(sage.structure.unique_representation.UniqueRepresentation, sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/combinat/debruijn_sequence.pyx (starting at line 195)

        Represent the De Bruijn sequences of given parameters `k` and `n`.

        A De Bruijn sequence of parameters `k` and `n` is defined as the shortest
        cyclic sequence that incorporates all substrings of length `n` a `k`-ary
        alphabet.

        This class can be used to generate the lexicographically smallest De Bruijn
        sequence, to count the number of existing De Bruijn sequences or to test
        whether a given sequence is De Bruijn.

        INPUT:

        - ``k`` -- a natural number to define arity; the letters used are the
          integers `0, \\ldots, k-1`

        - ``n`` -- a natural number that defines the length of the substring

        EXAMPLES:

        Obtaining a De Bruijn sequence::

            sage: seq = DeBruijnSequences(2, 3).an_element()
            sage: seq
            [0, 0, 0, 1, 0, 1, 1, 1]

        Testing whether it is indeed one::

            sage: seq in DeBruijnSequences(2, 3)
            True

        The total number for these parameters::

            sage: DeBruijnSequences(2, 3).cardinality()
            2

        .. NOTE::

           This function only generates one De Bruijn sequence (the smallest
           lexicographically). Support for generating all possible ones may be
           added in the future.

        TESTS:

        Setting ``k`` to 1 will return 0:

        ::

            sage: DeBruijnSequences(1, 3).an_element()
            [0]

        Setting ``n`` to 1 will return the alphabet::

            sage: DeBruijnSequences(3, 1).an_element()
            [0, 1, 2]

        The test suite::

            sage: d = DeBruijnSequences(2, 3)
            sage: TestSuite(d).run()
    """
    def __init__(self, k, n) -> Any:
        """DeBruijnSequences.__init__(self, k, n)

        File: /build/sagemath/src/sage/src/sage/combinat/debruijn_sequence.pyx (starting at line 257)

        Constructor.

        This checks the consistency of the given arguments.

        TESTS:

        Setting ``n`` or ``k`` to anything under 1 will return
        a :exc:`ValueError`::

            sage: DeBruijnSequences(3, 0).an_element()
            Traceback (most recent call last):
            ...
            ValueError: k and n cannot be under 1

        Setting ``n`` or ``k`` to any type except an integer will return a
        :exc:`TypeError`::

            sage: DeBruijnSequences(2.5, 3).an_element()
            Traceback (most recent call last):
            ...
            TypeError: k and n must be integers"""
    def cardinality(self) -> Any:
        """DeBruijnSequences.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/combinat/debruijn_sequence.pyx (starting at line 338)

        Return the number of distinct De Bruijn sequences for the object's
        parameters.

        EXAMPLES::

            sage: DeBruijnSequences(2, 5).cardinality()
            2048

        ALGORITHM:

        The formula for cardinality is `k!^{k^{n-1}}/k^n` [Ros2002]_."""
    def __contains__(self, seq) -> Any:
        """DeBruijnSequences.__contains__(self, seq)

        File: /build/sagemath/src/sage/src/sage/combinat/debruijn_sequence.pyx (starting at line 321)

        Test whether the given sequence is a De Bruijn sequence with
        the current object's parameters.

        INPUT:

        - ``seq`` -- a sequence of integers

        EXAMPLES::

           sage: Sequences =  DeBruijnSequences(2, 3)
           sage: Sequences.an_element() in Sequences
           True"""
