from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.real_double import RDF as RDF

class SpikeFunction:
    """
    Base class for spike functions.

    INPUT:

    - ``v`` -- list of pairs (x, height)

    - ``eps`` -- parameter that determines approximation to a true spike

    OUTPUT: a function with spikes at each point ``x`` in ``v`` with the given height

    EXAMPLES::

        sage: spike_function([(-3,4), (-1,1), (2,3)], 0.001)
        A spike function with spikes at [-3.0, -1.0, 2.0]

    Putting the spikes too close together may delete some::

        sage: spike_function([(1,1), (1.01,4)], 0.1)
        Some overlapping spikes have been deleted.
        You might want to use a smaller value for eps.
        A spike function with spikes at [1.0]

    Note this should normally be used indirectly via
    ``spike_function``, but one can use it directly::

        sage: from sage.functions.spike_function import SpikeFunction
        sage: S = SpikeFunction([(0,1), (1,2), (pi,-5)]); S                             # needs sage.symbolic
        A spike function with spikes at [0.0, 1.0, 3.141592653589793]
        sage: S.support                                                                 # needs sage.symbolic
        [0.0, 1.0, 3.141592653589793]
    """
    v: Incomplete
    eps: Incomplete
    support: Incomplete
    height: Incomplete
    def __init__(self, v, eps: float = 1e-07) -> None:
        """
        Initialize base class SpikeFunction.

        EXAMPLES::

            sage: S = spike_function([(-3,4), (-1,1), (2,3)], 0.001); S
            A spike function with spikes at [-3.0, -1.0, 2.0]
            sage: S.height
            [4.0, 1.0, 3.0]
            sage: S.eps                                                                 # needs sage.rings.real_mpfr
            0.00100000000000000
        """
    def __call__(self, x):
        """
        Called when spike function is used as callable function.

        EXAMPLES::

            sage: S = spike_function([(0,5)],eps=.001)
            sage: S(0)
            5.0
            sage: S(.1)
            0.0
            sage: S(.01)
            0.0
            sage: S(.001)
            5.0
        """
    def plot_fft_abs(self, samples=..., xmin=None, xmax=None, **kwds):
        """
        Plot of (absolute values of) Fast Fourier Transform of
        the spike function with given number of samples.

        EXAMPLES::

            sage: S = spike_function([(-3,4), (-1,1), (2,3)]); S
            A spike function with spikes at [-3.0, -1.0, 2.0]
            sage: P = S.plot_fft_abs(8)                                                 # needs sage.plot
            sage: p = P[0]; p.ydata  # abs tol 1e-8                                     # needs sage.plot
            [5.0, 5.0, 3.367958691924177, 3.367958691924177, 4.123105625617661,
             4.123105625617661, 4.759921664218055, 4.759921664218055]
        """
    def plot_fft_arg(self, samples=..., xmin=None, xmax=None, **kwds):
        """
        Plot of (absolute values of) Fast Fourier Transform of
        the spike function with given number of samples.

        EXAMPLES::

            sage: S = spike_function([(-3,4), (-1,1), (2,3)]); S
            A spike function with spikes at [-3.0, -1.0, 2.0]
            sage: P = S.plot_fft_arg(8)                                                 # needs sage.plot
            sage: p = P[0]; p.ydata  # abs tol 1e-8                                     # needs sage.plot
            [0.0, 0.0, -0.211524990023434, -0.211524990023434,
             0.244978663126864, 0.244978663126864, -0.149106180027477,
             -0.149106180027477]
        """
    def vector(self, samples=..., xmin=None, xmax=None):
        """
        Create a sampling vector of the spike function in question.

        EXAMPLES::

            sage: S = spike_function([(-3,4), (-1,1), (2,3)],0.001); S
            A spike function with spikes at [-3.0, -1.0, 2.0]
            sage: S.vector(16)                                                          # needs sage.modules
            (4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
             0.0, 0.0, 0.0)
        """
    def plot(self, xmin=None, xmax=None, **kwds):
        """
        Special fast plot method for spike functions.

        EXAMPLES::

            sage: S = spike_function([(-1,1), (1,40)])
            sage: P = plot(S)                                                           # needs sage.plot
            sage: P[0]                                                                  # needs sage.plot
            Line defined by 8 points
        """
spike_function = SpikeFunction
