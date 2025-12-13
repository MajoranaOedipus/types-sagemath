from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.tiling import Polyomino as Polyomino, TilingSolver as TilingSolver
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.structure.sage_object import SageObject as SageObject

pentaminos: Incomplete

def show_pentaminos(box=(5, 8, 2)):
    """
    Show the 17 3-D pentaminos included in the game and the `5 \\times 8
    \\times 2` box where 16 of them must fit.

    INPUT:

    - ``box`` -- tuple of size three (default: ``(5,8,2)``),
      size of the box

    OUTPUT: 3D Graphic object

    EXAMPLES::

        sage: from sage.games.quantumino import show_pentaminos
        sage: show_pentaminos()    # not tested (1s)

    To remove the frame do::

        sage: show_pentaminos().show(frame=False)  # not tested (1s)
    """

class QuantuminoState(SageObject):
    """
    A state of the Quantumino puzzle.

    Used to represent a solution or a partial solution of the Quantumino
    puzzle.

    INPUT:

    - ``pentos`` -- list of 16 3d pentamino representing the (partial)
      solution
    - ``aside`` -- 3d polyomino, the unused 3D pentamino
    - ``box`` -- tuple of size three (default: ``(5,8,2)``),
      size of the box

    EXAMPLES::

        sage: from sage.games.quantumino import pentaminos, QuantuminoState
        sage: p = pentaminos[0]
        sage: q = pentaminos[5]
        sage: r = pentaminos[11]
        sage: S = QuantuminoState([p,q], r)
        sage: S
        Quantumino state where the following pentamino is put aside :
        Polyomino: [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 2, 0)], Color: darkblue

    ::

        sage: from sage.games.quantumino import QuantuminoSolver
        sage: next(QuantuminoSolver(3).solve())      # not tested (1.5s)
        Quantumino state where the following pentamino is put aside :
        Polyomino: [(0, 0, 0), (0, 1, 0), (0, 2, 0), (1, 0, 0), (1, 0, 1)], Color: green
    """
    def __init__(self, pentos, aside, box=(5, 8, 2)) -> None:
        """
        EXAMPLES::

            sage: from sage.games.quantumino import pentaminos, QuantuminoState
            sage: p = pentaminos[0]
            sage: q = pentaminos[5]
            sage: QuantuminoState([p], q)
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 1)], Color: red
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.games.quantumino import pentaminos, QuantuminoState
            sage: p = pentaminos[0]
            sage: q = pentaminos[5]
            sage: r = pentaminos[11]
            sage: S = QuantuminoState([p,q], r)
            sage: for a in S: a
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 1)], Color: red
        """
    def list(self):
        """
        Return the list of 3d polyomino making the solution.

        EXAMPLES::

            sage: from sage.games.quantumino import pentaminos, QuantuminoState
            sage: p = pentaminos[0]
            sage: q = pentaminos[5]
            sage: r = pentaminos[11]
            sage: S = QuantuminoState([p,q], r)
            sage: L = S.list()
            sage: L[0]
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            sage: L[1]
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 1)], Color: red
        """
    def show3d(self, size: float = 0.85):
        """
        Return the solution as a 3D Graphic object.

        OUTPUT: 3D Graphic Object

        EXAMPLES::

            sage: from sage.games.quantumino import QuantuminoSolver
            sage: s = next(QuantuminoSolver(0).solve())    # not tested (1.5s)
            sage: G = s.show3d()                            # not tested (<1s)
            sage: type(G)                                   # not tested
            <class 'sage.plot.plot3d.base.Graphics3dGroup'>

        To remove the frame::

            sage: G.show(frame=False) # not tested

        To see the solution with Tachyon viewer::

            sage: G.show(viewer='tachyon', frame=False) # not tested
        """

