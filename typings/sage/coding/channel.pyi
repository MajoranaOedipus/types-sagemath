from sage.arith.misc import binomial as binomial
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.prandom import randint as randint, random as random, sample as sample
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

def random_error_vector(n, F, error_positions):
    """
    Return a vector of length ``n`` over ``F`` filled with random nonzero coefficients
    at the positions given by ``error_positions``.

    .. NOTE::

        This is a helper function, which should only be used when implementing new channels.

    INPUT:

    - ``n`` -- the length of the vector

    - ``F`` -- the field over which the vector is defined

    - ``error_positions`` -- the nonzero positions of the vector

    OUTPUT: a vector of ``F``

    AUTHORS:

    This function is taken from codinglib (https://bitbucket.org/jsrn/codinglib/)
    and was written by Johan Nielsen.

    EXAMPLES::

        sage: from sage.coding.channel import random_error_vector
        sage: random_error_vector(5, GF(2), [1,3])
        (0, 1, 0, 1, 0)
    """
def format_interval(t):
    """
    Return a formatted string representation of ``t``.

    This method should be called by any representation function in Channel classes.

    .. NOTE::

        This is a helper function, which should only be used when implementing new channels.

    INPUT:

    - ``t`` -- list or a tuple

    OUTPUT: string

    TESTS::

        sage: from sage.coding.channel import format_interval
        sage: t = (5, 5)
        sage: format_interval(t)
        '5'

        sage: t = (2, 10)
        sage: format_interval(t)
        'between 2 and 10'
    """

class Channel(SageObject):
    """
    Abstract top-class for Channel objects.

    All channel objects must inherit from this class. To implement a channel subclass, one should
    do the following:

    - inherit from this class,

    - call the super constructor,

    - override :meth:`transmit_unsafe`.

    While not being mandatory, it might be useful to reimplement representation methods (``_repr_`` and
    ``_latex_``).

    This abstract class provides the following parameters:

    - ``input_space`` -- the space of the words to transmit

    - ``output_space`` -- the space of the transmitted words
    """
    def __init__(self, input_space, output_space) -> None:
        """
        Initialize parameters for a Channel object.

        This is a private method, which should be called by the constructor
        of every encoder, as it automatically initializes the mandatory
        parameters of a Channel object.

        INPUT:

        - ``input_space`` -- the space of the words to transmit

        - ``output_space`` -- the space of the transmitted words

        EXAMPLES:

        We first create a new Channel subclass::

            sage: from sage.coding.channel import Channel
            sage: class ChannelExample(Channel):
            ....:   def __init__(self, input_space, output_space):
            ....:       super().__init__(input_space, output_space)

        We now create a member of our newly made class::

            sage: input = VectorSpace(GF(7), 6)
            sage: output = VectorSpace(GF(7), 5)
            sage: Chan = ChannelExample(input, output)

        We can check its parameters::

            sage: Chan.input_space()
            Vector space of dimension 6 over Finite Field of size 7
            sage: Chan.output_space()
            Vector space of dimension 5 over Finite Field of size 7
        """
    def transmit(self, message):
        """
        Return ``message``, modified accordingly with the algorithm of the channel it was
        transmitted through.

        Checks if ``message`` belongs to the input space, and returns an exception if not.
        Note that ``message`` itself is never modified by the channel.

        INPUT:

        - ``message`` -- a vector

        OUTPUT: a vector of the output space of ``self``

        EXAMPLES::

            sage: F = GF(59)^6
            sage: n_err = 2
            sage: Chan = channels.StaticErrorRateChannel(F, n_err)
            sage: msg = F((4, 8, 15, 16, 23, 42))
            sage: set_random_seed(10)
            sage: Chan.transmit(msg)
            (4, 8, 4, 16, 23, 53)

        We can check that the input ``msg`` is not modified::

            sage: msg
            (4, 8, 15, 16, 23, 42)

        If we transmit a vector which is not in the input space of ``self``::

            sage: n_err = 2
            sage: Chan = channels.StaticErrorRateChannel(GF(59)^6, n_err)
            sage: msg = (4, 8, 15, 16, 23, 42)
            sage: Chan.transmit(msg)
            Traceback (most recent call last):
            ...
            TypeError: Message must be an element of the input space for the given channel

        .. NOTE::

            One can also call directly ``Chan(message)``, which does the same as ``Chan.transmit(message)``
        """
    __call__ = transmit
    def input_space(self):
        """
        Return the input space of ``self``.

        EXAMPLES::

            sage: n_err = 2
            sage: Chan = channels.StaticErrorRateChannel(GF(59)^6, n_err)
            sage: Chan.input_space()
            Vector space of dimension 6 over Finite Field of size 59
        """
    def output_space(self):
        """
        Return the output space of ``self``.

        EXAMPLES::

            sage: n_err = 2
            sage: Chan = channels.StaticErrorRateChannel(GF(59)^6, n_err)
            sage: Chan.output_space()
            Vector space of dimension 6 over Finite Field of size 59
        """
    @abstract_method
    def transmit_unsafe(self, message) -> None:
        """
        Return ``message``, modified accordingly with the algorithm of the channel it was
        transmitted through.

        This method does not check if ``message`` belongs to the input space of ``self``.

        This is an abstract method which should be reimplemented in all the subclasses of
        Channel.

        EXAMPLES::

            sage: n_err = 2
            sage: Chan = channels.StaticErrorRateChannel(GF(59)^6, n_err)
            sage: v = Chan.input_space().random_element()
            sage: Chan.transmit_unsafe(v)  # random
            (1, 33, 46, 18, 20, 49)
        """

