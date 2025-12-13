from sage.interfaces.expect import Expect as Expect
from typing import overload
from weakref import ReferenceType

@overload
def cputime(t: float = 0, subprocesses: bool = False) -> float: ...
@overload
def cputime(t: GlobalCputime, subprocesses: bool) -> GlobalCputime: ...

class GlobalCputime:
    """
    Container for CPU times of subprocesses.

    AUTHOR:

    - Martin Albrecht - (2008-12): initial version

    EXAMPLES:

    Objects of this type are returned if ``subprocesses=True`` is
    passed to :func:`cputime`::

        sage: cputime(subprocesses=True)        # indirect doctest, output random
        0.2347431

    We can use it to keep track of the CPU time spent in Singular for
    example::

        sage: t = cputime(subprocesses=True)
        sage: P = PolynomialRing(QQ,7,'x')
        sage: I = sage.rings.ideal.Katsura(P)                                           # needs sage.libs.singular
        sage: gb = I.groebner_basis()  # calls Singular                                 # needs sage.libs.singular
        sage: cputime(subprocesses=True) - t    # output random
        0.462987

    For further processing we can then convert this container to a
    float::

        sage: t = cputime(subprocesses=True)
        sage: float(t)                          # output somewhat random
        2.1088339999999999

    .. SEEALSO::

      :func:`cputime`
    """
    total: float
    local: float
    interfaces: dict[ReferenceType[Expect], float]
    def __init__(self, t: float) -> None:
        """
        Create a new CPU time object which also keeps track of
        subprocesses.

        EXAMPLES::

            sage: from sage.misc.timing import GlobalCputime
            sage: ct = GlobalCputime(0.0); ct
            0.0...
        """
    def __add__(self, other: GlobalCputime | float) -> GlobalCputime:
        """
        EXAMPLES::

            sage: t = cputime(subprocesses=True)
            sage: P = PolynomialRing(QQ,7,'x')
            sage: I = sage.rings.ideal.Katsura(P)                                       # needs sage.libs.singular
            sage: gb = I.groebner_basis()  # calls Singular                             # needs sage.libs.singular
            sage: cputime(subprocesses=True) + t # output random
            2.798708
        """
    def __sub__(self, other: GlobalCputime | float) -> GlobalCputime:
        """
        EXAMPLES::

            sage: t = cputime(subprocesses=True)
            sage: P = PolynomialRing(QQ,7,'x')
            sage: I = sage.rings.ideal.Katsura(P)                                       # needs sage.libs.singular
            sage: gb = I.groebner_basis()  # calls Singular                             # needs sage.libs.singular
            sage: cputime(subprocesses=True) - t # output random
            0.462987
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: t = cputime(subprocesses=True)
            sage: float(t)                          # output somewhat random
            2.1088339999999999
        """

def walltime(t: float = 0) -> float:
    '''
    Return the wall time in second, or with optional argument ``t``, return
    the wall time since time ``t``. "Wall time" means the time on a wall
    clock, i.e., the actual time.

    INPUT:

    - ``t`` -- (optional) float, time in CPU seconds

    OUTPUT: ``float`` -- time in seconds

    EXAMPLES::

        sage: w = walltime()
        sage: F = factor(2^199-1)                                                       # needs sage.libs.pari
        sage: walltime(w)   # somewhat random
        0.8823847770690918
    '''