class QuantuminoSolver(SageObject):
    """
    Return the Quantumino solver for the given box where one of the
    pentamino is put aside.

    INPUT:

    - ``aside`` -- integer, from 0 to 16, the aside pentamino
    - ``box`` -- tuple of size three (default: ``(5,8,2)``),
      size of the box

    EXAMPLES::

        sage: from sage.games.quantumino import QuantuminoSolver
        sage: QuantuminoSolver(9)
        Quantumino solver for the box (5, 8, 2)
        Aside pentamino number: 9
        sage: QuantuminoSolver(12, box=(5,4,4))
        Quantumino solver for the box (5, 4, 4)
        Aside pentamino number: 12
    """
    def __init__(self, aside, box=(5, 8, 2)) -> None:
        """
        Constructor.

        EXAMPLES::

            sage: from sage.games.quantumino import QuantuminoSolver
            sage: QuantuminoSolver(9)
            Quantumino solver for the box (5, 8, 2)
            Aside pentamino number: 9
        """
    def tiling_solver(self):
        """
        Return the Tiling solver of the Quantumino Game where one of the
        pentamino is put aside.

        EXAMPLES::

            sage: from sage.games.quantumino import QuantuminoSolver
            sage: QuantuminoSolver(0).tiling_solver()
            Tiling solver of 16 pieces into a box of size 80
            Rotation allowed: True
            Reflection allowed: False
            Reusing pieces allowed: False
            sage: QuantuminoSolver(14).tiling_solver()
            Tiling solver of 16 pieces into a box of size 80
            Rotation allowed: True
            Reflection allowed: False
            Reusing pieces allowed: False
            sage: QuantuminoSolver(14, box=(5,4,4)).tiling_solver()
            Tiling solver of 16 pieces into a box of size 80
            Rotation allowed: True
            Reflection allowed: False
            Reusing pieces allowed: False
        """
    def solve(self, partial=None) -> Generator[Incomplete]:
        """
        Return an iterator over the solutions where one of the pentamino is
        put aside.

        INPUT:

        - ``partial`` -- string (default: ``None``), whether to
          include partial (incomplete) solutions. It can be one of the
          following:

          - ``None`` -- include only complete solution
          - ``'common'`` -- common part between two consecutive solutions
          - ``'incremental'`` -- one piece change at a time

        OUTPUT: iterator of :class:`QuantuminoState`

        EXAMPLES:

        Get one solution::

            sage: from sage.games.quantumino import QuantuminoSolver
            sage: s = next(QuantuminoSolver(8).solve())          # long time (9s)
            sage: s                                              # long time (fast)
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 0)], Color: yellow
            sage: s.show3d()                                     # long time (< 1s)
            Graphics3d Object

        The explicit solution::

            sage: for p in s: p                                  # long time (fast)
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...
            Polyomino: [(...), (...), (...), (...), (...)], Color: ...


        Enumerate the solutions::

            sage: it = QuantuminoSolver(0).solve()
            sage: next(it)                                          # not tested
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            sage: next(it)                                          # not tested
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink

        With the partial solutions included, one can see the evolution
        between consecutive solutions (an animation would be better)::

            sage: it = QuantuminoSolver(0).solve(partial='common')
            sage: next(it).show3d()               # not tested (2s)
            sage: next(it).show3d()               # not tested (< 1s)
            sage: next(it).show3d()               # not tested (< 1s)

        Generalizations of the game inside different boxes::

            sage: next(QuantuminoSolver(7, (4,4,5)).solve())       # long time (2s)
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 2, 1), (1, 0, 0)], Color: orange
            sage: next(QuantuminoSolver(7, (2,2,20)).solve())      # long time (1s)
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 2, 1), (1, 0, 0)], Color: orange
            sage: next(QuantuminoSolver(3, (2,2,20)).solve())      # long time (1s)
            Quantumino state where the following pentamino is put aside :
            Polyomino: [(0, 0, 0), (0, 1, 0), (0, 2, 0), (1, 0, 0), (1, 0, 1)], Color: green

        If the volume of the box is not 80, there is no solution::

            sage: next(QuantuminoSolver(7, box=(3,3,9)).solve())
            Traceback (most recent call last):
            ...
            StopIteration

        If the box is too small, there is no solution::

            sage: next(QuantuminoSolver(4, box=(40,2,1)).solve())
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def number_of_solutions(self):
        """
        Return the number of solutions.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.games.quantumino import QuantuminoSolver
            sage: QuantuminoSolver(4, box=(3,2,2)).number_of_solutions()
            0

        This computation takes several days::

            sage: QuantuminoSolver(0).number_of_solutions()                # not tested
            ??? hundreds of millions ???
        """
