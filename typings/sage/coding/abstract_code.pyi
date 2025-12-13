from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.sageinspect import sage_getargspec as sage_getargspec
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent

class AbstractCode(Parent):
    '''
    Abstract class for codes.

    This class contains all the methods that can be used on any code
    and on any code family. As opposed to
    :class:`sage.coding.linear_code.AbstractLinearCode`, this class makes no
    assumptions about linearity, metric, finiteness or the number of alphabets.

    The abstract notion of "code" that is implicitly used for this class is any
    enumerable subset of a cartesian product `A_1 \\times A_2 \\times \\ldots
    \\times A_n` for some sets `A_i`. Note that this class makes no attempt to
    directly represent the code in this fashion, allowing subclasses to make the
    appropriate choices. The notion of metric is also not mathematically
    enforced in any way, and is simply stored as a string value.

    Every code-related class should inherit from this abstract class.

    To implement a code, you need to:

    - inherit from :class:`AbstractCode`

    - call :class:`AbstractCode` ``__init__`` method in the subclass constructor.
      Example: ``super().__init__(length, "EncoderName",
      "DecoderName", "metric")``. "EncoderName" and "DecoderName" are set to
      ``None`` by default, a generic code class such as AbstractCode does
      not necessarily have to have general encoders/decoders. However, if you
      want to use the encoding/decoding methods, you have to add these.

    - since this class does not specify any category, it is highly recommended
      to set up the category framework in the subclass. To do this, use the
      ``Parent.__init__(self, base, facade, category)`` function in the subclass
      constructor. A good example is in
      :class:`sage.coding.linear_code.AbstractLinearCode`.

    - it is also recommended to override the ``ambient_space`` method, which is
      required by ``__call__``

    - to use the encoder/decoder framework, one has to set up the category and
      related functions ``__iter__`` and ``__contains__``. A good example is in
      :class:`sage.coding.linear_code.AbstractLinearCode`.

    - add the following two lines on the class level::

          _registered_encoders = {}
          _registered_decoders = {}


    - fill the dictionary of its encoders in ``sage.coding.__init__.py`` file.
      Example: I want to link the encoder ``MyEncoderClass`` to ``MyNewCodeClass``
      under the name ``MyEncoderName``.
      All I need to do is to write this line in the ``__init__.py`` file:
      ``MyNewCodeClass._registered_encoders["NameOfMyEncoder"] = MyEncoderClass``
      and all instances of ``MyNewCodeClass`` will be able to use instances of
      ``MyEncoderClass``.

    - fill the dictionary of its decoders in ``sage.coding.__init__`` file.
      Example: I want to link the encoder ``MyDecoderClass`` to ``MyNewCodeClass``
      under the name ``MyDecoderName``.
      All I need to do is to write this line in the ``__init__.py`` file:
      ``MyNewCodeClass._registered_decoders["NameOfMyDecoder"] = MyDecoderClass``
      and all instances of ``MyNewCodeClass`` will be able to use instances of
      ``MyDecoderClass``.


    As the class :class:`AbstractCode` is not designed to be instantiated, it
    does not have any representation methods. You should implement ``_repr_``
    and ``_latex_`` methods in the subclass.
    '''
    def __init__(self, length, default_encoder_name=None, default_decoder_name=None, metric: str = 'Hamming') -> None:
        '''
        Initialize mandatory parameters that any code shares.

        This method only exists for inheritance purposes as it initializes
        parameters that need to be known by every code. The class
        :class:`sage.coding.abstract_code.AbstractCode` should never be
        directly instantiated.

        INPUT:

        - ``length`` -- the length of ``self`` (a Python int or a Sage Integer,
          must be > 0)

        - ``default_encoder_name`` -- (default: ``None``) the name of
          the default encoder of ``self``

        - ``default_decoder_name`` -- (default: ``None``) the name of
          the default decoder of ``self``

        - ``metric`` -- (default: ``Hamming``) the name of the metric of ``self``

        EXAMPLES:

        The following example demonstrates how to use a subclass of ``AbstractCode``
        for representing a new family of codes::

            sage: from sage.coding.abstract_code import AbstractCode
            sage: class MyCodeFamily(AbstractCode):
            ....:   def __init__(self, length):
            ....:       super().__init__(length)
            ....:   def __iter__(self):
            ....:       for i in range(self.length() + 1):
            ....:            yield vector([1 for j in range(i)] + [0 for k in range(i, self.length())])
            ....:   def __contains__(self, word):
            ....:       return word in list(self)
            ....:   def _repr_(self):
            ....:       return "Dummy code of length {}".format(self.length())

        We now instantiate a member of our newly made code family::

            sage: C = MyCodeFamily(6)

        We can check its existence and parameters::

            sage: C
            Dummy code of length 6

        We can list its elements and check if an element is in the code::

            sage: list(C)
            [(0, 0, 0, 0, 0, 0),
            (1, 0, 0, 0, 0, 0),
            (1, 1, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 0),
            (1, 1, 1, 1, 0, 0),
            (1, 1, 1, 1, 1, 0),
            (1, 1, 1, 1, 1, 1)]
            sage: vector((0, 1, 0, 0, 0, 1)) in C
            False
            sage: vector((1, 1, 1, 0, 0, 0)) in C
            True

        And coming from AbstractCode code::

            sage: C.metric()
            \'Hamming\'

        TESTS:

        If the length field is neither a Python int nor a Sage Integer, it will
        raise a exception::

            sage: C = MyCodeFamily(10.0)
            Traceback (most recent call last):
            ...
            ValueError: length must be a Python int or a Sage Integer

        If the length of the code is not a nonzero positive integer
        (See :issue:`21326`), it will raise an exception::

            sage: C = MyCodeFamily(0)
            Traceback (most recent call last):
            ...
            ValueError: length must be a nonzero positive integer
        '''
    def __iter__(self):
        """
        Return an error message requiring to override ``__iter__`` in ``self``.

        As one has to implement specific category related methods (``__iter__`` and
        ``__contains__``) when writing a new code class which inherits from
        :class:`AbstractCode`, the generic call to ``__iter__`` has to fail.

        EXAMPLES:

        We create a new code class::

            sage: from sage.coding.abstract_code import AbstractCode
            sage: class MyCode(AbstractCode):
            ....:    def __init__(self):
            ....:        super().__init__(10)

        We check we get a sensible error message while asking for an
        iterator over the elements of our new class::

            sage: C = MyCode()
            sage: list(C)
            Traceback (most recent call last):
            ...
            RuntimeError: Please override __iter__ in the implementation of <class '__main__.MyCode'>
        """
    def __contains__(self, c) -> bool:
        """
        Return an error message requiring to override ``__contains__`` in ``self``.

        As one has to implement specific category related methods (``__iter__`` and
        ``__contains__``) when writing a new code class which inherits from
        :class:`AbstractCode`, the generic call to ``__contains__`` has to fail.

        EXAMPLES:

        We create a new code class::

            sage: from sage.coding.abstract_code import AbstractCode
            sage: class MyCode(AbstractCode):
            ....:    def __init__(self, length):
            ....:        super().__init__(length)

        We check we get a sensible error message while asking if an element is
        in our new class::

            sage: C = MyCode(3)
            sage: vector((1, 0, 0, 0, 0, 1, 1)) in C
            Traceback (most recent call last):
            ...
            RuntimeError: Please override __contains__ in the implementation of <class '__main__.MyCode'>
        """
    def ambient_space(self) -> None:
        """
        Return an error stating ``ambient_space`` of ``self`` is not implemented.

        This method is required by :meth:`__call__`.

        EXAMPLES::

            sage: from sage.coding.abstract_code import AbstractCode
            sage: class MyCode(AbstractCode):
            ....:    def __init__(self, length):
            ....:        super().__init__(length)
            sage: C = MyCode(3)
            sage: C.ambient_space()
            Traceback (most recent call last):
            ...
            NotImplementedError: No ambient space implemented for this code.
        """
    def __call__(self, m):
        """
        Return either ``m`` if it is a codeword or ``self.encode(m)``
        if it is an element of the message space of the encoder used by
        ``encode``.

        This implementation depends on :meth:`ambient_space`.

        INPUT:

        - ``m`` -- a vector whose length equals to code's length or an element
          of the message space used by ``encode``

        - ``**kwargs`` -- extra arguments are forwarded to ``encode``

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: word = vector((0, 1, 1, 0))
            sage: C(word)
            (1, 1, 0, 0, 1, 1, 0)

            sage: c = C.random_element()
            sage: C(c) == c
            True

        TESTS:

        If one passes a vector which belongs to the ambient space, it has to be a codeword.
        Otherwise, an exception is raised::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[0,1,0,1,0,1,0],[1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: word = vector((0, 1, 1, 0, 0, 1, 0))
            sage: C(word)
            Traceback (most recent call last):
            ...
            ValueError: If the input is a vector which belongs to the ambient space, it has to be a codeword
        """
    def list(self):
        """
        Return a list of all elements of this code.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: Clist = C.list()
            sage: Clist[5]; Clist[5] in C
            (1, 0, 1, 0, 1, 0, 1)
            True
        """
    def length(self):
        """
        Return the length of this code.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.length()
            7
        """
    def metric(self):
        """
        Return the metric of ``self``.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(2), 3)
            sage: C.metric()
            'Hamming'
        """
    def add_decoder(self, name, decoder) -> None:
        '''
        Add an decoder to the list of registered decoders of ``self``.

        .. NOTE::

            This method only adds ``decoder`` to ``self``, and not to any member of the class
            of ``self``. To know how to add an :class:`sage.coding.decoder.Decoder`, please refer
            to the documentation of :class:`AbstractCode`.

        INPUT:

        - ``name`` -- the string name for the decoder

        - ``decoder`` -- the class name of the decoder

        EXAMPLES:

        First of all, we create a (very basic) new decoder::

            sage: class MyDecoder(sage.coding.decoder.Decoder):
            ....:   def __init__(self, code):
            ....:       super().__init__(code)
            ....:   def _repr_(self):
            ....:       return "MyDecoder decoder with associated code %s" % self.code()

        We now create a new code::

            sage: C = codes.HammingCode(GF(2), 3)

        We can add our new decoder to the list of available decoders of C::

            sage: C.add_decoder("MyDecoder", MyDecoder)
            sage: sorted(C.decoders_available())
            [\'InformationSet\', \'MyDecoder\', \'NearestNeighbor\', \'Syndrome\']

        We can verify that any new code will not know MyDecoder::

            sage: C2 = codes.HammingCode(GF(2), 3)
            sage: sorted(C2.decoders_available())
            [\'InformationSet\', \'NearestNeighbor\', \'Syndrome\']

        TESTS:

        It is impossible to use a name which is in the dictionary of available decoders::

            sage: C.add_decoder("Syndrome", MyDecoder)
            Traceback (most recent call last):
            ...
            ValueError: There is already a registered decoder with this name
        '''
    def add_encoder(self, name, encoder) -> None:
        '''
        Add an encoder to the list of registered encoders of ``self``.

        .. NOTE::

            This method only adds ``encoder`` to ``self``, and not to any member of the class
            of ``self``. To know how to add an :class:`sage.coding.encoder.Encoder`, please refer
            to the documentation of :class:`AbstractCode`.

        INPUT:

        - ``name`` -- the string name for the encoder

        - ``encoder`` -- the class name of the encoder

        EXAMPLES:

        First of all, we create a (very basic) new encoder::

            sage: class MyEncoder(sage.coding.encoder.Encoder):
            ....:   def __init__(self, code):
            ....:       super().__init__(code)
            ....:   def _repr_(self):
            ....:       return "MyEncoder encoder with associated code %s" % self.code()

        We now create a new code::

            sage: C = codes.HammingCode(GF(2), 3)

        We can add our new encoder to the list of available encoders of C::

            sage: C.add_encoder("MyEncoder", MyEncoder)
            sage: sorted(C.encoders_available())
            [\'MyEncoder\', \'Systematic\']

        We can verify that any new code will not know MyEncoder::

            sage: C2 = codes.HammingCode(GF(2), 3)
            sage: sorted(C2.encoders_available())
            [\'Systematic\']

        TESTS:

        It is impossible to use a name which is in the dictionary of available encoders::

            sage: C.add_encoder("Systematic", MyEncoder)
            Traceback (most recent call last):
            ...
            ValueError: There is already a registered encoder with this name
        '''
    def decode_to_code(self, word, decoder_name=None, *args, **kwargs):
        """
        Correct the errors in ``word`` and returns a codeword.

        INPUT:

        - ``word`` -- an element in the ambient space as ``self``

        - ``decoder_name`` -- (default: ``None``) name of the decoder which will be used
          to decode ``word``. The default decoder of ``self`` will be used if
          default value is kept.

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to :meth:`decoder`

        OUTPUT: a vector of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: word = vector(GF(2), (1, 1, 0, 0, 1, 1, 0))
            sage: w_err = word + vector(GF(2), (1, 0, 0, 0, 0, 0, 0))
            sage: C.decode_to_code(w_err)
            (1, 1, 0, 0, 1, 1, 0)

        It is possible to manually choose the decoder amongst the list of the available ones::

            sage: sorted(C.decoders_available())
            ['InformationSet', 'NearestNeighbor', 'Syndrome']
            sage: C.decode_to_code(w_err, 'NearestNeighbor')
            (1, 1, 0, 0, 1, 1, 0)
        """
    def decode_to_message(self, word, decoder_name=None, *args, **kwargs):
        """
        Correct the errors in word and decodes it to the message space.

        INPUT:

        - ``word`` -- an element in the ambient space as ``self``

        - ``decoder_name`` -- (default: ``None``) name of the decoder which will be used
          to decode ``word``. The default decoder of ``self`` will be used if
          default value is kept.

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to :meth:`decoder`

        OUTPUT: a vector of the message space of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: word = vector(GF(2), (1, 1, 0, 0, 1, 1, 0))
            sage: C.decode_to_message(word)
            (0, 1, 1, 0)

        It is possible to manually choose the decoder amongst the list of the available ones::

            sage: sorted(C.decoders_available())
            ['InformationSet', 'NearestNeighbor', 'Syndrome']
            sage: C.decode_to_message(word, 'NearestNeighbor')
            (0, 1, 1, 0)
        """
    @cached_method
    def decoder(self, decoder_name=None, *args, **kwargs):
        '''
        Return a decoder of ``self``.

        INPUT:

        - ``decoder_name`` -- (default: ``None``) name of the decoder which will be
          returned. The default decoder of ``self`` will be used if
          default value is kept.

        - ``args``, ``kwargs`` -- all additional arguments will be forwarded to the constructor of the decoder
          that will be returned by this method

        OUTPUT: a decoder object

        Besides creating the decoder and returning it, this method also stores
        the decoder in a cache. With this behaviour, each decoder will be created
        at most one time for ``self``.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: C.decoder()
            Syndrome decoder for [7, 4] linear code over GF(2) handling errors of weight up to 1

        If there is no decoder for the code, we return an error::

            sage: from sage.coding.abstract_code import AbstractCode
            sage: class MyCodeFamily(AbstractCode):
            ....:   def __init__(self, length, field):
            ....:       sage.coding.abstract_code.AbstractCode.__init__(self, length)
            ....:       Parent.__init__(self, base=field, facade=False, category=Sets())
            ....:       self._field = field
            ....:   def field(self):
            ....:       return self._field
            ....:   def _repr_(self):
            ....:       return "%d dummy code over GF(%s)" % (self.length(), self.field().cardinality())
            sage: D = MyCodeFamily(5, GF(2))
            sage: D.decoder()
            Traceback (most recent call last):
            ...
            NotImplementedError: No decoder implemented for this code.

        If the name of a decoder which is not known by ``self`` is passed,
        an exception will be raised::

            sage: sorted(C.decoders_available())
            [\'InformationSet\', \'NearestNeighbor\', \'Syndrome\']
            sage: C.decoder(\'Try\')
            Traceback (most recent call last):
            ...
            ValueError: There is no Decoder named \'Try\'.
            The known Decoders are: [\'InformationSet\', \'NearestNeighbor\', \'Syndrome\']

        Some decoders take extra arguments. If the user forgets to supply these,
        the error message attempts to be helpful::

            sage: C.decoder(\'InformationSet\')
            Traceback (most recent call last):
            ...
            ValueError: Constructing the InformationSet decoder failed,
            possibly due to missing or incorrect parameters.
            The constructor requires the arguments [\'number_errors\'].
            It takes the optional arguments [\'algorithm\'].
            It accepts unspecified arguments as well. See the documentation of
            sage.coding.information_set_decoder.LinearCodeInformationSetDecoder
            for more details.
        '''
    def decoders_available(self, classes: bool = False):
        """
        Return a list of the available decoders' names for ``self``.

        INPUT:

        - ``classes`` -- boolean (default: ``False``); if ``classes`` is set to
          ``True``, return instead a :class:`dict` mapping available decoder
          name to the associated decoder class

        OUTPUT: list of strings, or a :class:`dict` mapping strings to classes

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: C.decoders_available()
            ['InformationSet', 'NearestNeighbor', 'Syndrome']

            sage: dictionary = C.decoders_available(True)
            sage: sorted(dictionary.keys())
            ['InformationSet', 'NearestNeighbor', 'Syndrome']
            sage: dictionary['NearestNeighbor']
            <class 'sage.coding.linear_code.LinearCodeNearestNeighborDecoder'>
        """
    def encode(self, word, encoder_name=None, *args, **kwargs):
        """
        Transform an element of a message space into a codeword.

        INPUT:

        - ``word`` -- an element of a message space of the code

        - ``encoder_name`` -- (default: ``None``) name of the encoder which
          will be used to encode ``word``. The default encoder of ``self`` will
          be used if default value is kept.

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to the
          construction of the encoder that is used

        One can use the following shortcut to encode a word ::

            C(word)

        OUTPUT: a vector of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: word = vector((0, 1, 1, 0))
            sage: C.encode(word)
            (1, 1, 0, 0, 1, 1, 0)
            sage: C(word)
            (1, 1, 0, 0, 1, 1, 0)

        It is possible to manually choose the encoder amongst the list of the available ones::

            sage: sorted(C.encoders_available())
            ['GeneratorMatrix', 'Systematic']
            sage: word = vector((0, 1, 1, 0))
            sage: C.encode(word, 'GeneratorMatrix')
            (1, 1, 0, 0, 1, 1, 0)
        """
    @cached_method
    def encoder(self, encoder_name=None, *args, **kwargs):
        '''
        Return an encoder of ``self``.

        The returned encoder provided by this method is cached.

        This methods creates a new instance of the encoder subclass designated by ``encoder_name``.
        While it is also possible to do the same by directly calling the subclass\' constructor,
        it is strongly advised to use this method to take advantage of the caching mechanism.

        INPUT:

        - ``encoder_name`` -- (default: ``None``) name of the encoder which will be
          returned. The default encoder of ``self`` will be used if
          default value is kept.

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to the
          constructor of the encoder this method will return

        OUTPUT: an Encoder object

        .. NOTE::

            The default encoder always has `F^{k}` as message space, with `k` the dimension
            of ``self`` and `F` the base ring of ``self``.

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: C.encoder()
            Generator matrix-based encoder for [7, 4] linear code over GF(2)

        If there is no encoder for the code, we return an error::

            sage: from sage.coding.abstract_code import AbstractCode
            sage: class MyCodeFamily(AbstractCode):
            ....:   def __init__(self, length, field):
            ....:       sage.coding.abstract_code.AbstractCode.__init__(self, length)
            ....:       Parent.__init__(self, base=field, facade=False, category=Sets())
            ....:       self._field = field
            ....:   def field(self):
            ....:       return self._field
            ....:   def _repr_(self):
            ....:       return "%d dummy code over GF(%s)" % (self.length(),
            ....:                                             self.field().cardinality())
            sage: D = MyCodeFamily(5, GF(2))
            sage: D.encoder()
            Traceback (most recent call last):
            ...
            NotImplementedError: No encoder implemented for this code.

        We check that the returned encoder is cached::

            sage: C.encoder.is_in_cache()
            True

        If the name of an encoder which is not known by ``self`` is passed,
        an exception will be raised::

            sage: sorted(C.encoders_available())
            [\'GeneratorMatrix\', \'Systematic\']
            sage: C.encoder(\'NonExistingEncoder\')
            Traceback (most recent call last):
            ...
            ValueError: There is no Encoder named \'NonExistingEncoder\'.
            The known Encoders are: [\'GeneratorMatrix\', \'Systematic\']

        Some encoders take extra arguments. If the user incorrectly supplies
        these, the error message attempts to be helpful::

            sage: C.encoder(\'Systematic\', strange_parameter=True)
            Traceback (most recent call last):
            ...
            ValueError: Constructing the Systematic encoder failed,
            possibly due to missing or incorrect parameters.
            The constructor requires no arguments. It takes the optional
            arguments [\'systematic_positions\']. See the documentation of
            sage.coding.linear_code_no_metric.LinearCodeSystematicEncoder
            for more details.
        '''
    def encoders_available(self, classes: bool = False):
        """
        Return a list of the available encoders' names for ``self``.

        INPUT:

        - ``classes`` -- boolean (default: ``False``); if ``classes`` is set to
          ``True``, return instead a :class:`dict` mapping available encoder
          name to the associated encoder class

        OUTPUT: list of strings, or a :class:`dict` mapping strings to classes

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: C.encoders_available()
            ['GeneratorMatrix', 'Systematic']
            sage: dictionary = C.encoders_available(True)
            sage: sorted(dictionary.items())
            [('GeneratorMatrix', <class 'sage.coding.linear_code.LinearCodeGeneratorMatrixEncoder'>),
             ('Systematic', <class 'sage.coding.linear_code_no_metric.LinearCodeSystematicEncoder'>)]
        """
    def unencode(self, c, encoder_name=None, nocheck: bool = False, **kwargs):
        """
        Return the message corresponding to ``c``.

        This is the inverse of :meth:`encode`.

        INPUT:

        - ``c`` -- a codeword of ``self``

        - ``encoder_name`` -- (default: ``None``) name of the decoder which will be used
          to decode ``word``. The default decoder of ``self`` will be used if
          default value is kept.

        - ``nocheck`` -- boolean (default: ``False``); checks if ``c`` is in
          ``self``. You might set this to ``True`` to disable the check for
          saving computation. Note that if ``c`` is not in ``self`` and
          ``nocheck = True``, then the output of :meth:`unencode` is not
          defined (except that it will be in the message space of ``self``).

        - ``kwargs`` -- all additional arguments are forwarded to the construction of the
          encoder that is used

        OUTPUT: an element of the message space of ``encoder_name`` of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(2), [[1,1,1,0,0,0,0], [1,0,0,1,1,0,0],
            ....:                    [0,1,0,1,0,1,0], [1,1,0,1,0,0,1]])
            sage: C = LinearCode(G)
            sage: c = vector(GF(2), (1, 1, 0, 0, 1, 1, 0))
            sage: C.unencode(c)
            (0, 1, 1, 0)
        """
    def random_element(self, *args, **kwds):
        """
        Return a random codeword; passes other positional and keyword
        arguments to ``random_element()`` method of vector space.

        OUTPUT: random element of the vector space of this code

        EXAMPLES::

            sage: C = codes.HammingCode(GF(4,'a'), 3)
            sage: C.random_element() # random test
            (1, 0, 0, a + 1, 1, a, a, a + 1, a + 1, 1, 1, 0, a + 1, a, 0, a, a, 0, a, a, 1)

        Passes extra positional or keyword arguments through::

            sage: C.random_element(prob=.5, distribution='1/n') # random test
            (1, 0, a, 0, 0, 0, 0, a + 1, 0, 0, 0, 0, 0, 0, 0, 0, a + 1, a + 1, 1, 0, 0)

        TESTS:

        Test that the codeword returned is immutable (see :issue:`16469`)::

            sage: c = C.random_element()
            sage: c.is_immutable()
            True

        Test that codeword returned has the same parent as any non-random codeword
        (see :issue:`19653`)::

            sage: C = codes.random_linear_code(GF(16, 'a'), 10, 4)
            sage: c1 = C.random_element()
            sage: c2 = C[1]
            sage: c1.parent() == c2.parent()
            True
        """
