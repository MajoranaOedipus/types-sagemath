from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SixVertexConfiguration(ClonableArray):
    """
    A configuration in the six vertex model.
    """
    def check(self) -> None:
        """
        Check if ``self`` is a valid 6 vertex configuration.

        EXAMPLES::

            sage: M = SixVertexModel(3, boundary_conditions='ice')
            sage: M[0].check()
        """
    def to_signed_matrix(self):
        """
        Return the signed matrix of ``self``.

        The signed matrix corresponding to a six vertex configuration is
        given by `0` if there is a cross flow, a `1` if the outward arrows
        are vertical and `-1` if the outward arrows are horizontal.

        EXAMPLES::

            sage: M = SixVertexModel(3, boundary_conditions='ice')
            sage: [x.to_signed_matrix() for x in M]                                     # needs sage.modules
            [
            [1 0 0]  [1 0 0]  [ 0  1  0]  [0 1 0]  [0 1 0]  [0 0 1]  [0 0 1]
            [0 1 0]  [0 0 1]  [ 1 -1  1]  [1 0 0]  [0 0 1]  [1 0 0]  [0 1 0]
            [0 0 1], [0 1 0], [ 0  1  0], [0 0 1], [1 0 0], [0 1 0], [1 0 0]
            ]
        """
    def plot(self, color: str = 'sign'):
        """
        Return a plot of ``self``.

        INPUT:

        - ``color`` -- can be any of the following:

          * ``4`` -- use 4 colors: black, red, blue, and green with each
            corresponding to up, right, down, and left respectively
          * ``2`` -- use 2 colors: red for horizontal, blue for vertical arrows
          * ``'sign'`` -- use red for right and down arrows, blue for left
            and up arrows
          * a list of 4 colors for each direction
          * a function which takes a direction and a boolean corresponding
            to the sign

        EXAMPLES::

            sage: M = SixVertexModel(2, boundary_conditions='ice')
            sage: print(M[0].plot().description())                                      # needs sage.plot
            Arrow from (-1.0,0.0) to (0.0,0.0)
            Arrow from (-1.0,1.0) to (0.0,1.0)
            Arrow from (0.0,0.0) to (0.0,-1.0)
            Arrow from (0.0,0.0) to (1.0,0.0)
            Arrow from (0.0,1.0) to (0.0,0.0)
            Arrow from (0.0,1.0) to (0.0,2.0)
            Arrow from (1.0,0.0) to (1.0,-1.0)
            Arrow from (1.0,0.0) to (1.0,1.0)
            Arrow from (1.0,1.0) to (0.0,1.0)
            Arrow from (1.0,1.0) to (1.0,2.0)
            Arrow from (2.0,0.0) to (1.0,0.0)
            Arrow from (2.0,1.0) to (1.0,1.0)
        """
    def energy(self, epsilon):
        """
        Return the energy of the configuration.

        The energy of a configuration `\\nu` is defined as

        .. MATH::

            E(\\nu) = n_0 \\epsilon_0 + n_1 \\epsilon_1 + \\cdots + n_5 \\epsilon_5

        where `n_i` is the number of vertices of type `i` and
        `\\epsilon_i` is the `i`-th energy constant.

        .. NOTE::

            We number our configurations as:

            0. LR
            1. LU
            2. LD
            3. UD
            4. UR
            5. RD

            which differs from :wikipedia:`Ice-type_model`.

        EXAMPLES::

            sage: M = SixVertexModel(3, boundary_conditions='ice')
            sage: nu = M[2]; nu
                ^    ^    ^
                |    |    |
            --> # -> # <- # <--
                ^    |    ^
                |    V    |
            --> # <- # -> # <--
                |    ^    |
                V    |    V
            --> # -> # <- # <--
                |    |    |
                V    V    V
            sage: nu.energy([1,2,1,2,1,2])
            15

        A KDP energy::

            sage: nu.energy([1,1,0,1,0,1])
            7

        A Rys `F` energy::

            sage: nu.energy([0,1,1,0,1,1])
            4

        The zero field assumption::

            sage: nu.energy([1,2,3,1,3,2])
            15
        """

