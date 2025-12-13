from typing import Any

class DegreeSequences:
    def __init__(self, n) -> Any:
        """DegreeSequences.__init__(self, n)

        File: /build/sagemath/src/sage/src/sage/combinat/degree_sequences.pyx (starting at line 287)

        Degree Sequences.

        An instance of this class represents the degree sequences of graphs on a
        given number `n` of vertices. It can be used to list and count them, as
        well as to test whether a sequence is a degree sequence. For more
        information, please refer to the documentation of the
        :mod:`DegreeSequence<sage.combinat.degree_sequences>` module.

        EXAMPLES::

            sage: DegreeSequences(8)
            Degree sequences on 8 elements
            sage: [3,3,2,2,2,2,2,2] in DegreeSequences(8)
            True

        TESTS:

        :issue:`21824`::

            sage: DegreeSequences(-1)
            Traceback (most recent call last):
            ...
            ValueError: the input parameter must be >= 0"""
    def __contains__(self, seq) -> Any:
        """DegreeSequences.__contains__(self, seq)

        File: /build/sagemath/src/sage/src/sage/combinat/degree_sequences.pyx (starting at line 317)

        Check whether a given integer sequence is the degree sequence
        of a graph on `n` elements.

        EXAMPLES::

            sage: [3,3,2,2,2,2,2,2] in DegreeSequences(8)
            True

        TESTS:

        :issue:`15503`::

            sage: [2,2,2,2,1,1,1] in DegreeSequences(7)
            False

        :issue:`21824`::

            sage: [d for d in DegreeSequences(0)]
            [[]]
            sage: [d for d in DegreeSequences(1)]
            [[0]]
            sage: [d for d in DegreeSequences(3)]
            [[0, 0, 0], [1, 1, 0], [2, 1, 1], [2, 2, 2]]
            sage: [d for d in DegreeSequences(1)]
            [[0]]"""
    def __dealloc__(self) -> Any:
        """DegreeSequences.__dealloc__()

        File: /build/sagemath/src/sage/src/sage/combinat/degree_sequences.pyx (starting at line 410)

        Freeing the memory"""
    def __iter__(self) -> Any:
        """DegreeSequences.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/degree_sequences.pyx (starting at line 395)

        Iterate over all the degree sequences.

        TODO: THIS SHOULD BE UPDATED AS SOON AS THE YIELD KEYWORD APPEARS IN
        CYTHON. See comment in the class' documentation.

        EXAMPLES::

            sage: DS = DegreeSequences(6)
            sage: all(seq in DS for seq in DS)
            True"""
