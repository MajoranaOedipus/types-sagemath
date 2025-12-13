from sage.misc.flatten import flatten as flatten
from sage.structure.element import Matrix as Matrix
from typing import Any, ClassVar

class HMM_Util:
    """File: /build/sagemath/src/sage/src/sage/stats/hmm/util.pyx (starting at line 22)

        A class used in order to share cdef's methods between different files.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def initial_probs_to_TimeSeries(self, pi, boolnormalize) -> TimeSeries:
        """HMM_Util.initial_probs_to_TimeSeries(self, pi, bool normalize) -> TimeSeries

        File: /build/sagemath/src/sage/src/sage/stats/hmm/util.pyx (starting at line 86)

        This function is used internally by the __init__ methods of
        various Hidden Markov Models.

        INPUT:

        - ``pi`` -- vector, list, or :class:`TimeSeries`
        - ``normalize`` -- if ``True``, replace negative entries by 0 and
          rescale to ensure that the sum of the entries in each row is
          equal to 1.  If the sum of the entries in a row is 0, replace them
          all by `1/N`.

        OUTPUT: a :class:`TimeSeries` of length `N`

        EXAMPLES::

            sage: import sage.stats.hmm.util
            sage: u = sage.stats.hmm.util.HMM_Util()
            sage: u.initial_probs_to_TimeSeries([0.1,0.2,0.9], True)
            [0.0833, 0.1667, 0.7500]
            sage: u.initial_probs_to_TimeSeries([0.1,0.2,0.9], False)
            [0.1000, 0.2000, 0.9000]"""
    def normalize_probability_TimeSeries(self, TimeSeriesT, Py_ssize_ti, Py_ssize_tj) -> Any:
        """HMM_Util.normalize_probability_TimeSeries(self, TimeSeries T, Py_ssize_t i, Py_ssize_t j)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/util.pyx (starting at line 26)

        This function is used internally by the Hidden Markov Models code.

        Replace entries of T[i:j] in place so that they are all
        nonnegative and sum to 1.  Negative entries are replaced by 0 and
        T[i:j] is then rescaled to ensure that the sum of the entries in
        each row is equal to 1.  If all entries are 0, replace them
        by 1/(j-i).

        INPUT:

        - ``T`` -- a :class:`TimeSeries`
        - ``i`` -- nonnegative integer
        - ``j`` -- nonnegative integer

        OUTPUT: ``T`` is modified

        EXAMPLES::

            sage: import sage.stats.hmm.util
            sage: T = stats.TimeSeries([.1, .3, .7, .5])
            sage: u = sage.stats.hmm.util.HMM_Util()
            sage: u.normalize_probability_TimeSeries(T,0,3)
            sage: T
            [0.0909, 0.2727, 0.6364, 0.5000]
            sage: u.normalize_probability_TimeSeries(T,0,4)
            sage: T
            [0.0606, 0.1818, 0.4242, 0.3333]
            sage: abs(T.sum()-1) < 1e-8    # might not exactly equal 1 due to rounding
            True"""
    def state_matrix_to_TimeSeries(self, A, intN, boolnormalize) -> TimeSeries:
        """HMM_Util.state_matrix_to_TimeSeries(self, A, int N, bool normalize) -> TimeSeries

        File: /build/sagemath/src/sage/src/sage/stats/hmm/util.pyx (starting at line 122)

        This function is used internally by the ``__init__`` methods of
        Hidden Markov Models to make a transition matrix from ``A``.

        INPUT:

        - ``A`` -- matrix, list, list of lists, or :class:`TimeSeries`
        - ``N`` -- number of states
        - ``normalize`` -- if ``True``, replace negative entries by 0 and
          rescale to ensure that the sum of the entries in each row is
          equal to 1.  If the sum of the entries in a row is 0, replace them
          all by `1/N`.

        OUTPUT: a :class:`TimeSeries`

        EXAMPLES::

            sage: import sage.stats.hmm.util
            sage: u = sage.stats.hmm.util.HMM_Util()
            sage: u.state_matrix_to_TimeSeries([[.1,.7],[3/7,4/7]], 2, True)
            [0.1250, 0.8750, 0.4286, 0.5714]
            sage: u.state_matrix_to_TimeSeries([[.1,.7],[3/7,4/7]], 2, False)
            [0.1000, 0.7000, 0.4286, 0.5714]"""