class SixVertexModel(UniqueRepresentation, Parent):
    """
    The six vertex model.

    We model a configuration by indicating which configuration by the
    following six configurations which are determined by the two outgoing
    arrows in the Up, Right, Down, Left directions:

    1. LR::

            |
            V
        <-- # -->
            ^
            |

    2. LU::

            ^
            |
        <-- # <--
            ^
            |

    3. LD::

            |
            V
        <-- # <--
            |
            V

    4. UD::

            ^
            |
        --> # <--
            |
            V

    5. UR::

            ^
            |
        --> # -->
            ^
            |
    6. RD::

            |
            V
        --> # -->
            |
            V

    INPUT:

    - ``n`` -- the number of rows
    - ``m`` -- (optional) the number of columns, if not specified, then
      the number of columns is the number of rows
    - ``boundary_conditions`` -- (optional) a quadruple of tuples whose
      entries are either:

      * ``True`` for an inward arrow,
      * ``False`` for an outward arrow, or
      * ``None`` for no boundary condition.

      There are also the following predefined boundary conditions:

      * ``'ice'`` -- the top and bottom boundary conditions are outward and the
        left and right boundary conditions are inward; this gives the square
        ice model. Also called domain wall boundary conditions.
      * ``'domain wall'`` -- same as ``'ice'``.
      * ``'alternating'`` -- the boundary conditions alternate between inward
        and outward.
      * ``'free'`` -- there are no boundary conditions.

    EXAMPLES:

    Here are the six types of vertices that can be created::

        sage: M = SixVertexModel(1)
        sage: list(M)
        [
            |          ^          |          ^          ^          |
            V          |          V          |          |          V
        <-- # -->  <-- # <--  <-- # <--  --> # <--  --> # -->  --> # -->
            ^          ^          |          |          ^          |
            |    ,     |    ,     V    ,     V    ,     |    ,     V
        ]

    When using the square ice model, it is known that the number of
    configurations is equal to the number of alternating sign matrices::

        sage: M = SixVertexModel(1, boundary_conditions='ice')
        sage: len(M)
        1
        sage: M = SixVertexModel(4, boundary_conditions='ice')
        sage: len(M)
        42
        sage: all(len(SixVertexModel(n, boundary_conditions='ice'))                     # needs sage.modules
        ....:     == AlternatingSignMatrices(n).cardinality() for n in range(1, 7))
        True

    An example with a specified non-standard boundary condition and
    non-rectangular shape::

        sage: M = SixVertexModel(2, 1, [[None], [True,True], [None], [None,None]])
        sage: list(M)
        [
            ^          ^          |          ^
            |          |          V          |
        <-- # <--  <-- # <--  <-- # <--  --> # <--
            ^          ^          |          |
            |          |          V          V
        <-- # <--  --> # <--  <-- # <--  <-- # <--
            ^          |          |          |
            |    ,     V    ,     V    ,     V
        ]

    REFERENCES:

    - :wikipedia:`Vertex_model`
    - :wikipedia:`Ice-type_model`
    """
    @staticmethod
    def __classcall_private__(cls, n, m=None, boundary_conditions=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: M1 = SixVertexModel(1, boundary_conditions=[[False],[True],[False],[True]])
            sage: M2 = SixVertexModel(1, 1, ((False,),(True,),(False,),(True,)))
            sage: M1 is M2
            True
        """
    def __init__(self, n, m, boundary_conditions) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: M = SixVertexModel(2, boundary_conditions='ice')
            sage: TestSuite(M).run()
        """
    Element = SixVertexConfiguration
    def __iter__(self):
        """
        Iterate through ``self``.

        EXAMPLES::

            sage: M = SixVertexModel(2, boundary_conditions='ice')
            sage: list(M)
            [
                ^    ^          ^    ^
                |    |          |    |
            --> # <- # <--  --> # -> # <--
                |    ^          ^    |
                V    |          |    V
            --> # -> # <--  --> # <- # <--
                |    |          |    |
                V    V    ,     V    V
            ]
        """
    def boundary_conditions(self):
        """
        Return the boundary conditions of ``self``.

        EXAMPLES::

            sage: M = SixVertexModel(2, boundary_conditions='ice')
            sage: M.boundary_conditions()
            ((False, False), (True, True), (False, False), (True, True))
        """
    def partition_function(self, beta, epsilon):
        """
        Return the partition function of ``self``.

        The partition function of a 6 vertex model is defined by:

        .. MATH::

            Z = \\sum_{\\nu} e^{-\\beta E(\\nu)}

        where we sum over all configurations and `E` is the energy function.
        The constant `\\beta` is known as the *inverse temperature* and is
        equal to `1 / k_B T` where `k_B` is Boltzmann's constant and `T` is
        the system's temperature.

        INPUT:

        - ``beta`` -- the inverse temperature constant `\\beta`
        - ``epsilon`` -- the energy constants, see
          :meth:`~sage.combinat.six_vertex_model.SixVertexConfiguration.energy()`

        EXAMPLES::

            sage: M = SixVertexModel(3, boundary_conditions='ice')
            sage: M.partition_function(2, [1,2,1,2,1,2])                                # needs sage.symbolic
            e^(-24) + 2*e^(-28) + e^(-30) + 2*e^(-32) + e^(-36)

        REFERENCES:

        :wikipedia:`Partition_function_(statistical_mechanics)`
        """

class SquareIceModel(SixVertexModel):
    """
    The square ice model.

    The square ice model is a 6 vertex model on an `n \\times n` grid with
    the boundary conditions that the top and bottom boundaries are pointing
    outward and the left and right boundaries are pointing inward. These
    boundary conditions are also called domain wall boundary conditions.

    Configurations of the 6 vertex model with domain wall boundary conditions
    are in bijection with alternating sign matrices.
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: M = SixVertexModel(3, boundary_conditions='ice')
            sage: TestSuite(M).run()
        """
    def from_alternating_sign_matrix(self, asm):
        """
        Return a configuration from the alternating sign matrix ``asm``.

        EXAMPLES::

            sage: M = SixVertexModel(3, boundary_conditions='ice')
            sage: asm = AlternatingSignMatrix([[0,1,0],[1,-1,1],[0,1,0]])               # needs sage.modules
            sage: M.from_alternating_sign_matrix(asm)                                   # needs sage.modules
                ^    ^    ^
                |    |    |
            --> # -> # <- # <--
                ^    |    ^
                |    V    |
            --> # <- # -> # <--
                |    ^    |
                V    |    V
            --> # -> # <- # <--
                |    |    |
                V    V    V

        TESTS::

            sage: M = SixVertexModel(5, boundary_conditions='ice')
            sage: ASM = AlternatingSignMatrices(5)                                      # needs sage.modules
            sage: all(M.from_alternating_sign_matrix(x.to_alternating_sign_matrix()) == x           # needs sage.modules
            ....:     for x in M)
            True
            sage: all(M.from_alternating_sign_matrix(x).to_alternating_sign_matrix() == x           # needs sage.modules
            ....:     for x in ASM)
            True
        """
    class Element(SixVertexConfiguration):
        """
        An element in the square ice model.
        """
        def to_alternating_sign_matrix(self):
            """
            Return an alternating sign matrix of ``self``.

            .. SEEALSO::

                :meth:`~sage.combinat.six_vertex_model.SixVertexConfiguration.to_signed_matrix()`

            EXAMPLES::

                sage: M = SixVertexModel(4, boundary_conditions='ice')
                sage: M[6].to_alternating_sign_matrix()                                 # needs sage.modules
                [1 0 0 0]
                [0 0 0 1]
                [0 0 1 0]
                [0 1 0 0]
                sage: M[7].to_alternating_sign_matrix()                                 # needs sage.modules
                [ 0  1  0  0]
                [ 1 -1  1  0]
                [ 0  1 -1  1]
                [ 0  0  1  0]
            """
