from sage.arith.misc import binomial as binomial
from sage.combinat.combination import Combinations as Combinations
from sage.combinat.designs.incidence_structures import IncidenceStructure as IncidenceStructure
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.rings.rational import Rational as Rational
from sage.structure.sage_object import SageObject as SageObject

def schonheim(v, k, t):
    """
    Return the Schonheim lower bound for the size of such a covering design.

    INPUT:

    - ``v`` -- integer; size of point set

    - ``k`` -- integer; cardinality of each block

    - ``t`` -- integer; cardinality of sets being covered

    OUTPUT:

    The Schonheim lower bound for such a covering design's size:
    `C(v, k, t) \\leq \\lceil(\\frac{v}{k} \\lceil \\frac{v-1}{k-1} \\cdots
    \\lceil \\frac{v-t+1}{k-t+1} \\rceil \\cdots \\rceil \\rceil`

    EXAMPLES::

        sage: from sage.combinat.designs.covering_design import schonheim
        sage: schonheim(10, 3, 2)
        17
        sage: schonheim(32, 16, 8)
        930
    """
def trivial_covering_design(v, k, t):
    """
    Construct a trivial covering design.

    INPUT:

    - ``v`` -- integer; size of point set

    - ``k`` -- integer; cardinality of each block

    - ``t`` -- integer; cardinality of sets being covered

    OUTPUT:

    A trivial `(v, k, t)` covering design

    EXAMPLES::

        sage: C = trivial_covering_design(8, 3, 1)
        sage: print(C)
        C(8, 3, 1) = 3
        Method: Trivial
        0   1   2
        0   6   7
        3   4   5
        sage: C = trivial_covering_design(5, 3, 2)
        sage: print(C)
        4 <= C(5, 3, 2) <= 10
        Method: Trivial
        0   1   2
        0   1   3
        0   1   4
        0   2   3
        0   2   4
        0   3   4
        1   2   3
        1   2   4
        1   3   4
        2   3   4

    .. NOTE::

        Cases are:

        * `t=0`: This could be empty, but it's a useful convention to have
          one block (which is empty if `k=0`).

        * `t=1` : This contains `\\lceil v/k \\rceil` blocks:
          `[0, ..., k-1], [k, ..., 2k-1], ...`.  The last block wraps around if
          `k` does not divide `v`.

        * anything else: Just use every `k`-subset of `[0, 1,..., v-1]`.
    """

class CoveringDesign(SageObject):
    """
    Covering design.

    INPUT:

    - ``v``, ``k``, ``t`` -- integer parameters of the covering design

    - ``size`` -- integer

    - ``points`` -- list of points (default: `[0, ..., v-1]`)

    - ``blocks``

    - ``low_bd`` -- integer; lower bound for such a design

    - ``method``, ``creator``, ``timestamp`` -- database information
    """
    def __init__(self, v: int = 0, k: int = 0, t: int = 0, size: int = 0, points=None, blocks=None, low_bd: int = 0, method: str = '', creator: str = '', timestamp: str = '') -> None:
        """
        EXAMPLES::

            sage: C = CoveringDesign(5, 4, 3, 4, range(5), [[0, 1, 2, 3],
            ....:     [0, 1, 2, 4], [0, 1, 3, 4], [0, 2, 3, 4]], 4,
            ....:     'Lexicographic Covering')
            sage: print(C)
            C(5, 4, 3) = 4
            Method: Lexicographic Covering
            0   1   2   3
            0   1   2   4
            0   1   3   4
            0   2   3   4
        """
    def is_covering(self):
        """
        Check all `t`-sets are in fact covered by the blocks of ``self``.

        .. NOTE::

            This is very slow and wasteful of memory.

        EXAMPLES::

            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.is_covering()
            True
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6], [2, 3, 6],
            ....:     [2, 4, 6]], 0, 'not a covering')   # last block altered
            sage: C.is_covering()
            False
        """
    def v(self):
        """
        Return `v`, the number of points in the covering design.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.v()
            7
        """
    def k(self):
        """
        Return `k`, the size of blocks of the covering design.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.k()
            3
        """
    def t(self):
        """
        Return `t`, the size of sets which must be covered by the
        blocks of the covering design

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.t()
            2
        """
    def size(self):
        """
        Return the number of blocks in the covering design.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.size()
            7
        """
    def low_bd(self):
        """
        Return a lower bound for the number of blocks a covering
        design with these parameters could have.

        Typically this is the Schonheim bound, but for some parameters
        better bounds have been shown.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.low_bd()
            7
        """
    def method(self):
        """
        Return the method used to create the covering design.

        This field is optional, and is used in a database to give information
        about how coverings were constructed.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: C.method()
            'Projective Plane'
        """
    def creator(self):
        """
        Return the creator of the covering design.

        This field is optional, and is used in a database to give
        attribution for the covering design It can refer to the person
        who submitted it, or who originally gave a construction

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6], [2, 3, 6],
            ....:     [2, 4, 5]],0, 'Projective Plane', 'Gino Fano')
            sage: C.creator()
            'Gino Fano'
        """
    def timestamp(self):
        """
        Return the time that the covering was submitted to the database.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]],0, 'Projective Plane',
            ....:     'Gino Fano', '1892-01-01 00:00:00')
            sage: C.timestamp()  # No exact date known; in Fano's 1892 article
            '1892-01-01 00:00:00'
        """
    def incidence_structure(self):
        """
        Return the incidence structure of this design, without extra parameters.

        EXAMPLES::

            sage: from sage.combinat.designs.covering_design import CoveringDesign
            sage: C = CoveringDesign(7, 3, 2, 7, range(7), [[0, 1, 2],
            ....:     [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6],
            ....:     [2, 3, 6], [2, 4, 5]], 0, 'Projective Plane')
            sage: D = C.incidence_structure()
            sage: D.ground_set()
            [0, 1, 2, 3, 4, 5, 6]
            sage: D.blocks()
            [[0, 1, 2], [0, 3, 4], [0, 5, 6], [1, 3, 5],
            [1, 4, 6], [2, 3, 6], [2, 4, 5]]
        """

def best_known_covering_design_www(v, k, t, verbose: bool = False):
    """
    Return the best known `(v, k, t)` covering design from an online database.

    This uses the La Jolla Covering Repository, a database
    available at `<https://ljcr.dmgordon.org/cover.html>`_

    INPUT:

    - ``v`` -- integer; the size of the point set for the design

    - ``k`` -- integer; the number of points per block

    - ``t`` -- integer; the size of sets covered by the blocks

    - ``verbose`` -- boolean (default: ``False``); print verbose message

    OUTPUT:

    A :class:`CoveringDesign` object representing the ``(v, k, t)``-covering
    design with smallest number of blocks available in the database.

    EXAMPLES::

        sage: from sage.combinat.designs.covering_design import (  # optional - internet
        ....:     best_known_covering_design_www)
        sage: C = best_known_covering_design_www(7, 3, 2)  # optional - internet
        sage: print(C)                                     # optional - internet
        C(7, 3, 2) = 7
        Method: lex covering
        Submitted on: 1996-12-01 00:00:00
        0  1  2
        0  3  4
        0  5  6
        1  3  5
        1  4  6
        2  3  6
        2  4  5

    A :exc:`ValueError` is raised if the ``(v, k, t)`` parameters are not
    found in the database.
    """
