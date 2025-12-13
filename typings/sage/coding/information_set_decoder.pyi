from .decoder import Decoder as Decoder
from sage.arith.misc import binomial as binomial
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

class InformationSetAlgorithm(SageObject):
    '''
    Abstract class for algorithms for
    :class:`sage.coding.information_set_decoder.LinearCodeInformationSetDecoder`.

    To sub-class this class, override ``decode`` and ``calibrate``, and call the
    super constructor from ``__init__``.

    INPUT:

    - ``code`` -- a linear code for which to decode

    - ``number_errors`` -- integer; the maximal number of errors to accept as
      correct decoding. An interval can also be specified by giving a pair of
      integers, where both end values are taken to be in the interval.

    - ``algorithm_name`` -- a name for the specific ISD algorithm used (used for
      printing)

    - ``parameters`` -- (optional) A dictionary for setting the parameters of
      this ISD algorithm. Note that sanity checking this dictionary for the
      individual sub-classes should be done in the sub-class constructor.

    EXAMPLES::

        sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
        sage: LeeBrickellISDAlgorithm(codes.GolayCode(GF(2)), (0,4))
        ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2)
         decoding up to 4 errors

    A minimal working example of how to sub-class::

        sage: from sage.coding.information_set_decoder import InformationSetAlgorithm
        sage: from sage.coding.decoder import DecodingError
        sage: class MinimalISD(InformationSetAlgorithm):
        ....:     def __init__(self, code, decoding_interval):
        ....:         super().__init__(code, decoding_interval, "MinimalISD")
        ....:     def calibrate(self):
        ....:         self._parameters = { } # calibrate parameters here
        ....:         self._time_estimate = 10.0  # calibrated time estimate
        ....:     def decode(self, r):
        ....:         # decoding algorithm here
        ....:         raise DecodingError("I failed")
        sage: MinimalISD(codes.GolayCode(GF(2)), (0,4))
        ISD Algorithm (MinimalISD) for [24, 12, 8] Extended Golay code over GF(2)
         decoding up to 4 errors
    '''
    def __init__(self, code, decoding_interval, algorithm_name, parameters=None) -> None:
        """
        TESTS::

            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: LeeBrickellISDAlgorithm(codes.GolayCode(GF(2)), (0,4))
            ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2) decoding up to 4 errors
        """
    def name(self):
        """
        Return the name of this ISD algorithm.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0,2))
            sage: A.name()
            'Lee-Brickell'
        """
    def decode(self, r) -> None:
        """
        Decode a received word using this ISD decoding algorithm.

        Must be overridden by sub-classes.

        EXAMPLES::

            sage: M = matrix(GF(2), [[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],\\\n            ....:                    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],\\\n            ....:                    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],\\\n            ....:                    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],\\\n            ....:                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]])
            sage: C = codes.LinearCode(M)
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (2,2))
            sage: r = vector(GF(2), [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            sage: A.decode(r)
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        """
    def time_estimate(self):
        """
        Estimate for how long this ISD algorithm takes to perform a single decoding.

        The estimate is for a received word whose number of errors is within the
        decoding interval of this ISD algorithm.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0,2))
            sage: A.time_estimate() #random
            0.0008162108571427874
        """
    def calibrate(self) -> None:
        """
        Uses test computations to estimate optimal values for any parameters
        this ISD algorithm may take.

        Must be overridden by sub-classes.

        If ``self._parameters_specified`` is ``False``, this method shall set
        ``self._parameters`` to the best parameters estimated. It shall always
        set ``self._time_estimate`` to the time estimate of using
        ``self._parameters``.

        EXAMPLES::

            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: C = codes.GolayCode(GF(2))
            sage: A = LeeBrickellISDAlgorithm(C, (0,3))
            sage: A.calibrate()
            sage: A.parameters() #random
            {'search_size': 1}
        """
    def code(self):
        """
        Return the code associated to this ISD algorithm.

        EXAMPLES::

            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: C = codes.GolayCode(GF(2))
            sage: A = LeeBrickellISDAlgorithm(C, (0,3))
            sage: A.code()
            [24, 12, 8] Extended Golay code over GF(2)
        """
    def decoding_interval(self):
        """
         A pair of integers specifying the interval of number of errors this
         ISD algorithm will attempt to correct.

         The interval includes both end values.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0,2))
            sage: A.decoding_interval()
            (0, 2)
        """
    def parameters(self):
        """
        Return any parameters this ISD algorithm uses.

        If the parameters have not already been set, efficient values will first
        be calibrated and returned.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0,4), search_size=3)
            sage: A.parameters()
            {'search_size': 3}

        If not set, calibration will determine a sensible value::

            sage: A = LeeBrickellISDAlgorithm(C, (0,4))
            sage: A.parameters() #random
            {'search_size': 1}
        """
    def __eq__(self, other):
        """
        Test equality between ISD algorithm objects.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0,4))
            sage: A == LeeBrickellISDAlgorithm(C, (0,4))
            True
            sage: A == LeeBrickellISDAlgorithm(C, (0,5))
            False
            sage: other_search = 1 if A.parameters()['search_size'] != 1 else 2
            sage: A == LeeBrickellISDAlgorithm(C, (0,4), search_size=other_search)
            False

        ISD Algorithm objects can be equal only if they have both calibrated
        the parameters, or if they both had it set and to the same value::

            sage: A2 = LeeBrickellISDAlgorithm(C, (0,4), search_size=A.parameters()['search_size'])
            sage: A == A2
            False
            sage: A2 == LeeBrickellISDAlgorithm(C, (0,4), search_size=A.parameters()['search_size'])
            True
        """
    def __hash__(self):
        """
        Return the hash value of ``self``.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0,4))
            sage: hash(A) #random
            5884357732955478461
            sage: C2 = codes.GolayCode(GF(3))
            sage: A2 = LeeBrickellISDAlgorithm(C2, (0,4))
            sage: hash(A) != hash(A2)
            True
        """