class StaticErrorRateChannel(Channel):
    """
    Channel which adds a static number of errors to each message it transmits.

    The input space and the output space of this channel are the same.

    INPUT:

    - ``space`` -- the space of both input and output

    - ``number_errors`` -- the number of errors added to each transmitted message
      It can be either an integer of a tuple. If a tuple is passed as
      argument, the number of errors will be a random integer between the
      two bounds of the tuple.

    EXAMPLES:

    We construct a :class:`StaticErrorRateChannel` which adds 2 errors
    to any transmitted message::

        sage: n_err = 2
        sage: Chan = channels.StaticErrorRateChannel(GF(59)^40, n_err)
        sage: Chan
        Static error rate channel creating 2 errors, of input and output space
        Vector space of dimension 40 over Finite Field of size 59

    We can also pass a tuple for the number of errors::

        sage: n_err = (1, 10)
        sage: Chan = channels.StaticErrorRateChannel(GF(59)^40, n_err)
        sage: Chan
        Static error rate channel creating between 1 and 10 errors,
        of input and output space Vector space of dimension 40 over Finite Field of size 59
    """
    def __init__(self, space, number_errors) -> None:
        """
        TESTS:

        If the number of errors exceeds the dimension of the input space,
        it will return an error::

            sage: n_err = 42
            sage: Chan = channels.StaticErrorRateChannel(GF(59)^40, n_err)
            Traceback (most recent call last):
            ...
            ValueError: There might be more errors than the dimension of the input space
        """
    def transmit_unsafe(self, message):
        """
        Return ``message`` with as many errors as ``self._number_errors`` in it.

        If ``self._number_errors`` was passed as a tuple for the number of errors, it will
        pick a random integer between the bounds of the tuple and use it as the number of errors.

        This method does not check if ``message`` belongs to the input space of ``self``.

        INPUT:

        - ``message`` -- a vector

        OUTPUT: a vector of the output space

        EXAMPLES::

            sage: F = GF(59)^6
            sage: n_err = 2
            sage: Chan = channels.StaticErrorRateChannel(F, n_err)
            sage: msg = F((4, 8, 15, 16, 23, 42))
            sage: set_random_seed(10)
            sage: Chan.transmit_unsafe(msg)
            (4, 8, 4, 16, 23, 53)

        This checks that :issue:`19863` is fixed::

            sage: V = VectorSpace(GF(2), 1000)
            sage: Chan = channels.StaticErrorRateChannel(V, 367)
            sage: c = V.random_element()
            sage: (c - Chan(c)).hamming_weight()
            367
        """
    def number_errors(self):
        """
        Return the number of errors created by ``self``.

        EXAMPLES::

            sage: n_err = 3
            sage: Chan = channels.StaticErrorRateChannel(GF(59)^6, n_err)
            sage: Chan.number_errors()
            (3, 3)
        """

