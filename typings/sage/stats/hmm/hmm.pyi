import _cython_3_2_1
from sage.matrix.constructor import matrix as matrix
from sage.structure.element import Matrix as Matrix
from typing import Any, ClassVar, overload

unpickle_discrete_hmm_v0: _cython_3_2_1.cython_function_or_method
unpickle_discrete_hmm_v1: _cython_3_2_1.cython_function_or_method

class DiscreteHiddenMarkovModel(HiddenMarkovModel):
    """DiscreteHiddenMarkovModel(A, B, pi, emission_symbols=None, bool normalize=True)

    File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 257)

    A discrete Hidden Markov model implemented using double precision
    floating point arithmetic.

    INPUT:

    - ``A`` -- list of lists or a square `N \\times N` matrix, whose
      `(i,j)` entry gives the probability of transitioning from
      state `i` to state `j`.

    - ``B`` -- list of `N` lists or a matrix with `N` rows, such that
      `B[i,k]` gives the probability of emitting symbol `k` while
      in state `i`.

    - ``pi`` -- the probabilities of starting in each initial
      state, i.e., ``pi[i]`` is the probability of starting in
      state `i`.

    - ``emission_symbols`` -- ``None`` or list (default: ``None``); if
      None, the emission_symbols are the ints ``[0..N-1]``, where `N`
      is the number of states.  Otherwise, they are the entries
      of the list ``emissions_symbols``, which must all be hashable.

    - ``normalize`` -- boolean (default: ``True``); if given, input is
      normalized to define valid probability distributions,
      e.g., the entries of `A` are made nonnegative and the rows
      sum to 1, and the probabilities in ``pi`` are normalized.

    EXAMPLES::

        sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
        ....:                                   [[0.1,0.9],[0.5,0.5]],
        ....:                                   [.5,.5]); m
        Discrete Hidden Markov Model with 2 States and 2 Emissions
        Transition matrix:
        [0.4 0.6]
        [0.1 0.9]
        Emission matrix:
        [0.1 0.9]
        [0.5 0.5]
        Initial probabilities: [0.5000, 0.5000]
        sage: m.log_likelihood([0,1,0,1,0,1])
        -4.66693474691329...
        sage: m.viterbi([0,1,0,1,0,1])
        ([1, 1, 1, 1, 1, 1], -5.378832842208748)
        sage: m.baum_welch([0,1,0,1,0,1])
        (0.0, 22)
        sage: m  # rel tol 1e-10
        Discrete Hidden Markov Model with 2 States and 2 Emissions
        Transition matrix:
        [1.0134345614745788e-70                    1.0]
        [                   1.0 3.9974352713558623e-19]
        Emission matrix:
        [ 7.380221566254936e-54                    1.0]
        [                   1.0 3.9974352626002193e-19]
        Initial probabilities: [0.0000, 1.0000]
        sage: m.sample(10)
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        sage: m.graph().plot()                                                          # needs sage.plot
        Graphics object consisting of 6 graphics primitives

    A 3-state model that happens to always outputs 'b'::

        sage: m = hmm.DiscreteHiddenMarkovModel([[1/3]*3]*3, [[0,1,0]]*3, [1/3]*3, ['a','b','c'])
        sage: m.sample(10)
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, A, B, pi, emission_symbols=..., boolnormalize=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 329)

                Create a discrete emissions HMM with transition probability
                matrix A, emission probabilities given by B, initial state
                probabilities pi, and given emission symbols (which default
                to the first few nonnegative integers).

                EXAMPLES::

                    sage: hmm.DiscreteHiddenMarkovModel([.5,0,-1,.5], [[1],[1]],[.5,.5]).transition_matrix()
                    [1.0 0.0]
                    [0.0 1.0]
                    sage: hmm.DiscreteHiddenMarkovModel([0,0,.1,.9], [[1],[1]],[.5,.5]).transition_matrix()
                    [0.5 0.5]
                    [0.1 0.9]
                    sage: hmm.DiscreteHiddenMarkovModel([-1,-2,.1,.9], [[1],[1]],[.5,.5]).transition_matrix()
                    [0.5 0.5]
                    [0.1 0.9]
                    sage: hmm.DiscreteHiddenMarkovModel([1,2,.1,1.2], [[1],[1]],[.5,.5]).transition_matrix()
                    [ 0.3333333333333333  0.6666666666666666]
                    [0.07692307692307693   0.923076923076923]
        """
    @overload
    def baum_welch(self, obs, intmax_iter=..., doublelog_likelihood_cutoff=..., boolfix_emissions=...) -> Any:
        """DiscreteHiddenMarkovModel.baum_welch(self, obs, int max_iter=100, double log_likelihood_cutoff=1e-4, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 1197)

        Given an observation sequence obs, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing obs.

        INPUT:

        - ``obs`` -- list of emissions

        - ``max_iter`` -- integer (default: 100); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do
          not change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[0,1]],
            ....:                                   [.2,.8])
            sage: m.baum_welch([1,0]*20, log_likelihood_cutoff=0)
            (0.0, 4)
            sage: m  # rel tol 1e-14
            Discrete Hidden Markov Model with 2 States and 2 Emissions
            Transition matrix:
            [1.3515269707707603e-51                    1.0]
            [                   1.0                    0.0]
            Emission matrix:
            [                  1.0 6.462537138850569e-52]
            [                  0.0                   1.0]
            Initial probabilities: [0.0000, 1.0000]

        The following illustrates how Baum-Welch is only a local
        optimizer, i.e., the above model is far more likely to produce
        the sequence [1,0]*20 than the one we get below::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.5,0.5],[0.5,0.5]],
            ....:                                   [[.5,.5],[.5,.5]],
            ....:                                   [.5,.5])
            sage: m.baum_welch([1,0]*20, log_likelihood_cutoff=0)
            (-27.725887222397784, 1)
            sage: m
            Discrete Hidden Markov Model with 2 States and 2 Emissions
            Transition matrix:
            [0.5 0.5]
            [0.5 0.5]
            Emission matrix:
            [0.5 0.5]
            [0.5 0.5]
            Initial probabilities: [0.5000, 0.5000]

        We illustrate fixing emissions::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[.2,.8]],
            ....:                                   [.2,.8])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-66.98630856918774, 100)
            sage: m.emission_matrix()
            [0.5 0.5]
            [0.2 0.8]
            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[.2,.8]],
            ....:                                   [.2,.8])
            sage: m.baum_welch(v)
            (-66.782360659293..., 100)
            sage: m.emission_matrix()  # rel tol 1e-14
            [ 0.5303085748626447 0.46969142513735535]
            [ 0.2909775550173978  0.7090224449826023]"""
    @overload
    def baum_welch(self, v, fix_emissions=...) -> Any:
        """DiscreteHiddenMarkovModel.baum_welch(self, obs, int max_iter=100, double log_likelihood_cutoff=1e-4, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 1197)

        Given an observation sequence obs, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing obs.

        INPUT:

        - ``obs`` -- list of emissions

        - ``max_iter`` -- integer (default: 100); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do
          not change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[0,1]],
            ....:                                   [.2,.8])
            sage: m.baum_welch([1,0]*20, log_likelihood_cutoff=0)
            (0.0, 4)
            sage: m  # rel tol 1e-14
            Discrete Hidden Markov Model with 2 States and 2 Emissions
            Transition matrix:
            [1.3515269707707603e-51                    1.0]
            [                   1.0                    0.0]
            Emission matrix:
            [                  1.0 6.462537138850569e-52]
            [                  0.0                   1.0]
            Initial probabilities: [0.0000, 1.0000]

        The following illustrates how Baum-Welch is only a local
        optimizer, i.e., the above model is far more likely to produce
        the sequence [1,0]*20 than the one we get below::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.5,0.5],[0.5,0.5]],
            ....:                                   [[.5,.5],[.5,.5]],
            ....:                                   [.5,.5])
            sage: m.baum_welch([1,0]*20, log_likelihood_cutoff=0)
            (-27.725887222397784, 1)
            sage: m
            Discrete Hidden Markov Model with 2 States and 2 Emissions
            Transition matrix:
            [0.5 0.5]
            [0.5 0.5]
            Emission matrix:
            [0.5 0.5]
            [0.5 0.5]
            Initial probabilities: [0.5000, 0.5000]

        We illustrate fixing emissions::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[.2,.8]],
            ....:                                   [.2,.8])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-66.98630856918774, 100)
            sage: m.emission_matrix()
            [0.5 0.5]
            [0.2 0.8]
            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[.2,.8]],
            ....:                                   [.2,.8])
            sage: m.baum_welch(v)
            (-66.782360659293..., 100)
            sage: m.emission_matrix()  # rel tol 1e-14
            [ 0.5303085748626447 0.46969142513735535]
            [ 0.2909775550173978  0.7090224449826023]"""
    @overload
    def baum_welch(self, v) -> Any:
        """DiscreteHiddenMarkovModel.baum_welch(self, obs, int max_iter=100, double log_likelihood_cutoff=1e-4, bool fix_emissions=False)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 1197)

        Given an observation sequence obs, improve this HMM using the
        Baum-Welch algorithm to increase the probability of observing obs.

        INPUT:

        - ``obs`` -- list of emissions

        - ``max_iter`` -- integer (default: 100); maximum number
          of Baum-Welch steps to take

        - ``log_likelihood_cutoff`` -- positive float (default: 1e-4);
          the minimal improvement in likelihood with respect to
          the last iteration required to continue. Relative value
          to log likelihood.

        - ``fix_emissions`` -- boolean (default: ``False``); if ``True``, do
          not change emissions when updating

        OUTPUT:

        changes the model in place, and returns the log
        likelihood and number of iterations.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[0,1]],
            ....:                                   [.2,.8])
            sage: m.baum_welch([1,0]*20, log_likelihood_cutoff=0)
            (0.0, 4)
            sage: m  # rel tol 1e-14
            Discrete Hidden Markov Model with 2 States and 2 Emissions
            Transition matrix:
            [1.3515269707707603e-51                    1.0]
            [                   1.0                    0.0]
            Emission matrix:
            [                  1.0 6.462537138850569e-52]
            [                  0.0                   1.0]
            Initial probabilities: [0.0000, 1.0000]

        The following illustrates how Baum-Welch is only a local
        optimizer, i.e., the above model is far more likely to produce
        the sequence [1,0]*20 than the one we get below::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.5,0.5],[0.5,0.5]],
            ....:                                   [[.5,.5],[.5,.5]],
            ....:                                   [.5,.5])
            sage: m.baum_welch([1,0]*20, log_likelihood_cutoff=0)
            (-27.725887222397784, 1)
            sage: m
            Discrete Hidden Markov Model with 2 States and 2 Emissions
            Transition matrix:
            [0.5 0.5]
            [0.5 0.5]
            Emission matrix:
            [0.5 0.5]
            [0.5 0.5]
            Initial probabilities: [0.5000, 0.5000]

        We illustrate fixing emissions::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[.2,.8]],
            ....:                                   [.2,.8])
            sage: set_random_seed(0); v = m.sample(100)
            sage: m.baum_welch(v,fix_emissions=True)
            (-66.98630856918774, 100)
            sage: m.emission_matrix()
            [0.5 0.5]
            [0.2 0.8]
            sage: m = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.9,0.1]],
            ....:                                   [[.5,.5],[.2,.8]],
            ....:                                   [.2,.8])
            sage: m.baum_welch(v)
            (-66.782360659293..., 100)
            sage: m.emission_matrix()  # rel tol 1e-14
            [ 0.5303085748626447 0.46969142513735535]
            [ 0.2909775550173978  0.7090224449826023]"""
    @overload
    def emission_matrix(self) -> Any:
        """DiscreteHiddenMarkovModel.emission_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 404)

        Return the matrix whose `i`-th row specifies the emission
        probability distribution for the `i`-th state.

        More precisely,
        the `i,j` entry of the matrix is the probability of the Markov
        model outputting the `j`-th symbol when it is in the `i`-th state.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.5,.5])
            sage: E = m.emission_matrix(); E
            [0.1 0.9]
            [0.5 0.5]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: E[0,0] = 0; E[0,1] = 1
            sage: m.emission_matrix()
            [0.1 0.9]
            [0.5 0.5]"""
    @overload
    def emission_matrix(self) -> Any:
        """DiscreteHiddenMarkovModel.emission_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 404)

        Return the matrix whose `i`-th row specifies the emission
        probability distribution for the `i`-th state.

        More precisely,
        the `i,j` entry of the matrix is the probability of the Markov
        model outputting the `j`-th symbol when it is in the `i`-th state.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.5,.5])
            sage: E = m.emission_matrix(); E
            [0.1 0.9]
            [0.5 0.5]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: E[0,0] = 0; E[0,1] = 1
            sage: m.emission_matrix()
            [0.1 0.9]
            [0.5 0.5]"""
    @overload
    def emission_matrix(self) -> Any:
        """DiscreteHiddenMarkovModel.emission_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 404)

        Return the matrix whose `i`-th row specifies the emission
        probability distribution for the `i`-th state.

        More precisely,
        the `i,j` entry of the matrix is the probability of the Markov
        model outputting the `j`-th symbol when it is in the `i`-th state.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.5,.5])
            sage: E = m.emission_matrix(); E
            [0.1 0.9]
            [0.5 0.5]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: E[0,0] = 0; E[0,1] = 1
            sage: m.emission_matrix()
            [0.1 0.9]
            [0.5 0.5]"""
    def generate_sequence(self, Py_ssize_tlength, starting_state=...) -> Any:
        """DiscreteHiddenMarkovModel.generate_sequence(self, Py_ssize_t length, starting_state=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 691)

        Return a sample of the given length from this HMM.

        INPUT:

        - ``length`` -- positive integer
        - ``starting_state`` -- integer (or ``None``); if specified, generate a
          sequence using this model starting with the given state instead of
          the initial probabilities to determine the starting state

        OUTPUT:

        - an :class:`IntList` or list of emission symbols
        - :class:`IntList` of the actual states the model was in when
          emitting the corresponding symbols

        EXAMPLES:

        In this example, the emission symbols are not set::

            sage: set_random_seed(0)
            sage: a = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.1,0.9]],
            ....:                                   [[1,0],[0,1]],
            ....:                                   [0,1])
            sage: a.generate_sequence(5)
            ([1, 0, 1, 1, 1], [1, 0, 1, 1, 1])
            sage: list(a.generate_sequence(1000)[0]).count(0)
            90

        Here the emission symbols are set::

            sage: set_random_seed(0)
            sage: a = hmm.DiscreteHiddenMarkovModel([[0.5,0.5],[0.1,0.9]],
            ....:                                   [[1,0],[0,1]],
            ....:                                   [0,1], ['up', 'down'])
            sage: a.generate_sequence(5)
            (['down', 'up', 'down', 'down', 'down'], [1, 0, 1, 1, 1])

        Specify the starting state::

            sage: set_random_seed(0); a.generate_sequence(5, starting_state=0)
            (['up', 'up', 'down', 'down', 'down'], [0, 0, 1, 1, 1])"""
    def log_likelihood(self, obs, boolscale=...) -> Any:
        """DiscreteHiddenMarkovModel.log_likelihood(self, obs, bool scale=True)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 493)

        Return the logarithm of the probability that this model produced the given
        observation sequence.  Thus the output is a nonpositive number.

        INPUT:

        - ``obs`` -- sequence of observations

        - ``scale`` -- boolean (default: ``True``); if ``True``, use rescaling
          to overoid loss of precision due to the very limited
          dynamic range of floats.  You should leave this as ``True``
          unless the ``obs`` sequence is very small.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: m.log_likelihood([0, 1, 0, 1, 1, 0, 1, 0, 0, 0])
            -7.3301308009370825
            sage: m.log_likelihood([0, 1, 0, 1, 1, 0, 1, 0, 0, 0], scale=False)
            -7.330130800937082
            sage: m.log_likelihood([])
            0.0

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8], ['happy','sad'])
            sage: m.log_likelihood(['happy','happy'])
            -1.6565295199679506
            sage: m.log_likelihood(['happy','sad'])
            -1.4731602941415523

        Overflow from not using the scale option::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: m.log_likelihood([0,1]*1000, scale=True)
            -1433.820666652728
            sage: m.log_likelihood([0,1]*1000, scale=False)
            -inf"""
    def viterbi(self, obs, log_scale=...) -> Any:
        '''DiscreteHiddenMarkovModel.viterbi(self, obs, log_scale=True)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 842)

        Determine "the" hidden sequence of states that is most likely
        to produce the given sequence seq of observations, along with
        the probability that this hidden sequence actually produced
        the observation.

        INPUT:

        - ``seq`` -- sequence of emitted ints or symbols

        - ``log_scale`` -- boolean (default: ``True``); whether to scale the
          sequence in order to avoid numerical overflow

        OUTPUT:

        - ``list`` -- "the" most probable sequence of hidden states, i.e.,
          the Viterbi path

        - ``float`` -- log of probability that the observed sequence
          was produced by the Viterbi sequence of states

        EXAMPLES::

            sage: a = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.1,0.9]],
            ....:                                   [[0.9,0.1],[0.1,0.9]],
            ....:                                   [0.5,0.5])
            sage: a.viterbi([1,0,0,1,0,0,1,1])
            ([1, 0, 0, 1, ..., 0, 1, 1], -11.06245322477221...)

        We predict the state sequence when the emissions are 3/4 and \'abc\'.::

            sage: a = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.1,0.9]],
            ....:                                   [[0.9,0.1],[0.1,0.9]],
            ....:                                   [0.5,0.5], [3/4, \'abc\'])

        Note that state 0 is common below, despite the model trying hard to
        switch to state 1::

            sage: a.viterbi([3/4, \'abc\', \'abc\'] + [3/4]*10)
            ([0, 1, 1, 0, 0 ... 0, 0, 0, 0, 0], -25.299405845367794)'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """DiscreteHiddenMarkovModel.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 371)

        Used in pickling.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]], [[0.0,1.0],[1,1]], [0,1], ['a','b'])
            sage: loads(dumps(m)) == m
            True"""

class HiddenMarkovModel:
    """File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 50)

        Abstract base class for all Hidden Markov Models.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def graph(self, eps=...) -> Any:
        """HiddenMarkovModel.graph(self, eps=1e-3)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 135)

        Create a weighted directed graph from the transition matrix,
        not including any edge with a probability less than ``eps``.

        INPUT:

        - ``eps`` -- nonnegative real number

        OUTPUT: a :class:`DiGraph`

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[.3,0,.7],[0,0,1],[.5,.5,0]],
            ....:                                   [[.5,.5,.2]]*3,
            ....:                                   [1/3]*3)
            sage: G = m.graph(); G                                                      # needs sage.graphs
            Looped digraph on 3 vertices
            sage: G.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, 0.3), (0, 2, 0.7), (1, 2, 1.0), (2, 0, 0.5), (2, 1, 0.5)]
            sage: G.plot()                                                              # needs sage.graphs sage.plot
            Graphics object consisting of 11 graphics primitives"""
    @overload
    def graph(self) -> Any:
        """HiddenMarkovModel.graph(self, eps=1e-3)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 135)

        Create a weighted directed graph from the transition matrix,
        not including any edge with a probability less than ``eps``.

        INPUT:

        - ``eps`` -- nonnegative real number

        OUTPUT: a :class:`DiGraph`

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[.3,0,.7],[0,0,1],[.5,.5,0]],
            ....:                                   [[.5,.5,.2]]*3,
            ....:                                   [1/3]*3)
            sage: G = m.graph(); G                                                      # needs sage.graphs
            Looped digraph on 3 vertices
            sage: G.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, 0.3), (0, 2, 0.7), (1, 2, 1.0), (2, 0, 0.5), (2, 1, 0.5)]
            sage: G.plot()                                                              # needs sage.graphs sage.plot
            Graphics object consisting of 11 graphics primitives"""
    @overload
    def initial_probabilities(self) -> Any:
        """HiddenMarkovModel.initial_probabilities(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 54)

        Return the initial probabilities as a :class:`TimeSeries` of
        length `N`, where `N` is the number of states of the Markov model.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: pi = m.initial_probabilities(); pi
            [0.2000, 0.8000]
            sage: type(pi)
            <... 'sage.stats.time_series.TimeSeries'>

        The returned time series is a copy, so changing it does not
        change the model::

            sage: pi[0] = .1; pi[1] = .9
            sage: m.initial_probabilities()
            [0.2000, 0.8000]

        Some other models::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.1,.9])
            sage: m.initial_probabilities()
            [0.1000, 0.9000]
            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.initial_probabilities()
            [0.7000, 0.3000]"""
    @overload
    def initial_probabilities(self) -> Any:
        """HiddenMarkovModel.initial_probabilities(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 54)

        Return the initial probabilities as a :class:`TimeSeries` of
        length `N`, where `N` is the number of states of the Markov model.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: pi = m.initial_probabilities(); pi
            [0.2000, 0.8000]
            sage: type(pi)
            <... 'sage.stats.time_series.TimeSeries'>

        The returned time series is a copy, so changing it does not
        change the model::

            sage: pi[0] = .1; pi[1] = .9
            sage: m.initial_probabilities()
            [0.2000, 0.8000]

        Some other models::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.1,.9])
            sage: m.initial_probabilities()
            [0.1000, 0.9000]
            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.initial_probabilities()
            [0.7000, 0.3000]"""
    @overload
    def initial_probabilities(self) -> Any:
        """HiddenMarkovModel.initial_probabilities(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 54)

        Return the initial probabilities as a :class:`TimeSeries` of
        length `N`, where `N` is the number of states of the Markov model.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: pi = m.initial_probabilities(); pi
            [0.2000, 0.8000]
            sage: type(pi)
            <... 'sage.stats.time_series.TimeSeries'>

        The returned time series is a copy, so changing it does not
        change the model::

            sage: pi[0] = .1; pi[1] = .9
            sage: m.initial_probabilities()
            [0.2000, 0.8000]

        Some other models::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.1,.9])
            sage: m.initial_probabilities()
            [0.1000, 0.9000]
            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.initial_probabilities()
            [0.7000, 0.3000]"""
    @overload
    def initial_probabilities(self) -> Any:
        """HiddenMarkovModel.initial_probabilities(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 54)

        Return the initial probabilities as a :class:`TimeSeries` of
        length `N`, where `N` is the number of states of the Markov model.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: pi = m.initial_probabilities(); pi
            [0.2000, 0.8000]
            sage: type(pi)
            <... 'sage.stats.time_series.TimeSeries'>

        The returned time series is a copy, so changing it does not
        change the model::

            sage: pi[0] = .1; pi[1] = .9
            sage: m.initial_probabilities()
            [0.2000, 0.8000]

        Some other models::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.1,.9])
            sage: m.initial_probabilities()
            [0.1000, 0.9000]
            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.initial_probabilities()
            [0.7000, 0.3000]"""
    @overload
    def initial_probabilities(self) -> Any:
        """HiddenMarkovModel.initial_probabilities(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 54)

        Return the initial probabilities as a :class:`TimeSeries` of
        length `N`, where `N` is the number of states of the Markov model.

        EXAMPLES::

            sage: m = hmm.DiscreteHiddenMarkovModel([[0.4,0.6],[0.1,0.9]],
            ....:                                   [[0.1,0.9],[0.5,0.5]],
            ....:                                   [.2,.8])
            sage: pi = m.initial_probabilities(); pi
            [0.2000, 0.8000]
            sage: type(pi)
            <... 'sage.stats.time_series.TimeSeries'>

        The returned time series is a copy, so changing it does not
        change the model::

            sage: pi[0] = .1; pi[1] = .9
            sage: m.initial_probabilities()
            [0.2000, 0.8000]

        Some other models::

            sage: m = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.1,.9])
            sage: m.initial_probabilities()
            [0.1000, 0.9000]
            sage: m = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))], [(1,(0,1))]],
            ....:         [.7,.3])
            sage: m.initial_probabilities()
            [0.7000, 0.3000]"""
    def sample(self, Py_ssize_tlength, number=..., starting_state=...) -> Any:
        """HiddenMarkovModel.sample(self, Py_ssize_t length, number=None, starting_state=None)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 167)

        Return number samples from this HMM of given length.

        INPUT:

        - ``length`` -- positive integer
        - ``number`` -- (default: ``None``) if given, compute list of this many
          sample sequences
        - ``starting_state`` -- integer (or ``None``); if specified, generate a
          sequence using this model starting with the given state instead of
          the initial probabilities to determine the starting state

        OUTPUT:

        - if ``number`` is not given, return a single :class:`TimeSeries`.
        - if ``number`` is given, return a list of :class:`TimeSeries`.

        EXAMPLES::

            sage: set_random_seed(0)
            sage: a = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.1,0.9]],
            ....:                                   [[1,0],[0,1]],
            ....:                                   [0,1])
            sage: print(a.sample(10, 3))
            [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
             [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 1, 0, 1, 1, 1]]
            sage: a.sample(15)
            [1, 1, 1, 1, 0 ... 1, 1, 1, 1, 1]
            sage: a.sample(3, 1)
            [[1, 1, 1]]
            sage: list(a.sample(1000)).count(0)
            88

        If the emission symbols are set::

            sage: set_random_seed(0)
            sage: a = hmm.DiscreteHiddenMarkovModel([[0.5,0.5],[0.1,0.9]],
            ....:                                   [[1,0],[0,1]], [0,1],
            ....:                                   ['up', 'down'])
            sage: a.sample(10)
            ['down', 'up', 'down', 'down', 'down', 'down', 'up', 'up', 'up', 'up']

        Force a starting state::

            sage: set_random_seed(0); a.sample(10, starting_state=0)
            ['up', 'up', 'down', 'down', 'down', 'down', 'up', 'up', 'up', 'up']"""
    @overload
    def transition_matrix(self) -> Any:
        """HiddenMarkovModel.transition_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 92)

        Return the state transition matrix.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: M = hmm.DiscreteHiddenMarkovModel([[0.7,0.3],[0.9,0.1]],
            ....:                                   [[0.5,.5],[.1,.9]],
            ....:                                   [0.3,0.7])
            sage: T = M.transition_matrix(); T
            [0.7 0.3]
            [0.9 0.1]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: T[0,0] = .1; T[0,1] = .9
            sage: M.transition_matrix()
            [0.7 0.3]
            [0.9 0.1]

        Transition matrices for other types of models::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.5,.5])
            sage: M.transition_matrix()
            [0.1 0.9]
            [0.5 0.5]
            sage: M = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]],
            ....:         [.7,.3])
            sage: M.transition_matrix()
            [0.9 0.1]
            [0.4 0.6]"""
    @overload
    def transition_matrix(self) -> Any:
        """HiddenMarkovModel.transition_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 92)

        Return the state transition matrix.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: M = hmm.DiscreteHiddenMarkovModel([[0.7,0.3],[0.9,0.1]],
            ....:                                   [[0.5,.5],[.1,.9]],
            ....:                                   [0.3,0.7])
            sage: T = M.transition_matrix(); T
            [0.7 0.3]
            [0.9 0.1]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: T[0,0] = .1; T[0,1] = .9
            sage: M.transition_matrix()
            [0.7 0.3]
            [0.9 0.1]

        Transition matrices for other types of models::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.5,.5])
            sage: M.transition_matrix()
            [0.1 0.9]
            [0.5 0.5]
            sage: M = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]],
            ....:         [.7,.3])
            sage: M.transition_matrix()
            [0.9 0.1]
            [0.4 0.6]"""
    @overload
    def transition_matrix(self) -> Any:
        """HiddenMarkovModel.transition_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 92)

        Return the state transition matrix.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: M = hmm.DiscreteHiddenMarkovModel([[0.7,0.3],[0.9,0.1]],
            ....:                                   [[0.5,.5],[.1,.9]],
            ....:                                   [0.3,0.7])
            sage: T = M.transition_matrix(); T
            [0.7 0.3]
            [0.9 0.1]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: T[0,0] = .1; T[0,1] = .9
            sage: M.transition_matrix()
            [0.7 0.3]
            [0.9 0.1]

        Transition matrices for other types of models::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.5,.5])
            sage: M.transition_matrix()
            [0.1 0.9]
            [0.5 0.5]
            sage: M = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]],
            ....:         [.7,.3])
            sage: M.transition_matrix()
            [0.9 0.1]
            [0.4 0.6]"""
    @overload
    def transition_matrix(self) -> Any:
        """HiddenMarkovModel.transition_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 92)

        Return the state transition matrix.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: M = hmm.DiscreteHiddenMarkovModel([[0.7,0.3],[0.9,0.1]],
            ....:                                   [[0.5,.5],[.1,.9]],
            ....:                                   [0.3,0.7])
            sage: T = M.transition_matrix(); T
            [0.7 0.3]
            [0.9 0.1]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: T[0,0] = .1; T[0,1] = .9
            sage: M.transition_matrix()
            [0.7 0.3]
            [0.9 0.1]

        Transition matrices for other types of models::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.5,.5])
            sage: M.transition_matrix()
            [0.1 0.9]
            [0.5 0.5]
            sage: M = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]],
            ....:         [.7,.3])
            sage: M.transition_matrix()
            [0.9 0.1]
            [0.4 0.6]"""
    @overload
    def transition_matrix(self) -> Any:
        """HiddenMarkovModel.transition_matrix(self)

        File: /build/sagemath/src/sage/src/sage/stats/hmm/hmm.pyx (starting at line 92)

        Return the state transition matrix.

        OUTPUT: a Sage matrix with real double precision (RDF) entries.

        EXAMPLES::

            sage: M = hmm.DiscreteHiddenMarkovModel([[0.7,0.3],[0.9,0.1]],
            ....:                                   [[0.5,.5],[.1,.9]],
            ....:                                   [0.3,0.7])
            sage: T = M.transition_matrix(); T
            [0.7 0.3]
            [0.9 0.1]

        The returned matrix is mutable, but changing it does not
        change the transition matrix for the model::

            sage: T[0,0] = .1; T[0,1] = .9
            sage: M.transition_matrix()
            [0.7 0.3]
            [0.9 0.1]

        Transition matrices for other types of models::

            sage: M = hmm.GaussianHiddenMarkovModel([[.1,.9],[.5,.5]],
            ....:                                   [(1,1), (-1,1)],
            ....:                                   [.5,.5])
            sage: M.transition_matrix()
            [0.1 0.9]
            [0.5 0.5]
            sage: M = hmm.GaussianMixtureHiddenMarkovModel(
            ....:         [[.9,.1],[.4,.6]],
            ....:         [[(.4,(0,1)), (.6,(1,0.1))],[(1,(0,1))]],
            ....:         [.7,.3])
            sage: M.transition_matrix()
            [0.9 0.1]
            [0.4 0.6]"""