class LeeBrickellISDAlgorithm(InformationSetAlgorithm):
    """
    The Lee-Brickell algorithm for information-set decoding.

    For a description of the information-set decoding paradigm (ISD), see
    :class:`sage.coding.information_set_decoder.LinearCodeInformationSetDecoder`.

    This implements the Lee-Brickell variant of ISD, see [LB1988]_ for the
    original binary case, and [Pet2010]_ for the `q`-ary extension.

    Let `C` be a `[n, k]`-linear code over `\\GF{q}`, and let `r \\in \\GF{q}^{n}` be
    a received word in a transmission. We seek the codeword whose Hamming
    distance from `r` is minimal. Let `p` and `w` be integers, such that `0\\leq
    p\\leq w`, Let `G` be a generator matrix of `C`, and for any set of indices
    `I`, we write `G_{I}` for the matrix formed by the columns of `G` indexed by
    `I`. The Lee-Brickell ISD loops the following until it is successful:

        1. Choose an information set `I` of `C`.
        2. Compute `r' = r - r_{I} G_I^{-1}  G`
        3. Consider every size-`p` subset of `I`, `\\{a_1, \\dots, a_p\\}`.
           For each `m = (m_1, \\dots, m_p) \\in \\GF{q}^{p}`, compute
           the error vector `e = r' - \\sum_{i=1}^{p} m_i g_{a_i}`,
        4. If `e` has a Hamming weight at most `w`, return `r-e`.

    INPUT:

    - ``code`` -- a linear code for which to decode

    - ``decoding_interval`` -- a pair of integers specifying an interval of
      number of errors to correct; includes both end values

    - ``search_size`` -- (optional) the size of subsets to use on step 3 of the
      algorithm as described above. Usually a small number. It has to be at most
      the largest allowed number of errors. A good choice will be approximated
      if this option is not set; see
      :meth:`sage.coding.LeeBrickellISDAlgorithm.calibrate`
      for details.

    EXAMPLES::

        sage: C = codes.GolayCode(GF(2))
        sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
        sage: A = LeeBrickellISDAlgorithm(C, (0,4)); A
        ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2)
         decoding up to 4 errors

        sage: C = codes.GolayCode(GF(2))
        sage: A = LeeBrickellISDAlgorithm(C, (2,3)); A
        ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2)
         decoding between 2 and 3 errors
    """
    def __init__(self, code, decoding_interval, search_size=None) -> None:
        """
        TESTS:

        If ``search_size`` is not a positive integer, or is bigger than the
        decoding radius, an error will be raised::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: LeeBrickellISDAlgorithm(C, (1, 3), search_size=-1)
            Traceback (most recent call last):
            ...
            ValueError: The search size parameter has to be a positive integer

            sage: LeeBrickellISDAlgorithm(C, (1, 3), search_size=4)
            Traceback (most recent call last):
            ...
            ValueError: The search size parameter has to be at most the maximal number of allowed errors
        """
    def decode(self, r):
        """
        The Lee-Brickell algorithm as described in the class doc.

        Note that either parameters must be given at construction time or
        :meth:`sage.coding.information_set_decoder.InformationSetAlgorithm.calibrate()`
        should be called before calling this method.

        INPUT:

        - ``r`` -- a received word, i.e. a vector in the ambient space of
          :meth:`decoder.Decoder.code`

        OUTPUT: a codeword whose distance to `r` satisfies ``self.decoding_interval()``.

        EXAMPLES::

            sage: M = matrix(GF(2), [[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],\\\n            ....:                    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],\\\n            ....:                    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],\\\n            ....:                    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],\\\n            ....:                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]])
            sage: C = codes.LinearCode(M)
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (2,2))
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(), 2)
            sage: r = Chan(c)
            sage: c_out = A.decode(r)
            sage: (r - c).hamming_weight() == 2
            True
        """
    def calibrate(self):
        """
        Run some test computations to estimate the optimal search size.

        Let `p` be the search size. We should simply choose `p` such that the
        average expected time is minimal. The algorithm succeeds when it chooses
        an information set with at least `k - p` correct positions, where `k` is
        the dimension of the code and `p` the search size. The expected number
        of trials we need before this occurs is:

        .. MATH::

            \\binom{n}{k}/(\\rho \\sum_{i=0}^p \\binom{n-\\tau}{k-i} \\binom{\\tau}{i})

        Here `\\rho` is the fraction of `k` subsets of indices which are
        information sets. If `T` is the average time for steps 1 and 2
        (including selecting `I` until an information set is found), while `P(i)`
        is the time for the body of the ``for``-loop in step 3 for `m` of weight
        `i`, then each information set trial takes roughly time `T +
        \\sum_{i=0}^{p} P(i) \\binom{k}{i} (q-1)^i`, where `\\GF{q}` is the base
        field.

        The values `T` and `P` are here estimated by running a few test
        computations similar to those done by the decoding algorithm.
        We don't explicitly estimate `\\rho`.

        OUTPUT: does not output anything but sets private fields used by
        :meth:`sage.coding.information_set_decoder.InformationSetAlgorithm.parameters()`
        and
        :meth:`sage.coding.information_set_decoder.InformationSetAlgorithm.time_estimate()`.

        EXAMPLES::

            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: C = codes.GolayCode(GF(2))
            sage: A = LeeBrickellISDAlgorithm(C, (0,3)); A
            ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2)
             decoding up to 3 errors
            sage: A.calibrate()
            sage: A.parameters() #random
            {'search_size': 1}
            sage: A.time_estimate() #random
            0.0008162108571427874

        If we specify the parameter at construction time, calibrate does not override this choice::

            sage: A = LeeBrickellISDAlgorithm(C, (0,3), search_size=2); A
            ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2)
             decoding up to 3 errors
            sage: A.parameters()
            {'search_size': 2}
            sage: A.calibrate()
            sage: A.parameters()
            {'search_size': 2}
            sage: A.time_estimate() #random
            0.0008162108571427874
        """

