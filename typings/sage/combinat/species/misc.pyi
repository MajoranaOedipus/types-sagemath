from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod

def change_support(perm, support, change_perm=None):
    """
    Changes the support of a permutation defined on [1, ..., n] to
    support.

    EXAMPLES::

        sage: from sage.combinat.species.misc import change_support
        sage: p = PermutationGroupElement((1,2,3)); p
        (1,2,3)
        sage: change_support(p, [3,4,5])
        (3,4,5)
    """
def accept_size(f):
    '''
    The purpose of this decorator is to change calls like
    species.SetSpecies(size=1) to species.SetSpecies(min=1, max=2).
    This is to make caching species easier and to restrict the number
    of parameters that the lower level code needs to know about.

    EXAMPLES::

        sage: from sage.combinat.species.misc import accept_size
        sage: def f(*args, **kwds):
        ....:       print("{} {}".format(args, sorted(kwds.items())))
        sage: f = accept_size(f)
        sage: f(min=1)
        () [(\'min\', 1)]
        sage: f(size=2)
        () [(\'max\', 3), (\'min\', 2)]
    '''
