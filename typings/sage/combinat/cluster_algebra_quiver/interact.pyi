from sage.misc.latex import latex as latex
from sage.repl.rich_output.pretty_print import pretty_print as pretty_print

def cluster_interact(self, fig_size: int = 1, circular: bool = True, kind: str = 'seed'):
    """
    Start an interactive window for cluster seed mutations.

    Only in *Jupyter notebook mode*.

    Not to be called directly. Use the :meth:`interact` methods
    of :class:`ClusterSeed` and :class:`ClusterQuiver` instead.

    INPUT:

    - ``fig_size`` -- (default: 1) factor by which the size of the
      plot is multiplied

    - ``circular`` -- boolean (default: ``True``); if ``True``, the circular
      plot is chosen, otherwise >>spring<< is used

    - ``kind`` -- either ``'seed'`` (default) or ``'quiver'``

    TESTS::

        sage: S = ClusterSeed(['A',4])                                                  # needs sage.graphs sage.modules
        sage: S.interact()   # indirect doctest                                         # needs sage.graphs sage.modules sage.symbolic
        ...VBox(children=...
    """