class LinearCodeInformationSetDecoder(Decoder):
    '''
    Information-set decoder for any linear code.

    Information-set decoding is a probabilistic decoding strategy that
    essentially tries to guess `k` correct positions in the received word,
    where `k` is the dimension of the code. A codeword agreeing with the
    received word on the guessed position can easily be computed, and their
    difference is one possible error vector. A "correct" guess is assumed when
    this error vector has low Hamming weight.

    The ISD strategy requires choosing how many errors is deemed acceptable. One
    choice could be `d/2`, where `d` is the minimum distance of the code, but
    sometimes `d` is not known, or sometimes more errors are expected. If one
    chooses anything above `d/2`, the algorithm does not guarantee to return a
    nearest codeword.

    This simple algorithm is not very efficient in itself, but there are numerous
    refinements to the strategy. Specifying which strategy to use among those
    that Sage knows is done using the ``algorithm`` keyword. If this is not set,
    an efficient choice will be made for you.

    The various ISD algorithms all need to select a number of parameters. If you
    choose a specific algorithm to use, you can pass these parameters as named
    parameters directly to this class\' constructor. If you don\'t, efficient
    choices will be calibrated for you.

    .. WARNING::

        If there is no codeword within the specified decoding distance, then the
        decoder may never terminate, or it may raise a
        :exc:`sage.coding.decoder.DecodingError` exception, depending on the ISD
        algorithm used.

    INPUT:

    - ``code`` -- a linear code for which to decode

    - ``number_errors`` -- integer; the maximal number of errors to accept as
      correct decoding. An interval can also be specified by giving a pair of
      integers, where both end values are taken to be in the interval.

    - ``algorithm`` -- (optional) the string name of the ISD algorithm to
      employ. If this is not set, an appropriate one will be chosen.
      A constructed
      :class:`sage.coding.information_set_decoder.InformationSetAlgorithm`
      object may also be given. In this case ``number_errors`` must match that
      of the passed algorithm.

    - ``**kwargs`` -- (optional) any number of named arguments passed on to the
      ISD algorithm. Such are usually not required, and they can only be set if
      ``algorithm`` is set to a specific algorithm. See the documentation for
      each individual ISD algorithm class for information on any named arguments
      they may accept. The easiest way to access this documentation is to first
      construct the decoder without passing any named arguments, then accessing
      the ISD algorithm using
      :meth:`sage.coding.information_set_decoder.LinearCodeInformationSetDecoder.algorithm`,
      and then reading the `?` help on the constructed object.

    EXAMPLES:

    The principal way to access this class is through the
    :meth:`sage.code.linear_code.AbstractLinearCode.decoder` method::

        sage: C = codes.GolayCode(GF(3))
        sage: D = C.decoder(\'InformationSet\', 2); D
        Information-set decoder (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors

    You can specify which algorithm you wish to use, and you should do so in
    order to pass special parameters to it::

        sage: C = codes.GolayCode(GF(3))
        sage: D2 = C.decoder(\'InformationSet\', 2, algorithm=\'Lee-Brickell\', search_size=2); D2
        Information-set decoder (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors
        sage: D2.algorithm()
        ISD Algorithm (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors
        sage: D2.algorithm().parameters()
        {\'search_size\': 2}

    If you specify an algorithm which is not known, you get a friendly error message::

        sage: C.decoder(\'InformationSet\', 2, algorithm="NoSuchThing")
        Traceback (most recent call last):
        ...
        ValueError: Unknown ISD algorithm \'NoSuchThing\'.
        The known algorithms are [\'Lee-Brickell\'].

    You can also construct an ISD algorithm separately and pass that. This is
    mostly useful if you write your own ISD algorithms::

        sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
        sage: A = LeeBrickellISDAlgorithm(C, (0, 2))
        sage: D = C.decoder(\'InformationSet\', 2, algorithm=A); D
        Information-set decoder (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors

    When passing an already constructed ISD algorithm, you can\'t also pass
    parameters to the ISD algorithm when constructing the decoder::

        sage: C.decoder(\'InformationSet\', 2, algorithm=A, search_size=2)
        Traceback (most recent call last):
        ...
        ValueError: ISD algorithm arguments are not allowed
        when supplying a constructed ISD algorithm

    We can also information-set decode non-binary codes::

        sage: C = codes.GolayCode(GF(3))
        sage: D = C.decoder(\'InformationSet\', 2); D
        Information-set decoder (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors

    There are two other ways to access this class::

        sage: D = codes.decoders.LinearCodeInformationSetDecoder(C, 2); D
        Information-set decoder (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors

        sage: from sage.coding.information_set_decoder import LinearCodeInformationSetDecoder
        sage: D = LinearCodeInformationSetDecoder(C, 2); D
        Information-set decoder (Lee-Brickell) for [12, 6, 6] Extended Golay code over GF(3)
         decoding up to 2 errors
    '''
    def __init__(self, code, number_errors, algorithm=None, **kwargs) -> None:
        '''
        TESTS:

        ``number_errors`` has to be either a list of Integers/ints, a tuple of Integers/ints,
        or an Integer/int::

            sage: C = codes.GolayCode(GF(2))
            sage: D = C.decoder(\'InformationSet\', "aa")
            Traceback (most recent call last):
            ...
            ValueError: number_errors should be an integer or a pair of integers

        If ``number_errors`` is passed as a list/tuple, it has to contain only
        two values, the first one being at most the second one::

            sage: C = codes.GolayCode(GF(2))
            sage: D = C.decoder(\'InformationSet\', (4, 2))
            Traceback (most recent call last):
            ...
            ValueError: number_errors should be a positive integer or a valid interval within the positive integers

        You cannot ask the decoder to correct more errors than the code length::

            sage: D = C.decoder(\'InformationSet\', 25)
            Traceback (most recent call last):
            ...
            ValueError: The provided number of errors should be at most the code\'s length

        If ``algorithm`` is not set, additional parameters cannot be passed to
        the ISD algorithm::

            sage: D = C.decoder(\'InformationSet\', 2, search_size=2)
            Traceback (most recent call last):
            ...
            ValueError: Additional arguments to an information-set decoder algorithm are only allowed if a specific algorithm is selected by setting the algorithm keyword

        If ``algorithm`` is set to a constructed ISD algorithm, additional
        parameters cannot be passed to the ISD algorithm::

            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0, 2))
            sage: D = C.decoder(\'InformationSet\', 2, A, search_size=3)
            Traceback (most recent call last):
            ...
            ValueError: ISD algorithm arguments are not allowed when supplying a constructed ISD algorithm

        If ``algorithm`` is set to a constructed
        :class:`sage.coding.information_set_decoder.InformationSetAlgorithm`,
        then ``number_errors`` must match that of the algorithm::

            sage: C = codes.GolayCode(GF(2))
            sage: from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
            sage: A = LeeBrickellISDAlgorithm(C, (0, 2))
            sage: D = C.decoder(\'InformationSet\', 2, A); D
            Information-set decoder (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2) decoding up to 2 errors
            sage: D = C.decoder(\'InformationSet\', (0,2), A); D
            Information-set decoder (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2) decoding up to 2 errors
            sage: D = C.decoder(\'InformationSet\', 3, A); D
            Traceback (most recent call last):
            ...
            ValueError: number_errors must match that of the passed ISD algorithm
        '''
    @staticmethod
    def known_algorithms(dictionary: bool = False):
        """
        Return the list of ISD algorithms that Sage knows.

        Passing any of these to the constructor of
        :class:`sage.coding.information_set_decoder.LinearCodeInformationSetDecoder`
        will make the ISD decoder use that algorithm.

        INPUT:

        - ``dictionary`` -- boolean (default: ``False``); if set to ``True``,
          return a ``dict`` mapping decoding algorithm name to its class

        OUTPUT: list of strings or a ``dict`` from string to ISD algorithm class

        EXAMPLES::

            sage: from sage.coding.information_set_decoder import LinearCodeInformationSetDecoder
            sage: sorted(LinearCodeInformationSetDecoder.known_algorithms())
            ['Lee-Brickell']
        """
    def algorithm(self):
        '''
        Return the ISD algorithm used by this ISD decoder.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: D = C.decoder(\'InformationSet\', (2,4), "Lee-Brickell")
            sage: D.algorithm()
            ISD Algorithm (Lee-Brickell) for [24, 12, 8] Extended Golay code over GF(2)
             decoding between 2 and 4 errors
        '''
    def decode_to_code(self, r):
        """
        Decodes a received word with respect to the associated code of this decoder.

        .. WARNING::

            If there is no codeword within the decoding radius of this decoder, this
            method may never terminate, or it may raise a
            :exc:`sage.coding.decoder.DecodingError` exception, depending on the ISD
            algorithm used.

        INPUT:

        - ``r`` -- a vector in the ambient space of :meth:`decoder.Decoder.code`

        OUTPUT: a codeword of :meth:`decoder.Decoder.code`

        EXAMPLES::

            sage: M = matrix(GF(2), [[1,0,0,0,0,0,1,0,1,0,1,1,0,0,1],\\\n            ....:                    [0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],\\\n            ....:                    [0,0,1,0,0,0,0,1,0,1,1,1,1,1,0],\\\n            ....:                    [0,0,0,1,0,0,1,0,1,0,0,0,1,1,0],\\\n            ....:                    [0,0,0,0,1,0,0,0,1,0,1,1,0,1,0]])
            sage: C = LinearCode(M)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(), 2)
            sage: r = Chan(c)
            sage: D = C.decoder('InformationSet', 2)
            sage: c == D.decode_to_code(r)
            True

        Information-set decoding a non-binary code::

            sage: C = codes.GolayCode(GF(3)); C
            [12, 6, 6] Extended Golay code over GF(3)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(), 2)
            sage: r = Chan(c)
            sage: D = C.decoder('InformationSet', 2)
            sage: c == D.decode_to_code(r)
            True

        Let's take a bigger example, for which syndrome decoding or
        nearest-neighbor decoding would be infeasible: the `[59, 30]` Quadratic
        Residue code over `\\GF{3}` has true minimum distance 17, so we can
        correct 8 errors::

            sage: C = codes.QuadraticResidueCode(59, GF(3))
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(), 2)
            sage: r = Chan(c)
            sage: D = C.decoder('InformationSet', 8)
            sage: c == D.decode_to_code(r) # long time
            True
        """
    def decoding_radius(self):
        """
        Return the maximal number of errors this decoder can decode.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: D = C.decoder('InformationSet', 2)
            sage: D.decoding_radius()
            2
        """
    def decoding_interval(self):
        """
        A pair of integers specifying the interval of number of errors this
        decoder will attempt to correct.

        The interval includes both end values.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: D = C.decoder('InformationSet', 2)
            sage: D.decoding_interval()
            (0, 2)
        """
