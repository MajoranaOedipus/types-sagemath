import _cython_3_2_1
import sage.stats.hmm.hmm
from sage.misc.flatten import flatten as flatten
from sage.structure.element import Matrix as Matrix
from typing import Any, ClassVar, overload

unpickle_gaussian_hmm_v0: _cython_3_2_1.cython_function_or_method
unpickle_gaussian_hmm_v1: _cython_3_2_1.cython_function_or_method
unpickle_gaussian_mixture_hmm_v1: _cython_3_2_1.cython_function_or_method

class GaussianHiddenMarkovModel(sage.stats.hmm.hmm.HiddenMarkovModel):
    """GaussianHiddenMarkovModel(A, B, pi, bool normalize=True)

    File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 70)

    Gaussian emissions Hidden Markov Model.

    INPUT:

    - ``A`` -- matrix; the `N \\times N` transition matrix
    - ``B`` -- list of pairs ``(mu, sigma)`` that define the distributions
    - ``pi`` -- initial state probabilities
    - ``normalize`` -- boolean (default: ``True``)

    EXAMPLES:

    We illustrate the primary functions with an example 2-state Gaussian HMM::

        sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
        ....:                                   [(1,1), (-1,1)],
        ....:                                   [.5,.5]); m
        Gaussian Hidden Markov Model with 2 States
        Transition matrix:
        [0.1 0.9]
        [0.5 0.5]
        Emission parameters:
        [(1.0, 1.0), (-1.0, 1.0)]
        Initial probabilities: [0.5000, 0.5000]

    We query the defining transition matrix, emission parameters, and
    initial state probabilities::

        sage: m.transition_matrix()
        [0.1 0.9]
        [0.5 0.5]
        sage: m.emission_parameters()
        [(1.0, 1.0), (-1.0, 1.0)]
        sage: m.initial_probabilities()
        [0.5000, 0.5000]

    We obtain a sample sequence with 10 entries in it, and compute the
    logarithm of the probability of obtaining this sequence, given the
    model::

        sage: obs = m.sample(5); obs  # random
        [-1.6835, 0.0635, -2.1688, 0.3043, -0.3188]
        sage: log_likelihood = m.log_likelihood(obs)
        sage: counter = 0
        sage: n = 0
        sage: def add_samples(i):
        ....:     global counter, n
        ....:     for _ in range(i):
        ....:         n += 1
        ....:         obs2 = m.sample(5)
        ....:         if all(abs(obs2[i] - obs[i]) < 0.25 for i in range(5)):
        ....:             counter += 1

        sage: add_samples(10000)
        sage: while abs(log_likelihood - log(counter*1.0/n/0.5^5)) < 0.1:
        ....:     add_samples(10000)

    We compute the Viterbi path, and probability that the given path
    of states produced obs::

        sage: m.viterbi(obs)  # random
        ([1, 0, 1, 0, 1], -8.714092684611794)

    We use the Baum-Welch iterative algorithm to find another model
    for which our observation sequence is more likely::

        sage: try:
        ....:     p, s = m.baum_welch(obs)
        ....:     assert p > log_likelihood
        ....:     assert (1 <= s <= 500)
        ....: except RuntimeError:
        ....:     pass

    Notice that running Baum-Welch changed our model::

        sage: m  # random
        Gaussian Hidden Markov Model with 2 States
        Transition matrix:
        [   0.4154981366185841     0.584501863381416]
        [   0.9999993174253741 6.825746258991804e-07]
        Emission parameters:
        [(0.4178882427119503, 0.5173109664360919),
         (-1.5025208631331122, 0.5085512836055119)]
        Initial probabilities: [0.0000, 1.0000]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, A, B, pi, boolnormalize=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 159)

                Create a Gaussian emissions HMM with transition probability
                matrix `A`, normal emissions given by `B`, and initial state
                probability distribution ``pi``.

                INPUT:

                - ``A`` -- list of lists or a square `N \\times N` matrix, whose
                  `(i,j)` entry gives the probability of transitioning from
                  state `i` to state `j`.

                - ``B`` -- list of `N` pairs ``(mu, std)``, where if ``B[i]=(mu,std)``,
                  then the probability distribution associated with state `i`
                  normal with mean ``mu`` and standard deviation ``std``.

                - ``pi`` -- the probabilities of starting in each initial
                  state, i.e., ``pi[i]`` is the probability of starting in
                  state `i`.

                - ``normalize`` -- boolean (default: ``True``); if given, input is
                  normalized to define valid probability distributions,
                  e.g., the entries of `A` are made nonnegative and the rows
                  sum to 1.

                EXAMPLES::

                    sage: hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]], [(1,1), (-1,1)], [.5,.5])
                    Gaussian Hidden Markov Model with 2 States
                    Transition matrix:
                    [0.1 0.9]
                    [0.5 0.5]
                    Emission parameters:
                    [(1.0, 1.0), (-1.0, 1.0)]
                    Initial probabilities: [0.5000, 0.5000]

                We input a model in which both `A` and ``pi`` have to be
                renormalized to define valid probability distributions::

                    sage: hmm.GaussianHiddenMarkovModel([[-1,.7],[.3,.4]], [(1,1), (-1,1)], [-1,.3])  # rel tol 3e-14
                    Gaussian Hidden Markov Model with 2 States
                    Transition matrix:
                    [                0.0                 1.0]
                    [0.42857142857142855  0.5714285714285714]
                    Emission parameters:
                    [(1.0, 1.0), (-1.0, 1.0)]
                    Initial probabilities: [0.0000, 1.0000]

                Bad things can happen::

                    sage: hmm.GaussianHiddenMarkovModel([[-1,.7],[.3,.4]], [(1,1), (-1,1)], [-1,.3],
                    ....:                               normalize=False)
                    Gaussian Hidden Markov Model with 2 States
                    Transition matrix:
                    [-1.0  0.7]
                    [ 0.3  0.4]
                    ...
        """
    @overload
    def baum_welch(self, obs, intmax_iter=..., doublelog_likelihood_cutoff=..., doublemin_sd=..., boolfix_emissions=..., boolv=...) -> Any:
        """GaussianHiddenMarkovModel.baum_welch(self, obs, int max_iter=500, double log_likelihood_cutoff=1e-4, double min_sd=0.01, bool fix_emissions=False, bool v=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 852)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions

        - ``max_iter`` -- integer (default: 500); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.log_likelihood([-2,-1,.1,0.1])
            -8.858282215986275
            sage: m.baum_welch([-2,-1,.1,0.1])
            (4.534646052182..., 7)
            sage: m.log_likelihood([-2,-1,.1,0.1])
            4.534646052182...
            sage: m  # rel tol 3e-14
            Gaussian Hidden Markov Model with 2 States
            Transition matrix:
            [   0.9999999992430161 7.569839394440382e-10]
            [  0.49998462791192644    0.5000153720880736]
            Emission parameters:
            [(0.09999999999999999, 0.01), (-1.4999508147591902, 0.5000710504895474)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the ``min_sd`` was the default of 0.01::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.baum_welch([-2,-1,.1,0.1], min_sd=1)
            (-4.07939572755..., 32)
            sage: m.emission_parameters()
            [(-0.2663018798..., 1.0), (-1.99850979..., 1.0)]

        We watch the log likelihoods of the model converge, step by step::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: v = m.sample(10)
            sage: l = stats.TimeSeries([m.baum_welch(v, max_iter=1)[0]
            ....:                       for _ in range(len(v))])
            sage: all(l[i] <= l[i+1] + 0.0001 for i in range(9))
            True
            sage: l  # random
            [-20.1167, -17.7611, -16.9814, -16.9364, -16.9314,
             -16.9309, -16.9309, -16.9309, -16.9309, -16.9309]

        We illustrate fixing emissions::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-164.72944548204..., 23)
            sage: m.emission_parameters()
            [(1.0, 2.0), (-1.0, 0.5)]
            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: m.baum_welch(v)
            (-162.854370397998..., 49)
            sage: m.emission_parameters()  # rel tol 3e-14
            [(1.2722419172602375, 2.371368751761901),
             (-0.9486174675179113, 0.5762360385123765)]"""
    @overload
    def baum_welch(self, v, max_iter=...) -> Any:
        """GaussianHiddenMarkovModel.baum_welch(self, obs, int max_iter=500, double log_likelihood_cutoff=1e-4, double min_sd=0.01, bool fix_emissions=False, bool v=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 852)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions

        - ``max_iter`` -- integer (default: 500); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.log_likelihood([-2,-1,.1,0.1])
            -8.858282215986275
            sage: m.baum_welch([-2,-1,.1,0.1])
            (4.534646052182..., 7)
            sage: m.log_likelihood([-2,-1,.1,0.1])
            4.534646052182...
            sage: m  # rel tol 3e-14
            Gaussian Hidden Markov Model with 2 States
            Transition matrix:
            [   0.9999999992430161 7.569839394440382e-10]
            [  0.49998462791192644    0.5000153720880736]
            Emission parameters:
            [(0.09999999999999999, 0.01), (-1.4999508147591902, 0.5000710504895474)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the ``min_sd`` was the default of 0.01::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.baum_welch([-2,-1,.1,0.1], min_sd=1)
            (-4.07939572755..., 32)
            sage: m.emission_parameters()
            [(-0.2663018798..., 1.0), (-1.99850979..., 1.0)]

        We watch the log likelihoods of the model converge, step by step::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: v = m.sample(10)
            sage: l = stats.TimeSeries([m.baum_welch(v, max_iter=1)[0]
            ....:                       for _ in range(len(v))])
            sage: all(l[i] <= l[i+1] + 0.0001 for i in range(9))
            True
            sage: l  # random
            [-20.1167, -17.7611, -16.9814, -16.9364, -16.9314,
             -16.9309, -16.9309, -16.9309, -16.9309, -16.9309]

        We illustrate fixing emissions::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-164.72944548204..., 23)
            sage: m.emission_parameters()
            [(1.0, 2.0), (-1.0, 0.5)]
            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: m.baum_welch(v)
            (-162.854370397998..., 49)
            sage: m.emission_parameters()  # rel tol 3e-14
            [(1.2722419172602375, 2.371368751761901),
             (-0.9486174675179113, 0.5762360385123765)]"""
    @overload
    def baum_welch(self, v, fix_emissions=...) -> Any:
        """GaussianHiddenMarkovModel.baum_welch(self, obs, int max_iter=500, double log_likelihood_cutoff=1e-4, double min_sd=0.01, bool fix_emissions=False, bool v=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 852)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions

        - ``max_iter`` -- integer (default: 500); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.log_likelihood([-2,-1,.1,0.1])
            -8.858282215986275
            sage: m.baum_welch([-2,-1,.1,0.1])
            (4.534646052182..., 7)
            sage: m.log_likelihood([-2,-1,.1,0.1])
            4.534646052182...
            sage: m  # rel tol 3e-14
            Gaussian Hidden Markov Model with 2 States
            Transition matrix:
            [   0.9999999992430161 7.569839394440382e-10]
            [  0.49998462791192644    0.5000153720880736]
            Emission parameters:
            [(0.09999999999999999, 0.01), (-1.4999508147591902, 0.5000710504895474)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the ``min_sd`` was the default of 0.01::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.baum_welch([-2,-1,.1,0.1], min_sd=1)
            (-4.07939572755..., 32)
            sage: m.emission_parameters()
            [(-0.2663018798..., 1.0), (-1.99850979..., 1.0)]

        We watch the log likelihoods of the model converge, step by step::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: v = m.sample(10)
            sage: l = stats.TimeSeries([m.baum_welch(v, max_iter=1)[0]
            ....:                       for _ in range(len(v))])
            sage: all(l[i] <= l[i+1] + 0.0001 for i in range(9))
            True
            sage: l  # random
            [-20.1167, -17.7611, -16.9814, -16.9364, -16.9314,
             -16.9309, -16.9309, -16.9309, -16.9309, -16.9309]

        We illustrate fixing emissions::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-164.72944548204..., 23)
            sage: m.emission_parameters()
            [(1.0, 2.0), (-1.0, 0.5)]
            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: m.baum_welch(v)
            (-162.854370397998..., 49)
            sage: m.emission_parameters()  # rel tol 3e-14
            [(1.2722419172602375, 2.371368751761901),
             (-0.9486174675179113, 0.5762360385123765)]"""
    @overload
    def baum_welch(self, v) -> Any:
        """GaussianHiddenMarkovModel.baum_welch(self, obs, int max_iter=500, double log_likelihood_cutoff=1e-4, double min_sd=0.01, bool fix_emissions=False, bool v=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 852)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions

        - ``max_iter`` -- integer (default: 500); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.log_likelihood([-2,-1,.1,0.1])
            -8.858282215986275
            sage: m.baum_welch([-2,-1,.1,0.1])
            (4.534646052182..., 7)
            sage: m.log_likelihood([-2,-1,.1,0.1])
            4.534646052182...
            sage: m  # rel tol 3e-14
            Gaussian Hidden Markov Model with 2 States
            Transition matrix:
            [   0.9999999992430161 7.569839394440382e-10]
            [  0.49998462791192644    0.5000153720880736]
            Emission parameters:
            [(0.09999999999999999, 0.01), (-1.4999508147591902, 0.5000710504895474)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the ``min_sd`` was the default of 0.01::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.baum_welch([-2,-1,.1,0.1], min_sd=1)
            (-4.07939572755..., 32)
            sage: m.emission_parameters()
            [(-0.2663018798..., 1.0), (-1.99850979..., 1.0)]

        We watch the log likelihoods of the model converge, step by step::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: v = m.sample(10)
            sage: l = stats.TimeSeries([m.baum_welch(v, max_iter=1)[0]
            ....:                       for _ in range(len(v))])
            sage: all(l[i] <= l[i+1] + 0.0001 for i in range(9))
            True
            sage: l  # random
            [-20.1167, -17.7611, -16.9814, -16.9364, -16.9314,
             -16.9309, -16.9309, -16.9309, -16.9309, -16.9309]

        We illustrate fixing emissions::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-164.72944548204..., 23)
            sage: m.emission_parameters()
            [(1.0, 2.0), (-1.0, 0.5)]
            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.9,.1]],
            ....:                                   [(1,2),(-1,.5)],
            ....:                                   [.3,.7])
            sage: m.baum_welch(v)
            (-162.854370397998..., 49)
            sage: m.emission_parameters()  # rel tol 3e-14
            [(1.2722419172602375, 2.371368751761901),
             (-0.9486174675179113, 0.5762360385123765)]"""
    @overload
    def emission_parameters(self) -> Any:
        """GaussianHiddenMarkovModel.emission_parameters(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 301)

        Return the parameters that define the normal distributions
        associated to all of the states.

        OUTPUT:

        a list ``B`` of pairs ``B[i] = (mu, std)``, such that the
        distribution associated to state `i` is normal with mean
        ``mu`` and standard deviation ``std``.

        EXAMPLES::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: M.emission_parameters()
            [(1.0, 0.5), (-1.0, 3.0)]"""
    @overload
    def emission_parameters(self) -> Any:
        """GaussianHiddenMarkovModel.emission_parameters(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 301)

        Return the parameters that define the normal distributions
        associated to all of the states.

        OUTPUT:

        a list ``B`` of pairs ``B[i] = (mu, std)``, such that the
        distribution associated to state `i` is normal with mean
        ``mu`` and standard deviation ``std``.

        EXAMPLES::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: M.emission_parameters()
            [(1.0, 0.5), (-1.0, 3.0)]"""
    def generate_sequence(self, Py_ssize_tlength, starting_state=...) -> Any:
        """GaussianHiddenMarkovModel.generate_sequence(self, Py_ssize_t length, starting_state=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 339)

        Return a sample of the given length from this HMM.

        INPUT:

        - ``length`` -- positive integer
        - ``starting_state`` -- integer (or ``None``); if specified then
          generate a sequence using this model starting with the given state
          instead of the initial probabilities to determine the
          starting state.

        OUTPUT:

        - an :class:`IntList` or list of emission symbols
        - :class:`TimeSeries` of emissions

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.generate_sequence(5)  # random
            ([-3.0505, 0.5317, -4.5065, 0.6521, 1.0435], [1, 0, 1, 0, 1])
            sage: m.generate_sequence(0)
            ([], [])
            sage: m.generate_sequence(-1)
            Traceback (most recent call last):
            ...
            ValueError: length must be nonnegative

        Verify numerically that the starting state is 0 with probability about 0.1::

            sage: counter = 0
            sage: n = 0
            sage: def add_samples(i):
            ....:     global counter, n
            ....:     for i in range(i):
            ....:         n += 1
            ....:         if m.generate_sequence(1)[1][0] == 0:
            ....:             counter += 1

            sage: add_samples(10^5)
            sage: while abs(counter*1.0 / n - 0.1) > 0.01: add_samples(10^5)

        Example in which the starting state is 0 (see :issue:`11452`)::

            sage: set_random_seed(23);  m.generate_sequence(2)
            ([0.6501, -2.0151], [0, 1])

        Force a starting state of 1 even though as we saw above it would be 0::

            sage: set_random_seed(23);  m.generate_sequence(2, starting_state=1)
            ([-3.1491, -1.0244], [1, 1])"""
    @overload
    def log_likelihood(self, obs) -> Any:
        '''GaussianHiddenMarkovModel.log_likelihood(self, obs)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 524)

        Return the logarithm of a continuous analogue of the
        probability that this model produced the given observation
        sequence.

        Note that the "continuous analogue of the probability" above can
        be bigger than 1, hence the logarithm can be positive.

        INPUT:

        - ``obs`` -- sequence of observations

        OUTPUT: float

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.log_likelihood([1,1,1])
            -4.297880766072486
            sage: s = m.sample(20)
            sage: -80 < m.log_likelihood(s) < -20
            True'''
    @overload
    def log_likelihood(self, s) -> Any:
        '''GaussianHiddenMarkovModel.log_likelihood(self, obs)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 524)

        Return the logarithm of a continuous analogue of the
        probability that this model produced the given observation
        sequence.

        Note that the "continuous analogue of the probability" above can
        be bigger than 1, hence the logarithm can be positive.

        INPUT:

        - ``obs`` -- sequence of observations

        OUTPUT: float

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.log_likelihood([1,1,1])
            -4.297880766072486
            sage: s = m.sample(20)
            sage: -80 < m.log_likelihood(s) < -20
            True'''
    def viterbi(self, obs) -> Any:
        '''GaussianHiddenMarkovModel.viterbi(self, obs)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 612)

        Determine "the" hidden sequence of states that is most likely
        to produce the given sequence ``obs`` of observations, along with
        the probability that this hidden sequence actually produced
        the observation.

        INPUT:

        - ``obs`` -- sequence of emitted ints or symbols

        OUTPUT:

        - ``list`` -- "the" most probable sequence of hidden states, i.e.,
          the Viterbi path

        - ``float`` -- log of probability that the observed sequence
          was produced by the Viterbi sequence of states

        EXAMPLES:

        We find the optimal state sequence for a given model::

            sage: m = hmm.GaussianHiddenMarkovModel([[0.5,0.5],[0.5,0.5]],
            ....:                                   [(0,1),(10,1)],
            ....:                                   [0.5,0.5])
            sage: m.viterbi([0,1,10,10,1])
            ([0, 0, 1, 1, 0], -9.0604285688230...)

        Another example in which the most likely states change based
        on the last observation::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,.5), (-1,3)],
            ....:                                   [.1,.9])
            sage: m.viterbi([-2,-1,.1,0.1])
            ([1, 1, 0, 1], -9.61823698847639...)
            sage: m.viterbi([-2,-1,.1,0.3])
            ([1, 1, 1, 0], -9.566023653378513)'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, Py_ssize_ti) -> Any:
        """GaussianHiddenMarkovModel.__getitem__(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 252)

        Return the mean and standard distribution for the `i`-th state.

        INPUT:

        - ``i`` -- integer

        OUTPUT: 2 floats

        EXAMPLES::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]], [(1,.5), (-2,.3)], [.5,.5])
            sage: m[0]
            (1.0, 0.5)
            sage: m[1]
            (-2.0, 0.3)
            sage: m[-1]
            (-2.0, 0.3)
            sage: m[3]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: m[-3]
            Traceback (most recent call last):
            ...
            IndexError: index out of range"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """GaussianHiddenMarkovModel.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 288)

        Used in pickling.

        EXAMPLES::

            sage: G = hmm.GaussianHiddenMarkovModel([[1]], [(0,1)], [1])
            sage: loads(dumps(G)) == G
            True"""

class GaussianMixtureHiddenMarkovModel(GaussianHiddenMarkovModel):
    """GaussianMixtureHiddenMarkovModel(A, B, pi=None, bool normalize=True)

    File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1044)

    Gaussian mixture Hidden Markov Model.

    INPUT:

    - ``A`` -- matrix; the `N \\times N` transition matrix

    - ``B`` -- list of mixture definitions for each state.  Each
      state may have a varying number of gaussians with selection
      probabilities that sum to 1 and encoded as ``(p, (mu,sigma))``

    - ``pi`` -- initial state probabilities

    - ``normalize`` -- boolean (default: ``True``); if given, input is
      normalized to define valid probability distributions,
      e.g., the entries of `A` are made nonnegative and the rows
      sum to 1, and the probabilities in ``pi`` are normalized.

    EXAMPLES::

        sage: A = [[0.5,0.5],[0.5,0.5]]
        sage: B = [[(0.9,(0.0,1.0)), (0.1,(1,10000))],[(1,(1,1)), (0,(0,0.1))]]
        sage: hmm.GaussianMixtureHiddenMarkovModel(A, B, [1,0])
        Gaussian Mixture Hidden Markov Model with 2 States
        Transition matrix:
        [0.5 0.5]
        [0.5 0.5]
        Emission parameters:
        [0.9*N(0.0,1.0) + 0.1*N(1.0,10000.0), 1.0*N(1.0,1.0) + 0.0*N(0.0,0.1)]
        Initial probabilities: [1.0000, 0.0000]

    TESTS:

    If a standard deviation is 0, it is normalized to be slightly bigger than 0.::

        sage: hmm.GaussianMixtureHiddenMarkovModel([[1]], [[(1,(0,0))]], [1])
        Gaussian Mixture Hidden Markov Model with 1 States
        Transition matrix:
        [1.0]
        Emission parameters:
        [1.0*N(0.0,1e-08)]
        Initial probabilities: [1.0000]

    We test that number of emission distributions must be the same as the number of states::

        sage: hmm.GaussianMixtureHiddenMarkovModel([[1]], [], [1])
        Traceback (most recent call last):
        ...
        ValueError: number of GaussianMixtures must be the same as number of entries of pi

        sage: hmm.GaussianMixtureHiddenMarkovModel([[1]], [[]], [1])
        Traceback (most recent call last):
        ...
        ValueError: must specify at least one component of the mixture model

    We test that the number of initial probabilities must equal the number of states::

        sage: hmm.GaussianMixtureHiddenMarkovModel([[1]], [[]], [1,2])
        Traceback (most recent call last):
        ...
        ValueError: number of entries of transition matrix A must be the square of the number of entries of pi"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, A, B, pi=..., boolnormalize=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1110)

                Initialize a Gaussian mixture hidden Markov model.

                EXAMPLES::

                    sage: hmm.GaussianMixtureHiddenMarkovModel([[.9,.1],[.4,.6]], [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]], [.7,.3])
                    Gaussian Mixture Hidden Markov Model with 2 States
                    Transition matrix:
                    [0.9 0.1]
                    [0.4 0.6]
                    Emission parameters:
                    [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1), 1.0*N(0.0,1.0)]
                    Initial probabilities: [0.7000, 0.3000]
        """
    @overload
    def baum_welch(self, obs, intmax_iter=..., doublelog_likelihood_cutoff=..., doublemin_sd=..., boolfix_emissions=...) -> Any:
        """GaussianMixtureHiddenMarkovModel.baum_welch(self, obs, int max_iter=1000, double log_likelihood_cutoff=1e-12, double min_sd=0.01, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1340)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions
        - ``max_iter`` -- integer (default: 1000); maximum number
          of Baum-Welch steps to take
        - ``log_likelihood_cutoff`` -- positive float (default: 1e-12);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.
        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.
        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10); v
            [0.3576, -0.9365, 0.9449, -0.6957, 1.0217,
             0.9644, 0.9987, -0.5950, -1.0219, 0.6477]
            sage: m.log_likelihood(v)
            -8.31408655939536...
            sage: m.baum_welch(v)
            (2.18905068682..., 15)
            sage: m.log_likelihood(v)
            2.18905068682...
            sage: m  # rel tol 6e-12
            Gaussian Mixture Hidden Markov Model with 2 States
            Transition matrix:
            [   0.8746363339773399   0.12536366602266016]
            [                  1.0 1.451685202290174e-40]
            Emission parameters:
            [0.500161629343*N(-0.812298726239,0.173329026744)
              + 0.499838370657*N(0.982433690378,0.029719932009),
             1.0*N(0.503260056832,0.145881515324)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the min_sd was the default of 0.01::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.baum_welch(v, min_sd=1)
            (-12.617885761692..., 1000)
            sage: m.emission_parameters()  # rel tol 6e-12
            [0.503545634447*N(0.200166509595,1.0) + 0.496454365553*N(0.200166509595,1.0),
             1.0*N(0.0543433426535,1.0)]

        We illustrate fixing all emissions::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10)
            sage: m.baum_welch(v, fix_emissions=True)
            (-7.58656858997..., 36)
            sage: m.emission_parameters()
            [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1),
             1.0*N(0.0,1.0)]"""
    @overload
    def baum_welch(self, v) -> Any:
        """GaussianMixtureHiddenMarkovModel.baum_welch(self, obs, int max_iter=1000, double log_likelihood_cutoff=1e-12, double min_sd=0.01, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1340)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions
        - ``max_iter`` -- integer (default: 1000); maximum number
          of Baum-Welch steps to take
        - ``log_likelihood_cutoff`` -- positive float (default: 1e-12);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.
        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.
        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10); v
            [0.3576, -0.9365, 0.9449, -0.6957, 1.0217,
             0.9644, 0.9987, -0.5950, -1.0219, 0.6477]
            sage: m.log_likelihood(v)
            -8.31408655939536...
            sage: m.baum_welch(v)
            (2.18905068682..., 15)
            sage: m.log_likelihood(v)
            2.18905068682...
            sage: m  # rel tol 6e-12
            Gaussian Mixture Hidden Markov Model with 2 States
            Transition matrix:
            [   0.8746363339773399   0.12536366602266016]
            [                  1.0 1.451685202290174e-40]
            Emission parameters:
            [0.500161629343*N(-0.812298726239,0.173329026744)
              + 0.499838370657*N(0.982433690378,0.029719932009),
             1.0*N(0.503260056832,0.145881515324)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the min_sd was the default of 0.01::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.baum_welch(v, min_sd=1)
            (-12.617885761692..., 1000)
            sage: m.emission_parameters()  # rel tol 6e-12
            [0.503545634447*N(0.200166509595,1.0) + 0.496454365553*N(0.200166509595,1.0),
             1.0*N(0.0543433426535,1.0)]

        We illustrate fixing all emissions::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10)
            sage: m.baum_welch(v, fix_emissions=True)
            (-7.58656858997..., 36)
            sage: m.emission_parameters()
            [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1),
             1.0*N(0.0,1.0)]"""
    @overload
    def baum_welch(self, v, min_sd=...) -> Any:
        """GaussianMixtureHiddenMarkovModel.baum_welch(self, obs, int max_iter=1000, double log_likelihood_cutoff=1e-12, double min_sd=0.01, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1340)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions
        - ``max_iter`` -- integer (default: 1000); maximum number
          of Baum-Welch steps to take
        - ``log_likelihood_cutoff`` -- positive float (default: 1e-12);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.
        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.
        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10); v
            [0.3576, -0.9365, 0.9449, -0.6957, 1.0217,
             0.9644, 0.9987, -0.5950, -1.0219, 0.6477]
            sage: m.log_likelihood(v)
            -8.31408655939536...
            sage: m.baum_welch(v)
            (2.18905068682..., 15)
            sage: m.log_likelihood(v)
            2.18905068682...
            sage: m  # rel tol 6e-12
            Gaussian Mixture Hidden Markov Model with 2 States
            Transition matrix:
            [   0.8746363339773399   0.12536366602266016]
            [                  1.0 1.451685202290174e-40]
            Emission parameters:
            [0.500161629343*N(-0.812298726239,0.173329026744)
              + 0.499838370657*N(0.982433690378,0.029719932009),
             1.0*N(0.503260056832,0.145881515324)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the min_sd was the default of 0.01::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.baum_welch(v, min_sd=1)
            (-12.617885761692..., 1000)
            sage: m.emission_parameters()  # rel tol 6e-12
            [0.503545634447*N(0.200166509595,1.0) + 0.496454365553*N(0.200166509595,1.0),
             1.0*N(0.0543433426535,1.0)]

        We illustrate fixing all emissions::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10)
            sage: m.baum_welch(v, fix_emissions=True)
            (-7.58656858997..., 36)
            sage: m.emission_parameters()
            [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1),
             1.0*N(0.0,1.0)]"""
    @overload
    def baum_welch(self, v, fix_emissions=...) -> Any:
        """GaussianMixtureHiddenMarkovModel.baum_welch(self, obs, int max_iter=1000, double log_likelihood_cutoff=1e-12, double min_sd=0.01, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1340)

        Given an observation sequence ``obs``, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing ``obs``.

        INPUT:

        - ``obs`` -- a time series of emissions
        - ``max_iter`` -- integer (default: 1000); maximum number
          of Baum-Welch steps to take
        - ``log_likelihood_cutoff`` -- positive float (default: 1e-12);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.
        - ``min_sd`` -- positive float (default: 0.01); when
          reestimating, the standard deviation of emissions is not
          allowed to be less than ``min_sd``.
        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do not
          change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10); v
            [0.3576, -0.9365, 0.9449, -0.6957, 1.0217,
             0.9644, 0.9987, -0.5950, -1.0219, 0.6477]
            sage: m.log_likelihood(v)
            -8.31408655939536...
            sage: m.baum_welch(v)
            (2.18905068682..., 15)
            sage: m.log_likelihood(v)
            2.18905068682...
            sage: m  # rel tol 6e-12
            Gaussian Mixture Hidden Markov Model with 2 States
            Transition matrix:
            [   0.8746363339773399   0.12536366602266016]
            [                  1.0 1.451685202290174e-40]
            Emission parameters:
            [0.500161629343*N(-0.812298726239,0.173329026744)
              + 0.499838370657*N(0.982433690378,0.029719932009),
             1.0*N(0.503260056832,0.145881515324)]
            Initial probabilities: [0.0000, 1.0000]

        We illustrate bounding the standard deviation below.  Note that above we had
        different emission parameters when the min_sd was the default of 0.01::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.baum_welch(v, min_sd=1)
            (-12.617885761692..., 1000)
            sage: m.emission_parameters()  # rel tol 6e-12
            [0.503545634447*N(0.200166509595,1.0) + 0.496454365553*N(0.200166509595,1.0),
             1.0*N(0.0543433426535,1.0)]

        We illustrate fixing all emissions::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: set_random_seed(0); v = m.sample(10)
            sage: m.baum_welch(v, fix_emissions=True)
            (-7.58656858997..., 36)
            sage: m.emission_parameters()
            [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1),
             1.0*N(0.0,1.0)]"""
    @overload
    def emission_parameters(self) -> Any:
        """GaussianMixtureHiddenMarkovModel.emission_parameters(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1229)

        Return a list of all the emission distributions.

        OUTPUT: list of Gaussian mixtures

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel([[.9,.1],[.4,.6]],
            ....:                                          [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:                                          [.7,.3])
            sage: m.emission_parameters()
            [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1), 1.0*N(0.0,1.0)]"""
    @overload
    def emission_parameters(self) -> Any:
        """GaussianMixtureHiddenMarkovModel.emission_parameters(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1229)

        Return a list of all the emission distributions.

        OUTPUT: list of Gaussian mixtures

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel([[.9,.1],[.4,.6]],
            ....:                                          [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:                                          [.7,.3])
            sage: m.emission_parameters()
            [0.4*N(0.0,1.0) + 0.6*N(1.0,0.1), 1.0*N(0.0,1.0)]"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, Py_ssize_ti) -> Any:
        """GaussianMixtureHiddenMarkovModel.__getitem__(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1188)

        Return the Gaussian mixture distribution associated to the
        i-th state.

        INPUT:

        - ``i`` -- integer

        OUTPUT: a Gaussian mixture distribution object

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel([[.9,.1],[.4,.6]], [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]], [.7,.3])
            sage: m[0]
            0.4*N(0.0,1.0) + 0.6*N(1.0,0.1)
            sage: m[1]
            1.0*N(0.0,1.0)

        Negative indexing works::

            sage: m[-1]
            1.0*N(0.0,1.0)

        Bounds are checked::

            sage: m[2]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: m[-3]
            Traceback (most recent call last):
            ...
            IndexError: index out of range"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """GaussianMixtureHiddenMarkovModel.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/chmm.pyx (starting at line 1152)

        Used in pickling.

        EXAMPLES::

            sage: m = hmm.GaussianMixtureHiddenMarkovModel([[1]], [[(.4,(0,1)), (.6,(1,0.1))]], [1])
            sage: loads(dumps(m)) == m
            True"""
