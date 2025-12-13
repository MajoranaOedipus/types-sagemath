from _typeshed import Incomplete
from collections.abc import Generator

ROOTNODE: int
LEFT: int
RIGHT: int
UP: int
DOWN: int
COLUMN: int
INDEX: int
COUNT: int

class DLXMatrix:
    def __init__(self, ones, initialsolution=None) -> None:
        """
        Solve the Exact Cover problem by using the Dancing Links algorithm
        described by Knuth.

        Consider a matrix M with entries of 0 and 1, and compute a subset
        of the rows of this matrix which sum to the vector of all 1s.

        The dancing links algorithm works particularly well for sparse
        matrices, so the input is a list of lists of the form: (note the
        1-index!)::

          [
           [1, [i_11,i_12,...,i_1r]]
           ...
           [m,[i_m1,i_m2,...,i_ms]]
          ]

        where M[j][i_jk] = 1.

        The first example below corresponds to the matrix::

           1110
           1010
           0100
           0001

        which is exactly covered by::

           1110
           0001

        and

        ::

           1010
           0100
           0001

        EXAMPLES::

            sage: from sage.combinat.dlx import *
            sage: ones = [[1,[1,2,3]]]
            sage: ones+= [[2,[1,3]]]
            sage: ones+= [[3,[2]]]
            sage: ones+= [[4,[4]]]
            sage: DLXM = DLXMatrix(ones,[4])
            sage: for C in DLXM:
            ....:      print(C)
            [4, 1]
            [4, 2, 3]

        .. NOTE::

            The 0 entry is reserved internally for headers in the
            sparse representation, so rows and columns begin their
            indexing with 1.  Apologies for any heartache this
            causes. Blame the original author, or fix it yourself.
        """
    def __eq__(self, other):
        """
        Return ``True`` if every attribute of ``other`` matches the attribute
        of ``self``.

        INPUT:

        - ``other`` -- a DLX matrix

        EXAMPLES::

            sage: from sage.combinat.dlx import *
            sage: M = DLXMatrix([[1,[1]]])
            sage: M == loads(dumps(M))
            True
        """
    def __iter__(self):
        """
        Return ``self``.

        TESTS::

            sage: from sage.combinat.dlx import *
            sage: M = DLXMatrix([[1,[1]]])
            sage: M.__iter__() is M
            True
        """
    def __next__(self):
        '''
        Search for the first solution we can find, and return it.

        Knuth describes the Dancing Links algorithm recursively, though
        actually implementing it as a recursive algorithm is permissible
        only for highly restricted problems. (for example, the original
        author implemented this for Sudoku, and it works beautifully
        there)

        What follows is an iterative description of DLX::

            stack <- [(NULL)]
            level <- 0
            while level >= 0:
                cur <- stack[level]
                if cur = NULL:
                    if R[h] = h:
                        level <- level - 1
                        yield solution
                    else:
                        cover(best_column)
                        stack[level] = best_column
                else if D[cur] != C[cur]:
                    if cur != C[cur]:
                        delete solution[level]
                        for j in L[cur], L[L[cur]], ... , while j != cur:
                            uncover(C[j])
                    cur <- D[cur]
                    solution[level] <- cur
                    stack[level] <- cur
                    for j in R[cur], R[R[cur]], ... , while j != cur:
                        cover(C[j])
                    level <- level + 1
                    stack[level] <- (NULL)
                else:
                    if C[cur] != cur:
                        delete solution[level]
                        for j in L[cur], L[L[cur]], ... , while j != cur:
                            uncover(C[j])
                    uncover(cur)
                    level <- level - 1

        TESTS::

            sage: from sage.combinat.dlx import *
            sage: M = DLXMatrix([[1,[1,2]],[2,[2,3]],[3,[1,3]]])
            sage: while 1:
            ....:     try:
            ....:         C = next(M)
            ....:     except StopIteration:
            ....:         print("StopIteration")
            ....:         break
            ....:     print(C)
            StopIteration
            sage: M = DLXMatrix([[1,[1,2]],[2,[2,3]],[3,[3]]])
            sage: for C in M:
            ....:       print(C)
            [1, 3]
            sage: M = DLXMatrix([[1,[1]],[2,[2,3]],[3,[2]],[4,[3]]])
            sage: for C in M:
            ....:       print(C)
            [1, 2]
            [1, 3, 4]
        '''
    next = __next__

def AllExactCovers(M) -> Generator[Incomplete]:
    """
    Use A. Ajanki's DLXMatrix class to solve the exact cover
    problem on the matrix M (treated as a dense binary matrix).

    EXAMPLES::

        sage: # needs sage.modules
        sage: M = Matrix([[1,1,0],[1,0,1],[0,1,1]])  # no exact covers
        sage: for cover in AllExactCovers(M):
        ....:     print(cover)
        sage: M = Matrix([[1,1,0],[1,0,1],[0,0,1],[0,1,0]]) # two exact covers
        sage: for cover in AllExactCovers(M):
        ....:     print(cover)
        [(1, 1, 0), (0, 0, 1)]
        [(1, 0, 1), (0, 1, 0)]
    """
def OneExactCover(M):
    """
    Use A. Ajanki's DLXMatrix class to solve the exact cover
    problem on the matrix M (treated as a dense binary matrix).

    EXAMPLES::

        sage: M = Matrix([[1,1,0],[1,0,1],[0,1,1]])  # no exact covers                  # needs sage.modules
        sage: OneExactCover(M)                                                          # needs sage.modules

        sage: M = Matrix([[1,1,0],[1,0,1],[0,0,1],[0,1,0]])  # two exact covers         # needs sage.modules
        sage: OneExactCover(M)                                                          # needs sage.modules
        [(1, 1, 0), (0, 0, 1)]
    """