class ErrorErasureChannel(Channel):
    """
    Channel which adds errors and erases several positions in any message it transmits.

    The output space of this channel is a Cartesian product between its input
    space and a VectorSpace of the same dimension over `\\GF{2}`.

    INPUT:

    - ``space`` -- the input and output space

    - ``number_errors`` -- the number of errors created in each transmitted
      message. It can be either an integer of a tuple. If a tuple is passed as
      an argument, the number of errors will be a random integer between the
      two bounds of this tuple.

    - ``number_erasures`` -- the number of erasures created in each transmitted
      message. It can be either an integer of a tuple. If a tuple is passed as an
      argument, the number of erasures will be a random integer between the
      two bounds of this tuple.

    EXAMPLES:

    We construct a ErrorErasureChannel which adds 2 errors
    and 2 erasures to any transmitted message::

        sage: n_err, n_era = 2, 2
        sage: Chan = channels.ErrorErasureChannel(GF(59)^40, n_err, n_era)
        sage: Chan
        Error-and-erasure channel creating 2 errors and 2 erasures
        of input space Vector space of dimension 40 over Finite Field of size 59
        and output space The Cartesian product of (Vector space of dimension 40
        over Finite Field of size 59, Vector space of dimension 40 over Finite Field of size 2)

    We can also pass the number of errors and erasures as a couple of integers::

        sage: n_err, n_era = (1, 10), (1, 10)
        sage: Chan = channels.ErrorErasureChannel(GF(59)^40, n_err, n_era)
        sage: Chan
        Error-and-erasure channel creating between 1 and 10 errors and
        between 1 and 10 erasures of input space Vector space of dimension 40
        over Finite Field of size 59 and output space The Cartesian product of
        (Vector space of dimension 40 over Finite Field of size 59,
        Vector space of dimension 40 over Finite Field of size 2)
    """
    def __init__(self, space, number_errors, number_erasures) -> None:
        """
        TESTS:

        If the sum of number of errors and number of erasures
        exceeds (or may exceed, in the case of tuples) the dimension of the input space,
        it will return an error::

            sage: n_err, n_era = 21, 21
            sage: Chan = channels.ErrorErasureChannel(GF(59)^40, n_err, n_era)
            Traceback (most recent call last):
            ...
            ValueError: The total number of errors and erasures cannot exceed the dimension of the input space
        """
    def transmit_unsafe(self, message):
        """
        Return ``message`` with as many errors as ``self._number_errors`` in it,
        and as many erasures as ``self._number_erasures`` in it.

        If ``self._number_errors`` was passed as a tuple for the number of errors, it will
        pick a random integer between the bounds of the tuple and use it as the number of errors.
        It does the same with ``self._number_erasures``.

        All erased positions are set to 0 in the transmitted message.
        It is guaranteed that the erasures and the errors will never overlap:
        the received message will always contains exactly as many errors and erasures
        as expected.

        This method does not check if ``message`` belongs to the input space of ``self``.

        INPUT:

        - ``message`` -- a vector

        OUTPUT: a couple of vectors, namely:

          - the transmitted message, which is ``message`` with erroneous and
            erased positions
          - the erasure vector, which contains ``1`` at the erased positions of
            the transmitted message and ``0`` elsewhere.

        EXAMPLES::

            sage: F = GF(59)^11
            sage: n_err, n_era = 2, 2
            sage: Chan = channels.ErrorErasureChannel(F, n_err, n_era)
            sage: msg = F((3, 14, 15, 9, 26, 53, 58, 9, 7, 9, 3))
            sage: set_random_seed(10)
            sage: Chan.transmit_unsafe(msg)
            ((31, 0, 15, 9, 38, 53, 58, 9, 0, 9, 3), (0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0))
        """
    def number_errors(self):
        """
        Return the number of errors created by ``self``.

        EXAMPLES::

            sage: n_err, n_era = 3, 0
            sage: Chan = channels.ErrorErasureChannel(GF(59)^6, n_err, n_era)
            sage: Chan.number_errors()
            (3, 3)
        """
    def number_erasures(self):
        """
        Return the number of erasures created by ``self``.

        EXAMPLES::

            sage: n_err, n_era = 0, 3
            sage: Chan = channels.ErrorErasureChannel(GF(59)^6, n_err, n_era)
            sage: Chan.number_erasures()
            (3, 3)
        """

