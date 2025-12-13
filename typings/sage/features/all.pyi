from _typeshed import Incomplete
from collections.abc import Generator

def all_features() -> Generator[Incomplete, Incomplete]:
    """
    Return an iterable of all features.

    EXAMPLES::

        sage: from sage.features.all import all_features
        sage: sorted(all_features(), key=lambda f: f.name)  # random
        [...Feature('sage.combinat')...]
    """
def module_feature(module_name):
    """
    Find a top-level :class:`Feature` that provides the Python module of the given ``module_name``.

    Only features known to :func:`all_features` are considered.

    INPUT:

    - ``module_name`` -- string

    OUTPUT: a :class:`Feature` or ``None``

    EXAMPLES::

        sage: from sage.features.all import module_feature
        sage: module_feature('sage.combinat.tableau')                                   # needs sage.combinat
        Feature('sage.combinat')
        sage: module_feature('sage.combinat.posets.poset')                              # needs sage.graphs
        Feature('sage.graphs')
        sage: module_feature('sage.schemes.toric.variety')                              # needs sage.geometry.polyhedron
        Feature('sage.geometry.polyhedron')
        sage: module_feature('scipy')                                                   # needs scipy
        Feature('scipy')
        sage: print(module_feature('sage.structure.element'))
        None
        sage: print(module_feature('sage.does_not_exist'))
        None
    """
def name_feature(name, toplevel=None):
    """
    Find a top-level :class:`Feature` that provides the top-level ``name``.

    Only features known to :func:`all_features` are considered.

    INPUT:

    - ``name`` -- string

    - ``toplevel`` -- a module or other namespace

    OUTPUT: a :class:`Feature` or ``None``

    EXAMPLES::

        sage: from sage.features.all import name_feature
        sage: name_feature('QuadraticField')                                            # needs sage.rings.number_field
        Feature('sage.rings.number_field')
        sage: name_feature('line')                                                      # needs sage.plot
        Feature('sage.plot')
        sage: print(name_feature('ZZ'))
        None
        sage: print(name_feature('does_not_exist'))
        None
    """
