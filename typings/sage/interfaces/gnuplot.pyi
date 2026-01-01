r"""
Interface to the Gnuplot interpreter
"""

from sage.structure.sage_object import SageObject as SageObject

class Gnuplot(SageObject):
    """
    Interface to the Gnuplot interpreter.
    """
    def gnuplot(self): ...
    def __call__(self, line): ...
    def plot(self, cmd, file=None, verbose: bool = True, reset: bool = True) -> None:
        """
        Draw the plot described by cmd, and possibly also save to an eps or
        png file.

        INPUT:

        - ``cmd`` -- string

        - ``file`` -- string (default: ``None``); if specified save
          plot to given file, which may be either an eps (default) or png file

        - ``verbose`` -- print some info

        - ``reset`` -- true; reset gnuplot before making graph

        OUTPUT: displays graph

        .. NOTE::

           Note that ``^`` s  are replaced by ``**`` s before being passed to gnuplot.
        """
    def plot3d(self, f, xmin: int = -1, xmax: int = 1, ymin: int = -1, ymax: int = 1, zmin: int = -1, zmax: int = 1, title=None, samples: int = 25, isosamples: int = 20, xlabel: str = 'x', ylabel: str = 'y', interact: bool = True) -> None: ...
    def plot3d_parametric(self, f: str = 'cos(u)*(3 + v*cos(u/2)), sin(u)*(3 + v*cos(u/2)), v*sin(u/2)', range1: str = '[u=-pi:pi]', range2: str = '[v=-0.2:0.2]', samples: int = 50, title=None, interact: bool = True) -> None:
        """
        Draw a parametric 3d surface and rotate it interactively.

        INPUT:

        - ``f`` -- string; a function of two variables, e.g.,
          ``'cos(u)\\*(3 + v\\*cos(u/2)), sin(u)\\*(3 + v\\*cos(u/2)), v\\*sin(u/2)'``

        - ``range1`` -- string; range of values for one
          variable, e.g., ``'[u=-pi:pi]'``

        - ``range2`` -- string; range of values for another
          variable, e.g., ``'[v=-0.2:0.2]'``

        - ``samples`` -- integer; number of sample points to use

        - ``title`` -- string; title of the graph

        EXAMPLES::

            sage: gnuplot.plot3d_parametric('v^2*sin(u), v*cos(u), v*(1-v)')   # optional - gnuplot, not tested (since something pops up)
        """
    def interact(self, cmd) -> None: ...
    def console(self) -> None: ...

gnuplot: Gnuplot

def gnuplot_console() -> None: ...