class QarySymmetricChannel(Channel):
    '''
    The `q`-ary symmetric, memoryless communication channel.

    Given an alphabet `\\Sigma` with `|\\Sigma| = q` and an error probability
    `\\epsilon`, a `q`-ary symmetric channel sends an element of `\\Sigma` into the
    same element with probability `1 - \\epsilon`, and any one of the other `q -
    1` elements with probability `\\frac{\\epsilon}{q - 1}`. This implementation
    operates over vectors in `\\Sigma^n`, and "transmits" each element of the
    vector independently in the above manner.

    Though `\\Sigma` is usually taken to be a finite field, this implementation
    allows any structure for which Sage can represent `\\Sigma^n` and for which
    `\\Sigma` has a ``random_element()`` method. However, beware that if `\\Sigma`
    is infinite, errors will not be uniformly distributed (since
    ``random_element()`` does not draw uniformly at random).

    The input space and the output space of this channel are the same:
    `\\Sigma^n`.

    INPUT:

    - ``space`` -- the input and output space of the channel; it has to be
      `\\GF{q}^n` for some finite field `\\GF{q}`

    - ``epsilon`` -- the transmission error probability of the individual elements

    EXAMPLES:

    We construct a :class:`QarySymmetricChannel` which corrupts 30% of all
    transmitted symbols::

        sage: epsilon = 0.3
        sage: Chan = channels.QarySymmetricChannel(GF(59)^50, epsilon)
        sage: Chan
        q-ary symmetric channel with error probability 0.300000000000000,
         of input and output space
          Vector space of dimension 50 over Finite Field of size 59
    '''
    def __init__(self, space, epsilon) -> None:
        """
        TESTS:

        If ``space`` is not a vector space, an error is raised::

            sage: epsilon = 0.42
            sage: Chan = channels.QarySymmetricChannel(GF(59), epsilon)
            Traceback (most recent call last):
            ...
            ValueError: space has to be of the form Sigma^n, where Sigma has a random_element() method

        If ``epsilon`` is not between 0 and 1, an error is raised::

            sage: epsilon = 42
            sage: Chan = channels.QarySymmetricChannel(GF(59)^50, epsilon)
            Traceback (most recent call last):
            ...
            ValueError: Error probability must be between 0 and 1
        """
    def transmit_unsafe(self, message):
        """
        Return ``message`` where each of the symbols has been changed to another from the alphabet with
        probability :meth:`error_probability`.

        This method does not check if ``message`` belongs to the input space of ``self``.

        INPUT:

        - ``message`` -- a vector

        EXAMPLES::

            sage: F = GF(59)^11
            sage: epsilon = 0.3
            sage: Chan = channels.QarySymmetricChannel(F, epsilon)
            sage: msg = F((3, 14, 15, 9, 26, 53, 58, 9, 7, 9, 3))
            sage: set_random_seed(10)
            sage: Chan.transmit_unsafe(msg)
            (3, 14, 15, 53, 12, 53, 58, 9, 55, 9, 3)
        """
    def error_probability(self):
        """
        Return the error probability of a single symbol transmission of
        ``self``.

        EXAMPLES::

            sage: epsilon = 0.3
            sage: Chan = channels.QarySymmetricChannel(GF(59)^50, epsilon)
            sage: Chan.error_probability()
            0.300000000000000
        """
    def probability_of_exactly_t_errors(self, t):
        """
        Return the probability ``self`` has to return
        exactly ``t`` errors.

        INPUT:

        - ``t`` -- integer

        EXAMPLES::

            sage: epsilon = 0.3
            sage: Chan = channels.QarySymmetricChannel(GF(59)^50, epsilon)
            sage: Chan.probability_of_exactly_t_errors(15)
            0.122346861835401
        """
    def probability_of_at_most_t_errors(self, t):
        """
        Return the probability ``self`` has to return
        at most ``t`` errors.

        INPUT:

        - ``t`` -- integer

        EXAMPLES::

            sage: epsilon = 0.3
            sage: Chan = channels.QarySymmetricChannel(GF(59)^50, epsilon)
            sage: Chan.probability_of_at_most_t_errors(20)
            0.952236164579467
        """
