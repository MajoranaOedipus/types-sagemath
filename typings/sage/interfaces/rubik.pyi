from . import quit as quit
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.groups.perm_gps.cubegroup import index2singmaster as index2singmaster

optimal_solver_tokens: Incomplete
optimal_solver_format: str

class SingNot:
    '''
    This class is to resolve difference between various Singmaster notation.

    Case is ignored, and the second and third letters may be swapped.

    EXAMPLES::

        sage: from sage.interfaces.rubik import SingNot
        sage: SingNot("acb") == SingNot("ACB")
        True
        sage: SingNot("acb") == SingNot("bca")
        False
    '''
    rep: Incomplete
    canonical: Incomplete
    def __init__(self, s) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

singmaster_list: Incomplete

class OptimalSolver:
    """
    Interface to Michael Reid's optimal Rubik's Cube solver.
    """
    verbose: Incomplete
    def __init__(self, verbose: bool = False, wait: bool = True) -> None: ...
    child: Incomplete
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def ready(self) -> None: ...
    def __call__(self, facets): ...
    def solve(self, facets):
        '''
        The initial startup and precomputation are substantial...

        .. TODO:: Let it keep searching once it found a solution?

        EXAMPLES::

            sage: # optional - rubiks
            sage: from sage.interfaces.rubik import *
            sage: solver = DikSolver()
            sage: solver = OptimalSolver()      # long time (28s on sage.math, 2012)
            Initializing tables...
            Done.
            sage: C = RubiksCube("R U")
            sage: solver.solve(C.facets())
            \'R  U\'
            sage: C = RubiksCube("R U F L B D")
            sage: solver.solve(C.facets())
            \'R  U  F  L  B  D\'
            sage: C = RubiksCube("R2 D2")
            sage: solver.solve(C.facets())
            \'R2 D2\'
        '''
    def format_cube(self, facets): ...

move_map: Incomplete

class CubexSolver:
    def __call__(self, facets): ...
    def solve(self, facets):
        '''
        EXAMPLES::

            sage: # optional - rubiks
            sage: from sage.interfaces.rubik import *
            sage: C = RubiksCube("R U")
            sage: CubexSolver().solve(C.facets())
            \'R U\'
            sage: C = RubiksCube("R U F L B D")
            sage: sol = CubexSolver().solve(C.facets()); sol
            "U\' L\' L\' U L U\' L U D L L D\' L\' D L\' D\' L D L\' U\' L D\' L\' U L\' B\' U\' L\' U B L D L D\' U\' L\' U L B L B\' L\' U L U\' L\' F\' L\' F L\' F L F\' L\' D\' L\' D D L D\' B L B\' L B\' L B F\' L F F B\' L F\' B D\' D\' L D B\' B\' L\' D\' B U\' U\' L\' B\' D\' F\' F\' L D F\'"
            sage: RubiksCube(sol) == C
            True
            sage: C = RubiksCube("R2 F\'")
            sage: CubexSolver().solve(C.facets())
            "R\' R\' F\'"
            sage: C = RubiksCube().scramble()
            sage: sol = CubexSolver().solve(C.facets())
            sage: C == RubiksCube(sol)
            True
        '''
    def format_cube(self, facets): ...

class DikSolver:
    def __call__(self, facets): ...
    def solve(self, facets, timeout: int = 10, extra_time: int = 2):
        '''
        EXAMPLES::

            sage: # optional - rubiks
            sage: from sage.interfaces.rubik import *
            sage: C = RubiksCube().move("R U")
            sage: DikSolver().solve(C.facets())
            \'R U\'
            sage: C = RubiksCube().move("R U F L B D")
            sage: DikSolver().solve(C.facets())
            \'R U F L B D\'
            sage: C = RubiksCube().move("R2 F\'")
            sage: DikSolver().solve(C.facets())
            "R2 F\'"
        '''
    def format_cube(self, facets): ...
    facet_map: Incomplete
    rot_map: Incomplete
