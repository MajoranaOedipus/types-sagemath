from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method

class BraidMoveCalculator:
    """
    Helper class to compute braid moves.
    """
    coxeter_matrix: Incomplete
    def __init__(self, coxeter_group) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.braid_move_calculator import BraidMoveCalculator
            sage: W = CoxeterGroup(['C',3])
            sage: B = BraidMoveCalculator(W)
            sage: TestSuite(B).run(skip='_test_pickling')
        """
    def put_in_front(self, k, input_word):
        """
        Return a list of reduced words starting with ``input_word``
        and ending with a reduced word whose first letter  is ``k``.

        There still remains an issue with 0 indices.

        EXAMPLES::

            sage: from sage.combinat.root_system.braid_move_calculator import BraidMoveCalculator
            sage: W = CoxeterGroup(['C',3])
            sage: B = BraidMoveCalculator(W)
            sage: B.put_in_front(2, (3, 2, 3, 1, 2, 3, 1, 2, 1))
            ((3, 2, 3, 1, 2, 3, 1, 2, 1),
             (3, 2, 3, 1, 2, 1, 3, 2, 1),
             (3, 2, 3, 2, 1, 2, 3, 2, 1),
             (2, 3, 2, 3, 1, 2, 3, 2, 1))
            sage: B.put_in_front(1, (3, 2, 3, 1, 2, 3, 1, 2, 1))
            ((3, 2, 3, 1, 2, 3, 1, 2, 1),
             (3, 2, 1, 3, 2, 3, 1, 2, 1),
             (3, 2, 1, 3, 2, 3, 2, 1, 2),
             (3, 2, 1, 2, 3, 2, 3, 1, 2),
             (3, 1, 2, 1, 3, 2, 3, 1, 2),
             (1, 3, 2, 1, 3, 2, 3, 1, 2))
            sage: B.put_in_front(1, (1, 3, 2, 3, 2, 1, 2, 3, 2))
            ((1, 3, 2, 3, 2, 1, 2, 3, 2),)
        """
    @cached_method
    def chain_of_reduced_words(self, start_word, end_word):
        """
        Compute the chain of reduced words from ``stard_word``
        to ``end_word``.

        INPUT:

        - ``start_word``, ``end_word`` -- two reduced expressions
          for the long word

        EXAMPLES::

            sage: from sage.combinat.root_system.braid_move_calculator import BraidMoveCalculator
            sage: W = CoxeterGroup(['A',5])
            sage: B = BraidMoveCalculator(W)
            sage: B.chain_of_reduced_words((1,2,1,3,2,1,4,3,2,1,5,4,3,2,1), # not tested
            ....:                          (5,4,5,3,4,5,2,3,4,5,1,2,3,4,5))
        """
