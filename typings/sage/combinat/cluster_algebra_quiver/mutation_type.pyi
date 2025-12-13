from sage.combinat.cluster_algebra_quiver.quiver_mutation_type import QuiverMutationType as QuiverMutationType
from sage.combinat.combination import Combinations as Combinations
from sage.graphs.digraph import DiGraph as DiGraph
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.flatten import flatten as flatten
from typing import Any

def is_mutation_finite(M, nr_of_checks=None) -> tuple[bool, Any]:
    """
    Use a non-deterministic method by random mutations in various
    directions. Can result in a wrong answer.

    .. WARNING::

        This method modifies the input matrix ``M``!

    INPUT:

    - ``nr_of_checks`` -- number of mutations applied (default: ``None``);
      standard is 500*(number of vertices of self)

    ALGORITHM:

    A quiver is mutation infinite if and only if every edge label (a, -b) satisfy a*b > 4.
    Thus, we apply random mutations in random directions

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.mutation_type import is_mutation_finite

        sage: Q = ClusterQuiver(['A', 10])                                               # needs sage.modules
        sage: M = Q.b_matrix()                                                          # needs sage.modules
        sage: is_mutation_finite(M)                                                     # needs sage.modules
        (True, None)

        sage: # needs sage.modules
        sage: Q = ClusterQuiver([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 9)])
        sage: M = Q.b_matrix()
        sage: is_mutation_finite(M)  # random
        (False, [9, 6, 9, 8, 9, 4, 0, 4, 5, 2, 1, 0, 1, 0, 7, 1, 9, 2, 5, 7, 8, 6, 3, 0, 2, 5, 4, 2, 6, 9, 2, 7, 3, 5, 3, 7, 9, 5, 9, 0, 2, 7, 9, 2, 4, 2, 1, 6, 9, 4, 3, 5, 0, 8, 2, 9, 5, 3, 7, 0, 1, 8, 3, 7, 2, 7, 3, 4, 8, 0, 4, 9, 5, 2, 8, 4, 8, 1, 7, 8, 9, 1, 5, 0, 8, 7, 4, 8, 9, 8, 0, 7, 4, 7, 1, 2, 8, 6, 1, 3, 9, 3, 9, 1, 3, 2, 4, 9, 5, 1, 2, 9, 4, 8, 5, 3, 4, 6, 8, 9, 2, 5, 9, 4, 6, 2, 1, 4, 9, 6, 0, 9, 8, 0, 4, 7, 9, 2, 1, 6])

    Check that :issue:`19495` is fixed::

        sage: dg = DiGraph(); dg.add_vertex(0); S = ClusterSeed(dg); S                  # needs sage.modules
        A seed for a cluster algebra of rank 1
        sage: S.is_mutation_finite()                                                    # needs sage.modules
        True
    """
@cached_function
def load_data(n: int, user: bool = True) -> dict:
    """
    Load a dict with keys being tuples representing exceptional
    QuiverMutationTypes, and with values being lists or sets
    containing all mutation equivalent quivers as dig6 data.

    We check

    - the data stored by the user (unless ``user=False`` was given)
    - and the data installed by the optional package ``database_mutation_class``.

    INPUT:

    - ``user`` -- boolean (default: ``True``); whether to look at user
      data. If not, only consider the optional package.

    EXAMPLES::

        sage: from sage.combinat.cluster_algebra_quiver.mutation_type import load_data
        sage: load_data(2) # random - depends on the data the user has stored
        {('G', 2): [('AO', (((0, 1), (1, -3)), )), ('AO', (((0, 1), (3, -1)), ))]}

    TESTS:

    We test data from the ``database_mutation_class`` optional package::

        sage: load_data(2, user=False)      # optional - database_mutation_class
        {('G', 2): [('AO', (((0, 1), (1, -3)), )), ('AO', (((0, 1), (3, -1)), ))]}
        sage: D = load_data(3, user=False)  # optional - database_mutation_class
        sage: sorted(D.items())             # optional - database_mutation_class
        [(('G', 2, -1),
          [('BH?', (((1, 2), (1, -3)), )),
           ('BGO', (((2, 1), (3, -1)), )),
           ('BW?', (((0, 1), (3, -1)), )),
           ('BP?', (((0, 1), (1, -3)), )),
           ('BP_', (((0, 1), (1, -3)), ((2, 0), (3, -1)))),
           ('BP_', (((0, 1), (3, -1)), ((1, 2), (1, -3)), ((2, 0), (2, -2))))]),
         (('G', 2, 1),
          [('BH?', (((1, 2), (3, -1)), )),
           ('BGO', (((2, 1), (1, -3)), )),
           ('BW?', (((0, 1), (1, -3)), )),
           ('BP?', (((0, 1), (3, -1)), )),
           ('BKO', (((1, 0), (3, -1)), ((2, 1), (1, -3)))),
           ('BP_', (((0, 1), (2, -2)), ((1, 2), (1, -3)), ((2, 0), (3, -1))))])]
    """
